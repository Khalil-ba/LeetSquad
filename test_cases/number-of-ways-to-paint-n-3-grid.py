def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 246: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 650420578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 650420578: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 905790447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 905790447: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 80958521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 80958521: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 1122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 1122: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == 134620719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == 134620719: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 30228214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 30228214: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 350959293
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 350959293: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 151149117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 151149117: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 10107954
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 10107954: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5118: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000) == 685933196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000) == 685933196: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 210323922
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 210323922: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 897054912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 897054912: {e}')
    
    total += 1
    try:
        result = candidate(n = 3750) == 477003884
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3750) == 477003884: {e}')
    
    total += 1
    try:
        result = candidate(n = 3500) == 28484708
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3500) == 28484708: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 313837042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 313837042: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 462032897
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 462032897: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 62485141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 62485141: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 779575021
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 779575021: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 485778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 485778: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 601916395
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 601916395: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 672393158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 672393158: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 554911778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 554911778: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 690883140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 690883140: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 46107966
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 46107966: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 963045241
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 963045241: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 693684710
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 693684710: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 18988659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 18988659: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 493513580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 493513580: {e}')
    
    total += 1
    try:
        result = candidate(n = 4500) == 471193061
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4500) == 471193061: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 23346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 23346: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 106494
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 106494: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 676744457
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 676744457: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 814277332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 814277332: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 246
    assert candidate(n = 1000) == 650420578
    assert candidate(n = 100) == 905790447
    assert candidate(n = 2500) == 80958521
    assert candidate(n = 4) == 1122
    assert candidate(n = 4999) == 134620719
    assert candidate(n = 5000) == 30228214
    assert candidate(n = 2) == 54
    assert candidate(n = 1) == 12
    assert candidate(n = 500) == 350959293
    assert candidate(n = 50) == 151149117
    assert candidate(n = 10) == 10107954
    assert candidate(n = 5) == 5118
    assert candidate(n = 4000) == 685933196
    assert candidate(n = 12) == 210323922
    assert candidate(n = 2000) == 897054912
    assert candidate(n = 3750) == 477003884
    assert candidate(n = 3500) == 28484708
    assert candidate(n = 3000) == 313837042
    assert candidate(n = 30) == 462032897
    assert candidate(n = 16) == 62485141
    assert candidate(n = 10000) == 779575021
    assert candidate(n = 8) == 485778
    assert candidate(n = 250) == 601916395
    assert candidate(n = 999) == 672393158
    assert candidate(n = 32) == 554911778
    assert candidate(n = 20) == 690883140
    assert candidate(n = 11) == 46107966
    assert candidate(n = 15) == 963045241
    assert candidate(n = 200) == 693684710
    assert candidate(n = 1234) == 18988659
    assert candidate(n = 750) == 493513580
    assert candidate(n = 4500) == 471193061
    assert candidate(n = 6) == 23346
    assert candidate(n = 7) == 106494
    assert candidate(n = 25) == 676744457
    assert candidate(n = 1500) == 814277332


