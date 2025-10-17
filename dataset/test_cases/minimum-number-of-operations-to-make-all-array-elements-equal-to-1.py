def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 21, 35, 49, 63]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 21, 35, 49, 63]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 3, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 3, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 10, 6, 14]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 10, 6, 14]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 9, 3, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 9, 3, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 3, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 3, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 9, 12, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 9, 12, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 55, 11, 22, 88, 44, 66]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 55, 11, 22, 88, 44, 66]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [48, 64, 80, 96, 112]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [48, 64, 80, 96, 112]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 42, 56]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 42, 56]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 18, 24, 30, 36]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 18, 24, 30, 36]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 12, 15, 18, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 12, 15, 18, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 28, 35, 42, 49]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 28, 35, 42, 49]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 25, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 25, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 17, 19, 23, 29, 31, 37]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 17, 19, 23, 29, 31, 37]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 70, 105, 140, 210]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 70, 105, 140, 210]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1500, 2000, 2500]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1500, 2000, 2500]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 27, 81, 243, 729]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 27, 81, 243, 729]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 16, 20, 24, 28]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 16, 20, 24, 28]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 27, 36, 45, 54]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 27, 36, 45, 54]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 21, 28, 35, 42]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 21, 28, 35, 42]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [103, 206, 309, 412, 515, 618, 721, 824, 927, 1030, 1133, 1236, 1339, 1442, 1545, 1648, 1751, 1854, 1957, 2060, 2163, 2266, 2369]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [103, 206, 309, 412, 515, 618, 721, 824, 927, 1030, 1133, 1236, 1339, 1442, 1545, 1648, 1751, 1854, 1957, 2060, 2163, 2266, 2369]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 18, 30, 42, 54, 66, 78]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 18, 30, 42, 54, 66, 78]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 90, 135, 180, 225, 270]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 90, 135, 180, 225, 270]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 20, 40, 80, 160]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 20, 40, 80, 160]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 24, 30, 36, 42]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 24, 30, 36, 42]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 42, 7, 14, 28, 35]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 42, 7, 14, 28, 35]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 51, 85, 102, 136]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 51, 85, 102, 136]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [109, 218, 327, 436, 545, 654, 763, 872, 981, 1090, 1199, 1308, 1417, 1526, 1635, 1744, 1853, 1962, 2071, 2180, 2289, 2398, 2507, 2616, 2725, 2834, 2943]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [109, 218, 327, 436, 545, 654, 763, 872, 981, 1090, 1199, 1308, 1417, 1526, 1635, 1744, 1853, 1962, 2071, 2180, 2289, 2398, 2507, 2616, 2725, 2834, 2943]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 35, 49, 63, 77, 91, 105]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 35, 49, 63, 77, 91, 105]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 194, 291, 388, 485, 582]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 194, 291, 388, 485, 582]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483, 506]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483, 506]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [107, 214, 321, 428, 535, 642, 749, 856, 963, 1070, 1177, 1284, 1391, 1498, 1605, 1712, 1819, 1926, 2033, 2140, 2247, 2354, 2461, 2568, 2675]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [107, 214, 321, 428, 535, 642, 749, 856, 963, 1070, 1177, 1284, 1391, 1498, 1605, 1712, 1819, 1926, 2033, 2140, 2247, 2354, 2461, 2568, 2675]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464, 493, 522, 551, 580, 609, 638, 667, 696, 725]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464, 493, 522, 551, 580, 609, 638, 667, 696, 725]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 20, 25, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 20, 25, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 49, 91, 35, 119, 56]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 49, 91, 35, 119, 56]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 98, 147, 196, 245, 294]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 98, 147, 196, 245, 294]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [61, 122, 183, 244, 305, 366, 427, 488, 549, 610, 671, 732, 793, 854, 915, 976]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [61, 122, 183, 244, 305, 366, 427, 488, 549, 610, 671, 732, 793, 854, 915, 976]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 9, 21, 6, 12]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 9, 21, 6, 12]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 18, 24, 30, 36]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 18, 24, 30, 36]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 35, 42]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 35, 42]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 56, 70, 84, 98]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 56, 70, 84, 98]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [41, 82, 123, 164, 205, 246, 287, 328, 369, 410, 451, 492, 533, 574, 615, 656, 697, 738, 779, 820]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [41, 82, 123, 164, 205, 246, 287, 328, 369, 410, 451, 492, 533, 574, 615, 656, 697, 738, 779, 820]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 42, 63, 84, 105]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 42, 63, 84, 105]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2046, 3069, 4092, 5115, 6138, 7161, 8184, 9207, 10230]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2046, 3069, 4092, 5115, 6138, 7161, 8184, 9207, 10230]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 98, 147, 196, 245, 294, 343]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 98, 147, 196, 245, 294, 343]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [35, 55, 77, 99, 121, 143, 165]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [35, 55, 77, 99, 121, 143, 165]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 5, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 5, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [997, 1994, 2991, 3988, 4985, 5982, 6979, 7976, 8973, 9970]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [997, 1994, 2991, 3988, 4985, 5982, 6979, 7976, 8973, 9970]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 9, 15, 21]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 9, 15, 21]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [7, 7, 7, 1]) == 3
    assert candidate(nums = [100, 200, 300, 400]) == -1
    assert candidate(nums = [1, 2, 2, 3]) == 3
    assert candidate(nums = [7, 21, 35, 49, 63]) == -1
    assert candidate(nums = [2, 4, 6, 8, 10, 12]) == -1
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == -1
    assert candidate(nums = [1, 1, 1, 1]) == 0
    assert candidate(nums = [10, 15, 25]) == -1
    assert candidate(nums = [2, 4, 6, 8, 10]) == -1
    assert candidate(nums = [3, 6, 9, 12]) == -1
    assert candidate(nums = [2, 6, 3, 4]) == 4
    assert candidate(nums = [2, 10, 6, 14]) == -1
    assert candidate(nums = [5, 15, 25, 35]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50]) == -1
    assert candidate(nums = [15, 9, 3, 6]) == -1
    assert candidate(nums = [5, 5, 5, 5]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [3, 5, 7, 11]) == 4
    assert candidate(nums = [10, 15, 20, 25]) == -1
    assert candidate(nums = [2, 3, 5, 7]) == 4
    assert candidate(nums = [3, 9, 3, 3]) == -1
    assert candidate(nums = [2, 2, 2, 2]) == -1
    assert candidate(nums = [6, 9, 12, 15]) == -1
    assert candidate(nums = [3, 3, 3, 3, 3]) == -1
    assert candidate(nums = [7, 14, 21, 28]) == -1
    assert candidate(nums = [2, 4, 6, 8]) == -1
    assert candidate(nums = [33, 55, 11, 22, 88, 44, 66]) == -1
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == -1
    assert candidate(nums = [48, 64, 80, 96, 112]) == -1
    assert candidate(nums = [5, 10, 15, 20, 25, 30]) == -1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == -1
    assert candidate(nums = [100, 150, 200, 250, 300, 350]) == -1
    assert candidate(nums = [17, 34, 51, 68, 85]) == -1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == -1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == -1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == -1
    assert candidate(nums = [7, 14, 28, 42, 56]) == -1
    assert candidate(nums = [8, 12, 18, 24, 30, 36]) == -1
    assert candidate(nums = [9, 12, 15, 18, 21]) == -1
    assert candidate(nums = [21, 28, 35, 42, 49]) == -1
    assert candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464]) == -1
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == -1
    assert candidate(nums = [10, 15, 25, 50]) == -1
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37]) == 7
    assert candidate(nums = [7, 14, 21, 28, 35, 42]) == -1
    assert candidate(nums = [33, 66, 99, 132, 165]) == -1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 15
    assert candidate(nums = [42, 70, 105, 140, 210]) == -1
    assert candidate(nums = [1000, 1500, 2000, 2500]) == -1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == -1
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500]) == -1
    assert candidate(nums = [8, 16, 24, 32, 40, 48]) == -1
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
    assert candidate(nums = [9, 27, 81, 243, 729]) == -1
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210]) == -1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204]) == -1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]) == -1
    assert candidate(nums = [4, 8, 12, 16, 20, 24]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500]) == -1
    assert candidate(nums = [8, 12, 16, 20, 24, 28]) == -1
    assert candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144]) == -1
    assert candidate(nums = [3, 6, 9, 12, 15, 18]) == -1
    assert candidate(nums = [15, 25, 35, 5]) == -1
    assert candidate(nums = [3, 5, 7, 9, 11]) == 5
    assert candidate(nums = [18, 27, 36, 45, 54]) == -1
    assert candidate(nums = [14, 21, 28, 35, 42]) == -1
    assert candidate(nums = [7, 14, 21, 28, 35]) == -1
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == -1
    assert candidate(nums = [12, 15, 18, 21, 24]) == -1
    assert candidate(nums = [103, 206, 309, 412, 515, 618, 721, 824, 927, 1030, 1133, 1236, 1339, 1442, 1545, 1648, 1751, 1854, 1957, 2060, 2163, 2266, 2369]) == -1
    assert candidate(nums = [6, 18, 30, 42, 54, 66, 78]) == -1
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77]) == -1
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40]) == -1
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65]) == -1
    assert candidate(nums = [45, 90, 135, 180, 225, 270]) == -1
    assert candidate(nums = [5, 10, 20, 40, 80, 160]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500]) == -1
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77]) == -1
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == -1
    assert candidate(nums = [18, 24, 30, 36, 42]) == -1
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285]) == -1
    assert candidate(nums = [21, 42, 7, 14, 28, 35]) == -1
    assert candidate(nums = [15, 25, 35, 45]) == -1
    assert candidate(nums = [13, 26, 39, 52, 65]) == -1
    assert candidate(nums = [17, 51, 85, 102, 136]) == -1
    assert candidate(nums = [109, 218, 327, 436, 545, 654, 763, 872, 981, 1090, 1199, 1308, 1417, 1526, 1635, 1744, 1853, 1962, 2071, 2180, 2289, 2398, 2507, 2616, 2725, 2834, 2943]) == -1
    assert candidate(nums = [3, 9, 27, 81, 243, 729]) == -1
    assert candidate(nums = [21, 35, 49, 63, 77, 91, 105]) == -1
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230]) == -1
    assert candidate(nums = [3, 9, 27, 81]) == -1
    assert candidate(nums = [97, 194, 291, 388, 485, 582]) == -1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == -1
    assert candidate(nums = [3, 9, 27, 81, 243]) == -1
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == -1
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483, 506]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 5
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == -1
    assert candidate(nums = [107, 214, 321, 428, 535, 642, 749, 856, 963, 1070, 1177, 1284, 1391, 1498, 1605, 1712, 1819, 1926, 2033, 2140, 2247, 2354, 2461, 2568, 2675]) == -1
    assert candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464, 493, 522, 551, 580, 609, 638, 667, 696, 725]) == -1
    assert candidate(nums = [15, 20, 25, 30]) == -1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == -1
    assert candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144]) == -1
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == -1
    assert candidate(nums = [7, 49, 91, 35, 119, 56]) == -1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600]) == -1
    assert candidate(nums = [49, 98, 147, 196, 245, 294]) == -1
    assert candidate(nums = [61, 122, 183, 244, 305, 366, 427, 488, 549, 610, 671, 732, 793, 854, 915, 976]) == -1
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322]) == -1
    assert candidate(nums = [15, 9, 21, 6, 12]) == -1
    assert candidate(nums = [12, 18, 24, 30, 36]) == -1
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == -1
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31]) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 10
    assert candidate(nums = [15, 25, 35, 45, 55]) == -1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == -1
    assert candidate(nums = [7, 14, 21, 35, 42]) == -1
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40]) == -1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260]) == -1
    assert candidate(nums = [42, 56, 70, 84, 98]) == -1
    assert candidate(nums = [41, 82, 123, 164, 205, 246, 287, 328, 369, 410, 451, 492, 533, 574, 615, 656, 697, 738, 779, 820]) == -1
    assert candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(nums = [21, 42, 63, 84, 105]) == -1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111]) == -1
    assert candidate(nums = [15, 25, 35, 45, 55]) == -1
    assert candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == -1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == -1
    assert candidate(nums = [1023, 2046, 3069, 4092, 5115, 6138, 7161, 8184, 9207, 10230]) == -1
    assert candidate(nums = [3, 5, 7, 11, 13]) == 5
    assert candidate(nums = [49, 98, 147, 196, 245, 294, 343]) == -1
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247]) == -1
    assert candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]) == 15
    assert candidate(nums = [100, 150, 200, 250, 300]) == -1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]) == -1
    assert candidate(nums = [35, 55, 77, 99, 121, 143, 165]) == 8
    assert candidate(nums = [15, 25, 35, 5, 10]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == -1
    assert candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132]) == -1
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 10
    assert candidate(nums = [8, 16, 32, 64, 128]) == -1
    assert candidate(nums = [7, 14, 21, 28, 35]) == -1
    assert candidate(nums = [11, 22, 33, 44, 55, 66]) == -1
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42]) == -1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340]) == -1
    assert candidate(nums = [997, 1994, 2991, 3988, 4985, 5982, 6979, 7976, 8973, 9970]) == -1
    assert candidate(nums = [3, 5, 9, 15, 21]) == 5
    assert candidate(nums = [100, 101, 102, 103, 104]) == 5


