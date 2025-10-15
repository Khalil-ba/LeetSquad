def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 4],nums2 = [1, 3, 4],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 4],nums2 = [1, 3, 4],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [10, 20, 30],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [10, 20, 30],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15],nums2 = [1, 5, 10],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15],nums2 = [1, 5, 10],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 28],nums2 = [1, 2, 4],k = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 28],nums2 = [1, 2, 4],k = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 12],nums2 = [2, 4],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 12],nums2 = [2, 4],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [5, 10, 15],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [5, 10, 15],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 2, 5],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 2, 5],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 999998, 999997, 999996, 999995],nums2 = [1, 2, 3, 4, 5],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 999998, 999997, 999996, 999995],nums2 = [1, 2, 3, 4, 5],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [1, 2, 3, 4, 5, 6, 7],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [1, 2, 3, 4, 5, 6, 7],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [1, 7, 14, 21, 28, 35],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [1, 7, 14, 21, 28, 35],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24, 30],nums2 = [2, 3, 6],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24, 30],nums2 = [2, 3, 6],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [5, 10, 15, 20, 25, 30],k = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [5, 10, 15, 20, 25, 30],k = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 2) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 2) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 200000, 300000, 400000],nums2 = [100, 200, 300, 400],k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 200000, 300000, 400000],nums2 = [100, 200, 300, 400],k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [120, 180, 240, 300],nums2 = [5, 10, 15, 20, 25, 30],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [120, 180, 240, 300],nums2 = [5, 10, 15, 20, 25, 30],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [72, 144, 216, 288, 360],nums2 = [8, 12, 24, 36],k = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [72, 144, 216, 288, 360],nums2 = [8, 12, 24, 36],k = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [810, 1620, 2430, 3240, 4050, 4860, 5490, 6120, 6840, 7560],nums2 = [5, 10, 15, 18, 20, 25, 30, 45, 60, 90],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [810, 1620, 2430, 3240, 4050, 4860, 5490, 6120, 6840, 7560],nums2 = [5, 10, 15, 18, 20, 25, 30, 45, 60, 90],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [500000, 750000, 1000000, 1250000, 1500000],nums2 = [100, 250, 500, 1250, 2500],k = 20) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [500000, 750000, 1000000, 1250000, 1500000],nums2 = [100, 250, 500, 1250, 2500],k = 20) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [987654, 876543, 765432, 654321, 543210],nums2 = [98765, 87654, 76543, 65432, 54321],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [987654, 876543, 765432, 654321, 543210],nums2 = [98765, 87654, 76543, 65432, 54321],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [210, 330, 450, 570],nums2 = [3, 6, 9, 12],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [210, 330, 450, 570],nums2 = [3, 6, 9, 12],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [101, 202, 303, 404, 505],nums2 = [1, 101, 202, 303, 404],k = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [101, 202, 303, 404, 505],nums2 = [1, 101, 202, 303, 404],k = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [333, 666, 999, 1332, 1665],nums2 = [3, 6, 9, 12, 15],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [333, 666, 999, 1332, 1665],nums2 = [3, 6, 9, 12, 15],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 999998, 999997],nums2 = [999, 998, 997],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 999998, 999997],nums2 = [999, 998, 997],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [987654321, 987654322, 987654323, 987654324],nums2 = [987, 988, 989, 990],k = 987) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [987654321, 987654322, 987654323, 987654324],nums2 = [987, 988, 989, 990],k = 987) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 999998, 999997, 999996, 999995],nums2 = [999, 998, 997, 996, 995],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 999998, 999997, 999996, 999995],nums2 = [999, 998, 997, 996, 995],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [104729, 209458, 314187, 418916, 523645, 628374, 733103, 837832, 942561],nums2 = [104729, 209458, 314187],k = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [104729, 209458, 314187, 418916, 523645, 628374, 733103, 837832, 942561],nums2 = [104729, 209458, 314187],k = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [120, 150, 180, 210],nums2 = [3, 5, 6, 7],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [120, 150, 180, 210],nums2 = [3, 5, 6, 7],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [1000, 2000, 3000, 4000, 5000],k = 500) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [1000, 2000, 3000, 4000, 5000],k = 500) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [333, 666, 999, 1332, 1665],nums2 = [3, 9, 27, 81],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [333, 666, 999, 1332, 1665],nums2 = [3, 9, 27, 81],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],nums2 = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],nums2 = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 999999, 999998],nums2 = [1, 2, 3, 4, 5],k = 1000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 999999, 999998],nums2 = [1, 2, 3, 4, 5],k = 1000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 2000000, 3000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 2000000, 3000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [500, 1000, 1500, 2000, 2500],nums2 = [5, 10, 25],k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [500, 1000, 1500, 2000, 2500],nums2 = [5, 10, 25],k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 1000000, 1000000, 1000000],nums2 = [1, 2, 4, 5],k = 1000) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 1000000, 1000000, 1000000],nums2 = [1, 2, 4, 5],k = 1000) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [10, 20, 30, 40, 50],k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [10, 20, 30, 40, 50],k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],nums2 = [1, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],nums2 = [1, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [500, 1000, 1500, 2000, 2500],nums2 = [25, 50, 75],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [500, 1000, 1500, 2000, 2500],nums2 = [25, 50, 75],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [987654, 321456, 789123, 123456, 456789],nums2 = [123, 321, 654, 456, 789],k = 23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [987654, 321456, 789123, 123456, 456789],nums2 = [123, 321, 654, 456, 789],k = 23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [111111, 222222, 333333, 444444, 555555],nums2 = [11, 22, 33, 44, 55],k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [111111, 222222, 333333, 444444, 555555],nums2 = [11, 22, 33, 44, 55],k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [555555, 666666, 777777, 888888, 999999],nums2 = [5, 6, 7, 8, 9, 55, 66, 77, 88, 99],k = 111) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [555555, 666666, 777777, 888888, 999999],nums2 = [5, 6, 7, 8, 9, 55, 66, 77, 88, 99],k = 111) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [300000, 300000, 300000, 300000, 300000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [300000, 300000, 300000, 300000, 300000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [101, 202, 303, 404, 505, 606, 707, 808, 909],nums2 = [1, 10, 100, 1000],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [101, 202, 303, 404, 505, 606, 707, 808, 909],nums2 = [1, 10, 100, 1000],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 888888, 777777, 666666, 555555],nums2 = [111111, 222222, 333333, 444444, 555555],k = 111) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 888888, 777777, 666666, 555555],nums2 = [111111, 222222, 333333, 444444, 555555],k = 111) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1024, 2048, 4096, 8192],nums2 = [32, 64, 128],k = 16) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1024, 2048, 4096, 8192],nums2 = [32, 64, 128],k = 16) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345, 456],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345, 456],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999, 888888, 777777, 666666],nums2 = [333333, 222222, 111111],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999, 888888, 777777, 666666],nums2 = [333333, 222222, 111111],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [10, 20, 30, 40, 50],k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [10, 20, 30, 40, 50],k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 500000, 250000, 125000, 62500],nums2 = [125, 250, 500],k = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 500000, 250000, 125000, 62500],nums2 = [125, 250, 500],k = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [210, 420, 630, 840, 1050],nums2 = [1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210],k = 2) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [210, 420, 630, 840, 1050],nums2 = [1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210],k = 2) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 200000, 300000, 400000, 500000],nums2 = [50000, 100000, 150000, 200000, 250000],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 200000, 300000, 400000, 500000],nums2 = [50000, 100000, 150000, 200000, 250000],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999],nums2 = [1, 3, 9, 27, 81],k = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999],nums2 = [1, 3, 9, 27, 81],k = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 234567, 345678, 456789, 567890],nums2 = [123, 456, 789],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 234567, 345678, 456789, 567890],nums2 = [123, 456, 789],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12345, 67890, 11111, 22222, 33333],nums2 = [3, 9, 27, 81, 243],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12345, 67890, 11111, 22222, 33333],nums2 = [3, 9, 27, 81, 243],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1, 2, 5, 10, 20],k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1, 2, 5, 10, 20],k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [101, 202, 303, 404, 505],nums2 = [1, 2, 3, 4, 5, 6],k = 101) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [101, 202, 303, 404, 505],nums2 = [1, 2, 3, 4, 5, 6],k = 101) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 1000000, 1000000],nums2 = [1, 10, 100, 1000],k = 100) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 1000000, 1000000],nums2 = [1, 10, 100, 1000],k = 100) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [500000, 600000, 700000, 800000],nums2 = [50000, 60000, 70000, 80000],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [500000, 600000, 700000, 800000],nums2 = [50000, 60000, 70000, 80000],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [987654, 456789, 123456, 654321],nums2 = [6, 12, 18, 24, 30, 36, 42],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [987654, 456789, 123456, 654321],nums2 = [6, 12, 18, 24, 30, 36, 42],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [987654, 987654, 987654, 987654, 987654],nums2 = [123456, 246912, 370368, 493824, 617280],k = 61728) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [987654, 987654, 987654, 987654, 987654],nums2 = [123456, 246912, 370368, 493824, 617280],k = 61728) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [97, 194, 291, 388, 485],nums2 = [1, 97, 194],k = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [97, 194, 291, 388, 485],nums2 = [1, 97, 194],k = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [77, 143, 209, 275],nums2 = [7, 11, 13, 17],k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [77, 143, 209, 275],nums2 = [7, 11, 13, 17],k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 1000000, 1000000, 1000000, 1000000],nums2 = [1, 1, 1, 1, 1],k = 1000000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 1000000, 1000000, 1000000, 1000000],nums2 = [1, 1, 1, 1, 1],k = 1000000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [555555, 444444, 333333, 222222, 111111],nums2 = [111111, 222222, 333333, 444444, 555555],k = 11111) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [555555, 444444, 333333, 222222, 111111],nums2 = [111111, 222222, 333333, 444444, 555555],k = 11111) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [21, 42, 63, 84, 105],nums2 = [3, 7, 21],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [21, 42, 63, 84, 105],nums2 = [3, 7, 21],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 2, 4, 5, 10, 20, 25, 50, 100],k = 1) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 2, 4, 5, 10, 20, 25, 50, 100],k = 1) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5],k = 1) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5],k = 1) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [1, 2, 3, 4, 5, 6, 7],k = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [1, 2, 3, 4, 5, 6, 7],k = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],nums2 = [5, 10, 15, 20, 25],k = 50) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],nums2 = [5, 10, 15, 20, 25],k = 50) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100000) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100000) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345, 456],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345, 456],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 2) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 2) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 654321, 111111, 222222],nums2 = [123, 321, 111, 222, 444],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 654321, 111111, 222222],nums2 = [123, 321, 111, 222, 444],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1024, 2048, 4096, 8192, 16384],nums2 = [16, 32, 64, 128, 256],k = 32) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1024, 2048, 4096, 8192, 16384],nums2 = [16, 32, 64, 128, 256],k = 32) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 67: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 200000, 300000, 400000],nums2 = [1, 2, 3, 4, 5],k = 100) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 200000, 300000, 400000],nums2 = [1, 2, 3, 4, 5],k = 100) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 900000, 800000, 700000],nums2 = [100, 200, 300, 400],k = 25) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 900000, 800000, 700000],nums2 = [100, 200, 300, 400],k = 25) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 30],k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 30],k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 234567, 345678, 456789, 567890],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 123) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 234567, 345678, 456789, 567890],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 123) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [1, 5, 10, 15, 20, 25, 30],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [1, 5, 10, 15, 20, 25, 30],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9],k = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9],k = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [111111, 222222, 333333, 444444, 555555],nums2 = [111, 222, 333, 444, 555],k = 111) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [111111, 222222, 333333, 444444, 555555],nums2 = [111, 222, 333, 444, 555],k = 111) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 200000, 300000, 400000, 500000, 600000],nums2 = [100, 200, 300, 400, 500, 600],k = 1000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 200000, 300000, 400000, 500000, 600000],nums2 = [100, 200, 300, 400, 500, 600],k = 1000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [777777, 888888, 999999],nums2 = [7, 8, 9, 77, 88, 99, 777, 888, 999],k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [777777, 888888, 999999],nums2 = [7, 8, 9, 77, 88, 99, 777, 888, 999],k = 11) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [7, 14, 21],nums2 = [1, 7, 14],k = 7) == 3
    assert candidate(nums1 = [1, 3, 4],nums2 = [1, 3, 4],k = 1) == 5
    assert candidate(nums1 = [100, 200, 300],nums2 = [10, 20, 30],k = 10) == 5
    assert candidate(nums1 = [5, 10, 15],nums2 = [1, 5, 10],k = 1) == 7
    assert candidate(nums1 = [7, 14, 28],nums2 = [1, 2, 4],k = 7) == 6
    assert candidate(nums1 = [1, 2, 4, 12],nums2 = [2, 4],k = 3) == 2
    assert candidate(nums1 = [100, 200, 300],nums2 = [5, 10, 15],k = 5) == 7
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 2, 5],k = 2) == 5
    assert candidate(nums1 = [999999, 999998, 999997, 999996, 999995],nums2 = [1, 2, 3, 4, 5],k = 100) == 0
    assert candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [1, 2, 3, 4, 5, 6, 7],k = 7) == 10
    assert candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [1, 7, 14, 21, 28, 35],k = 1) == 15
    assert candidate(nums1 = [6, 12, 18, 24, 30],nums2 = [2, 3, 6],k = 2) == 9
    assert candidate(nums1 = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 0
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [5, 10, 15, 20, 25, 30],k = 10) == 22
    assert candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 2) == 23
    assert candidate(nums1 = [100000, 200000, 300000, 400000],nums2 = [100, 200, 300, 400],k = 10) == 13
    assert candidate(nums1 = [120, 180, 240, 300],nums2 = [5, 10, 15, 20, 25, 30],k = 6) == 13
    assert candidate(nums1 = [72, 144, 216, 288, 360],nums2 = [8, 12, 24, 36],k = 3) == 16
    assert candidate(nums1 = [810, 1620, 2430, 3240, 4050, 4860, 5490, 6120, 6840, 7560],nums2 = [5, 10, 15, 18, 20, 25, 30, 45, 60, 90],k = 5) == 16
    assert candidate(nums1 = [500000, 750000, 1000000, 1250000, 1500000],nums2 = [100, 250, 500, 1250, 2500],k = 20) == 25
    assert candidate(nums1 = [987654, 876543, 765432, 654321, 543210],nums2 = [98765, 87654, 76543, 65432, 54321],k = 10) == 1
    assert candidate(nums1 = [210, 330, 450, 570],nums2 = [3, 6, 9, 12],k = 5) == 9
    assert candidate(nums1 = [101, 202, 303, 404, 505],nums2 = [1, 101, 202, 303, 404],k = 1) == 14
    assert candidate(nums1 = [333, 666, 999, 1332, 1665],nums2 = [3, 6, 9, 12, 15],k = 3) == 10
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 50
    assert candidate(nums1 = [999999, 999998, 999997],nums2 = [999, 998, 997],k = 1) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 25
    assert candidate(nums1 = [987654321, 987654322, 987654323, 987654324],nums2 = [987, 988, 989, 990],k = 987) == 0
    assert candidate(nums1 = [999999, 999998, 999997, 999996, 999995],nums2 = [999, 998, 997, 996, 995],k = 1000) == 0
    assert candidate(nums1 = [104729, 209458, 314187, 418916, 523645, 628374, 733103, 837832, 942561],nums2 = [104729, 209458, 314187],k = 1) == 16
    assert candidate(nums1 = [120, 150, 180, 210],nums2 = [3, 5, 6, 7],k = 4) == 5
    assert candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [1000, 2000, 3000, 4000, 5000],k = 500) == 14
    assert candidate(nums1 = [333, 666, 999, 1332, 1665],nums2 = [3, 9, 27, 81],k = 3) == 6
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 100
    assert candidate(nums1 = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],nums2 = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 10) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
    assert candidate(nums1 = [1000000, 999999, 999998],nums2 = [1, 2, 3, 4, 5],k = 1000) == 4
    assert candidate(nums1 = [1000000, 2000000, 3000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000) == 20
    assert candidate(nums1 = [500, 1000, 1500, 2000, 2500],nums2 = [5, 10, 25],k = 4) == 12
    assert candidate(nums1 = [1000000, 1000000, 1000000, 1000000],nums2 = [1, 2, 4, 5],k = 1000) == 16
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [10, 20, 30, 40, 50],k = 5) == 14
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],nums2 = [1, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 11
    assert candidate(nums1 = [500, 1000, 1500, 2000, 2500],nums2 = [25, 50, 75],k = 2) == 11
    assert candidate(nums1 = [987654, 321456, 789123, 123456, 456789],nums2 = [123, 321, 654, 456, 789],k = 23) == 0
    assert candidate(nums1 = [111111, 222222, 333333, 444444, 555555],nums2 = [11, 22, 33, 44, 55],k = 11) == 0
    assert candidate(nums1 = [555555, 666666, 777777, 888888, 999999],nums2 = [5, 6, 7, 8, 9, 55, 66, 77, 88, 99],k = 111) == 18
    assert candidate(nums1 = [300000, 300000, 300000, 300000, 300000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15000) == 25
    assert candidate(nums1 = [101, 202, 303, 404, 505, 606, 707, 808, 909],nums2 = [1, 10, 100, 1000],k = 1) == 9
    assert candidate(nums1 = [999999, 888888, 777777, 666666, 555555],nums2 = [111111, 222222, 333333, 444444, 555555],k = 111) == 0
    assert candidate(nums1 = [1024, 2048, 4096, 8192],nums2 = [32, 64, 128],k = 16) == 11
    assert candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345, 456],k = 7) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 100
    assert candidate(nums1 = [999999, 888888, 777777, 666666],nums2 = [333333, 222222, 111111],k = 3) == 4
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [10, 20, 30, 40, 50],k = 10) == 18
    assert candidate(nums1 = [1000000, 500000, 250000, 125000, 62500],nums2 = [125, 250, 500],k = 2) == 14
    assert candidate(nums1 = [210, 420, 630, 840, 1050],nums2 = [1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210],k = 2) == 56
    assert candidate(nums1 = [100000, 200000, 300000, 400000, 500000],nums2 = [50000, 100000, 150000, 200000, 250000],k = 1000) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 25
    assert candidate(nums1 = [999999],nums2 = [1, 3, 9, 27, 81],k = 10000) == 0
    assert candidate(nums1 = [123456, 234567, 345678, 456789, 567890],nums2 = [123, 456, 789],k = 12) == 0
    assert candidate(nums1 = [12345, 67890, 11111, 22222, 33333],nums2 = [3, 9, 27, 81, 243],k = 3) == 0
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1, 2, 5, 10, 20],k = 25) == 25
    assert candidate(nums1 = [101, 202, 303, 404, 505],nums2 = [1, 2, 3, 4, 5, 6],k = 101) == 10
    assert candidate(nums1 = [1000000, 1000000, 1000000],nums2 = [1, 10, 100, 1000],k = 100) == 12
    assert candidate(nums1 = [500000, 600000, 700000, 800000],nums2 = [50000, 60000, 70000, 80000],k = 10) == 4
    assert candidate(nums1 = [987654, 456789, 123456, 654321],nums2 = [6, 12, 18, 24, 30, 36, 42],k = 7) == 0
    assert candidate(nums1 = [987654, 987654, 987654, 987654, 987654],nums2 = [123456, 246912, 370368, 493824, 617280],k = 61728) == 0
    assert candidate(nums1 = [97, 194, 291, 388, 485],nums2 = [1, 97, 194],k = 1) == 12
    assert candidate(nums1 = [77, 143, 209, 275],nums2 = [7, 11, 13, 17],k = 1) == 6
    assert candidate(nums1 = [1000000, 1000000, 1000000, 1000000, 1000000],nums2 = [1, 1, 1, 1, 1],k = 1000000) == 25
    assert candidate(nums1 = [555555, 444444, 333333, 222222, 111111],nums2 = [111111, 222222, 333333, 444444, 555555],k = 11111) == 0
    assert candidate(nums1 = [21, 42, 63, 84, 105],nums2 = [3, 7, 21],k = 1) == 15
    assert candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 2, 4, 5, 10, 20, 25, 50, 100],k = 1) == 90
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5],k = 1) == 22
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [1, 2, 3, 4, 5, 6, 7],k = 7) == 16
    assert candidate(nums1 = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],nums2 = [5, 10, 15, 20, 25],k = 50) == 21
    assert candidate(nums1 = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100000) == 40
    assert candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345, 456],k = 3) == 0
    assert candidate(nums1 = [123456, 234567, 345678, 456789],nums2 = [123, 234, 345],k = 6) == 0
    assert candidate(nums1 = [12, 24, 36, 48, 60],nums2 = [1, 2, 3, 4, 5, 6],k = 2) == 23
    assert candidate(nums1 = [123456, 654321, 111111, 222222],nums2 = [123, 321, 111, 222, 444],k = 3) == 0
    assert candidate(nums1 = [1024, 2048, 4096, 8192, 16384],nums2 = [16, 32, 64, 128, 256],k = 32) == 19
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 67
    assert candidate(nums1 = [100000, 200000, 300000, 400000],nums2 = [1, 2, 3, 4, 5],k = 100) == 17
    assert candidate(nums1 = [1000000, 900000, 800000, 700000],nums2 = [100, 200, 300, 400],k = 25) == 13
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 40
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 30],k = 4) == 6
    assert candidate(nums1 = [123456, 234567, 345678, 456789, 567890],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 123) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [1, 5, 10, 15, 20, 25, 30],k = 5) == 7
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9],k = 1) == 17
    assert candidate(nums1 = [111111, 222222, 333333, 444444, 555555],nums2 = [111, 222, 333, 444, 555],k = 111) == 0
    assert candidate(nums1 = [100000, 200000, 300000, 400000, 500000, 600000],nums2 = [100, 200, 300, 400, 500, 600],k = 1000) == 14
    assert candidate(nums1 = [777777, 888888, 999999],nums2 = [7, 8, 9, 77, 88, 99, 777, 888, 999],k = 11) == 10


