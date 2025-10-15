def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([4, 5, 2, 1])) == "Tie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([4, 5, 2, 1])) == "Tie": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 5, 4, 7, 20, 5])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 5, 4, 7, 20, 5])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([12, 11, 14, 13, 16, 15])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([12, 11, 14, 13, 16, 15])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([6, 1, 6, 1, 6, 1])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([6, 1, 6, 1, 6, 1])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 3, 8, 5, 12, 7])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 3, 8, 5, 12, 7])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([6, 3, 8, 7, 10, 9])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([6, 3, 8, 7, 10, 9])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 20, 19, 20, 19, 20, 19, 20, 19])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 20, 19, 20, 19, 20, 19, 20, 19])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([60, 59, 62, 57, 64, 55, 66, 53, 68, 51])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([60, 59, 62, 57, 64, 55, 66, 53, 68, 51])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([24, 13, 26, 15, 28, 17, 30, 19, 32, 21, 34, 23, 36, 25, 38, 27])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([24, 13, 26, 15, 28, 17, 30, 19, 32, 21, 34, 23, 36, 25, 38, 27])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([90, 89, 92, 91, 94, 93, 96, 95, 98, 97, 100, 99, 102, 101, 104, 103])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([90, 89, 92, 91, 94, 93, 96, 95, 98, 97, 100, 99, 102, 101, 104, 103])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([98, 99, 96, 97, 94, 95, 92, 93, 90, 91, 88, 89, 86, 87, 84, 85, 82, 83, 80, 81])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([98, 99, 96, 97, 94, 95, 92, 93, 90, 91, 88, 89, 86, 87, 84, 85, 82, 83, 80, 81])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 1, 98, 3, 96, 5, 94, 7, 92, 9, 90, 11, 88, 13, 86, 15, 84, 17])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 1, 98, 3, 96, 5, 94, 7, 92, 9, 90, 11, 88, 13, 86, 15, 84, 17])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 11, 20, 19, 30, 29, 40, 39, 50, 49, 60, 59, 70, 69, 80, 79])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 11, 20, 19, 30, 29, 40, 39, 50, 49, 60, 59, 70, 69, 80, 79])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([24, 23, 34, 33, 44, 43, 54, 53, 64, 63, 74, 73])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([24, 23, 34, 33, 44, 43, 54, 53, 64, 63, 74, 73])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([60, 59, 62, 57, 64, 55, 66, 53, 68, 51, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([60, 59, 62, 57, 64, 55, 66, 53, 68, 51, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 88, 87, 76, 75, 64, 63, 52, 51, 40, 39, 28, 27, 16, 15])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 88, 87, 76, 75, 64, 63, 52, 51, 40, 39, 28, 27, 16, 15])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([42, 31, 44, 33, 46, 35, 48, 37, 50, 49])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([42, 31, 44, 33, 46, 35, 48, 37, 50, 49])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 99, 4, 97, 6, 95, 8, 93, 10, 91, 12, 89, 14, 87, 16, 85, 18, 83, 20, 81])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 99, 4, 97, 6, 95, 8, 93, 10, 91, 12, 89, 14, 87, 16, 85, 18, 83, 20, 81])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79, 82, 81, 84, 83, 86, 85, 88, 87])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79, 82, 81, 84, 83, 86, 85, 88, 87])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([24, 23, 26, 25, 30, 29, 32, 31, 36, 35, 40, 39])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([24, 23, 26, 25, 30, 29, 32, 31, 36, 35, 40, 39])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88, 14, 87, 15, 86, 16, 85, 17, 84, 18, 83, 19, 82, 20, 81])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88, 14, 87, 15, 86, 16, 85, 17, 84, 18, 83, 19, 82, 20, 81])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 52, 47, 54, 45, 56, 43, 58, 41, 60, 39, 62, 37, 64, 35, 66, 33, 68, 31])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 52, 47, 54, 45, 56, 43, 58, 41, 60, 39, 62, 37, 64, 35, 66, 33, 68, 31])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([6, 1, 6, 3, 6, 5, 6, 7, 6, 9, 6, 11, 6, 13, 6, 15, 6, 17, 6, 19])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([6, 1, 6, 3, 6, 5, 6, 7, 6, 9, 6, 11, 6, 13, 6, 15, 6, 17, 6, 19])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 20, 17, 20, 15, 20, 13, 20, 11, 20, 9, 20, 7, 20, 5])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 20, 17, 20, 15, 20, 13, 20, 11, 20, 9, 20, 7, 20, 5])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 60, 59, 70, 69, 80, 79, 90, 89, 100, 99, 110, 109, 120, 119, 130, 129, 140, 139])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 60, 59, 70, 69, 80, 79, 90, 89, 100, 99, 110, 109, 120, 119, 130, 129, 140, 139])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([60, 59, 62, 58, 64, 61, 66, 63, 68, 65, 70, 67, 72, 71])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([60, 59, 62, 58, 64, 61, 66, 63, 68, 65, 70, 67, 72, 71])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 1, 12, 3, 14, 5, 16, 7, 18, 9, 20, 11, 22, 13, 24, 15, 26, 17, 28, 19, 30, 21])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 1, 12, 3, 14, 5, 16, 7, 18, 9, 20, 11, 22, 13, 24, 15, 26, 17, 28, 19, 30, 21])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == "Odd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == "Odd": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([82, 81, 72, 71, 62, 61, 52, 51, 42, 41, 32, 31, 22, 21, 12, 11, 2, 1])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([82, 81, 72, 71, 62, 61, 52, 51, 42, 41, 32, 31, 22, 21, 12, 11, 2, 1])) == "Even": {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 1, 6, 3, 10, 5, 12, 7, 14, 9, 16, 11, 18, 13, 20, 15])) == "Even"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 1, 6, 3, 10, 5, 12, 7, 14, 9, 16, 11, 18, 13, 20, 15])) == "Even": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([4, 5, 2, 1])) == "Tie"
    assert candidate(head = list_node([2, 5, 4, 7, 20, 5])) == "Odd"
    assert candidate(head = list_node([12, 11, 14, 13, 16, 15])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95])) == "Even"
    assert candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9])) == "Odd"
    assert candidate(head = list_node([2, 1])) == "Even"
    assert candidate(head = list_node([6, 1, 6, 1, 6, 1])) == "Even"
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5])) == "Even"
    assert candidate(head = list_node([10, 3, 8, 5, 12, 7])) == "Even"
    assert candidate(head = list_node([6, 3, 8, 7, 10, 9])) == "Even"
    assert candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == "Odd"
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even"
    assert candidate(head = list_node([20, 19, 20, 19, 20, 19, 20, 19, 20, 19])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91])) == "Even"
    assert candidate(head = list_node([60, 59, 62, 57, 64, 55, 66, 53, 68, 51])) == "Even"
    assert candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37])) == "Even"
    assert candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even"
    assert candidate(head = list_node([98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83])) == "Even"
    assert candidate(head = list_node([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71])) == "Odd"
    assert candidate(head = list_node([24, 13, 26, 15, 28, 17, 30, 19, 32, 21, 34, 23, 36, 25, 38, 27])) == "Even"
    assert candidate(head = list_node([12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 11])) == "Even"
    assert candidate(head = list_node([30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29])) == "Even"
    assert candidate(head = list_node([3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20])) == "Even"
    assert candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even"
    assert candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59])) == "Even"
    assert candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47])) == "Even"
    assert candidate(head = list_node([12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even"
    assert candidate(head = list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == "Odd"
    assert candidate(head = list_node([90, 89, 92, 91, 94, 93, 96, 95, 98, 97, 100, 99, 102, 101, 104, 103])) == "Even"
    assert candidate(head = list_node([14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81])) == "Even"
    assert candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21])) == "Even"
    assert candidate(head = list_node([80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65])) == "Even"
    assert candidate(head = list_node([98, 99, 96, 97, 94, 95, 92, 93, 90, 91, 88, 89, 86, 87, 84, 85, 82, 83, 80, 81])) == "Odd"
    assert candidate(head = list_node([100, 1, 98, 3, 96, 5, 94, 7, 92, 9, 90, 11, 88, 13, 86, 15, 84, 17])) == "Even"
    assert candidate(head = list_node([10, 11, 20, 19, 30, 29, 40, 39, 50, 49, 60, 59, 70, 69, 80, 79])) == "Even"
    assert candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71])) == "Even"
    assert candidate(head = list_node([24, 23, 34, 33, 44, 43, 54, 53, 64, 63, 74, 73])) == "Even"
    assert candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == "Even"
    assert candidate(head = list_node([5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26])) == "Even"
    assert candidate(head = list_node([60, 59, 62, 57, 64, 55, 66, 53, 68, 51, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77])) == "Even"
    assert candidate(head = list_node([100, 99, 88, 87, 76, 75, 64, 63, 52, 51, 40, 39, 28, 27, 16, 15])) == "Even"
    assert candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31])) == "Even"
    assert candidate(head = list_node([2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == "Odd"
    assert candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63])) == "Even"
    assert candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even"
    assert candidate(head = list_node([34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even"
    assert candidate(head = list_node([20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39])) == "Even"
    assert candidate(head = list_node([80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61])) == "Even"
    assert candidate(head = list_node([98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79])) == "Even"
    assert candidate(head = list_node([42, 31, 44, 33, 46, 35, 48, 37, 50, 49])) == "Even"
    assert candidate(head = list_node([94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61])) == "Even"
    assert candidate(head = list_node([3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24])) == "Even"
    assert candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31])) == "Even"
    assert candidate(head = list_node([18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == "Even"
    assert candidate(head = list_node([88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69])) == "Even"
    assert candidate(head = list_node([24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41])) == "Even"
    assert candidate(head = list_node([44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])) == "Even"
    assert candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61])) == "Even"
    assert candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79])) == "Even"
    assert candidate(head = list_node([2, 99, 4, 97, 6, 95, 8, 93, 10, 91, 12, 89, 14, 87, 16, 85, 18, 83, 20, 81])) == "Odd"
    assert candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15])) == "Even"
    assert candidate(head = list_node([12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even"
    assert candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])) == "Even"
    assert candidate(head = list_node([70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79, 82, 81, 84, 83, 86, 85, 88, 87])) == "Even"
    assert candidate(head = list_node([24, 23, 26, 25, 30, 29, 32, 31, 36, 35, 40, 39])) == "Even"
    assert candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])) == "Even"
    assert candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19])) == "Even"
    assert candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == "Odd"
    assert candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87])) == "Even"
    assert candidate(head = list_node([1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88, 14, 87, 15, 86, 16, 85, 17, 84, 18, 83, 19, 82, 20, 81])) == "Odd"
    assert candidate(head = list_node([82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53])) == "Even"
    assert candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67])) == "Even"
    assert candidate(head = list_node([50, 49, 52, 47, 54, 45, 56, 43, 58, 41, 60, 39, 62, 37, 64, 35, 66, 33, 68, 31])) == "Even"
    assert candidate(head = list_node([50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65])) == "Even"
    assert candidate(head = list_node([6, 1, 6, 3, 6, 5, 6, 7, 6, 9, 6, 11, 6, 13, 6, 15, 6, 17, 6, 19])) == "Odd"
    assert candidate(head = list_node([8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27])) == "Even"
    assert candidate(head = list_node([22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35])) == "Even"
    assert candidate(head = list_node([44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89])) == "Even"
    assert candidate(head = list_node([20, 19, 20, 17, 20, 15, 20, 13, 20, 11, 20, 9, 20, 7, 20, 5])) == "Even"
    assert candidate(head = list_node([40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39, 40, 39])) == "Even"
    assert candidate(head = list_node([50, 49, 60, 59, 70, 69, 80, 79, 90, 89, 100, 99, 110, 109, 120, 119, 130, 129, 140, 139])) == "Even"
    assert candidate(head = list_node([44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59])) == "Even"
    assert candidate(head = list_node([60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59, 60, 59])) == "Even"
    assert candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23])) == "Even"
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85])) == "Even"
    assert candidate(head = list_node([60, 59, 62, 58, 64, 61, 66, 63, 68, 65, 70, 67, 72, 71])) == "Even"
    assert candidate(head = list_node([10, 1, 12, 3, 14, 5, 16, 7, 18, 9, 20, 11, 22, 13, 24, 15, 26, 17, 28, 19, 30, 21])) == "Even"
    assert candidate(head = list_node([90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71])) == "Even"
    assert candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == "Odd"
    assert candidate(head = list_node([82, 81, 72, 71, 62, 61, 52, 51, 42, 41, 32, 31, 22, 21, 12, 11, 2, 1])) == "Even"
    assert candidate(head = list_node([8, 1, 6, 3, 10, 5, 12, 7, 14, 9, 16, 11, 18, 13, 20, 15])) == "Even"


