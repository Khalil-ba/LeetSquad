def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 9, 6, 12]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 9, 6, 12]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 12, 6, 14]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 12, 6, 14]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 9, 27, 81, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 9, 27, 81, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 6, 3, 14, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 6, 3, 14, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 16]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 16]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 9, 3, 6, 2, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 9, 3, 6, 2, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 9, 27, 36, 54]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 9, 27, 36, 54]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 27, 9, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 27, 9, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 125, 200]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 125, 200]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [54, 81, 162, 243, 324]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [54, 81, 162, 243, 324]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [72, 84, 12, 6, 3, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [72, 84, 12, 6, 3, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 90, 135, 180, 225, 270, 315, 360]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 90, 135, 180, 225, 270, 315, 360]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504, 540]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504, 540]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44100, 88200, 132300, 176400, 220500]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44100, 88200, 132300, 176400, 220500]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 36, 81, 144, 225, 324, 441, 576, 729, 900]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 36, 81, 144, 225, 324, 441, 576, 729, 900]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 72, 108, 144, 180]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 72, 108, 144, 180]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 242, 484, 968, 1936, 3872]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 242, 484, 968, 1936, 3872]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [315, 270, 585, 1035, 2070, 4140]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [315, 270, 585, 1035, 2070, 4140]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [28, 14, 7, 35, 49]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [28, 14, 7, 35, 49]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 242, 363, 484, 605, 726, 847, 968, 1089, 1210]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 242, 363, 484, 605, 726, 847, 968, 1089, 1210]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [77, 154, 308, 616, 1232, 2464, 4928]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [77, 154, 308, 616, 1232, 2464, 4928]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [360, 180, 90, 45, 15, 5, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [360, 180, 90, 45, 15, 5, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [144, 180, 216, 252, 288, 324, 360]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [144, 180, 216, 252, 288, 324, 360]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [315, 210, 105, 70, 35]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [315, 210, 105, 70, 35]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 45, 60, 90, 120, 150]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 45, 60, 90, 120, 150]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 125, 625, 3125, 15625]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 125, 625, 3125, 15625]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 25, 50, 125, 200]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 25, 50, 125, 200]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [28, 56, 84, 112, 140, 168, 196, 224, 252, 280]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [28, 56, 84, 112, 140, 168, 196, 224, 252, 280]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 48, 36, 24, 12, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 48, 36, 24, 12, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [504, 252, 126, 63, 21, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [504, 252, 126, 63, 21, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 98, 147, 196, 245, 294, 343, 392, 441, 490]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 98, 147, 196, 245, 294, 343, 392, 441, 490]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [105, 210, 315, 420, 525, 630, 735]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [105, 210, 315, 420, 525, 630, 735]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240, 300]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240, 300]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [120, 180, 240, 300, 360, 420]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [120, 180, 240, 300, 360, 420]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [120, 180, 240, 300, 360, 420, 480, 540, 600]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [120, 180, 240, 300, 360, 420, 480, 540, 600]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 7, 14, 28, 35, 70]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 7, 14, 28, 35, 70]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [180, 120, 60, 30, 15, 5, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [180, 120, 60, 30, 15, 5, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 27, 81, 243, 729]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 27, 81, 243, 729]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120, 150, 180]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120, 150, 180]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 7, 14, 21, 28, 35]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 7, 14, 21, 28, 35]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260, 273, 286, 299, 312, 325, 338, 351, 364, 377, 390]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260, 273, 286, 299, 312, 325, 338, 351, 364, 377, 390]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 110, 99, 88, 77, 66, 55]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 110, 99, 88, 77, 66, 55]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [840, 1260, 70, 210, 105]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [840, 1260, 70, 210, 105]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [77, 154, 231, 308, 385]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [77, 154, 231, 308, 385]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 45, 60, 75, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 45, 60, 75, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1369, 2738, 4107, 5476, 6845]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1369, 2738, 4107, 5476, 6845]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 242, 363, 484, 605, 726, 847]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 242, 363, 484, 605, 726, 847]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 12, 18, 24, 30, 36]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 12, 18, 24, 30, 36]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 98, 147, 196, 245, 294]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 98, 147, 196, 245, 294]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [72, 96, 120, 144, 168, 192]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [72, 96, 120, 144, 168, 192]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240, 300, 360, 420]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240, 300, 360, 420]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 42, 35, 28, 21, 14, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 42, 35, 28, 21, 14, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 125, 250, 625, 3125]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 125, 250, 625, 3125]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 40, 20, 10, 5, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 40, 20, 10, 5, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 56, 98, 14, 21, 28, 35]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 56, 98, 14, 21, 28, 35]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 105, 35, 70, 140]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 105, 35, 70, 140]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [22, 44, 66, 88, 110, 132]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [22, 44, 66, 88, 110, 132]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [252, 168, 84, 42, 21, 14, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [252, 168, 84, 42, 21, 14, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104, 130, 156, 182, 208, 234, 260, 286, 312, 338]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104, 130, 156, 182, 208, 234, 260, 286, 312, 338]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [105, 210, 315, 420, 525, 630, 735, 840, 945, 1050]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [105, 210, 315, 420, 525, 630, 735, 840, 945, 1050]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [55, 110, 165, 220, 275, 330, 385, 440, 495, 550]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55, 110, 165, 220, 275, 330, 385, 440, 495, 550]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [40, 80, 120, 160, 200]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [40, 80, 120, 160, 200]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009, 10010]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009, 10010]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 220, 330, 440, 550, 660, 770, 880, 990]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 220, 330, 440, 550, 660, 770, 880, 990]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440, 1584, 1728, 1872, 2016, 2160]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440, 1584, 1728, 1872, 2016, 2160]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 30, 15, 75, 105]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 30, 15, 75, 105]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 14, 7, 35, 49, 28, 56, 98, 196, 42]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 14, 7, 35, 49, 28, 56, 98, 196, 42]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 168, 336, 672, 1344, 2688]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 168, 336, 672, 1344, 2688]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240, 264, 288, 312, 336, 360, 384]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240, 264, 288, 312, 336, 360, 384]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [140, 70, 35, 175, 875, 4375]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [140, 70, 35, 175, 875, 4375]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 45, 90, 135, 180, 225]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 45, 90, 135, 180, 225]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [110, 220, 330, 440, 550, 660, 770, 880, 990]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [110, 220, 330, 440, 550, 660, 770, 880, 990]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [84, 140, 196, 252, 308, 364, 420]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [84, 140, 196, 252, 308, 364, 420]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627, 660]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627, 660]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 45, 90, 105, 75]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 45, 90, 105, 75]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 330, 165, 220, 110, 55]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 330, 165, 220, 110, 55]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44, 88, 132, 176, 220, 264, 308, 352, 396, 440]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44, 88, 132, 176, 220, 264, 308, 352, 396, 440]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 120, 150, 180, 210]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 120, 150, 180, 210]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [147, 294, 441, 588, 735]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [147, 294, 441, 588, 735]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 420, 630, 840, 1050]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 420, 630, 840, 1050]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [135, 270, 405, 540, 675]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [135, 270, 405, 540, 675]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 400, 800, 1600, 3200]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 400, 800, 1600, 3200]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [126, 63, 21, 7, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [126, 63, 21, 7, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [84, 126, 42, 70, 56]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [84, 126, 42, 70, 56]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [72, 108, 144, 180, 216, 252]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [72, 108, 144, 180, 216, 252]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 112, 168, 224, 280, 336]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 112, 168, 224, 280, 336]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 224, 336, 448, 560]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 224, 336, 448, 560]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 27, 81, 243, 729, 2187, 6561, 19683]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 27, 81, 243, 729, 2187, 6561, 19683]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 32, 64, 128, 256]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 32, 64, 128, 256]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [243, 81, 27, 9, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [243, 81, 27, 9, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 162, 324, 648, 1296, 2592, 5184, 10368, 20736, 41472]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 162, 324, 648, 1296, 2592, 5184, 10368, 20736, 41472]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 600, 900, 1200, 1500, 1800, 2100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 600, 900, 1200, 1500, 1800, 2100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [315, 630, 945, 1260, 1575, 1890, 2205, 2520, 2835, 3150, 3465, 3780, 4095, 4410, 4725, 5040, 5355, 5670, 5985, 6300]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [315, 630, 945, 1260, 1575, 1890, 2205, 2520, 2835, 3150, 3465, 3780, 4095, 4410, 4725, 5040, 5355, 5670, 5985, 6300]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 45, 60, 75, 90, 105, 120]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 45, 60, 75, 90, 105, 120]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [27, 81, 243, 729, 2187, 6561, 19683]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [27, 81, 243, 729, 2187, 6561, 19683]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [48, 24, 12, 6, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [48, 24, 12, 6, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100, 200, 300, 400]) == 1
    assert candidate(nums = [30, 60, 90, 120]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11]) == 5
    assert candidate(nums = [18, 9, 6, 12]) == 1
    assert candidate(nums = [4, 12, 6, 14]) == 1
    assert candidate(nums = [18, 9, 27, 81, 3]) == 1
    assert candidate(nums = [30, 20, 10, 5]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7]) == 1
    assert candidate(nums = [60, 120, 180, 240]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7]) == 1
    assert candidate(nums = [12, 6, 3, 14, 8]) == 2
    assert candidate(nums = [8, 4, 2, 16]) == 1
    assert candidate(nums = [100, 50, 25, 10]) == 1
    assert candidate(nums = [5, 10, 15, 20, 25]) == 1
    assert candidate(nums = [18, 9, 3, 6, 2, 12]) == 2
    assert candidate(nums = [18, 9, 27, 36, 54]) == 1
    assert candidate(nums = [3, 9, 27, 81]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 1
    assert candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209]) == 1
    assert candidate(nums = [81, 27, 9, 3, 1]) == 2
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 1
    assert candidate(nums = [100, 50, 25, 125, 200]) == 1
    assert candidate(nums = [54, 81, 162, 243, 324]) == 1
    assert candidate(nums = [72, 84, 12, 6, 3, 9]) == 1
    assert candidate(nums = [45, 90, 135, 180, 225, 270, 315, 360]) == 1
    assert candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504, 540]) == 1
    assert candidate(nums = [44100, 88200, 132300, 176400, 220500]) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == 1
    assert candidate(nums = [9, 36, 81, 144, 225, 324, 441, 576, 729, 900]) == 1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == 1
    assert candidate(nums = [1024, 512, 256, 128, 64]) == 1
    assert candidate(nums = [36, 72, 108, 144, 180]) == 1
    assert candidate(nums = [121, 242, 484, 968, 1936, 3872]) == 1
    assert candidate(nums = [315, 270, 585, 1035, 2070, 4140]) == 1
    assert candidate(nums = [28, 14, 7, 35, 49]) == 1
    assert candidate(nums = [121, 242, 363, 484, 605, 726, 847, 968, 1089, 1210]) == 1
    assert candidate(nums = [77, 154, 308, 616, 1232, 2464, 4928]) == 1
    assert candidate(nums = [360, 180, 90, 45, 15, 5, 1]) == 2
    assert candidate(nums = [144, 180, 216, 252, 288, 324, 360]) == 1
    assert candidate(nums = [315, 210, 105, 70, 35]) == 1
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]) == 1
    assert candidate(nums = [30, 45, 60, 90, 120, 150]) == 1
    assert candidate(nums = [100, 50, 25, 125, 625, 3125, 15625]) == 1
    assert candidate(nums = [100, 25, 50, 125, 200]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
    assert candidate(nums = [28, 56, 84, 112, 140, 168, 196, 224, 252, 280]) == 1
    assert candidate(nums = [60, 48, 36, 24, 12, 6]) == 1
    assert candidate(nums = [504, 252, 126, 63, 21, 7]) == 1
    assert candidate(nums = [33, 66, 99, 132, 165]) == 1
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 1
    assert candidate(nums = [49, 98, 147, 196, 245, 294, 343, 392, 441, 490]) == 1
    assert candidate(nums = [105, 210, 315, 420, 525, 630, 735]) == 1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136]) == 1
    assert candidate(nums = [15, 30, 45, 60, 75, 90]) == 1
    assert candidate(nums = [60, 120, 180, 240, 300]) == 1
    assert candidate(nums = [120, 180, 240, 300, 360, 420]) == 1
    assert candidate(nums = [120, 180, 240, 300, 360, 420, 480, 540, 600]) == 1
    assert candidate(nums = [42, 7, 14, 28, 35, 70]) == 1
    assert candidate(nums = [180, 120, 60, 30, 15, 5, 1]) == 2
    assert candidate(nums = [9, 27, 81, 243, 729]) == 1
    assert candidate(nums = [30, 60, 90, 120, 150, 180]) == 1
    assert candidate(nums = [49, 7, 14, 21, 28, 35]) == 1
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500]) == 1
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 1
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260, 273, 286, 299, 312, 325, 338, 351, 364, 377, 390]) == 1
    assert candidate(nums = [121, 110, 99, 88, 77, 66, 55]) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104]) == 1
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 1
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == 1
    assert candidate(nums = [840, 1260, 70, 210, 105]) == 1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707]) == 1
    assert candidate(nums = [77, 154, 231, 308, 385]) == 1
    assert candidate(nums = [30, 45, 60, 75, 90]) == 1
    assert candidate(nums = [1369, 2738, 4107, 5476, 6845]) == 1
    assert candidate(nums = [10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80]) == 1
    assert candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420]) == 1
    assert candidate(nums = [121, 242, 363, 484, 605, 726, 847]) == 1
    assert candidate(nums = [60, 12, 18, 24, 30, 36]) == 1
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 1
    assert candidate(nums = [49, 98, 147, 196, 245, 294]) == 1
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 1
    assert candidate(nums = [72, 96, 120, 144, 168, 192]) == 1
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]) == 1
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420]) == 1
    assert candidate(nums = [49, 42, 35, 28, 21, 14, 7]) == 1
    assert candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]) == 1
    assert candidate(nums = [100, 50, 25, 125, 250, 625, 3125]) == 1
    assert candidate(nums = [60, 40, 20, 10, 5, 1]) == 2
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005]) == 1
    assert candidate(nums = [42, 56, 98, 14, 21, 28, 35]) == 1
    assert candidate(nums = [210, 105, 35, 70, 140]) == 1
    assert candidate(nums = [22, 44, 66, 88, 110, 132]) == 1
    assert candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120]) == 1
    assert candidate(nums = [100, 150, 200, 250, 300]) == 1
    assert candidate(nums = [252, 168, 84, 42, 21, 14, 7]) == 1
    assert candidate(nums = [104, 130, 156, 182, 208, 234, 260, 286, 312, 338]) == 1
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 1
    assert candidate(nums = [105, 210, 315, 420, 525, 630, 735, 840, 945, 1050]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600]) == 1
    assert candidate(nums = [55, 110, 165, 220, 275, 330, 385, 440, 495, 550]) == 1
    assert candidate(nums = [40, 80, 120, 160, 200]) == 1
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009, 10010]) == 1
    assert candidate(nums = [121, 220, 330, 440, 550, 660, 770, 880, 990]) == 1
    assert candidate(nums = [144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440, 1584, 1728, 1872, 2016, 2160]) == 1
    assert candidate(nums = [60, 30, 15, 75, 105]) == 1
    assert candidate(nums = [21, 14, 7, 35, 49, 28, 56, 98, 196, 42]) == 1
    assert candidate(nums = [3, 9, 27, 81, 243, 729]) == 1
    assert candidate(nums = [42, 84, 126, 168, 210, 252]) == 1
    assert candidate(nums = [42, 84, 168, 336, 672, 1344, 2688]) == 1
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 1
    assert candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240, 264, 288, 312, 336, 360, 384]) == 1
    assert candidate(nums = [140, 70, 35, 175, 875, 4375]) == 1
    assert candidate(nums = [60, 45, 90, 135, 180, 225]) == 1
    assert candidate(nums = [110, 220, 330, 440, 550, 660, 770, 880, 990]) == 1
    assert candidate(nums = [84, 140, 196, 252, 308, 364, 420]) == 1
    assert candidate(nums = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 21
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627, 660]) == 1
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200]) == 1
    assert candidate(nums = [60, 45, 90, 105, 75]) == 1
    assert candidate(nums = [210, 330, 165, 220, 110, 55]) == 1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 1
    assert candidate(nums = [44, 88, 132, 176, 220, 264, 308, 352, 396, 440]) == 1
    assert candidate(nums = [90, 120, 150, 180, 210]) == 1
    assert candidate(nums = [147, 294, 441, 588, 735]) == 1
    assert candidate(nums = [210, 420, 630, 840, 1050]) == 1
    assert candidate(nums = [135, 270, 405, 540, 675]) == 1
    assert candidate(nums = [100, 200, 400, 800, 1600, 3200]) == 1
    assert candidate(nums = [126, 63, 21, 7, 1]) == 2
    assert candidate(nums = [84, 126, 42, 70, 56]) == 1
    assert candidate(nums = [72, 108, 144, 180, 216, 252]) == 1
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 1
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504]) == 1
    assert candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]) == 1
    assert candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240]) == 1
    assert candidate(nums = [56, 112, 168, 224, 280, 336]) == 1
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]) == 1
    assert candidate(nums = [112, 224, 336, 448, 560]) == 1
    assert candidate(nums = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140]) == 1
    assert candidate(nums = [9, 27, 81, 243, 729, 2187, 6561, 19683]) == 1
    assert candidate(nums = [16, 32, 64, 128, 256]) == 1
    assert candidate(nums = [243, 81, 27, 9, 3]) == 1
    assert candidate(nums = [81, 162, 324, 648, 1296, 2592, 5184, 10368, 20736, 41472]) == 1
    assert candidate(nums = [300, 600, 900, 1200, 1500, 1800, 2100]) == 1
    assert candidate(nums = [315, 630, 945, 1260, 1575, 1890, 2205, 2520, 2835, 3150, 3465, 3780, 4095, 4410, 4725, 5040, 5355, 5670, 5985, 6300]) == 1
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120]) == 1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 1
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137]) == 8
    assert candidate(nums = [27, 81, 243, 729, 2187, 6561, 19683]) == 1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 1
    assert candidate(nums = [81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489]) == 1
    assert candidate(nums = [48, 24, 12, 6, 3]) == 1
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840]) == 1


