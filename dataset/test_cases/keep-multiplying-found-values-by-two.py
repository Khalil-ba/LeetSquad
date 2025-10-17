def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],original = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],original = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 625],original = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 625],original = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],original = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],original = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8],original = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8],original = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128],original = 8) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128],original = 8) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 9],original = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 9],original = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000],original = 1000) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000],original = 1000) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],original = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],original = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],original = 10) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],original = 10) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2],original = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2],original = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512],original = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512],original = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31],original = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31],original = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16],original = 1) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16],original = 1) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 16, 32, 64],original = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 16, 32, 64],original = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 1, 12],original = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 1, 12],original = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125],original = 125) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125],original = 125) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 40, 80, 160],original = 10) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 40, 80, 160],original = 10) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112],original = 7) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112],original = 7) == 224: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448],original = 7) == 896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448],original = 7) == 896: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21],original = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21],original = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],original = 10) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],original = 10) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656],original = 13) == 13312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656],original = 13) == 13312: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304],original = 9) == 4608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304],original = 9) == 4608: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 6, 7, 10, 11, 13, 14, 17, 19, 21, 22, 23, 26, 29, 31],original = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 6, 7, 10, 11, 13, 14, 17, 19, 21, 22, 23, 26, 29, 31],original = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],original = 9) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],original = 9) == 288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816, 5632],original = 11) == 11264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816, 5632],original = 11) == 11264: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 4) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 4) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],original = 2) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],original = 2) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],original = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],original = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],original = 4) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],original = 4) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 1) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 1) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],original = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],original = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],original = 4) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],original = 4) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300],original = 15) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300],original = 15) == 480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],original = 10) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],original = 10) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],original = 1) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],original = 1) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144],original = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144],original = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152],original = 6) == 98304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152],original = 6) == 98304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],original = 1) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],original = 1) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328],original = 13) == 6656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328],original = 13) == 6656: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],original = 500) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],original = 500) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],original = 10) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],original = 10) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729],original = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729],original = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 58, 116, 232, 464, 928, 1856],original = 29) == 3712
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 58, 116, 232, 464, 928, 1856],original = 29) == 3712: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],original = 13) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],original = 13) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],original = 7) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],original = 7) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280],original = 5) == 2560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280],original = 5) == 2560: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561],original = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561],original = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816, 5632, 11264, 22528, 45056, 90112],original = 11) == 180224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816, 5632, 11264, 22528, 45056, 90112],original = 11) == 180224: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560],original = 10) == 5120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560],original = 10) == 5120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],original = 11) == 352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],original = 11) == 352: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],original = 10) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],original = 10) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],original = 500) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],original = 500) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],original = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],original = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],original = 7) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],original = 7) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312],original = 13) == 26624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312],original = 13) == 26624: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000],original = 250) == 256000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000],original = 250) == 256000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 60, 120, 240, 480, 960, 1920, 3840],original = 15) == 7680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 60, 120, 240, 480, 960, 1920, 3840],original = 15) == 7680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 76, 152, 304, 608, 1216, 2432, 4864, 9728],original = 19) == 19456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 76, 152, 304, 608, 1216, 2432, 4864, 9728],original = 19) == 19456: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],original = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],original = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],original = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],original = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66],original = 6) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66],original = 6) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792],original = 7) == 3584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792],original = 7) == 3584: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180],original = 6) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180],original = 6) == 192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832],original = 13) == 1664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832],original = 13) == 1664: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366],original = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366],original = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816],original = 11) == 5632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816],original = 11) == 5632: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],original = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],original = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584],original = 7) == 7168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584],original = 7) == 7168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],original = 15) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],original = 15) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],original = 7) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],original = 7) == 224: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],original = 990) == 1980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],original = 990) == 1980: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683],original = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683],original = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],original = 13) == 416
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],original = 13) == 416: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792],original = 7) == 3584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792],original = 7) == 3584: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],original = 5) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],original = 5) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],original = 9) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],original = 9) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 2) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 2) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 68, 136, 272, 544, 1088, 2176, 4352],original = 17) == 8704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 68, 136, 272, 544, 1088, 2176, 4352],original = 17) == 8704: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],original = 10) == 10240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],original = 10) == 10240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],original = 500) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],original = 500) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312, 26624, 53248, 106496],original = 13) == 212992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312, 26624, 53248, 106496],original = 13) == 212992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],original = 7) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],original = 7) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340],original = 17) == 544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340],original = 17) == 544: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 76, 152, 304, 608, 1216],original = 19) == 2432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 76, 152, 304, 608, 1216],original = 19) == 2432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100],original = 4) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100],original = 4) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400],original = 100) == 204800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400],original = 100) == 204800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 92, 184, 368, 736, 1472],original = 23) == 2944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 92, 184, 368, 736, 1472],original = 23) == 2944: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],original = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],original = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],original = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],original = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 1) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 1) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],original = 980) == 1960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],original = 980) == 1960: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],original = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],original = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 24, 48, 96, 192, 384, 768, 1536],original = 6) == 3072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 24, 48, 96, 192, 384, 768, 1536],original = 6) == 3072: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 10, 12, 15, 20, 30, 60, 120, 240, 480, 960],original = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 10, 12, 15, 20, 30, 60, 120, 240, 480, 960],original = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896],original = 7) == 1792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896],original = 7) == 1792: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304],original = 9) == 4608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304],original = 9) == 4608: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 45, 135, 405, 1215, 3645, 10935, 32805],original = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 45, 135, 405, 1215, 3645, 10935, 32805],original = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],original = 8) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],original = 8) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240],original = 10) == 20480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240],original = 10) == 20480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 44, 88, 176, 352, 704],original = 11) == 1408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 44, 88, 176, 352, 704],original = 11) == 1408: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512],original = 2) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512],original = 2) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],original = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],original = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683],original = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683],original = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 28, 56, 112, 224, 448, 896, 1792, 3584],original = 14) == 7168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 28, 56, 112, 224, 448, 896, 1792, 3584],original = 14) == 7168: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],original = 5) == 5
    assert candidate(nums = [1000, 500, 250, 125, 625],original = 5) == 5
    assert candidate(nums = [3, 6, 9, 12, 15],original = 3) == 24
    assert candidate(nums = [1, 2, 4, 8],original = 1) == 16
    assert candidate(nums = [8, 16, 32, 64, 128],original = 8) == 256
    assert candidate(nums = [2, 7, 9],original = 4) == 4
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000],original = 1000) == 2000
    assert candidate(nums = [1, 3, 5, 7, 9],original = 2) == 2
    assert candidate(nums = [10, 20, 30, 40, 50],original = 10) == 80
    assert candidate(nums = [2, 2, 2, 2, 2],original = 2) == 4
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512],original = 4) == 4
    assert candidate(nums = [1000, 500, 250, 125, 62, 31],original = 1) == 1
    assert candidate(nums = [1, 1, 1, 1, 1],original = 1) == 2
    assert candidate(nums = [1, 2, 4, 8, 16],original = 1) == 32
    assert candidate(nums = [4, 8, 16, 32, 64],original = 2) == 2
    assert candidate(nums = [5, 3, 6, 1, 12],original = 3) == 24
    assert candidate(nums = [1000, 500, 250, 125],original = 125) == 2000
    assert candidate(nums = [10, 20, 40, 80, 160],original = 10) == 320
    assert candidate(nums = [7, 14, 28, 56, 112],original = 7) == 224
    assert candidate(nums = [1, 3, 5, 7, 9],original = 1) == 2
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448],original = 7) == 896
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21],original = 3) == 24
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],original = 10) == 160
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656],original = 13) == 13312
    assert candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304],original = 9) == 4608
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],original = 1) == 2
    assert candidate(nums = [2, 3, 5, 6, 7, 10, 11, 13, 14, 17, 19, 21, 22, 23, 26, 29, 31],original = 2) == 4
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],original = 9) == 288
    assert candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816, 5632],original = 11) == 11264
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 4) == 2048
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],original = 2) == 32
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],original = 2) == 2
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],original = 4) == 128
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],original = 1) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],original = 1) == 2
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 1) == 2048
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],original = 1) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],original = 2) == 4
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],original = 4) == 65536
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300],original = 15) == 480
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],original = 10) == 160
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],original = 1) == 1024
    assert candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144],original = 4) == 8
    assert candidate(nums = [6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152],original = 6) == 98304
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],original = 1) == 32
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328],original = 13) == 6656
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],original = 500) == 8000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],original = 10) == 320
    assert candidate(nums = [3, 9, 27, 81, 243, 729],original = 3) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],original = 1) == 2
    assert candidate(nums = [29, 58, 116, 232, 464, 928, 1856],original = 29) == 3712
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],original = 13) == 208
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],original = 7) == 112
    assert candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280],original = 5) == 2560
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561],original = 3) == 6
    assert candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816, 5632, 11264, 22528, 45056, 90112],original = 11) == 180224
    assert candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560],original = 10) == 5120
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],original = 11) == 352
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],original = 10) == 320
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],original = 500) == 8000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],original = 5) == 80
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],original = 7) == 112
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312],original = 13) == 26624
    assert candidate(nums = [250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000],original = 250) == 256000
    assert candidate(nums = [15, 30, 60, 120, 240, 480, 960, 1920, 3840],original = 15) == 7680
    assert candidate(nums = [19, 38, 76, 152, 304, 608, 1216, 2432, 4864, 9728],original = 19) == 19456
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],original = 1) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],original = 1) == 16
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66],original = 6) == 96
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792],original = 7) == 3584
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],original = 1) == 2
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180],original = 6) == 192
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832],original = 13) == 1664
    assert candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366],original = 2) == 4
    assert candidate(nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561],original = 1) == 2
    assert candidate(nums = [11, 22, 44, 88, 176, 352, 704, 1408, 2816],original = 11) == 5632
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],original = 1) == 2
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],original = 5) == 80
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584],original = 7) == 7168
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],original = 15) == 240
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],original = 7) == 224
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],original = 990) == 1980
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683],original = 3) == 6
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],original = 13) == 416
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792],original = 7) == 3584
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],original = 5) == 160
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],original = 9) == 144
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 2) == 2048
    assert candidate(nums = [17, 34, 68, 136, 272, 544, 1088, 2176, 4352],original = 17) == 8704
    assert candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],original = 10) == 10240
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],original = 500) == 1000
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312, 26624, 53248, 106496],original = 13) == 212992
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],original = 7) == 112
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340],original = 17) == 544
    assert candidate(nums = [19, 38, 76, 152, 304, 608, 1216],original = 19) == 2432
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100],original = 4) == 128
    assert candidate(nums = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400],original = 100) == 204800
    assert candidate(nums = [23, 46, 92, 184, 368, 736, 1472],original = 23) == 2944
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],original = 2) == 4
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],original = 1) == 2
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],original = 1) == 2048
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],original = 980) == 1960
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],original = 3) == 6
    assert candidate(nums = [6, 12, 24, 48, 96, 192, 384, 768, 1536],original = 6) == 3072
    assert candidate(nums = [1, 2, 3, 5, 6, 10, 12, 15, 20, 30, 60, 120, 240, 480, 960],original = 1) == 4
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896],original = 7) == 1792
    assert candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304],original = 9) == 4608
    assert candidate(nums = [5, 15, 45, 135, 405, 1215, 3645, 10935, 32805],original = 5) == 10
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],original = 8) == 128
    assert candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240],original = 10) == 20480
    assert candidate(nums = [11, 22, 44, 88, 176, 352, 704],original = 11) == 1408
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512],original = 2) == 1024
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],original = 3) == 6
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683],original = 3) == 6
    assert candidate(nums = [14, 28, 56, 112, 224, 448, 896, 1792, 3584],original = 14) == 7168


