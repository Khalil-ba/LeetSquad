def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 7,maxValue = 7) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxValue = 7) == 106: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,maxValue = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,maxValue = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,maxValue = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,maxValue = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,maxValue = 6) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,maxValue = 6) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxValue = 12) == 327
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxValue = 12) == 327: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxValue = 5) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxValue = 5) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxValue = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxValue = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxValue = 10) == 571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxValue = 10) == 571: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxValue = 7) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxValue = 7) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,maxValue = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,maxValue = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,maxValue = 10000) == 22940607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,maxValue = 10000) == 22940607: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,maxValue = 10) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,maxValue = 10) == 89: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxValue = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxValue = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,maxValue = 10) == 347343994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,maxValue = 10) == 347343994: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,maxValue = 10) == 1431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,maxValue = 10) == 1431: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxValue = 20) == 1191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxValue = 20) == 1191: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,maxValue = 8000) == 106406983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,maxValue = 8000) == 106406983: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxValue = 16) == 1115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxValue = 16) == 1115: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,maxValue = 6000) == 883250062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,maxValue = 6000) == 883250062: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,maxValue = 5000) == 716352377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,maxValue = 5000) == 716352377: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,maxValue = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,maxValue = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,maxValue = 50) == 604383896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,maxValue = 50) == 604383896: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,maxValue = 4) == 502501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,maxValue = 4) == 502501: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,maxValue = 5) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,maxValue = 5) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,maxValue = 15) == 575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,maxValue = 15) == 575: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxValue = 20) == 3176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxValue = 20) == 3176: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,maxValue = 1000) == 534638579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,maxValue = 1000) == 534638579: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxValue = 15) == 1341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxValue = 15) == 1341: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,maxValue = 20) == 519126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,maxValue = 20) == 519126: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxValue = 3) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxValue = 3) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,maxValue = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,maxValue = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxValue = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxValue = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,maxValue = 3) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,maxValue = 3) == 201: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,maxValue = 5000) == 22892639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,maxValue = 5000) == 22892639: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999,maxValue = 10000) == 667133522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999,maxValue = 10000) == 667133522: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,maxValue = 3000) == 80648523
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,maxValue = 3000) == 80648523: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,maxValue = 3000) == 806624302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,maxValue = 3000) == 806624302: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,maxValue = 2000) == 585712681
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,maxValue = 2000) == 585712681: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,maxValue = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,maxValue = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,maxValue = 5) == 12517501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,maxValue = 5) == 12517501: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,maxValue = 2000) == 802769368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,maxValue = 2000) == 802769368: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,maxValue = 2000) == 228299266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,maxValue = 2000) == 228299266: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxValue = 20) == 1707
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxValue = 20) == 1707: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,maxValue = 25) == 1630451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,maxValue = 25) == 1630451: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,maxValue = 2) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,maxValue = 2) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxValue = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxValue = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,maxValue = 8) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,maxValue = 8) == 138: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxValue = 9999) == 6309016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxValue = 9999) == 6309016: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,maxValue = 5) == 5351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,maxValue = 5) == 5351: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,maxValue = 3) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,maxValue = 3) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,maxValue = 50) == 74895101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,maxValue = 50) == 74895101: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,maxValue = 100) == 959337187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,maxValue = 100) == 959337187: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,maxValue = 100) == 7537
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,maxValue = 100) == 7537: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,maxValue = 10) == 202201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,maxValue = 10) == 202201: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,maxValue = 9) == 373
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,maxValue = 9) == 373: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,maxValue = 20) == 436322284
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,maxValue = 20) == 436322284: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,maxValue = 10000) == 239341549
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,maxValue = 10000) == 239341549: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,maxValue = 50) == 388980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,maxValue = 50) == 388980: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,maxValue = 500) == 397370814
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,maxValue = 500) == 397370814: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,maxValue = 1000) == 91997497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,maxValue = 1000) == 91997497: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,maxValue = 7500) == 143340271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,maxValue = 7500) == 143340271: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,maxValue = 30) == 153176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,maxValue = 30) == 153176: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,maxValue = 500) == 652553975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,maxValue = 500) == 652553975: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,maxValue = 100) == 853200627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,maxValue = 100) == 853200627: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,maxValue = 5000) == 144035088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,maxValue = 5000) == 144035088: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,maxValue = 100) == 607180637
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,maxValue = 100) == 607180637: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,maxValue = 100) == 268368886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,maxValue = 100) == 268368886: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,maxValue = 100) == 200548806
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,maxValue = 100) == 200548806: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxValue = 100) == 105568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxValue = 100) == 105568: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,maxValue = 10000) == 93668
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,maxValue = 10000) == 93668: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,maxValue = 10000) == 466423769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,maxValue = 10000) == 466423769: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,maxValue = 10000) == 888200964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,maxValue = 10000) == 888200964: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,maxValue = 15) == 3711
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,maxValue = 15) == 3711: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,maxValue = 6000) == 321990518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,maxValue = 6000) == 321990518: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,maxValue = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,maxValue = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,maxValue = 30) == 290436
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,maxValue = 30) == 290436: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,maxValue = 10) == 170172001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,maxValue = 10) == 170172001: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,maxValue = 10000) == 430119293
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,maxValue = 10000) == 430119293: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,maxValue = 9000) == 358648747
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,maxValue = 9000) == 358648747: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,maxValue = 5000) == 777616479
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,maxValue = 5000) == 777616479: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 7,maxValue = 7) == 106
    assert candidate(n = 2,maxValue = 5) == 10
    assert candidate(n = 3,maxValue = 7) == 28
    assert candidate(n = 3,maxValue = 6) == 25
    assert candidate(n = 6,maxValue = 12) == 327
    assert candidate(n = 10,maxValue = 5) == 86
    assert candidate(n = 4,maxValue = 4) == 19
    assert candidate(n = 10,maxValue = 10) == 571
    assert candidate(n = 4,maxValue = 7) == 43
    assert candidate(n = 3,maxValue = 2) == 4
    assert candidate(n = 10000,maxValue = 10000) == 22940607
    assert candidate(n = 4,maxValue = 10) == 89
    assert candidate(n = 5,maxValue = 3) == 11
    assert candidate(n = 2000,maxValue = 10) == 347343994
    assert candidate(n = 15,maxValue = 10) == 1431
    assert candidate(n = 7,maxValue = 20) == 1191
    assert candidate(n = 8000,maxValue = 8000) == 106406983
    assert candidate(n = 8,maxValue = 16) == 1115
    assert candidate(n = 6000,maxValue = 6000) == 883250062
    assert candidate(n = 2000,maxValue = 5000) == 716352377
    assert candidate(n = 10000,maxValue = 1) == 1
    assert candidate(n = 100,maxValue = 50) == 604383896
    assert candidate(n = 1000,maxValue = 4) == 502501
    assert candidate(n = 9,maxValue = 5) == 73
    assert candidate(n = 7,maxValue = 15) == 575
    assert candidate(n = 10,maxValue = 20) == 3176
    assert candidate(n = 2000,maxValue = 1000) == 534638579
    assert candidate(n = 10,maxValue = 15) == 1341
    assert candidate(n = 50,maxValue = 20) == 519126
    assert candidate(n = 8,maxValue = 3) == 17
    assert candidate(n = 20,maxValue = 2) == 21
    assert candidate(n = 6,maxValue = 3) == 13
    assert candidate(n = 100,maxValue = 3) == 201
    assert candidate(n = 10000,maxValue = 5000) == 22892639
    assert candidate(n = 9999,maxValue = 10000) == 667133522
    assert candidate(n = 6000,maxValue = 3000) == 80648523
    assert candidate(n = 3000,maxValue = 3000) == 806624302
    assert candidate(n = 2000,maxValue = 2000) == 585712681
    assert candidate(n = 3,maxValue = 1) == 1
    assert candidate(n = 5000,maxValue = 5) == 12517501
    assert candidate(n = 5000,maxValue = 2000) == 802769368
    assert candidate(n = 1000,maxValue = 2000) == 228299266
    assert candidate(n = 8,maxValue = 20) == 1707
    assert candidate(n = 50,maxValue = 25) == 1630451
    assert candidate(n = 100,maxValue = 2) == 101
    assert candidate(n = 5,maxValue = 1) == 1
    assert candidate(n = 6,maxValue = 8) == 138
    assert candidate(n = 5,maxValue = 9999) == 6309016
    assert candidate(n = 100,maxValue = 5) == 5351
    assert candidate(n = 500,maxValue = 3) == 1001
    assert candidate(n = 2000,maxValue = 50) == 74895101
    assert candidate(n = 100,maxValue = 100) == 959337187
    assert candidate(n = 5,maxValue = 100) == 7537
    assert candidate(n = 100,maxValue = 10) == 202201
    assert candidate(n = 9,maxValue = 9) == 373
    assert candidate(n = 5000,maxValue = 20) == 436322284
    assert candidate(n = 2000,maxValue = 10000) == 239341549
    assert candidate(n = 20,maxValue = 50) == 388980
    assert candidate(n = 10000,maxValue = 500) == 397370814
    assert candidate(n = 1000,maxValue = 1000) == 91997497
    assert candidate(n = 7500,maxValue = 7500) == 143340271
    assert candidate(n = 25,maxValue = 30) == 153176
    assert candidate(n = 500,maxValue = 500) == 652553975
    assert candidate(n = 5000,maxValue = 100) == 853200627
    assert candidate(n = 5000,maxValue = 5000) == 144035088
    assert candidate(n = 1000,maxValue = 100) == 607180637
    assert candidate(n = 50,maxValue = 100) == 268368886
    assert candidate(n = 10000,maxValue = 100) == 200548806
    assert candidate(n = 10,maxValue = 100) == 105568
    assert candidate(n = 2,maxValue = 10000) == 93668
    assert candidate(n = 10,maxValue = 10000) == 466423769
    assert candidate(n = 1000,maxValue = 10000) == 888200964
    assert candidate(n = 15,maxValue = 15) == 3711
    assert candidate(n = 3000,maxValue = 6000) == 321990518
    assert candidate(n = 8,maxValue = 2) == 9
    assert candidate(n = 30,maxValue = 30) == 290436
    assert candidate(n = 1000,maxValue = 10) == 170172001
    assert candidate(n = 7500,maxValue = 10000) == 430119293
    assert candidate(n = 8000,maxValue = 9000) == 358648747
    assert candidate(n = 7500,maxValue = 5000) == 777616479


