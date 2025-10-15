def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4]],portsCount = 4,maxBoxes = 2,maxWeight = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4]],portsCount = 4,maxBoxes = 2,maxWeight = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 2], [2, 2], [1, 2], [2, 2], [1, 2]],portsCount = 2,maxBoxes = 3,maxWeight = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 2], [2, 2], [1, 2], [2, 2], [1, 2]],portsCount = 2,maxBoxes = 3,maxWeight = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 1,maxWeight = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 1,maxWeight = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [1, 5], [1, 5], [2, 5], [2, 5], [2, 5]],portsCount = 2,maxBoxes = 2,maxWeight = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [1, 5], [1, 5], [2, 5], [2, 5], [2, 5]],portsCount = 2,maxBoxes = 2,maxWeight = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5]],portsCount = 2,maxBoxes = 2,maxWeight = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5]],portsCount = 2,maxBoxes = 2,maxWeight = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1]],portsCount = 15,maxBoxes = 5,maxWeight = 15) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1]],portsCount = 15,maxBoxes = 5,maxWeight = 15) == 18: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2]],portsCount = 2,maxBoxes = 4,maxWeight = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2]],portsCount = 2,maxBoxes = 4,maxWeight = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 1], [1, 1]],portsCount = 2,maxBoxes = 3,maxWeight = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 1], [1, 1]],portsCount = 2,maxBoxes = 3,maxWeight = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100]],portsCount = 5,maxBoxes = 5,maxWeight = 500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100]],portsCount = 5,maxBoxes = 5,maxWeight = 500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3]],portsCount = 5,maxBoxes = 3,maxWeight = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3]],portsCount = 5,maxBoxes = 3,maxWeight = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 3,maxWeight = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 3,maxWeight = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],portsCount = 9,maxBoxes = 3,maxWeight = 15) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],portsCount = 9,maxBoxes = 3,maxWeight = 15) == 13: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 3], [3, 2], [2, 1], [1, 4]],portsCount = 3,maxBoxes = 5,maxWeight = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 3], [3, 2], [2, 1], [1, 4]],portsCount = 3,maxBoxes = 5,maxWeight = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 2,maxWeight = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 2,maxWeight = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 3,maxWeight = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 3,maxWeight = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]],portsCount = 3,maxBoxes = 6,maxWeight = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]],portsCount = 3,maxBoxes = 6,maxWeight = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],portsCount = 5,maxBoxes = 3,maxWeight = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],portsCount = 5,maxBoxes = 3,maxWeight = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],portsCount = 10,maxBoxes = 10,maxWeight = 55) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],portsCount = 10,maxBoxes = 10,maxWeight = 55) == 11: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10]],portsCount = 3,maxBoxes = 2,maxWeight = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10]],portsCount = 3,maxBoxes = 2,maxWeight = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],portsCount = 1,maxBoxes = 3,maxWeight = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],portsCount = 1,maxBoxes = 3,maxWeight = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 5], [3, 7], [4, 9]],portsCount = 4,maxBoxes = 2,maxWeight = 12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 5], [3, 7], [4, 9]],portsCount = 4,maxBoxes = 2,maxWeight = 12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],portsCount = 5,maxBoxes = 2,maxWeight = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],portsCount = 5,maxBoxes = 2,maxWeight = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 2], [3, 3], [1, 1]],portsCount = 3,maxBoxes = 3,maxWeight = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 2], [3, 3], [1, 1]],portsCount = 3,maxBoxes = 3,maxWeight = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]],portsCount = 10,maxBoxes = 10,maxWeight = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]],portsCount = 10,maxBoxes = 10,maxWeight = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 2], [3, 1]],portsCount = 3,maxBoxes = 5,maxWeight = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 2], [3, 1]],portsCount = 3,maxBoxes = 5,maxWeight = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 1,maxWeight = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 1,maxWeight = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 2], [1, 4], [2, 2], [3, 1]],portsCount = 3,maxBoxes = 3,maxWeight = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 2], [1, 4], [2, 2], [3, 1]],portsCount = 3,maxBoxes = 3,maxWeight = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],portsCount = 1,maxBoxes = 5,maxWeight = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],portsCount = 1,maxBoxes = 5,maxWeight = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],portsCount = 10,maxBoxes = 5,maxWeight = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],portsCount = 10,maxBoxes = 5,maxWeight = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5]],portsCount = 4,maxBoxes = 4,maxWeight = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5]],portsCount = 4,maxBoxes = 4,maxWeight = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [1, 10], [2, 10], [3, 10]],portsCount = 3,maxBoxes = 3,maxWeight = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [1, 10], [2, 10], [3, 10]],portsCount = 3,maxBoxes = 3,maxWeight = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [1, 5], [2, 5], [2, 5], [3, 5], [3, 5]],portsCount = 3,maxBoxes = 3,maxWeight = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [1, 5], [2, 5], [2, 5], [3, 5], [3, 5]],portsCount = 3,maxBoxes = 3,maxWeight = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]],portsCount = 5,maxBoxes = 2,maxWeight = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]],portsCount = 5,maxBoxes = 2,maxWeight = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],portsCount = 1,maxBoxes = 5,maxWeight = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],portsCount = 1,maxBoxes = 5,maxWeight = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 40) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 40) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],portsCount = 10,maxBoxes = 5,maxWeight = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],portsCount = 10,maxBoxes = 5,maxWeight = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],portsCount = 7,maxBoxes = 4,maxWeight = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],portsCount = 7,maxBoxes = 4,maxWeight = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [1, 3], [2, 3], [2, 3], [3, 3], [3, 3]],portsCount = 3,maxBoxes = 4,maxWeight = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [1, 3], [2, 3], [2, 3], [3, 3], [3, 3]],portsCount = 3,maxBoxes = 4,maxWeight = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 1,maxWeight = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 1,maxWeight = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[2, 3], [2, 3], [3, 2], [3, 2], [3, 2]],portsCount = 3,maxBoxes = 2,maxWeight = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[2, 3], [2, 3], [3, 2], [3, 2], [3, 2]],portsCount = 3,maxBoxes = 2,maxWeight = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 10,maxWeight = 50) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 10,maxWeight = 50) == 11: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 2], [3, 1], [4, 4], [5, 3]],portsCount = 5,maxBoxes = 2,maxWeight = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 2], [3, 1], [4, 4], [5, 3]],portsCount = 5,maxBoxes = 2,maxWeight = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [2, 10], [1, 10]],portsCount = 3,maxBoxes = 2,maxWeight = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [2, 10], [1, 10]],portsCount = 3,maxBoxes = 2,maxWeight = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 3], [3, 3], [2, 3], [1, 3]],portsCount = 3,maxBoxes = 2,maxWeight = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 3], [3, 3], [2, 3], [1, 3]],portsCount = 3,maxBoxes = 2,maxWeight = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]],portsCount = 3,maxBoxes = 3,maxWeight = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]],portsCount = 3,maxBoxes = 3,maxWeight = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5]],portsCount = 2,maxBoxes = 5,maxWeight = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5]],portsCount = 2,maxBoxes = 5,maxWeight = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 2,maxWeight = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 2,maxWeight = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 3], [3, 2], [4, 1], [2, 2]],portsCount = 4,maxBoxes = 5,maxWeight = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 3], [3, 2], [4, 1], [2, 2]],portsCount = 4,maxBoxes = 5,maxWeight = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 3], [2, 2], [3, 2], [4, 2], [5, 2]],portsCount = 5,maxBoxes = 3,maxWeight = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 3], [2, 2], [3, 2], [4, 2], [5, 2]],portsCount = 5,maxBoxes = 3,maxWeight = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5]],portsCount = 2,maxBoxes = 3,maxWeight = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5]],portsCount = 2,maxBoxes = 3,maxWeight = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 6], [3, 7]],portsCount = 3,maxBoxes = 2,maxWeight = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 6], [3, 7]],portsCount = 3,maxBoxes = 2,maxWeight = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 10,maxWeight = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 10,maxWeight = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[2, 5], [2, 4], [5, 1], [5, 1], [5, 1], [1, 5], [1, 5], [1, 5], [1, 5], [5, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[2, 5], [2, 4], [5, 1], [5, 1], [5, 1], [1, 5], [1, 5], [1, 5], [1, 5], [5, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 2,maxWeight = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 2,maxWeight = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 3], [3, 2], [4, 1], [2, 2]],portsCount = 4,maxBoxes = 4,maxWeight = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 3], [3, 2], [4, 1], [2, 2]],portsCount = 4,maxBoxes = 4,maxWeight = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3]],portsCount = 3,maxBoxes = 3,maxWeight = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3]],portsCount = 3,maxBoxes = 3,maxWeight = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 10], [1, 10], [1, 10], [1, 10]],portsCount = 1,maxBoxes = 2,maxWeight = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 10], [1, 10], [1, 10], [1, 10]],portsCount = 1,maxBoxes = 2,maxWeight = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 5,maxWeight = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 5,maxWeight = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 1,maxWeight = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 1,maxWeight = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [[2, 10], [2, 10], [3, 10], [3, 10]],portsCount = 3,maxBoxes = 3,maxWeight = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [[2, 10], [2, 10], [3, 10], [3, 10]],portsCount = 3,maxBoxes = 3,maxWeight = 20) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 5) == 4
    assert candidate(boxes = [[2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4]],portsCount = 4,maxBoxes = 2,maxWeight = 4) == 10
    assert candidate(boxes = [[1, 2], [2, 2], [1, 2], [2, 2], [1, 2]],portsCount = 2,maxBoxes = 3,maxWeight = 6) == 7
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 1,maxWeight = 5) == 10
    assert candidate(boxes = [[1, 5], [1, 5], [1, 5], [2, 5], [2, 5], [2, 5]],portsCount = 2,maxBoxes = 2,maxWeight = 10) == 7
    assert candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5]],portsCount = 2,maxBoxes = 2,maxWeight = 10) == 9
    assert candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1]],portsCount = 15,maxBoxes = 5,maxWeight = 15) == 18
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 12
    assert candidate(boxes = [[1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2], [1, 2], [2, 2]],portsCount = 2,maxBoxes = 4,maxWeight = 10) == 13
    assert candidate(boxes = [[1, 1], [2, 1], [1, 1]],portsCount = 2,maxBoxes = 3,maxWeight = 3) == 4
    assert candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 5) == 6
    assert candidate(boxes = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100]],portsCount = 5,maxBoxes = 5,maxWeight = 500) == 6
    assert candidate(boxes = [[2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3]],portsCount = 5,maxBoxes = 3,maxWeight = 10) == 10
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 3,maxWeight = 30) == 7
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],portsCount = 9,maxBoxes = 3,maxWeight = 15) == 13
    assert candidate(boxes = [[1, 5], [2, 3], [3, 2], [2, 1], [1, 4]],portsCount = 3,maxBoxes = 5,maxWeight = 15) == 6
    assert candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 2,maxWeight = 2) == 6
    assert candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 3,maxWeight = 5) == 4
    assert candidate(boxes = [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]],portsCount = 3,maxBoxes = 6,maxWeight = 7) == 6
    assert candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],portsCount = 5,maxBoxes = 3,maxWeight = 5) == 16
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],portsCount = 10,maxBoxes = 10,maxWeight = 55) == 11
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10]],portsCount = 3,maxBoxes = 2,maxWeight = 20) == 5
    assert candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 10) == 8
    assert candidate(boxes = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],portsCount = 1,maxBoxes = 3,maxWeight = 9) == 4
    assert candidate(boxes = [[1, 3], [2, 5], [3, 7], [4, 9]],portsCount = 4,maxBoxes = 2,maxWeight = 12) == 7
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 5) == 9
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 50) == 6
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 25) == 8
    assert candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 5) == 10
    assert candidate(boxes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6
    assert candidate(boxes = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],portsCount = 5,maxBoxes = 2,maxWeight = 4) == 8
    assert candidate(boxes = [[1, 5], [2, 2], [3, 3], [1, 1]],portsCount = 3,maxBoxes = 3,maxWeight = 11) == 6
    assert candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]],portsCount = 10,maxBoxes = 10,maxWeight = 30) == 11
    assert candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6
    assert candidate(boxes = [[1, 3], [2, 2], [3, 1]],portsCount = 3,maxBoxes = 5,maxWeight = 6) == 4
    assert candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 1,maxWeight = 1) == 20
    assert candidate(boxes = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 12
    assert candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],portsCount = 5,maxBoxes = 2,maxWeight = 4) == 0
    assert candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 10) == 4
    assert candidate(boxes = [[1, 3], [2, 2], [1, 4], [2, 2], [3, 1]],portsCount = 3,maxBoxes = 3,maxWeight = 10) == 7
    assert candidate(boxes = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],portsCount = 1,maxBoxes = 5,maxWeight = 25) == 2
    assert candidate(boxes = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],portsCount = 10,maxBoxes = 5,maxWeight = 10) == 12
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 30) == 7
    assert candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5]],portsCount = 4,maxBoxes = 4,maxWeight = 20) == 5
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [1, 10], [2, 10], [3, 10]],portsCount = 3,maxBoxes = 3,maxWeight = 20) == 9
    assert candidate(boxes = [[1, 5], [1, 5], [2, 5], [2, 5], [3, 5], [3, 5]],portsCount = 3,maxBoxes = 3,maxWeight = 15) == 6
    assert candidate(boxes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]],portsCount = 5,maxBoxes = 2,maxWeight = 100) == 8
    assert candidate(boxes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],portsCount = 1,maxBoxes = 5,maxWeight = 15) == 2
    assert candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 5,maxWeight = 5) == 2
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 5,maxWeight = 40) == 7
    assert candidate(boxes = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],portsCount = 10,maxBoxes = 5,maxWeight = 15) == 2
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],portsCount = 7,maxBoxes = 4,maxWeight = 8) == 12
    assert candidate(boxes = [[1, 3], [1, 3], [2, 3], [2, 3], [3, 3], [3, 3]],portsCount = 3,maxBoxes = 4,maxWeight = 9) == 6
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 1,maxWeight = 10) == 10
    assert candidate(boxes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],portsCount = 5,maxBoxes = 5,maxWeight = 15) == 6
    assert candidate(boxes = [[2, 3], [2, 3], [3, 2], [3, 2], [3, 2]],portsCount = 3,maxBoxes = 2,maxWeight = 5) == 7
    assert candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 10,maxWeight = 50) == 11
    assert candidate(boxes = [[1, 5], [2, 2], [3, 1], [4, 4], [5, 3]],portsCount = 5,maxBoxes = 2,maxWeight = 10) == 8
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [2, 10], [1, 10]],portsCount = 3,maxBoxes = 2,maxWeight = 20) == 8
    assert candidate(boxes = [[1, 3], [2, 3], [3, 3], [2, 3], [1, 3]],portsCount = 3,maxBoxes = 2,maxWeight = 9) == 8
    assert candidate(boxes = [[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]],portsCount = 3,maxBoxes = 3,maxWeight = 6) == 6
    assert candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5], [1, 5], [2, 5]],portsCount = 2,maxBoxes = 5,maxWeight = 25) == 12
    assert candidate(boxes = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],portsCount = 5,maxBoxes = 2,maxWeight = 20) == 8
    assert candidate(boxes = [[1, 5], [2, 3], [3, 2], [4, 1], [2, 2]],portsCount = 4,maxBoxes = 5,maxWeight = 10) == 7
    assert candidate(boxes = [[1, 3], [2, 2], [3, 2], [4, 2], [5, 2]],portsCount = 5,maxBoxes = 3,maxWeight = 5) == 8
    assert candidate(boxes = [[1, 5], [2, 5], [1, 5], [2, 5], [1, 5]],portsCount = 2,maxBoxes = 3,maxWeight = 15) == 7
    assert candidate(boxes = [[1, 5], [2, 6], [3, 7]],portsCount = 3,maxBoxes = 2,maxWeight = 12) == 5
    assert candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 10,maxWeight = 10) == 11
    assert candidate(boxes = [[2, 5], [2, 4], [5, 1], [5, 1], [5, 1], [1, 5], [1, 5], [1, 5], [1, 5], [5, 1]],portsCount = 5,maxBoxes = 5,maxWeight = 10) == 10
    assert candidate(boxes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],portsCount = 1,maxBoxes = 2,maxWeight = 2) == 6
    assert candidate(boxes = [[1, 5], [2, 3], [3, 2], [4, 1], [2, 2]],portsCount = 4,maxBoxes = 4,maxWeight = 10) == 7
    assert candidate(boxes = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3]],portsCount = 3,maxBoxes = 3,maxWeight = 10) == 6
    assert candidate(boxes = [[1, 10], [1, 10], [1, 10], [1, 10]],portsCount = 1,maxBoxes = 2,maxWeight = 20) == 4
    assert candidate(boxes = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],portsCount = 10,maxBoxes = 5,maxWeight = 5) == 12
    assert candidate(boxes = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],portsCount = 5,maxBoxes = 1,maxWeight = 5) == 10
    assert candidate(boxes = [[2, 10], [2, 10], [3, 10], [3, 10]],portsCount = 3,maxBoxes = 3,maxWeight = 20) == 4


