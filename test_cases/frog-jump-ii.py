def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 15, 20, 25]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 15, 20, 25]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 6, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 6, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 10, 15, 20, 25, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 10, 15, 20, 25, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 15, 25, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 15, 25, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 20, 30, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 20, 30, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 5, 7, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 5, 7, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 5, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 5, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 100, 200, 300, 400]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 100, 200, 300, 400]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 9, 20, 33, 48, 65, 84, 105, 128, 153, 180, 209, 240, 273, 308, 345, 384, 425, 468, 513, 560, 609, 660, 713, 768, 825]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 9, 20, 33, 48, 65, 84, 105, 128, 153, 180, 209, 240, 273, 308, 345, 384, 425, 468, 513, 560, 609, 660, 713, 768, 825]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 14, 27, 44, 65, 90, 121, 158, 201, 250]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 14, 27, 44, 65, 90, 121, 158, 201, 250]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 10, 22, 46, 94, 190, 382, 766, 1534, 3070, 6142, 12286]) == 9216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 10, 22, 46, 94, 190, 382, 766, 1534, 3070, 6142, 12286]) == 9216: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 11, 24, 39, 56, 75, 96, 119, 144, 171, 200, 231, 264, 300, 339, 380, 423, 468, 515, 564, 615, 668, 723, 780, 840, 903, 968, 1035, 1104, 1175]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 11, 24, 39, 56, 75, 96, 119, 144, 171, 200, 231, 264, 300, 339, 380, 423, 468, 515, 564, 615, 668, 723, 780, 840, 903, 968, 1035, 1104, 1175]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 8, 16, 28, 44, 63, 85, 110, 138, 169, 203, 240, 279, 321]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 8, 16, 28, 44, 63, 85, 110, 138, 169, 203, 240, 279, 321]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 100, 250, 450, 700, 1000, 1350, 1750, 2200, 2700]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 100, 250, 450, 700, 1000, 1350, 1750, 2200, 2700]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 25, 45, 70, 100, 140, 185, 240, 305, 380, 470, 575, 695, 830, 980]) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 25, 45, 70, 100, 140, 185, 240, 305, 380, 470, 575, 695, 830, 980]) == 285: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 6144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 6144: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == 805306368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == 805306368: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 12288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 12288: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 6144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 6144: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 10, 19, 31, 46, 64, 85, 109, 136]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 10, 19, 31, 46, 64, 85, 109, 136]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 4, 7, 11, 16, 22]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 4, 7, 11, 16, 22]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 15, 25, 35, 50, 75, 110, 150, 200, 260, 330, 410, 500, 600, 710, 830, 960, 1100, 1250, 1410, 1580, 1760, 1950, 2150, 2360, 2580, 2810, 3050, 3300, 3560, 3830, 4110, 4400, 4700, 5010, 5330, 5660, 6000, 6350, 6710, 7080, 7460, 7850, 8250, 8660, 9080, 9510, 9950, 10400, 10860, 11330, 11810, 12300, 12800, 13310, 13830, 14360, 14900, 15450, 16010, 16580, 17160, 17750, 18350, 18960, 19580, 20210, 20850, 21500, 22160, 22830, 23510, 24200, 24900, 25610, 26330, 27060, 27800, 28550, 29310, 30080, 30860, 31650, 32450, 33260, 34080, 34910, 35750, 36600, 37460, 38330, 39210, 40100, 41000, 41910, 42830, 43760, 44700, 45650, 46610, 47580, 48560, 49550, 50550, 51560, 52580, 53610, 54650, 55700, 56760, 57830, 58910, 60000]) == 2170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 15, 25, 35, 50, 75, 110, 150, 200, 260, 330, 410, 500, 600, 710, 830, 960, 1100, 1250, 1410, 1580, 1760, 1950, 2150, 2360, 2580, 2810, 3050, 3300, 3560, 3830, 4110, 4400, 4700, 5010, 5330, 5660, 6000, 6350, 6710, 7080, 7460, 7850, 8250, 8660, 9080, 9510, 9950, 10400, 10860, 11330, 11810, 12300, 12800, 13310, 13830, 14360, 14900, 15450, 16010, 16580, 17160, 17750, 18350, 18960, 19580, 20210, 20850, 21500, 22160, 22830, 23510, 24200, 24900, 25610, 26330, 27060, 27800, 28550, 29310, 30080, 30860, 31650, 32450, 33260, 34080, 34910, 35750, 36600, 37460, 38330, 39210, 40100, 41000, 41910, 42830, 43760, 44700, 45650, 46610, 47580, 48560, 49550, 50550, 51560, 52580, 53610, 54650, 55700, 56760, 57830, 58910, 60000]) == 2170: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 5, 14, 29, 50, 81, 122, 173, 234, 305, 386, 477, 578, 689, 810, 941, 1082, 1233, 1394, 1565, 1746, 1937, 2148, 2379, 2620, 2871, 3132, 3403, 3684, 3975, 4276, 4587, 4908, 5239, 5580, 5931, 6292, 6663, 7044, 7435, 7836, 8247, 8668, 9099, 9540, 9991, 10452, 10923, 11404, 11895, 12406, 12937, 13488, 14059, 14640, 15231, 15832, 16443, 17064, 17695, 18336, 18987, 19648, 20320]) == 1333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 5, 14, 29, 50, 81, 122, 173, 234, 305, 386, 477, 578, 689, 810, 941, 1082, 1233, 1394, 1565, 1746, 1937, 2148, 2379, 2620, 2871, 3132, 3403, 3684, 3975, 4276, 4587, 4908, 5239, 5580, 5931, 6292, 6663, 7044, 7435, 7836, 8247, 8668, 9099, 9540, 9991, 10452, 10923, 11404, 11895, 12406, 12937, 13488, 14059, 14640, 15231, 15832, 16443, 17064, 17695, 18336, 18987, 19648, 20320]) == 1333: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]) == 1610612736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]) == 1610612736: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 9, 18, 30, 45, 63, 84, 108, 135, 165, 198, 234, 273, 315, 360, 408, 459, 513, 570]) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 9, 18, 30, 45, 63, 84, 108, 135, 165, 198, 234, 273, 315, 360, 408, 459, 513, 570]) == 111: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 7, 12, 20, 30, 45, 65, 90]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 7, 12, 20, 30, 45, 65, 90]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 7, 15, 26, 39, 54, 71, 90, 111, 134, 159]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 7, 15, 26, 39, 54, 71, 90, 111, 134, 159]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 335, 395, 460, 530, 605, 685, 770, 860, 955, 1055, 1160, 1270, 1385, 1505, 1630, 1760, 1895, 2035]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 335, 395, 460, 530, 605, 685, 770, 860, 955, 1055, 1160, 1270, 1385, 1505, 1630, 1760, 1895, 2035]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096]) == 1352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096]) == 1352: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 14, 27, 42, 60, 81, 105]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 14, 27, 42, 60, 81, 105]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 8, 18, 30, 44, 60, 78, 98, 120, 144, 170, 198, 228, 260, 294, 330, 368, 408, 450, 494, 540]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 8, 18, 30, 44, 60, 78, 98, 120, 144, 170, 198, 228, 260, 294, 330, 368, 408, 450, 494, 540]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 8, 15, 25, 38, 54, 73]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 8, 15, 25, 38, 54, 73]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 12, 20, 28, 36, 45, 55, 66, 78, 90]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 12, 20, 28, 36, 45, 55, 66, 78, 90]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660, 780, 910, 1050, 1200]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660, 780, 910, 1050, 1200]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 6, 14, 24, 36, 50, 66, 84, 104, 126, 150, 176, 204, 234, 266, 300, 336]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 6, 14, 24, 36, 50, 66, 84, 104, 126, 150, 176, 204, 234, 266, 300, 336]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 8, 12, 15, 20, 25, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 8, 12, 15, 20, 25, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 5, 14, 28, 47, 71, 100, 134, 173, 217, 266, 320, 379, 443, 512, 586, 665, 749, 834, 922, 1015, 1113, 1216]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 5, 14, 28, 47, 71, 100, 134, 173, 217, 266, 320, 379, 443, 512, 586, 665, 749, 834, 922, 1015, 1113, 1216]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 8, 13, 21, 28, 35, 40]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 8, 13, 21, 28, 35, 40]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 5, 11, 19, 29, 41, 55, 71, 89, 109, 131, 155, 181, 209, 239, 271, 305, 341, 379, 419, 461, 505, 551, 600, 651, 704, 759, 817, 877, 940, 1005, 1072, 1141, 1212, 1285, 1360, 1437, 1516, 1597, 1680, 1765, 1852, 1941, 2032, 2125, 2220, 2317, 2416, 2517, 2620, 2725, 2832, 2941, 3052, 3165, 3280, 3400, 3523, 3648, 3775, 3904, 4035, 4168, 4303, 4440, 4580, 4722, 4867, 5014, 5163, 5314, 5467, 5622, 5779, 5938, 6099, 6262, 6427, 6594, 6763, 6934, 7107, 7282, 7459, 7638, 7819, 8002, 8187, 8374, 8563, 8754, 8947, 9142, 9339, 9538, 9739, 9942]) == 404
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 5, 11, 19, 29, 41, 55, 71, 89, 109, 131, 155, 181, 209, 239, 271, 305, 341, 379, 419, 461, 505, 551, 600, 651, 704, 759, 817, 877, 940, 1005, 1072, 1141, 1212, 1285, 1360, 1437, 1516, 1597, 1680, 1765, 1852, 1941, 2032, 2125, 2220, 2317, 2416, 2517, 2620, 2725, 2832, 2941, 3052, 3165, 3280, 3400, 3523, 3648, 3775, 3904, 4035, 4168, 4303, 4440, 4580, 4722, 4867, 5014, 5163, 5314, 5467, 5622, 5779, 5938, 6099, 6262, 6427, 6594, 6763, 6934, 7107, 7282, 7459, 7638, 7819, 8002, 8187, 8374, 8563, 8754, 8947, 9142, 9339, 9538, 9739, 9942]) == 404: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273, 307, 343, 381, 421, 463, 507, 553, 601]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273, 307, 343, 381, 421, 463, 507, 553, 601]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646, 9565938, 28697814, 86093442, 258280326, 774840978, 2324522934]) == 2066242608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646, 9565938, 28697814, 86093442, 258280326, 774840978, 2324522934]) == 2066242608: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 400]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 400]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 384: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660, 780, 910, 1050]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660, 780, 910, 1050]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390, 455, 525]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390, 455, 525]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 25, 40, 55, 70, 85, 100, 120, 140, 160, 180, 200]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 25, 40, 55, 70, 85, 100, 120, 140, 160, 180, 200]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 25, 45, 70, 100, 135, 175, 220, 270, 325]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 25, 45, 70, 100, 135, 175, 220, 270, 325]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 11, 18, 26, 35, 45, 56, 68, 81, 95, 110, 126, 143, 161, 180, 200]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 11, 18, 26, 35, 45, 56, 68, 81, 95, 110, 126, 143, 161, 180, 200]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273, 307, 343, 381]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273, 307, 343, 381]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991, 1036, 1082, 1129, 1177, 1226, 1276, 1327, 1379, 1432, 1486, 1541, 1597, 1654, 1712, 1771, 1831, 1892, 1954, 2017, 2081, 2146, 2212, 2279, 2347, 2416, 2486, 2557, 2629, 2702, 2776, 2851, 2927, 3004, 3082, 3161, 3241, 3322, 3404, 3487, 3571, 3656, 3742, 3829, 3917, 4006, 4096, 4187, 4279, 4372, 4466, 4561, 4657, 4754, 4852, 4951, 5051]) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991, 1036, 1082, 1129, 1177, 1226, 1276, 1327, 1379, 1432, 1486, 1541, 1597, 1654, 1712, 1771, 1831, 1892, 1954, 2017, 2081, 2146, 2212, 2279, 2347, 2416, 2486, 2557, 2629, 2702, 2776, 2851, 2927, 3004, 3082, 3161, 3241, 3322, 3404, 3487, 3571, 3656, 3742, 3829, 3917, 4006, 4096, 4187, 4279, 4372, 4466, 4561, 4657, 4754, 4852, 4951, 5051]) == 199: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 7, 17, 32, 52, 77, 107, 142, 182, 227, 277, 332, 392]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 7, 17, 32, 52, 77, 107, 142, 182, 227, 277, 332, 392]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 5, 14, 29, 49, 74, 104, 139, 179, 218]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 5, 14, 29, 49, 74, 104, 139, 179, 218]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330]) == 361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330]) == 361: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 7, 16, 27, 40, 55, 72, 91, 112, 135, 160, 187, 216, 247, 280, 315, 352, 391, 432, 475]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 7, 16, 27, 40, 55, 72, 91, 112, 135, 160, 187, 216, 247, 280, 315, 352, 391, 432, 475]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 21, 33, 46, 60, 75, 91, 108, 126, 145, 165, 186, 208, 231, 255, 280, 306, 333, 361, 390, 420, 451, 483, 516]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 21, 33, 46, 60, 75, 91, 108, 126, 145, 165, 186, 208, 231, 255, 280, 306, 333, 361, 390, 420, 451, 483, 516]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 10, 19, 31, 46, 64, 85, 109, 136, 166, 200]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 10, 19, 31, 46, 64, 85, 109, 136, 166, 200]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 10, 15, 23, 30, 35]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 10, 15, 23, 30, 35]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 25, 45, 70, 100, 135, 175, 220, 270]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 25, 45, 70, 100, 135, 175, 220, 270]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 7, 14, 22, 31, 40, 50, 60, 70]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 7, 14, 22, 31, 40, 50, 60, 70]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 8, 15, 23, 36, 55, 89, 144]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 8, 15, 23, 36, 55, 89, 144]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 13, 24, 37, 52, 69, 88, 109, 132, 157, 184, 213, 244, 277, 312, 349, 388, 429]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 13, 24, 37, 52, 69, 88, 109, 132, 157, 184, 213, 244, 277, 312, 349, 388, 429]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]) == 28657
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]) == 28657: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 6, 14, 25, 40, 58, 79, 103, 130, 160, 193, 230, 270, 315]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 6, 14, 25, 40, 58, 79, 103, 130, 160, 193, 230, 270, 315]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 5, 14, 29, 49, 74, 104, 139, 179, 218, 258, 300, 344, 391, 441, 494, 550, 610, 674, 742, 815, 893, 976]) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 5, 14, 29, 49, 74, 104, 139, 179, 218, 258, 300, 344, 391, 441, 494, 550, 610, 674, 742, 815, 893, 976]) == 161: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230, 252, 275, 299, 324, 350, 377, 405, 434, 464, 495]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230, 252, 275, 299, 324, 350, 377, 405, 434, 464, 495]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 5, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 5, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 3, 8, 14, 21, 29, 38, 48, 59, 71, 84, 98]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 3, 8, 14, 21, 29, 38, 48, 59, 71, 84, 98]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 10, 22, 36, 52, 70, 90, 112, 136, 162, 190, 220, 252, 286]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 10, 22, 36, 52, 70, 90, 112, 136, 162, 190, 220, 252, 286]) == 66: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(stones = [0, 10, 15, 20, 25]) == 15
    assert candidate(stones = [0, 1, 2, 3, 4, 5]) == 2
    assert candidate(stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(stones = [0, 2, 5, 6, 7]) == 5
    assert candidate(stones = [0, 1, 3, 6, 10, 15]) == 9
    assert candidate(stones = [0, 5, 10, 15, 20, 25, 30]) == 10
    assert candidate(stones = [0, 3, 9]) == 9
    assert candidate(stones = [0, 10, 15, 25, 30]) == 15
    assert candidate(stones = [0, 10, 20, 30, 40]) == 20
    assert candidate(stones = [0, 1, 3, 5, 7, 9]) == 4
    assert candidate(stones = [0, 1, 3, 5, 10]) == 7
    assert candidate(stones = [0, 100, 200, 300, 400]) == 200
    assert candidate(stones = [0, 9, 20, 33, 48, 65, 84, 105, 128, 153, 180, 209, 240, 273, 308, 345, 384, 425, 468, 513, 560, 609, 660, 713, 768, 825]) == 112
    assert candidate(stones = [0, 5, 14, 27, 44, 65, 90, 121, 158, 201, 250]) == 92
    assert candidate(stones = [0, 1, 4, 10, 22, 46, 94, 190, 382, 766, 1534, 3070, 6142, 12286]) == 9216
    assert candidate(stones = [0, 11, 24, 39, 56, 75, 96, 119, 144, 171, 200, 231, 264, 300, 339, 380, 423, 468, 515, 564, 615, 668, 723, 780, 840, 903, 968, 1035, 1104, 1175]) == 140
    assert candidate(stones = [0, 3, 8, 16, 28, 44, 63, 85, 110, 138, 169, 203, 240, 279, 321]) == 81
    assert candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379]) == 53
    assert candidate(stones = [0, 100, 250, 450, 700, 1000, 1350, 1750, 2200, 2700]) == 950
    assert candidate(stones = [0, 10, 25, 45, 70, 100, 140, 185, 240, 305, 380, 470, 575, 695, 830, 980]) == 285
    assert candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 6144
    assert candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == 805306368
    assert candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225]) == 85
    assert candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 12288
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 17
    assert candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 6144
    assert candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600]) == 94
    assert candidate(stones = [0, 1, 4, 10, 19, 31, 46, 64, 85, 109, 136]) == 51
    assert candidate(stones = [0, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330]) == 83
    assert candidate(stones = [0, 2, 4, 7, 11, 16, 22]) == 11
    assert candidate(stones = [0, 10, 15, 25, 35, 50, 75, 110, 150, 200, 260, 330, 410, 500, 600, 710, 830, 960, 1100, 1250, 1410, 1580, 1760, 1950, 2150, 2360, 2580, 2810, 3050, 3300, 3560, 3830, 4110, 4400, 4700, 5010, 5330, 5660, 6000, 6350, 6710, 7080, 7460, 7850, 8250, 8660, 9080, 9510, 9950, 10400, 10860, 11330, 11810, 12300, 12800, 13310, 13830, 14360, 14900, 15450, 16010, 16580, 17160, 17750, 18350, 18960, 19580, 20210, 20850, 21500, 22160, 22830, 23510, 24200, 24900, 25610, 26330, 27060, 27800, 28550, 29310, 30080, 30860, 31650, 32450, 33260, 34080, 34910, 35750, 36600, 37460, 38330, 39210, 40100, 41000, 41910, 42830, 43760, 44700, 45650, 46610, 47580, 48560, 49550, 50550, 51560, 52580, 53610, 54650, 55700, 56760, 57830, 58910, 60000]) == 2170
    assert candidate(stones = [0, 1, 5, 14, 29, 50, 81, 122, 173, 234, 305, 386, 477, 578, 689, 810, 941, 1082, 1233, 1394, 1565, 1746, 1937, 2148, 2379, 2620, 2871, 3132, 3403, 3684, 3975, 4276, 4587, 4908, 5239, 5580, 5931, 6292, 6663, 7044, 7435, 7836, 8247, 8668, 9099, 9540, 9991, 10452, 10923, 11404, 11895, 12406, 12937, 13488, 14059, 14640, 15231, 15832, 16443, 17064, 17695, 18336, 18987, 19648, 20320]) == 1333
    assert candidate(stones = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]) == 1610612736
    assert candidate(stones = [0, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 36
    assert candidate(stones = [0, 3, 9, 18, 30, 45, 63, 84, 108, 135, 165, 198, 234, 273, 315, 360, 408, 459, 513, 570]) == 111
    assert candidate(stones = [0, 3, 7, 12, 20, 30, 45, 65, 90]) == 45
    assert candidate(stones = [0, 2, 7, 15, 26, 39, 54, 71, 90, 111, 134, 159]) == 48
    assert candidate(stones = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224]) == 56
    assert candidate(stones = [0, 5, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 335, 395, 460, 530, 605, 685, 770, 860, 955, 1055, 1160, 1270, 1385, 1505, 1630, 1760, 1895, 2035]) == 275
    assert candidate(stones = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096]) == 1352
    assert candidate(stones = [0, 5, 14, 27, 42, 60, 81, 105]) == 45
    assert candidate(stones = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]) == 200
    assert candidate(stones = [0, 8, 18, 30, 44, 60, 78, 98, 120, 144, 170, 198, 228, 260, 294, 330, 368, 408, 450, 494, 540]) == 90
    assert candidate(stones = [0, 3, 8, 15, 25, 38, 54, 73]) == 35
    assert candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380]) == 74
    assert candidate(stones = [0, 5, 12, 20, 28, 36, 45, 55, 66, 78, 90]) == 24
    assert candidate(stones = [0, 10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660, 780, 910, 1050, 1200]) == 290
    assert candidate(stones = [0, 6, 14, 24, 36, 50, 66, 84, 104, 126, 150, 176, 204, 234, 266, 300, 336]) == 70
    assert candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65]) == 21
    assert candidate(stones = [0, 2, 8, 12, 15, 20, 25, 30]) == 10
    assert candidate(stones = [0, 1, 5, 14, 28, 47, 71, 100, 134, 173, 217, 266, 320, 379, 443, 512, 586, 665, 749, 834, 922, 1015, 1113, 1216]) == 201
    assert candidate(stones = [0, 2, 5, 8, 13, 21, 28, 35, 40]) == 15
    assert candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90]) == 25
    assert candidate(stones = [0, 1, 5, 11, 19, 29, 41, 55, 71, 89, 109, 131, 155, 181, 209, 239, 271, 305, 341, 379, 419, 461, 505, 551, 600, 651, 704, 759, 817, 877, 940, 1005, 1072, 1141, 1212, 1285, 1360, 1437, 1516, 1597, 1680, 1765, 1852, 1941, 2032, 2125, 2220, 2317, 2416, 2517, 2620, 2725, 2832, 2941, 3052, 3165, 3280, 3400, 3523, 3648, 3775, 3904, 4035, 4168, 4303, 4440, 4580, 4722, 4867, 5014, 5163, 5314, 5467, 5622, 5779, 5938, 6099, 6262, 6427, 6594, 6763, 6934, 7107, 7282, 7459, 7638, 7819, 8002, 8187, 8374, 8563, 8754, 8947, 9142, 9339, 9538, 9739, 9942]) == 404
    assert candidate(stones = [0, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273, 307, 343, 381, 421, 463, 507, 553, 601]) == 94
    assert candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44]) == 17
    assert candidate(stones = [0, 2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646, 9565938, 28697814, 86093442, 258280326, 774840978, 2324522934]) == 2066242608
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 19
    assert candidate(stones = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 400]) == 77
    assert candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]) == 46
    assert candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172]) == 35
    assert candidate(stones = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 384
    assert candidate(stones = [0, 10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660, 780, 910, 1050]) == 270
    assert candidate(stones = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 100
    assert candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390, 455, 525]) == 135
    assert candidate(stones = [0, 10, 25, 40, 55, 70, 85, 100, 120, 140, 160, 180, 200]) == 40
    assert candidate(stones = [0, 10, 25, 45, 70, 100, 135, 175, 220, 270, 325]) == 105
    assert candidate(stones = [0, 5, 11, 18, 26, 35, 45, 56, 68, 81, 95, 110, 126, 143, 161, 180, 200]) == 39
    assert candidate(stones = [0, 1, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111, 133, 157, 183, 211, 241, 273, 307, 343, 381]) == 74
    assert candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991, 1036, 1082, 1129, 1177, 1226, 1276, 1327, 1379, 1432, 1486, 1541, 1597, 1654, 1712, 1771, 1831, 1892, 1954, 2017, 2081, 2146, 2212, 2279, 2347, 2416, 2486, 2557, 2629, 2702, 2776, 2851, 2927, 3004, 3082, 3161, 3241, 3322, 3404, 3487, 3571, 3656, 3742, 3829, 3917, 4006, 4096, 4187, 4279, 4372, 4466, 4561, 4657, 4754, 4852, 4951, 5051]) == 199
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 39
    assert candidate(stones = [0, 2, 7, 17, 32, 52, 77, 107, 142, 182, 227, 277, 332, 392]) == 115
    assert candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380]) == 74
    assert candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104]) == 27
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 17
    assert candidate(stones = [0, 1, 5, 14, 29, 49, 74, 104, 139, 179, 218]) == 79
    assert candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390]) == 115
    assert candidate(stones = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330]) == 361
    assert candidate(stones = [0, 7, 16, 27, 40, 55, 72, 91, 112, 135, 160, 187, 216, 247, 280, 315, 352, 391, 432, 475]) == 84
    assert candidate(stones = [0, 10, 21, 33, 46, 60, 75, 91, 108, 126, 145, 165, 186, 208, 231, 255, 280, 306, 333, 361, 390, 420, 451, 483, 516]) == 65
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528]) == 63
    assert candidate(stones = [0, 1, 4, 10, 19, 31, 46, 64, 85, 109, 136, 166, 200]) == 64
    assert candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 76
    assert candidate(stones = [0, 1, 4, 10, 15, 23, 30, 35]) == 15
    assert candidate(stones = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991]) == 87
    assert candidate(stones = [0, 10, 25, 45, 70, 100, 135, 175, 220, 270]) == 95
    assert candidate(stones = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 6
    assert candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600]) == 94
    assert candidate(stones = [0, 3, 7, 14, 22, 31, 40, 50, 60, 70]) == 20
    assert candidate(stones = [0, 1, 4, 8, 15, 23, 36, 55, 89, 144]) == 89
    assert candidate(stones = [0, 5, 13, 24, 37, 52, 69, 88, 109, 132, 157, 184, 213, 244, 277, 312, 349, 388, 429]) == 80
    assert candidate(stones = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]) == 28657
    assert candidate(stones = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420]) == 78
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190]) == 37
    assert candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024]) == 124
    assert candidate(stones = [0, 2, 6, 14, 25, 40, 58, 79, 103, 130, 160, 193, 230, 270, 315]) == 85
    assert candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64]) == 28
    assert candidate(stones = [0, 2, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 10
    assert candidate(stones = [0, 1, 3, 6, 10, 15, 21, 28]) == 13
    assert candidate(stones = [0, 1, 5, 14, 29, 49, 74, 104, 139, 179, 218, 258, 300, 344, 391, 441, 494, 550, 610, 674, 742, 815, 893, 976]) == 161
    assert candidate(stones = [0, 5, 15, 30, 50, 75, 105, 140, 180]) == 75
    assert candidate(stones = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230, 252, 275, 299, 324, 350, 377, 405, 434, 464, 495]) == 61
    assert candidate(stones = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 44
    assert candidate(stones = [0, 5, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 20
    assert candidate(stones = [0, 3, 8, 14, 21, 29, 38, 48, 59, 71, 84, 98]) == 27
    assert candidate(stones = [0, 10, 22, 36, 52, 70, 90, 112, 136, 162, 190, 220, 252, 286]) == 66


