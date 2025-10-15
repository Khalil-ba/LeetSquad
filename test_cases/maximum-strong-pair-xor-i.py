def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4, 4, 6, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4, 4, 6, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 484
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 484: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 25, 30]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 25, 30]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310, 341, 372, 403, 434, 465, 496, 527, 558, 589, 620]) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310, 341, 372, 403, 434, 465, 496, 527, 558, 589, 620]) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310]) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310]) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 968: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 67, 89, 111, 133, 155, 177, 199, 221]) == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 67, 89, 111, 133, 155, 177, 199, 221]) == 244: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 49, 50, 98, 51]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 49, 50, 98, 51]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 288, 384, 480, 576, 672, 768, 864, 960, 1056, 1152, 1248, 1344, 1440]) == 2016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 288, 384, 480, 576, 672, 768, 864, 960, 1056, 1152, 1248, 1344, 1440]) == 2016: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101, 1201, 1301, 1401, 1501, 1601, 1701, 1801, 1901]) == 1992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101, 1201, 1301, 1401, 1501, 1601, 1701, 1801, 1901]) == 1992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 20, 30, 40, 50]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 20, 30, 40, 50]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536, 1664, 1792, 1920]) == 1920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536, 1664, 1792, 1920]) == 1920: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 247: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]) == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]) == 244: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512]) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512]) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999]) == 984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999]) == 984: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 253: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums = [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160]) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160]) == 248: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 968: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]) == 968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]) == 968: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 23, 42, 55, 60, 62, 71]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 23, 42, 55, 60, 62, 71]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]) == 498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]) == 498: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 96, 128]) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 96, 128]) == 224: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 1011, 1314, 1617, 1918, 2221, 2520, 2829]) == 4051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 1011, 1314, 1617, 1918, 2221, 2520, 2829]) == 4051: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 14, 15, 20, 22, 25]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 14, 15, 20, 22, 25]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 99, 98, 98, 97, 97, 96, 96, 95, 95]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 99, 98, 98, 97, 97, 96, 96, 95, 95]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 98304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 98304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 3072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 3072: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1]) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1]) == 192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072]) == 3840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072]) == 3840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 510: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 25, 50, 75, 100, 125, 150, 175, 200]) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 25, 50, 75, 100, 125, 150, 175, 200]) == 242: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 61, 91, 121, 151, 181, 211, 241, 271, 301]) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 61, 91, 121, 151, 181, 211, 241, 271, 301]) == 510: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840]) == 1008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840]) == 1008: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [15, 25, 35, 45, 55]) == 58
    assert candidate(nums = [2, 4, 6, 8, 10, 12]) == 14
    assert candidate(nums = [1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16]) == 24
    assert candidate(nums = [2, 2, 4, 4, 6, 6]) == 6
    assert candidate(nums = [3, 5, 7, 9, 11]) == 14
    assert candidate(nums = [99, 98, 97, 96, 95]) == 63
    assert candidate(nums = [2, 4, 6, 8, 10]) == 14
    assert candidate(nums = [1, 3, 5, 7, 9]) == 14
    assert candidate(nums = [100]) == 0
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50]) == 60
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 122
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 14
    assert candidate(nums = [100, 90, 80, 70, 60]) == 122
    assert candidate(nums = [100, 200, 300, 400, 500]) == 484
    assert candidate(nums = [10, 100]) == 0
    assert candidate(nums = [5, 6, 25, 30]) == 7
    assert candidate(nums = [7, 14, 21, 28, 35]) == 63
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == 48
    assert candidate(nums = [15, 30, 45, 60, 75]) == 119
    assert candidate(nums = [50, 40, 30, 20, 10]) == 60
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35]) == 31
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 126
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 768
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420]) == 504
    assert candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310, 341, 372, 403, 434, 465, 496, 527, 558, 589, 620]) == 1023
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231]) == 231
    assert candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310]) == 495
    assert candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91]) == 126
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 968
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == 15
    assert candidate(nums = [23, 45, 67, 89, 111, 133, 155, 177, 199, 221]) == 244
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 63
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 96
    assert candidate(nums = [99, 1, 49, 50, 98, 51]) == 83
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 288, 384, 480, 576, 672, 768, 864, 960, 1056, 1152, 1248, 1344, 1440]) == 2016
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 120
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 61
    assert candidate(nums = [100, 99, 98, 97, 96, 95]) == 63
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 0
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 255
    assert candidate(nums = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101, 1201, 1301, 1401, 1501, 1601, 1701, 1801, 1901]) == 1992
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 0
    assert candidate(nums = [1, 10, 20, 30, 40, 50]) == 60
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144
    assert candidate(nums = [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536, 1664, 1792, 1920]) == 1920
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 61
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 247
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 250
    assert candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]) == 244
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == 63
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 15
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512]) == 768
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 31
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 62
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7
    assert candidate(nums = [1, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 61
    assert candidate(nums = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 126
    assert candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 1023
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 192
    assert candidate(nums = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999]) == 984
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 63
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]) == 255
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 124
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 253
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 122
    assert candidate(nums = [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == 63
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 63
    assert candidate(nums = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99]) == 126
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160]) == 248
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 7
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 968
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
    assert candidate(nums = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]) == 201
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 110
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 124
    assert candidate(nums = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]) == 968
    assert candidate(nums = [8, 15, 23, 42, 55, 60, 62, 71]) == 123
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
    assert candidate(nums = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]) == 498
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 96, 128]) == 224
    assert candidate(nums = [50, 49, 48, 47, 46, 45]) == 31
    assert candidate(nums = [63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [123, 456, 789, 1011, 1314, 1617, 1918, 2221, 2520, 2829]) == 4051
    assert candidate(nums = [8, 10, 14, 15, 20, 22, 25]) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 250
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 768
    assert candidate(nums = [99, 99, 98, 98, 97, 97, 96, 96, 95, 95]) == 63
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999]) == 0
    assert candidate(nums = [2, 18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 125
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 122
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 98304
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 126
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 125
    assert candidate(nums = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 3072
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 127
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 126
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1]) == 192
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 0
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79]) == 124
    assert candidate(nums = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 250
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 120
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 61
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 122
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 63
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072]) == 3840
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 63
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 510
    assert candidate(nums = [5, 25, 50, 75, 100, 125, 150, 175, 200]) == 242
    assert candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 63
    assert candidate(nums = [31, 61, 91, 121, 151, 181, 211, 241, 271, 301]) == 510
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 250
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 63
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 124
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840]) == 1008


