def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 500) == 70047606
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 500) == 70047606: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 7) == 796297179
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 7) == 796297179: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 3) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 3) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 4) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 4) == 165: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50) == 237930091
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50) == 237930091: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 10) == 10015005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 10) == 10015005: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3) == 924
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3) == 924: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 200) == 849395041
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 200) == 849395041: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 150) == 188049093
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 150) == 188049093: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 125) == 61117700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 125) == 61117700: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 100) == 412289370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 100) == 412289370: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 50) == 703668401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 50) == 703668401: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 200) == 89039524
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 200) == 89039524: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,k = 20) == 527894588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,k = 20) == 527894588: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 998) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 998) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 300) == 966786381
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 300) == 966786381: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 350) == 811412361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 350) == 811412361: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,k = 400) == 686452764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,k = 400) == 686452764: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 10) == 391975633
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 10) == 391975633: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 300) == 535696304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 300) == 535696304: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 10) == 984308396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 10) == 984308396: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 250) == 917595427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 250) == 917595427: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 150) == 37130153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 150) == 37130153: {e}')
    
    total += 1
    try:
        result = candidate(n = 998,k = 499) == 990039585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998,k = 499) == 990039585: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 250) == 1718306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 250) == 1718306: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 20) == 875426906
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 20) == 875426906: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 350) == 906610068
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 350) == 906610068: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 499) == 970118741
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 499) == 970118741: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 450) == 891508928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 450) == 891508928: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 100) == 945626632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 100) == 945626632: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 3) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 3) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 75) == 937415442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 75) == 937415442: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 20) == 344905395
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 20) == 344905395: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 100) == 47365034
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 100) == 47365034: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 5) == 20030010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 5) == 20030010: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10) == 697218647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10) == 697218647: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 20) == 114267332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 20) == 114267332: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5) == 92378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5) == 92378: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 15) == 188331431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 15) == 188331431: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 40) == 234333249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 40) == 234333249: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1) == 499500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1) == 499500: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 220) == 66442708
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 220) == 66442708: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 300) == 374845297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 300) == 374845297: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 375) == 796219809
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 375) == 796219809: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 300) == 508930020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 300) == 508930020: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 5) == 930713009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 5) == 930713009: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 400) == 530286193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 400) == 530286193: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 75) == 928665746
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 75) == 928665746: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 500) == 688428127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 500) == 688428127: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,k = 175) == 134369598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,k = 175) == 134369598: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 100) == 698790075
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 100) == 698790075: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 540818587
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 540818587: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3,k = 1) == 3
    assert candidate(n = 1000,k = 500) == 70047606
    assert candidate(n = 30,k = 7) == 796297179
    assert candidate(n = 6,k = 3) == 28
    assert candidate(n = 8,k = 4) == 165
    assert candidate(n = 5,k = 2) == 15
    assert candidate(n = 7,k = 1) == 21
    assert candidate(n = 100,k = 50) == 237930091
    assert candidate(n = 4,k = 2) == 5
    assert candidate(n = 20,k = 10) == 10015005
    assert candidate(n = 9,k = 2) == 210
    assert candidate(n = 10,k = 3) == 924
    assert candidate(n = 400,k = 200) == 849395041
    assert candidate(n = 300,k = 150) == 188049093
    assert candidate(n = 250,k = 125) == 61117700
    assert candidate(n = 200,k = 100) == 412289370
    assert candidate(n = 150,k = 50) == 703668401
    assert candidate(n = 500,k = 200) == 89039524
    assert candidate(n = 80,k = 20) == 527894588
    assert candidate(n = 1000,k = 999) == 1
    assert candidate(n = 999,k = 998) == 1
    assert candidate(n = 750,k = 300) == 966786381
    assert candidate(n = 800,k = 350) == 811412361
    assert candidate(n = 950,k = 400) == 686452764
    assert candidate(n = 25,k = 10) == 391975633
    assert candidate(n = 1000,k = 300) == 535696304
    assert candidate(n = 50,k = 10) == 984308396
    assert candidate(n = 600,k = 250) == 917595427
    assert candidate(n = 400,k = 150) == 37130153
    assert candidate(n = 998,k = 499) == 990039585
    assert candidate(n = 700,k = 250) == 1718306
    assert candidate(n = 50,k = 20) == 875426906
    assert candidate(n = 700,k = 350) == 906610068
    assert candidate(n = 999,k = 499) == 970118741
    assert candidate(n = 900,k = 450) == 891508928
    assert candidate(n = 600,k = 100) == 945626632
    assert candidate(n = 8,k = 3) == 210
    assert candidate(n = 150,k = 75) == 937415442
    assert candidate(n = 250,k = 20) == 344905395
    assert candidate(n = 250,k = 100) == 47365034
    assert candidate(n = 25,k = 5) == 20030010
    assert candidate(n = 100,k = 10) == 697218647
    assert candidate(n = 100,k = 20) == 114267332
    assert candidate(n = 15,k = 5) == 92378
    assert candidate(n = 50,k = 15) == 188331431
    assert candidate(n = 100,k = 40) == 234333249
    assert candidate(n = 1000,k = 1) == 499500
    assert candidate(n = 600,k = 220) == 66442708
    assert candidate(n = 800,k = 300) == 374845297
    assert candidate(n = 750,k = 375) == 796219809
    assert candidate(n = 600,k = 300) == 508930020
    assert candidate(n = 50,k = 5) == 930713009
    assert candidate(n = 800,k = 400) == 530286193
    assert candidate(n = 250,k = 75) == 928665746
    assert candidate(n = 999,k = 500) == 688428127
    assert candidate(n = 350,k = 175) == 134369598
    assert candidate(n = 500,k = 100) == 698790075
    assert candidate(n = 500,k = 250) == 540818587


