def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 135) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135) == 110: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 738: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 162: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 5274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 5274: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 803
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 803: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 1242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 1242: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876) == 5274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876) == 5274: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 2392084
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 2392084: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000) == 229050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000) == 229050: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000000) == 5974650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000000) == 5974650: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 234: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999) == 5974650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999) == 5974650: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 738: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222) == 2789370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222) == 2789370: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == 171: {e}')
    
    total += 1
    try:
        result = candidate(n = 102030405060708090) == 8877690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 102030405060708090) == 8877690: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 5611770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 5611770: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 5660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 5660: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999) == 712890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999) == 712890: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 6028170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 6028170: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111) == 34170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111) == 34170: {e}')
    
    total += 1
    try:
        result = candidate(n = 111222333) == 2386170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111222333) == 2386170: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 213456789) == 2754964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 213456789) == 2754964: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 168570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 168570: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210) == 5202657
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210) == 5202657: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000) == 47610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000) == 47610: {e}')
    
    total += 1
    try:
        result = candidate(n = 2100000000) == 6014970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2100000000) == 6014970: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 2345850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 2345850: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000) == 2708730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000) == 2708730: {e}')
    
    total += 1
    try:
        result = candidate(n = 12344321) == 735990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12344321) == 735990: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210) == 8877690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210) == 8877690: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987) == 3975354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987) == 3975354: {e}')
    
    total += 1
    try:
        result = candidate(n = 1122334455) == 5652090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1122334455) == 5652090: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 5274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 5274: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555) == 3998970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555) == 3998970: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111) == 175290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111) == 175290: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 5611770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 5611770: {e}')
    
    total += 1
    try:
        result = candidate(n = 88888) == 29130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888) == 29130: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 5611770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 5611770: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 2386170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 2386170: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 5611770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 5611770: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 5208570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 5208570: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890) == 5658004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890) == 5658004: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123) == 4028371
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123) == 4028371: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010) == 32490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010) == 32490: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654320) == 5611769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654320) == 5611769: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 32490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 32490: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 168570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 168570: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 168570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 168570: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 34417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 34417: {e}')
    
    total += 1
    try:
        result = candidate(n = 87654321) == 2141294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87654321) == 2141294: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == 5652090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == 5652090: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 135) == 110
    assert candidate(n = 999) == 738
    assert candidate(n = 200) == 162
    assert candidate(n = 10000) == 5274
    assert candidate(n = 1234) == 803
    assert candidate(n = 2000) == 1242
    assert candidate(n = 9876) == 5274
    assert candidate(n = 123456789) == 2392084
    assert candidate(n = 20) == 19
    assert candidate(n = 2000000) == 229050
    assert candidate(n = 2000000000) == 5974650
    assert candidate(n = 300) == 234
    assert candidate(n = 100) == 90
    assert candidate(n = 1999999999) == 5974650
    assert candidate(n = 1000) == 738
    assert candidate(n = 1) == 1
    assert candidate(n = 5) == 5
    assert candidate(n = 222222222) == 2789370
    assert candidate(n = 210) == 171
    assert candidate(n = 102030405060708090) == 8877690
    assert candidate(n = 999999999) == 5611770
    assert candidate(n = 12345) == 5660
    assert candidate(n = 9999999) == 712890
    assert candidate(n = 2147483647) == 6028170
    assert candidate(n = 111111) == 34170
    assert candidate(n = 111222333) == 2386170
    assert candidate(n = 111) == 98
    assert candidate(n = 213456789) == 2754964
    assert candidate(n = 987654) == 168570
    assert candidate(n = 876543210) == 5202657
    assert candidate(n = 200000) == 47610
    assert candidate(n = 2100000000) == 6014970
    assert candidate(n = 101010101) == 2345850
    assert candidate(n = 200000000) == 2708730
    assert candidate(n = 12344321) == 735990
    assert candidate(n = 9876543210) == 8877690
    assert candidate(n = 543210987) == 3975354
    assert candidate(n = 1122334455) == 5652090
    assert candidate(n = 9999) == 5274
    assert candidate(n = 555555555) == 3998970
    assert candidate(n = 1111111) == 175290
    assert candidate(n = 1000000000) == 5611770
    assert candidate(n = 88888) == 29130
    assert candidate(n = 1000000001) == 5611770
    assert candidate(n = 111111111) == 2386170
    assert candidate(n = 987654321) == 5611770
    assert candidate(n = 888888888) == 5208570
    assert candidate(n = 1234567890) == 5658004
    assert candidate(n = 567890123) == 4028371
    assert candidate(n = 101010) == 32490
    assert candidate(n = 987654320) == 5611769
    assert candidate(n = 98765) == 32490
    assert candidate(n = 1000000) == 168570
    assert candidate(n = 999999) == 168570
    assert candidate(n = 123456) == 34417
    assert candidate(n = 87654321) == 2141294
    assert candidate(n = 1111111111) == 5652090


