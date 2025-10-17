def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [20, 50, 9, 63]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 50, 9, 63]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 7, 4, 12, 21, 39]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 7, 4, 12, 21, 39]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 20, 5, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 20, 5, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 11, 13]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 11, 13]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 42, 70, 28, 10, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 42, 70, 28, 10, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 42, 66, 55]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 42, 66, 55]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 5, 23, 31, 37, 41, 43, 47, 53]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 5, 23, 31, 37, 41, 43, 47, 53]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 15, 35]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 15, 35]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 42, 70, 28]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 42, 70, 28]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [105, 210, 315, 420, 525, 630]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [105, 210, 315, 420, 525, 630]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 90, 120, 135, 180, 225, 270, 315, 360, 405, 450, 495]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 90, 120, 135, 180, 225, 270, 315, 360, 405, 450, 495]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 30, 90, 120, 180, 210, 240, 300]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 30, 90, 120, 180, 210, 240, 300]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [28, 49, 98, 147, 196, 245, 294, 343, 392, 441, 490, 539, 588, 637, 686]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [28, 49, 98, 147, 196, 245, 294, 343, 392, 441, 490, 539, 588, 637, 686]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 10, 14, 15, 21, 22, 26, 33, 35, 38, 39, 44, 45, 46, 51, 55, 57, 58, 62, 65, 66, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 10, 14, 15, 21, 22, 26, 33, 35, 38, 39, 44, 45, 46, 51, 55, 57, 58, 62, 65, 66, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 135, 189, 243, 315, 378, 459, 513, 567, 639, 693, 756, 819, 873, 945]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 135, 189, 243, 315, 378, 459, 513, 567, 639, 693, 756, 819, 873, 945]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [840, 1680, 2520, 3360, 4200, 5040, 5880, 6720, 7560, 8400, 9240, 10080, 10920, 11760, 12600]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [840, 1680, 2520, 3360, 4200, 5040, 5880, 6720, 7560, 8400, 9240, 10080, 10920, 11760, 12600]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 84, 112, 140, 168, 196, 224, 252, 280, 308, 336, 364, 392]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 84, 112, 140, 168, 196, 224, 252, 280, 308, 336, 364, 392]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 98, 168, 224, 231, 252, 336, 392, 441, 462, 504, 539, 616, 672, 784, 882, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1596, 1680, 1764, 1848, 1932, 2016, 2100]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 98, 168, 224, 231, 252, 336, 392, 441, 462, 504, 539, 616, 672, 784, 882, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1596, 1680, 1764, 1848, 1932, 2016, 2100]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2520, 5040, 10080, 20160, 40320]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2520, 5040, 10080, 20160, 40320]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30030, 30031, 30032, 30033, 30034, 30035, 30036, 30037, 30038, 30039, 30040, 30041, 30042, 30043, 30044, 30045, 30046, 30047, 30048, 30049, 30050, 30051, 30052, 30053, 30054, 30055]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30030, 30031, 30032, 30033, 30034, 30035, 30036, 30037, 30038, 30039, 30040, 30041, 30042, 30043, 30044, 30045, 30046, 30047, 30048, 30049, 30050, 30051, 30052, 30053, 30054, 30055]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1024, 1050, 1080, 1100, 1120, 1140, 1150, 1170, 1190, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1024, 1050, 1080, 1100, 1120, 1140, 1150, 1170, 1190, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 100, 150, 200, 250, 300]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 100, 150, 200, 250, 300]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 194, 291, 388, 485, 582, 679, 776, 873, 970, 1067, 1164, 1261, 1358, 1455, 1552, 1649, 1746, 1843, 1940]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 194, 291, 388, 485, 582, 679, 776, 873, 970, 1067, 1164, 1261, 1358, 1455, 1552, 1649, 1746, 1843, 1940]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [105, 115, 130, 140, 154, 165, 170, 182, 187, 195, 210, 220, 221, 231, 238, 247, 253, 260, 273, 286, 299]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [105, 115, 130, 140, 154, 165, 170, 182, 187, 195, 210, 220, 221, 231, 238, 247, 253, 260, 273, 286, 299]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 420, 630, 840, 1050, 1260, 1470, 1680, 1890, 2100, 2310, 2520, 2730, 2940, 3150]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 420, 630, 840, 1050, 1260, 1470, 1680, 1890, 2100, 2310, 2520, 2730, 2940, 3150]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 121, 143, 165, 187, 209, 231, 253, 275, 297, 319, 330, 352, 374, 396, 418, 440, 462, 484, 506]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 121, 143, 165, 187, 209, 231, 253, 275, 297, 319, 330, 352, 374, 396, 418, 440, 462, 484, 506]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10001, 20002, 30003, 40004, 50005, 60006, 70007, 80008, 90009, 100010]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10001, 20002, 30003, 40004, 50005, 60006, 70007, 80008, 90009, 100010]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 35, 55, 77, 91, 119, 143, 165, 187, 209, 231, 253, 286, 308, 330]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 35, 55, 77, 91, 119, 143, 165, 187, 209, 231, 253, 286, 308, 330]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 330, 462, 594, 726, 858, 990, 1122, 1254, 1386, 1518, 1650, 1782, 1914, 2046]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 330, 462, 594, 726, 858, 990, 1122, 1254, 1386, 1518, 1650, 1782, 1914, 2046]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 65, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 143, 154, 165, 182, 210, 231, 252]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 65, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 143, 154, 165, 182, 210, 231, 252]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44, 66, 100, 121, 143, 165]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44, 66, 100, 121, 143, 165]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 100, 140, 210, 280, 350, 420, 500, 560, 630, 700, 770, 840, 910, 980, 1050, 1120, 1190, 1260, 1330, 1400, 1470, 1540, 1610, 1680, 1750, 1820, 1890, 1960, 2030]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 100, 140, 210, 280, 350, 420, 500, 560, 630, 700, 770, 840, 910, 980, 1050, 1120, 1190, 1260, 1330, 1400, 1470, 1540, 1610, 1680, 1750, 1820, 1890, 1960, 2030]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [840, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1596, 1680, 1764, 1848, 1932, 2016, 2100, 2184, 2268, 2352, 2436, 2520]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [840, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1596, 1680, 1764, 1848, 1932, 2016, 2100, 2184, 2268, 2352, 2436, 2520]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 45, 75, 105, 135, 165, 195, 225, 255, 285, 315, 345, 375, 405, 435, 465, 495, 525, 555, 585]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 45, 75, 105, 135, 165, 195, 225, 255, 285, 315, 345, 375, 405, 435, 465, 495, 525, 555, 585]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609, 630, 651, 672, 693, 714, 735, 756, 777, 798, 819, 840, 861, 882, 903, 924, 945, 966, 987, 1008, 1029]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609, 630, 651, 672, 693, 714, 735, 756, 777, 798, 819, 840, 861, 882, 903, 924, 945, 966, 987, 1008, 1029]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104729, 104731, 104743, 104759, 104761, 104771, 104773, 104777, 104783, 104791, 104797, 104801, 104807, 104813, 104819, 104831, 104833, 104837, 104839, 104843, 104857, 104858, 104861, 104863, 104867, 104869]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104729, 104731, 104743, 104759, 104761, 104771, 104773, 104777, 104783, 104791, 104797, 104801, 104807, 104813, 104819, 104831, 104833, 104837, 104839, 104843, 104857, 104858, 104861, 104863, 104867, 104869]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 10, 14, 15, 21, 22, 26, 28, 33, 35, 39, 44, 45, 55, 65, 77, 88, 99, 105, 110]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 10, 14, 15, 21, 22, 26, 28, 33, 35, 39, 44, 45, 55, 65, 77, 88, 99, 105, 110]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 121, 169, 225, 289, 361, 441, 529, 625, 729]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 121, 169, 225, 289, 361, 441, 529, 625, 729]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 105, 108, 110, 112, 114, 115, 117, 119]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 105, 108, 110, 112, 114, 115, 117, 119]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 15, 25, 45, 75, 105, 125, 135, 175, 225, 245, 315, 375, 525]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 15, 25, 45, 75, 105, 125, 135, 175, 225, 245, 315, 375, 525]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44, 88, 132, 176, 220, 264, 308, 352, 396, 440, 484, 528, 572, 616, 660]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44, 88, 132, 176, 220, 264, 308, 352, 396, 440, 484, 528, 572, 616, 660]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 104, 105, 106, 108, 110, 112, 114, 115, 117, 119, 121, 122, 123, 124, 126, 128, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142, 143, 145]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 104, 105, 106, 108, 110, 112, 114, 115, 117, 119, 121, 122, 123, 124, 126, 128, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142, 143, 145]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 105, 110, 115, 120]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 105, 110, 115, 120]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [154, 308, 462, 616, 770, 924, 1078, 1232, 1386, 1540, 1694, 1848, 2002, 2156, 2310]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [154, 308, 462, 616, 770, 924, 1078, 1232, 1386, 1540, 1694, 1848, 2002, 2156, 2310]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 42, 70, 105, 210]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 42, 70, 105, 210]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 63, 77, 91, 105, 119, 133, 147, 161, 175, 189, 203, 217, 231, 245]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 63, 77, 91, 105, 119, 133, 147, 161, 175, 189, 203, 217, 231, 245]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 24, 30, 42, 56, 72, 84, 90]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 24, 30, 42, 56, 72, 84, 90]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [77, 91, 119, 133, 143, 161, 187, 209, 221, 231, 247, 253, 287, 299, 319]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [77, 91, 119, 133, 143, 161, 187, 209, 221, 231, 247, 253, 287, 299, 319]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [20, 50, 9, 63]) == 2
    assert candidate(nums = [2, 3, 6, 7, 4, 12, 21, 39]) == 8
    assert candidate(nums = [30, 60, 20, 5, 15]) == 5
    assert candidate(nums = [5, 7, 11, 13]) == 1
    assert candidate(nums = [30, 42, 70, 28, 10, 5]) == 6
    assert candidate(nums = [30, 42, 66, 55]) == 4
    assert candidate(nums = [7, 3, 5, 23, 31, 37, 41, 43, 47, 53]) == 1
    assert candidate(nums = [4, 6, 15, 35]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(nums = [30, 42, 70, 28]) == 4
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 8
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]) == 23
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 10
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 15
    assert candidate(nums = [105, 210, 315, 420, 525, 630]) == 6
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10
    assert candidate(nums = [45, 90, 120, 135, 180, 225, 270, 315, 360, 405, 450, 495]) == 12
    assert candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 11
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 15
    assert candidate(nums = [100, 150, 200, 250, 300, 350]) == 6
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]) == 11
    assert candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 10
    assert candidate(nums = [60, 30, 90, 120, 180, 210, 240, 300]) == 8
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1
    assert candidate(nums = [28, 49, 98, 147, 196, 245, 294, 343, 392, 441, 490, 539, 588, 637, 686]) == 15
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]) == 1
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 1
    assert candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253]) == 20
    assert candidate(nums = [6, 10, 14, 15, 21, 22, 26, 33, 35, 38, 39, 44, 45, 46, 51, 55, 57, 58, 62, 65, 66, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106]) == 33
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 19
    assert candidate(nums = [21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 12
    assert candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330]) == 20
    assert candidate(nums = [81, 135, 189, 243, 315, 378, 459, 513, 567, 639, 693, 756, 819, 873, 945]) == 15
    assert candidate(nums = [840, 1680, 2520, 3360, 4200, 5040, 5880, 6720, 7560, 8400, 9240, 10080, 10920, 11760, 12600]) == 15
    assert candidate(nums = [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]) == 16
    assert candidate(nums = [961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980]) == 16
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 20
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 8
    assert candidate(nums = [56, 84, 112, 140, 168, 196, 224, 252, 280, 308, 336, 364, 392]) == 13
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500]) == 9
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515]) == 15
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 1
    assert candidate(nums = [56, 98, 168, 224, 231, 252, 336, 392, 441, 462, 504, 539, 616, 672, 784, 882, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1596, 1680, 1764, 1848, 1932, 2016, 2100]) == 31
    assert candidate(nums = [2520, 5040, 10080, 20160, 40320]) == 5
    assert candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420]) == 20
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108]) == 18
    assert candidate(nums = [36, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255]) == 16
    assert candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495]) == 42
    assert candidate(nums = [30030, 30031, 30032, 30033, 30034, 30035, 30036, 30037, 30038, 30039, 30040, 30041, 30042, 30043, 30044, 30045, 30046, 30047, 30048, 30049, 30050, 30051, 30052, 30053, 30054, 30055]) == 22
    assert candidate(nums = [1000, 1024, 1050, 1080, 1100, 1120, 1140, 1150, 1170, 1190, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470]) == 20
    assert candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
    assert candidate(nums = [60, 100, 150, 200, 250, 300]) == 6
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 10
    assert candidate(nums = [97, 194, 291, 388, 485, 582, 679, 776, 873, 970, 1067, 1164, 1261, 1358, 1455, 1552, 1649, 1746, 1843, 1940]) == 20
    assert candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 15
    assert candidate(nums = [105, 115, 130, 140, 154, 165, 170, 182, 187, 195, 210, 220, 221, 231, 238, 247, 253, 260, 273, 286, 299]) == 21
    assert candidate(nums = [210, 420, 630, 840, 1050, 1260, 1470, 1680, 1890, 2100, 2310, 2520, 2730, 2940, 3150]) == 15
    assert candidate(nums = [99, 121, 143, 165, 187, 209, 231, 253, 275, 297, 319, 330, 352, 374, 396, 418, 440, 462, 484, 506]) == 20
    assert candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609]) == 20
    assert candidate(nums = [10001, 20002, 30003, 40004, 50005, 60006, 70007, 80008, 90009, 100010]) == 10
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 10
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 16
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10
    assert candidate(nums = [21, 35, 55, 77, 91, 119, 143, 165, 187, 209, 231, 253, 286, 308, 330]) == 15
    assert candidate(nums = [210, 330, 462, 594, 726, 858, 990, 1122, 1254, 1386, 1518, 1650, 1782, 1914, 2046]) == 15
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
    assert candidate(nums = [60, 65, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 143, 154, 165, 182, 210, 231, 252]) == 20
    assert candidate(nums = [44, 66, 100, 121, 143, 165]) == 6
    assert candidate(nums = [60, 100, 140, 210, 280, 350, 420, 500, 560, 630, 700, 770, 840, 910, 980, 1050, 1120, 1190, 1260, 1330, 1400, 1470, 1540, 1610, 1680, 1750, 1820, 1890, 1960, 2030]) == 30
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1
    assert candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550]) == 40
    assert candidate(nums = [840, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1596, 1680, 1764, 1848, 1932, 2016, 2100, 2184, 2268, 2352, 2436, 2520]) == 21
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 20
    assert candidate(nums = [15, 45, 75, 105, 135, 165, 195, 225, 255, 285, 315, 345, 375, 405, 435, 465, 495, 525, 555, 585]) == 20
    assert candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609, 630, 651, 672, 693, 714, 735, 756, 777, 798, 819, 840, 861, 882, 903, 924, 945, 966, 987, 1008, 1029]) == 40
    assert candidate(nums = [104729, 104731, 104743, 104759, 104761, 104771, 104773, 104777, 104783, 104791, 104797, 104801, 104807, 104813, 104819, 104831, 104833, 104837, 104839, 104843, 104857, 104858, 104861, 104863, 104867, 104869]) == 9
    assert candidate(nums = [6, 10, 14, 15, 21, 22, 26, 28, 33, 35, 39, 44, 45, 55, 65, 77, 88, 99, 105, 110]) == 20
    assert candidate(nums = [81, 121, 169, 225, 289, 361, 441, 529, 625, 729]) == 5
    assert candidate(nums = [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 14
    assert candidate(nums = [100, 102, 105, 108, 110, 112, 114, 115, 117, 119]) == 10
    assert candidate(nums = [3, 5, 15, 25, 45, 75, 105, 125, 135, 175, 225, 245, 315, 375, 525]) == 15
    assert candidate(nums = [44, 88, 132, 176, 220, 264, 308, 352, 396, 440, 484, 528, 572, 616, 660]) == 15
    assert candidate(nums = [210, 231, 252, 273, 294, 315, 336, 357, 378, 399]) == 10
    assert candidate(nums = [100, 102, 104, 105, 106, 108, 110, 112, 114, 115, 117, 119, 121, 122, 123, 124, 126, 128, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142, 143, 145]) == 30
    assert candidate(nums = [100, 105, 110, 115, 120]) == 5
    assert candidate(nums = [154, 308, 462, 616, 770, 924, 1078, 1232, 1386, 1540, 1694, 1848, 2002, 2156, 2310]) == 15
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 10
    assert candidate(nums = [30, 42, 70, 105, 210]) == 5
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84]) == 20
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]) == 1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 10
    assert candidate(nums = [49, 63, 77, 91, 105, 119, 133, 147, 161, 175, 189, 203, 217, 231, 245]) == 15
    assert candidate(nums = [18, 24, 30, 42, 56, 72, 84, 90]) == 8
    assert candidate(nums = [77, 91, 119, 133, 143, 161, 187, 209, 221, 231, 247, 253, 287, 299, 319]) == 15


