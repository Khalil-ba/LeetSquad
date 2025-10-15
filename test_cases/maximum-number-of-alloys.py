def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,budget = 15,composition = [[1, 1, 1], [1, 1, 10]],stock = [0, 0, 0],cost = [1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,budget = 15,composition = [[1, 1, 1], [1, 1, 10]],stock = [0, 0, 0],cost = [1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1,budget = 100,composition = [[5]],stock = [0],cost = [20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1,budget = 100,composition = [[5]],stock = [0],cost = [20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2,budget = 20,composition = [[1, 2], [2, 1]],stock = [10, 10],cost = [1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2,budget = 20,composition = [[1, 2], [2, 1]],stock = [10, 10],cost = [1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,budget = 15,composition = [[1, 1, 1], [1, 1, 10]],stock = [0, 0, 100],cost = [1, 2, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,budget = 15,composition = [[1, 1, 1], [1, 1, 10]],stock = [0, 0, 100],cost = [1, 2, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3,budget = 10,composition = [[2, 1], [1, 2], [1, 1]],stock = [1, 1],cost = [5, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3,budget = 10,composition = [[2, 1], [1, 2], [1, 1]],stock = [1, 1],cost = [5, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 4,budget = 200,composition = [[1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2], [1, 3, 5, 7, 9, 11]],stock = [5, 10, 15, 20, 25, 30],cost = [1, 2, 3, 4, 5, 6]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 4,budget = 200,composition = [[1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2], [1, 3, 5, 7, 9, 11]],stock = [5, 10, 15, 20, 25, 30],cost = [1, 2, 3, 4, 5, 6]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 4,budget = 200,composition = [[1, 1], [2, 2], [3, 3], [4, 4]],stock = [10, 10],cost = [1, 2]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 4,budget = 200,composition = [[1, 1], [2, 2], [3, 3], [4, 4]],stock = [10, 10],cost = [1, 2]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,budget = 250,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]],stock = [0, 0, 0, 0, 0],cost = [1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,budget = 250,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]],stock = [0, 0, 0, 0, 0],cost = [1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 4,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 4,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 100,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2, 2]],stock = [5, 5, 5, 5],cost = [1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 100,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2, 2]],stock = [5, 5, 5, 5],cost = [1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,budget = 1000,composition = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],stock = [100, 100, 100, 100, 100],cost = [1, 1, 1, 1, 1]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,budget = 1000,composition = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],stock = [100, 100, 100, 100, 100],cost = [1, 1, 1, 1, 1]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3,budget = 150,composition = [[1, 1], [2, 1], [1, 2]],stock = [50, 50],cost = [10, 20]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3,budget = 150,composition = [[1, 1], [2, 1], [1, 2]],stock = [50, 50],cost = [10, 20]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 500,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 3, 4]],stock = [10, 10, 10, 10],cost = [10, 20, 30, 40]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 500,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 3, 4]],stock = [10, 10, 10, 10],cost = [10, 20, 30, 40]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 2,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10]],stock = [5, 5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 2,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10]],stock = [5, 5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5,budget = 500,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [0, 0, 0],cost = [1, 2, 3]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5,budget = 500,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [0, 0, 0],cost = [1, 2, 3]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 350,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [50, 50, 50, 50],cost = [1, 2, 3, 4]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 350,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [50, 50, 50, 50],cost = [1, 2, 3, 4]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [10, 1, 1], [1, 10, 1]],stock = [100, 100, 100],cost = [1, 10, 100]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [10, 1, 1], [1, 10, 1]],stock = [100, 100, 100],cost = [1, 10, 100]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 200,composition = [[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],stock = [20, 20, 20, 20],cost = [1, 2, 3, 4]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 200,composition = [[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],stock = [20, 20, 20, 20],cost = [1, 2, 3, 4]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,budget = 50,composition = [[1, 2, 3], [3, 2, 1]],stock = [10, 20, 30],cost = [1, 2, 3]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,budget = 50,composition = [[1, 2, 3], [3, 2, 1]],stock = [10, 20, 30],cost = [1, 2, 3]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 1000,composition = [[10, 20, 30], [20, 30, 40], [30, 40, 50]],stock = [0, 0, 0],cost = [1, 2, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 1000,composition = [[10, 20, 30], [20, 30, 40], [30, 40, 50]],stock = [0, 0, 0],cost = [1, 2, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 50,composition = [[2, 1, 3, 1], [1, 2, 1, 2], [3, 3, 3, 3]],stock = [10, 5, 0, 0],cost = [5, 3, 2, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 50,composition = [[2, 1, 3, 1], [1, 2, 1, 2], [3, 3, 3, 3]],stock = [10, 5, 0, 0],cost = [5, 3, 2, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3,budget = 250,composition = [[10, 1], [1, 10], [5, 5]],stock = [100, 100],cost = [1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3,budget = 250,composition = [[10, 1], [1, 10], [5, 5]],stock = [100, 100],cost = [1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,budget = 500,composition = [[2, 3, 1, 4, 5], [1, 1, 1, 1, 1], [5, 5, 5, 5, 5]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,budget = 500,composition = [[2, 3, 1, 4, 5], [1, 1, 1, 1, 1], [5, 5, 5, 5, 5]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 1,budget = 50,composition = [[10, 10, 10]],stock = [5, 5, 5],cost = [1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1,budget = 50,composition = [[10, 10, 10]],stock = [5, 5, 5],cost = [1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 300,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stock = [50, 50, 50, 50],cost = [1, 2, 3, 4]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 300,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stock = [50, 50, 50, 50],cost = [1, 2, 3, 4]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 100,composition = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]],stock = [5, 5, 5, 5],cost = [2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 100,composition = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]],stock = [5, 5, 5, 5],cost = [2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4,budget = 100,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [10, 10, 10, 10, 10]],stock = [5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4,budget = 100,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [10, 10, 10, 10, 10]],stock = [5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 150,composition = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],stock = [50, 0, 0, 0],cost = [1, 10, 10, 10]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 150,composition = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],stock = [50, 0, 0, 0],cost = [1, 10, 10, 10]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 2,budget = 300,composition = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 2,budget = 300,composition = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,budget = 300,composition = [[1, 1, 1], [2, 2, 2]],stock = [0, 0, 0],cost = [100, 50, 25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,budget = 300,composition = [[1, 1, 1], [2, 2, 2]],stock = [0, 0, 0],cost = [100, 50, 25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 800,composition = [[1, 1, 1, 1], [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1]],stock = [10, 20, 30, 40],cost = [5, 10, 15, 20]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 800,composition = [[1, 1, 1, 1], [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1]],stock = [10, 20, 30, 40],cost = [5, 10, 15, 20]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3,budget = 1500,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [3, 3, 3, 3, 3, 3, 3]],stock = [50, 60, 70, 80, 90, 100, 110],cost = [1, 2, 3, 4, 5, 6, 7]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3,budget = 1500,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [3, 3, 3, 3, 3, 3, 3]],stock = [50, 60, 70, 80, 90, 100, 110],cost = [1, 2, 3, 4, 5, 6, 7]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,budget = 1000,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],stock = [500, 500, 500, 500, 500],cost = [1, 1, 1, 1, 1]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,budget = 1000,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],stock = [500, 500, 500, 500, 500],cost = [1, 1, 1, 1, 1]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 200,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [0, 0, 0, 0],cost = [5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 200,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [0, 0, 0, 0],cost = [5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 4,budget = 300,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2]],stock = [20, 30, 40],cost = [5, 10, 15]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 4,budget = 300,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2]],stock = [20, 30, 40],cost = [5, 10, 15]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 200,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],stock = [0, 0, 0, 100],cost = [10, 20, 30, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 200,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],stock = [0, 0, 0, 100],cost = [10, 20, 30, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3,budget = 10000,composition = [[100, 1], [1, 100], [50, 50]],stock = [5000, 5000],cost = [1, 1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3,budget = 10000,composition = [[100, 1], [1, 100], [50, 50]],stock = [5000, 5000],cost = [1, 1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 2,budget = 3000,composition = [[1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10]],stock = [5, 10, 15, 20, 25, 30],cost = [1, 2, 3, 4, 5, 6]) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 2,budget = 3000,composition = [[1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10]],stock = [5, 10, 15, 20, 25, 30],cost = [1, 2, 3, 4, 5, 6]) == 164: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 100,composition = [[2, 3, 1, 4], [1, 1, 1, 1], [5, 5, 5, 5]],stock = [10, 10, 10, 10],cost = [1, 2, 3, 4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 100,composition = [[2, 3, 1, 4], [1, 1, 1, 1], [5, 5, 5, 5]],stock = [10, 10, 10, 10],cost = [1, 2, 3, 4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2,budget = 1000,composition = [[1, 1, 1, 1], [99, 99, 99, 99]],stock = [100, 100, 100, 100],cost = [1, 1, 1, 1]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2,budget = 1000,composition = [[1, 1, 1, 1], [99, 99, 99, 99]],stock = [100, 100, 100, 100],cost = [1, 1, 1, 1]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 2,budget = 5000,composition = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],stock = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 2,budget = 5000,composition = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],stock = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3,budget = 2500,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [2, 3, 2, 3, 2, 3, 2]],stock = [50, 50, 50, 50, 50, 50, 50],cost = [1, 1, 1, 1, 1, 1, 1]) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3,budget = 2500,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [2, 3, 2, 3, 2, 3, 2]],stock = [50, 50, 50, 50, 50, 50, 50],cost = [1, 1, 1, 1, 1, 1, 1]) == 167: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3,budget = 1000,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13]],stock = [100, 200, 300, 400, 500, 600, 700],cost = [1, 2, 3, 4, 5, 6, 7]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3,budget = 1000,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13]],stock = [100, 200, 300, 400, 500, 600, 700],cost = [1, 2, 3, 4, 5, 6, 7]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,budget = 500,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 2, 2, 2, 2]],stock = [10, 20, 30, 40, 50],cost = [5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,budget = 500,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 2, 2, 2, 2]],stock = [10, 20, 30, 40, 50],cost = [5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5,budget = 200,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [10, 10, 10],cost = [10, 20, 30]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5,budget = 200,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [10, 10, 10],cost = [10, 20, 30]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 2,budget = 250,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],stock = [0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 2,budget = 250,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],stock = [0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3,budget = 50,composition = [[1, 1], [2, 2], [3, 3]],stock = [20, 20],cost = [1, 2]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3,budget = 50,composition = [[1, 1], [2, 2], [3, 3]],stock = [20, 20],cost = [1, 2]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 5,budget = 1000,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 5,budget = 1000,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 4,budget = 500,composition = [[1, 1], [1, 2], [2, 1], [2, 2]],stock = [100, 100],cost = [1, 1]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 4,budget = 500,composition = [[1, 1], [1, 2], [2, 1], [2, 2]],stock = [100, 100],cost = [1, 1]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [1, 0, 1], [0, 1, 1]],stock = [10, 10, 10],cost = [1, 1, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [1, 0, 1], [0, 1, 1]],stock = [10, 10, 10],cost = [1, 1, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [10, 10, 10], [5, 5, 5]],stock = [100, 100, 100],cost = [1, 2, 3]) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [10, 10, 10], [5, 5, 5]],stock = [100, 100, 100],cost = [1, 2, 3]) == 133: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 5,budget = 500,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],stock = [50, 50, 50, 50],cost = [10, 20, 30, 40]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 5,budget = 500,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],stock = [50, 50, 50, 50],cost = [10, 20, 30, 40]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 6,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 6,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2,budget = 200,composition = [[1, 2, 3, 4], [4, 3, 2, 1]],stock = [0, 0, 0, 0],cost = [10, 20, 30, 40]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2,budget = 200,composition = [[1, 2, 3, 4], [4, 3, 2, 1]],stock = [0, 0, 0, 0],cost = [10, 20, 30, 40]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,budget = 1000,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 2, 1, 2]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,budget = 1000,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 2, 1, 2]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,budget = 2000,composition = [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 10, 10, 10, 10], [2, 3, 4, 5, 6]],stock = [0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5]) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,budget = 2000,composition = [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 10, 10, 10, 10], [2, 3, 4, 5, 6]],stock = [0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5]) == 133: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,budget = 50,composition = [[1, 1, 1], [1, 2, 3]],stock = [10, 10, 10],cost = [1, 1, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,budget = 50,composition = [[1, 1, 1], [1, 2, 3]],stock = [10, 10, 10],cost = [1, 1, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 2,budget = 800,composition = [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10]],stock = [100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 2,budget = 800,composition = [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10]],stock = [100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 100,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1]],stock = [10, 10, 10],cost = [10, 10, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 100,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1]],stock = [10, 10, 10],cost = [10, 10, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,budget = 100,composition = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],stock = [10, 10, 10, 10, 10],cost = [10, 10, 10, 10, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,budget = 100,composition = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],stock = [10, 10, 10, 10, 10],cost = [10, 10, 10, 10, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5,budget = 300,composition = [[1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [3, 3, 3]],stock = [0, 0, 0],cost = [10, 20, 30]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5,budget = 300,composition = [[1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [3, 3, 3]],stock = [0, 0, 0],cost = [10, 20, 30]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 450,composition = [[3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [0, 0, 0],cost = [5, 10, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 450,composition = [[3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [0, 0, 0],cost = [5, 10, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 2,budget = 200,composition = [[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0]],stock = [10, 20, 30, 40, 50, 60],cost = [1, 2, 3, 4, 5, 6]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 2,budget = 200,composition = [[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0]],stock = [10, 20, 30, 40, 50, 60],cost = [1, 2, 3, 4, 5, 6]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 3,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3]],stock = [10, 10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5, 6]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 3,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3]],stock = [10, 10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5, 6]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,budget = 1000,composition = [[2, 3, 1, 1, 2], [1, 2, 3, 4, 5], [3, 2, 1, 2, 1]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,budget = 1000,composition = [[2, 3, 1, 1, 2], [1, 2, 3, 4, 5], [3, 2, 1, 2, 1]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 5,budget = 50,composition = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 3]],stock = [5, 5],cost = [10, 20]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 5,budget = 50,composition = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 3]],stock = [5, 5],cost = [10, 20]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 1000,composition = [[2, 2, 2], [3, 3, 3], [1, 1, 1]],stock = [100, 200, 300],cost = [1, 1, 1]) == 533
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 1000,composition = [[2, 2, 2], [3, 3, 3], [1, 1, 1]],stock = [100, 200, 300],cost = [1, 1, 1]) == 533: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4,budget = 500,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 10, 10, 10, 10], [1, 1, 1, 1, 1]],stock = [50, 50, 50, 50, 50],cost = [5, 5, 5, 5, 5]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4,budget = 500,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 10, 10, 10, 10], [1, 1, 1, 1, 1]],stock = [50, 50, 50, 50, 50],cost = [5, 5, 5, 5, 5]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 50,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3]],stock = [15, 15, 15],cost = [1, 1, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 50,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3]],stock = [15, 15, 15],cost = [1, 1, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 5,budget = 300,composition = [[1, 1], [2, 1], [1, 2], [3, 1], [1, 3]],stock = [100, 100],cost = [50, 100]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 5,budget = 300,composition = [[1, 1], [2, 1], [1, 2], [3, 1], [1, 3]],stock = [100, 100],cost = [50, 100]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 6,budget = 600,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 6,budget = 600,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5,budget = 200,composition = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2]],stock = [10, 20, 30],cost = [1, 2, 3]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5,budget = 200,composition = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2]],stock = [10, 20, 30],cost = [1, 2, 3]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,budget = 500,composition = [[10, 20, 30], [30, 20, 10]],stock = [50, 50, 50],cost = [5, 10, 15]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,budget = 500,composition = [[10, 20, 30], [30, 20, 10]],stock = [50, 50, 50],cost = [5, 10, 15]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 100,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stock = [25, 25, 25, 25],cost = [1, 1, 1, 1]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 100,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stock = [25, 25, 25, 25],cost = [1, 1, 1, 1]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3,budget = 1000,composition = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3]],stock = [100, 100, 100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5, 6, 7]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3,budget = 1000,composition = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3]],stock = [100, 100, 100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5, 6, 7]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 1000,composition = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60], [40, 50, 60, 70]],stock = [0, 0, 0, 0],cost = [5, 4, 3, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 1000,composition = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60], [40, 50, 60, 70]],stock = [0, 0, 0, 0],cost = [5, 4, 3, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 1,budget = 200,composition = [[10, 20, 30, 40, 50]],stock = [5, 10, 15, 20, 25],cost = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 1,budget = 200,composition = [[10, 20, 30, 40, 50]],stock = [5, 10, 15, 20, 25],cost = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 2,budget = 50,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]],stock = [5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 2,budget = 50,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]],stock = [5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 2,budget = 1000,composition = [[10, 10, 10, 10, 10], [1, 1, 1, 1, 1]],stock = [100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5]) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 2,budget = 1000,composition = [[10, 10, 10, 10, 10], [1, 1, 1, 1, 1]],stock = [100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5]) == 166: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3,budget = 500,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1]],stock = [100, 100, 100, 100],cost = [1, 2, 3, 4]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3,budget = 500,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1]],stock = [100, 100, 100, 100],cost = [1, 2, 3, 4]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4,budget = 100,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 1, 5, 4], [3, 3, 3, 3, 3]],stock = [10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4,budget = 100,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 1, 5, 4], [3, 3, 3, 3, 3]],stock = [10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 500,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [100, 100, 100, 100],cost = [1, 2, 3, 4]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 500,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [100, 100, 100, 100],cost = [1, 2, 3, 4]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 2,budget = 3000,composition = [[1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10]],stock = [100, 100, 100, 100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8]) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 2,budget = 3000,composition = [[1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10]],stock = [100, 100, 100, 100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8]) == 183: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10,budget = 100000,composition = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],stock = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10,budget = 100000,composition = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],stock = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2818: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 5,budget = 50,composition = [[1, 1], [2, 1], [1, 2], [3, 1], [1, 3]],stock = [0, 0],cost = [5, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 5,budget = 50,composition = [[1, 1], [2, 1], [1, 2], [3, 1], [1, 3]],stock = [0, 0],cost = [5, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3,budget = 150,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1]],stock = [10, 20, 30],cost = [10, 20, 30]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3,budget = 150,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1]],stock = [10, 20, 30],cost = [10, 20, 30]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,budget = 200,composition = [[1, 1, 1, 1, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]],stock = [10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,budget = 200,composition = [[1, 1, 1, 1, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]],stock = [10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5,budget = 200,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [50, 50, 50],cost = [10, 20, 30]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5,budget = 200,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [50, 50, 50],cost = [10, 20, 30]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5,budget = 500,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [10, 10, 10],cost = [1, 1, 1]) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5,budget = 500,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [10, 10, 10],cost = [1, 1, 1]) == 176: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 5,budget = 1200,composition = [[1, 1, 1, 1], [2, 1, 1, 2], [1, 2, 2, 1], [2, 2, 1, 1], [1, 1, 2, 2]],stock = [50, 50, 50, 50],cost = [10, 20, 30, 40]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 5,budget = 1200,composition = [[1, 1, 1, 1], [2, 1, 1, 2], [1, 2, 2, 1], [2, 2, 1, 1], [1, 1, 2, 2]],stock = [50, 50, 50, 50],cost = [10, 20, 30, 40]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4,budget = 1000,composition = [[10, 20, 30, 40], [5, 15, 25, 35], [1, 1, 1, 1], [100, 50, 25, 10]],stock = [0, 0, 0, 0],cost = [1, 2, 3, 4]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4,budget = 1000,composition = [[10, 20, 30, 40], [5, 15, 25, 35], [1, 1, 1, 1], [100, 50, 25, 10]],stock = [0, 0, 0, 0],cost = [1, 2, 3, 4]) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3,k = 2,budget = 15,composition = [[1, 1, 1], [1, 1, 10]],stock = [0, 0, 0],cost = [1, 2, 3]) == 2
    assert candidate(n = 1,k = 1,budget = 100,composition = [[5]],stock = [0],cost = [20]) == 1
    assert candidate(n = 2,k = 2,budget = 20,composition = [[1, 2], [2, 1]],stock = [10, 10],cost = [1, 1]) == 13
    assert candidate(n = 3,k = 2,budget = 15,composition = [[1, 1, 1], [1, 1, 10]],stock = [0, 0, 100],cost = [1, 2, 3]) == 5
    assert candidate(n = 2,k = 3,budget = 10,composition = [[2, 1], [1, 2], [1, 1]],stock = [1, 1],cost = [5, 5]) == 2
    assert candidate(n = 6,k = 4,budget = 200,composition = [[1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2], [1, 3, 5, 7, 9, 11]],stock = [5, 10, 15, 20, 25, 30],cost = [1, 2, 3, 4, 5, 6]) == 31
    assert candidate(n = 2,k = 4,budget = 200,composition = [[1, 1], [2, 2], [3, 3], [4, 4]],stock = [10, 10],cost = [1, 2]) == 76
    assert candidate(n = 5,k = 3,budget = 250,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]],stock = [0, 0, 0, 0, 0],cost = [1, 1, 1, 1, 1]) == 50
    assert candidate(n = 6,k = 4,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 14
    assert candidate(n = 4,k = 3,budget = 100,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2, 2]],stock = [5, 5, 5, 5],cost = [1, 1, 1, 1]) == 15
    assert candidate(n = 5,k = 5,budget = 1000,composition = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],stock = [100, 100, 100, 100, 100],cost = [1, 1, 1, 1, 1]) == 1100
    assert candidate(n = 2,k = 3,budget = 150,composition = [[1, 1], [2, 1], [1, 2]],stock = [50, 50],cost = [10, 20]) == 55
    assert candidate(n = 4,k = 3,budget = 500,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 3, 4]],stock = [10, 10, 10, 10],cost = [10, 20, 30, 40]) == 15
    assert candidate(n = 6,k = 2,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10]],stock = [5, 5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1, 1]) == 55
    assert candidate(n = 3,k = 5,budget = 500,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [0, 0, 0],cost = [1, 2, 3]) == 83
    assert candidate(n = 4,k = 4,budget = 350,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [50, 50, 50, 50],cost = [1, 2, 3, 4]) == 85
    assert candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [10, 1, 1], [1, 10, 1]],stock = [100, 100, 100],cost = [1, 10, 100]) == 101
    assert candidate(n = 4,k = 4,budget = 200,composition = [[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],stock = [20, 20, 20, 20],cost = [1, 2, 3, 4]) == 60
    assert candidate(n = 3,k = 2,budget = 50,composition = [[1, 2, 3], [3, 2, 1]],stock = [10, 20, 30],cost = [1, 2, 3]) == 14
    assert candidate(n = 3,k = 3,budget = 1000,composition = [[10, 20, 30], [20, 30, 40], [30, 40, 50]],stock = [0, 0, 0],cost = [1, 2, 3]) == 7
    assert candidate(n = 4,k = 3,budget = 50,composition = [[2, 1, 3, 1], [1, 2, 1, 2], [3, 3, 3, 3]],stock = [10, 5, 0, 0],cost = [5, 3, 2, 4]) == 5
    assert candidate(n = 2,k = 3,budget = 250,composition = [[10, 1], [1, 10], [5, 5]],stock = [100, 100],cost = [1, 1]) == 45
    assert candidate(n = 5,k = 3,budget = 500,composition = [[2, 3, 1, 4, 5], [1, 1, 1, 1, 1], [5, 5, 5, 5, 5]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 70
    assert candidate(n = 3,k = 1,budget = 50,composition = [[10, 10, 10]],stock = [5, 5, 5],cost = [1, 1, 1]) == 2
    assert candidate(n = 4,k = 4,budget = 300,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stock = [50, 50, 50, 50],cost = [1, 2, 3, 4]) == 350
    assert candidate(n = 4,k = 3,budget = 100,composition = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]],stock = [5, 5, 5, 5],cost = [2, 3, 4, 5]) == 4
    assert candidate(n = 5,k = 4,budget = 100,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [10, 10, 10, 10, 10]],stock = [5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5]) == 11
    assert candidate(n = 4,k = 4,budget = 150,composition = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],stock = [50, 0, 0, 0],cost = [1, 10, 10, 10]) == 200
    assert candidate(n = 6,k = 2,budget = 300,composition = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 5
    assert candidate(n = 3,k = 2,budget = 300,composition = [[1, 1, 1], [2, 2, 2]],stock = [0, 0, 0],cost = [100, 50, 25]) == 1
    assert candidate(n = 4,k = 4,budget = 800,composition = [[1, 1, 1, 1], [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1]],stock = [10, 20, 30, 40],cost = [5, 10, 15, 20]) == 46
    assert candidate(n = 7,k = 3,budget = 1500,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [3, 3, 3, 3, 3, 3, 3]],stock = [50, 60, 70, 80, 90, 100, 110],cost = [1, 2, 3, 4, 5, 6, 7]) == 47
    assert candidate(n = 5,k = 5,budget = 1000,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],stock = [500, 500, 500, 500, 500],cost = [1, 1, 1, 1, 1]) == 700
    assert candidate(n = 4,k = 4,budget = 200,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [0, 0, 0, 0],cost = [5, 5, 5, 5]) == 10
    assert candidate(n = 3,k = 4,budget = 300,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2]],stock = [20, 30, 40],cost = [5, 10, 15]) == 20
    assert candidate(n = 4,k = 3,budget = 200,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],stock = [0, 0, 0, 100],cost = [10, 20, 30, 40]) == 20
    assert candidate(n = 2,k = 3,budget = 10000,composition = [[100, 1], [1, 100], [50, 50]],stock = [5000, 5000],cost = [1, 1]) == 200
    assert candidate(n = 6,k = 2,budget = 3000,composition = [[1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10]],stock = [5, 10, 15, 20, 25, 30],cost = [1, 2, 3, 4, 5, 6]) == 164
    assert candidate(n = 4,k = 3,budget = 100,composition = [[2, 3, 1, 4], [1, 1, 1, 1], [5, 5, 5, 5]],stock = [10, 10, 10, 10],cost = [1, 2, 3, 4]) == 20
    assert candidate(n = 4,k = 2,budget = 1000,composition = [[1, 1, 1, 1], [99, 99, 99, 99]],stock = [100, 100, 100, 100],cost = [1, 1, 1, 1]) == 350
    assert candidate(n = 10,k = 2,budget = 5000,composition = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],stock = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 90
    assert candidate(n = 7,k = 3,budget = 2500,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [2, 3, 2, 3, 2, 3, 2]],stock = [50, 50, 50, 50, 50, 50, 50],cost = [1, 1, 1, 1, 1, 1, 1]) == 167
    assert candidate(n = 7,k = 3,budget = 1000,composition = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13]],stock = [100, 200, 300, 400, 500, 600, 700],cost = [1, 2, 3, 4, 5, 6, 7]) == 107
    assert candidate(n = 5,k = 3,budget = 500,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 2, 2, 2, 2]],stock = [10, 20, 30, 40, 50],cost = [5, 4, 3, 2, 1]) == 28
    assert candidate(n = 3,k = 5,budget = 200,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [10, 10, 10],cost = [10, 20, 30]) == 13
    assert candidate(n = 5,k = 2,budget = 250,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],stock = [0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5]) == 7
    assert candidate(n = 2,k = 3,budget = 50,composition = [[1, 1], [2, 2], [3, 3]],stock = [20, 20],cost = [1, 2]) == 36
    assert candidate(n = 6,k = 5,budget = 1000,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 47
    assert candidate(n = 2,k = 4,budget = 500,composition = [[1, 1], [1, 2], [2, 1], [2, 2]],stock = [100, 100],cost = [1, 1]) == 350
    assert candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [1, 0, 1], [0, 1, 1]],stock = [10, 10, 10],cost = [1, 1, 1]) == 110
    assert candidate(n = 3,k = 3,budget = 200,composition = [[1, 1, 1], [10, 10, 10], [5, 5, 5]],stock = [100, 100, 100],cost = [1, 2, 3]) == 133
    assert candidate(n = 4,k = 5,budget = 500,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],stock = [50, 50, 50, 50],cost = [10, 20, 30, 40]) == 55
    assert candidate(n = 6,k = 6,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 14
    assert candidate(n = 4,k = 2,budget = 200,composition = [[1, 2, 3, 4], [4, 3, 2, 1]],stock = [0, 0, 0, 0],cost = [10, 20, 30, 40]) == 1
    assert candidate(n = 5,k = 3,budget = 1000,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 2, 1, 2]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 55
    assert candidate(n = 5,k = 5,budget = 2000,composition = [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 10, 10, 10, 10], [2, 3, 4, 5, 6]],stock = [0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5]) == 133
    assert candidate(n = 3,k = 2,budget = 50,composition = [[1, 1, 1], [1, 2, 3]],stock = [10, 10, 10],cost = [1, 1, 1]) == 26
    assert candidate(n = 5,k = 2,budget = 800,composition = [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10]],stock = [100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5]) == 6
    assert candidate(n = 3,k = 3,budget = 100,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1]],stock = [10, 10, 10],cost = [10, 10, 10]) == 6
    assert candidate(n = 5,k = 5,budget = 100,composition = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],stock = [10, 10, 10, 10, 10],cost = [10, 10, 10, 10, 10]) == 20
    assert candidate(n = 3,k = 5,budget = 300,composition = [[1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [3, 3, 3]],stock = [0, 0, 0],cost = [10, 20, 30]) == 5
    assert candidate(n = 3,k = 3,budget = 450,composition = [[3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [0, 0, 0],cost = [5, 10, 15]) == 5
    assert candidate(n = 6,k = 2,budget = 200,composition = [[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0]],stock = [10, 20, 30, 40, 50, 60],cost = [1, 2, 3, 4, 5, 6]) == 81
    assert candidate(n = 6,k = 3,budget = 300,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3]],stock = [10, 10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5, 6]) == 24
    assert candidate(n = 5,k = 3,budget = 1000,composition = [[2, 3, 1, 1, 2], [1, 2, 3, 4, 5], [3, 2, 1, 2, 1]],stock = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 67
    assert candidate(n = 2,k = 5,budget = 50,composition = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 3]],stock = [5, 5],cost = [10, 20]) == 6
    assert candidate(n = 3,k = 3,budget = 1000,composition = [[2, 2, 2], [3, 3, 3], [1, 1, 1]],stock = [100, 200, 300],cost = [1, 1, 1]) == 533
    assert candidate(n = 5,k = 4,budget = 500,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 10, 10, 10, 10], [1, 1, 1, 1, 1]],stock = [50, 50, 50, 50, 50],cost = [5, 5, 5, 5, 5]) == 70
    assert candidate(n = 3,k = 3,budget = 50,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3]],stock = [15, 15, 15],cost = [1, 1, 1]) == 31
    assert candidate(n = 2,k = 5,budget = 300,composition = [[1, 1], [2, 1], [1, 2], [3, 1], [1, 3]],stock = [100, 100],cost = [50, 100]) == 102
    assert candidate(n = 6,k = 6,budget = 600,composition = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]],stock = [0, 0, 0, 0, 0, 0],cost = [1, 2, 3, 4, 5, 6]) == 28
    assert candidate(n = 3,k = 5,budget = 200,composition = [[1, 2, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2]],stock = [10, 20, 30],cost = [1, 2, 3]) == 34
    assert candidate(n = 3,k = 2,budget = 500,composition = [[10, 20, 30], [30, 20, 10]],stock = [50, 50, 50],cost = [5, 10, 15]) == 3
    assert candidate(n = 4,k = 4,budget = 100,composition = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stock = [25, 25, 25, 25],cost = [1, 1, 1, 1]) == 125
    assert candidate(n = 7,k = 3,budget = 1000,composition = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3]],stock = [100, 100, 100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5, 6, 7]) == 135
    assert candidate(n = 4,k = 4,budget = 1000,composition = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60], [40, 50, 60, 70]],stock = [0, 0, 0, 0],cost = [5, 4, 3, 2]) == 3
    assert candidate(n = 5,k = 1,budget = 200,composition = [[10, 20, 30, 40, 50]],stock = [5, 10, 15, 20, 25],cost = [1, 2, 3, 4, 5]) == 0
    assert candidate(n = 5,k = 2,budget = 50,composition = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]],stock = [5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1]) == 15
    assert candidate(n = 5,k = 2,budget = 1000,composition = [[10, 10, 10, 10, 10], [1, 1, 1, 1, 1]],stock = [100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5]) == 166
    assert candidate(n = 4,k = 3,budget = 500,composition = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1]],stock = [100, 100, 100, 100],cost = [1, 2, 3, 4]) == 68
    assert candidate(n = 5,k = 4,budget = 100,composition = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 1, 5, 4], [3, 3, 3, 3, 3]],stock = [10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5]) == 6
    assert candidate(n = 4,k = 4,budget = 500,composition = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],stock = [100, 100, 100, 100],cost = [1, 2, 3, 4]) == 150
    assert candidate(n = 8,k = 2,budget = 3000,composition = [[1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10]],stock = [100, 100, 100, 100, 100, 100, 100, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8]) == 183
    assert candidate(n = 10,k = 10,budget = 100000,composition = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],stock = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2818
    assert candidate(n = 2,k = 5,budget = 50,composition = [[1, 1], [2, 1], [1, 2], [3, 1], [1, 3]],stock = [0, 0],cost = [5, 10]) == 3
    assert candidate(n = 3,k = 3,budget = 150,composition = [[1, 2, 3], [3, 2, 1], [2, 3, 1]],stock = [10, 20, 30],cost = [10, 20, 30]) == 11
    assert candidate(n = 5,k = 5,budget = 200,composition = [[1, 1, 1, 1, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]],stock = [10, 10, 10, 10, 10],cost = [1, 2, 3, 4, 5]) == 23
    assert candidate(n = 3,k = 5,budget = 200,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [50, 50, 50],cost = [10, 20, 30]) == 53
    assert candidate(n = 3,k = 5,budget = 500,composition = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],stock = [10, 10, 10],cost = [1, 1, 1]) == 176
    assert candidate(n = 4,k = 5,budget = 1200,composition = [[1, 1, 1, 1], [2, 1, 1, 2], [1, 2, 2, 1], [2, 2, 1, 1], [1, 1, 2, 2]],stock = [50, 50, 50, 50],cost = [10, 20, 30, 40]) == 62
    assert candidate(n = 4,k = 4,budget = 1000,composition = [[10, 20, 30, 40], [5, 15, 25, 35], [1, 1, 1, 1], [100, 50, 25, 10]],stock = [0, 0, 0, 0],cost = [1, 2, 3, 4]) == 100


