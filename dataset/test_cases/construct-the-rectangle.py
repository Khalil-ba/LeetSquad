def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(area = 81) == [9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 81) == [9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(area = 122122) == [427, 286]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 122122) == [427, 286]: {e}')
    
    total += 1
    try:
        result = candidate(area = 37) == [37, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 37) == [37, 1]: {e}')
    
    total += 1
    try:
        result = candidate(area = 10000000) == [3200, 3125]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 10000000) == [3200, 3125]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(area = 4) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 4) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(area = 50) == [10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 50) == [10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(area = 10000) == [100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 10000) == [100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(area = 999999) == [1001, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 999999) == [1001, 999]: {e}')
    
    total += 1
    try:
        result = candidate(area = 60) == [10, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 60) == [10, 6]: {e}')
    
    total += 1
    try:
        result = candidate(area = 987654321) == [379721, 2601]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 987654321) == [379721, 2601]: {e}')
    
    total += 1
    try:
        result = candidate(area = 314159) == [314159, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 314159) == [314159, 1]: {e}')
    
    total += 1
    try:
        result = candidate(area = 9876543) == [14503, 681]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 9876543) == [14503, 681]: {e}')
    
    total += 1
    try:
        result = candidate(area = 7920) == [90, 88]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 7920) == [90, 88]: {e}')
    
    total += 1
    try:
        result = candidate(area = 131072) == [512, 256]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 131072) == [512, 256]: {e}')
    
    total += 1
    try:
        result = candidate(area = 87654321) == [14631, 5991]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 87654321) == [14631, 5991]: {e}')
    
    total += 1
    try:
        result = candidate(area = 841) == [29, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 841) == [29, 29]: {e}')
    
    total += 1
    try:
        result = candidate(area = 98765) == [19753, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 98765) == [19753, 5]: {e}')
    
    total += 1
    try:
        result = candidate(area = 625) == [25, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 625) == [25, 25]: {e}')
    
    total += 1
    try:
        result = candidate(area = 123456789) == [11409, 10821]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 123456789) == [11409, 10821]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1024) == [32, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1024) == [32, 32]: {e}')
    
    total += 1
    try:
        result = candidate(area = 8281) == [91, 91]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 8281) == [91, 91]: {e}')
    
    total += 1
    try:
        result = candidate(area = 86400) == [300, 288]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 86400) == [300, 288]: {e}')
    
    total += 1
    try:
        result = candidate(area = 12345678) == [14593, 846]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 12345678) == [14593, 846]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1000000000) == [32000, 31250]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1000000000) == [32000, 31250]: {e}')
    
    total += 1
    try:
        result = candidate(area = 12345) == [823, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 12345) == [823, 15]: {e}')
    
    total += 1
    try:
        result = candidate(area = 50000000) == [8000, 6250]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 50000000) == [8000, 6250]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1000000) == [1000, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1000000) == [1000, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(area = 100000000) == [10000, 10000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 100000000) == [10000, 10000]: {e}')
    
    total += 1
    try:
        result = candidate(area = 20000000) == [5000, 4000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 20000000) == [5000, 4000]: {e}')
    
    total += 1
    try:
        result = candidate(area = 8192) == [128, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 8192) == [128, 64]: {e}')
    
    total += 1
    try:
        result = candidate(area = 432432) == [693, 624]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 432432) == [693, 624]: {e}')
    
    total += 1
    try:
        result = candidate(area = 121) == [11, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 121) == [11, 11]: {e}')
    
    total += 1
    try:
        result = candidate(area = 333333) == [693, 481]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 333333) == [693, 481]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1048576) == [1024, 1024]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1048576) == [1024, 1024]: {e}')
    
    total += 1
    try:
        result = candidate(area = 54321) == [953, 57]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 54321) == [953, 57]: {e}')
    
    total += 1
    try:
        result = candidate(area = 250000) == [500, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 250000) == [500, 500]: {e}')
    
    total += 1
    try:
        result = candidate(area = 9801) == [99, 99]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 9801) == [99, 99]: {e}')
    
    total += 1
    try:
        result = candidate(area = 135895476) == [11324623, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 135895476) == [11324623, 12]: {e}')
    
    total += 1
    try:
        result = candidate(area = 2345678) == [50993, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 2345678) == [50993, 46]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1111111) == [4649, 239]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1111111) == [4649, 239]: {e}')
    
    total += 1
    try:
        result = candidate(area = 9999999) == [4649, 2151]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 9999999) == [4649, 2151]: {e}')
    
    total += 1
    try:
        result = candidate(area = 987654) == [1697, 582]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 987654) == [1697, 582]: {e}')
    
    total += 1
    try:
        result = candidate(area = 84100) == [290, 290]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 84100) == [290, 290]: {e}')
    
    total += 1
    try:
        result = candidate(area = 9999997) == [1428571, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 9999997) == [1428571, 7]: {e}')
    
    total += 1
    try:
        result = candidate(area = 500500) == [715, 700]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 500500) == [715, 700]: {e}')
    
    total += 1
    try:
        result = candidate(area = 9999991) == [9999991, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 9999991) == [9999991, 1]: {e}')
    
    total += 1
    try:
        result = candidate(area = 102400) == [320, 320]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 102400) == [320, 320]: {e}')
    
    total += 1
    try:
        result = candidate(area = 49) == [7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 49) == [7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(area = 7654321) == [402859, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 7654321) == [402859, 19]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1413721) == [1189, 1189]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1413721) == [1189, 1189]: {e}')
    
    total += 1
    try:
        result = candidate(area = 216000000) == [15000, 14400]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 216000000) == [15000, 14400]: {e}')
    
    total += 1
    try:
        result = candidate(area = 5000000) == [2500, 2000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 5000000) == [2500, 2000]: {e}')
    
    total += 1
    try:
        result = candidate(area = 123456) == [643, 192]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 123456) == [643, 192]: {e}')
    
    total += 1
    try:
        result = candidate(area = 9765625) == [3125, 3125]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 9765625) == [3125, 3125]: {e}')
    
    total += 1
    try:
        result = candidate(area = 100) == [10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 100) == [10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(area = 555555) == [777, 715]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 555555) == [777, 715]: {e}')
    
    total += 1
    try:
        result = candidate(area = 169) == [13, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 169) == [13, 13]: {e}')
    
    total += 1
    try:
        result = candidate(area = 100000001) == [5882353, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 100000001) == [5882353, 17]: {e}')
    
    total += 1
    try:
        result = candidate(area = 720) == [30, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 720) == [30, 24]: {e}')
    
    total += 1
    try:
        result = candidate(area = 2000000) == [1600, 1250]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 2000000) == [1600, 1250]: {e}')
    
    total += 1
    try:
        result = candidate(area = 67600) == [260, 260]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 67600) == [260, 260]: {e}')
    
    total += 1
    try:
        result = candidate(area = 676) == [26, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 676) == [26, 26]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1234567) == [9721, 127]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1234567) == [9721, 127]: {e}')
    
    total += 1
    try:
        result = candidate(area = 3199128) == [7841, 408]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 3199128) == [7841, 408]: {e}')
    
    total += 1
    try:
        result = candidate(area = 111111) == [407, 273]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 111111) == [407, 273]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1524157875) == [44019, 34625]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1524157875) == [44019, 34625]: {e}')
    
    total += 1
    try:
        result = candidate(area = 134217728) == [16384, 8192]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 134217728) == [16384, 8192]: {e}')
    
    total += 1
    try:
        result = candidate(area = 2048) == [64, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 2048) == [64, 32]: {e}')
    
    total += 1
    try:
        result = candidate(area = 65536) == [256, 256]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 65536) == [256, 256]: {e}')
    
    total += 1
    try:
        result = candidate(area = 789456123) == [41487, 19029]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 789456123) == [41487, 19029]: {e}')
    
    total += 1
    try:
        result = candidate(area = 567890123) == [28151, 20173]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 567890123) == [28151, 20173]: {e}')
    
    total += 1
    try:
        result = candidate(area = 73456) == [4591, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 73456) == [4591, 16]: {e}')
    
    total += 1
    try:
        result = candidate(area = 1000001) == [9901, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(area = 1000001) == [9901, 101]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(area = 81) == [9, 9]
    assert candidate(area = 122122) == [427, 286]
    assert candidate(area = 37) == [37, 1]
    assert candidate(area = 10000000) == [3200, 3125]
    assert candidate(area = 1) == [1, 1]
    assert candidate(area = 4) == [2, 2]
    assert candidate(area = 50) == [10, 5]
    assert candidate(area = 10000) == [100, 100]
    assert candidate(area = 999999) == [1001, 999]
    assert candidate(area = 60) == [10, 6]
    assert candidate(area = 987654321) == [379721, 2601]
    assert candidate(area = 314159) == [314159, 1]
    assert candidate(area = 9876543) == [14503, 681]
    assert candidate(area = 7920) == [90, 88]
    assert candidate(area = 131072) == [512, 256]
    assert candidate(area = 87654321) == [14631, 5991]
    assert candidate(area = 841) == [29, 29]
    assert candidate(area = 98765) == [19753, 5]
    assert candidate(area = 625) == [25, 25]
    assert candidate(area = 123456789) == [11409, 10821]
    assert candidate(area = 1024) == [32, 32]
    assert candidate(area = 8281) == [91, 91]
    assert candidate(area = 86400) == [300, 288]
    assert candidate(area = 12345678) == [14593, 846]
    assert candidate(area = 1000000000) == [32000, 31250]
    assert candidate(area = 12345) == [823, 15]
    assert candidate(area = 50000000) == [8000, 6250]
    assert candidate(area = 1000000) == [1000, 1000]
    assert candidate(area = 100000000) == [10000, 10000]
    assert candidate(area = 20000000) == [5000, 4000]
    assert candidate(area = 8192) == [128, 64]
    assert candidate(area = 432432) == [693, 624]
    assert candidate(area = 121) == [11, 11]
    assert candidate(area = 333333) == [693, 481]
    assert candidate(area = 1048576) == [1024, 1024]
    assert candidate(area = 54321) == [953, 57]
    assert candidate(area = 250000) == [500, 500]
    assert candidate(area = 9801) == [99, 99]
    assert candidate(area = 135895476) == [11324623, 12]
    assert candidate(area = 2345678) == [50993, 46]
    assert candidate(area = 1111111) == [4649, 239]
    assert candidate(area = 9999999) == [4649, 2151]
    assert candidate(area = 987654) == [1697, 582]
    assert candidate(area = 84100) == [290, 290]
    assert candidate(area = 9999997) == [1428571, 7]
    assert candidate(area = 500500) == [715, 700]
    assert candidate(area = 9999991) == [9999991, 1]
    assert candidate(area = 102400) == [320, 320]
    assert candidate(area = 49) == [7, 7]
    assert candidate(area = 7654321) == [402859, 19]
    assert candidate(area = 1413721) == [1189, 1189]
    assert candidate(area = 216000000) == [15000, 14400]
    assert candidate(area = 5000000) == [2500, 2000]
    assert candidate(area = 123456) == [643, 192]
    assert candidate(area = 9765625) == [3125, 3125]
    assert candidate(area = 100) == [10, 10]
    assert candidate(area = 555555) == [777, 715]
    assert candidate(area = 169) == [13, 13]
    assert candidate(area = 100000001) == [5882353, 17]
    assert candidate(area = 720) == [30, 24]
    assert candidate(area = 2000000) == [1600, 1250]
    assert candidate(area = 67600) == [260, 260]
    assert candidate(area = 676) == [26, 26]
    assert candidate(area = 1234567) == [9721, 127]
    assert candidate(area = 3199128) == [7841, 408]
    assert candidate(area = 111111) == [407, 273]
    assert candidate(area = 1524157875) == [44019, 34625]
    assert candidate(area = 134217728) == [16384, 8192]
    assert candidate(area = 2048) == [64, 32]
    assert candidate(area = 65536) == [256, 256]
    assert candidate(area = 789456123) == [41487, 19029]
    assert candidate(area = 567890123) == [28151, 20173]
    assert candidate(area = 73456) == [4591, 16]
    assert candidate(area = 1000001) == [9901, 101]


