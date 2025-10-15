def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 5, 15, 2, 7, 12, 20]), tree_node([20, 15, None, 10, 12, None, 5, 7, None, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 5, 15, 2, 7, 12, 20]), tree_node([20, 15, None, 10, 12, None, 5, 7, None, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), tree_node([10, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), tree_node([10, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1]), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1]), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 3, 2, 6, 5, 7, 4]), tree_node([7, 6, 4, 3, 5, None, None, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 3, 2, 6, 5, 7, 4]), tree_node([7, 6, 4, 3, 5, None, None, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1000, 999, 998, 997, 996]), tree_node([1000, None, 999, None, 998, None, 997, None, 996]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1000, 999, 998, 997, 996]), tree_node([1000, None, 999, None, 998, None, 997, None, 996])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [2, 1, 3]), tree_node([3, 2, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [2, 1, 3]), tree_node([3, 2, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 20, 30, 40, 50]), tree_node([50, 40, None, 30, None, 20, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 20, 30, 40, 50]), tree_node([50, 40, None, 30, None, 20, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 2, 1, 6, 0, 5]), tree_node([6, 3, 5, None, 2, 0, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 2, 1, 6, 0, 5]), tree_node([6, 3, 5, None, 2, 0, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5]), tree_node([5, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5]), tree_node([5, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 3, 2, 5, 4, 7, 6]), tree_node([7, 5, 6, 3, 4, None, None, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 3, 2, 5, 4, 7, 6]), tree_node([7, 5, 6, 3, 4, None, None, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 2, 1, 6, 0, 5, 9, 8, 7]), tree_node([9, 6, 8, 3, 5, None, 7, None, 2, 0, None, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 2, 1, 6, 0, 5, 9, 8, 7]), tree_node([9, 6, 8, 3, 5, None, 7, None, 2, 0, None, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 3, 2]), tree_node([3, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 3, 2]), tree_node([3, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [7, 5, 2, 6, 3, 1, 4]), tree_node([7, None, 6, 5, 4, None, 2, 3, None, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [7, 5, 2, 6, 3, 1, 4]), tree_node([7, None, 6, 5, 4, None, 2, 3, None, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 6, 5, 4, 9, 8, 7]), tree_node([9, 6, 8, 3, 5, None, 7, 2, None, None, 4, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 6, 5, 4, 9, 8, 7]), tree_node([9, 6, 8, 3, 5, None, 7, 2, None, None, 4, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 2, 1]), tree_node([3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 2, 1]), tree_node([3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 1, 4, 2]), tree_node([4, 3, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 1, 4, 2]), tree_node([4, 3, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 4, 3, 2, 1]), tree_node([5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 4, 3, 2, 1]), tree_node([5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3]), tree_node([3, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3]), tree_node([3, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 1, 2]), tree_node([3, None, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 1, 2]), tree_node([3, None, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 40, 30, 20, 10]), tree_node([50, None, 40, None, 30, None, 20, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 40, 30, 20, 10]), tree_node([50, None, 40, None, 30, None, 20, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [12, 24, 18, 15, 30, 28, 26, 25, 27, 35, 32, 31, 33, 34]), tree_node([35, 30, 34, 24, 28, 33, None, 12, 18, None, 27, 32, None, None, None, None, 15, 26, None, None, 31, None, None, None, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [12, 24, 18, 15, 30, 28, 26, 25, 27, 35, 32, 31, 33, 34]), tree_node([35, 30, 34, 24, 28, 33, None, 12, 18, None, 27, 32, None, None, None, None, 15, 26, None, None, 31, None, None, None, 25])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 1, 2, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 19, 20]), tree_node([20, 19, None, 18, None, 15, 17, 12, 14, None, 16, 9, 11, None, 13, None, None, 6, 8, None, 10, None, None, 3, 5, None, 7, None, None, None, 2, None, 4, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 1, 2, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 19, 20]), tree_node([20, 19, None, 18, None, 15, 17, 12, 14, None, 16, 9, 11, None, 13, None, None, 6, 8, None, 10, None, None, 3, 5, None, 7, None, None, None, 2, None, 4, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [34, 2, 78, 56, 90, 12, 3, 8, 5]), tree_node([90, 78, 12, 34, 56, None, 8, None, 2, None, None, 3, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [34, 2, 78, 56, 90, 12, 3, 8, 5]), tree_node([90, 78, 12, 34, 56, None, 8, None, 2, None, None, 3, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [2, 7, 11, 15, 3, 6, 7, 10, 1, 5, 4, 8, 12, 9]), tree_node([15, 11, 12, 7, None, 10, 9, 2, None, 7, 8, None, None, None, None, 6, None, 5, None, 3, None, 1, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [2, 7, 11, 15, 3, 6, 7, 10, 1, 5, 4, 8, 12, 9]), tree_node([15, 11, 12, 7, None, 10, 9, 2, None, 7, 8, None, None, None, None, 6, None, 5, None, 3, None, 1, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]), tree_node([150, None, 140, None, 130, None, 120, None, 110, None, 100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]), tree_node([150, None, 140, None, 130, None, 120, None, 110, None, 100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 50, 95, 60, 80, 30, 40, 70, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 90, 99]), tree_node([99, 95, None, 50, 90, 5, None, 85, None, None, None, 80, None, 60, 75, None, None, 70, None, 40, 65, 30, None, 55, None, None, None, 45, None, 35, None, 25, None, 20, None, None, 15, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 50, 95, 60, 80, 30, 40, 70, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 90, 99]), tree_node([99, 95, None, 50, 90, 5, None, 85, None, None, None, 80, None, 60, 75, None, None, 70, None, 40, 65, 30, None, 55, None, None, None, 45, None, 35, None, 25, None, 20, None, None, 15, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [2, 25, 1, 24, 3, 23, 4, 22, 5, 21, 6, 20, 7, 19, 8, 18, 9, 17, 10, 16, 11, 15, 12, 14, 13]), tree_node([25, 2, 24, None, None, 1, 23, None, None, 3, 22, None, None, 4, 21, None, None, 5, 20, None, None, 6, 19, None, None, 7, 18, None, None, 8, 17, None, None, 9, 16, None, None, 10, 15, None, None, 11, 14, None, None, 12, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [2, 25, 1, 24, 3, 23, 4, 22, 5, 21, 6, 20, 7, 19, 8, 18, 9, 17, 10, 16, 11, 15, 12, 14, 13]), tree_node([25, 2, 24, None, None, 1, 23, None, None, 3, 22, None, None, 4, 21, None, None, 5, 20, None, None, 6, 19, None, None, 7, 18, None, None, 8, 17, None, None, 9, 16, None, None, 10, 15, None, None, 11, 14, None, None, 12, 13])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [42, 17, 13, 14, 35, 65, 23, 54, 78, 9, 11, 2, 3, 5, 7, 19, 21, 25, 30]), tree_node([78, 65, 30, 42, 54, 25, None, None, 35, 23, None, 21, None, 17, None, None, None, 19, None, None, 14, 11, None, 13, None, 9, 7, None, None, None, None, 5, None, 3, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [42, 17, 13, 14, 35, 65, 23, 54, 78, 9, 11, 2, 3, 5, 7, 19, 21, 25, 30]), tree_node([78, 65, 30, 42, 54, 25, None, None, 35, 23, None, 21, None, 17, None, None, None, 19, None, None, 14, 11, None, 13, None, 9, 7, None, None, None, None, 5, None, 3, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [42, 53, 23, 78, 12, 34, 65, 89, 100, 56]), tree_node([100, 89, 56, 78, None, None, None, 53, 65, 42, 23, 34, None, None, None, None, None, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [42, 53, 23, 78, 12, 34, 65, 89, 100, 56]), tree_node([100, 89, 56, 78, None, None, None, 53, 65, 42, 23, 34, None, None, None, None, None, 12])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 5, 2, 4, 1, 6, 7, 8, 9, 10, 0]), tree_node([10, 9, 0, 8, None, None, None, 7, None, 6, None, 5, None, 3, 4, None, None, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 5, 2, 4, 1, 6, 7, 8, 9, 10, 0]), tree_node([10, 9, 0, 8, None, None, None, 7, None, 6, None, 5, None, 3, 4, None, None, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), tree_node([15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), tree_node([15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [12, 5, 15, 3, 8, 18, 1, 4, 7, 11, 13, 17, 6, 2, 9, 14, 10, 16]), tree_node([18, 15, 17, 12, 8, 13, 16, None, 5, 3, None, 11, None, 14, None, None, None, None, None, 7, None, 9, 10, 4, None, 6, None, None, None, 1, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [12, 5, 15, 3, 8, 18, 1, 4, 7, 11, 13, 17, 6, 2, 9, 14, 10, 16]), tree_node([18, 15, 17, 12, 8, 13, 16, None, 5, 3, None, 11, None, 14, None, None, None, None, None, 7, None, 9, 10, 4, None, 6, None, None, None, 1, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 8, 3, 9, 6, 2, 10, 7, 1, 4]), tree_node([10, 9, 7, 8, 6, None, 4, 5, 3, None, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 8, 3, 9, 6, 2, 10, 7, 1, 4]), tree_node([10, 9, 7, 8, 6, None, 4, 5, 3, None, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [999, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25]), tree_node([999, None, 800, None, 700, None, 600, None, 500, None, 400, None, 300, None, 200, None, 100, None, 50, None, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [999, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25]), tree_node([999, None, 800, None, 700, None, 600, None, 500, None, 400, None, 300, None, 200, None, 100, None, 50, None, 25])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 30, 20, 40, 10, 60, 50, 70, 80, 15]), tree_node([80, 70, 15, 60, None, None, None, 50, 50, None, 40, None, None, 30, 10, None, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 30, 20, 40, 10, 60, 50, 70, 80, 15]), tree_node([80, 70, 15, 60, None, None, None, 50, 50, None, 40, None, None, 30, 10, None, 20])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, 10, 30, 60, 90, 110, 130, 160, 180, 210, 230, 260, 280, 310, 330, 360, 380]), tree_node([380, 375, None, 350, 360, 300, 325, 330, None, 200, 250, 275, None, 310, None, None, 100, 150, None, 225, None, 280, None, None, None, 50, None, 175, None, 260, None, None, None, 125, None, 230, None, 75, None, 210, None, 25, None, 180, None, None, None, 160, None, 130, None, 110, None, 90, None, 60, None, 30, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, 10, 30, 60, 90, 110, 130, 160, 180, 210, 230, 260, 280, 310, 330, 360, 380]), tree_node([380, 375, None, 350, 360, 300, 325, 330, None, 200, 250, 275, None, 310, None, None, 100, 150, None, 225, None, 280, None, None, None, 50, None, 175, None, 260, None, None, None, 125, None, 230, None, 75, None, 210, None, 25, None, 180, None, None, None, 160, None, 130, None, 110, None, 90, None, 60, None, 30, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [99, 23, 77, 45, 67, 89, 12, 34, 56, 78, 90, 100, 110, 120, 130, 140, 150]), tree_node([150, 140, None, 130, None, 120, None, 110, None, 100, None, 99, None, None, 90, 89, None, 77, 78, 23, 67, 56, None, None, None, 45, None, 34, None, None, None, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [99, 23, 77, 45, 67, 89, 12, 34, 56, 78, 90, 100, 110, 120, 130, 140, 150]), tree_node([150, 140, None, 130, None, 120, None, 110, None, 100, None, 99, None, None, 90, 89, None, 77, 78, 23, 67, 56, None, None, None, 45, None, 34, None, None, None, 12])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9]), tree_node([1000, None, 950, None, 900, None, 850, None, 800, None, 750, None, 700, None, 650, None, 600, None, 550, None, 500, None, 450, None, 400, None, 350, None, 300, None, 250, None, 200, None, 150, None, 100, None, 50, None, 9, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9]), tree_node([1000, None, 950, None, 900, None, 850, None, 800, None, 750, None, 700, None, 650, None, 600, None, 550, None, 500, None, 450, None, 400, None, 350, None, 300, None, 250, None, 200, None, 150, None, 100, None, 50, None, 9, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 20, 30, 40, 50, 60, 70, 80, 90, 10]), tree_node([100, None, 90, 80, 10, 70, None, None, None, 60, None, 50, None, 40, None, 30, None, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 20, 30, 40, 50, 60, 70, 80, 90, 10]), tree_node([100, None, 90, 80, 10, 70, None, None, None, 60, None, 50, None, 40, None, 30, None, 20])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 6, 3, 5, 2, 4, 7, 10, 8, 9, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 10, None, 7, 9, 6, None, 8, None, 1, 5, None, None, None, None, 3, 4, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 6, 3, 5, 2, 4, 7, 10, 8, 9, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 10, None, 7, 9, 6, None, 8, None, 1, 5, None, None, None, None, 3, 4, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [42, 17, 93, 31, 58, 72, 12, 67, 85, 29, 47, 63, 54, 81, 96, 50, 77, 21, 61, 88, 19, 35, 52, 69, 37, 74, 90, 24, 44, 59, 76, 40, 66, 84, 27, 48, 65, 82, 33, 49, 64, 83, 30, 45, 57, 73, 32, 43, 56, 71, 34, 46, 55, 70, 36, 41, 51, 68, 38, 39]), tree_node([96, 93, 90, 42, 85, 88, 84, None, 17, 72, 81, 77, 74, 76, 83, None, None, 58, 67, 63, None, 50, 61, 69, None, 59, 66, 82, 73, 31, None, 12, None, 47, 54, None, None, 21, None, 52, 37, 44, None, 40, None, 65, 64, 57, 71, None, None, None, None, 29, None, None, None, None, None, 35, None, None, None, 24, None, None, None, 48, None, 49, None, 45, None, 56, 70, None, None, 19, None, None, None, 27, None, 33, None, 30, None, 43, None, 55, 68, None, None, None, None, None, None, None, None, 32, None, 46, None, 51, 39, None, None, 34, None, 41, None, 38, None, None, None, 36]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [42, 17, 93, 31, 58, 72, 12, 67, 85, 29, 47, 63, 54, 81, 96, 50, 77, 21, 61, 88, 19, 35, 52, 69, 37, 74, 90, 24, 44, 59, 76, 40, 66, 84, 27, 48, 65, 82, 33, 49, 64, 83, 30, 45, 57, 73, 32, 43, 56, 71, 34, 46, 55, 70, 36, 41, 51, 68, 38, 39]), tree_node([96, 93, 90, 42, 85, 88, 84, None, 17, 72, 81, 77, 74, 76, 83, None, None, 58, 67, 63, None, 50, 61, 69, None, 59, 66, 82, 73, 31, None, 12, None, 47, 54, None, None, 21, None, 52, 37, 44, None, 40, None, 65, 64, 57, 71, None, None, None, None, 29, None, None, None, None, None, 35, None, None, None, 24, None, None, None, 48, None, 49, None, 45, None, 56, 70, None, None, 19, None, None, None, 27, None, 33, None, 30, None, 43, None, 55, 68, None, None, None, None, None, None, None, None, 32, None, 46, None, 51, 39, None, None, 34, None, 41, None, 38, None, None, None, 36])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), tree_node([10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9, None, -10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), tree_node([10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9, None, -10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 15, 3, 7, 9, 1, 20, 18, 17, 16, 14, 13]), tree_node([20, 15, 18, 8, 9, None, 17, None, None, 7, 1, None, 16, 3, None, None, None, None, 14, None, None, None, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 15, 3, 7, 9, 1, 20, 18, 17, 16, 14, 13]), tree_node([20, 15, 18, 8, 9, None, 17, None, None, 7, 1, None, 16, 3, None, None, None, None, 14, None, None, None, 13])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]), tree_node([1000, 900, 975, 800, None, 925, None, 700, None, 875, None, 600, None, 825, None, 500, None, 775, None, 400, None, 725, None, 300, None, 675, None, 200, None, 625, None, 100, None, 575, None, None, None, 525, None, 475, None, 425, None, 375, None, 325, None, 275, None, 225, None, 175, None, 125, None, 75, None, 50, None, None, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]), tree_node([1000, 900, 975, 800, None, 925, None, 700, None, 875, None, 600, None, 825, None, 500, None, 775, None, 400, None, 725, None, 300, None, 675, None, 200, None, 625, None, 100, None, 575, None, None, None, 525, None, 475, None, 425, None, 375, None, 325, None, 275, None, 225, None, 175, None, 125, None, 75, None, 50, None, None, 25])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [7, 4, 9, 1, 3, 8, 2, 5, 6]), tree_node([9, 7, 8, None, 4, 3, 6, None, None, 1, None, 5, None, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [7, 4, 9, 1, 3, 8, 2, 5, 6]), tree_node([9, 7, 8, None, 4, 3, 6, None, None, 1, None, 5, None, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]), tree_node([9, 5, 9, 4, None, 6, None, 3, 1, 2, 5, None, 1, None, None, None, None, None, 5, None, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]), tree_node([9, 5, 9, 4, None, 6, None, 3, 1, 2, 5, None, 1, None, None, None, None, None, 5, None, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 8, 2, 1, 4, 6, 3, 9, 7, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, 7, 5, 6, None, 0, None, None, 4, 3, None, None, 2, None, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 8, 2, 1, 4, 6, 3, 9, 7, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, 7, 5, 6, None, 0, None, None, 4, 3, None, None, 2, None, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [42, 3, 56, 23, 89, 12, 67, 45]), tree_node([89, 56, 67, 42, 23, 12, 45, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [42, 3, 56, 23, 89, 12, 67, 45]), tree_node([89, 56, 67, 42, 23, 12, 45, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 90, 110, 80, 95, 105, 70, 85, 92, 98, 60, 75, 82, 88, 93, 97, 50, 65, 72, 78, 83, 87, 91, 94, 96, 40, 55, 62, 68, 73, 77, 81, 86, 90, 99, 30, 45, 52, 58, 63, 67, 71, 76, 84, 89, 20, 35, 42, 48, 53, 57, 61, 66, 74, 79, 85, 9, 18, 25, 32, 38, 43, 47, 51, 56, 60, 64, 69, 75, 80, 3, 12, 21, 27, 33, 37, 41, 46, 50, 55, 59, 63, 68, 72, 77, 82, 7, 15, 23, 29, 34, 38, 42, 45, 49, 54, 58, 62, 67, 71, 76, 1, 6, 11, 16, 22, 28, 32, 36, 40, 44, 48, 52, 57, 61, 66, 70, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]), tree_node([110, 100, 105, None, 90, 95, 99, None, None, 80, None, 98, 89, None, None, 92, 97, 84, 85, 85, None, 93, 96, 76, None, 79, 82, 70, None, 88, None, 94, 90, 71, None, 74, None, 80, 76, None, None, 82, None, 91, None, 86, None, 67, None, 66, None, 75, 77, 71, 70, 75, None, 87, None, 81, None, 63, None, 61, None, 69, None, 72, None, 67, None, 66, 70, 60, None, 83, None, 77, None, 58, None, 57, None, 64, None, 68, None, 62, None, 61, None, 65, None, None, None, 78, None, 73, None, 52, None, 53, None, 60, None, 63, None, 58, None, 57, None, 60, None, 72, None, 68, None, 45, None, 48, None, 56, None, 59, None, 54, None, 52, None, 55, None, 65, None, 62, None, 30, None, 42, None, 51, None, 55, None, 49, None, 48, None, 50, None, 50, None, 55, None, None, None, 35, None, 47, None, 50, None, 45, None, 44, None, 45, None, None, None, 40, None, 20, None, 43, None, 46, None, 42, None, 40, None, 40, None, None, None, None, None, 38, None, 41, None, 38, None, 36, None, 35, None, 32, None, 37, None, 34, None, 32, None, 30, None, 25, None, 33, None, 29, None, 28, None, 25, None, 18, None, 27, None, 23, None, 22, None, 20, None, 9, None, 21, None, 15, None, 16, None, 15, None, None, None, 12, None, 7, None, 11, None, 10, None, 3, None, None, None, 6, None, 5, None, None, None, 1, None, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 90, 110, 80, 95, 105, 70, 85, 92, 98, 60, 75, 82, 88, 93, 97, 50, 65, 72, 78, 83, 87, 91, 94, 96, 40, 55, 62, 68, 73, 77, 81, 86, 90, 99, 30, 45, 52, 58, 63, 67, 71, 76, 84, 89, 20, 35, 42, 48, 53, 57, 61, 66, 74, 79, 85, 9, 18, 25, 32, 38, 43, 47, 51, 56, 60, 64, 69, 75, 80, 3, 12, 21, 27, 33, 37, 41, 46, 50, 55, 59, 63, 68, 72, 77, 82, 7, 15, 23, 29, 34, 38, 42, 45, 49, 54, 58, 62, 67, 71, 76, 1, 6, 11, 16, 22, 28, 32, 36, 40, 44, 48, 52, 57, 61, 66, 70, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]), tree_node([110, 100, 105, None, 90, 95, 99, None, None, 80, None, 98, 89, None, None, 92, 97, 84, 85, 85, None, 93, 96, 76, None, 79, 82, 70, None, 88, None, 94, 90, 71, None, 74, None, 80, 76, None, None, 82, None, 91, None, 86, None, 67, None, 66, None, 75, 77, 71, 70, 75, None, 87, None, 81, None, 63, None, 61, None, 69, None, 72, None, 67, None, 66, 70, 60, None, 83, None, 77, None, 58, None, 57, None, 64, None, 68, None, 62, None, 61, None, 65, None, None, None, 78, None, 73, None, 52, None, 53, None, 60, None, 63, None, 58, None, 57, None, 60, None, 72, None, 68, None, 45, None, 48, None, 56, None, 59, None, 54, None, 52, None, 55, None, 65, None, 62, None, 30, None, 42, None, 51, None, 55, None, 49, None, 48, None, 50, None, 50, None, 55, None, None, None, 35, None, 47, None, 50, None, 45, None, 44, None, 45, None, None, None, 40, None, 20, None, 43, None, 46, None, 42, None, 40, None, 40, None, None, None, None, None, 38, None, 41, None, 38, None, 36, None, 35, None, 32, None, 37, None, 34, None, 32, None, 30, None, 25, None, 33, None, 29, None, 28, None, 25, None, 18, None, 27, None, 23, None, 22, None, 20, None, 9, None, 21, None, 15, None, 16, None, 15, None, None, None, 12, None, 7, None, 11, None, 10, None, 3, None, None, None, 6, None, 5, None, None, None, 1, None, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), tree_node([20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), tree_node([20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [7, 2, 9, 3, 5, 8, 1, 4, 6, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, None, 7, 8, None, 2, 5, 6, None, None, 3, None, 4, 0, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [7, 2, 9, 3, 5, 8, 1, 4, 6, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, None, 7, 8, None, 2, 5, 6, None, None, 3, None, 4, 0, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16, 21, 30, 22, 29, 23, 28, 24, 27, 25, 26]), tree_node([30, 21, 29, 20, None, 22, 28, 11, 19, None, None, 23, 27, 10, None, 12, 18, None, None, 24, 26, 1, 9, None, None, 13, 17, None, None, 25, None, None, None, 2, 8, None, None, 14, 16, None, None, None, None, 3, 7, None, None, 15, None, None, None, 4, 6, None, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16, 21, 30, 22, 29, 23, 28, 24, 27, 25, 26]), tree_node([30, 21, 29, 20, None, 22, 28, 11, 19, None, None, 23, 27, 10, None, 12, 18, None, None, 24, 26, 1, 9, None, None, 13, 17, None, None, 25, None, None, None, 2, 8, None, None, 14, 16, None, None, None, None, 3, 7, None, None, 15, None, None, None, 4, 6, None, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]), tree_node([29, 27, None, 25, None, 23, None, 21, None, 19, None, 17, None, 15, None, 13, None, 11, None, 9, None, 7, None, 5, None, 3, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]), tree_node([29, 27, None, 25, None, 23, None, 21, None, 19, None, 17, None, 15, None, 13, None, 11, None, 9, None, 7, None, 5, None, 3, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 5, 12, 1, 10, 2, 9, 3, 7, 4, 6, 11]), tree_node([12, 8, 11, None, 5, 10, None, None, None, 1, 9, None, None, 2, 7, None, None, 3, 6, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 5, 12, 1, 10, 2, 9, 3, 7, 4, 6, 11]), tree_node([12, 8, 11, None, 5, 10, None, None, None, 1, 9, None, None, 2, 7, None, None, 3, 6, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), tree_node([9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9, None, -10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), tree_node([9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9, None, -10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989]), tree_node([999, None, 998, None, 997, None, 996, None, 995, None, 994, None, 993, None, 992, None, 991, None, 990, None, 989]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989]), tree_node([999, None, 998, None, 997, None, 996, None, 995, None, 994, None, 993, None, 992, None, 991, None, 990, None, 989])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 40, 30, 20, 10, 90, 80, 70, 60, 100]), tree_node([100, 90, None, 50, 80, None, 40, None, 70, None, 30, None, 60, None, 20, None, None, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 40, 30, 20, 10, 90, 80, 70, 60, 100]), tree_node([100, 90, None, 50, 80, None, 40, None, 70, None, 30, None, 60, None, 20, None, None, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 2, 7, 1, 8, 6, 4, 3, 9, 0, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, 10, 8, 0, None, None, 7, 6, None, None, 5, 1, None, 4, None, 2, None, None, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 2, 7, 1, 8, 6, 4, 3, 9, 0, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, 10, 8, 0, None, None, 7, 6, None, None, 5, 1, None, 4, None, 2, None, None, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [300, 200, 100, 250, 150, 50, 275, 225, 175, 125, 75, 325, 305, 255, 205, 155, 105, 350, 320, 290, 260, 230, 210, 180, 160, 130, 110, 80, 60, 40]), tree_node([350, 325, 320, 300, 305, None, 290, None, 275, None, 255, None, 260, 250, 225, None, 205, None, 230, 200, 150, None, 175, None, 155, None, 210, None, 100, None, 50, None, 125, None, 105, None, 180, None, None, None, None, None, 75, None, None, None, 160, None, None, None, 130, None, 110, None, 80, None, 60, None, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [300, 200, 100, 250, 150, 50, 275, 225, 175, 125, 75, 325, 305, 255, 205, 155, 105, 350, 320, 290, 260, 230, 210, 180, 160, 130, 110, 80, 60, 40]), tree_node([350, 325, 320, 300, 305, None, 290, None, 275, None, 255, None, 260, 250, 225, None, 205, None, 230, 200, 150, None, 175, None, 155, None, 210, None, 100, None, 50, None, 125, None, 105, None, 180, None, None, None, None, None, 75, None, None, None, 160, None, None, None, 130, None, 110, None, 80, None, 60, None, 40])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 9, 1, 8, 2, 7, 3, 6, 4]), tree_node([9, 5, 8, None, None, 1, 7, None, None, 2, 6, None, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 9, 1, 8, 2, 7, 3, 6, 4]), tree_node([9, 5, 8, None, None, 1, 7, None, None, 2, 6, None, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]), tree_node([305, 295, None, 285, None, 275, None, 265, None, 255, None, 245, None, 235, None, 225, None, 215, None, 205, None, 195, None, 185, None, 175, None, 165, None, 155, None, 145, None, 135, None, 125, None, 115, None, 105, None, 95, None, 85, None, 75, None, 65, None, 55, None, 45, None, 35, None, 25, None, 15, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]), tree_node([305, 295, None, 285, None, 275, None, 265, None, 255, None, 245, None, 235, None, 225, None, 215, None, 205, None, 195, None, 185, None, 175, None, 165, None, 155, None, 145, None, 135, None, 125, None, 115, None, 105, None, 95, None, 85, None, 75, None, 65, None, 55, None, 45, None, 35, None, 25, None, 15, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [45, 67, 23, 89, 12, 34, 56, 78, 90]), tree_node([90, 89, None, 67, 78, 45, 23, 56, None, None, None, None, None, 34, None, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [45, 67, 23, 89, 12, 34, 56, 78, 90]), tree_node([90, 89, None, 67, 78, 45, 23, 56, None, None, None, None, None, 34, None, 12])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 90, 30, 70, 20, 80, 10, 60, 40]), tree_node([90, 50, 80, None, None, 70, 60, 30, 20, 10, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 90, 30, 70, 20, 80, 10, 60, 40]), tree_node([90, 50, 80, None, None, 70, 60, 30, 20, 10, 40])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 1, 9, None, None, 2, 8, None, None, 3, 7, None, None, 4, 6, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 1, 9, None, None, 2, 8, None, None, 3, 7, None, None, 4, 6, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]), tree_node([1024, 512, None, 256, None, 128, None, 64, None, 32, None, 16, None, 8, None, 4, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]), tree_node([1024, 512, None, 256, None, 128, None, 64, None, 32, None, 16, None, 8, None, 4, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [7, 10, 4, 3, 20, 15, 9, 8, 6, 11, 18]), tree_node([20, 10, 18, 7, 4, 15, None, None, None, None, 3, None, 11, None, None, 9, None, None, 8, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [7, 10, 4, 3, 20, 15, 9, 8, 6, 11, 18]), tree_node([20, 10, 18, 7, 4, 15, None, None, None, None, 3, None, 11, None, None, 9, None, None, 8, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 90, 30, 40, 70, 80, 20, 60, 10]), tree_node([90, 50, 80, None, None, 70, 60, 40, None, 20, 10, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 90, 30, 40, 70, 80, 20, 60, 10]), tree_node([90, 50, 80, None, None, 70, 60, 40, None, 20, 10, 30])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [42, 27, 61, 30, 19, 7, 5, 66, 39, 21, 22]), tree_node([66, 61, 39, 42, 30, None, 22, None, 27, None, 19, 21, None, None, None, None, 7, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [42, 27, 61, 30, 19, 7, 5, 66, 39, 21, 22]), tree_node([66, 61, 39, 42, 30, None, 22, None, 27, None, 19, 21, None, None, None, None, 7, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 4, 3, 7, 6, 5, 8, 9, 10, 12, 11, 14, 13, 15]), tree_node([15, 14, None, 12, 13, 10, 11, None, None, 9, None, None, None, 8, None, 7, None, 4, 6, 2, 3, None, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 4, 3, 7, 6, 5, 8, 9, 10, 12, 11, 14, 13, 15]), tree_node([15, 14, None, 12, 13, 10, 11, None, None, 9, None, None, None, 8, None, 7, None, 4, 6, 2, 3, None, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]), tree_node([5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]), tree_node([5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [20, 50, 40, 30, 60, 90, 80, 70, 100]), tree_node([100, 90, None, 60, 80, 50, None, None, 70, 20, 40, None, None, None, None, None, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [20, 50, 40, 30, 60, 90, 80, 70, 100]), tree_node([100, 90, None, 60, 80, 50, None, None, 70, 20, 40, None, None, None, None, None, 30])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 10, 90, 9, 80, 8, 70, 7, 60, 6, 50, 5, 40, 4, 30, 3, 20, 2, 10, 1]), tree_node([100, None, 90, 10, 80, None, None, 9, 70, None, None, 8, 60, None, None, 7, 50, None, None, 6, 40, None, None, 5, 30, None, None, 4, 20, None, None, 3, 10, None, None, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 10, 90, 9, 80, 8, 70, 7, 60, 6, 50, 5, 40, 4, 30, 3, 20, 2, 10, 1]), tree_node([100, None, 90, 10, 80, None, None, 9, 70, None, None, 8, 60, None, None, 7, 50, None, None, 6, 40, None, None, 5, 30, None, None, 4, 20, None, None, 3, 10, None, None, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [2, 1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]), tree_node([15, 13, 14, 11, 12, None, None, 9, 10, None, None, 7, 8, None, None, 5, 6, None, None, 3, 4, None, None, 2, None, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [2, 1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]), tree_node([15, 13, 14, 11, 12, None, None, 9, 10, None, None, 7, 8, None, None, 5, 6, None, None, 3, 4, None, None, 2, None, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15]), tree_node([15, 14, None, 12, 13, 10, 11, None, None, 8, 9, None, None, 6, 7, None, None, 4, 5, None, None, 2, 3, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15]), tree_node([15, 14, None, 12, 13, 10, 11, None, None, 8, 9, None, None, 6, 7, None, None, 4, 5, None, None, 2, 3, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]), tree_node([9, 8, None, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]), tree_node([9, 8, None, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]), tree_node([20, 15, 19, 10, 14, None, 18, 5, 9, None, 13, None, 17, None, 4, None, 8, None, 12, None, 16, None, 3, None, 7, None, 11, None, None, None, 2, None, 6, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]), tree_node([20, 15, 19, 10, 14, None, 18, 5, 9, None, 13, None, 17, None, 4, None, 8, None, 12, None, 16, None, 3, None, 7, None, 11, None, None, None, 2, None, 6, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 5, 12, 22, 32, 42, 52, 60, 65, 70, 75, 80]), tree_node([80, 75, None, 70, None, 65, None, 60, None, 55, None, 50, 52, 40, 45, 42, None, 30, None, 35, None, 32, None, 20, None, 25, None, 22, None, 10, None, 15, None, 12, None, None, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 5, 12, 22, 32, 42, 52, 60, 65, 70, 75, 80]), tree_node([80, 75, None, 70, None, 65, None, 60, None, 55, None, 50, 52, 40, 45, 42, None, 30, None, 35, None, 32, None, 20, None, 25, None, 22, None, 10, None, 15, None, 12, None, None, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), tree_node([25, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), tree_node([25, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), tree_node([100, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), tree_node([100, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50]), tree_node([50, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50]), tree_node([50, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 50, 150, 250, 350, 450, 5, 25, 125, 175, 225, 275, 325, 375, 425, 475]), tree_node([500, 400, 475, 300, None, 450, None, 200, None, 350, 425, 100, None, 250, None, 375, None, None, None, 150, None, 325, None, 50, None, 275, None, None, None, 225, None, 175, None, 125, None, 25, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 50, 150, 250, 350, 450, 5, 25, 125, 175, 225, 275, 325, 375, 425, 475]), tree_node([500, 400, 475, 300, None, 450, None, 200, None, 350, 425, 100, None, 250, None, 375, None, None, None, 150, None, 325, None, 50, None, 275, None, None, None, 225, None, 175, None, 125, None, 25, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 25, 75, 12, 38, 62, 88, 6, 18, 32, 46, 58, 70, 82, 94, 3, 9, 15, 21, 28, 34, 41, 48, 54, 60, 66, 72, 78, 84, 90, 96]), tree_node([96, 94, None, 88, 90, 75, 82, 84, None, 50, 62, 70, None, 78, None, None, 25, 38, None, 58, None, 72, None, None, None, 12, None, 46, None, 66, None, None, None, 32, None, 60, None, 18, None, 54, None, 6, None, 48, None, None, None, 41, None, 34, None, 28, None, 21, None, 15, None, 9, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 25, 75, 12, 38, 62, 88, 6, 18, 32, 46, 58, 70, 82, 94, 3, 9, 15, 21, 28, 34, 41, 48, 54, 60, 66, 72, 78, 84, 90, 96]), tree_node([96, 94, None, 88, 90, 75, 82, 84, None, 50, 62, 70, None, 78, None, None, 25, 38, None, 58, None, 72, None, None, None, 12, None, 46, None, 66, None, None, None, 32, None, 60, None, 18, None, 54, None, 6, None, 48, None, None, None, 41, None, 34, None, 28, None, 21, None, 15, None, 9, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6]), tree_node([9, 5, 8, None, 1, 2, 7, None, None, None, None, 3, 6, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6]), tree_node([9, 5, 8, None, 1, 2, 7, None, None, None, None, 3, 6, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 70, 82, 93, 3, 9, 15, 21, 27, 34, 40, 49, 53, 61, 69, 76, 81, 88, 91, 95, 97]), tree_node([97, 95, None, 93, None, 87, 91, 75, 82, 88, None, 50, 62, 70, None, 81, None, None, 25, 37, None, 56, None, 76, None, None, None, 12, None, 43, None, 69, None, None, None, 31, None, 61, None, 18, None, 53, None, 6, None, 49, None, None, None, 40, None, 34, None, 27, None, 21, None, 15, None, 9, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 70, 82, 93, 3, 9, 15, 21, 27, 34, 40, 49, 53, 61, 69, 76, 81, 88, 91, 95, 97]), tree_node([97, 95, None, 93, None, 87, 91, 75, 82, 88, None, 50, 62, 70, None, 81, None, None, 25, 37, None, 56, None, 76, None, None, None, 12, None, 43, None, 69, None, None, None, 31, None, 61, None, 18, None, 53, None, 6, None, 49, None, None, None, 40, None, 34, None, 27, None, 21, None, 15, None, 9, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 3, 10, 1, 6, 14, 4, 7, 13, 2, 9, 12, 11, 5]), tree_node([14, 10, 13, 8, 6, 7, 12, None, 3, 1, None, 4, None, 9, 11, None, None, None, None, None, None, 2, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 3, 10, 1, 6, 14, 4, 7, 13, 2, 9, 12, 11, 5]), tree_node([14, 10, 13, 8, 6, 7, 12, None, 3, 1, None, 4, None, 9, 11, None, None, None, None, None, None, 2, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [15, 10, 18, 8, 12, 19, 13, 7, 9, 11, 14, 16, 17]), tree_node([19, 18, 17, 15, 12, 16, None, None, 10, 8, None, 14, None, None, None, None, None, 13, None, None, 11, 9, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [15, 10, 18, 8, 12, 19, 13, 7, 9, 11, 14, 16, 17]), tree_node([19, 18, 17, 15, 12, 16, None, None, 10, 8, None, 14, None, None, None, None, None, 13, None, None, 11, 9, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]), tree_node([10, 1, 9, None, None, 2, 8, None, None, 3, 7, None, None, 4, 6, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]), tree_node([10, 1, 9, None, None, 2, 8, None, None, 3, 7, None, None, 4, 6, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 4, 3, 7, 6, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 4, 6, 2, 3, None, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 4, 3, 7, 6, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 4, 6, 2, 3, None, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]), tree_node([150, 140, None, 130, None, 120, None, 110, None, 100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]), tree_node([150, 140, None, 130, None, 120, None, 110, None, 100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 5, 2, 3, 15, 12, 8, 7, 18, 17, 14]), tree_node([18, 15, 17, 10, 12, None, 14, None, 5, None, 8, None, None, None, 3, None, 7, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 5, 2, 3, 15, 12, 8, 7, 18, 17, 14]), tree_node([18, 15, 17, 10, 12, None, 14, None, 5, None, 8, None, None, None, 3, None, 7, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [7, 5, 3, 2, 1, 0, 8, 6, 4]), tree_node([8, 7, 6, None, 5, None, 4, None, 3, None, None, None, 2, None, 1, None, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [7, 5, 3, 2, 1, 0, 8, 6, 4]), tree_node([8, 7, 6, None, 5, None, 4, None, 3, None, None, None, 2, None, 1, None, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 0, 3, 0, 1, 4, 3, 3, 0, 9, 2, 6, 1, 4, 8, 6, 7, 0, 1, 0, 3, 2, 9, 6, 2, 9, 8, 9, 6, 5, 9, 8, 9, 3, 0, 9, 1, 6, 9, 8, 9, 8, 6, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9]), tree_node([9, 5, 9, 4, None, 6, 9, 3, 1, 2, 5, 7, 9, None, 1, None, None, None, None, None, 5, None, None, 8, 9, None, None, 3, None, 3, 8, 8, 9, None, None, None, 3, 6, 7, 5, 8, 7, 9, 2, None, 4, 6, 3, None, None, 2, None, 4, None, 6, 3, 9, None, None, None, None, 2, 4, None, 2, 0, None, None, 1, 1, None, None, None, None, 9, None, None, None, 3, None, None, None, None, None, None, None, None, 8, 9, None, 3, 7, 2, 7, 9, None, None, 3, 5, None, 0, None, 4, 5, 9, None, None, None, 5, None, None, None, None, 4, None, 8, 9, 1, None, None, 4, 7, 8, 4, 9, None, 0, None, None, 3, None, 6, 6, 3, 3, 8, 9, None, None, 2, 0, 1, 6, None, 4, 0, 1, None, 3, 6, 7, 6, 9, None, None, None, None, None, None, 4, 2, 2, None, None, None, 0, None, None, 0, 2, 4, 6, 3, None, 2, 8, 9, None, 0, None, None, None, 0, None, None, None, None, None, None, 1, None, None, None, 1, 2, None, None, None, None, 6, 9, None, None, None, None, None, None, 0, 0, None, None, None, 5, 8, 9, None, None, None, None, None, None, None, None, 3, 9, None, 0, 6, 9, None, None, 1, None, 8, 9, None, None, None, None, 8, 9, None, 6, 7, 9, None, 5, None, None, 8, 9, None, None, 3, 8, 8, 9, None, 3, 6, 7, 5, 8, 7, 9, 2, None, 4, 6, 3, None, None, 2, None, 4, None, 6, 3, 9, None, None, None, None, 2, 4, None, 2, 0, None, None, 1, 1, None, None, None, None, 9, None, None, None, 3, None, None, None, None, None, None, None, None, 8, 9, None, 3, 7, 2, 7, 9, None, None, 3, 5, None, 0, None, 4, 5, None, None, None, None, 5, None, None, None, None, 4, None, 1, None, None, 4, None, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 0, 3, 0, 1, 4, 3, 3, 0, 9, 2, 6, 1, 4, 8, 6, 7, 0, 1, 0, 3, 2, 9, 6, 2, 9, 8, 9, 6, 5, 9, 8, 9, 3, 0, 9, 1, 6, 9, 8, 9, 8, 6, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9]), tree_node([9, 5, 9, 4, None, 6, 9, 3, 1, 2, 5, 7, 9, None, 1, None, None, None, None, None, 5, None, None, 8, 9, None, None, 3, None, 3, 8, 8, 9, None, None, None, 3, 6, 7, 5, 8, 7, 9, 2, None, 4, 6, 3, None, None, 2, None, 4, None, 6, 3, 9, None, None, None, None, 2, 4, None, 2, 0, None, None, 1, 1, None, None, None, None, 9, None, None, None, 3, None, None, None, None, None, None, None, None, 8, 9, None, 3, 7, 2, 7, 9, None, None, 3, 5, None, 0, None, 4, 5, 9, None, None, None, 5, None, None, None, None, 4, None, 8, 9, 1, None, None, 4, 7, 8, 4, 9, None, 0, None, None, 3, None, 6, 6, 3, 3, 8, 9, None, None, 2, 0, 1, 6, None, 4, 0, 1, None, 3, 6, 7, 6, 9, None, None, None, None, None, None, 4, 2, 2, None, None, None, 0, None, None, 0, 2, 4, 6, 3, None, 2, 8, 9, None, 0, None, None, None, 0, None, None, None, None, None, None, 1, None, None, None, 1, 2, None, None, None, None, 6, 9, None, None, None, None, None, None, 0, 0, None, None, None, 5, 8, 9, None, None, None, None, None, None, None, None, 3, 9, None, 0, 6, 9, None, None, 1, None, 8, 9, None, None, None, None, 8, 9, None, 6, 7, 9, None, 5, None, None, 8, 9, None, None, 3, 8, 8, 9, None, 3, 6, 7, 5, 8, 7, 9, 2, None, 4, 6, 3, None, None, 2, None, 4, None, 6, 3, 9, None, None, None, None, 2, 4, None, 2, 0, None, None, 1, 1, None, None, None, None, 9, None, None, None, 3, None, None, None, None, None, None, None, None, 8, 9, None, 3, 7, 2, 7, 9, None, None, 3, 5, None, 0, None, 4, 5, None, None, None, None, 5, None, None, None, None, 4, None, 1, None, None, 4, None, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]), tree_node([100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]), tree_node([100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), tree_node([50, 49, None, 48, None, 47, None, 46, None, 45, None, 44, None, 43, None, 42, None, 41, None, 40, None, 39, None, 38, None, 37, None, 36, None, 35, None, 34, None, 33, None, 32, None, 31, None, 30, None, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), tree_node([50, 49, None, 48, None, 47, None, 46, None, 45, None, 44, None, 43, None, 42, None, 41, None, 40, None, 39, None, 38, None, 37, None, 36, None, 35, None, 34, None, 33, None, 32, None, 31, None, 30, None, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 1, 5, 3, 7, 10, 2, 6, 4, 9]), tree_node([10, 8, 9, None, 7, 6, None, 5, None, 2, 4, 1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 1, 5, 3, 7, 10, 2, 6, 4, 9]), tree_node([10, 8, 9, None, 7, 6, None, 5, None, 2, 4, 1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 20, 15, 13, 18, 25, 22, 23, 24, 21, 19, 16, 17]), tree_node([25, 20, 24, 10, 18, 23, 21, None, None, 15, None, 22, None, None, 19, None, 13, None, None, None, 17, None, None, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 20, 15, 13, 18, 25, 22, 23, 24, 21, 19, 16, 17]), tree_node([25, 20, 24, 10, 18, 23, 21, None, None, 15, None, 22, None, None, 19, None, 13, None, None, None, 17, None, None, 16])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 15, 10, 20, 25, 18, 17, 16, 22, 21]), tree_node([25, 20, 22, 15, None, 18, 21, 5, 10, None, 17, None, None, None, None, None, None, None, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 15, 10, 20, 25, 18, 17, 16, 22, 21]), tree_node([25, 20, 22, 15, None, 18, 21, 5, 10, None, 17, None, None, None, None, None, None, None, 16])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [25, 15, 35, 10, 20, 30, 40, 5, 7, 12, 18, 22, 28, 32, 38, 1, 3, 6, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]), tree_node([40, 35, 39, 25, 30, 38, None, None, 15, 20, None, 32, 37, None, None, 10, None, 28, None, 33, None, None, None, 22, None, 31, None, 18, None, 29, None, 12, None, 27, None, 7, None, 23, None, 5, None, 21, None, None, None, 19, None, 17, None, 13, None, 11, None, 9, None, 6, None, 3, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [25, 15, 35, 10, 20, 30, 40, 5, 7, 12, 18, 22, 28, 32, 38, 1, 3, 6, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]), tree_node([40, 35, 39, 25, 30, 38, None, None, 15, 20, None, 32, 37, None, None, 10, None, 28, None, 33, None, None, None, 22, None, 31, None, 18, None, 29, None, 12, None, 27, None, 7, None, 23, None, 5, None, 21, None, None, None, 19, None, 17, None, 13, None, 11, None, 9, None, 6, None, 3, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [1, 5, 3, 4, 2, 6, 7, 8, 9, 0]), tree_node([9, 8, 0, 7, None, None, None, 6, None, 5, None, 1, 4, None, None, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [1, 5, 3, 4, 2, 6, 7, 8, 9, 0]), tree_node([9, 8, 0, 7, None, None, None, 6, None, 5, None, 1, 4, None, None, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [45, 30, 50, 20, 35, 40, 55, 25, 32, 37, 42, 52, 60, 28, 31, 33, 36, 39, 41, 43, 48, 51, 53, 58, 29, 34, 44, 46, 47, 54, 56, 57, 59]), tree_node([60, 55, 59, 50, 52, 58, None, 45, 40, 42, None, 53, 57, None, 30, 35, None, 37, None, 51, None, 56, None, None, None, 20, None, 32, None, 48, None, 54, None, None, None, 25, None, 43, None, 47, None, None, None, 41, None, 46, None, 39, None, 44, None, 36, None, 34, None, 33, None, 29, None, 31, None, None, None, 28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [45, 30, 50, 20, 35, 40, 55, 25, 32, 37, 42, 52, 60, 28, 31, 33, 36, 39, 41, 43, 48, 51, 53, 58, 29, 34, 44, 46, 47, 54, 56, 57, 59]), tree_node([60, 55, 59, 50, 52, 58, None, 45, 40, 42, None, 53, 57, None, 30, 35, None, 37, None, 51, None, 56, None, None, None, 20, None, 32, None, 48, None, 54, None, None, None, 25, None, 43, None, 47, None, None, None, 41, None, 46, None, 39, None, 44, None, 36, None, 34, None, 33, None, 29, None, 31, None, None, None, 28])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [500, 400, 300, 200, 100, 150, 250, 350, 450, 550]), tree_node([550, 500, None, None, 450, 400, None, None, 350, 300, None, None, 250, 200, None, None, 150, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [500, 400, 300, 200, 100, 150, 250, 350, 450, 550]), tree_node([550, 500, None, None, 450, 400, None, None, 350, 300, None, None, 250, 200, None, None, 150, 100])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [42, 41, 39, 40, 38, 37, 35, 36, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([42, None, 41, None, 40, 39, 38, None, None, None, 37, None, 36, 35, 34, None, None, None, 33, None, 32, None, 31, None, 30, None, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [42, 41, 39, 40, 38, 37, 35, 36, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([42, None, 41, None, 40, 39, 38, None, None, None, 37, None, 36, 35, 34, None, None, None, 33, None, 32, None, 31, None, 30, None, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 850, 750, 650, 550, 450, 350, 250, 150, 50]), tree_node([1000, 900, 950, 800, None, None, 850, 700, None, None, 750, 600, None, None, 650, 500, None, None, 550, 400, None, None, 450, 300, None, None, 350, 200, None, None, 250, 100, None, None, 150, None, None, None, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 850, 750, 650, 550, 450, 350, 250, 150, 50]), tree_node([1000, 900, 950, 800, None, None, 850, 700, None, None, 750, 600, None, None, 650, 500, None, None, 550, 400, None, None, 450, 300, None, None, 350, 200, None, None, 250, 100, None, None, 150, None, None, None, 50])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [25, 15, 35, 10, 20, 30, 40, 5, 25, 18, 32, 45, 7, 12, 28, 38, 50]), tree_node([50, 45, None, 40, 38, 35, 32, 28, None, 25, 30, 25, None, 12, None, None, 15, 20, None, 5, 18, 7, None, None, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [25, 15, 35, 10, 20, 30, 40, 5, 25, 18, 32, 45, 7, 12, 28, 38, 50]), tree_node([50, 45, None, 40, 38, 35, 32, 28, None, 25, 30, 25, None, 12, None, None, 15, 20, None, 5, 18, 7, None, None, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [6, 2, 8, 1, 3, 7, 5, 4, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, None, 8, 0, 6, 7, None, None, None, 2, 3, 5, None, None, 1, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [6, 2, 8, 1, 3, 7, 5, 4, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, None, 8, 0, 6, 7, None, None, None, 2, 3, 5, None, None, 1, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [150, 120, 180, 110, 130, 160, 190, 90, 100, 140, 170, 200, 80, 70, 115, 125, 135, 145, 155, 165, 175, 185, 195, 60, 50, 40, 30, 20, 10, 105, 95, 85]), tree_node([200, 190, 195, 180, 170, 185, 105, 150, 160, 140, None, 175, None, 60, 95, None, 120, 130, None, 100, None, 165, None, None, 50, None, 85, None, None, 110, None, 90, None, 155, None, None, 40, None, None, None, None, None, None, 145, None, None, 30, 135, None, None, 20, 125, None, None, 10, 115, None, None, None, 80, None, None, 70]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [150, 120, 180, 110, 130, 160, 190, 90, 100, 140, 170, 200, 80, 70, 115, 125, 135, 145, 155, 165, 175, 185, 195, 60, 50, 40, 30, 20, 10, 105, 95, 85]), tree_node([200, 190, 195, 180, 170, 185, 105, 150, 160, 140, None, 175, None, 60, 95, None, 120, 130, None, 100, None, 165, None, None, 50, None, 85, None, None, 110, None, 90, None, 155, None, None, 40, None, None, None, None, None, None, 145, None, None, 30, 135, None, None, 20, 125, None, None, 10, 115, None, None, None, 80, None, None, 70])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 1, 4, 3, 2, 6, 5, 7, 9, 0, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 9, None, 8, 0, None, 7, None, None, 6, None, 4, 5, 1, 3, None, None, None, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 1, 4, 3, 2, 6, 5, 7, 9, 0, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 9, None, 8, 0, None, 7, None, None, 6, None, 4, 5, 1, 3, None, None, None, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]), tree_node([15, 14, None, 12, 13, 8, 10, 11, None, None, 4, 6, None, 9, None, None, None, 2, None, 7, None, None, None, 5, None, 3, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]), tree_node([15, 14, None, 12, 13, 8, 10, 11, None, None, 4, 6, None, 9, None, None, None, 2, None, 7, None, None, None, 5, None, 3, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [10, 15, 20, 25, 30, 5, 9, 14, 19, 24, 29]), tree_node([30, 25, 29, 20, None, 24, None, 15, None, 19, None, 10, None, 14, None, None, None, 9, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [10, 15, 20, 25, 30, 5, 9, 14, 19, 24, 29]), tree_node([30, 25, 29, 20, None, 24, None, 15, None, 19, None, 10, None, 14, None, None, None, 9, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [5, 10, 3, 8, 1, 4, 6, 9, 2, 7]), tree_node([10, 5, 9, None, None, 8, 7, 3, 6, 2, None, None, None, 4, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [5, 10, 3, 8, 1, 4, 6, 9, 2, 7]), tree_node([10, 5, 9, None, None, 8, 7, 3, 6, 2, None, None, None, 4, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]), tree_node([100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10, None, 0, None, -10, None, -20, None, -30, None, -40, None, -50, None, -60, None, -70, None, -80, None, -90, None, -100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]), tree_node([100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10, None, 0, None, -10, None, -20, None, -30, None, -40, None, -50, None, -60, None, -70, None, -80, None, -90, None, -100])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(nums = [10, 5, 15, 2, 7, 12, 20]), tree_node([20, 15, None, 10, 12, None, 5, 7, None, None, None, 2]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), tree_node([10, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [1]), tree_node([1]))
    assert is_same_tree(candidate(nums = [1, 3, 2, 6, 5, 7, 4]), tree_node([7, 6, 4, 3, 5, None, None, 1, 2]))
    assert is_same_tree(candidate(nums = [1000, 999, 998, 997, 996]), tree_node([1000, None, 999, None, 998, None, 997, None, 996]))
    assert is_same_tree(candidate(nums = [2, 1, 3]), tree_node([3, 2, None, None, 1]))
    assert is_same_tree(candidate(nums = [10, 20, 30, 40, 50]), tree_node([50, 40, None, 30, None, 20, None, 10]))
    assert is_same_tree(candidate(nums = [3, 2, 1, 6, 0, 5]), tree_node([6, 3, 5, None, 2, 0, None, None, 1]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5]), tree_node([5, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [1, 3, 2, 5, 4, 7, 6]), tree_node([7, 5, 6, 3, 4, None, None, 1, 2]))
    assert is_same_tree(candidate(nums = [3, 2, 1, 6, 0, 5, 9, 8, 7]), tree_node([9, 6, 8, 3, 5, None, 7, None, 2, 0, None, None, None, None, 1]))
    assert is_same_tree(candidate(nums = [1, 3, 2]), tree_node([3, 1, 2]))
    assert is_same_tree(candidate(nums = [7, 5, 2, 6, 3, 1, 4]), tree_node([7, None, 6, 5, 4, None, 2, 3, None, None, None, None, 1]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 6, 5, 4, 9, 8, 7]), tree_node([9, 6, 8, 3, 5, None, 7, 2, None, None, 4, None, None, 1]))
    assert is_same_tree(candidate(nums = [3, 2, 1]), tree_node([3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [3, 1, 4, 2]), tree_node([4, 3, 2, None, 1]))
    assert is_same_tree(candidate(nums = [5, 4, 3, 2, 1]), tree_node([5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [1, 2, 3]), tree_node([3, 2, None, 1]))
    assert is_same_tree(candidate(nums = [3, 1, 2]), tree_node([3, None, 2, 1]))
    assert is_same_tree(candidate(nums = [50, 40, 30, 20, 10]), tree_node([50, None, 40, None, 30, None, 20, None, 10]))
    assert is_same_tree(candidate(nums = [12, 24, 18, 15, 30, 28, 26, 25, 27, 35, 32, 31, 33, 34]), tree_node([35, 30, 34, 24, 28, 33, None, 12, 18, None, 27, 32, None, None, None, None, 15, 26, None, None, 31, None, None, None, 25]))
    assert is_same_tree(candidate(nums = [3, 1, 2, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 19, 20]), tree_node([20, 19, None, 18, None, 15, 17, 12, 14, None, 16, 9, 11, None, 13, None, None, 6, 8, None, 10, None, None, 3, 5, None, 7, None, None, None, 2, None, 4, None, None, 1]))
    assert is_same_tree(candidate(nums = [34, 2, 78, 56, 90, 12, 3, 8, 5]), tree_node([90, 78, 12, 34, 56, None, 8, None, 2, None, None, 3, 5]))
    assert is_same_tree(candidate(nums = [2, 7, 11, 15, 3, 6, 7, 10, 1, 5, 4, 8, 12, 9]), tree_node([15, 11, 12, 7, None, 10, 9, 2, None, 7, 8, None, None, None, None, 6, None, 5, None, 3, None, 1, 4]))
    assert is_same_tree(candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]), tree_node([150, None, 140, None, 130, None, 120, None, 110, None, 100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
    assert is_same_tree(candidate(nums = [5, 50, 95, 60, 80, 30, 40, 70, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 90, 99]), tree_node([99, 95, None, 50, 90, 5, None, 85, None, None, None, 80, None, 60, 75, None, None, 70, None, 40, 65, 30, None, 55, None, None, None, 45, None, 35, None, 25, None, 20, None, None, 15, 10]))
    assert is_same_tree(candidate(nums = [2, 25, 1, 24, 3, 23, 4, 22, 5, 21, 6, 20, 7, 19, 8, 18, 9, 17, 10, 16, 11, 15, 12, 14, 13]), tree_node([25, 2, 24, None, None, 1, 23, None, None, 3, 22, None, None, 4, 21, None, None, 5, 20, None, None, 6, 19, None, None, 7, 18, None, None, 8, 17, None, None, 9, 16, None, None, 10, 15, None, None, 11, 14, None, None, 12, 13]))
    assert is_same_tree(candidate(nums = [42, 17, 13, 14, 35, 65, 23, 54, 78, 9, 11, 2, 3, 5, 7, 19, 21, 25, 30]), tree_node([78, 65, 30, 42, 54, 25, None, None, 35, 23, None, 21, None, 17, None, None, None, 19, None, None, 14, 11, None, 13, None, 9, 7, None, None, None, None, 5, None, 3, None, 2]))
    assert is_same_tree(candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [42, 53, 23, 78, 12, 34, 65, 89, 100, 56]), tree_node([100, 89, 56, 78, None, None, None, 53, 65, 42, 23, 34, None, None, None, None, None, 12]))
    assert is_same_tree(candidate(nums = [3, 5, 2, 4, 1, 6, 7, 8, 9, 10, 0]), tree_node([10, 9, 0, 8, None, None, None, 7, None, 6, None, 5, None, 3, 4, None, None, 2, 1]))
    assert is_same_tree(candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), tree_node([15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0]))
    assert is_same_tree(candidate(nums = [12, 5, 15, 3, 8, 18, 1, 4, 7, 11, 13, 17, 6, 2, 9, 14, 10, 16]), tree_node([18, 15, 17, 12, 8, 13, 16, None, 5, 3, None, 11, None, 14, None, None, None, None, None, 7, None, 9, 10, 4, None, 6, None, None, None, 1, None, None, 2]))
    assert is_same_tree(candidate(nums = [5, 8, 3, 9, 6, 2, 10, 7, 1, 4]), tree_node([10, 9, 7, 8, 6, None, 4, 5, 3, None, 2, 1]))
    assert is_same_tree(candidate(nums = [999, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25]), tree_node([999, None, 800, None, 700, None, 600, None, 500, None, 400, None, 300, None, 200, None, 100, None, 50, None, 25]))
    assert is_same_tree(candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [50, 30, 20, 40, 10, 60, 50, 70, 80, 15]), tree_node([80, 70, 15, 60, None, None, None, 50, 50, None, 40, None, None, 30, 10, None, 20]))
    assert is_same_tree(candidate(nums = [200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, 10, 30, 60, 90, 110, 130, 160, 180, 210, 230, 260, 280, 310, 330, 360, 380]), tree_node([380, 375, None, 350, 360, 300, 325, 330, None, 200, 250, 275, None, 310, None, None, 100, 150, None, 225, None, 280, None, None, None, 50, None, 175, None, 260, None, None, None, 125, None, 230, None, 75, None, 210, None, 25, None, 180, None, None, None, 160, None, 130, None, 110, None, 90, None, 60, None, 30, None, 10]))
    assert is_same_tree(candidate(nums = [99, 23, 77, 45, 67, 89, 12, 34, 56, 78, 90, 100, 110, 120, 130, 140, 150]), tree_node([150, 140, None, 130, None, 120, None, 110, None, 100, None, 99, None, None, 90, 89, None, 77, 78, 23, 67, 56, None, None, None, 45, None, 34, None, None, None, 12]))
    assert is_same_tree(candidate(nums = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9]), tree_node([1000, None, 950, None, 900, None, 850, None, 800, None, 750, None, 700, None, 650, None, 600, None, 550, None, 500, None, 450, None, 400, None, 350, None, 300, None, 250, None, 200, None, 150, None, 100, None, 50, None, 9, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [100, 20, 30, 40, 50, 60, 70, 80, 90, 10]), tree_node([100, None, 90, 80, 10, 70, None, None, None, 60, None, 50, None, 40, None, 30, None, 20]))
    assert is_same_tree(candidate(nums = [1, 6, 3, 5, 2, 4, 7, 10, 8, 9, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 10, None, 7, 9, 6, None, 8, None, 1, 5, None, None, None, None, 3, 4, None, None, 2]))
    assert is_same_tree(candidate(nums = [42, 17, 93, 31, 58, 72, 12, 67, 85, 29, 47, 63, 54, 81, 96, 50, 77, 21, 61, 88, 19, 35, 52, 69, 37, 74, 90, 24, 44, 59, 76, 40, 66, 84, 27, 48, 65, 82, 33, 49, 64, 83, 30, 45, 57, 73, 32, 43, 56, 71, 34, 46, 55, 70, 36, 41, 51, 68, 38, 39]), tree_node([96, 93, 90, 42, 85, 88, 84, None, 17, 72, 81, 77, 74, 76, 83, None, None, 58, 67, 63, None, 50, 61, 69, None, 59, 66, 82, 73, 31, None, 12, None, 47, 54, None, None, 21, None, 52, 37, 44, None, 40, None, 65, 64, 57, 71, None, None, None, None, 29, None, None, None, None, None, 35, None, None, None, 24, None, None, None, 48, None, 49, None, 45, None, 56, 70, None, None, 19, None, None, None, 27, None, 33, None, 30, None, 43, None, 55, 68, None, None, None, None, None, None, None, None, 32, None, 46, None, 51, 39, None, None, 34, None, 41, None, 38, None, None, None, 36]))
    assert is_same_tree(candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), tree_node([10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9, None, -10]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [8, 15, 3, 7, 9, 1, 20, 18, 17, 16, 14, 13]), tree_node([20, 15, 18, 8, 9, None, 17, None, None, 7, 1, None, 16, 3, None, None, None, None, 14, None, None, None, 13]))
    assert is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]), tree_node([1000, 900, 975, 800, None, 925, None, 700, None, 875, None, 600, None, 825, None, 500, None, 775, None, 400, None, 725, None, 300, None, 675, None, 200, None, 625, None, 100, None, 575, None, None, None, 525, None, 475, None, 425, None, 375, None, 325, None, 275, None, 225, None, 175, None, 125, None, 75, None, 50, None, None, 25]))
    assert is_same_tree(candidate(nums = [7, 4, 9, 1, 3, 8, 2, 5, 6]), tree_node([9, 7, 8, None, 4, 3, 6, None, None, 1, None, 5, None, None, None, 2]))
    assert is_same_tree(candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]), tree_node([9, 5, 9, 4, None, 6, None, 3, 1, 2, 5, None, 1, None, None, None, None, None, 5, None, None, 3]))
    assert is_same_tree(candidate(nums = [5, 8, 2, 1, 4, 6, 3, 9, 7, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, 7, 5, 6, None, 0, None, None, 4, 3, None, None, 2, None, None, None, None, 1]))
    assert is_same_tree(candidate(nums = [42, 3, 56, 23, 89, 12, 67, 45]), tree_node([89, 56, 67, 42, 23, 12, 45, None, 3]))
    assert is_same_tree(candidate(nums = [100, 90, 110, 80, 95, 105, 70, 85, 92, 98, 60, 75, 82, 88, 93, 97, 50, 65, 72, 78, 83, 87, 91, 94, 96, 40, 55, 62, 68, 73, 77, 81, 86, 90, 99, 30, 45, 52, 58, 63, 67, 71, 76, 84, 89, 20, 35, 42, 48, 53, 57, 61, 66, 74, 79, 85, 9, 18, 25, 32, 38, 43, 47, 51, 56, 60, 64, 69, 75, 80, 3, 12, 21, 27, 33, 37, 41, 46, 50, 55, 59, 63, 68, 72, 77, 82, 7, 15, 23, 29, 34, 38, 42, 45, 49, 54, 58, 62, 67, 71, 76, 1, 6, 11, 16, 22, 28, 32, 36, 40, 44, 48, 52, 57, 61, 66, 70, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]), tree_node([110, 100, 105, None, 90, 95, 99, None, None, 80, None, 98, 89, None, None, 92, 97, 84, 85, 85, None, 93, 96, 76, None, 79, 82, 70, None, 88, None, 94, 90, 71, None, 74, None, 80, 76, None, None, 82, None, 91, None, 86, None, 67, None, 66, None, 75, 77, 71, 70, 75, None, 87, None, 81, None, 63, None, 61, None, 69, None, 72, None, 67, None, 66, 70, 60, None, 83, None, 77, None, 58, None, 57, None, 64, None, 68, None, 62, None, 61, None, 65, None, None, None, 78, None, 73, None, 52, None, 53, None, 60, None, 63, None, 58, None, 57, None, 60, None, 72, None, 68, None, 45, None, 48, None, 56, None, 59, None, 54, None, 52, None, 55, None, 65, None, 62, None, 30, None, 42, None, 51, None, 55, None, 49, None, 48, None, 50, None, 50, None, 55, None, None, None, 35, None, 47, None, 50, None, 45, None, 44, None, 45, None, None, None, 40, None, 20, None, 43, None, 46, None, 42, None, 40, None, 40, None, None, None, None, None, 38, None, 41, None, 38, None, 36, None, 35, None, 32, None, 37, None, 34, None, 32, None, 30, None, 25, None, 33, None, 29, None, 28, None, 25, None, 18, None, 27, None, 23, None, 22, None, 20, None, 9, None, 21, None, 15, None, 16, None, 15, None, None, None, 12, None, 7, None, 11, None, 10, None, 3, None, None, None, 6, None, 5, None, None, None, 1, None, 0]))
    assert is_same_tree(candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), tree_node([20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0]))
    assert is_same_tree(candidate(nums = [7, 2, 9, 3, 5, 8, 1, 4, 6, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, None, 7, 8, None, 2, 5, 6, None, None, 3, None, 4, 0, None, None, 1]))
    assert is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16, 21, 30, 22, 29, 23, 28, 24, 27, 25, 26]), tree_node([30, 21, 29, 20, None, 22, 28, 11, 19, None, None, 23, 27, 10, None, 12, 18, None, None, 24, 26, 1, 9, None, None, 13, 17, None, None, 25, None, None, None, 2, 8, None, None, 14, 16, None, None, None, None, 3, 7, None, None, 15, None, None, None, 4, 6, None, None, None, None, 5]))
    assert is_same_tree(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]), tree_node([29, 27, None, 25, None, 23, None, 21, None, 19, None, 17, None, 15, None, 13, None, 11, None, 9, None, 7, None, 5, None, 3, None, 1]))
    assert is_same_tree(candidate(nums = [8, 5, 12, 1, 10, 2, 9, 3, 7, 4, 6, 11]), tree_node([12, 8, 11, None, 5, 10, None, None, None, 1, 9, None, None, 2, 7, None, None, 3, 6, None, None, 4]))
    assert is_same_tree(candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), tree_node([9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9, None, -10]))
    assert is_same_tree(candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989]), tree_node([999, None, 998, None, 997, None, 996, None, 995, None, 994, None, 993, None, 992, None, 991, None, 990, None, 989]))
    assert is_same_tree(candidate(nums = [50, 40, 30, 20, 10, 90, 80, 70, 60, 100]), tree_node([100, 90, None, 50, 80, None, 40, None, 70, None, 30, None, 60, None, 20, None, None, None, 10]))
    assert is_same_tree(candidate(nums = [5, 2, 7, 1, 8, 6, 4, 3, 9, 0, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, 10, 8, 0, None, None, 7, 6, None, None, 5, 1, None, 4, None, 2, None, None, None, 3]))
    assert is_same_tree(candidate(nums = [300, 200, 100, 250, 150, 50, 275, 225, 175, 125, 75, 325, 305, 255, 205, 155, 105, 350, 320, 290, 260, 230, 210, 180, 160, 130, 110, 80, 60, 40]), tree_node([350, 325, 320, 300, 305, None, 290, None, 275, None, 255, None, 260, 250, 225, None, 205, None, 230, 200, 150, None, 175, None, 155, None, 210, None, 100, None, 50, None, 125, None, 105, None, 180, None, None, None, None, None, 75, None, None, None, 160, None, None, None, 130, None, 110, None, 80, None, 60, None, 40]))
    assert is_same_tree(candidate(nums = [5, 9, 1, 8, 2, 7, 3, 6, 4]), tree_node([9, 5, 8, None, None, 1, 7, None, None, 2, 6, None, None, 3, 4]))
    assert is_same_tree(candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]), tree_node([305, 295, None, 285, None, 275, None, 265, None, 255, None, 245, None, 235, None, 225, None, 215, None, 205, None, 195, None, 185, None, 175, None, 165, None, 155, None, 145, None, 135, None, 125, None, 115, None, 105, None, 95, None, 85, None, 75, None, 65, None, 55, None, 45, None, 35, None, 25, None, 15, None, 5]))
    assert is_same_tree(candidate(nums = [45, 67, 23, 89, 12, 34, 56, 78, 90]), tree_node([90, 89, None, 67, 78, 45, 23, 56, None, None, None, None, None, 34, None, 12]))
    assert is_same_tree(candidate(nums = [50, 90, 30, 70, 20, 80, 10, 60, 40]), tree_node([90, 50, 80, None, None, 70, 60, 30, 20, 10, 40]))
    assert is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 1, 9, None, None, 2, 8, None, None, 3, 7, None, None, 4, 6, None, None, 5]))
    assert is_same_tree(candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]), tree_node([1024, 512, None, 256, None, 128, None, 64, None, 32, None, 16, None, 8, None, 4, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [7, 10, 4, 3, 20, 15, 9, 8, 6, 11, 18]), tree_node([20, 10, 18, 7, 4, 15, None, None, None, None, 3, None, 11, None, None, 9, None, None, 8, None, 6]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [50, 90, 30, 40, 70, 80, 20, 60, 10]), tree_node([90, 50, 80, None, None, 70, 60, 40, None, 20, 10, 30]))
    assert is_same_tree(candidate(nums = [42, 27, 61, 30, 19, 7, 5, 66, 39, 21, 22]), tree_node([66, 61, 39, 42, 30, None, 22, None, 27, None, 19, 21, None, None, None, None, 7, None, None, None, 5]))
    assert is_same_tree(candidate(nums = [1, 2, 4, 3, 7, 6, 5, 8, 9, 10, 12, 11, 14, 13, 15]), tree_node([15, 14, None, 12, 13, 10, 11, None, None, 9, None, None, None, 8, None, 7, None, 4, 6, 2, 3, None, 5, 1]))
    assert is_same_tree(candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]), tree_node([5, None, 4, None, 3, None, 2, None, 1, None, 0, None, -1, None, -2, None, -3, None, -4, None, -5]))
    assert is_same_tree(candidate(nums = [20, 50, 40, 30, 60, 90, 80, 70, 100]), tree_node([100, 90, None, 60, 80, 50, None, None, 70, 20, 40, None, None, None, None, None, 30]))
    assert is_same_tree(candidate(nums = [100, 10, 90, 9, 80, 8, 70, 7, 60, 6, 50, 5, 40, 4, 30, 3, 20, 2, 10, 1]), tree_node([100, None, 90, 10, 80, None, None, 9, 70, None, None, 8, 60, None, None, 7, 50, None, None, 6, 40, None, None, 5, 30, None, None, 4, 20, None, None, 3, 10, None, None, 2, 1]))
    assert is_same_tree(candidate(nums = [2, 1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]), tree_node([15, 13, 14, 11, 12, None, None, 9, 10, None, None, 7, 8, None, None, 5, 6, None, None, 3, 4, None, None, 2, None, None, None, None, 1]))
    assert is_same_tree(candidate(nums = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15]), tree_node([15, 14, None, 12, 13, 10, 11, None, None, 8, 9, None, None, 6, 7, None, None, 4, 5, None, None, 2, 3, None, None, 1]))
    assert is_same_tree(candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]), tree_node([9, 8, None, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, 0]))
    assert is_same_tree(candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]), tree_node([20, 15, 19, 10, 14, None, 18, 5, 9, None, 13, None, 17, None, 4, None, 8, None, 12, None, 16, None, 3, None, 7, None, 11, None, None, None, 2, None, 6, None, None, None, 1]))
    assert is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 5, 12, 22, 32, 42, 52, 60, 65, 70, 75, 80]), tree_node([80, 75, None, 70, None, 65, None, 60, None, 55, None, 50, 52, 40, 45, 42, None, 30, None, 35, None, 32, None, 20, None, 25, None, 22, None, 10, None, 15, None, 12, None, None, None, None, None, 5]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), tree_node([25, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), tree_node([100, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50]), tree_node([50, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 50, 150, 250, 350, 450, 5, 25, 125, 175, 225, 275, 325, 375, 425, 475]), tree_node([500, 400, 475, 300, None, 450, None, 200, None, 350, 425, 100, None, 250, None, 375, None, None, None, 150, None, 325, None, 50, None, 275, None, None, None, 225, None, 175, None, 125, None, 25, None, 5]))
    assert is_same_tree(candidate(nums = [50, 25, 75, 12, 38, 62, 88, 6, 18, 32, 46, 58, 70, 82, 94, 3, 9, 15, 21, 28, 34, 41, 48, 54, 60, 66, 72, 78, 84, 90, 96]), tree_node([96, 94, None, 88, 90, 75, 82, 84, None, 50, 62, 70, None, 78, None, None, 25, 38, None, 58, None, 72, None, None, None, 12, None, 46, None, 66, None, None, None, 32, None, 60, None, 18, None, 54, None, 6, None, 48, None, None, None, 41, None, 34, None, 28, None, 21, None, 15, None, 9, None, 3]))
    assert is_same_tree(candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), tree_node([30, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6]), tree_node([9, 5, 8, None, 1, 2, 7, None, None, None, None, 3, 6, None, None, 4]))
    assert is_same_tree(candidate(nums = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 70, 82, 93, 3, 9, 15, 21, 27, 34, 40, 49, 53, 61, 69, 76, 81, 88, 91, 95, 97]), tree_node([97, 95, None, 93, None, 87, 91, 75, 82, 88, None, 50, 62, 70, None, 81, None, None, 25, 37, None, 56, None, 76, None, None, None, 12, None, 43, None, 69, None, None, None, 31, None, 61, None, 18, None, 53, None, 6, None, 49, None, None, None, 40, None, 34, None, 27, None, 21, None, 15, None, 9, None, 3]))
    assert is_same_tree(candidate(nums = [8, 3, 10, 1, 6, 14, 4, 7, 13, 2, 9, 12, 11, 5]), tree_node([14, 10, 13, 8, 6, 7, 12, None, 3, 1, None, 4, None, 9, 11, None, None, None, None, None, None, 2, None, None, 5]))
    assert is_same_tree(candidate(nums = [15, 10, 18, 8, 12, 19, 13, 7, 9, 11, 14, 16, 17]), tree_node([19, 18, 17, 15, 12, 16, None, None, 10, 8, None, 14, None, None, None, None, None, 13, None, None, 11, 9, None, 7]))
    assert is_same_tree(candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]), tree_node([10, 1, 9, None, None, 2, 8, None, None, 3, 7, None, None, 4, 6, None, None, 5]))
    assert is_same_tree(candidate(nums = [1, 2, 4, 3, 7, 6, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 4, 6, 2, 3, None, 5, 1]))
    assert is_same_tree(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]), tree_node([150, 140, None, 130, None, 120, None, 110, None, 100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
    assert is_same_tree(candidate(nums = [10, 5, 2, 3, 15, 12, 8, 7, 18, 17, 14]), tree_node([18, 15, 17, 10, 12, None, 14, None, 5, None, 8, None, None, None, 3, None, 7, 2]))
    assert is_same_tree(candidate(nums = [7, 5, 3, 2, 1, 0, 8, 6, 4]), tree_node([8, 7, 6, None, 5, None, 4, None, 3, None, None, None, 2, None, 1, None, 0]))
    assert is_same_tree(candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 0, 3, 0, 1, 4, 3, 3, 0, 9, 2, 6, 1, 4, 8, 6, 7, 0, 1, 0, 3, 2, 9, 6, 2, 9, 8, 9, 6, 5, 9, 8, 9, 3, 0, 9, 1, 6, 9, 8, 9, 8, 6, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9]), tree_node([9, 5, 9, 4, None, 6, 9, 3, 1, 2, 5, 7, 9, None, 1, None, None, None, None, None, 5, None, None, 8, 9, None, None, 3, None, 3, 8, 8, 9, None, None, None, 3, 6, 7, 5, 8, 7, 9, 2, None, 4, 6, 3, None, None, 2, None, 4, None, 6, 3, 9, None, None, None, None, 2, 4, None, 2, 0, None, None, 1, 1, None, None, None, None, 9, None, None, None, 3, None, None, None, None, None, None, None, None, 8, 9, None, 3, 7, 2, 7, 9, None, None, 3, 5, None, 0, None, 4, 5, 9, None, None, None, 5, None, None, None, None, 4, None, 8, 9, 1, None, None, 4, 7, 8, 4, 9, None, 0, None, None, 3, None, 6, 6, 3, 3, 8, 9, None, None, 2, 0, 1, 6, None, 4, 0, 1, None, 3, 6, 7, 6, 9, None, None, None, None, None, None, 4, 2, 2, None, None, None, 0, None, None, 0, 2, 4, 6, 3, None, 2, 8, 9, None, 0, None, None, None, 0, None, None, None, None, None, None, 1, None, None, None, 1, 2, None, None, None, None, 6, 9, None, None, None, None, None, None, 0, 0, None, None, None, 5, 8, 9, None, None, None, None, None, None, None, None, 3, 9, None, 0, 6, 9, None, None, 1, None, 8, 9, None, None, None, None, 8, 9, None, 6, 7, 9, None, 5, None, None, 8, 9, None, None, 3, 8, 8, 9, None, 3, 6, 7, 5, 8, 7, 9, 2, None, 4, 6, 3, None, None, 2, None, 4, None, 6, 3, 9, None, None, None, None, 2, 4, None, 2, 0, None, None, 1, 1, None, None, None, None, 9, None, None, None, 3, None, None, None, None, None, None, None, None, 8, 9, None, 3, 7, 2, 7, 9, None, None, 3, 5, None, 0, None, 4, 5, None, None, None, None, 5, None, None, None, None, 4, None, 1, None, None, 4, None, 0]))
    assert is_same_tree(candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]), tree_node([100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10]))
    assert is_same_tree(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), tree_node([50, 49, None, 48, None, 47, None, 46, None, 45, None, 44, None, 43, None, 42, None, 41, None, 40, None, 39, None, 38, None, 37, None, 36, None, 35, None, 34, None, 33, None, 32, None, 31, None, 30, None, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [8, 1, 5, 3, 7, 10, 2, 6, 4, 9]), tree_node([10, 8, 9, None, 7, 6, None, 5, None, 2, 4, 1, 3]))
    assert is_same_tree(candidate(nums = [10, 20, 15, 13, 18, 25, 22, 23, 24, 21, 19, 16, 17]), tree_node([25, 20, 24, 10, 18, 23, 21, None, None, 15, None, 22, None, None, 19, None, 13, None, None, None, 17, None, None, 16]))
    assert is_same_tree(candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [5, 15, 10, 20, 25, 18, 17, 16, 22, 21]), tree_node([25, 20, 22, 15, None, 18, 21, 5, 10, None, 17, None, None, None, None, None, None, None, 16]))
    assert is_same_tree(candidate(nums = [25, 15, 35, 10, 20, 30, 40, 5, 7, 12, 18, 22, 28, 32, 38, 1, 3, 6, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]), tree_node([40, 35, 39, 25, 30, 38, None, None, 15, 20, None, 32, 37, None, None, 10, None, 28, None, 33, None, None, None, 22, None, 31, None, 18, None, 29, None, 12, None, 27, None, 7, None, 23, None, 5, None, 21, None, None, None, 19, None, 17, None, 13, None, 11, None, 9, None, 6, None, 3, None, 1]))
    assert is_same_tree(candidate(nums = [1, 5, 3, 4, 2, 6, 7, 8, 9, 0]), tree_node([9, 8, 0, 7, None, None, None, 6, None, 5, None, 1, 4, None, None, 3, 2]))
    assert is_same_tree(candidate(nums = [45, 30, 50, 20, 35, 40, 55, 25, 32, 37, 42, 52, 60, 28, 31, 33, 36, 39, 41, 43, 48, 51, 53, 58, 29, 34, 44, 46, 47, 54, 56, 57, 59]), tree_node([60, 55, 59, 50, 52, 58, None, 45, 40, 42, None, 53, 57, None, 30, 35, None, 37, None, 51, None, 56, None, None, None, 20, None, 32, None, 48, None, 54, None, None, None, 25, None, 43, None, 47, None, None, None, 41, None, 46, None, 39, None, 44, None, 36, None, 34, None, 33, None, 29, None, 31, None, None, None, 28]))
    assert is_same_tree(candidate(nums = [500, 400, 300, 200, 100, 150, 250, 350, 450, 550]), tree_node([550, 500, None, None, 450, 400, None, None, 350, 300, None, None, 250, 200, None, None, 150, 100]))
    assert is_same_tree(candidate(nums = [42, 41, 39, 40, 38, 37, 35, 36, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), tree_node([42, None, 41, None, 40, 39, 38, None, None, None, 37, None, 36, 35, 34, None, None, None, 33, None, 32, None, 31, None, 30, None, 29, None, 28, None, 27, None, 26, None, 25, None, 24, None, 23, None, 22, None, 21, None, 20, None, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 10, None, 9, None, 8, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]))
    assert is_same_tree(candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 850, 750, 650, 550, 450, 350, 250, 150, 50]), tree_node([1000, 900, 950, 800, None, None, 850, 700, None, None, 750, 600, None, None, 650, 500, None, None, 550, 400, None, None, 450, 300, None, None, 350, 200, None, None, 250, 100, None, None, 150, None, None, None, 50]))
    assert is_same_tree(candidate(nums = [25, 15, 35, 10, 20, 30, 40, 5, 25, 18, 32, 45, 7, 12, 28, 38, 50]), tree_node([50, 45, None, 40, 38, 35, 32, 28, None, 25, 30, 25, None, 12, None, None, 15, 20, None, 5, 18, 7, None, None, None, 10]))
    assert is_same_tree(candidate(nums = [6, 2, 8, 1, 3, 7, 5, 4, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), tree_node([20, 19, None, 18, None, 17, None, 16, None, 15, None, 14, None, 13, None, 12, None, 11, None, 9, None, 8, 0, 6, 7, None, None, None, 2, 3, 5, None, None, 1, None, None, 4]))
    assert is_same_tree(candidate(nums = [150, 120, 180, 110, 130, 160, 190, 90, 100, 140, 170, 200, 80, 70, 115, 125, 135, 145, 155, 165, 175, 185, 195, 60, 50, 40, 30, 20, 10, 105, 95, 85]), tree_node([200, 190, 195, 180, 170, 185, 105, 150, 160, 140, None, 175, None, 60, 95, None, 120, 130, None, 100, None, 165, None, None, 50, None, 85, None, None, 110, None, 90, None, 155, None, None, 40, None, None, None, None, None, None, 145, None, None, 30, 135, None, None, 20, 125, None, None, 10, 115, None, None, None, 80, None, None, 70]))
    assert is_same_tree(candidate(nums = [8, 1, 4, 3, 2, 6, 5, 7, 9, 0, 11, 12, 13, 14, 15]), tree_node([15, 14, None, 13, None, 12, None, 11, None, 9, None, 8, 0, None, 7, None, None, 6, None, 4, 5, 1, 3, None, None, None, None, None, 2]))
    assert is_same_tree(candidate(nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]), tree_node([15, 14, None, 12, 13, 8, 10, 11, None, None, 4, 6, None, 9, None, None, None, 2, None, 7, None, None, None, 5, None, 3, None, 1]))
    assert is_same_tree(candidate(nums = [10, 15, 20, 25, 30, 5, 9, 14, 19, 24, 29]), tree_node([30, 25, 29, 20, None, 24, None, 15, None, 19, None, 10, None, 14, None, None, None, 9, None, 5]))
    assert is_same_tree(candidate(nums = [5, 10, 3, 8, 1, 4, 6, 9, 2, 7]), tree_node([10, 5, 9, None, None, 8, 7, 3, 6, 2, None, None, None, 4, None, None, None, 1]))
    assert is_same_tree(candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]), tree_node([100, None, 90, None, 80, None, 70, None, 60, None, 50, None, 40, None, 30, None, 20, None, 10, None, 0, None, -10, None, -20, None, -30, None, -40, None, -50, None, -60, None, -70, None, -80, None, -90, None, -100]))


