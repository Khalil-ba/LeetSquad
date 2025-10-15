def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(encoded = [15, 8, 12, 4, 1]) == [11, 4, 12, 0, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 8, 12, 4, 1]) == [11, 4, 12, 0, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1, 7, 6, 5, 4, 3]) == [1, 0, 7, 1, 4, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1, 7, 6, 5, 4, 3]) == [1, 0, 7, 1, 4, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [6, 5, 4, 6]) == [2, 4, 1, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [6, 5, 4, 6]) == [2, 4, 1, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [8, 12, 4, 6, 1, 3, 5]) == [1, 9, 5, 1, 7, 6, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [8, 12, 4, 6, 1, 3, 5]) == [1, 9, 5, 1, 7, 6, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 3, 1, 4, 7]) == [0, 2, 1, 0, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 3, 1, 4, 7]) == [0, 2, 1, 0, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [8, 13, 10, 3, 7, 12, 9]) == [10, 2, 15, 5, 6, 1, 13, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [8, 13, 10, 3, 7, 12, 9]) == [10, 2, 15, 5, 6, 1, 13, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 3, 1, 6, 7, 0]) == [5, 7, 4, 5, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 3, 1, 6, 7, 0]) == [5, 7, 4, 5, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1, 5, 7]) == [1, 0, 5, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1, 5, 7]) == [1, 0, 5, 2]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [8, 9, 10, 11, 12, 13, 14]) == [7, 15, 6, 12, 7, 11, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [8, 9, 10, 11, 12, 13, 14]) == [7, 15, 6, 12, 7, 11, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 8, 9, 10, 11, 12]) == [14, 9, 1, 8, 2, 9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 8, 9, 10, 11, 12]) == [14, 9, 1, 8, 2, 9, 5]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 10, 5, 2, 1, 4]) == [12, 3, 9, 12, 14, 15, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 10, 5, 2, 1, 4]) == [12, 3, 9, 12, 14, 15, 11]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 3, 2]) == [7, 5, 6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 3, 2]) == [7, 5, 6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1, 0, 1, 0, 1]) == [7, 6, 6, 7, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1, 0, 1, 0, 1]) == [7, 6, 6, 7, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 3, 5]) == [7, 0, 3, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 3, 5]) == [7, 0, 3, 6]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1, 6, 5, 4, 3, 2]) == [0, 1, 7, 2, 6, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1, 6, 5, 4, 3, 2]) == [0, 1, 7, 2, 6, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 3, 1, 4, 5]) == [0, 2, 1, 0, 4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 3, 1, 4, 5]) == [0, 2, 1, 0, 4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [3, 1]) == [1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [3, 1]) == [1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [123, 234, 345, 456, 567, 678, 789, 890, 901, 1002]) == [788, 879, 901, 732, 788, 291, 901, 144, 1002, 111, 901]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [123, 234, 345, 456, 567, 678, 789, 890, 901, 1002]) == [788, 879, 901, 732, 788, 291, 901, 144, 1002, 111, 901]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == [9, 7, 21, 3, 25, 7, 37, 3, 41, 7, 53, 3, 57]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == [9, 7, 21, 3, 25, 7, 37, 3, 41, 7, 53, 3, 57]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 10, 5, 3, 2, 1, 4]) == [0, 15, 5, 0, 3, 1, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 10, 5, 3, 2, 1, 4]) == [0, 15, 5, 0, 3, 1, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 10, 15, 20, 25, 30, 35]) == [8, 13, 7, 8, 28, 5, 27, 56]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 10, 15, 20, 25, 30, 35]) == [8, 13, 7, 8, 28, 5, 27, 56]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 15, 18, 17, 20, 23, 22, 25, 28]) == [27, 25, 22, 4, 21, 1, 22, 0, 25, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 15, 18, 17, 20, 23, 22, 25, 28]) == [27, 25, 22, 4, 21, 1, 22, 0, 25, 5]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [3, 2, 0, 3, 7, 2, 4, 3, 11, 2, 8, 3, 15, 2, 12, 3, 19, 2, 16, 3, 23, 2, 20, 3, 27, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [3, 2, 0, 3, 7, 2, 4, 3, 11, 2, 8, 3, 15, 2, 12, 3, 19, 2, 16, 3, 23, 2, 20, 3, 27, 2]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198]) == [95, 18, 74, 41, 71, 62, 186, 53, 175, 10, 186, 1, 199]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198]) == [95, 18, 74, 41, 71, 62, 186, 53, 175, 10, 186, 1, 199]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [9, 20, 27, 34, 41, 48, 55]) == [14, 7, 19, 8, 42, 3, 51, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [9, 20, 27, 34, 41, 48, 55]) == [14, 7, 19, 8, 42, 3, 51, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 2, 5, 8, 3, 6, 1, 4, 9]) == [3, 4, 6, 3, 11, 8, 14, 15, 11, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 2, 5, 8, 3, 6, 1, 4, 9]) == [3, 4, 6, 3, 11, 8, 14, 15, 11, 2]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [65, 131, 263, 527, 1055, 2111, 4223, 8447, 16895, 33791, 67583, 135167]) == [173645, 173580, 173711, 173960, 173447, 172440, 174503, 178648, 170279, 186584, 154407, 220376, 86823]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [65, 131, 263, 527, 1055, 2111, 4223, 8447, 16895, 33791, 67583, 135167]) == [173645, 173580, 173711, 173960, 173447, 172440, 174503, 178648, 170279, 186584, 154407, 220376, 86823]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 18, 27, 34, 41, 48, 55]) == [8, 15, 29, 6, 36, 13, 61, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 18, 27, 34, 41, 48, 55]) == [8, 15, 29, 6, 36, 13, 61, 10]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323]) == [583287, 583284, 583293, 583270, 583223, 583364, 582685, 584854, 587063, 571860, 548733, 715910, 194423, 1746084]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323]) == [583287, 583284, 583293, 583270, 583223, 583364, 582685, 584854, 587063, 571860, 548733, 715910, 194423, 1746084]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 7, 13, 18, 24, 30, 36, 42, 48, 54, 60]) == [27, 25, 30, 19, 1, 25, 7, 35, 9, 57, 15, 51]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 7, 13, 18, 24, 30, 36, 42, 48, 54, 60]) == [27, 25, 30, 19, 1, 25, 7, 35, 9, 57, 15, 51]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39]) == [39, 36, 35, 40, 39, 52, 35, 56, 39, 4, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39]) == [39, 36, 35, 40, 39, 52, 35, 56, 39, 4, 35]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 34, 37, 40, 43, 46, 49]) == [44, 51, 17, 52, 28, 55, 25, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 34, 37, 40, 43, 46, 49]) == [44, 51, 17, 52, 28, 55, 25, 40]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [255, 222, 199, 176, 153, 130, 107, 84]) == [185, 70, 152, 95, 239, 118, 244, 159, 203]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [255, 222, 199, 176, 153, 130, 107, 84]) == [185, 70, 152, 95, 239, 118, 244, 159, 203]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [19, 22, 25, 28, 31, 34, 37]) == [32, 51, 37, 60, 32, 63, 29, 56]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [19, 22, 25, 28, 31, 34, 37]) == [32, 51, 37, 60, 32, 63, 29, 56]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 22, 13, 20, 9, 16, 11]) == [26, 21, 3, 14, 26, 19, 3, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 22, 13, 20, 9, 16, 11]) == [26, 21, 3, 14, 26, 19, 3, 8]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]) == [93, 57, 175, 103, 157, 433, 239, 383, 189, 329, 879, 311, 957]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]) == [93, 57, 175, 103, 157, 433, 239, 383, 189, 329, 879, 311, 957]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 22, 3, 26, 11, 28, 7, 30, 13, 32, 9, 34, 5, 36, 1]) == [56, 55, 33, 34, 56, 51, 47, 40, 54, 59, 27, 18, 48, 53, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 22, 3, 26, 11, 28, 7, 30, 13, 32, 9, 34, 5, 36, 1]) == [56, 55, 33, 34, 56, 51, 47, 40, 54, 59, 27, 18, 48, 53, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [3267, 4924, 7363, 6972, 6339, 6460, 6595, 6588, 6531, 6556, 6547, 6548, 6551, 6550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [3267, 4924, 7363, 6972, 6339, 6460, 6595, 6588, 6531, 6556, 6547, 6548, 6551, 6550]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [4, 12, 8, 16, 10, 18, 14]) == [6, 2, 14, 6, 22, 28, 14, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [4, 12, 8, 16, 10, 18, 14]) == [6, 2, 14, 6, 22, 28, 14, 0]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [42, 35, 26, 15, 4, 17, 38, 67, 114, 181, 278, 399]) == [325, 367, 332, 342, 345, 349, 332, 362, 297, 347, 494, 248, 375]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [42, 35, 26, 15, 4, 17, 38, 67, 114, 181, 278, 399]) == [325, 367, 332, 342, 345, 349, 332, 362, 297, 347, 494, 248, 375]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [968, 940, 868, 584, 984, 556, 116, 712, 488, 620, 388]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [968, 940, 868, 584, 984, 556, 116, 712, 488, 620, 388]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245]) == [250, 5, 251, 6, 250, 1, 251, 2, 250, 13, 251, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245]) == [250, 5, 251, 6, 250, 1, 251, 2, 250, 13, 251, 14]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]) == [2796223, 2796219, 2796211, 2796195, 2796163, 2796227, 2796099, 2796355, 2795843, 2796867, 2794819, 2798915, 2790723, 2807107, 2774339, 2839875, 2708803, 2970947, 2446659, 3495235, 1398083, 5592387]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]) == [2796223, 2796219, 2796211, 2796195, 2796163, 2796227, 2796099, 2796355, 2795843, 2796867, 2794819, 2798915, 2790723, 2807107, 2774339, 2839875, 2708803, 2970947, 2446659, 3495235, 1398083, 5592387]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]) == [14, 2, 12, 28, 14, 26, 12, 20, 14, 18, 12, 44, 14, 42, 12, 36, 14, 34, 12, 60, 14, 58, 12, 52, 14, 50, 12, 76, 14, 74, 12, 68, 14, 66, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]) == [14, 2, 12, 28, 14, 26, 12, 20, 14, 18, 12, 44, 14, 42, 12, 36, 14, 34, 12, 60, 14, 58, 12, 52, 14, 50, 12, 76, 14, 74, 12, 68, 14, 66, 12]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64]) == [16, 8, 20, 52, 16, 56, 20, 36, 16, 40, 20, 84]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64]) == [16, 8, 20, 52, 16, 56, 20, 36, 16, 40, 20, 84]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == [11, 14, 9, 0, 11, 6, 9, 24, 11, 30, 9, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == [11, 14, 9, 0, 11, 6, 9, 24, 11, 30, 9, 16]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]) == [40, 45, 37, 46, 32, 49, 37, 50, 40, 53, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]) == [40, 45, 37, 46, 32, 49, 37, 50, 40, 53, 21]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [17, 19, 21, 23, 25, 27, 29, 31]) == [1, 16, 3, 22, 1, 24, 3, 30, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [17, 19, 21, 23, 25, 27, 29, 31]) == [1, 16, 3, 22, 1, 24, 3, 30, 1]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [19, 22, 17, 24, 19, 30, 17, 0, 19, 6, 17, 8, 19, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [19, 22, 17, 24, 19, 30, 17, 0, 19, 6, 17, 8, 19, 14]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [99, 198, 297, 396, 495, 594, 693, 792, 891, 990, 1089]) == [978, 945, 887, 606, 978, 573, 111, 730, 450, 697, 359, 1318]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [99, 198, 297, 396, 495, 594, 693, 792, 891, 990, 1089]) == [978, 945, 887, 606, 978, 573, 111, 730, 450, 697, 359, 1318]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2047, 4094, 2047, 4094, 2047, 4094, 2047, 4094, 2047, 4094, 2047]) == [4082, 2061, 2035, 12, 4082, 2061, 2035, 12, 4082, 2061, 2035, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2047, 4094, 2047, 4094, 2047, 4094, 2047, 4094, 2047, 4094, 2047]) == [4082, 2061, 2035, 12, 4082, 2061, 2035, 12, 4082, 2061, 2035, 12]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == [2097151, 2097149, 2097147, 2097143, 2097135, 2097119, 2097087, 2097023, 2096895, 2096639, 2096127, 2095103, 2093055, 2088959, 2080767, 2064383, 2031615, 1966079, 1835007, 1572863, 1048575]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == [2097151, 2097149, 2097147, 2097143, 2097135, 2097119, 2097087, 2097023, 2096895, 2096639, 2096127, 2095103, 2093055, 2088959, 2080767, 2064383, 2031615, 1966079, 1835007, 1572863, 1048575]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [30, 10, 20, 15, 25, 12, 22, 17, 27, 14, 24, 19, 29, 16, 26]) == [5, 27, 17, 5, 10, 19, 31, 9, 24, 3, 13, 21, 6, 27, 11, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [30, 10, 20, 15, 25, 12, 22, 17, 27, 14, 24, 19, 29, 16, 26]) == [5, 27, 17, 5, 10, 19, 31, 9, 24, 3, 13, 21, 6, 27, 11, 17]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == [161, 94, 222, 158, 190, 174, 166, 162, 160, 161]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == [161, 94, 222, 158, 190, 174, 166, 162, 160, 161]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 22, 33, 46, 59, 74, 91, 110, 131, 154]) == [134, 137, 159, 190, 144, 171, 225, 186, 212, 87, 205]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 22, 33, 46, 59, 74, 91, 110, 131, 154]) == [134, 137, 159, 190, 144, 171, 225, 186, 212, 87, 205]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [14, 11, 12, 15, 16, 19, 20, 23, 24, 27]) == [27, 21, 30, 18, 29, 13, 30, 10, 29, 5, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [14, 11, 12, 15, 16, 19, 20, 23, 24, 27]) == [27, 21, 30, 18, 29, 13, 30, 10, 29, 5, 30]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == [838849, 838878, 838881, 838814, 838753, 839070, 839265, 838046, 837217, 842142, 845409, 825758, 812641, 891294, 943713, 629150, 419425]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == [838849, 838878, 838881, 838814, 838753, 839070, 839265, 838046, 837217, 842142, 845409, 825758, 812641, 891294, 943713, 629150, 419425]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [11, 24, 29, 36, 43, 50, 57]) == [6, 13, 21, 8, 44, 7, 53, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [11, 24, 29, 36, 43, 50, 57]) == [6, 13, 21, 8, 44, 7, 53, 12]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [13, 22, 31, 40, 49, 58, 67]) == [12, 1, 23, 8, 32, 17, 43, 104]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [13, 22, 31, 40, 49, 58, 67]) == [12, 1, 23, 8, 32, 17, 43, 104]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == [35, 38, 44, 35, 55, 46, 48, 19, 59, 22, 36, 19, 47, 110, 40, 99, 51, 102]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == [35, 38, 44, 35, 55, 46, 48, 19, 59, 22, 36, 19, 47, 110, 40, 99, 51, 102]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [14, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [5, 11, 29, 9, 27, 11, 5, 9, 3, 11, 13, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [14, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [5, 11, 29, 9, 27, 11, 5, 9, 3, 11, 13, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 14, 21, 28, 35, 42, 49]) == [48, 55, 57, 44, 48, 19, 57, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 14, 21, 28, 35, 42, 49]) == [48, 55, 57, 44, 48, 19, 57, 8]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [127, 63, 31, 15, 7, 3, 1]) == [59, 68, 123, 100, 107, 108, 111, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [127, 63, 31, 15, 7, 3, 1]) == [59, 68, 123, 100, 107, 108, 111, 110]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [27, 24, 21, 18, 15, 12, 9, 6, 3]) == [11, 16, 8, 29, 15, 0, 12, 5, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [27, 24, 21, 18, 15, 12, 9, 6, 3]) == [11, 16, 8, 29, 15, 0, 12, 5, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [409, 614, 921, 870, 793, 806, 825, 822, 817, 818, 819]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [409, 614, 921, 870, 793, 806, 825, 822, 817, 818, 819]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 28, 33, 30, 35, 32, 37]) == [42, 53, 41, 8, 22, 53, 21, 48]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 28, 33, 30, 35, 32, 37]) == [42, 53, 41, 8, 22, 53, 21, 48]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 23, 19, 21, 17, 13, 9, 5, 1]) == [1, 14, 25, 10, 31, 14, 3, 10, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 23, 19, 21, 17, 13, 9, 5, 1]) == [1, 14, 25, 10, 31, 14, 3, 10, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 6, 14, 7, 13, 6, 10, 7, 9, 6, 22, 7, 21, 6, 18, 7, 17, 6, 30, 7, 29, 6, 26, 7, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 6, 14, 7, 13, 6, 10, 7, 9, 6, 22, 7, 21, 6, 18, 7, 17, 6, 30, 7, 29, 6, 26, 7, 25]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == [29, 24, 17, 28, 13, 24, 1, 28, 61, 24, 49, 28, 45, 24, 33, 28, 93, 24, 81, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == [29, 24, 17, 28, 13, 24, 1, 28, 61, 24, 49, 28, 45, 24, 33, 28, 93, 24, 81, 28]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1639, 2456, 3687, 3480, 3175, 3224, 3303, 3288, 3271, 3272, 3279, 3276, 3277]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1639, 2456, 3687, 3480, 3175, 3224, 3303, 3288, 3271, 3272, 3279, 3276, 3277]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [25, 30, 35, 40, 45, 50, 55]) == [12, 21, 11, 40, 0, 45, 31, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [25, 30, 35, 40, 45, 50, 55]) == [12, 21, 11, 40, 0, 45, 31, 40]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == [33, 37, 35, 43, 33, 45, 35, 51, 33, 53, 35, 59, 33, 61, 35, 3, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == [33, 37, 35, 43, 33, 45, 35, 51, 33, 53, 35, 59, 33, 61, 35, 3, 33]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [13091, 19676, 29475, 27868, 25379, 25820, 26403, 26332, 26147, 26204, 26211, 26236, 26227, 26228, 26231, 26230]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [13091, 19676, 29475, 27868, 25379, 25820, 26403, 26332, 26147, 26204, 26211, 26236, 26227, 26228, 26231, 26230]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [3, 10, 17, 24, 31, 38, 45]) == [60, 63, 53, 36, 60, 35, 5, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [3, 10, 17, 24, 31, 38, 45]) == [60, 63, 53, 36, 60, 35, 5, 40]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [13, 23, 37, 55, 77, 103, 133, 167, 205, 247, 293, 343, 397]) == [335, 322, 341, 368, 327, 266, 365, 488, 335, 386, 373, 80, 263, 138]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [13, 23, 37, 55, 77, 103, 133, 167, 205, 247, 293, 343, 397]) == [335, 322, 341, 368, 327, 266, 365, 488, 335, 386, 373, 80, 263, 138]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [14, 23, 32, 41, 50, 59, 68]) == [13, 3, 20, 52, 29, 47, 20, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [14, 23, 32, 41, 50, 59, 68]) == [13, 3, 20, 52, 29, 47, 20, 80]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 26, 2, 21, 3, 22, 2, 17, 3, 18, 2, 13, 3, 14, 2, 9, 3, 10, 2, 5, 3, 6, 2, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 26, 2, 21, 3, 22, 2, 17, 3, 18, 2, 13, 3, 14, 2, 9, 3, 10, 2, 5, 3, 6, 2, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [10, 20, 15, 25, 30, 22, 28, 19, 29, 12]) == [4, 14, 26, 21, 12, 18, 4, 24, 11, 22, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [10, 20, 15, 25, 30, 22, 28, 19, 29, 12]) == [4, 14, 26, 21, 12, 18, 4, 24, 11, 22, 26]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [23, 45, 12, 34, 56, 78, 90, 112, 134]) == [58, 45, 0, 12, 46, 22, 88, 2, 114, 244]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [23, 45, 12, 34, 56, 78, 90, 112, 134]) == [58, 45, 0, 12, 46, 22, 88, 2, 114, 244]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 22, 30, 39, 45, 51, 57, 63, 69]) == [54, 57, 47, 49, 22, 59, 8, 49, 14, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 22, 30, 39, 45, 51, 57, 63, 69]) == [54, 57, 47, 49, 22, 59, 8, 49, 14, 75]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [3, 9, 15, 21, 27, 33, 39]) == [53, 54, 63, 48, 37, 62, 31, 56]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [3, 9, 15, 21, 27, 33, 39]) == [53, 54, 63, 48, 37, 62, 31, 56]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312, 26624, 53248, 106496, 212992, 425984, 851968, 1703936, 3407872, 6815744, 13631488, 27262976, 54525952, 109051904, 218103808, 436207616, 872415232, 1744830464, 3489660928, 6979321856, 13958643712, 27917287424, 55834574848, 111669149696, 223338299392, 446676598784, 893353197568, 1786706395136, 3573412790272]) == [2015771317626, 2015771317623, 2015771317613, 2015771317593, 2015771317553, 2015771317729, 2015771317313, 2015771318017, 2015771316609, 2015771319425, 2015771313793, 2015771325057, 2015771302529, 2015771347585, 2015771257473, 2015771437697, 2015771077249, 2015771798145, 2015770356353, 2015773239937, 2015767472769, 2015779007105, 2015755938433, 2015802075777, 2015709801089, 2015894350465, 2015525251713, 2016263449217, 2014787054209, 2017739844225, 2011834264193, 2023645424257, 2000023104129, 2047267744385, 1952778463873, 2141757024897, 1763799902849, 1420202519169, 1007885658753, 4031542635137]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312, 26624, 53248, 106496, 212992, 425984, 851968, 1703936, 3407872, 6815744, 13631488, 27262976, 54525952, 109051904, 218103808, 436207616, 872415232, 1744830464, 3489660928, 6979321856, 13958643712, 27917287424, 55834574848, 111669149696, 223338299392, 446676598784, 893353197568, 1786706395136, 3573412790272]) == [2015771317626, 2015771317623, 2015771317613, 2015771317593, 2015771317553, 2015771317729, 2015771317313, 2015771318017, 2015771316609, 2015771319425, 2015771313793, 2015771325057, 2015771302529, 2015771347585, 2015771257473, 2015771437697, 2015771077249, 2015771798145, 2015770356353, 2015773239937, 2015767472769, 2015779007105, 2015755938433, 2015802075777, 2015709801089, 2015894350465, 2015525251713, 2016263449217, 2014787054209, 2017739844225, 2011834264193, 2023645424257, 2000023104129, 2047267744385, 1952778463873, 2141757024897, 1763799902849, 1420202519169, 1007885658753, 4031542635137]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 12, 19, 26, 33, 40, 47]) == [54, 51, 63, 44, 54, 23, 63, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 12, 19, 26, 33, 40, 47]) == [54, 51, 63, 44, 54, 23, 63, 16]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == [8, 10, 14, 8, 0, 10, 6, 8, 24, 10, 30, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == [8, 10, 14, 8, 0, 10, 6, 8, 24, 10, 30, 8]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143]) == [197, 206, 216, 249, 213, 226, 160, 237, 181, 214, 184, 193, 69, 202]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143]) == [197, 206, 216, 249, 213, 226, 160, 237, 181, 214, 184, 193, 69, 202]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [63, 66, 69, 72, 75, 78, 81]) == [76, 115, 49, 116, 60, 119, 57, 104]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [63, 66, 69, 72, 75, 78, 81]) == [76, 115, 49, 116, 60, 119, 57, 104]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == [109, 112, 111, 74, 99, 72, 103, 82, 105, 84, 23, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == [109, 112, 111, 74, 99, 72, 103, 82, 105, 84, 23, 80]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1023, 511, 255, 127, 63, 31, 15, 7]) == [409, 614, 921, 870, 793, 806, 825, 822, 817]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1023, 511, 255, 127, 63, 31, 15, 7]) == [409, 614, 921, 870, 793, 806, 825, 822, 817]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 30, 29, 28, 27, 26, 25, 24, 23]) == [11, 20, 10, 23, 11, 16, 10, 19, 11, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 30, 29, 28, 27, 26, 25, 24, 23]) == [11, 20, 10, 23, 11, 16, 10, 19, 11, 28]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189, 16381, 32765, 65533, 131077, 262149]) == [157301, 157304, 157285, 157272, 157221, 157400, 157477, 156888, 156453, 158936, 160549, 150744, 144165, 183512, 52445, 314584]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189, 16381, 32765, 65533, 131077, 262149]) == [157301, 157304, 157285, 157272, 157221, 157400, 157477, 156888, 156453, 158936, 160549, 150744, 144165, 183512, 52445, 314584]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [9, 19, 31, 45, 61, 79, 99, 121, 145, 171, 199, 229, 261, 295, 331]) == [369, 376, 363, 372, 345, 356, 299, 328, 305, 416, 267, 460, 297, 44, 267, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [9, 19, 31, 45, 61, 79, 99, 121, 145, 171, 199, 229, 261, 295, 331]) == [369, 376, 363, 372, 345, 356, 299, 328, 305, 416, 267, 460, 297, 44, 267, 64]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 14, 17, 9, 22, 15, 26, 11, 24]) == [8, 23, 25, 8, 1, 23, 24, 2, 9, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 14, 17, 9, 22, 15, 26, 11, 24]) == [8, 23, 25, 8, 1, 23, 24, 2, 9, 17]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [4, 13, 12, 15, 10, 19, 18, 21, 14, 23, 22]) == [31, 27, 22, 26, 21, 31, 12, 30, 11, 5, 18, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [4, 13, 12, 15, 10, 19, 18, 21, 14, 23, 22]) == [31, 27, 22, 26, 21, 31, 12, 30, 11, 5, 18, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273]) == [163, 164, 169, 188, 163, 136, 177, 248, 163, 204, 73, 212, 99, 176, 65, 336]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273]) == [163, 164, 169, 188, 163, 136, 177, 248, 163, 204, 73, 212, 99, 176, 65, 336]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 22, 17, 24, 19, 26, 21, 28, 23]) == [3, 12, 26, 11, 19, 0, 26, 15, 19, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 22, 17, 24, 19, 26, 21, 28, 23]) == [3, 12, 26, 11, 19, 0, 26, 15, 19, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [2, 3, 1, 6, 5, 4, 11, 10, 9, 16, 15, 14, 21, 20, 19]) == [17, 19, 16, 17, 23, 18, 22, 29, 23, 30, 14, 1, 15, 26, 14, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [2, 3, 1, 6, 5, 4, 11, 10, 9, 16, 15, 14, 21, 20, 19]) == [17, 19, 16, 17, 23, 18, 22, 29, 23, 30, 14, 1, 15, 26, 14, 29]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 20, 17, 23, 18, 24, 19]) == [19, 28, 8, 25, 14, 28, 4, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 20, 17, 23, 18, 24, 19]) == [19, 28, 8, 25, 14, 28, 4, 23]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 29, 27, 25, 23, 21, 19, 17, 15]) == [11, 20, 9, 18, 11, 28, 9, 26, 11, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 29, 27, 25, 23, 21, 19, 17, 15]) == [11, 20, 9, 18, 11, 28, 9, 26, 11, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [65, 68, 71, 74, 77, 80, 83]) == [86, 23, 83, 20, 94, 19, 67, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [65, 68, 71, 74, 77, 80, 83]) == [86, 23, 83, 20, 94, 19, 67, 16]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 20, 25, 30, 35, 40, 45, 50, 55]) == [27, 20, 0, 25, 7, 36, 12, 33, 19, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 20, 25, 30, 35, 40, 45, 50, 55]) == [27, 20, 0, 25, 7, 36, 12, 33, 19, 36]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [100, 200, 50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == [639, 539, 723, 737, 631, 653, 979, 529, 55, 701, 83, 769, 183]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [100, 200, 50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == [639, 539, 723, 737, 631, 653, 979, 529, 55, 701, 83, 769, 183]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101]) == [122, 5, 123, 6, 122, 1, 123, 2, 122, 13, 123, 14, 122, 9, 123, 10, 122, 21, 123, 22, 122, 17, 123, 18, 122, 29, 123, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101]) == [122, 5, 123, 6, 122, 1, 123, 2, 122, 13, 123, 14, 122, 9, 123, 10, 122, 21, 123, 22, 122, 17, 123, 18, 122, 29, 123, 30]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [6553, 9830, 14745, 13926, 12697, 12902, 13209, 13158, 13081, 13094, 13113, 13110, 13105, 13106, 13107]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [6553, 9830, 14745, 13926, 12697, 12902, 13209, 13158, 13081, 13094, 13113, 13110, 13105, 13106, 13107]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [127, 130, 133, 136, 139, 142, 145]) == [140, 243, 113, 244, 124, 247, 121, 232]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [127, 130, 133, 136, 139, 142, 145]) == [140, 243, 113, 244, 124, 247, 121, 232]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == [5, 0, 9, 4, 21, 0, 25, 4, 37, 0, 41, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == [5, 0, 9, 4, 21, 0, 25, 4, 37, 0, 41, 4]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120]) == [1, 2, 4, 13, 1, 14, 28, 9, 17, 10, 20, 53, 17, 54, 28, 49, 1, 50, 4, 61, 1, 62, 124, 57, 113, 58, 116, 37, 113, 38, 124, 33, 65, 34, 68, 45, 65, 46, 92, 41, 81]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120]) == [1, 2, 4, 13, 1, 14, 28, 9, 17, 10, 20, 53, 17, 54, 28, 49, 1, 50, 4, 61, 1, 62, 124, 57, 113, 58, 116, 37, 113, 38, 124, 33, 65, 34, 68, 45, 65, 46, 92, 41, 81]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == [831, 830, 829, 826, 821, 810, 789, 874, 917, 618, 405, 1642]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == [831, 830, 829, 826, 821, 810, 789, 874, 917, 618, 405, 1642]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == [1, 101, 6, 100, 5, 101, 58, 100, 57, 101, 62, 100, 61, 101, 50, 100, 49]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == [1, 101, 6, 100, 5, 101, 58, 100, 57, 101, 62, 100, 61, 101, 50, 100, 49]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [31, 14, 7, 3, 1, 0, 2, 6, 14, 30, 62, 126, 254]) == [100, 123, 117, 114, 113, 112, 112, 114, 116, 122, 100, 90, 36, 218]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [31, 14, 7, 3, 1, 0, 2, 6, 14, 30, 62, 126, 254]) == [100, 123, 117, 114, 113, 112, 112, 114, 116, 122, 100, 90, 36, 218]: {e}')
    
    total += 1
    try:
        result = candidate(encoded = [15, 27, 18, 23, 31, 45, 56, 67, 78]) == [105, 102, 125, 111, 120, 103, 74, 114, 49, 127]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(encoded = [15, 27, 18, 23, 31, 45, 56, 67, 78]) == [105, 102, 125, 111, 120, 103, 74, 114, 49, 127]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(encoded = [15, 8, 12, 4, 1]) == [11, 4, 12, 0, 4, 5]
    assert candidate(encoded = [1, 7, 6, 5, 4, 3]) == [1, 0, 7, 1, 4, 0, 3]
    assert candidate(encoded = [6, 5, 4, 6]) == [2, 4, 1, 5, 3]
    assert candidate(encoded = [8, 12, 4, 6, 1, 3, 5]) == [1, 9, 5, 1, 7, 6, 5, 0]
    assert candidate(encoded = [2, 3, 1, 4, 7]) == [0, 2, 1, 0, 4, 3]
    assert candidate(encoded = [8, 13, 10, 3, 7, 12, 9]) == [10, 2, 15, 5, 6, 1, 13, 4]
    assert candidate(encoded = [2, 3, 1, 6, 7, 0]) == [5, 7, 4, 5, 3, 4, 4]
    assert candidate(encoded = [1, 5, 7]) == [1, 0, 5, 2]
    assert candidate(encoded = [8, 9, 10, 11, 12, 13, 14]) == [7, 15, 6, 12, 7, 11, 6, 8]
    assert candidate(encoded = [7, 8, 9, 10, 11, 12]) == [14, 9, 1, 8, 2, 9, 5]
    assert candidate(encoded = [15, 10, 5, 2, 1, 4]) == [12, 3, 9, 12, 14, 15, 11]
    assert candidate(encoded = [2, 3, 2]) == [7, 5, 6, 4]
    assert candidate(encoded = [1, 0, 1, 0, 1]) == [7, 6, 6, 7, 7, 6]
    assert candidate(encoded = [7, 3, 5]) == [7, 0, 3, 6]
    assert candidate(encoded = [1, 6, 5, 4, 3, 2]) == [0, 1, 7, 2, 6, 5, 7]
    assert candidate(encoded = [2, 3, 1, 4, 5]) == [0, 2, 1, 0, 4, 1]
    assert candidate(encoded = [3, 1]) == [1, 2, 3]
    assert candidate(encoded = [123, 234, 345, 456, 567, 678, 789, 890, 901, 1002]) == [788, 879, 901, 732, 788, 291, 901, 144, 1002, 111, 901]
    assert candidate(encoded = [14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == [9, 7, 21, 3, 25, 7, 37, 3, 41, 7, 53, 3, 57]
    assert candidate(encoded = [15, 10, 5, 3, 2, 1, 4]) == [0, 15, 5, 0, 3, 1, 0, 4]
    assert candidate(encoded = [5, 10, 15, 20, 25, 30, 35]) == [8, 13, 7, 8, 28, 5, 27, 56]
    assert candidate(encoded = [2, 15, 18, 17, 20, 23, 22, 25, 28]) == [27, 25, 22, 4, 21, 1, 22, 0, 25, 5]
    assert candidate(encoded = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [3, 2, 0, 3, 7, 2, 4, 3, 11, 2, 8, 3, 15, 2, 12, 3, 19, 2, 16, 3, 23, 2, 20, 3, 27, 2]
    assert candidate(encoded = [77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198]) == [95, 18, 74, 41, 71, 62, 186, 53, 175, 10, 186, 1, 199]
    assert candidate(encoded = [9, 20, 27, 34, 41, 48, 55]) == [14, 7, 19, 8, 42, 3, 51, 4]
    assert candidate(encoded = [7, 2, 5, 8, 3, 6, 1, 4, 9]) == [3, 4, 6, 3, 11, 8, 14, 15, 11, 2]
    assert candidate(encoded = [65, 131, 263, 527, 1055, 2111, 4223, 8447, 16895, 33791, 67583, 135167]) == [173645, 173580, 173711, 173960, 173447, 172440, 174503, 178648, 170279, 186584, 154407, 220376, 86823]
    assert candidate(encoded = [7, 18, 27, 34, 41, 48, 55]) == [8, 15, 29, 6, 36, 13, 61, 10]
    assert candidate(encoded = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323]) == [583287, 583284, 583293, 583270, 583223, 583364, 582685, 584854, 587063, 571860, 548733, 715910, 194423, 1746084]
    assert candidate(encoded = [2, 7, 13, 18, 24, 30, 36, 42, 48, 54, 60]) == [27, 25, 30, 19, 1, 25, 7, 35, 9, 57, 15, 51]
    assert candidate(encoded = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39]) == [39, 36, 35, 40, 39, 52, 35, 56, 39, 4, 35]
    assert candidate(encoded = [31, 34, 37, 40, 43, 46, 49]) == [44, 51, 17, 52, 28, 55, 25, 40]
    assert candidate(encoded = [255, 222, 199, 176, 153, 130, 107, 84]) == [185, 70, 152, 95, 239, 118, 244, 159, 203]
    assert candidate(encoded = [19, 22, 25, 28, 31, 34, 37]) == [32, 51, 37, 60, 32, 63, 29, 56]
    assert candidate(encoded = [15, 22, 13, 20, 9, 16, 11]) == [26, 21, 3, 14, 26, 19, 3, 8]
    assert candidate(encoded = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]) == [93, 57, 175, 103, 157, 433, 239, 383, 189, 329, 879, 311, 957]
    assert candidate(encoded = [15, 22, 3, 26, 11, 28, 7, 30, 13, 32, 9, 34, 5, 36, 1]) == [56, 55, 33, 34, 56, 51, 47, 40, 54, 59, 27, 18, 48, 53, 17, 16]
    assert candidate(encoded = [8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [3267, 4924, 7363, 6972, 6339, 6460, 6595, 6588, 6531, 6556, 6547, 6548, 6551, 6550]
    assert candidate(encoded = [4, 12, 8, 16, 10, 18, 14]) == [6, 2, 14, 6, 22, 28, 14, 0]
    assert candidate(encoded = [42, 35, 26, 15, 4, 17, 38, 67, 114, 181, 278, 399]) == [325, 367, 332, 342, 345, 349, 332, 362, 297, 347, 494, 248, 375]
    assert candidate(encoded = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [968, 940, 868, 584, 984, 556, 116, 712, 488, 620, 388]
    assert candidate(encoded = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245]) == [250, 5, 251, 6, 250, 1, 251, 2, 250, 13, 251, 14]
    assert candidate(encoded = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]) == [2796223, 2796219, 2796211, 2796195, 2796163, 2796227, 2796099, 2796355, 2795843, 2796867, 2794819, 2798915, 2790723, 2807107, 2774339, 2839875, 2708803, 2970947, 2446659, 3495235, 1398083, 5592387]
    assert candidate(encoded = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]) == [14, 2, 12, 28, 14, 26, 12, 20, 14, 18, 12, 44, 14, 42, 12, 36, 14, 34, 12, 60, 14, 58, 12, 52, 14, 50, 12, 76, 14, 74, 12, 68, 14, 66, 12]
    assert candidate(encoded = [24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64]) == [16, 8, 20, 52, 16, 56, 20, 36, 16, 40, 20, 84]
    assert candidate(encoded = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == [11, 14, 9, 0, 11, 6, 9, 24, 11, 30, 9, 16]
    assert candidate(encoded = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]) == [40, 45, 37, 46, 32, 49, 37, 50, 40, 53, 21]
    assert candidate(encoded = [17, 19, 21, 23, 25, 27, 29, 31]) == [1, 16, 3, 22, 1, 24, 3, 30, 1]
    assert candidate(encoded = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [19, 22, 17, 24, 19, 30, 17, 0, 19, 6, 17, 8, 19, 14]
    assert candidate(encoded = [99, 198, 297, 396, 495, 594, 693, 792, 891, 990, 1089]) == [978, 945, 887, 606, 978, 573, 111, 730, 450, 697, 359, 1318]
    assert candidate(encoded = [2047, 4094, 2047, 4094, 2047, 4094, 2047, 4094, 2047, 4094, 2047]) == [4082, 2061, 2035, 12, 4082, 2061, 2035, 12, 4082, 2061, 2035, 12]
    assert candidate(encoded = [2, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == [2097151, 2097149, 2097147, 2097143, 2097135, 2097119, 2097087, 2097023, 2096895, 2096639, 2096127, 2095103, 2093055, 2088959, 2080767, 2064383, 2031615, 1966079, 1835007, 1572863, 1048575]
    assert candidate(encoded = [30, 10, 20, 15, 25, 12, 22, 17, 27, 14, 24, 19, 29, 16, 26]) == [5, 27, 17, 5, 10, 19, 31, 9, 24, 3, 13, 21, 6, 27, 11, 17]
    assert candidate(encoded = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == [161, 94, 222, 158, 190, 174, 166, 162, 160, 161]
    assert candidate(encoded = [15, 22, 33, 46, 59, 74, 91, 110, 131, 154]) == [134, 137, 159, 190, 144, 171, 225, 186, 212, 87, 205]
    assert candidate(encoded = [14, 11, 12, 15, 16, 19, 20, 23, 24, 27]) == [27, 21, 30, 18, 29, 13, 30, 10, 29, 5, 30]
    assert candidate(encoded = [31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == [838849, 838878, 838881, 838814, 838753, 839070, 839265, 838046, 837217, 842142, 845409, 825758, 812641, 891294, 943713, 629150, 419425]
    assert candidate(encoded = [11, 24, 29, 36, 43, 50, 57]) == [6, 13, 21, 8, 44, 7, 53, 12]
    assert candidate(encoded = [13, 22, 31, 40, 49, 58, 67]) == [12, 1, 23, 8, 32, 17, 43, 104]
    assert candidate(encoded = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == [35, 38, 44, 35, 55, 46, 48, 19, 59, 22, 36, 19, 47, 110, 40, 99, 51, 102]
    assert candidate(encoded = [14, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [5, 11, 29, 9, 27, 11, 5, 9, 3, 11, 13, 9, 11]
    assert candidate(encoded = [7, 14, 21, 28, 35, 42, 49]) == [48, 55, 57, 44, 48, 19, 57, 8]
    assert candidate(encoded = [127, 63, 31, 15, 7, 3, 1]) == [59, 68, 123, 100, 107, 108, 111, 110]
    assert candidate(encoded = [27, 24, 21, 18, 15, 12, 9, 6, 3]) == [11, 16, 8, 29, 15, 0, 12, 5, 3, 0]
    assert candidate(encoded = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [409, 614, 921, 870, 793, 806, 825, 822, 817, 818, 819]
    assert candidate(encoded = [31, 28, 33, 30, 35, 32, 37]) == [42, 53, 41, 8, 22, 53, 21, 48]
    assert candidate(encoded = [15, 23, 19, 21, 17, 13, 9, 5, 1]) == [1, 14, 25, 10, 31, 14, 3, 10, 15, 14]
    assert candidate(encoded = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 6, 14, 7, 13, 6, 10, 7, 9, 6, 22, 7, 21, 6, 18, 7, 17, 6, 30, 7, 29, 6, 26, 7, 25]
    assert candidate(encoded = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == [29, 24, 17, 28, 13, 24, 1, 28, 61, 24, 49, 28, 45, 24, 33, 28, 93, 24, 81, 28]
    assert candidate(encoded = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1639, 2456, 3687, 3480, 3175, 3224, 3303, 3288, 3271, 3272, 3279, 3276, 3277]
    assert candidate(encoded = [25, 30, 35, 40, 45, 50, 55]) == [12, 21, 11, 40, 0, 45, 31, 40]
    assert candidate(encoded = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == [33, 37, 35, 43, 33, 45, 35, 51, 33, 53, 35, 59, 33, 61, 35, 3, 33]
    assert candidate(encoded = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [13091, 19676, 29475, 27868, 25379, 25820, 26403, 26332, 26147, 26204, 26211, 26236, 26227, 26228, 26231, 26230]
    assert candidate(encoded = [3, 10, 17, 24, 31, 38, 45]) == [60, 63, 53, 36, 60, 35, 5, 40]
    assert candidate(encoded = [13, 23, 37, 55, 77, 103, 133, 167, 205, 247, 293, 343, 397]) == [335, 322, 341, 368, 327, 266, 365, 488, 335, 386, 373, 80, 263, 138]
    assert candidate(encoded = [14, 23, 32, 41, 50, 59, 68]) == [13, 3, 20, 52, 29, 47, 20, 80]
    assert candidate(encoded = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 26, 2, 21, 3, 22, 2, 17, 3, 18, 2, 13, 3, 14, 2, 9, 3, 10, 2, 5, 3, 6, 2, 1, 3, 2]
    assert candidate(encoded = [10, 20, 15, 25, 30, 22, 28, 19, 29, 12]) == [4, 14, 26, 21, 12, 18, 4, 24, 11, 22, 26]
    assert candidate(encoded = [23, 45, 12, 34, 56, 78, 90, 112, 134]) == [58, 45, 0, 12, 46, 22, 88, 2, 114, 244]
    assert candidate(encoded = [15, 22, 30, 39, 45, 51, 57, 63, 69]) == [54, 57, 47, 49, 22, 59, 8, 49, 14, 75]
    assert candidate(encoded = [3, 9, 15, 21, 27, 33, 39]) == [53, 54, 63, 48, 37, 62, 31, 56]
    assert candidate(encoded = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312, 26624, 53248, 106496, 212992, 425984, 851968, 1703936, 3407872, 6815744, 13631488, 27262976, 54525952, 109051904, 218103808, 436207616, 872415232, 1744830464, 3489660928, 6979321856, 13958643712, 27917287424, 55834574848, 111669149696, 223338299392, 446676598784, 893353197568, 1786706395136, 3573412790272]) == [2015771317626, 2015771317623, 2015771317613, 2015771317593, 2015771317553, 2015771317729, 2015771317313, 2015771318017, 2015771316609, 2015771319425, 2015771313793, 2015771325057, 2015771302529, 2015771347585, 2015771257473, 2015771437697, 2015771077249, 2015771798145, 2015770356353, 2015773239937, 2015767472769, 2015779007105, 2015755938433, 2015802075777, 2015709801089, 2015894350465, 2015525251713, 2016263449217, 2014787054209, 2017739844225, 2011834264193, 2023645424257, 2000023104129, 2047267744385, 1952778463873, 2141757024897, 1763799902849, 1420202519169, 1007885658753, 4031542635137]
    assert candidate(encoded = [5, 12, 19, 26, 33, 40, 47]) == [54, 51, 63, 44, 54, 23, 63, 16]
    assert candidate(encoded = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == [8, 10, 14, 8, 0, 10, 6, 8, 24, 10, 30, 8]
    assert candidate(encoded = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143]) == [197, 206, 216, 249, 213, 226, 160, 237, 181, 214, 184, 193, 69, 202]
    assert candidate(encoded = [63, 66, 69, 72, 75, 78, 81]) == [76, 115, 49, 116, 60, 119, 57, 104]
    assert candidate(encoded = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == [109, 112, 111, 74, 99, 72, 103, 82, 105, 84, 23, 80]
    assert candidate(encoded = [1023, 511, 255, 127, 63, 31, 15, 7]) == [409, 614, 921, 870, 793, 806, 825, 822, 817]
    assert candidate(encoded = [31, 30, 29, 28, 27, 26, 25, 24, 23]) == [11, 20, 10, 23, 11, 16, 10, 19, 11, 28]
    assert candidate(encoded = [13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189, 16381, 32765, 65533, 131077, 262149]) == [157301, 157304, 157285, 157272, 157221, 157400, 157477, 156888, 156453, 158936, 160549, 150744, 144165, 183512, 52445, 314584]
    assert candidate(encoded = [9, 19, 31, 45, 61, 79, 99, 121, 145, 171, 199, 229, 261, 295, 331]) == [369, 376, 363, 372, 345, 356, 299, 328, 305, 416, 267, 460, 297, 44, 267, 64]
    assert candidate(encoded = [31, 14, 17, 9, 22, 15, 26, 11, 24]) == [8, 23, 25, 8, 1, 23, 24, 2, 9, 17]
    assert candidate(encoded = [4, 13, 12, 15, 10, 19, 18, 21, 14, 23, 22]) == [31, 27, 22, 26, 21, 31, 12, 30, 11, 5, 18, 4]
    assert candidate(encoded = [7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273]) == [163, 164, 169, 188, 163, 136, 177, 248, 163, 204, 73, 212, 99, 176, 65, 336]
    assert candidate(encoded = [15, 22, 17, 24, 19, 26, 21, 28, 23]) == [3, 12, 26, 11, 19, 0, 26, 15, 19, 4]
    assert candidate(encoded = [2, 3, 1, 6, 5, 4, 11, 10, 9, 16, 15, 14, 21, 20, 19]) == [17, 19, 16, 17, 23, 18, 22, 29, 23, 30, 14, 1, 15, 26, 14, 29]
    assert candidate(encoded = [15, 20, 17, 23, 18, 24, 19]) == [19, 28, 8, 25, 14, 28, 4, 23]
    assert candidate(encoded = [31, 29, 27, 25, 23, 21, 19, 17, 15]) == [11, 20, 9, 18, 11, 28, 9, 26, 11, 4]
    assert candidate(encoded = [65, 68, 71, 74, 77, 80, 83]) == [86, 23, 83, 20, 94, 19, 67, 16]
    assert candidate(encoded = [15, 20, 25, 30, 35, 40, 45, 50, 55]) == [27, 20, 0, 25, 7, 36, 12, 33, 19, 36]
    assert candidate(encoded = [100, 200, 50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == [639, 539, 723, 737, 631, 653, 979, 529, 55, 701, 83, 769, 183]
    assert candidate(encoded = [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101]) == [122, 5, 123, 6, 122, 1, 123, 2, 122, 13, 123, 14, 122, 9, 123, 10, 122, 21, 123, 22, 122, 17, 123, 18, 122, 29, 123, 30]
    assert candidate(encoded = [16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [6553, 9830, 14745, 13926, 12697, 12902, 13209, 13158, 13081, 13094, 13113, 13110, 13105, 13106, 13107]
    assert candidate(encoded = [127, 130, 133, 136, 139, 142, 145]) == [140, 243, 113, 244, 124, 247, 121, 232]
    assert candidate(encoded = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == [5, 0, 9, 4, 21, 0, 25, 4, 37, 0, 41, 4]
    assert candidate(encoded = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120]) == [1, 2, 4, 13, 1, 14, 28, 9, 17, 10, 20, 53, 17, 54, 28, 49, 1, 50, 4, 61, 1, 62, 124, 57, 113, 58, 116, 37, 113, 38, 124, 33, 65, 34, 68, 45, 65, 46, 92, 41, 81]
    assert candidate(encoded = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == [831, 830, 829, 826, 821, 810, 789, 874, 917, 618, 405, 1642]
    assert candidate(encoded = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == [1, 101, 6, 100, 5, 101, 58, 100, 57, 101, 62, 100, 61, 101, 50, 100, 49]
    assert candidate(encoded = [31, 14, 7, 3, 1, 0, 2, 6, 14, 30, 62, 126, 254]) == [100, 123, 117, 114, 113, 112, 112, 114, 116, 122, 100, 90, 36, 218]
    assert candidate(encoded = [15, 27, 18, 23, 31, 45, 56, 67, 78]) == [105, 102, 125, 111, 120, 103, 74, 114, 49, 127]


