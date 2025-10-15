def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21],nums2 = [1, 7],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21],nums2 = [1, 7],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 4],nums2 = [1, 3, 4],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 4],nums2 = [1, 3, 4],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21],nums2 = [7, 14],k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21],nums2 = [7, 14],k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 40, 60],nums2 = [5, 10],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 40, 60],nums2 = [5, 10],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15],nums2 = [1, 2, 3],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15],nums2 = [1, 2, 3],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [2, 5, 10],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [2, 5, 10],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15],nums2 = [1, 5],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15],nums2 = [1, 5],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [5, 10],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [5, 10],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 12],nums2 = [2, 4],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 12],nums2 = [2, 4],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60, 72, 84, 96, 108],nums2 = [4, 8, 12],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60, 72, 84, 96, 108],nums2 = [4, 8, 12],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [1, 5, 15],k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [1, 5, 15],k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32],nums2 = [2, 4, 8],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32],nums2 = [2, 4, 8],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [121, 242, 363, 484, 605],nums2 = [11, 121],k = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [121, 242, 363, 484, 605],nums2 = [11, 121],k = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [2, 4, 8],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [2, 4, 8],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [121, 242, 363, 484, 605],nums2 = [11, 22, 33],k = 11) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [121, 242, 363, 484, 605],nums2 = [11, 22, 33],k = 11) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 4, 5, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 4, 5, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [5, 10, 20, 25, 50],k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [5, 10, 20, 25, 50],k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [5, 25],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [5, 25],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 4, 5, 10],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 4, 5, 10],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 40, 60, 80, 100],nums2 = [2, 4, 5, 10],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 40, 60, 80, 100],nums2 = [2, 4, 5, 10],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72],nums2 = [1, 2, 4, 8],k = 2) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72],nums2 = [1, 2, 4, 8],k = 2) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [35, 70, 105, 140, 175, 210, 245],nums2 = [5, 7, 35],k = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [35, 70, 105, 140, 175, 210, 245],nums2 = [5, 7, 35],k = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [1, 3, 5, 15],k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [1, 3, 5, 15],k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [169, 338, 507, 676, 845],nums2 = [13, 26, 39],k = 13) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [169, 338, 507, 676, 845],nums2 = [13, 26, 39],k = 13) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [22, 44, 66, 88, 110],nums2 = [1, 2, 11],k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [22, 44, 66, 88, 110],nums2 = [1, 2, 11],k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [28, 56, 84, 112, 140],nums2 = [4, 7, 14],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [28, 56, 84, 112, 140],nums2 = [4, 7, 14],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [45, 90, 135, 180, 225],nums2 = [5, 9, 15, 45],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [45, 90, 135, 180, 225],nums2 = [5, 9, 15, 45],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180],nums2 = [1, 2, 3, 4, 6, 9],k = 9) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180],nums2 = [1, 2, 3, 4, 6, 9],k = 9) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [225, 450, 675, 900, 1125],nums2 = [15, 30, 75],k = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [225, 450, 675, 900, 1125],nums2 = [15, 30, 75],k = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196],nums2 = [2, 7, 14],k = 7) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196],nums2 = [2, 7, 14],k = 7) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48, 56],nums2 = [2, 4, 8],k = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48, 56],nums2 = [2, 4, 8],k = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],nums2 = [1, 13, 26],k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],nums2 = [1, 13, 26],k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [1, 2, 3, 6, 9],k = 9) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [1, 2, 3, 6, 9],k = 9) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [35, 70, 105, 140, 175, 210, 245, 280, 315, 350],nums2 = [5, 7, 35],k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [35, 70, 105, 140, 175, 210, 245, 280, 315, 350],nums2 = [5, 7, 35],k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [21, 42, 63, 84, 105],nums2 = [3, 7, 21],k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [21, 42, 63, 84, 105],nums2 = [3, 7, 21],k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [49, 98, 147, 196, 245],nums2 = [7, 14, 21],k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [49, 98, 147, 196, 245],nums2 = [7, 14, 21],k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],nums2 = [2, 4, 8],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],nums2 = [2, 4, 8],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [40, 80, 120, 160, 200, 240, 280, 320],nums2 = [4, 8, 20],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [40, 80, 120, 160, 200, 240, 280, 320],nums2 = [4, 8, 20],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99],nums2 = [1, 11],k = 11) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99],nums2 = [1, 11],k = 11) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24, 30],nums2 = [1, 2, 3, 4, 5],k = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24, 30],nums2 = [1, 2, 3, 4, 5],k = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [35, 70, 105, 140, 175, 210],nums2 = [5, 7, 35],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [35, 70, 105, 140, 175, 210],nums2 = [5, 7, 35],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],nums2 = [2, 6, 12],k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],nums2 = [2, 6, 12],k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 5, 10],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 5, 10],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [5, 10, 25],k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [5, 10, 25],k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [36, 72, 108, 144, 180],nums2 = [2, 3, 6],k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [36, 72, 108, 144, 180],nums2 = [2, 3, 6],k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [42, 84, 126, 168, 210],nums2 = [6, 12, 21],k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [42, 84, 126, 168, 210],nums2 = [6, 12, 21],k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],nums2 = [1, 13],k = 13) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],nums2 = [1, 13],k = 13) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99],nums2 = [11, 22, 33],k = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99],nums2 = [11, 22, 33],k = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 60, 90, 120, 150, 180, 210],nums2 = [2, 5, 10],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 60, 90, 120, 150, 180, 210],nums2 = [2, 5, 10],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24, 30, 36],nums2 = [1, 2, 3, 4, 6],k = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24, 30, 36],nums2 = [1, 2, 3, 4, 6],k = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [5, 10, 25],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [5, 10, 25],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [5, 10, 15],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [5, 10, 15],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [33, 66, 99, 132, 165],nums2 = [11, 22, 33],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [33, 66, 99, 132, 165],nums2 = [11, 22, 33],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 9, 27, 81],nums2 = [1, 3, 9],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 9, 27, 81],nums2 = [1, 3, 9],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [64, 128, 192, 256, 320],nums2 = [8, 16, 32],k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [64, 128, 192, 256, 320],nums2 = [8, 16, 32],k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [14, 28, 42, 56, 70],nums2 = [7, 14, 28],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [14, 28, 42, 56, 70],nums2 = [7, 14, 28],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270],nums2 = [3, 6, 9, 18],k = 9) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270],nums2 = [3, 6, 9, 18],k = 9) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [3, 5, 15],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [3, 5, 15],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [45, 90, 135, 180, 225],nums2 = [5, 15, 45],k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [45, 90, 135, 180, 225],nums2 = [5, 15, 45],k = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [2, 3, 6, 9, 18],k = 3) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [2, 3, 6, 9, 18],k = 3) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [60, 120, 180, 240],nums2 = [2, 5, 10],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [60, 120, 180, 240],nums2 = [2, 5, 10],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [3, 5, 15],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [3, 5, 15],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [49, 98, 147, 196, 245],nums2 = [7, 49],k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [49, 98, 147, 196, 245],nums2 = [7, 49],k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55],nums2 = [1, 11, 22],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55],nums2 = [1, 11, 22],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],nums2 = [2, 4, 8],k = 8) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],nums2 = [2, 4, 8],k = 8) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [63, 126, 189, 252, 315],nums2 = [9, 21, 63],k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [63, 126, 189, 252, 315],nums2 = [9, 21, 63],k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160],nums2 = [2, 4, 8, 16],k = 8) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160],nums2 = [2, 4, 8, 16],k = 8) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210],nums2 = [3, 7, 21],k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210],nums2 = [3, 7, 21],k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 5, 10],k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 5, 10],k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 198, 297, 396],nums2 = [9, 18, 27, 36],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 198, 297, 396],nums2 = [9, 18, 27, 36],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [16, 32, 48, 64, 80],nums2 = [4, 8, 16],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [16, 32, 48, 64, 80],nums2 = [4, 8, 16],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [6, 9, 18],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [6, 9, 18],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [121, 143, 165, 187],nums2 = [11, 13, 15],k = 11) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [121, 143, 165, 187],nums2 = [11, 13, 15],k = 11) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],nums2 = [3, 6, 9],k = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],nums2 = [3, 6, 9],k = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [3, 6, 12],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [3, 6, 12],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 18, 24, 36, 48],nums2 = [1, 3, 4, 6, 12],k = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 18, 24, 36, 48],nums2 = [1, 3, 4, 6, 12],k = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 150, 200, 250],nums2 = [5, 10, 20],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 150, 200, 250],nums2 = [5, 10, 20],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 40, 60, 80, 100],nums2 = [4, 8, 20],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 40, 60, 80, 100],nums2 = [4, 8, 20],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [3, 5, 15],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [3, 5, 15],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56],nums2 = [1, 7, 14],k = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56],nums2 = [1, 7, 14],k = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [1, 5, 25],k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [1, 5, 25],k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 5, 10],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 5, 10],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, 50, 75, 100, 125, 150],nums2 = [5, 10, 25],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, 50, 75, 100, 125, 150],nums2 = [5, 10, 25],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],nums2 = [1, 11],k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],nums2 = [1, 11],k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [33, 66, 99, 132, 165],nums2 = [11, 33],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [33, 66, 99, 132, 165],nums2 = [11, 33],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [81, 108, 144, 180],nums2 = [9, 18, 27],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [81, 108, 144, 180],nums2 = [9, 18, 27],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [24, 48, 72, 96, 120],nums2 = [8, 12, 24],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [24, 48, 72, 96, 120],nums2 = [8, 12, 24],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [5, 10, 25, 50],k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [5, 10, 25, 50],k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 60, 90, 120],nums2 = [2, 5, 10],k = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 60, 90, 120],nums2 = [2, 5, 10],k = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180],nums2 = [3, 5, 15],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180],nums2 = [3, 5, 15],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [45, 90, 135, 180],nums2 = [3, 9, 15],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [45, 90, 135, 180],nums2 = [3, 9, 15],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [2, 4, 6, 8, 10],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [2, 4, 6, 8, 10],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [24, 36, 48],nums2 = [2, 3, 6, 12],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [24, 36, 48],nums2 = [2, 3, 6, 12],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [21, 42, 63, 84, 105, 126],nums2 = [7, 14, 21],k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [21, 42, 63, 84, 105, 126],nums2 = [7, 14, 21],k = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 18, 24, 30, 36, 42],nums2 = [2, 3, 4],k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 18, 24, 30, 36, 42],nums2 = [2, 3, 4],k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [3, 6, 9],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [3, 6, 9],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81],nums2 = [1, 3, 9],k = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81],nums2 = [1, 3, 9],k = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [2, 4, 8],k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [2, 4, 8],k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [28, 56, 84, 112],nums2 = [7, 14, 21],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [28, 56, 84, 112],nums2 = [7, 14, 21],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, 50, 75, 100, 125, 150],nums2 = [5, 10, 25],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, 50, 75, 100, 125, 150],nums2 = [5, 10, 25],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 25, 35, 45, 55],nums2 = [5, 10, 15],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 25, 35, 45, 55],nums2 = [5, 10, 15],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [1, 7, 14],k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [1, 7, 14],k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [1, 3, 9],k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [1, 3, 9],k = 3) == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [7, 14, 21],nums2 = [1, 7],k = 3) == 2
    assert candidate(nums1 = [1, 3, 4],nums2 = [1, 3, 4],k = 1) == 5
    assert candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 1) == 7
    assert candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 3) == 2
    assert candidate(nums1 = [7, 14, 21],nums2 = [7, 14],k = 1) == 4
    assert candidate(nums1 = [20, 40, 60],nums2 = [5, 10],k = 4) == 4
    assert candidate(nums1 = [5, 10, 15],nums2 = [1, 2, 3],k = 5) == 5
    assert candidate(nums1 = [10, 20, 30],nums2 = [2, 5, 10],k = 1) == 9
    assert candidate(nums1 = [5, 10, 15],nums2 = [1, 5],k = 2) == 2
    assert candidate(nums1 = [10, 20, 30],nums2 = [5, 10],k = 2) == 4
    assert candidate(nums1 = [1, 2, 4, 12],nums2 = [2, 4],k = 3) == 2
    assert candidate(nums1 = [12, 24, 36, 48, 60, 72, 84, 96, 108],nums2 = [4, 8, 12],k = 4) == 5
    assert candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [1, 5, 15],k = 3) == 14
    assert candidate(nums1 = [8, 16, 24, 32],nums2 = [2, 4, 8],k = 2) == 10
    assert candidate(nums1 = [121, 242, 363, 484, 605],nums2 = [11, 121],k = 11) == 5
    assert candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 4) == 16
    assert candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [2, 4, 8],k = 4) == 8
    assert candidate(nums1 = [121, 242, 363, 484, 605],nums2 = [11, 22, 33],k = 11) == 8
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 4, 5, 10],k = 5) == 9
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [5, 10, 20, 25, 50],k = 5) == 17
    assert candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [5, 25],k = 5) == 6
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 4, 5, 10],k = 2) == 10
    assert candidate(nums1 = [20, 40, 60, 80, 100],nums2 = [2, 4, 5, 10],k = 5) == 12
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72],nums2 = [1, 2, 4, 8],k = 2) == 31
    assert candidate(nums1 = [35, 70, 105, 140, 175, 210, 245],nums2 = [5, 7, 35],k = 7) == 9
    assert candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [1, 3, 5, 15],k = 2) == 12
    assert candidate(nums1 = [169, 338, 507, 676, 845],nums2 = [13, 26, 39],k = 13) == 8
    assert candidate(nums1 = [22, 44, 66, 88, 110],nums2 = [1, 2, 11],k = 11) == 10
    assert candidate(nums1 = [28, 56, 84, 112, 140],nums2 = [4, 7, 14],k = 4) == 8
    assert candidate(nums1 = [45, 90, 135, 180, 225],nums2 = [5, 9, 15, 45],k = 5) == 8
    assert candidate(nums1 = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180],nums2 = [1, 2, 3, 4, 6, 9],k = 9) == 32
    assert candidate(nums1 = [225, 450, 675, 900, 1125],nums2 = [15, 30, 75],k = 15) == 8
    assert candidate(nums1 = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196],nums2 = [2, 7, 14],k = 7) == 18
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48, 56],nums2 = [2, 4, 8],k = 2) == 17
    assert candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],nums2 = [1, 13, 26],k = 1) == 25
    assert candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [1, 2, 3, 6, 9],k = 9) == 12
    assert candidate(nums1 = [35, 70, 105, 140, 175, 210, 245, 280, 315, 350],nums2 = [5, 7, 35],k = 5) == 14
    assert candidate(nums1 = [21, 42, 63, 84, 105],nums2 = [3, 7, 21],k = 7) == 5
    assert candidate(nums1 = [49, 98, 147, 196, 245],nums2 = [7, 14, 21],k = 7) == 8
    assert candidate(nums1 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],nums2 = [2, 4, 8],k = 4) == 8
    assert candidate(nums1 = [40, 80, 120, 160, 200, 240, 280, 320],nums2 = [4, 8, 20],k = 4) == 10
    assert candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99],nums2 = [1, 11],k = 11) == 9
    assert candidate(nums1 = [6, 12, 18, 24, 30],nums2 = [1, 2, 3, 4, 5],k = 2) == 14
    assert candidate(nums1 = [35, 70, 105, 140, 175, 210],nums2 = [5, 7, 35],k = 5) == 8
    assert candidate(nums1 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],nums2 = [2, 6, 12],k = 2) == 12
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 5, 10],k = 2) == 9
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [5, 10, 25],k = 10) == 11
    assert candidate(nums1 = [36, 72, 108, 144, 180],nums2 = [2, 3, 6],k = 6) == 15
    assert candidate(nums1 = [42, 84, 126, 168, 210],nums2 = [6, 12, 21],k = 7) == 7
    assert candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],nums2 = [1, 13],k = 13) == 16
    assert candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99],nums2 = [11, 22, 33],k = 1) == 16
    assert candidate(nums1 = [30, 60, 90, 120, 150, 180, 210],nums2 = [2, 5, 10],k = 6) == 13
    assert candidate(nums1 = [6, 12, 18, 24, 30, 36],nums2 = [1, 2, 3, 4, 6],k = 2) == 19
    assert candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [5, 10, 25],k = 5) == 8
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [5, 10, 15],k = 5) == 2
    assert candidate(nums1 = [33, 66, 99, 132, 165],nums2 = [11, 22, 33],k = 3) == 8
    assert candidate(nums1 = [3, 9, 27, 81],nums2 = [1, 3, 9],k = 3) == 9
    assert candidate(nums1 = [64, 128, 192, 256, 320],nums2 = [8, 16, 32],k = 4) == 12
    assert candidate(nums1 = [14, 28, 42, 56, 70],nums2 = [7, 14, 28],k = 2) == 8
    assert candidate(nums1 = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270],nums2 = [3, 6, 9, 18],k = 9) == 12
    assert candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [3, 5, 15],k = 5) == 7
    assert candidate(nums1 = [45, 90, 135, 180, 225],nums2 = [5, 15, 45],k = 3) == 11
    assert candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [2, 3, 6, 9, 18],k = 3) == 17
    assert candidate(nums1 = [60, 120, 180, 240],nums2 = [2, 5, 10],k = 4) == 8
    assert candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [3, 5, 15],k = 5) == 8
    assert candidate(nums1 = [49, 98, 147, 196, 245],nums2 = [7, 49],k = 7) == 5
    assert candidate(nums1 = [11, 22, 33, 44, 55],nums2 = [1, 11, 22],k = 5) == 2
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],nums2 = [2, 4, 8],k = 8) == 10
    assert candidate(nums1 = [63, 126, 189, 252, 315],nums2 = [9, 21, 63],k = 9) == 1
    assert candidate(nums1 = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160],nums2 = [2, 4, 8, 16],k = 8) == 18
    assert candidate(nums1 = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210],nums2 = [3, 7, 21],k = 7) == 12
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 5, 10],k = 10) == 13
    assert candidate(nums1 = [99, 198, 297, 396],nums2 = [9, 18, 27, 36],k = 9) == 0
    assert candidate(nums1 = [16, 32, 48, 64, 80],nums2 = [4, 8, 16],k = 4) == 8
    assert candidate(nums1 = [18, 36, 54, 72, 90],nums2 = [6, 9, 18],k = 3) == 7
    assert candidate(nums1 = [121, 143, 165, 187],nums2 = [11, 13, 15],k = 11) == 3
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],nums2 = [3, 6, 9],k = 3) == 18
    assert candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [3, 6, 12],k = 4) == 8
    assert candidate(nums1 = [12, 18, 24, 36, 48],nums2 = [1, 3, 4, 6, 12],k = 2) == 18
    assert candidate(nums1 = [100, 150, 200, 250],nums2 = [5, 10, 20],k = 5) == 10
    assert candidate(nums1 = [20, 40, 60, 80, 100],nums2 = [4, 8, 20],k = 5) == 8
    assert candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [3, 5, 15],k = 3) == 7
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56],nums2 = [1, 7, 14],k = 1) == 20
    assert candidate(nums1 = [25, 50, 75, 100, 125],nums2 = [1, 5, 25],k = 5) == 11
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [2, 5, 10],k = 5) == 7
    assert candidate(nums1 = [25, 50, 75, 100, 125, 150],nums2 = [5, 10, 25],k = 5) == 10
    assert candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],nums2 = [1, 11],k = 11) == 10
    assert candidate(nums1 = [33, 66, 99, 132, 165],nums2 = [11, 33],k = 3) == 6
    assert candidate(nums1 = [81, 108, 144, 180],nums2 = [9, 18, 27],k = 3) == 4
    assert candidate(nums1 = [24, 48, 72, 96, 120],nums2 = [8, 12, 24],k = 4) == 4
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [5, 10, 25, 50],k = 10) == 18
    assert candidate(nums1 = [30, 60, 90, 120],nums2 = [2, 5, 10],k = 6) == 8
    assert candidate(nums1 = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180],nums2 = [3, 5, 15],k = 5) == 16
    assert candidate(nums1 = [45, 90, 135, 180],nums2 = [3, 9, 15],k = 5) == 8
    assert candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [2, 4, 6, 8, 10],k = 4) == 5
    assert candidate(nums1 = [24, 36, 48],nums2 = [2, 3, 6, 12],k = 4) == 8
    assert candidate(nums1 = [21, 42, 63, 84, 105, 126],nums2 = [7, 14, 21],k = 3) == 11
    assert candidate(nums1 = [12, 18, 24, 30, 36, 42],nums2 = [2, 3, 4],k = 6) == 6
    assert candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [3, 6, 9],k = 3) == 8
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81],nums2 = [1, 3, 9],k = 3) == 21
    assert candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [2, 4, 8],k = 2) == 12
    assert candidate(nums1 = [28, 56, 84, 112],nums2 = [7, 14, 21],k = 7) == 0
    assert candidate(nums1 = [25, 50, 75, 100, 125, 150],nums2 = [5, 10, 25],k = 5) == 10
    assert candidate(nums1 = [15, 25, 35, 45, 55],nums2 = [5, 10, 15],k = 5) == 1
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [1, 7, 14],k = 7) == 8
    assert candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [1, 3, 9],k = 3) == 11


