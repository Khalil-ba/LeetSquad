def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]), tree_node([1, 2, None, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]), tree_node([1, 2, None, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]), tree_node([50, 20, 80, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]), tree_node([50, 20, 80, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [3, 1, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0]]), tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [3, 1, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0]]), tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [1, 3, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [6, 12, 1], [6, 13, 0], [7, 14, 1], [7, 15, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [1, 3, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [6, 12, 1], [6, 13, 0], [7, 14, 1], [7, 15, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[99, 98, 1], [98, 97, 1], [97, 96, 1], [96, 95, 1], [95, 94, 1], [94, 93, 1], [93, 92, 1], [92, 91, 1], [91, 90, 1], [90, 89, 1], [89, 88, 1], [88, 87, 1], [87, 86, 1], [86, 85, 1]]), tree_node([99, 98, None, 97, None, 96, None, 95, None, 94, None, 93, None, 92, None, 91, None, 90, None, 89, None, 88, None, 87, None, 86, None, 85]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[99, 98, 1], [98, 97, 1], [97, 96, 1], [96, 95, 1], [95, 94, 1], [94, 93, 1], [93, 92, 1], [92, 91, 1], [91, 90, 1], [90, 89, 1], [89, 88, 1], [88, 87, 1], [87, 86, 1], [86, 85, 1]]), tree_node([99, 98, None, 97, None, 96, None, 95, None, 94, None, 93, None, 92, None, 91, None, 90, None, 89, None, 88, None, 87, None, 86, None, 85])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [4, 8, 1], [8, 16, 1], [16, 32, 1], [32, 64, 1], [64, 128, 1], [1, 3, 0], [3, 5, 1], [5, 9, 1], [9, 17, 1], [17, 33, 1], [33, 65, 1], [65, 129, 1], [1, 6, 0], [6, 10, 1], [10, 18, 1], [18, 34, 1], [34, 66, 1], [66, 130, 1], [1, 7, 0], [7, 11, 1], [11, 19, 1], [19, 35, 1], [35, 67, 1], [67, 131, 1], [1, 8, 0], [8, 12, 1], [12, 20, 1], [20, 36, 1], [36, 68, 1], [68, 132, 1], [1, 9, 0], [9, 13, 1], [13, 21, 1], [21, 37, 1], [37, 69, 1], [69, 133, 1], [1, 10, 0], [10, 14, 1], [14, 22, 1], [22, 38, 1], [38, 70, 1], [70, 134, 1]]), tree_node([1, 2, 10, 4, None, 14, None, 8, None, 22, None, 12, None, 38, None, 20, None, 70, None, 36, None, 134, None, 68, None, None, None, 132]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [4, 8, 1], [8, 16, 1], [16, 32, 1], [32, 64, 1], [64, 128, 1], [1, 3, 0], [3, 5, 1], [5, 9, 1], [9, 17, 1], [17, 33, 1], [33, 65, 1], [65, 129, 1], [1, 6, 0], [6, 10, 1], [10, 18, 1], [18, 34, 1], [34, 66, 1], [66, 130, 1], [1, 7, 0], [7, 11, 1], [11, 19, 1], [19, 35, 1], [35, 67, 1], [67, 131, 1], [1, 8, 0], [8, 12, 1], [12, 20, 1], [20, 36, 1], [36, 68, 1], [68, 132, 1], [1, 9, 0], [9, 13, 1], [13, 21, 1], [21, 37, 1], [37, 69, 1], [69, 133, 1], [1, 10, 0], [10, 14, 1], [14, 22, 1], [22, 38, 1], [38, 70, 1], [70, 134, 1]]), tree_node([1, 2, 10, 4, None, 14, None, 8, None, 22, None, 12, None, 38, None, 20, None, 70, None, 36, None, 134, None, 68, None, None, None, 132])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[2, 1, 1], [2, 3, 0], [3, 6, 0], [6, 12, 0], [12, 24, 0], [24, 48, 0], [48, 96, 0], [96, 192, 0], [192, 384, 0], [384, 768, 0]]), tree_node([2, 1, 3, None, None, None, 6, None, 12, None, 24, None, 48, None, 96, None, 192, None, 384, None, 768]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[2, 1, 1], [2, 3, 0], [3, 6, 0], [6, 12, 0], [12, 24, 0], [24, 48, 0], [48, 96, 0], [96, 192, 0], [192, 384, 0], [384, 768, 0]]), tree_node([2, 1, 3, None, None, None, 6, None, 12, None, 24, None, 48, None, 96, None, 192, None, 384, None, 768])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [2, 5, 0], [1, 3, 0], [3, 6, 1], [3, 7, 0], [7, 14, 1], [7, 15, 0], [15, 30, 1], [15, 31, 0], [31, 62, 1], [31, 63, 0], [63, 126, 1], [63, 127, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 14, 15, None, None, 30, 31, None, None, 62, 63, None, None, 126, 127]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [2, 5, 0], [1, 3, 0], [3, 6, 1], [3, 7, 0], [7, 14, 1], [7, 15, 0], [15, 30, 1], [15, 31, 0], [31, 62, 1], [31, 63, 0], [63, 126, 1], [63, 127, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 14, 15, None, None, 30, 31, None, None, 62, 63, None, None, 126, 127])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1000, 500, 1], [500, 250, 1], [500, 750, 0], [1000, 1500, 0], [1500, 1250, 1], [1500, 1750, 0], [1750, 1600, 1], [1750, 1800, 0], [1800, 1775, 1], [1800, 1825, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, None, None, None, None, 1600, 1800, None, None, 1775, 1825]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1000, 500, 1], [500, 250, 1], [500, 750, 0], [1000, 1500, 0], [1500, 1250, 1], [1500, 1750, 0], [1750, 1600, 1], [1750, 1800, 0], [1800, 1775, 1], [1800, 1825, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, None, None, None, None, 1600, 1800, None, None, 1775, 1825])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [2, 5, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [1, 3, 0], [3, 6, 1], [3, 7, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [2, 5, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [1, 3, 0], [3, 6, 1], [3, 7, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [750, 375, 1], [750, 1125, 0], [1250, 625, 1], [1250, 937, 0], [1750, 1562, 1], [1750, 1875, 0], [375, 187, 1], [375, 562, 0], [1125, 843, 1], [1125, 1406, 0], [625, 312, 1], [625, 468, 0], [937, 468, 1], [937, 703, 0], [1562, 781, 1], [1562, 1281, 0], [1875, 937, 1], [1875, 938, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, 375, 1125, 625, 937, 1562, 1875, 187, 562, 843, 1406, 312, 468, 468, 703, 781, 1281, 937, 938, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 468, 703]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [750, 375, 1], [750, 1125, 0], [1250, 625, 1], [1250, 937, 0], [1750, 1562, 1], [1750, 1875, 0], [375, 187, 1], [375, 562, 0], [1125, 843, 1], [1125, 1406, 0], [625, 312, 1], [625, 468, 0], [937, 468, 1], [937, 703, 0], [1562, 781, 1], [1562, 1281, 0], [1875, 937, 1], [1875, 938, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, 375, 1125, 625, 937, 1562, 1875, 187, 562, 843, 1406, 312, 468, 468, 703, 781, 1281, 937, 938, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 468, 703])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 8, 0], [3, 2, 1], [3, 4, 0], [8, 7, 1], [8, 9, 0], [4, 6, 0], [9, 10, 1]]), tree_node([5, 3, 8, 2, 4, 7, 9, None, None, None, 6, None, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 8, 0], [3, 2, 1], [3, 4, 0], [8, 7, 1], [8, 9, 0], [4, 6, 0], [9, 10, 1]]), tree_node([5, 3, 8, 2, 4, 7, 9, None, None, None, 6, None, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[60, 30, 1], [60, 90, 0], [30, 15, 1], [30, 45, 0], [45, 40, 1], [45, 50, 0], [90, 75, 1], [90, 105, 0], [105, 100, 1], [105, 110, 0]]), tree_node([60, 30, 90, 15, 45, 75, 105, None, None, 40, 50, None, None, 100, 110]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[60, 30, 1], [60, 90, 0], [30, 15, 1], [30, 45, 0], [45, 40, 1], [45, 50, 0], [90, 75, 1], [90, 105, 0], [105, 100, 1], [105, 110, 0]]), tree_node([60, 30, 90, 15, 45, 75, 105, None, None, 40, 50, None, None, 100, 110])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 160, 1], [175, 190, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, 160, 190]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 160, 1], [175, 190, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, 160, 190])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 45, 0], [10, 5, 1], [10, 15, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, 5, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 45, 0], [10, 5, 1], [10, 15, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, 5, 15])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [1250, 1125, 1], [1250, 1375, 0], [1750, 1625, 1], [1750, 1875, 0], [1875, 1825, 1], [1875, 1925, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, None, None, 1125, 1375, 1625, 1875, None, None, None, None, None, None, 1825, 1925]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [1250, 1125, 1], [1250, 1375, 0], [1750, 1625, 1], [1750, 1875, 0], [1875, 1825, 1], [1875, 1925, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, None, None, 1125, 1375, 1625, 1875, None, None, None, None, None, None, 1825, 1925])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 200, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, None, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 200, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, None, 200])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[99, 88, 1], [99, 77, 0], [88, 66, 1], [88, 55, 0], [77, 44, 1], [77, 33, 0], [66, 22, 1], [66, 11, 0], [55, 9, 1], [55, 8, 0], [44, 7, 1], [44, 6, 0], [33, 5, 1], [33, 4, 0], [22, 3, 1], [22, 2, 0], [11, 1, 1], [11, 0, 0]]), tree_node([99, 88, 77, 66, 55, 44, 33, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[99, 88, 1], [99, 77, 0], [88, 66, 1], [88, 55, 0], [77, 44, 1], [77, 33, 0], [66, 22, 1], [66, 11, 0], [55, 9, 1], [55, 8, 0], [44, 7, 1], [44, 6, 0], [33, 5, 1], [33, 4, 0], [22, 3, 1], [22, 2, 0], [11, 1, 1], [11, 0, 0]]), tree_node([99, 88, 77, 66, 55, 44, 33, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[25, 10, 1], [25, 30, 0], [10, 5, 1], [10, 15, 0], [30, 28, 1], [30, 32, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [28, 26, 1], [28, 29, 0], [32, 31, 1], [32, 33, 0]]), tree_node([25, 10, 30, 5, 15, 28, 32, 3, 7, 12, 18, 26, 29, 31, 33]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[25, 10, 1], [25, 30, 0], [10, 5, 1], [10, 15, 0], [30, 28, 1], [30, 32, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [28, 26, 1], [28, 29, 0], [32, 31, 1], [32, 33, 0]]), tree_node([25, 10, 30, 5, 15, 28, 32, 3, 7, 12, 18, 26, 29, 31, 33])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [3, 5, 1], [3, 4, 0], [5, 7, 1], [5, 6, 0], [7, 11, 1], [7, 8, 0], [8, 9, 1], [8, 10, 0]]), tree_node([1, 3, 2, 5, 4, None, None, 7, 6, None, None, 11, 8, None, None, None, None, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [3, 5, 1], [3, 4, 0], [5, 7, 1], [5, 6, 0], [7, 11, 1], [7, 8, 0], [8, 9, 1], [8, 10, 0]]), tree_node([1, 3, 2, 5, 4, None, None, 7, 6, None, None, 11, 8, None, None, None, None, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [75, 60, 0], [175, 180, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, 60, None, None, None, 180]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [75, 60, 0], [175, 180, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, 60, None, None, None, 180])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[200, 100, 1], [200, 300, 0], [100, 50, 1], [100, 150, 0], [300, 250, 1], [300, 350, 0], [150, 125, 1], [150, 175, 0], [350, 325, 1], [350, 375, 0]]), tree_node([200, 100, 300, 50, 150, 250, 350, None, None, 125, 175, None, None, 325, 375]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[200, 100, 1], [200, 300, 0], [100, 50, 1], [100, 150, 0], [300, 250, 1], [300, 350, 0], [150, 125, 1], [150, 175, 0], [350, 325, 1], [350, 375, 0]]), tree_node([200, 100, 300, 50, 150, 250, 350, None, None, 125, 175, None, None, 325, 375])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 50, 0], [50, 45, 1], [50, 55, 0]]), tree_node([30, 20, 40, 10, 25, 35, 50, None, None, None, None, None, None, 45, 55]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 50, 0], [50, 45, 1], [50, 55, 0]]), tree_node([30, 20, 40, 10, 25, 35, 50, None, None, None, None, None, None, 45, 55])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [18, 17, 1], [18, 19, 0], [19, 16, 0], [19, 20, 1]]), tree_node([10, 5, 15, 3, 7, 12, 18, None, None, None, None, None, None, 17, 19, None, None, 20, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [18, 17, 1], [18, 19, 0], [19, 16, 0], [19, 20, 1]]), tree_node([10, 5, 15, 3, 7, 12, 18, None, None, None, None, None, None, 17, 19, None, None, 20, 16])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [25, 10, 1], [75, 60, 0], [125, 110, 0], [175, 190, 1]]), tree_node([100, 50, 150, 25, 75, 125, 175, 10, None, None, 60, None, 110, 190]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [25, 10, 1], [75, 60, 0], [125, 110, 0], [175, 190, 1]]), tree_node([100, 50, 150, 25, 75, 125, 175, 10, None, None, 60, None, 110, 190])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[8, 4, 1], [8, 12, 0], [4, 2, 1], [4, 6, 0], [12, 10, 1], [12, 14, 0], [2, 1, 1], [2, 3, 0], [6, 5, 1], [6, 7, 0]]), tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[8, 4, 1], [8, 12, 0], [4, 2, 1], [4, 6, 0], [12, 10, 1], [12, 14, 0], [2, 1, 1], [2, 3, 0], [6, 5, 1], [6, 7, 0]]), tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[99, 66, 1], [66, 33, 1], [33, 16, 1], [16, 8, 1], [8, 4, 1], [4, 2, 1], [2, 1, 1], [99, 77, 0], [77, 55, 0], [55, 38, 0], [38, 19, 0], [19, 9, 0], [9, 4, 0], [4, 2, 0], [99, 88, 0], [88, 55, 1], [55, 34, 1], [34, 17, 1], [17, 8, 0]]), tree_node([99, 66, 88, 33, None, 55, None, 16, None, 34, 38, 8, None, 17, None, None, 19, 4, None, None, 8, None, 9, 2, 2, 4, None, None, 4, 1, None, 1, None, 2, 2, 2, 2, None, None, None, None, 1, None, 1, None, 1, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[99, 66, 1], [66, 33, 1], [33, 16, 1], [16, 8, 1], [8, 4, 1], [4, 2, 1], [2, 1, 1], [99, 77, 0], [77, 55, 0], [55, 38, 0], [38, 19, 0], [19, 9, 0], [9, 4, 0], [4, 2, 0], [99, 88, 0], [88, 55, 1], [55, 34, 1], [34, 17, 1], [17, 8, 0]]), tree_node([99, 66, 88, 33, None, 55, None, 16, None, 34, 38, 8, None, 17, None, None, 19, 4, None, None, 8, None, 9, 2, 2, 4, None, None, 4, 1, None, 1, None, 2, 2, 2, 2, None, None, None, None, 1, None, 1, None, 1, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [25, 10, 1], [25, 40, 0], [75, 60, 1], [75, 85, 0], [125, 110, 1], [125, 135, 0], [175, 160, 1], [175, 185, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 85, 110, 135, 160, 185]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [25, 10, 1], [25, 40, 0], [75, 60, 1], [75, 85, 0], [125, 110, 1], [125, 135, 0], [175, 160, 1], [175, 185, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 85, 110, 135, 160, 185])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 2, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [2, 1, 1], [4, 9, 0], [9, 10, 1]]), tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, 9, None, None, None, None, None, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 2, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [2, 1, 1], [4, 9, 0], [9, 10, 1]]), tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, 9, None, None, None, None, None, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[30, 20, 1], [20, 10, 1], [20, 25, 0], [30, 40, 0], [40, 35, 1], [40, 45, 0], [35, 32, 1], [35, 37, 0], [45, 42, 1], [45, 47, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, None, None, None, None, 32, 37, 42, 47]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[30, 20, 1], [20, 10, 1], [20, 25, 0], [30, 40, 0], [40, 35, 1], [40, 45, 0], [35, 32, 1], [35, 37, 0], [45, 42, 1], [45, 47, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, None, None, None, None, 32, 37, 42, 47])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 1, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [8, 9, 1], [9, 10, 0], [10, 11, 1], [11, 12, 0], [12, 13, 1]]), tree_node([5, 3, 7, 1, 4, 6, 8, None, None, None, None, None, None, 9, None, None, 10, 11, None, None, 12, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 1, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [8, 9, 1], [9, 10, 0], [10, 11, 1], [11, 12, 0], [12, 13, 1]]), tree_node([5, 3, 7, 1, 4, 6, 8, None, None, None, None, None, None, 9, None, None, 10, 11, None, None, 12, 13])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [6, 12, 1], [6, 13, 0], [7, 14, 1], [7, 15, 0], [8, 16, 1], [8, 17, 0], [9, 18, 1], [9, 19, 0]]), tree_node([1, 3, 2, 6, 7, 4, 5, 12, 13, 14, 15, 8, 9, 10, 11, None, None, None, None, None, None, None, None, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [6, 12, 1], [6, 13, 0], [7, 14, 1], [7, 15, 0], [8, 16, 1], [8, 17, 0], [9, 18, 1], [9, 19, 0]]), tree_node([1, 3, 2, 6, 7, 4, 5, 12, 13, 14, 15, 8, 9, 10, 11, None, None, None, None, None, None, None, None, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0]]), tree_node([10, 5, 15, 3, 7, 12, 18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0]]), tree_node([10, 5, 15, 3, 7, 12, 18])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[500, 250, 1], [500, 750, 0], [250, 125, 1], [250, 375, 0], [750, 625, 1], [750, 875, 0], [125, 60, 1], [125, 180, 0], [375, 290, 1], [375, 440, 0], [625, 550, 1], [625, 680, 0], [875, 800, 1], [875, 940, 0]]), tree_node([500, 250, 750, 125, 375, 625, 875, 60, 180, 290, 440, 550, 680, 800, 940]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[500, 250, 1], [500, 750, 0], [250, 125, 1], [250, 375, 0], [750, 625, 1], [750, 875, 0], [125, 60, 1], [125, 180, 0], [375, 290, 1], [375, 440, 0], [625, 550, 1], [625, 680, 0], [875, 800, 1], [875, 940, 0]]), tree_node([500, 250, 750, 125, 375, 625, 875, 60, 180, 290, 440, 550, 680, 800, 940])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[5, 4, 1], [5, 6, 0], [4, 3, 1], [4, 2, 0], [6, 7, 1], [6, 8, 0], [7, 9, 1], [7, 10, 0], [8, 11, 1], [8, 12, 0], [9, 13, 1], [9, 14, 0], [10, 15, 1], [10, 16, 0], [11, 17, 1], [11, 18, 0], [12, 19, 1], [12, 20, 0], [13, 21, 1], [13, 22, 0], [14, 23, 1], [14, 24, 0], [15, 25, 1], [15, 26, 0], [16, 27, 1], [16, 28, 0]]), tree_node([5, 4, 6, 3, 2, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[5, 4, 1], [5, 6, 0], [4, 3, 1], [4, 2, 0], [6, 7, 1], [6, 8, 0], [7, 9, 1], [7, 10, 0], [8, 11, 1], [8, 12, 0], [9, 13, 1], [9, 14, 0], [10, 15, 1], [10, 16, 0], [11, 17, 1], [11, 18, 0], [12, 19, 1], [12, 20, 0], [13, 21, 1], [13, 22, 0], [14, 23, 1], [14, 24, 0], [15, 25, 1], [15, 26, 0], [16, 27, 1], [16, 28, 0]]), tree_node([5, 4, 6, 3, 2, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[7, 3, 1], [7, 10, 0], [3, 1, 1], [3, 5, 0], [10, 8, 1], [10, 12, 0], [5, 4, 0], [5, 6, 1], [8, 9, 1], [12, 11, 0]]), tree_node([7, 3, 10, 1, 5, 8, 12, None, None, 6, 4, 9, None, None, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[7, 3, 1], [7, 10, 0], [3, 1, 1], [3, 5, 0], [10, 8, 1], [10, 12, 0], [5, 4, 0], [5, 6, 1], [8, 9, 1], [12, 11, 0]]), tree_node([7, 3, 10, 1, 5, 8, 12, None, None, 6, 4, 9, None, None, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[60, 30, 1], [60, 90, 0], [30, 15, 1], [30, 45, 0], [90, 75, 1], [90, 105, 0], [15, 10, 1], [15, 20, 0], [45, 35, 1], [45, 50, 0], [75, 65, 1], [75, 85, 0], [105, 100, 1], [105, 110, 0]]), tree_node([60, 30, 90, 15, 45, 75, 105, 10, 20, 35, 50, 65, 85, 100, 110]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[60, 30, 1], [60, 90, 0], [30, 15, 1], [30, 45, 0], [90, 75, 1], [90, 105, 0], [15, 10, 1], [15, 20, 0], [45, 35, 1], [45, 50, 0], [75, 65, 1], [75, 85, 0], [105, 100, 1], [105, 110, 0]]), tree_node([60, 30, 90, 15, 45, 75, 105, 10, 20, 35, 50, 65, 85, 100, 110])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 2, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [2, 1, 1], [4, 9, 0], [6, 11, 1], [8, 13, 0], [1, 0, 1], [9, 12, 0], [11, 10, 0], [13, 14, 1]]), tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, 9, 11, None, None, 13, 0, None, None, 12, None, 10, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 2, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [2, 1, 1], [4, 9, 0], [6, 11, 1], [8, 13, 0], [1, 0, 1], [9, 12, 0], [11, 10, 0], [13, 14, 1]]), tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, 9, 11, None, None, 13, 0, None, None, 12, None, 10, 14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [75, 60, 1], [75, 90, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, 60, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [75, 60, 1], [75, 90, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, 60, 90])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 160, 1]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, 160]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 160, 1]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, 160])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [250, 100, 1], [750, 600, 0], [1250, 1100, 0], [1750, 1900, 1], [100, 50, 1], [600, 550, 0], [1100, 1050, 0], [1900, 1850, 1]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 100, None, None, 600, None, 1100, 1900, None, 50, None, None, 550, None, 1050, 1850]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [250, 100, 1], [750, 600, 0], [1250, 1100, 0], [1750, 1900, 1], [100, 50, 1], [600, 550, 0], [1100, 1050, 0], [1900, 1850, 1]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 100, None, None, 600, None, 1100, 1900, None, 50, None, None, 550, None, 1050, 1850])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 45, 0], [10, 5, 1], [25, 15, 0], [35, 32, 1], [45, 47, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, 5, None, None, 15, 32, None, None, 47]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 45, 0], [10, 5, 1], [25, 15, 0], [35, 32, 1], [45, 47, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, 5, None, None, 15, 32, None, None, 47])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[30, 20, 1], [20, 10, 1], [10, 5, 1], [5, 2, 1], [30, 40, 0], [40, 50, 0], [50, 60, 0]]), tree_node([30, 20, 40, 10, None, None, 50, 5, None, None, 60, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[30, 20, 1], [20, 10, 1], [10, 5, 1], [5, 2, 1], [30, 40, 0], [40, 50, 0], [50, 60, 0]]), tree_node([30, 20, 40, 10, None, None, 50, 5, None, None, 60, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0]]), tree_node([1, 3, 2, 6, 7, 4, 5, None, None, None, None, 8, 9, 10, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0]]), tree_node([1, 3, 2, 6, 7, 4, 5, None, None, None, None, 8, 9, 10, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1], [11, 12, 1], [12, 13, 1], [13, 14, 1], [14, 15, 1], [15, 16, 1], [16, 17, 1], [17, 18, 1], [18, 19, 1], [19, 20, 1]]), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1], [11, 12, 1], [12, 13, 1], [13, 14, 1], [14, 15, 1], [15, 16, 1], [16, 17, 1], [17, 18, 1], [18, 19, 1], [19, 20, 1]]), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1], [4, 5, 0], [5, 6, 1], [6, 7, 0], [7, 8, 1], [8, 9, 0], [9, 10, 1], [10, 11, 0]]), tree_node([1, 2, None, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1], [4, 5, 0], [5, 6, 1], [6, 7, 0], [7, 8, 1], [8, 9, 0], [9, 10, 1], [10, 11, 0]]), tree_node([1, 2, None, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 8, 0], [3, 2, 1], [3, 4, 0], [8, 7, 1], [8, 9, 0], [7, 6, 1], [9, 10, 0], [6, 11, 1], [6, 12, 0], [10, 13, 1], [10, 14, 0], [12, 15, 1], [12, 16, 0]]), tree_node([5, 3, 8, 2, 4, 7, 9, None, None, None, None, 6, None, None, 10, 11, 12, 13, 14, None, None, 15, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 8, 0], [3, 2, 1], [3, 4, 0], [8, 7, 1], [8, 9, 0], [7, 6, 1], [9, 10, 0], [6, 11, 1], [6, 12, 0], [10, 13, 1], [10, 14, 0], [12, 15, 1], [12, 16, 0]]), tree_node([5, 3, 8, 2, 4, 7, 9, None, None, None, None, 6, None, None, 10, 11, 12, 13, 14, None, None, 15, 16])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]), tree_node([1, 2, None, None, 3, 4]))
    assert is_same_tree(candidate(descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]), tree_node([50, 20, 80, 15, 17, 19]))
    assert is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [3, 1, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0]]), tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8]))
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [1, 3, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [6, 12, 1], [6, 13, 0], [7, 14, 1], [7, 15, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_tree(candidate(descriptions = [[99, 98, 1], [98, 97, 1], [97, 96, 1], [96, 95, 1], [95, 94, 1], [94, 93, 1], [93, 92, 1], [92, 91, 1], [91, 90, 1], [90, 89, 1], [89, 88, 1], [88, 87, 1], [87, 86, 1], [86, 85, 1]]), tree_node([99, 98, None, 97, None, 96, None, 95, None, 94, None, 93, None, 92, None, 91, None, 90, None, 89, None, 88, None, 87, None, 86, None, 85]))
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [4, 8, 1], [8, 16, 1], [16, 32, 1], [32, 64, 1], [64, 128, 1], [1, 3, 0], [3, 5, 1], [5, 9, 1], [9, 17, 1], [17, 33, 1], [33, 65, 1], [65, 129, 1], [1, 6, 0], [6, 10, 1], [10, 18, 1], [18, 34, 1], [34, 66, 1], [66, 130, 1], [1, 7, 0], [7, 11, 1], [11, 19, 1], [19, 35, 1], [35, 67, 1], [67, 131, 1], [1, 8, 0], [8, 12, 1], [12, 20, 1], [20, 36, 1], [36, 68, 1], [68, 132, 1], [1, 9, 0], [9, 13, 1], [13, 21, 1], [21, 37, 1], [37, 69, 1], [69, 133, 1], [1, 10, 0], [10, 14, 1], [14, 22, 1], [22, 38, 1], [38, 70, 1], [70, 134, 1]]), tree_node([1, 2, 10, 4, None, 14, None, 8, None, 22, None, 12, None, 38, None, 20, None, 70, None, 36, None, 134, None, 68, None, None, None, 132]))
    assert is_same_tree(candidate(descriptions = [[2, 1, 1], [2, 3, 0], [3, 6, 0], [6, 12, 0], [12, 24, 0], [24, 48, 0], [48, 96, 0], [96, 192, 0], [192, 384, 0], [384, 768, 0]]), tree_node([2, 1, 3, None, None, None, 6, None, 12, None, 24, None, 48, None, 96, None, 192, None, 384, None, 768]))
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [2, 5, 0], [1, 3, 0], [3, 6, 1], [3, 7, 0], [7, 14, 1], [7, 15, 0], [15, 30, 1], [15, 31, 0], [31, 62, 1], [31, 63, 0], [63, 126, 1], [63, 127, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 14, 15, None, None, 30, 31, None, None, 62, 63, None, None, 126, 127]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175]))
    assert is_same_tree(candidate(descriptions = [[1000, 500, 1], [500, 250, 1], [500, 750, 0], [1000, 1500, 0], [1500, 1250, 1], [1500, 1750, 0], [1750, 1600, 1], [1750, 1800, 0], [1800, 1775, 1], [1800, 1825, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, None, None, None, None, 1600, 1800, None, None, 1775, 1825]))
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 4, 1], [2, 5, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [1, 3, 0], [3, 6, 1], [3, 7, 0]]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [750, 375, 1], [750, 1125, 0], [1250, 625, 1], [1250, 937, 0], [1750, 1562, 1], [1750, 1875, 0], [375, 187, 1], [375, 562, 0], [1125, 843, 1], [1125, 1406, 0], [625, 312, 1], [625, 468, 0], [937, 468, 1], [937, 703, 0], [1562, 781, 1], [1562, 1281, 0], [1875, 937, 1], [1875, 938, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, 375, 1125, 625, 937, 1562, 1875, 187, 562, 843, 1406, 312, 468, 468, 703, 781, 1281, 937, 938, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 468, 703]))
    assert is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 8, 0], [3, 2, 1], [3, 4, 0], [8, 7, 1], [8, 9, 0], [4, 6, 0], [9, 10, 1]]), tree_node([5, 3, 8, 2, 4, 7, 9, None, None, None, 6, None, None, 10]))
    assert is_same_tree(candidate(descriptions = [[60, 30, 1], [60, 90, 0], [30, 15, 1], [30, 45, 0], [45, 40, 1], [45, 50, 0], [90, 75, 1], [90, 105, 0], [105, 100, 1], [105, 110, 0]]), tree_node([60, 30, 90, 15, 45, 75, 105, None, None, 40, 50, None, None, 100, 110]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 160, 1], [175, 190, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, 160, 190]))
    assert is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 45, 0], [10, 5, 1], [10, 15, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, 5, 15]))
    assert is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [1250, 1125, 1], [1250, 1375, 0], [1750, 1625, 1], [1750, 1875, 0], [1875, 1825, 1], [1875, 1925, 0]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, None, None, None, None, 1125, 1375, 1625, 1875, None, None, None, None, None, None, 1825, 1925]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 200, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, None, 200]))
    assert is_same_tree(candidate(descriptions = [[99, 88, 1], [99, 77, 0], [88, 66, 1], [88, 55, 0], [77, 44, 1], [77, 33, 0], [66, 22, 1], [66, 11, 0], [55, 9, 1], [55, 8, 0], [44, 7, 1], [44, 6, 0], [33, 5, 1], [33, 4, 0], [22, 3, 1], [22, 2, 0], [11, 1, 1], [11, 0, 0]]), tree_node([99, 88, 77, 66, 55, 44, 33, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
    assert is_same_tree(candidate(descriptions = [[25, 10, 1], [25, 30, 0], [10, 5, 1], [10, 15, 0], [30, 28, 1], [30, 32, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [28, 26, 1], [28, 29, 0], [32, 31, 1], [32, 33, 0]]), tree_node([25, 10, 30, 5, 15, 28, 32, 3, 7, 12, 18, 26, 29, 31, 33]))
    assert is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [3, 5, 1], [3, 4, 0], [5, 7, 1], [5, 6, 0], [7, 11, 1], [7, 8, 0], [8, 9, 1], [8, 10, 0]]), tree_node([1, 3, 2, 5, 4, None, None, 7, 6, None, None, 11, 8, None, None, None, None, 9, 10]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [75, 60, 0], [175, 180, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, 60, None, None, None, 180]))
    assert is_same_tree(candidate(descriptions = [[200, 100, 1], [200, 300, 0], [100, 50, 1], [100, 150, 0], [300, 250, 1], [300, 350, 0], [150, 125, 1], [150, 175, 0], [350, 325, 1], [350, 375, 0]]), tree_node([200, 100, 300, 50, 150, 250, 350, None, None, 125, 175, None, None, 325, 375]))
    assert is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 50, 0], [50, 45, 1], [50, 55, 0]]), tree_node([30, 20, 40, 10, 25, 35, 50, None, None, None, None, None, None, 45, 55]))
    assert is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0], [18, 17, 1], [18, 19, 0], [19, 16, 0], [19, 20, 1]]), tree_node([10, 5, 15, 3, 7, 12, 18, None, None, None, None, None, None, 17, 19, None, None, 20, 16]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [25, 10, 1], [75, 60, 0], [125, 110, 0], [175, 190, 1]]), tree_node([100, 50, 150, 25, 75, 125, 175, 10, None, None, 60, None, 110, 190]))
    assert is_same_tree(candidate(descriptions = [[8, 4, 1], [8, 12, 0], [4, 2, 1], [4, 6, 0], [12, 10, 1], [12, 14, 0], [2, 1, 1], [2, 3, 0], [6, 5, 1], [6, 7, 0]]), tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7]))
    assert is_same_tree(candidate(descriptions = [[99, 66, 1], [66, 33, 1], [33, 16, 1], [16, 8, 1], [8, 4, 1], [4, 2, 1], [2, 1, 1], [99, 77, 0], [77, 55, 0], [55, 38, 0], [38, 19, 0], [19, 9, 0], [9, 4, 0], [4, 2, 0], [99, 88, 0], [88, 55, 1], [55, 34, 1], [34, 17, 1], [17, 8, 0]]), tree_node([99, 66, 88, 33, None, 55, None, 16, None, 34, 38, 8, None, 17, None, None, 19, 4, None, None, 8, None, 9, 2, 2, 4, None, None, 4, 1, None, 1, None, 2, 2, 2, 2, None, None, None, None, 1, None, 1, None, 1, None, 1]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [25, 10, 1], [25, 40, 0], [75, 60, 1], [75, 85, 0], [125, 110, 1], [125, 135, 0], [175, 160, 1], [175, 185, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 85, 110, 135, 160, 185]))
    assert is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 2, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [2, 1, 1], [4, 9, 0], [9, 10, 1]]), tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, 9, None, None, None, None, None, None, 10]))
    assert is_same_tree(candidate(descriptions = [[30, 20, 1], [20, 10, 1], [20, 25, 0], [30, 40, 0], [40, 35, 1], [40, 45, 0], [35, 32, 1], [35, 37, 0], [45, 42, 1], [45, 47, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, None, None, None, None, 32, 37, 42, 47]))
    assert is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 1, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [8, 9, 1], [9, 10, 0], [10, 11, 1], [11, 12, 0], [12, 13, 1]]), tree_node([5, 3, 7, 1, 4, 6, 8, None, None, None, None, None, None, 9, None, None, 10, 11, None, None, 12, 13]))
    assert is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0], [6, 12, 1], [6, 13, 0], [7, 14, 1], [7, 15, 0], [8, 16, 1], [8, 17, 0], [9, 18, 1], [9, 19, 0]]), tree_node([1, 3, 2, 6, 7, 4, 5, 12, 13, 14, 15, 8, 9, 10, 11, None, None, None, None, None, None, None, None, 16, 17, 18, 19]))
    assert is_same_tree(candidate(descriptions = [[10, 5, 1], [10, 15, 0], [5, 3, 1], [5, 7, 0], [15, 12, 1], [15, 18, 0]]), tree_node([10, 5, 15, 3, 7, 12, 18]))
    assert is_same_tree(candidate(descriptions = [[500, 250, 1], [500, 750, 0], [250, 125, 1], [250, 375, 0], [750, 625, 1], [750, 875, 0], [125, 60, 1], [125, 180, 0], [375, 290, 1], [375, 440, 0], [625, 550, 1], [625, 680, 0], [875, 800, 1], [875, 940, 0]]), tree_node([500, 250, 750, 125, 375, 625, 875, 60, 180, 290, 440, 550, 680, 800, 940]))
    assert is_same_tree(candidate(descriptions = [[5, 4, 1], [5, 6, 0], [4, 3, 1], [4, 2, 0], [6, 7, 1], [6, 8, 0], [7, 9, 1], [7, 10, 0], [8, 11, 1], [8, 12, 0], [9, 13, 1], [9, 14, 0], [10, 15, 1], [10, 16, 0], [11, 17, 1], [11, 18, 0], [12, 19, 1], [12, 20, 0], [13, 21, 1], [13, 22, 0], [14, 23, 1], [14, 24, 0], [15, 25, 1], [15, 26, 0], [16, 27, 1], [16, 28, 0]]), tree_node([5, 4, 6, 3, 2, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]))
    assert is_same_tree(candidate(descriptions = [[7, 3, 1], [7, 10, 0], [3, 1, 1], [3, 5, 0], [10, 8, 1], [10, 12, 0], [5, 4, 0], [5, 6, 1], [8, 9, 1], [12, 11, 0]]), tree_node([7, 3, 10, 1, 5, 8, 12, None, None, 6, 4, 9, None, None, 11]))
    assert is_same_tree(candidate(descriptions = [[60, 30, 1], [60, 90, 0], [30, 15, 1], [30, 45, 0], [90, 75, 1], [90, 105, 0], [15, 10, 1], [15, 20, 0], [45, 35, 1], [45, 50, 0], [75, 65, 1], [75, 85, 0], [105, 100, 1], [105, 110, 0]]), tree_node([60, 30, 90, 15, 45, 75, 105, 10, 20, 35, 50, 65, 85, 100, 110]))
    assert is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 7, 0], [3, 2, 1], [3, 4, 0], [7, 6, 1], [7, 8, 0], [2, 1, 1], [4, 9, 0], [6, 11, 1], [8, 13, 0], [1, 0, 1], [9, 12, 0], [11, 10, 0], [13, 14, 1]]), tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, 9, 11, None, None, 13, 0, None, None, 12, None, 10, 14]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [75, 60, 1], [75, 90, 0]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, 60, 90]))
    assert is_same_tree(candidate(descriptions = [[100, 50, 1], [100, 150, 0], [50, 25, 1], [50, 75, 0], [150, 125, 1], [150, 175, 0], [175, 160, 1]]), tree_node([100, 50, 150, 25, 75, 125, 175, None, None, None, None, None, None, 160]))
    assert is_same_tree(candidate(descriptions = [[1000, 500, 1], [1000, 1500, 0], [500, 250, 1], [500, 750, 0], [1500, 1250, 1], [1500, 1750, 0], [250, 100, 1], [750, 600, 0], [1250, 1100, 0], [1750, 1900, 1], [100, 50, 1], [600, 550, 0], [1100, 1050, 0], [1900, 1850, 1]]), tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 100, None, None, 600, None, 1100, 1900, None, 50, None, None, 550, None, 1050, 1850]))
    assert is_same_tree(candidate(descriptions = [[30, 20, 1], [30, 40, 0], [20, 10, 1], [20, 25, 0], [40, 35, 1], [40, 45, 0], [10, 5, 1], [25, 15, 0], [35, 32, 1], [45, 47, 0]]), tree_node([30, 20, 40, 10, 25, 35, 45, 5, None, None, 15, 32, None, None, 47]))
    assert is_same_tree(candidate(descriptions = [[30, 20, 1], [20, 10, 1], [10, 5, 1], [5, 2, 1], [30, 40, 0], [40, 50, 0], [50, 60, 0]]), tree_node([30, 20, 40, 10, None, None, 50, 5, None, None, 60, 2]))
    assert is_same_tree(candidate(descriptions = [[1, 3, 1], [1, 2, 0], [2, 4, 1], [2, 5, 0], [3, 6, 1], [3, 7, 0], [4, 8, 1], [4, 9, 0], [5, 10, 1], [5, 11, 0]]), tree_node([1, 3, 2, 6, 7, 4, 5, None, None, None, None, 8, 9, 10, 11]))
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1], [11, 12, 1], [12, 13, 1], [13, 14, 1], [14, 15, 1], [15, 16, 1], [16, 17, 1], [17, 18, 1], [18, 19, 1], [19, 20, 1]]), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]))
    assert is_same_tree(candidate(descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1], [4, 5, 0], [5, 6, 1], [6, 7, 0], [7, 8, 1], [8, 9, 0], [9, 10, 1], [10, 11, 0]]), tree_node([1, 2, None, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11]))
    assert is_same_tree(candidate(descriptions = [[5, 3, 1], [5, 8, 0], [3, 2, 1], [3, 4, 0], [8, 7, 1], [8, 9, 0], [7, 6, 1], [9, 10, 0], [6, 11, 1], [6, 12, 0], [10, 13, 1], [10, 14, 0], [12, 15, 1], [12, 16, 0]]), tree_node([5, 3, 8, 2, 4, 7, 9, None, None, None, None, 6, None, None, 10, 11, 12, 13, 14, None, None, 15, 16]))


