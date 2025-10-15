def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 16443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 16443: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 1650467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 1650467: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 161: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 329) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 329) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 344) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 344) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == 130: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890) == 11279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890) == 11279: {e}')
    
    total += 1
    try:
        result = candidate(n = 324) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 324) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 333) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 316) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 316) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 303) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 303) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 334) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 334) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 347) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 347) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 474: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123) == 1131581
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123) == 1131581: {e}')
    
    total += 1
    try:
        result = candidate(n = 4913) == 464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4913) == 464: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 53: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 1039682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 1039682: {e}')
    
    total += 1
    try:
        result = candidate(n = 313) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 313) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 317) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 317) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 3375) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3375) == 365: {e}')
    
    total += 1
    try:
        result = candidate(n = 897543210) == 1535456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897543210) == 1535456: {e}')
    
    total += 1
    try:
        result = candidate(n = 341) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 341) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 216) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 216) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 2210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 2210: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 16287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 16287: {e}')
    
    total += 1
    try:
        result = candidate(n = 314) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 314) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 318) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 318) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 3536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 3536: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 350) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000) == 48159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000) == 48159: {e}')
    
    total += 1
    try:
        result = candidate(n = 325) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 325) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 305) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 305) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 408968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 408968: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 16443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 16443: {e}')
    
    total += 1
    try:
        result = candidate(n = 308) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 308) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 12167) == 857
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12167) == 857: {e}')
    
    total += 1
    try:
        result = candidate(n = 342) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 342) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 666) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 315) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 315) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 1650467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 1650467: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 252: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000) == 654763
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000) == 654763: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 23456789) == 135151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23456789) == 135151: {e}')
    
    total += 1
    try:
        result = candidate(n = 345) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 336) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 336) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 9261) == 719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9261) == 719: {e}')
    
    total += 1
    try:
        result = candidate(n = 311) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 311) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 310) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 310) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 337) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 337) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 343) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 343) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 339) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 339) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 320) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 320) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 332) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 332) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 1636751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 1636751: {e}')
    
    total += 1
    try:
        result = candidate(n = 307) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 307) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 309) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 309) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 10365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 10365: {e}')
    
    total += 1
    try:
        result = candidate(n = 328) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 328) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 348) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 348) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 304) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 304) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 208: {e}')
    
    total += 1
    try:
        result = candidate(n = 2197) == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2197) == 272: {e}')
    
    total += 1
    try:
        result = candidate(n = 1331) == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1331) == 191: {e}')
    
    total += 1
    try:
        result = candidate(n = 319) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 319) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 39: {e}')
    
    total += 1
    try:
        result = candidate(n = 321) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 321) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 6859) == 586
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6859) == 586: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 323) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 323) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 331) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 331) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 327) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 327) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 349) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 349) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 756: {e}')
    
    total += 1
    try:
        result = candidate(n = 335) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 335) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 302) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 302) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 312) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 312) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 330) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 330) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 322) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 322) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 338) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 338) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 306) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 306) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 326) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 326) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 301) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 301) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 4068
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 4068: {e}')
    
    total += 1
    try:
        result = candidate(n = 346) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 346) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 340) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 340) == 76: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 6
    assert candidate(n = 3) == 3
    assert candidate(n = 100) == 34
    assert candidate(n = 15) == 9
    assert candidate(n = 4) == 3
    assert candidate(n = 1000000) == 16443
    assert candidate(n = 20) == 10
    assert candidate(n = 1) == 1
    assert candidate(n = 1000000000) == 1650467
    assert candidate(n = 1000) == 161
    assert candidate(n = 10) == 6
    assert candidate(n = 329) == 75
    assert candidate(n = 344) == 77
    assert candidate(n = 729) == 130
    assert candidate(n = 567890) == 11279
    assert candidate(n = 324) == 75
    assert candidate(n = 300) == 71
    assert candidate(n = 333) == 76
    assert candidate(n = 316) == 74
    assert candidate(n = 23) == 12
    assert candidate(n = 303) == 72
    assert candidate(n = 334) == 76
    assert candidate(n = 35) == 15
    assert candidate(n = 347) == 77
    assert candidate(n = 5000) == 474
    assert candidate(n = 567890123) == 1131581
    assert candidate(n = 4913) == 464
    assert candidate(n = 200) == 53
    assert candidate(n = 500000000) == 1039682
    assert candidate(n = 313) == 73
    assert candidate(n = 500) == 100
    assert candidate(n = 317) == 74
    assert candidate(n = 3375) == 365
    assert candidate(n = 897543210) == 1535456
    assert candidate(n = 341) == 76
    assert candidate(n = 216) == 55
    assert candidate(n = 50000) == 2210
    assert candidate(n = 987654) == 16287
    assert candidate(n = 314) == 73
    assert candidate(n = 318) == 74
    assert candidate(n = 100000) == 3536
    assert candidate(n = 25) == 13
    assert candidate(n = 350) == 77
    assert candidate(n = 5000000) == 48159
    assert candidate(n = 325) == 75
    assert candidate(n = 305) == 72
    assert candidate(n = 123456789) == 408968
    assert candidate(n = 999999) == 16443
    assert candidate(n = 308) == 73
    assert candidate(n = 12167) == 857
    assert candidate(n = 342) == 77
    assert candidate(n = 666) == 120
    assert candidate(n = 315) == 74
    assert candidate(n = 999999999) == 1650467
    assert candidate(n = 2000) == 252
    assert candidate(n = 250000000) == 654763
    assert candidate(n = 30) == 14
    assert candidate(n = 23456789) == 135151
    assert candidate(n = 345) == 77
    assert candidate(n = 336) == 76
    assert candidate(n = 9261) == 719
    assert candidate(n = 311) == 73
    assert candidate(n = 310) == 73
    assert candidate(n = 337) == 76
    assert candidate(n = 343) == 77
    assert candidate(n = 339) == 76
    assert candidate(n = 320) == 74
    assert candidate(n = 332) == 76
    assert candidate(n = 987654321) == 1636751
    assert candidate(n = 307) == 72
    assert candidate(n = 309) == 73
    assert candidate(n = 500000) == 10365
    assert candidate(n = 328) == 75
    assert candidate(n = 348) == 77
    assert candidate(n = 304) == 72
    assert candidate(n = 1500) == 208
    assert candidate(n = 2197) == 272
    assert candidate(n = 1331) == 191
    assert candidate(n = 319) == 74
    assert candidate(n = 125) == 39
    assert candidate(n = 321) == 74
    assert candidate(n = 6859) == 586
    assert candidate(n = 50) == 20
    assert candidate(n = 323) == 75
    assert candidate(n = 331) == 75
    assert candidate(n = 40) == 18
    assert candidate(n = 327) == 75
    assert candidate(n = 349) == 77
    assert candidate(n = 10000) == 756
    assert candidate(n = 335) == 76
    assert candidate(n = 302) == 72
    assert candidate(n = 312) == 73
    assert candidate(n = 330) == 75
    assert candidate(n = 322) == 74
    assert candidate(n = 338) == 76
    assert candidate(n = 306) == 72
    assert candidate(n = 326) == 75
    assert candidate(n = 301) == 71
    assert candidate(n = 123456) == 4068
    assert candidate(n = 346) == 77
    assert candidate(n = 340) == 76


