def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 825: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6])) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6])) == 110: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, 6])) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, 6])) == 90: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 9, 10, 7, 4, 6, 5, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6])) == 3410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 9, 10, 7, 4, 6, 5, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6])) == 3410: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 486675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 486675: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])) == 270725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])) == 270725: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31])) == 61503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31])) == 61503: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 756: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, None, None, 3, None, None, 4, None, None, 4])) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, None, None, 3, None, None, 4, None, None, 4])) == 88: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 24600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 24600: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 374900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 374900: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 5933400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 5933400: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 2, 20, 1, None, 15, 30, 8, None, None, None, 9, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 3672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 2, 20, 1, None, 15, 30, 8, None, None, None, 9, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 3672: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 756: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 166875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 166875: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9999, 4999, 4999, 2499, 2500, 2499, 2500, 1249, 1250, 1250, 1250, 1249, 1250, 1249, 1250, 624, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625])) == 599780020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9999, 4999, 4999, 2499, 2500, 2499, 2500, 1249, 1250, 1250, 1250, 1249, 1250, 1249, 1250, 624, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625])) == 599780020: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5000, 2500, 7500, 1250, 3750, 6250, 8750, 625, 1875, 2500, 5000, 4375, 7500, 8125, 9375])) == 263281243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5000, 2500, 7500, 1250, 3750, 6250, 8750, 625, 1875, 2500, 5000, 4375, 7500, 8125, 9375])) == 263281243: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 9, 1, 3, 8, 12, None, None, None, None, 6, 10, 11, 13])) == 1584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 9, 1, 3, 8, 12, None, None, None, None, 6, 10, 11, 13])) == 1584: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 680: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 9, 10, 7, 4, 6, 5, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6, 7, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6, 7, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6])) == 18522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 9, 10, 7, 4, 6, 5, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6, 7, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6, 7, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6])) == 18522: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, 4, None, None, None, None, None, 25, 20])) == 2970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, 4, None, None, None, None, None, 25, 20])) == 2970: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 756: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 250, 750, 125, 375, 500, 1000, 62, 188, 250, 500, 375, 625, 875, 1125, 31, 94, 125, 250, 375, 438, 625, 750, 875, 1000, 1125, 1250, 1375, 1500, 1625, 1750, 1875])) == 123145250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 250, 750, 125, 375, 500, 1000, 62, 188, 250, 500, 375, 625, 875, 1125, 31, 94, 125, 250, 375, 438, 625, 750, 875, 1000, 1125, 1250, 1375, 1500, 1625, 1750, 1875])) == 123145250: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 899800054
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 899800054: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 11025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 11025: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 376650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 376650: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 6, 2, 4, None, 10, 1, 5, None, None, 8, 9, 11, 12])) == 1520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 6, 2, 4, None, 10, 1, 5, None, None, 8, 9, 11, 12])) == 1520: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 11024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 11024: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([999, 499, 1499, 249, 749, 999, 1999, 124, 374, 499, 749, 999, 1249, 1499, 1749, 62, 187, 249, 374, 499, 562, 749, 999, 1249, 1499, 1749, 1999, 2249, 2499, 2749, 2999, 3249, 3499, 3749, 3999, 4249, 4499, 4749, 4999, 5249, 5499, 5749, 5999])) == 930774628
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([999, 499, 1499, 249, 749, 999, 1999, 124, 374, 499, 749, 999, 1249, 1499, 1749, 62, 187, 249, 374, 499, 562, 749, 999, 1249, 1499, 1749, 1999, 2249, 2499, 2749, 2999, 3249, 3499, 3749, 3999, 4249, 4499, 4749, 4999, 5249, 5499, 5749, 5999])) == 930774628: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])) == 115500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])) == 115500: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, None, 15, 20, None, None, 25, 30, 35, 40, None, None, None, None, 45, 50, None, None, None, None, None, None, 55, 60])) == 18900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, None, 15, 20, None, None, 25, 30, 35, 40, None, None, None, None, 45, 50, None, None, None, None, None, None, 55, 60])) == 18900: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25000, 12500, 37500, 6250, 18750, 25000, 50000, 3125, 9375, 15625, 21875, 12500, 18750, 31250, 37500, 1562, 4688, 7812, 9375, 12500, 15625, 18750, 21875, 25000, 31250, 37500, 43750, 46875, 50000, 53125, 56250, 59375, 62500])) == 650111233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25000, 12500, 37500, 6250, 18750, 25000, 50000, 3125, 9375, 15625, 21875, 12500, 18750, 31250, 37500, 1562, 4688, 7812, 9375, 12500, 15625, 18750, 21875, 25000, 31250, 37500, 43750, 46875, 50000, 53125, 56250, 59375, 62500])) == 650111233: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 190])) == 496125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 190])) == 496125: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37, 0, 2, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 90405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37, 0, 2, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 90405: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 400, 600, 300, 450, 550, 650, 200, 350, 425, 475, 525, 575, 625, 675, 100, 250, 325, 375, 412, 437, 462, 487, 512, 537, 562, 587, 612, 637, 662, 687, 90, 160, 225, 275, 312, 337, 362, 387, 402, 447, 492, 532, 557, 592, 627, 642, 677, 702, 65, 125, 187, 237, 262, 287, 302, 347, 392, 417, 432, 477, 502, 527, 542, 577, 602, 632, 657, 692, 717, 742, 767, 792])) == 287180438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 400, 600, 300, 450, 550, 650, 200, 350, 425, 475, 525, 575, 625, 675, 100, 250, 325, 375, 412, 437, 462, 487, 512, 537, 562, 587, 612, 637, 662, 687, 90, 160, 225, 275, 312, 337, 362, 387, 402, 447, 492, 532, 557, 592, 627, 642, 677, 702, 65, 125, 187, 237, 262, 287, 302, 347, 392, 417, 432, 477, 502, 527, 542, 577, 602, 632, 657, 692, 717, 742, 767, 792])) == 287180438: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190, None, 40, 55, 65, 70, 85, 90, 115, 120, 130, 145, 155, 165, 185, 195, None, 35, 45, 56, 64, 72, 78, 82, 88, 95, 105, 117, 123, 127, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, None, 9, 11, 13, 17, 21, 23, 27, 29, 33, 37, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99])) == 16555528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190, None, 40, 55, 65, 70, 85, 90, 115, 120, 130, 145, 155, 165, 185, 195, None, 35, 45, 56, 64, 72, 78, 82, 88, 95, 105, 117, 123, 127, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, None, 9, 11, 13, 17, 21, 23, 27, 29, 33, 37, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99])) == 16555528: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5000, 2500, 7500, 1250, 3750, 6250, 8750, 625, 1875, 2500, 4375, 5625, 7187, 9375, 10625, 3125, 937, 1250, 1687, 2187, 3125, 3750, 4687, 5312, 5937, 6562, 7187, 7812, 8437, 9062, 9687, 10312, 10937, 11562, 12187, 12812, 13437, 14062, 14687, 15312])) == 398822622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5000, 2500, 7500, 1250, 3750, 6250, 8750, 625, 1875, 2500, 4375, 5625, 7187, 9375, 10625, 3125, 937, 1250, 1687, 2187, 3125, 3750, 4687, 5312, 5937, 6562, 7187, 7812, 8437, 9062, 9687, 10312, 10937, 11562, 12187, 12812, 13437, 14062, 14687, 15312])) == 398822622: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 2, 6, 8, 16, 20, None, None, None, None, 9, 12, None, None, None, None, 17, 21])) == 7176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 2, 6, 8, 16, 20, None, None, None, None, 9, 12, None, None, None, None, 17, 21])) == 7176: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 225: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])) == 16687500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])) == 16687500: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 315: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 3575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 3575: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 491825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 491825: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 53354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 53354: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None])) == 11025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None])) == 11025: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, 6, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15, None, None, 16])) == 4588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, 6, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15, None, None, 16])) == 4588: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 100, 300, 600, 800, 1100, 1400, 1600, 1800, 50, 150, 250, 350, 450, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950])) == 277680000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 100, 300, 600, 800, 1100, 1400, 1600, 1800, 50, 150, 250, 350, 450, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950])) == 277680000: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40, None, 41, None, 42, None, 43, None, 44, None, 45, None, 46, None, 47, None, 48, None, 49, None, 50])) == 406350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40, None, 41, None, 42, None, 43, None, 44, None, 45, None, 46, None, 47, None, 48, None, 49, None, 50])) == 406350: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500, 1000, 3000, 6000, 8000, 11000, 13000, 16000, 18000, 500, 1500, 2500, 3500, 4500, 6500, 7500, 8500, 9500, 10500, 11500, 12500, 13500, 14500, 15500])) == 482499888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500, 1000, 3000, 6000, 8000, 11000, 13000, 16000, 18000, 500, 1500, 2500, 3500, 4500, 6500, 7500, 8500, 9500, 10500, 11500, 12500, 13500, 14500, 15500])) == 482499888: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, None, None, 14, 15, 16, 17])) == 5670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, None, None, 14, 15, 16, 17])) == 5670: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 504: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8, None, None, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8, None, None, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10829
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10829: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 900, 100, 800, 950, 50, 150, 700, 850, 925, 975, 25, 75, 125, 175, 650, 750, 825, 875, 912, 937, 962, 987, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 40, 85, 90, 113, 130, 153, 172, 183, 190])) == 68450028
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 900, 100, 800, 950, 50, 150, 700, 850, 925, 975, 25, 75, 125, 175, 650, 750, 825, 875, 912, 937, 962, 987, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 40, 85, 90, 113, 130, 153, 172, 183, 190])) == 68450028: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 50, 100, 6, 18, 25, 37, 43, 62, 75, 87, 3, 9, 12, 25, 37, 43, 56, 62, 75, 87, 100, 112, 125, 137, 150, 162, 175, 187])) == 1189628
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 50, 100, 6, 18, 25, 37, 43, 62, 75, 87, 3, 9, 12, 25, 37, 43, 56, 62, 75, 87, 100, 112, 125, 137, 150, 162, 175, 187])) == 1189628: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 40, 85, 95, 115, 135, 155, 170, 185, 3, 7, 12, 18, 35, 45, 77, 90, 113, 130, 153, 172, 183, 190])) == 3437925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 40, 85, 95, 115, 135, 155, 170, 185, 3, 7, 12, 18, 35, 45, 77, 90, 113, 130, 153, 172, 183, 190])) == 3437925: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9999, None, 9998, None, 9997, None, 9996, None, 9995, None, 9994, None, 9993, None, 9992, None, 9991, None, 9990, None, 9989, None, 9988, None, 9987, None, 9986, None, 9985, None, 9984, None, 9983, None, 9982, None, 9981, None, 9980, None, 9979, None, 9978, None, 9977, None, 9976, None, 9975, None, 9974, None, 9973, None, 9972, None, 9971, None, 9970, None, 9969, None, 9968, None, 9967, None, 9966, None, 9965, None, 9964, None, 9963, None, 9962, None, 9961, None, 9960])) == 836127827
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9999, None, 9998, None, 9997, None, 9996, None, 9995, None, 9994, None, 9993, None, 9992, None, 9991, None, 9990, None, 9989, None, 9988, None, 9987, None, 9986, None, 9985, None, 9984, None, 9983, None, 9982, None, 9981, None, 9980, None, 9979, None, 9978, None, 9977, None, 9976, None, 9975, None, 9974, None, 9973, None, 9972, None, 9971, None, 9970, None, 9969, None, 9968, None, 9967, None, 9966, None, 9965, None, 9964, None, 9963, None, 9962, None, 9961, None, 9960])) == 836127827: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 53244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 53244: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875, 62, 188, 288, 462, 512, 688, 748, 1062, 1112, 1288, 1348, 1662, 1712, 1888, 1938, 31, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968])) == 533225977
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875, 62, 188, 288, 462, 512, 688, 748, 1062, 1112, 1288, 1348, 1662, 1712, 1888, 1938, 31, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968])) == 533225977: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, 6, None, 7, None, None, None, None, 8, None, 9, None, None, None, None, 10, None, 11, None, None, None, None, 12, None, 13, None, None, None, None, 14, None, 15])) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, 6, None, 7, None, None, None, None, 8, None, 9, None, None, None, None, 10, None, 11, None, None, None, None, 12, None, 13, None, None, None, None, 14, None, 15])) == 192: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 5000, 5000, 2500, 2500, 2500, 2500, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250])) == 375000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 5000, 5000, 2500, 2500, 2500, 2500, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250])) == 375000000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3])) == 9
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 825
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6])) == 110
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, 6])) == 90
    assert candidate(root = tree_node([2, 3, 9, 10, 7, 4, 6, 5, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6])) == 3410
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 486675
    assert candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])) == 270725
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31])) == 61503
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 756
    assert candidate(root = tree_node([1, 2, 2, 3, None, None, 3, None, None, 4, None, None, 4])) == 88
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 24600
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 374900
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 5933400
    assert candidate(root = tree_node([10, 2, 20, 1, None, 15, 30, 8, None, None, None, 9, None, 7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 3672
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 756
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 166875
    assert candidate(root = tree_node([9999, 4999, 4999, 2499, 2500, 2499, 2500, 1249, 1250, 1250, 1250, 1249, 1250, 1249, 1250, 624, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625])) == 599780020
    assert candidate(root = tree_node([5000, 2500, 7500, 1250, 3750, 6250, 8750, 625, 1875, 2500, 5000, 4375, 7500, 8125, 9375])) == 263281243
    assert candidate(root = tree_node([5, 2, 9, 1, 3, 8, 12, None, None, None, None, 6, 10, 11, 13])) == 1584
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 680
    assert candidate(root = tree_node([2, 3, 9, 10, 7, 4, 6, 5, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6, 7, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6, 7, 8, 11, 13, None, 14, 9, 1, None, 2, 3, None, None, None, None, None, None, 4, 6])) == 18522
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, 4, None, None, None, None, None, 25, 20])) == 2970
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 756
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 500, 1000, 62, 188, 250, 500, 375, 625, 875, 1125, 31, 94, 125, 250, 375, 438, 625, 750, 875, 1000, 1125, 1250, 1375, 1500, 1625, 1750, 1875])) == 123145250
    assert candidate(root = tree_node([10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 899800054
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 11025
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 376650
    assert candidate(root = tree_node([7, 3, 6, 2, 4, None, 10, 1, 5, None, None, 8, 9, 11, 12])) == 1520
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 11024
    assert candidate(root = tree_node([999, 499, 1499, 249, 749, 999, 1999, 124, 374, 499, 749, 999, 1249, 1499, 1749, 62, 187, 249, 374, 499, 562, 749, 999, 1249, 1499, 1749, 1999, 2249, 2499, 2749, 2999, 3249, 3499, 3749, 3999, 4249, 4499, 4749, 4999, 5249, 5499, 5749, 5999])) == 930774628
    assert candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])) == 115500
    assert candidate(root = tree_node([5, 10, None, 15, 20, None, None, 25, 30, 35, 40, None, None, None, None, 45, 50, None, None, None, None, None, None, 55, 60])) == 18900
    assert candidate(root = tree_node([25000, 12500, 37500, 6250, 18750, 25000, 50000, 3125, 9375, 15625, 21875, 12500, 18750, 31250, 37500, 1562, 4688, 7812, 9375, 12500, 15625, 18750, 21875, 25000, 31250, 37500, 43750, 46875, 50000, 53125, 56250, 59375, 62500])) == 650111233
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 190])) == 496125
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37, 0, 2, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 90405
    assert candidate(root = tree_node([500, 400, 600, 300, 450, 550, 650, 200, 350, 425, 475, 525, 575, 625, 675, 100, 250, 325, 375, 412, 437, 462, 487, 512, 537, 562, 587, 612, 637, 662, 687, 90, 160, 225, 275, 312, 337, 362, 387, 402, 447, 492, 532, 557, 592, 627, 642, 677, 702, 65, 125, 187, 237, 262, 287, 302, 347, 392, 417, 432, 477, 502, 527, 542, 577, 602, 632, 657, 692, 717, 742, 767, 792])) == 287180438
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190, None, 40, 55, 65, 70, 85, 90, 115, 120, 130, 145, 155, 165, 185, 195, None, 35, 45, 56, 64, 72, 78, 82, 88, 95, 105, 117, 123, 127, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, None, 9, 11, 13, 17, 21, 23, 27, 29, 33, 37, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99])) == 16555528
    assert candidate(root = tree_node([5000, 2500, 7500, 1250, 3750, 6250, 8750, 625, 1875, 2500, 4375, 5625, 7187, 9375, 10625, 3125, 937, 1250, 1687, 2187, 3125, 3750, 4687, 5312, 5937, 6562, 7187, 7812, 8437, 9062, 9687, 10312, 10937, 11562, 12187, 12812, 13437, 14062, 14687, 15312])) == 398822622
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 2, 6, 8, 16, 20, None, None, None, None, 9, 12, None, None, None, None, 17, 21])) == 7176
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 225
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])) == 16687500
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 315
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 3575
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 491825
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 53354
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None])) == 11025
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, 6, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15, None, None, 16])) == 4588
    assert candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 100, 300, 600, 800, 1100, 1400, 1600, 1800, 50, 150, 250, 350, 450, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950])) == 277680000
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40, None, 41, None, 42, None, 43, None, 44, None, 45, None, 46, None, 47, None, 48, None, 49, None, 50])) == 406350
    assert candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500, 1000, 3000, 6000, 8000, 11000, 13000, 16000, 18000, 500, 1500, 2500, 3500, 4500, 6500, 7500, 8500, 9500, 10500, 11500, 12500, 13500, 14500, 15500])) == 482499888
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, None, None, 14, 15, 16, 17])) == 5670
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 504
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8, None, None, None, 9])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10829
    assert candidate(root = tree_node([1000, 900, 100, 800, 950, 50, 150, 700, 850, 925, 975, 25, 75, 125, 175, 650, 750, 825, 875, 912, 937, 962, 987, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 40, 85, 90, 113, 130, 153, 172, 183, 190])) == 68450028
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 50, 100, 6, 18, 25, 37, 43, 62, 75, 87, 3, 9, 12, 25, 37, 43, 56, 62, 75, 87, 100, 112, 125, 137, 150, 162, 175, 187])) == 1189628
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 3500
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 40, 85, 95, 115, 135, 155, 170, 185, 3, 7, 12, 18, 35, 45, 77, 90, 113, 130, 153, 172, 183, 190])) == 3437925
    assert candidate(root = tree_node([9999, None, 9998, None, 9997, None, 9996, None, 9995, None, 9994, None, 9993, None, 9992, None, 9991, None, 9990, None, 9989, None, 9988, None, 9987, None, 9986, None, 9985, None, 9984, None, 9983, None, 9982, None, 9981, None, 9980, None, 9979, None, 9978, None, 9977, None, 9976, None, 9975, None, 9974, None, 9973, None, 9972, None, 9971, None, 9970, None, 9969, None, 9968, None, 9967, None, 9966, None, 9965, None, 9964, None, 9963, None, 9962, None, 9961, None, 9960])) == 836127827
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 53244
    assert candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875, 62, 188, 288, 462, 512, 688, 748, 1062, 1112, 1288, 1348, 1662, 1712, 1888, 1938, 31, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968])) == 533225977
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, 6, None, 7, None, None, None, None, 8, None, 9, None, None, None, None, 10, None, 11, None, None, None, None, 12, None, 13, None, None, None, None, 14, None, 15])) == 192
    assert candidate(root = tree_node([10000, 5000, 5000, 2500, 2500, 2500, 2500, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250])) == 375000000


