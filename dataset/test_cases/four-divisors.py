def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [101, 103, 107, 109, 113]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 103, 107, 109, 113]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2310, 2320, 2330, 2340, 2350]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2310, 2320, 2330, 2340, 2350]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 44, 25, 63]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 44, 25, 63]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 100, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 100, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 8, 10, 12, 14]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 8, 10, 12, 14]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 144, 169]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 144, 169]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 13, 17, 19, 23]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 13, 17, 19, 23]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 21, 28, 30, 35]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 21, 28, 30, 35]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(nums = [105, 106, 107, 108, 109]) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [105, 106, 107, 108, 109]) == 162: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [110, 111, 112, 113, 114]) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [110, 111, 112, 113, 114]) == 152: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 21]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 21]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 21, 25, 49, 77]) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 21, 25, 49, 77]) == 152: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 8, 10, 12]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 8, 10, 12]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 21, 28, 30]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 21, 28, 30]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 49, 64, 81, 97]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 49, 64, 81, 97]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 49, 64, 81]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 49, 64, 81]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 21, 22]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 21, 22]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 4, 7]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 4, 7]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 40, 50, 60, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 40, 50, 60, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 1009, 1013, 1019, 1021]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 1009, 1013, 1019, 1021]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 21, 22, 28]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 21, 22, 28]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 28, 91]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 28, 91]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 49, 64, 81, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 49, 64, 81, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 8, 10, 12, 14]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 8, 10, 12, 14]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 525, 546, 567, 570, 588, 594, 616, 630, 646, 660, 672, 684]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 525, 546, 567, 570, 588, 594, 616, 630, 646, 660, 672, 684]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 162: {e}')
    
    total += 1
    try:
        result = candidate(nums = [144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [231, 252, 273, 294, 315]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [231, 252, 273, 294, 315]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [901, 903, 917, 923, 925, 927, 931, 943, 945, 949, 957, 963, 965, 979, 987, 989, 993, 995, 999, 1001]) == 10908
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [901, 903, 917, 923, 925, 927, 931, 943, 945, 949, 957, 963, 965, 979, 987, 989, 993, 995, 999, 1001]) == 10908: {e}')
    
    total += 1
    try:
        result = candidate(nums = [323, 333, 341, 351, 361]) == 744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [323, 333, 341, 351, 361]) == 744: {e}')
    
    total += 1
    try:
        result = candidate(nums = [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]) == 1242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]) == 1242: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010]) == 36664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010]) == 36664: {e}')
    
    total += 1
    try:
        result = candidate(nums = [231, 275, 299, 322, 341, 361, 385, 407, 429, 451, 473, 495]) == 2208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [231, 275, 299, 322, 341, 361, 385, 407, 429, 451, 473, 495]) == 2208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 505, 511, 513, 529, 539, 551, 561, 573, 583, 585, 595, 605, 621, 627, 637, 645, 651, 655, 667, 685]) == 5560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 505, 511, 513, 529, 539, 551, 561, 573, 583, 585, 595, 605, 621, 627, 637, 645, 651, 655, 667, 685]) == 5560: {e}')
    
    total += 1
    try:
        result = candidate(nums = [220, 280, 300, 330, 350]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [220, 280, 300, 330, 350]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [882, 924, 966, 1008, 1050]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [882, 924, 966, 1008, 1050]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2048, 2187, 2345, 2500, 2648, 2809, 3003, 3215, 3432, 3654, 3888]) == 3864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2048, 2187, 2345, 2500, 2648, 2809, 3003, 3215, 3432, 3654, 3888]) == 3864: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 143, 169, 181]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 143, 169, 181]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5005, 5007, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087]) == 6680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5005, 5007, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087]) == 6680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1001, 1002, 1003, 1005, 1006, 1007, 1009, 1011, 1013, 1015, 1017, 1019, 1021, 1023, 1025, 1027, 1029, 1031, 1033, 1035, 1037, 1039, 1041, 1043, 1045, 1047, 1049, 1051, 1053, 1055]) == 12524
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1001, 1002, 1003, 1005, 1006, 1007, 1009, 1011, 1013, 1015, 1017, 1019, 1021, 1023, 1025, 1027, 1029, 1031, 1033, 1035, 1037, 1039, 1041, 1043, 1045, 1047, 1049, 1051, 1053, 1055]) == 12524: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 84, 91, 112, 119, 126, 133]) == 416
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 84, 91, 112, 119, 126, 133]) == 416: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1100, 1120, 1122, 1134, 1140, 1155, 1166, 1176, 1183, 1197, 1209, 1225, 1232, 1242, 1254, 1260, 1275]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1100, 1120, 1122, 1134, 1140, 1155, 1166, 1176, 1183, 1197, 1209, 1225, 1232, 1242, 1254, 1260, 1275]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1485, 1506, 1527, 1548, 1569]) == 4136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1485, 1506, 1527, 1548, 1569]) == 4136: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 144, 169, 196, 225]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 144, 169, 196, 225]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1275, 1296, 1317, 1338, 1359]) == 1760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1275, 1296, 1317, 1338, 1359]) == 1760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10001, 10003, 10007, 10009, 10037, 10039, 10061, 10067, 10079]) == 21652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10001, 10003, 10007, 10009, 10037, 10039, 10061, 10067, 10079]) == 21652: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1330, 1333, 1343, 1353, 1369]) == 2848
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1330, 1333, 1343, 1353, 1369]) == 2848: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1105, 1111, 1122, 1147, 1159]) == 3680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1105, 1111, 1122, 1147, 1159]) == 3680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99997, 99989, 99971, 99959, 99949, 99929, 99907]) == 206104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99997, 99989, 99971, 99959, 99949, 99929, 99907]) == 206104: {e}')
    
    total += 1
    try:
        result = candidate(nums = [961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 143, 169, 189]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 143, 169, 189]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 18, 20, 24, 30, 36, 40, 42, 44, 45, 48, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 18, 20, 24, 30, 36, 40, 42, 44, 45, 48, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [435, 456, 477, 498, 519]) == 696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [435, 456, 477, 498, 519]) == 696: {e}')
    
    total += 1
    try:
        result = candidate(nums = [540, 561, 582, 603, 624]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [540, 561, 582, 603, 624]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11025, 11236, 11449, 11664, 11881, 12100, 12321, 12544, 12769, 12996]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11025, 11236, 11449, 11664, 11881, 12100, 12321, 12544, 12769, 12996]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [221, 231, 253, 273, 299]) == 876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [221, 231, 253, 273, 299]) == 876: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1380, 1401, 1422, 1443, 1464]) == 1872
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1380, 1401, 1422, 1443, 1464]) == 1872: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1820, 1833, 1849, 1859, 1877]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1820, 1833, 1849, 1859, 1877]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [713, 721, 741, 759, 779]) == 2440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [713, 721, 741, 759, 779]) == 2440: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1170, 1191, 1212, 1233, 1254]) == 1592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1170, 1191, 1212, 1233, 1254]) == 1592: {e}')
    
    total += 1
    try:
        result = candidate(nums = [130, 156, 168, 182, 208, 224, 234]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [130, 156, 168, 182, 208, 224, 234]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [407, 413, 437, 459, 463]) == 1416
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [407, 413, 437, 459, 463]) == 1416: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 41, 53, 61, 67, 71, 73, 79, 83, 89, 97, 101]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 41, 53, 61, 67, 71, 73, 79, 83, 89, 97, 101]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [960, 981, 1002, 1023, 1044]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [960, 981, 1002, 1023, 1044]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1363, 1403, 1459, 1489, 1517]) == 4524
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1363, 1403, 1459, 1489, 1517]) == 4524: {e}')
    
    total += 1
    try:
        result = candidate(nums = [496, 504, 512, 520, 528]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [496, 504, 512, 520, 528]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [245, 273, 294, 322, 338, 364, 378]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [245, 273, 294, 322, 338, 364, 378]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739]) == 2712
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739]) == 2712: {e}')
    
    total += 1
    try:
        result = candidate(nums = [385, 405, 429, 441, 455, 462, 473, 483, 495]) == 528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [385, 405, 429, 441, 455, 462, 473, 483, 495]) == 528: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1800, 1821, 1842, 1863, 1884]) == 2432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1800, 1821, 1842, 1863, 1884]) == 2432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 144, 169, 196]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 144, 169, 196]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1065, 1086, 1107, 1128, 1149]) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1065, 1086, 1107, 1128, 1149]) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2115, 2136, 2157, 2178, 2199]) == 5816
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2115, 2136, 2157, 2178, 2199]) == 5816: {e}')
    
    total += 1
    try:
        result = candidate(nums = [120, 180, 240, 300, 360]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [120, 180, 240, 300, 360]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 1189, 1247, 1271, 1309]) == 5148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 1189, 1247, 1271, 1309]) == 5148: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2002, 2014, 2021, 2035, 2047]) == 4272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2002, 2014, 2021, 2035, 2047]) == 4272: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1610, 1619, 1643, 1657, 1679]) == 3504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1610, 1619, 1643, 1657, 1679]) == 3504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [110, 132, 154, 176, 198]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [110, 132, 154, 176, 198]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [913, 943, 979, 1009, 1037]) == 4212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [913, 943, 979, 1009, 1037]) == 4212: {e}')
    
    total += 1
    try:
        result = candidate(nums = [700, 715, 729, 741, 756, 765, 777, 784, 792, 805, 819, 828, 832, 840, 855]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [700, 715, 729, 741, 756, 765, 777, 784, 792, 805, 819, 828, 832, 840, 855]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [330, 351, 372, 393, 414]) == 528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [330, 351, 372, 393, 414]) == 528: {e}')
    
    total += 1
    try:
        result = candidate(nums = [855, 876, 897, 918, 939]) == 1256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [855, 876, 897, 918, 939]) == 1256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1155, 1365, 1785, 1995, 2310, 2730, 3003, 3276, 3570]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1155, 1365, 1785, 1995, 2310, 2730, 3003, 3276, 3570]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [900, 910, 924, 936, 945, 966, 975, 990, 1001, 1008, 1014, 1029, 1035, 1053, 1056, 1065]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [900, 910, 924, 936, 945, 966, 975, 990, 1001, 1008, 1014, 1029, 1035, 1053, 1056, 1065]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [561, 609, 657, 703, 759]) == 760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [561, 609, 657, 703, 759]) == 760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1430, 1441, 1451, 1463, 1481]) == 1584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1430, 1441, 1451, 1463, 1481]) == 1584: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 143, 169, 180]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 143, 169, 180]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1541, 1547, 1561, 1577, 1589]) == 6928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1541, 1547, 1561, 1577, 1589]) == 6928: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1925, 1931, 1943, 1946, 1957]) == 4120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1925, 1931, 1943, 1946, 1957]) == 4120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1729, 1739, 1751, 1763, 1771]) == 5544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1729, 1739, 1751, 1763, 1771]) == 5544: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [143, 221, 247, 299, 323]) == 1396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [143, 221, 247, 299, 323]) == 1396: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1905, 1926, 1947, 1968, 1989]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1905, 1926, 1947, 1968, 1989]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [600, 625, 648, 675, 700, 729, 756, 784, 810, 841, 864, 891]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [600, 625, 648, 675, 700, 729, 756, 784, 810, 841, 864, 891]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [667, 713, 779, 817, 851]) == 4120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [667, 713, 779, 817, 851]) == 4120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65537, 65539, 65543, 65551, 65561, 65579, 65591, 65597]) == 208140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65537, 65539, 65543, 65551, 65561, 65579, 65591, 65597]) == 208140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [645, 666, 687, 708, 729]) == 920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [645, 666, 687, 708, 729]) == 920: {e}')
    
    total += 1
    try:
        result = candidate(nums = [105, 126, 147, 168, 189]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [105, 126, 147, 168, 189]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1386, 1452, 1518, 1584, 1650]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1386, 1452, 1518, 1584, 1650]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [903, 913, 924, 931, 943]) == 2016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [903, 913, 924, 931, 943]) == 2016: {e}')
    
    total += 1
    try:
        result = candidate(nums = [841, 961, 1089, 1225, 1369]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [841, 961, 1089, 1225, 1369]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [609, 621, 637, 651, 671]) == 744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [609, 621, 637, 651, 671]) == 744: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 125, 143, 147, 169, 175, 182, 189, 196, 209, 221, 225, 245, 253, 265, 275, 287, 299]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 125, 143, 147, 169, 175, 182, 189, 196, 209, 221, 225, 245, 253, 265, 275, 287, 299]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1695, 1716, 1737, 1758, 1779]) == 2376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1695, 1716, 1737, 1758, 1779]) == 2376: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1590, 1611, 1632, 1653, 1674]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1590, 1611, 1632, 1653, 1674]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [496, 672, 728, 840, 924]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [496, 672, 728, 840, 924]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 144, 169, 196, 225]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 144, 169, 196, 225]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1105, 1365, 1615, 1885, 2145, 2415, 2685, 2955, 3225, 3495, 3765]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1105, 1365, 1615, 1885, 2145, 2415, 2685, 2955, 3225, 3495, 3765]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [506, 518, 529, 539, 551]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [506, 518, 529, 539, 551]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1331, 1369, 1406, 1444, 1482, 1521, 1562, 1600, 1640, 1681, 1722, 1764]) == 1464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1331, 1369, 1406, 1444, 1482, 1521, 1562, 1600, 1640, 1681, 1722, 1764]) == 1464: {e}')
    
    total += 1
    try:
        result = candidate(nums = [406, 429, 455, 462, 494, 518, 546]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [406, 429, 455, 462, 494, 518, 546]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 60, 77, 84, 91, 99, 100]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 60, 77, 84, 91, 99, 100]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [325, 351, 375, 399, 425]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [325, 351, 375, 399, 425]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 458
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 458: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2010, 2031, 2052, 2073, 2094]) == 5480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2010, 2031, 2052, 2073, 2094]) == 5480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]) == 686
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]) == 686: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 1007, 1029, 1045, 1067]) == 2256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 1007, 1029, 1045, 1067]) == 2256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [805, 819, 836, 851, 869]) == 1872
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [805, 819, 836, 851, 869]) == 1872: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1221, 1235, 1241, 1254, 1265]) == 1332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1221, 1235, 1241, 1254, 1265]) == 1332: {e}')
    
    total += 1
    try:
        result = candidate(nums = [750, 771, 792, 813, 834]) == 2120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [750, 771, 792, 813, 834]) == 2120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [703, 707, 713, 725, 729, 735, 741, 745, 749, 759, 763, 779, 783, 799, 803, 805, 815, 825, 833, 835, 837, 841]) == 9572
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [703, 707, 713, 725, 729, 735, 741, 745, 749, 759, 763, 779, 783, 799, 803, 805, 815, 825, 833, 835, 837, 841]) == 9572: {e}')
    
    total += 1
    try:
        result = candidate(nums = [77, 110, 143, 176, 209]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [77, 110, 143, 176, 209]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [324, 325, 329, 333, 341, 343, 345, 351, 357, 361, 363, 371, 375, 385, 387, 399, 405, 425, 427, 429, 441, 451]) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [324, 325, 329, 333, 341, 343, 345, 351, 357, 361, 363, 371, 375, 385, 387, 399, 405, 425, 427, 429, 441, 451]) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1021, 1031, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1021, 1031, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [391, 437, 493, 529, 551]) == 2052
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [391, 437, 493, 529, 551]) == 2052: {e}')
    
    total += 1
    try:
        result = candidate(nums = [231, 255, 273, 297, 315, 333, 351]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [231, 255, 273, 297, 315, 333, 351]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [101, 103, 107, 109, 113]) == 0
    assert candidate(nums = [2310, 2320, 2330, 2340, 2350]) == 0
    assert candidate(nums = [30, 44, 25, 63]) == 0
    assert candidate(nums = [30, 100, 49]) == 0
    assert candidate(nums = [6, 8, 10, 12, 14]) == 69
    assert candidate(nums = [100, 121, 144, 169]) == 0
    assert candidate(nums = [11, 13, 17, 19, 23]) == 0
    assert candidate(nums = [15, 21, 28, 30, 35]) == 104
    assert candidate(nums = [105, 106, 107, 108, 109]) == 162
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [110, 111, 112, 113, 114]) == 152
    assert candidate(nums = [21, 21]) == 64
    assert candidate(nums = [15, 21, 25, 49, 77]) == 152
    assert candidate(nums = [6, 8, 10, 12]) == 45
    assert candidate(nums = [10, 15, 21, 28, 30]) == 74
    assert candidate(nums = [100, 101, 102, 103, 104]) == 0
    assert candidate(nums = [30, 49, 64, 81, 97]) == 0
    assert candidate(nums = [30, 49, 64, 81]) == 0
    assert candidate(nums = [10, 15, 21, 22]) == 110
    assert candidate(nums = [21, 4, 7]) == 32
    assert candidate(nums = [30, 40, 50, 60, 70]) == 0
    assert candidate(nums = [1001, 1009, 1013, 1019, 1021]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19]) == 0
    assert candidate(nums = [10, 15, 21, 22, 28]) == 110
    assert candidate(nums = [15, 28, 91]) == 136
    assert candidate(nums = [36, 49, 64, 81, 100]) == 0
    assert candidate(nums = [6, 8, 10, 12, 14]) == 69
    assert candidate(nums = [100, 101, 102, 103, 104]) == 0
    assert candidate(nums = [500, 525, 546, 567, 570, 588, 594, 616, 630, 646, 660, 672, 684]) == 0
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 162
    assert candidate(nums = [144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484]) == 0
    assert candidate(nums = [231, 252, 273, 294, 315]) == 0
    assert candidate(nums = [901, 903, 917, 923, 925, 927, 931, 943, 945, 949, 957, 963, 965, 979, 987, 989, 993, 995, 999, 1001]) == 10908
    assert candidate(nums = [323, 333, 341, 351, 361]) == 744
    assert candidate(nums = [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]) == 1242
    assert candidate(nums = [9999, 10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010]) == 36664
    assert candidate(nums = [231, 275, 299, 322, 341, 361, 385, 407, 429, 451, 473, 495]) == 2208
    assert candidate(nums = [500, 505, 511, 513, 529, 539, 551, 561, 573, 583, 585, 595, 605, 621, 627, 637, 645, 651, 655, 667, 685]) == 5560
    assert candidate(nums = [220, 280, 300, 330, 350]) == 0
    assert candidate(nums = [882, 924, 966, 1008, 1050]) == 0
    assert candidate(nums = [2048, 2187, 2345, 2500, 2648, 2809, 3003, 3215, 3432, 3654, 3888]) == 3864
    assert candidate(nums = [100, 121, 143, 169, 181]) == 168
    assert candidate(nums = [5005, 5007, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087]) == 6680
    assert candidate(nums = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 0
    assert candidate(nums = [1000, 1001, 1002, 1003, 1005, 1006, 1007, 1009, 1011, 1013, 1015, 1017, 1019, 1021, 1023, 1025, 1027, 1029, 1031, 1033, 1035, 1037, 1039, 1041, 1043, 1045, 1047, 1049, 1051, 1053, 1055]) == 12524
    assert candidate(nums = [56, 84, 91, 112, 119, 126, 133]) == 416
    assert candidate(nums = [1100, 1120, 1122, 1134, 1140, 1155, 1166, 1176, 1183, 1197, 1209, 1225, 1232, 1242, 1254, 1260, 1275]) == 0
    assert candidate(nums = [1485, 1506, 1527, 1548, 1569]) == 4136
    assert candidate(nums = [100, 121, 144, 169, 196, 225]) == 0
    assert candidate(nums = [1275, 1296, 1317, 1338, 1359]) == 1760
    assert candidate(nums = [10001, 10003, 10007, 10009, 10037, 10039, 10061, 10067, 10079]) == 21652
    assert candidate(nums = [1330, 1333, 1343, 1353, 1369]) == 2848
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 0
    assert candidate(nums = [1105, 1111, 1122, 1147, 1159]) == 3680
    assert candidate(nums = [100000, 99999, 99997, 99989, 99971, 99959, 99949, 99929, 99907]) == 206104
    assert candidate(nums = [961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600]) == 0
    assert candidate(nums = [100, 121, 143, 169, 189]) == 168
    assert candidate(nums = [12, 18, 20, 24, 30, 36, 40, 42, 44, 45, 48, 50]) == 0
    assert candidate(nums = [435, 456, 477, 498, 519]) == 696
    assert candidate(nums = [540, 561, 582, 603, 624]) == 0
    assert candidate(nums = [11025, 11236, 11449, 11664, 11881, 12100, 12321, 12544, 12769, 12996]) == 0
    assert candidate(nums = [221, 231, 253, 273, 299]) == 876
    assert candidate(nums = [1380, 1401, 1422, 1443, 1464]) == 1872
    assert candidate(nums = [1820, 1833, 1849, 1859, 1877]) == 0
    assert candidate(nums = [713, 721, 741, 759, 779]) == 2440
    assert candidate(nums = [1170, 1191, 1212, 1233, 1254]) == 1592
    assert candidate(nums = [130, 156, 168, 182, 208, 224, 234]) == 0
    assert candidate(nums = [407, 413, 437, 459, 463]) == 1416
    assert candidate(nums = [29, 41, 53, 61, 67, 71, 73, 79, 83, 89, 97, 101]) == 0
    assert candidate(nums = [960, 981, 1002, 1023, 1044]) == 0
    assert candidate(nums = [1363, 1403, 1459, 1489, 1517]) == 4524
    assert candidate(nums = [496, 504, 512, 520, 528]) == 0
    assert candidate(nums = [245, 273, 294, 322, 338, 364, 378]) == 0
    assert candidate(nums = [729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739]) == 2712
    assert candidate(nums = [385, 405, 429, 441, 455, 462, 473, 483, 495]) == 528
    assert candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 0
    assert candidate(nums = [1800, 1821, 1842, 1863, 1884]) == 2432
    assert candidate(nums = [100, 121, 144, 169, 196]) == 0
    assert candidate(nums = [1065, 1086, 1107, 1128, 1149]) == 1536
    assert candidate(nums = [1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249]) == 0
    assert candidate(nums = [2115, 2136, 2157, 2178, 2199]) == 5816
    assert candidate(nums = [120, 180, 240, 300, 360]) == 0
    assert candidate(nums = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063]) == 0
    assert candidate(nums = [1111, 1189, 1247, 1271, 1309]) == 5148
    assert candidate(nums = [2002, 2014, 2021, 2035, 2047]) == 4272
    assert candidate(nums = [1610, 1619, 1643, 1657, 1679]) == 3504
    assert candidate(nums = [110, 132, 154, 176, 198]) == 0
    assert candidate(nums = [913, 943, 979, 1009, 1037]) == 4212
    assert candidate(nums = [700, 715, 729, 741, 756, 765, 777, 784, 792, 805, 819, 828, 832, 840, 855]) == 0
    assert candidate(nums = [330, 351, 372, 393, 414]) == 528
    assert candidate(nums = [855, 876, 897, 918, 939]) == 1256
    assert candidate(nums = [1155, 1365, 1785, 1995, 2310, 2730, 3003, 3276, 3570]) == 0
    assert candidate(nums = [900, 910, 924, 936, 945, 966, 975, 990, 1001, 1008, 1014, 1029, 1035, 1053, 1056, 1065]) == 0
    assert candidate(nums = [561, 609, 657, 703, 759]) == 760
    assert candidate(nums = [1430, 1441, 1451, 1463, 1481]) == 1584
    assert candidate(nums = [100, 121, 143, 169, 180]) == 168
    assert candidate(nums = [1541, 1547, 1561, 1577, 1589]) == 6928
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 0
    assert candidate(nums = [1925, 1931, 1943, 1946, 1957]) == 4120
    assert candidate(nums = [1729, 1739, 1751, 1763, 1771]) == 5544
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0
    assert candidate(nums = [143, 221, 247, 299, 323]) == 1396
    assert candidate(nums = [1905, 1926, 1947, 1968, 1989]) == 0
    assert candidate(nums = [600, 625, 648, 675, 700, 729, 756, 784, 810, 841, 864, 891]) == 0
    assert candidate(nums = [667, 713, 779, 817, 851]) == 4120
    assert candidate(nums = [65537, 65539, 65543, 65551, 65561, 65579, 65591, 65597]) == 208140
    assert candidate(nums = [645, 666, 687, 708, 729]) == 920
    assert candidate(nums = [105, 126, 147, 168, 189]) == 0
    assert candidate(nums = [1386, 1452, 1518, 1584, 1650]) == 0
    assert candidate(nums = [903, 913, 924, 931, 943]) == 2016
    assert candidate(nums = [841, 961, 1089, 1225, 1369]) == 0
    assert candidate(nums = [609, 621, 637, 651, 671]) == 744
    assert candidate(nums = [121, 125, 143, 147, 169, 175, 182, 189, 196, 209, 221, 225, 245, 253, 265, 275, 287, 299]) == 2100
    assert candidate(nums = [1695, 1716, 1737, 1758, 1779]) == 2376
    assert candidate(nums = [1590, 1611, 1632, 1653, 1674]) == 0
    assert candidate(nums = [496, 672, 728, 840, 924]) == 0
    assert candidate(nums = [121, 144, 169, 196, 225]) == 0
    assert candidate(nums = [1105, 1365, 1615, 1885, 2145, 2415, 2685, 2955, 3225, 3495, 3765]) == 0
    assert candidate(nums = [506, 518, 529, 539, 551]) == 600
    assert candidate(nums = [1331, 1369, 1406, 1444, 1482, 1521, 1562, 1600, 1640, 1681, 1722, 1764]) == 1464
    assert candidate(nums = [406, 429, 455, 462, 494, 518, 546]) == 0
    assert candidate(nums = [45, 60, 77, 84, 91, 99, 100]) == 208
    assert candidate(nums = [325, 351, 375, 399, 425]) == 0
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 458
    assert candidate(nums = [2010, 2031, 2052, 2073, 2094]) == 5480
    assert candidate(nums = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]) == 686
    assert candidate(nums = [1001, 1007, 1029, 1045, 1067]) == 2256
    assert candidate(nums = [805, 819, 836, 851, 869]) == 1872
    assert candidate(nums = [1221, 1235, 1241, 1254, 1265]) == 1332
    assert candidate(nums = [750, 771, 792, 813, 834]) == 2120
    assert candidate(nums = [703, 707, 713, 725, 729, 735, 741, 745, 749, 759, 763, 779, 783, 799, 803, 805, 815, 825, 833, 835, 837, 841]) == 9572
    assert candidate(nums = [77, 110, 143, 176, 209]) == 504
    assert candidate(nums = [324, 325, 329, 333, 341, 343, 345, 351, 357, 361, 363, 371, 375, 385, 387, 399, 405, 425, 427, 429, 441, 451]) == 2600
    assert candidate(nums = [1021, 1031, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]) == 0
    assert candidate(nums = [391, 437, 493, 529, 551]) == 2052
    assert candidate(nums = [231, 255, 273, 297, 315, 333, 351]) == 0


