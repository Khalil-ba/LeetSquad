def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 2,n = 4) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 4) == 162: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3) == 1122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3) == 1122: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1) == 48: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5) == 580986
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5) == 580986: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 4) == 1122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 4) == 1122: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 2) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 2) == 162: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3) == 246: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 3) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 3) == 54: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 800) == 253729951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 800) == 253729951: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4) == 7812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4) == 7812: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 800) == 351341125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 800) == 351341125: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 500) == 859596253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 500) == 859596253: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 250) == 385854418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 250) == 385854418: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1000) == 32634808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1000) == 32634808: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 350) == 47085356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 350) == 47085356: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 10) == 10107954
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 10) == 10107954: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 500) == 614795573
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 500) == 614795573: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5) == 48: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 500) == 85724507
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 500) == 85724507: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 50) == 151149117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 50) == 151149117: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 600) == 643128638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 600) == 643128638: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 750) == 346928514
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 750) == 346928514: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 500) == 350959293
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 500) == 350959293: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 100) == 772083415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 100) == 772083415: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2) == 486
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2) == 486: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 900) == 360544652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 900) == 360544652: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 1000) == 281273229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 1000) == 281273229: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 998) == 16509421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 998) == 16509421: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 7) == 106494
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 7) == 106494: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 1000) == 650420578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 1000) == 650420578: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 50) == 597561939
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 50) == 597561939: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 100) == 80216004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 100) == 80216004: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 10) == 896895828
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 10) == 896895828: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 999) == 772309689
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 999) == 772309689: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 6) == 379602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 6) == 379602: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 999) == 37925462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 999) == 37925462: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 100) == 714933866
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 100) == 714933866: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 600) == 138487123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 600) == 138487123: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 10) == 796884854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 10) == 796884854: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 800) == 314710698
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 800) == 314710698: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5) == 54450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5) == 54450: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 200) == 55054779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 200) == 55054779: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 750) == 493513580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 750) == 493513580: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 997) == 582030758
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 997) == 582030758: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 900) == 999754739
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 900) == 999754739: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 700) == 360760626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 700) == 360760626: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 300) == 194398079
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 300) == 194398079: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 9) == 128643282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 9) == 128643282: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 1000) == 113776386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 1000) == 113776386: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 700) == 795691966
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 700) == 795691966: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 250) == 727847864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 250) == 727847864: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3) == 5118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3) == 5118: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 800) == 197304781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 800) == 197304781: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 300) == 748221310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 300) == 748221310: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1000) == 408208448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1000) == 408208448: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 20) == 690883140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 20) == 690883140: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5) == 486
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5) == 486: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 2,n = 4) == 162
    assert candidate(m = 4,n = 3) == 1122
    assert candidate(m = 5,n = 1) == 48
    assert candidate(m = 1,n = 2) == 6
    assert candidate(m = 5,n = 5) == 580986
    assert candidate(m = 3,n = 4) == 1122
    assert candidate(m = 1,n = 1) == 3
    assert candidate(m = 4,n = 2) == 162
    assert candidate(m = 3,n = 3) == 246
    assert candidate(m = 2,n = 3) == 54
    assert candidate(m = 5,n = 800) == 253729951
    assert candidate(m = 4,n = 4) == 7812
    assert candidate(m = 2,n = 800) == 351341125
    assert candidate(m = 5,n = 500) == 859596253
    assert candidate(m = 5,n = 250) == 385854418
    assert candidate(m = 1,n = 1000) == 32634808
    assert candidate(m = 4,n = 350) == 47085356
    assert candidate(m = 3,n = 10) == 10107954
    assert candidate(m = 4,n = 500) == 614795573
    assert candidate(m = 1,n = 5) == 48
    assert candidate(m = 1,n = 500) == 85724507
    assert candidate(m = 3,n = 50) == 151149117
    assert candidate(m = 4,n = 600) == 643128638
    assert candidate(m = 4,n = 750) == 346928514
    assert candidate(m = 3,n = 500) == 350959293
    assert candidate(m = 2,n = 100) == 772083415
    assert candidate(m = 5,n = 2) == 486
    assert candidate(m = 2,n = 900) == 360544652
    assert candidate(m = 2,n = 2) == 18
    assert candidate(m = 4,n = 1000) == 281273229
    assert candidate(m = 4,n = 998) == 16509421
    assert candidate(m = 3,n = 7) == 106494
    assert candidate(m = 3,n = 1000) == 650420578
    assert candidate(m = 5,n = 50) == 597561939
    assert candidate(m = 4,n = 100) == 80216004
    assert candidate(m = 4,n = 10) == 896895828
    assert candidate(m = 4,n = 999) == 772309689
    assert candidate(m = 4,n = 6) == 379602
    assert candidate(m = 2,n = 999) == 37925462
    assert candidate(m = 5,n = 100) == 714933866
    assert candidate(m = 2,n = 600) == 138487123
    assert candidate(m = 3,n = 1) == 12
    assert candidate(m = 5,n = 10) == 796884854
    assert candidate(m = 3,n = 800) == 314710698
    assert candidate(m = 4,n = 5) == 54450
    assert candidate(m = 5,n = 200) == 55054779
    assert candidate(m = 3,n = 750) == 493513580
    assert candidate(m = 5,n = 997) == 582030758
    assert candidate(m = 3,n = 900) == 999754739
    assert candidate(m = 3,n = 700) == 360760626
    assert candidate(m = 5,n = 300) == 194398079
    assert candidate(m = 4,n = 9) == 128643282
    assert candidate(m = 2,n = 1000) == 113776386
    assert candidate(m = 4,n = 700) == 795691966
    assert candidate(m = 4,n = 250) == 727847864
    assert candidate(m = 5,n = 3) == 5118
    assert candidate(m = 4,n = 800) == 197304781
    assert candidate(m = 3,n = 300) == 748221310
    assert candidate(m = 5,n = 1000) == 408208448
    assert candidate(m = 3,n = 20) == 690883140
    assert candidate(m = 2,n = 5) == 486


