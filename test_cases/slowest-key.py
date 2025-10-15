def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(releaseTimes = [2, 3, 7, 10, 15],keysPressed = "zzzaa") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [2, 3, 7, 10, 15],keysPressed = "zzzaa") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [5, 10, 15, 20, 25],keysPressed = "zabzc") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [5, 10, 15, 20, 25],keysPressed = "zabzc") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [5, 15, 25, 35, 45, 55],keysPressed = "abcdef") == "f"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [5, 15, 25, 35, 45, 55],keysPressed = "abcdef") == "f": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [50, 70, 80, 90],keysPressed = "abcd") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [50, 70, 80, 90],keysPressed = "abcd") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [9, 29, 49, 50],keysPressed = "cbcd") == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [9, 29, 49, 50],keysPressed = "cbcd") == "c": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 15, 20, 25, 30],keysPressed = "aabcd") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 15, 20, 25, 30],keysPressed = "aabcd") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [12, 23, 36, 46, 62],keysPressed = "spuda") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [12, 23, 36, 46, 62],keysPressed = "spuda") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 2, 3, 4, 5],keysPressed = "abcde") == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 2, 3, 4, 5],keysPressed = "abcde") == "e": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [50, 75, 100, 125, 150],keysPressed = "zzzzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [50, 75, 100, 125, 150],keysPressed = "zzzzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keysPressed = "qwertyuiopz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keysPressed = "qwertyuiopz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [100, 200, 300, 400, 500],keysPressed = "aaaaa") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [100, 200, 300, 400, 500],keysPressed = "aaaaa") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [2, 5, 10, 15, 20, 25, 30],keysPressed = "zzzzzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [2, 5, 10, 15, 20, 25, 30],keysPressed = "zzzzzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 3, 5, 7, 9],keysPressed = "abcde") == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 3, 5, 7, 9],keysPressed = "abcde") == "e": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keysPressed = "abcdefghij") == "j"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keysPressed = "abcdefghij") == "j": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [100, 200, 300, 400],keysPressed = "abcd") == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [100, 200, 300, 400],keysPressed = "abcd") == "d": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 20, 30, 40, 50],keysPressed = "aaaaa") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 20, 30, 40, 50],keysPressed = "aaaaa") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],keysPressed = "abcdefghijk") == "k"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],keysPressed = "abcdefghijk") == "k": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [5, 10, 15, 20, 25, 30],keysPressed = "ppppp") == "p"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [5, 10, 15, 20, 25, 30],keysPressed = "ppppp") == "p": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 20, 30, 40],keysPressed = "abcd") == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 20, 30, 40],keysPressed = "abcd") == "d": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],keysPressed = "abcdefghijklmnopqrstuvwxyz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],keysPressed = "abcdefghijklmnopqrstuvwxyz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 30, 70, 150, 230, 320, 420, 530, 650, 780, 920, 1080, 1260, 1460, 1680, 1920],keysPressed = "zzzzzzzzzzzzzzzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 30, 70, 150, 230, 320, 420, 530, 650, 780, 920, 1080, 1260, 1460, 1680, 1920],keysPressed = "zzzzzzzzzzzzzzzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950],keysPressed = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950],keysPressed = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 250, 265, 280, 295, 310, 325, 340, 355, 370, 385, 400, 415, 430, 445],keysPressed = "zyxwvutsrqponmlkjihgfedcba") == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 250, 265, 280, 295, 310, 325, 340, 355, 370, 385, 400, 415, 430, 445],keysPressed = "zyxwvutsrqponmlkjihgfedcba") == "y": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],keysPressed = "abcdefghijklmno") == "o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],keysPressed = "abcdefghijklmno") == "o": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],keysPressed = "zzzzzzzzzzzzzzzzzzzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],keysPressed = "zzzzzzzzzzzzzzzzzzzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],keysPressed = "nopqrstuvwxyz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],keysPressed = "nopqrstuvwxyz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],keysPressed = "abcdefghijklmno") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],keysPressed = "abcdefghijklmno") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],keysPressed = "abcdefghijklmn") == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],keysPressed = "abcdefghijklmn") == "b": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [20, 45, 60, 80, 100, 120, 140, 160, 180, 200],keysPressed = "abcdefghij") == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [20, 45, 60, 80, 100, 120, 140, 160, 180, 200],keysPressed = "abcdefghij") == "b": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],keysPressed = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],keysPressed = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200],keysPressed = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200],keysPressed = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [5, 15, 30, 45, 60, 75, 90, 105, 120, 135],keysPressed = "abcdefghij") == "j"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [5, 15, 30, 45, 60, 75, 90, 105, 120, 135],keysPressed = "abcdefghij") == "j": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],keysPressed = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],keysPressed = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "a": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],keysPressed = "zzzzzzzzzzzzzzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],keysPressed = "zzzzzzzzzzzzzzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],keysPressed = "abcdefghijklmnopqrst") == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],keysPressed = "abcdefghijklmnopqrst") == "t": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],keysPressed = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],keysPressed = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [5, 9, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253],keysPressed = "mississippiissiippi") == "i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [5, 9, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253],keysPressed = "mississippiissiippi") == "i": {e}')
    
    total += 1
    try:
        result = candidate(releaseTimes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],keysPressed = "abcdefghijklmnopqrst") == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(releaseTimes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],keysPressed = "abcdefghijklmnopqrst") == "t": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(releaseTimes = [2, 3, 7, 10, 15],keysPressed = "zzzaa") == "a"
    assert candidate(releaseTimes = [5, 10, 15, 20, 25],keysPressed = "zabzc") == "z"
    assert candidate(releaseTimes = [5, 15, 25, 35, 45, 55],keysPressed = "abcdef") == "f"
    assert candidate(releaseTimes = [50, 70, 80, 90],keysPressed = "abcd") == "a"
    assert candidate(releaseTimes = [9, 29, 49, 50],keysPressed = "cbcd") == "c"
    assert candidate(releaseTimes = [10, 15, 20, 25, 30],keysPressed = "aabcd") == "a"
    assert candidate(releaseTimes = [12, 23, 36, 46, 62],keysPressed = "spuda") == "a"
    assert candidate(releaseTimes = [1, 2, 3, 4, 5],keysPressed = "abcde") == "e"
    assert candidate(releaseTimes = [50, 75, 100, 125, 150],keysPressed = "zzzzz") == "z"
    assert candidate(releaseTimes = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keysPressed = "qwertyuiopz") == "z"
    assert candidate(releaseTimes = [100, 200, 300, 400, 500],keysPressed = "aaaaa") == "a"
    assert candidate(releaseTimes = [2, 5, 10, 15, 20, 25, 30],keysPressed = "zzzzzz") == "z"
    assert candidate(releaseTimes = [1, 3, 5, 7, 9],keysPressed = "abcde") == "e"
    assert candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keysPressed = "abcdefghij") == "j"
    assert candidate(releaseTimes = [100, 200, 300, 400],keysPressed = "abcd") == "d"
    assert candidate(releaseTimes = [10, 20, 30, 40, 50],keysPressed = "aaaaa") == "a"
    assert candidate(releaseTimes = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],keysPressed = "abcdefghijk") == "k"
    assert candidate(releaseTimes = [5, 10, 15, 20, 25, 30],keysPressed = "ppppp") == "p"
    assert candidate(releaseTimes = [10, 20, 30, 40],keysPressed = "abcd") == "d"
    assert candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],keysPressed = "abcdefghijklmnopqrstuvwxyz") == "z"
    assert candidate(releaseTimes = [10, 30, 70, 150, 230, 320, 420, 530, 650, 780, 920, 1080, 1260, 1460, 1680, 1920],keysPressed = "zzzzzzzzzzzzzzzz") == "z"
    assert candidate(releaseTimes = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950],keysPressed = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == "a"
    assert candidate(releaseTimes = [10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 250, 265, 280, 295, 310, 325, 340, 355, 370, 385, 400, 415, 430, 445],keysPressed = "zyxwvutsrqponmlkjihgfedcba") == "y"
    assert candidate(releaseTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],keysPressed = "abcdefghijklmno") == "o"
    assert candidate(releaseTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],keysPressed = "zzzzzzzzzzzzzzzzzzzz") == "z"
    assert candidate(releaseTimes = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],keysPressed = "nopqrstuvwxyz") == "z"
    assert candidate(releaseTimes = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],keysPressed = "abcdefghijklmno") == "a"
    assert candidate(releaseTimes = [10, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],keysPressed = "abcdefghijklmn") == "b"
    assert candidate(releaseTimes = [20, 45, 60, 80, 100, 120, 140, 160, 180, 200],keysPressed = "abcdefghij") == "b"
    assert candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],keysPressed = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "z"
    assert candidate(releaseTimes = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200],keysPressed = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "z"
    assert candidate(releaseTimes = [5, 15, 30, 45, 60, 75, 90, 105, 120, 135],keysPressed = "abcdefghij") == "j"
    assert candidate(releaseTimes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],keysPressed = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "a"
    assert candidate(releaseTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],keysPressed = "zzzzzzzzzzzzzzz") == "z"
    assert candidate(releaseTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],keysPressed = "abcdefghijklmnopqrst") == "t"
    assert candidate(releaseTimes = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],keysPressed = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == "z"
    assert candidate(releaseTimes = [5, 9, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253],keysPressed = "mississippiissiippi") == "i"
    assert candidate(releaseTimes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],keysPressed = "abcdefghijklmnopqrst") == "t"


