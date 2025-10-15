def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,goal = 5,k = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,goal = 5,k = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,goal = 4,k = 1) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,goal = 4,k = 1) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,goal = 6,k = 2) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,goal = 6,k = 2) == 168: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,goal = 3,k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,goal = 3,k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,goal = 3,k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,goal = 3,k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,goal = 10,k = 5) == 3628800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,goal = 10,k = 5) == 3628800: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,goal = 10,k = 0) == 3628800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,goal = 10,k = 0) == 3628800: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,goal = 100,k = 99) == 437918130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,goal = 100,k = 99) == 437918130: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,goal = 8,k = 3) == 50400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,goal = 8,k = 3) == 50400: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,goal = 6,k = 3) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,goal = 6,k = 3) == 720: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,goal = 5,k = 2) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,goal = 5,k = 2) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,goal = 3,k = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,goal = 3,k = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,goal = 15,k = 5) == 314718922
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,goal = 15,k = 5) == 314718922: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,goal = 5,k = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,goal = 5,k = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,goal = 6,k = 2) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,goal = 6,k = 2) == 720: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,goal = 1,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,goal = 1,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,goal = 80,k = 15) == 735857219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,goal = 80,k = 15) == 735857219: {e}')
    
    total += 1
    try:
        result = candidate(n = 95,goal = 100,k = 50) == 174977625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95,goal = 100,k = 50) == 174977625: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,goal = 100,k = 40) == 538034361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,goal = 100,k = 40) == 538034361: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,goal = 20,k = 2) == 930652117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,goal = 20,k = 2) == 930652117: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,goal = 100,k = 40) == 871833725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,goal = 100,k = 40) == 871833725: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 50,k = 10) == 865239591
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 50,k = 10) == 865239591: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 75,k = 25) == 937903747
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 75,k = 25) == 937903747: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,goal = 70,k = 30) == 540386145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,goal = 70,k = 30) == 540386145: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,goal = 10,k = 2) == 115920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,goal = 10,k = 2) == 115920: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,goal = 9,k = 1) == 762
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,goal = 9,k = 1) == 762: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,goal = 12,k = 0) == 953029440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,goal = 12,k = 0) == 953029440: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,goal = 6,k = 1) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,goal = 6,k = 1) == 600: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,goal = 35,k = 12) == 371031271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,goal = 35,k = 12) == 371031271: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,goal = 100,k = 60) == 978677402
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,goal = 100,k = 60) == 978677402: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,goal = 15,k = 2) == 98280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,goal = 15,k = 2) == 98280: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 40,k = 10) == 300617761
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 40,k = 10) == 300617761: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,goal = 100,k = 80) == 515779794
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,goal = 100,k = 80) == 515779794: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 75,k = 20) == 512461610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 75,k = 20) == 512461610: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,goal = 16,k = 4) == 655720152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,goal = 16,k = 4) == 655720152: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,goal = 25,k = 10) == 708676825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,goal = 25,k = 10) == 708676825: {e}')
    
    total += 1
    try:
        result = candidate(n = 55,goal = 75,k = 25) == 829204517
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55,goal = 75,k = 25) == 829204517: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 100,k = 25) == 238440403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 100,k = 25) == 238440403: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,goal = 50,k = 10) == 681866396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,goal = 50,k = 10) == 681866396: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 50,k = 25) == 318608048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 50,k = 25) == 318608048: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,goal = 25,k = 7) == 357904575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,goal = 25,k = 7) == 357904575: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,goal = 15,k = 4) == 876639965
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,goal = 15,k = 4) == 876639965: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,goal = 80,k = 40) == 172533607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,goal = 80,k = 40) == 172533607: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 50,k = 30) == 292538678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 50,k = 30) == 292538678: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,goal = 80,k = 40) == 183945178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,goal = 80,k = 40) == 183945178: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 40,k = 5) == 922217496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 40,k = 5) == 922217496: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 100,k = 35) == 953525405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 100,k = 35) == 953525405: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,goal = 100,k = 50) == 65098072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,goal = 100,k = 50) == 65098072: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,goal = 15,k = 3) == 694588868
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,goal = 15,k = 3) == 694588868: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,goal = 90,k = 50) == 237760215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,goal = 90,k = 50) == 237760215: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,goal = 50,k = 10) == 429087363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,goal = 50,k = 10) == 429087363: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,goal = 50,k = 5) == 198199125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,goal = 50,k = 5) == 198199125: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 100,k = 45) == 838158734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 100,k = 45) == 838158734: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 60,k = 10) == 228726453
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 60,k = 10) == 228726453: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 100,k = 1) == 80478639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 100,k = 1) == 80478639: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,goal = 80,k = 30) == 601847758
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,goal = 80,k = 30) == 601847758: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,goal = 5,k = 1) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,goal = 5,k = 1) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 50,k = 10) == 198995152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 50,k = 10) == 198995152: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 45,k = 15) == 496260317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 45,k = 15) == 496260317: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,goal = 12,k = 1) == 904614480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,goal = 12,k = 1) == 904614480: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,goal = 20,k = 10) == 146326063
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,goal = 20,k = 10) == 146326063: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,goal = 20,k = 3) == 7864200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,goal = 20,k = 3) == 7864200: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,goal = 10,k = 1) == 1530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,goal = 10,k = 1) == 1530: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,goal = 30,k = 10) == 681973277
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,goal = 30,k = 10) == 681973277: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,goal = 30,k = 5) == 252498779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,goal = 30,k = 5) == 252498779: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,goal = 100,k = 70) == 614582964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,goal = 100,k = 70) == 614582964: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,goal = 20,k = 5) == 993942190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,goal = 20,k = 5) == 993942190: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,goal = 50,k = 15) == 325370660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,goal = 50,k = 15) == 325370660: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 50,k = 20) == 73692427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 50,k = 20) == 73692427: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 70,k = 25) == 598060511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 70,k = 25) == 598060511: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 100,k = 30) == 226791857
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 100,k = 30) == 226791857: {e}')
    
    total += 1
    try:
        result = candidate(n = 65,goal = 80,k = 35) == 757952334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65,goal = 80,k = 35) == 757952334: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,goal = 40,k = 15) == 504044110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,goal = 40,k = 15) == 504044110: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 40,k = 15) == 213845140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 40,k = 15) == 213845140: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 60,k = 20) == 611199752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 60,k = 20) == 611199752: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 50,k = 15) == 745316193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 50,k = 15) == 745316193: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,goal = 60,k = 10) == 447565182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,goal = 60,k = 10) == 447565182: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,goal = 60,k = 25) == 422620880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,goal = 60,k = 25) == 422620880: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,goal = 90,k = 40) == 803255223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,goal = 90,k = 40) == 803255223: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,goal = 30,k = 5) == 557163012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,goal = 30,k = 5) == 557163012: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,goal = 10,k = 3) == 1764000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,goal = 10,k = 3) == 1764000: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,goal = 90,k = 15) == 707675175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,goal = 90,k = 15) == 707675175: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,goal = 75,k = 30) == 167112607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,goal = 75,k = 30) == 167112607: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,goal = 15,k = 3) == 81965019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,goal = 15,k = 3) == 81965019: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,goal = 12,k = 2) == 24555600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,goal = 12,k = 2) == 24555600: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 60,k = 20) == 833839566
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 60,k = 20) == 833839566: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,goal = 25,k = 4) == 754974000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,goal = 25,k = 4) == 754974000: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,goal = 80,k = 25) == 764575926
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,goal = 80,k = 25) == 764575926: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,goal = 5,k = 2) == 120
    assert candidate(n = 3,goal = 4,k = 1) == 18
    assert candidate(n = 4,goal = 6,k = 2) == 168
    assert candidate(n = 3,goal = 3,k = 1) == 6
    assert candidate(n = 2,goal = 3,k = 1) == 2
    assert candidate(n = 10,goal = 10,k = 5) == 3628800
    assert candidate(n = 10,goal = 10,k = 0) == 3628800
    assert candidate(n = 100,goal = 100,k = 99) == 437918130
    assert candidate(n = 7,goal = 8,k = 3) == 50400
    assert candidate(n = 6,goal = 6,k = 3) == 720
    assert candidate(n = 4,goal = 5,k = 2) == 72
    assert candidate(n = 2,goal = 3,k = 0) == 6
    assert candidate(n = 10,goal = 15,k = 5) == 314718922
    assert candidate(n = 5,goal = 5,k = 0) == 120
    assert candidate(n = 5,goal = 6,k = 2) == 720
    assert candidate(n = 1,goal = 1,k = 0) == 1
    assert candidate(n = 60,goal = 80,k = 15) == 735857219
    assert candidate(n = 95,goal = 100,k = 50) == 174977625
    assert candidate(n = 70,goal = 100,k = 40) == 538034361
    assert candidate(n = 8,goal = 20,k = 2) == 930652117
    assert candidate(n = 80,goal = 100,k = 40) == 871833725
    assert candidate(n = 40,goal = 50,k = 10) == 865239591
    assert candidate(n = 50,goal = 75,k = 25) == 937903747
    assert candidate(n = 60,goal = 70,k = 30) == 540386145
    assert candidate(n = 5,goal = 10,k = 2) == 115920
    assert candidate(n = 3,goal = 9,k = 1) == 762
    assert candidate(n = 6,goal = 12,k = 0) == 953029440
    assert candidate(n = 4,goal = 6,k = 1) == 600
    assert candidate(n = 25,goal = 35,k = 12) == 371031271
    assert candidate(n = 80,goal = 100,k = 60) == 978677402
    assert candidate(n = 4,goal = 15,k = 2) == 98280
    assert candidate(n = 30,goal = 40,k = 10) == 300617761
    assert candidate(n = 90,goal = 100,k = 80) == 515779794
    assert candidate(n = 50,goal = 75,k = 20) == 512461610
    assert candidate(n = 8,goal = 16,k = 4) == 655720152
    assert candidate(n = 20,goal = 25,k = 10) == 708676825
    assert candidate(n = 55,goal = 75,k = 25) == 829204517
    assert candidate(n = 30,goal = 100,k = 25) == 238440403
    assert candidate(n = 35,goal = 50,k = 10) == 681866396
    assert candidate(n = 50,goal = 50,k = 25) == 318608048
    assert candidate(n = 15,goal = 25,k = 7) == 357904575
    assert candidate(n = 8,goal = 15,k = 4) == 876639965
    assert candidate(n = 70,goal = 80,k = 40) == 172533607
    assert candidate(n = 40,goal = 50,k = 30) == 292538678
    assert candidate(n = 60,goal = 80,k = 40) == 183945178
    assert candidate(n = 30,goal = 40,k = 5) == 922217496
    assert candidate(n = 40,goal = 100,k = 35) == 953525405
    assert candidate(n = 70,goal = 100,k = 50) == 65098072
    assert candidate(n = 10,goal = 15,k = 3) == 694588868
    assert candidate(n = 80,goal = 90,k = 50) == 237760215
    assert candidate(n = 25,goal = 50,k = 10) == 429087363
    assert candidate(n = 35,goal = 50,k = 5) == 198199125
    assert candidate(n = 50,goal = 100,k = 45) == 838158734
    assert candidate(n = 40,goal = 60,k = 10) == 228726453
    assert candidate(n = 50,goal = 100,k = 1) == 80478639
    assert candidate(n = 60,goal = 80,k = 30) == 601847758
    assert candidate(n = 3,goal = 5,k = 1) == 42
    assert candidate(n = 30,goal = 50,k = 10) == 198995152
    assert candidate(n = 40,goal = 45,k = 15) == 496260317
    assert candidate(n = 7,goal = 12,k = 1) == 904614480
    assert candidate(n = 20,goal = 20,k = 10) == 146326063
    assert candidate(n = 5,goal = 20,k = 3) == 7864200
    assert candidate(n = 3,goal = 10,k = 1) == 1530
    assert candidate(n = 20,goal = 30,k = 10) == 681973277
    assert candidate(n = 20,goal = 30,k = 5) == 252498779
    assert candidate(n = 90,goal = 100,k = 70) == 614582964
    assert candidate(n = 10,goal = 20,k = 5) == 993942190
    assert candidate(n = 25,goal = 50,k = 15) == 325370660
    assert candidate(n = 40,goal = 50,k = 20) == 73692427
    assert candidate(n = 50,goal = 70,k = 25) == 598060511
    assert candidate(n = 50,goal = 100,k = 30) == 226791857
    assert candidate(n = 65,goal = 80,k = 35) == 757952334
    assert candidate(n = 20,goal = 40,k = 15) == 504044110
    assert candidate(n = 30,goal = 40,k = 15) == 213845140
    assert candidate(n = 30,goal = 60,k = 20) == 611199752
    assert candidate(n = 30,goal = 50,k = 15) == 745316193
    assert candidate(n = 45,goal = 60,k = 10) == 447565182
    assert candidate(n = 45,goal = 60,k = 25) == 422620880
    assert candidate(n = 80,goal = 90,k = 40) == 803255223
    assert candidate(n = 7,goal = 30,k = 5) == 557163012
    assert candidate(n = 7,goal = 10,k = 3) == 1764000
    assert candidate(n = 30,goal = 90,k = 15) == 707675175
    assert candidate(n = 50,goal = 75,k = 30) == 167112607
    assert candidate(n = 7,goal = 15,k = 3) == 81965019
    assert candidate(n = 6,goal = 12,k = 2) == 24555600
    assert candidate(n = 40,goal = 60,k = 20) == 833839566
    assert candidate(n = 6,goal = 25,k = 4) == 754974000
    assert candidate(n = 40,goal = 80,k = 25) == 764575926


