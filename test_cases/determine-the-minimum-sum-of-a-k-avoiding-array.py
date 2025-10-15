def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,k = 8) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 8) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 15) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 15) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 7) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 7) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 8) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 8) == 153: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 18) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 18) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 16) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 16) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 35) == 936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 35) == 936: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 30) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 30) == 280: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 25) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 25) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3) == 134: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 31) == 690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 31) == 690: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 1) == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 1) == 1275: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 11) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 11) == 65: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 15) == 626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 15) == 626: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 30) == 1455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 30) == 1455: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 9) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 9) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 8) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 8) == 102: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 40) == 1510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 40) == 1510: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 11) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 11) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 20) == 1090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 20) == 1090: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 13) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 13) == 114: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 16) == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 16) == 444: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 18) == 558
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 18) == 558: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 20) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 20) == 460: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 11) == 1235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 11) == 1235: {e}')
    
    total += 1
    try:
        result = candidate(n = 48,k = 49) == 1752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48,k = 49) == 1752: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 12) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 12) == 165: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 25) == 1669
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 25) == 1669: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 30) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 30) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 12) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 12) == 60: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 14) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 14) == 57: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 25) == 681
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 25) == 681: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 18) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 18) == 243: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 22) == 213
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 22) == 213: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 30) == 1701
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 30) == 1701: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 7) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 7) == 216: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 9) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 9) == 52: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 10) == 565
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 10) == 565: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 12) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 12) == 280: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 35) == 686
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 35) == 686: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 30) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 30) == 465: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 25) == 906
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 25) == 906: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 45) == 1216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 45) == 1216: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 12) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 12) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5) == 146: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 15) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 15) == 301: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 51) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 51) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 8) == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 8) == 258: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 20) == 855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 20) == 855: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 40) == 655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 40) == 655: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 50) == 1875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 50) == 1875: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 27) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 27) == 370: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 45) == 1541
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 45) == 1541: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 28) == 588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 28) == 588: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 20) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 20) == 165: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 47) == 1541
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 47) == 1541: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 18) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 18) == 145: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 18) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 18) == 102: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 8) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 8) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 35) == 1211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 35) == 1211: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 30) == 1170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 30) == 1170: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 35) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 35) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 9) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 9) == 145: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 25) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 25) == 306: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 10) == 960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 10) == 960: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 50) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 50) == 325: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 40) == 1845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 40) == 1845: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 20) == 1350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 20) == 1350: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 100) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 100) == 325: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,k = 8) == 10
    assert candidate(n = 3,k = 5) == 8
    assert candidate(n = 10,k = 15) == 76
    assert candidate(n = 4,k = 7) == 13
    assert candidate(n = 7,k = 10) == 36
    assert candidate(n = 2,k = 6) == 3
    assert candidate(n = 10,k = 10) == 75
    assert candidate(n = 5,k = 4) == 18
    assert candidate(n = 15,k = 8) == 153
    assert candidate(n = 10,k = 18) == 63
    assert candidate(n = 8,k = 16) == 36
    assert candidate(n = 35,k = 35) == 936
    assert candidate(n = 20,k = 30) == 280
    assert candidate(n = 15,k = 25) == 156
    assert candidate(n = 15,k = 3) == 134
    assert candidate(n = 30,k = 31) == 690
    assert candidate(n = 50,k = 1) == 1275
    assert candidate(n = 9,k = 11) == 65
    assert candidate(n = 30,k = 15) == 626
    assert candidate(n = 45,k = 30) == 1455
    assert candidate(n = 10,k = 9) == 79
    assert candidate(n = 12,k = 8) == 102
    assert candidate(n = 45,k = 40) == 1510
    assert candidate(n = 6,k = 11) == 26
    assert candidate(n = 40,k = 20) == 1090
    assert candidate(n = 12,k = 13) == 114
    assert candidate(n = 25,k = 16) == 444
    assert candidate(n = 5,k = 20) == 15
    assert candidate(n = 28,k = 18) == 558
    assert candidate(n = 25,k = 20) == 460
    assert candidate(n = 45,k = 11) == 1235
    assert candidate(n = 48,k = 49) == 1752
    assert candidate(n = 15,k = 12) == 165
    assert candidate(n = 49,k = 25) == 1669
    assert candidate(n = 15,k = 30) == 120
    assert candidate(n = 9,k = 12) == 60
    assert candidate(n = 9,k = 14) == 57
    assert candidate(n = 30,k = 25) == 681
    assert candidate(n = 10,k = 5) == 71
    assert candidate(n = 18,k = 18) == 243
    assert candidate(n = 17,k = 22) == 213
    assert candidate(n = 5,k = 10) == 15
    assert candidate(n = 49,k = 30) == 1701
    assert candidate(n = 18,k = 7) == 216
    assert candidate(n = 8,k = 9) == 52
    assert candidate(n = 30,k = 10) == 565
    assert candidate(n = 20,k = 12) == 280
    assert candidate(n = 30,k = 35) == 686
    assert candidate(n = 25,k = 30) == 465
    assert candidate(n = 35,k = 25) == 906
    assert candidate(n = 40,k = 45) == 1216
    assert candidate(n = 8,k = 12) == 46
    assert candidate(n = 15,k = 5) == 146
    assert candidate(n = 20,k = 15) == 301
    assert candidate(n = 50,k = 51) == 1900
    assert candidate(n = 20,k = 8) == 258
    assert candidate(n = 35,k = 20) == 855
    assert candidate(n = 30,k = 40) == 655
    assert candidate(n = 50,k = 50) == 1875
    assert candidate(n = 22,k = 27) == 370
    assert candidate(n = 45,k = 45) == 1541
    assert candidate(n = 28,k = 28) == 588
    assert candidate(n = 15,k = 20) == 165
    assert candidate(n = 45,k = 47) == 1541
    assert candidate(n = 14,k = 18) == 145
    assert candidate(n = 12,k = 18) == 102
    assert candidate(n = 8,k = 8) == 48
    assert candidate(n = 40,k = 35) == 1211
    assert candidate(n = 40,k = 30) == 1170
    assert candidate(n = 6,k = 35) == 21
    assert candidate(n = 14,k = 9) == 145
    assert candidate(n = 20,k = 25) == 306
    assert candidate(n = 40,k = 10) == 960
    assert candidate(n = 25,k = 50) == 325
    assert candidate(n = 50,k = 40) == 1845
    assert candidate(n = 45,k = 20) == 1350
    assert candidate(n = 25,k = 100) == 325


