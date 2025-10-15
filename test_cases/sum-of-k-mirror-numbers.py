def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 2,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 8) == 638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 8) == 638: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 15) == 5818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 15) == 5818: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 6) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 6) == 21: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 9) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 9) == 158: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 8) == 1498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 8) == 1498: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 30) == 18627530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 30) == 18627530: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 10) == 1772
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 10) == 1772: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 10) == 3224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 10) == 3224: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 7) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 7) == 499: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 10) == 1940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 10) == 1940: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 10) == 509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 10) == 509: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 20) == 156242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 20) == 156242: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 15) == 233041
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 15) == 233041: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 12) == 1297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 12) == 1297: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 20) == 94182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 20) == 94182: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 5) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 5) == 136: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 15) == 20526195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 15) == 20526195: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 30) == 2609044274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 30) == 2609044274: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 17) == 20379000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 17) == 20379000: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 28) == 115121130305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 28) == 115121130305: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 25) == 6849225412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 25) == 6849225412: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 20) == 2863752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 20) == 2863752: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 28) == 7054305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 28) == 7054305: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 35) == 639048703165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 35) == 639048703165: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 15) == 3203
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 15) == 3203: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 20) == 1000828708
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 20) == 1000828708: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 15) == 6822448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 15) == 6822448: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 25) == 7009551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 25) == 7009551: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 25) == 1651182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 25) == 1651182: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 30) == 28888231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 30) == 28888231: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 25) == 20005383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 25) == 20005383: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 28) == 19806423
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 28) == 19806423: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 22) == 22726545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 22) == 22726545: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 29) == 16185088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 29) == 16185088: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 28) == 19101218022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 28) == 19101218022: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 27) == 11349704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 27) == 11349704: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 17) == 27727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 17) == 27727: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 15) == 4383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 15) == 4383: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 30) == 43401017264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 30) == 43401017264: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 28) == 721411086
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 28) == 721411086: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 28) == 44192979
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 28) == 44192979: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 20) == 12448815
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 20) == 12448815: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 25) == 7586042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 25) == 7586042: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 19) == 91104965
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 19) == 91104965: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 35) == 33584024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 35) == 33584024: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,n = 28) == 13750746
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,n = 28) == 13750746: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 28) == 759196316
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 28) == 759196316: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 25) == 38898160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 25) == 38898160: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 20) == 156389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 20) == 156389: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 30) == 155059889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 30) == 155059889: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 18) == 41058
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 18) == 41058: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 20) == 321578997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 20) == 321578997: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 25) == 3428700695
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 25) == 3428700695: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 30) == 66619574
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 30) == 66619574: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 18) == 41849
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 18) == 41849: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 30) == 241030621167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 30) == 241030621167: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 2,n = 1) == 1
    assert candidate(k = 5,n = 8) == 638
    assert candidate(k = 8,n = 15) == 5818
    assert candidate(k = 9,n = 5) == 15
    assert candidate(k = 9,n = 6) == 21
    assert candidate(k = 8,n = 9) == 158
    assert candidate(k = 4,n = 8) == 1498
    assert candidate(k = 9,n = 30) == 18627530
    assert candidate(k = 2,n = 10) == 1772
    assert candidate(k = 4,n = 10) == 3224
    assert candidate(k = 3,n = 7) == 499
    assert candidate(k = 5,n = 10) == 1940
    assert candidate(k = 9,n = 10) == 509
    assert candidate(k = 9,n = 20) == 156242
    assert candidate(k = 4,n = 15) == 233041
    assert candidate(k = 6,n = 12) == 1297
    assert candidate(k = 8,n = 20) == 94182
    assert candidate(k = 3,n = 5) == 136
    assert candidate(k = 5,n = 15) == 20526195
    assert candidate(k = 2,n = 5) == 25
    assert candidate(k = 2,n = 30) == 2609044274
    assert candidate(k = 7,n = 17) == 20379000
    assert candidate(k = 7,n = 28) == 115121130305
    assert candidate(k = 5,n = 25) == 6849225412
    assert candidate(k = 3,n = 20) == 2863752
    assert candidate(k = 8,n = 28) == 7054305
    assert candidate(k = 7,n = 35) == 639048703165
    assert candidate(k = 9,n = 15) == 3203
    assert candidate(k = 5,n = 20) == 1000828708
    assert candidate(k = 7,n = 15) == 6822448
    assert candidate(k = 6,n = 25) == 7009551
    assert candidate(k = 8,n = 25) == 1651182
    assert candidate(k = 6,n = 30) == 28888231
    assert candidate(k = 2,n = 25) == 20005383
    assert candidate(k = 6,n = 28) == 19806423
    assert candidate(k = 4,n = 22) == 22726545
    assert candidate(k = 9,n = 29) == 16185088
    assert candidate(k = 5,n = 28) == 19101218022
    assert candidate(k = 9,n = 27) == 11349704
    assert candidate(k = 8,n = 17) == 27727
    assert candidate(k = 6,n = 15) == 4383
    assert candidate(k = 5,n = 30) == 43401017264
    assert candidate(k = 4,n = 28) == 721411086
    assert candidate(k = 3,n = 28) == 44192979
    assert candidate(k = 4,n = 20) == 12448815
    assert candidate(k = 9,n = 25) == 7586042
    assert candidate(k = 7,n = 19) == 91104965
    assert candidate(k = 9,n = 35) == 33584024
    assert candidate(k = 9,n = 28) == 13750746
    assert candidate(k = 2,n = 28) == 759196316
    assert candidate(k = 4,n = 25) == 38898160
    assert candidate(k = 6,n = 20) == 156389
    assert candidate(k = 3,n = 30) == 155059889
    assert candidate(k = 8,n = 18) == 41058
    assert candidate(k = 7,n = 20) == 321578997
    assert candidate(k = 7,n = 25) == 3428700695
    assert candidate(k = 8,n = 30) == 66619574
    assert candidate(k = 6,n = 18) == 41849
    assert candidate(k = 7,n = 30) == 241030621167


