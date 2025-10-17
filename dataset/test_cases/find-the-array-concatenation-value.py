def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 14, 13, 8, 12]) == 673
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 14, 13, 8, 12]) == 673: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555]) == 334332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555]) == 334332: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 78, 90, 12, 34]) == 13536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 78, 90, 12, 34]) == 13536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 52, 2, 4]) == 596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 52, 2, 4]) == 596: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999]) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999]) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 5678, 9101]) == 12354779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 5678, 9101]) == 12354779: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789]) == 124245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789]) == 124245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999]) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999]) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 301200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 301200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 5432, 1234]) == 98766666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 5432, 1234]) == 98766666: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000]) == 30012000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000]) == 30012000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20]) == 1020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20]) == 1020: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333]) == 111555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333]) == 111555: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 112]) == 580002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 112]) == 580002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9999, 9998, 9997, 9996]) == 200019991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9999, 9998, 9997, 9996]) == 200019991: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101]) == 579890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101]) == 579890: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40]) == 3070
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40]) == 3070: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 1113885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 1113885: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 31111000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 31111000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 32775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 32775: {e}')
    
    total += 1
    try:
        result = candidate(nums = [54321, 67890, 12345, 98760, 43215]) == 12221254320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [54321, 67890, 12345, 98760, 43215]) == 12221254320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2404000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2404000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 102480707478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 102480707478: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 43210, 13579, 24680]) == 14197538259
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 43210, 13579, 24680]) == 14197538259: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 1011, 1213]) == 5793013
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 1011, 1213]) == 5793013: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55]) == 31152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55]) == 31152: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005]) == 3000330012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005]) == 3000330012: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5, 1000000000]) == 10000000001000000042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5, 1000000000]) == 10000000001000000042: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 11107000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 11107000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6]) == 678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6]) == 678: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021, 2223]) == 35929095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021, 2223]) == 35929095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 321098, 765432, 109876]) == 1308752875308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 321098, 765432, 109876]) == 1308752875308: {e}')
    
    total += 1
    try:
        result = candidate(nums = [55555, 44444, 33333, 22222, 11111]) == 9999966666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55555, 44444, 33333, 22222, 11111]) == 9999966666: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555, 555, 555, 555, 555, 555, 555, 555, 555, 555]) == 2777775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555, 555, 555, 555, 555, 555, 555, 555, 555, 555]) == 2777775: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 100135035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 100135035: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 1, 222, 33, 4444, 555]) == 10036232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 1, 222, 33, 4444, 555]) == 10036232: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == 55555555555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == 55555555555: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 16818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 16818: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 43210, 1111, 2222, 3333, 4444]) == 1430869999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 43210, 1111, 2222, 3333, 4444]) == 1430869999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 233896111620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 233896111620: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 22, 333, 4444, 55555, 66666, 777777, 8888888, 99999999]) == 1207188885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 22, 333, 4444, 55555, 66666, 777777, 8888888, 99999999]) == 1207188885: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 433316665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 433316665: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 12345, 67890, 12345, 67890, 12345, 67890, 12345]) == 16047172815
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 12345, 67890, 12345, 67890, 12345, 67890, 12345]) == 16047172815: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 9999, 999, 99, 9, 8888, 888, 88, 8, 7777, 777, 77, 7]) == 13208429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 9999, 999, 99, 9, 8888, 888, 88, 8, 7777, 777, 77, 7]) == 13208429: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 8, 7, 6, 5, 4, 3, 2]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 8, 7, 6, 5, 4, 3, 2]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 9999, 999, 99, 9]) == 10122116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 9999, 999, 99, 9]) == 10122116: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 333316665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 333316665: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021]) == 1368586266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021]) == 1368586266: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 112233445, 556677889, 998877665, 554433221, 110011223, 334455667, 778899110]) == 1780022446776676886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 112233445, 556677889, 998877665, 554433221, 110011223, 334455667, 778899110]) == 1780022446776676886: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555, 555, 555, 555, 555, 555, 555, 555]) == 2222220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555, 555, 555, 555, 555, 555, 555, 555]) == 2222220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 42510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 42510: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0]) == 333416665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0]) == 333416665: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5655: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 101010, 111111, 121212]) == 6833009997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 101010, 111111, 121212]) == 6833009997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 1, 10000, 1, 10000, 1, 10000]) == 2000020012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 1, 10000, 1, 10000, 1, 10000]) == 2000020012: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060]) == 606061515150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060]) == 606061515150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 40000, 30000, 20000, 10000, 10001, 20002, 30003, 40004, 50005]) == 15000150015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 40000, 30000, 20000, 10000, 10001, 20002, 30003, 40004, 50005]) == 15000150015: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 12, 345]) == 19134357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 12, 345]) == 19134357: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 10350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 10350: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104729, 209458, 314187, 418926, 523665, 628404, 733143, 837882, 942621]) == 1047303665715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104729, 209458, 314187, 418926, 523665, 628404, 733143, 837882, 942621]) == 1047303665715: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 5432, 1234, 8765, 4321]) == 153094320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 5432, 1234, 8765, 4321]) == 153094320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [777, 888, 999, 111, 222, 333, 444, 555, 666, 0, 1]) == 1350649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [777, 888, 999, 111, 222, 333, 444, 555, 666, 0, 1]) == 1350649: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 233896111620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 233896111620: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 34, 56, 78, 90, 87, 65, 43, 21]) == 18306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 34, 56, 78, 90, 87, 65, 43, 21]) == 18306: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 51111100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 51111100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 8047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 8047: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 22, 333, 4444, 55555, 66666, 777777, 8888888, 99999999, 1]) == 15639233341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 22, 333, 4444, 55555, 66666, 777777, 8888888, 99999999, 1]) == 15639233341: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 200, 30, 4, 500, 60, 7000, 800]) == 3015360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 200, 30, 4, 500, 60, 7000, 800]) == 3015360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2262: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 1]) == 33334166666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 1]) == 33334166666: {e}')
    
    total += 1
    try:
        result = candidate(nums = [505, 404, 303, 202, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 151845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [505, 404, 303, 202, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 151845: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 551550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 551550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 111138885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 111138885: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == 29999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == 29999997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1010, 1111, 2222]) == 8332007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1010, 1111, 2222]) == 8332007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 75570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 75570: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5655: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 5432, 1098, 7654, 3210, 98765, 43210, 12345, 67890]) == 2406225420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 5432, 1098, 7654, 3210, 98765, 43210, 12345, 67890]) == 2406225420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 11111, 22222, 33333, 44444]) == 9134699999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 11111, 22222, 33333, 44444]) == 9134699999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 112, 131, 141, 151]) == 1469535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 112, 131, 141, 151]) == 1469535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 1000, 100, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]) == 1010112245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 1000, 100, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]) == 1010112245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [54321, 67890, 11111, 22222, 33333, 44444, 55555]) == 13332355554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [54321, 67890, 11111, 22222, 33333, 44444, 55555]) == 13332355554: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 1234]) == 388862344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 1234]) == 388862344: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11111, 22222, 33333, 44444, 55555]) == 3333433332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11111, 22222, 33333, 44444, 55555]) == 3333433332: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333]) == 8334330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333]) == 8334330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11111, 2222, 333, 44, 5, 6, 77, 888, 9999, 111111]) == 11133679531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11111, 2222, 333, 44, 5, 6, 77, 888, 9999, 111111]) == 11133679531: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090, 101010]) == 1151531310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090, 101010]) == 1151531310: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104, 205, 306, 407, 508, 609, 710, 811, 912, 1013, 1114, 1215, 1316, 1417, 1518]) == 22109316
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104, 205, 306, 407, 508, 609, 710, 811, 912, 1013, 1114, 1215, 1316, 1417, 1518]) == 22109316: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 101112, 131415]) == 80235232527
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 101112, 131415]) == 80235232527: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == 49895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == 49895: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 499999999995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 499999999995: {e}')
    
    total += 1
    try:
        result = candidate(nums = [876, 543, 210, 987, 654, 321]) == 1630962
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [876, 543, 210, 987, 654, 321]) == 1630962: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 60075015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 60075015: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125]) == 2998531250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125]) == 2998531250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 496450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 496450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 200, 3000, 40000, 500000, 6000000]) == 606540000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 200, 3000, 40000, 500000, 6000000]) == 606540000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 14690533329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 14690533329: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 987654, 12345, 9876, 1234, 987, 123, 98, 12, 9]) == 22343210973
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 987654, 12345, 9876, 1234, 987, 123, 98, 12, 9]) == 22343210973: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 111138885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 111138885: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 411110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 411110000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 2428040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 2428040: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 9999, 999, 99, 9]) == 101110095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 9999, 999, 99, 9]) == 101110095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 240040000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 240040000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 2222, 3333, 4444, 5555, 4444, 3333, 2222, 1111]) == 111116665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 2222, 3333, 4444, 5555, 4444, 3333, 2222, 1111]) == 111116665: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]) == 12071388885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]) == 12071388885: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 9999, 8888, 7777]) == 570060664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 9999, 8888, 7777]) == 570060664: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 14, 13, 8, 12]) == 673
    assert candidate(nums = [1, 1, 1, 1]) == 22
    assert candidate(nums = [111, 222, 333, 444, 555]) == 334332
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 315
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 280
    assert candidate(nums = [9]) == 9
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [56, 78, 90, 12, 34]) == 13536
    assert candidate(nums = [7, 52, 2, 4]) == 596
    assert candidate(nums = [9999]) == 9999
    assert candidate(nums = [1234, 5678, 9101]) == 12354779
    assert candidate(nums = [1, 2, 3, 4, 5]) == 42
    assert candidate(nums = [123, 456, 789]) == 124245
    assert candidate(nums = [9, 99, 999, 9999]) == 199998
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 75
    assert candidate(nums = [100, 200, 300, 400, 500]) == 301200
    assert candidate(nums = [9876, 5432, 1234]) == 98766666
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000]) == 30012000
    assert candidate(nums = [10, 20]) == 1020
    assert candidate(nums = [111, 222, 333]) == 111555
    assert candidate(nums = [123, 456, 789, 101, 112]) == 580002
    assert candidate(nums = [1, 2, 3]) == 15
    assert candidate(nums = [10000]) == 10000
    assert candidate(nums = [10000, 9999, 9998, 9997, 9996]) == 200019991
    assert candidate(nums = [123, 456, 789, 101]) == 579890
    assert candidate(nums = [10, 20, 30, 40]) == 3070
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 1113885
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 31111000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 32775
    assert candidate(nums = [54321, 67890, 12345, 98760, 43215]) == 12221254320
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2404000
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 102480707478
    assert candidate(nums = [98765, 43210, 13579, 24680]) == 14197538259
    assert candidate(nums = [123, 456, 789, 1011, 1213]) == 5793013
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55]) == 31152
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 315
    assert candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005]) == 3000330012
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 1000000000]) == 10000000001000000042
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 11107000
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6]) == 678
    assert candidate(nums = [123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021, 2223]) == 35929095
    assert candidate(nums = [987654, 321098, 765432, 109876]) == 1308752875308
    assert candidate(nums = [55555, 44444, 33333, 22222, 11111]) == 9999966666
    assert candidate(nums = [555, 555, 555, 555, 555, 555, 555, 555, 555, 555]) == 2777775
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 100135035
    assert candidate(nums = [9999, 1, 222, 33, 4444, 555]) == 10036232
    assert candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == 55555555555
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 16818
    assert candidate(nums = [98765, 43210, 1111, 2222, 3333, 4444]) == 1430869999
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 233896111620
    assert candidate(nums = [1, 22, 333, 4444, 55555, 66666, 777777, 8888888, 99999999]) == 1207188885
    assert candidate(nums = [10000, 9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 433316665
    assert candidate(nums = [12345, 67890, 12345, 67890, 12345, 67890, 12345, 67890, 12345]) == 16047172815
    assert candidate(nums = [1, 10, 100, 1000, 10000, 9999, 999, 99, 9, 8888, 888, 88, 8, 7777, 777, 77, 7]) == 13208429
    assert candidate(nums = [1, 9, 8, 7, 6, 5, 4, 3, 2]) == 270
    assert candidate(nums = [1, 10, 100, 1000, 10000, 9999, 999, 99, 9]) == 10122116
    assert candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 333316665
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021]) == 1368586266
    assert candidate(nums = [123456789, 987654321, 112233445, 556677889, 998877665, 554433221, 110011223, 334455667, 778899110]) == 1780022446776676886
    assert candidate(nums = [555, 555, 555, 555, 555, 555, 555, 555]) == 2222220
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 42510
    assert candidate(nums = [10000, 9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0]) == 333416665
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5655
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 101010, 111111, 121212]) == 6833009997
    assert candidate(nums = [10000, 1, 10000, 1, 10000, 1, 10000]) == 2000020012
    assert candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060]) == 606061515150
    assert candidate(nums = [50000, 40000, 30000, 20000, 10000, 10001, 20002, 30003, 40004, 50005]) == 15000150015
    assert candidate(nums = [12345, 67890, 12, 345]) == 19134357
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 10350
    assert candidate(nums = [104729, 209458, 314187, 418926, 523665, 628404, 733143, 837882, 942621]) == 1047303665715
    assert candidate(nums = [9876, 5432, 1234, 8765, 4321]) == 153094320
    assert candidate(nums = [777, 888, 999, 111, 222, 333, 444, 555, 666, 0, 1]) == 1350649
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 233896111620
    assert candidate(nums = [12, 34, 56, 78, 90, 87, 65, 43, 21]) == 18306
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 51111100000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 8047
    assert candidate(nums = [1, 22, 333, 4444, 55555, 66666, 777777, 8888888, 99999999, 1]) == 15639233341
    assert candidate(nums = [1000, 200, 30, 4, 500, 60, 7000, 800]) == 3015360
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2262
    assert candidate(nums = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 1]) == 33334166666
    assert candidate(nums = [505, 404, 303, 202, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 151845
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 551550
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 111138885
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == 29999997
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 360
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1010, 1111, 2222]) == 8332007
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 75570
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5655
    assert candidate(nums = [9876, 5432, 1098, 7654, 3210, 98765, 43210, 12345, 67890]) == 2406225420
    assert candidate(nums = [12345, 67890, 11111, 22222, 33333, 44444]) == 9134699999
    assert candidate(nums = [123, 456, 789, 101, 112, 131, 141, 151]) == 1469535
    assert candidate(nums = [10000, 1000, 100, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]) == 1010112245
    assert candidate(nums = [54321, 67890, 11111, 22222, 33333, 44444, 55555]) == 13332355554
    assert candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 1234]) == 388862344
    assert candidate(nums = [11111, 22222, 33333, 44444, 55555]) == 3333433332
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333]) == 8334330
    assert candidate(nums = [11111, 2222, 333, 44, 5, 6, 77, 888, 9999, 111111]) == 11133679531
    assert candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090, 101010]) == 1151531310
    assert candidate(nums = [104, 205, 306, 407, 508, 609, 710, 811, 912, 1013, 1114, 1215, 1316, 1417, 1518]) == 22109316
    assert candidate(nums = [12345, 67890, 101112, 131415]) == 80235232527
    assert candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == 49895
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 499999999995
    assert candidate(nums = [876, 543, 210, 987, 654, 321]) == 1630962
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 60075015
    assert candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125]) == 2998531250
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 496450
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 275
    assert candidate(nums = [10, 200, 3000, 40000, 500000, 6000000]) == 606540000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 110
    assert candidate(nums = [12345, 67890, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 14690533329
    assert candidate(nums = [987654321, 123456789, 987654, 12345, 9876, 1234, 987, 123, 98, 12, 9]) == 22343210973
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 360
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 111138885
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 411110000
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 2428040
    assert candidate(nums = [9, 99, 999, 9999, 99999, 9999, 999, 99, 9]) == 101110095
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 240040000
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 4444, 3333, 2222, 1111]) == 111116665
    assert candidate(nums = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]) == 12071388885
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 9999, 8888, 7777]) == 570060664


