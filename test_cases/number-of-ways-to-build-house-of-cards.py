def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 184941
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 184941: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 209: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 25008984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 25008984: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 496) == 22861784
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 496) == 22861784: {e}')
    
    total += 1
    try:
        result = candidate(n = 333) == 455290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333) == 455290: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 498) == 23870227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 498) == 23870227: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 9090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 9090: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 65) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 480) == 16023822
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 480) == 16023822: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 444) == 7073140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 444) == 7073140: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 450) == 8122366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450) == 8122366: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 360) == 921049
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 360) == 921049: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 195) == 7728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 195) == 7728: {e}')
    
    total += 1
    try:
        result = candidate(n = 495) == 22346078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 495) == 22346078: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 207: {e}')
    
    total += 1
    try:
        result = candidate(n = 299) == 180379
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 299) == 180379: {e}')
    
    total += 1
    try:
        result = candidate(n = 46) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 240) == 31975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 240) == 31975: {e}')
    
    total += 1
    try:
        result = candidate(n = 350) == 705904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350) == 705904: {e}')
    
    total += 1
    try:
        result = candidate(n = 497) == 23415948
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 497) == 23415948: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 499) == 24423102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499) == 24423102: {e}')
    
    total += 1
    try:
        result = candidate(n = 52) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 52) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 109: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 295) == 163082
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 295) == 163082: {e}')
    
    total += 1
    try:
        result = candidate(n = 280) == 106587
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 280) == 106587: {e}')
    
    total += 1
    try:
        result = candidate(n = 34) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 518: {e}')
    
    total += 1
    try:
        result = candidate(n = 222) == 18341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222) == 18341: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 95) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95) == 162: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 76) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 76) == 59: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == 20149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == 20149: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 249) == 42008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 249) == 42008: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 1574
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 1574: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == 4668
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == 4668: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 543
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 543: {e}')
    
    total += 1
    try:
        result = candidate(n = 58) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 58) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 395) == 2198030
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 395) == 2198030: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 349) == 693173
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 349) == 693173: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 170: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 449) == 7947751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 449) == 7947751: {e}')
    
    total += 1
    try:
        result = candidate(n = 175) == 3730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 175) == 3730: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 43794
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 43794: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 140) == 988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140) == 988: {e}')
    
    total += 1
    try:
        result = candidate(n = 149) == 1406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 149) == 1406: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 275) == 91942
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 275) == 91942: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 2480683
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 2480683: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 451: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 0
    assert candidate(n = 11) == 1
    assert candidate(n = 30) == 5
    assert candidate(n = 1) == 0
    assert candidate(n = 4) == 0
    assert candidate(n = 16) == 2
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 1
    assert candidate(n = 300) == 184941
    assert candidate(n = 100) == 209
    assert candidate(n = 500) == 25008984
    assert candidate(n = 50) == 16
    assert candidate(n = 7) == 1
    assert candidate(n = 10) == 1
    assert candidate(n = 5) == 1
    assert candidate(n = 45) == 14
    assert candidate(n = 70) == 41
    assert candidate(n = 496) == 22861784
    assert candidate(n = 333) == 455290
    assert candidate(n = 8) == 1
    assert candidate(n = 35) == 4
    assert candidate(n = 36) == 8
    assert candidate(n = 77) == 74
    assert candidate(n = 24) == 3
    assert candidate(n = 498) == 23870227
    assert candidate(n = 200) == 9090
    assert candidate(n = 55) == 16
    assert candidate(n = 65) == 40
    assert candidate(n = 480) == 16023822
    assert candidate(n = 21) == 2
    assert candidate(n = 444) == 7073140
    assert candidate(n = 28) == 4
    assert candidate(n = 450) == 8122366
    assert candidate(n = 17) == 1
    assert candidate(n = 360) == 921049
    assert candidate(n = 42) == 12
    assert candidate(n = 80) == 86
    assert candidate(n = 195) == 7728
    assert candidate(n = 495) == 22346078
    assert candidate(n = 101) == 207
    assert candidate(n = 299) == 180379
    assert candidate(n = 46) == 9
    assert candidate(n = 75) == 55
    assert candidate(n = 240) == 31975
    assert candidate(n = 350) == 705904
    assert candidate(n = 497) == 23415948
    assert candidate(n = 6) == 0
    assert candidate(n = 499) == 24423102
    assert candidate(n = 52) == 13
    assert candidate(n = 90) == 109
    assert candidate(n = 49) == 11
    assert candidate(n = 295) == 163082
    assert candidate(n = 280) == 106587
    assert candidate(n = 34) == 5
    assert candidate(n = 123) == 518
    assert candidate(n = 222) == 18341
    assert candidate(n = 60) == 28
    assert candidate(n = 95) == 162
    assert candidate(n = 33) == 7
    assert candidate(n = 76) == 59
    assert candidate(n = 225) == 20149
    assert candidate(n = 18) == 1
    assert candidate(n = 249) == 42008
    assert candidate(n = 48) == 16
    assert candidate(n = 150) == 1574
    assert candidate(n = 15) == 1
    assert candidate(n = 14) == 1
    assert candidate(n = 180) == 4668
    assert candidate(n = 12) == 0
    assert candidate(n = 125) == 543
    assert candidate(n = 58) == 19
    assert candidate(n = 395) == 2198030
    assert candidate(n = 40) == 7
    assert candidate(n = 349) == 693173
    assert candidate(n = 99) == 170
    assert candidate(n = 64) == 28
    assert candidate(n = 449) == 7947751
    assert candidate(n = 175) == 3730
    assert candidate(n = 250) == 43794
    assert candidate(n = 22) == 3
    assert candidate(n = 140) == 988
    assert candidate(n = 149) == 1406
    assert candidate(n = 19) == 3
    assert candidate(n = 85) == 98
    assert candidate(n = 275) == 91942
    assert candidate(n = 400) == 2480683
    assert candidate(n = 31) == 5
    assert candidate(n = 120) == 451
    assert candidate(n = 25) == 4


