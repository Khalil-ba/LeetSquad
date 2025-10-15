def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 2,target = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,target = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,target = 100) == 7500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,target = 100) == 7500: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,target = 8) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,target = 8) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,target = 1000000000) == 750000042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,target = 1000000000) == 750000042: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,target = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,target = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,target = 15) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,target = 15) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,target = 5) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,target = 5) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,target = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,target = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,target = 10) == 5430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,target = 10) == 5430: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,target = 100) == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,target = 100) == 1275: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,target = 1) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,target = 1) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,target = 10001) == 75005000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,target = 10001) == 75005000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,target = 20000) == 50005000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,target = 20000) == 50005000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,target = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,target = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,target = 250) == 29400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,target = 250) == 29400: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,target = 250) == 171750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,target = 250) == 171750: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,target = 10) == 127230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,target = 10) == 127230: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,target = 10000000) == 916675007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,target = 10000000) == 916675007: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000,target = 5000000) == 997018757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000,target = 5000000) == 997018757: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,target = 150000000) == 769375007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,target = 150000000) == 769375007: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,target = 40) == 4380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,target = 40) == 4380: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,target = 1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,target = 1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,target = 500) == 687250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,target = 500) == 687250: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,target = 1500) == 6186750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,target = 1500) == 6186750: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,target = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,target = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,target = 5000) == 68747500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,target = 5000) == 68747500: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,target = 1001) == 750500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,target = 1001) == 750500: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,target = 50) == 6850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,target = 50) == 6850: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,target = 750000000) == 921875014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,target = 750000000) == 921875014: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,target = 7500) == 73436250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,target = 7500) == 73436250: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,target = 101) == 7550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,target = 101) == 7550: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,target = 50) == 4050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,target = 50) == 4050: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,target = 1000) == 750000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,target = 1000) == 750000: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,target = 15) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,target = 15) == 301: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 1000000000) == 250000050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 1000000000) == 250000050: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,target = 100000000) == 947500007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,target = 100000000) == 947500007: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,target = 500000000) == 687500014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,target = 500000000) == 687500014: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,target = 301) == 67650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,target = 301) == 67650: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,target = 100000) == 499798971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,target = 100000) == 499798971: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,target = 25) == 681
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,target = 25) == 681: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,target = 2000) == 500500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,target = 2000) == 500500: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,target = 100) == 4075
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,target = 100) == 4075: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 999999999) == 750000049
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 999999999) == 750000049: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,target = 500000) == 499745191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,target = 500000) == 499745191: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,target = 300) == 27550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,target = 300) == 27550: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000,target = 1000000) == 997896757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000,target = 1000000) == 997896757: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,target = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,target = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,target = 150) == 61800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,target = 150) == 61800: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,target = 10) == 1455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,target = 10) == 1455: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000000,target = 75000000) == 10312500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000000,target = 75000000) == 10312500: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,target = 50000) == 874974958
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,target = 50000) == 874974958: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,target = 150) == 2850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,target = 150) == 2850: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,target = 150) == 29350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,target = 150) == 29350: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,target = 800000000) == 960000007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,target = 800000000) == 960000007: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,target = 500) == 187500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,target = 500) == 187500: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,target = 25000) == 718737493
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,target = 25000) == 718737493: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,target = 20) == 1635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,target = 20) == 1635: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,target = 100) == 547050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,target = 100) == 547050: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,target = 150) == 331575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,target = 150) == 331575: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000000,target = 50000000) == 10312500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000000,target = 50000000) == 10312500: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,target = 25) == 1731
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,target = 25) == 1731: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000000,target = 25000000) == 949843757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000000,target = 25000000) == 949843757: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,target = 300) == 11325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,target = 300) == 11325: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,target = 100) == 147300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,target = 100) == 147300: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000,target = 500000000) == 906250007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000,target = 500000000) == 906250007: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,target = 505) == 688996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,target = 505) == 688996: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,target = 1000000) == 999994757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,target = 1000000) == 999994757: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,target = 75) == 4256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,target = 75) == 4256: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,target = 2000) == 16498500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,target = 2000) == 16498500: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,target = 150000000) == 976875007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,target = 150000000) == 976875007: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999,target = 100000000) == 797500008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999,target = 100000000) == 797500008: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,target = 5001) == 18752500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,target = 5001) == 18752500: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 500000000) == 687500050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 500000000) == 687500050: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,target = 90) == 6075
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,target = 90) == 6075: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,target = 100001) == 500049951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,target = 100001) == 500049951: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,target = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,target = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,target = 11) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,target = 11) == 80: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000,target = 25000000) == 975468757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000,target = 25000000) == 975468757: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,target = 15) == 451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,target = 15) == 451: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,target = 75) == 15506
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,target = 75) == 15506: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,target = 10000) == 75000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,target = 10000) == 75000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,target = 1) == 15000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,target = 1) == 15000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,target = 1000000000) == 375000007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,target = 1000000000) == 375000007: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,target = 300) == 177400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,target = 300) == 177400: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,target = 200) == 16275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,target = 200) == 16275: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,target = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,target = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,target = 200) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,target = 200) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,target = 30) == 1765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,target = 30) == 1765: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,target = 10000) == 474979993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,target = 10000) == 474979993: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 2,target = 3) == 4
    assert candidate(n = 100,target = 100) == 7500
    assert candidate(n = 5,target = 8) == 18
    assert candidate(n = 1,target = 1) == 1
    assert candidate(n = 1000000000,target = 1000000000) == 750000042
    assert candidate(n = 3,target = 3) == 8
    assert candidate(n = 10,target = 15) == 76
    assert candidate(n = 10,target = 5) == 71
    assert candidate(n = 5,target = 10) == 15
    assert candidate(n = 100,target = 10) == 5430
    assert candidate(n = 50,target = 100) == 1275
    assert candidate(n = 100,target = 1) == 5050
    assert candidate(n = 10000,target = 10001) == 75005000
    assert candidate(n = 10000,target = 20000) == 50005000
    assert candidate(n = 5,target = 2) == 15
    assert candidate(n = 200,target = 250) == 29400
    assert candidate(n = 500,target = 250) == 171750
    assert candidate(n = 500,target = 10) == 127230
    assert candidate(n = 100000000,target = 10000000) == 916675007
    assert candidate(n = 10000000,target = 5000000) == 997018757
    assert candidate(n = 200000000,target = 150000000) == 769375007
    assert candidate(n = 80,target = 40) == 4380
    assert candidate(n = 1000000000,target = 1) == 21
    assert candidate(n = 1000,target = 500) == 687250
    assert candidate(n = 3000,target = 1500) == 6186750
    assert candidate(n = 3,target = 7) == 6
    assert candidate(n = 10000,target = 5000) == 68747500
    assert candidate(n = 1000,target = 1001) == 750500
    assert candidate(n = 100,target = 50) == 6850
    assert candidate(n = 500000000,target = 750000000) == 921875014
    assert candidate(n = 10000,target = 7500) == 73436250
    assert candidate(n = 100,target = 101) == 7550
    assert candidate(n = 75,target = 50) == 4050
    assert candidate(n = 1000,target = 1000) == 750000
    assert candidate(n = 20,target = 15) == 301
    assert candidate(n = 999999999,target = 1000000000) == 250000050
    assert candidate(n = 100000000,target = 100000000) == 947500007
    assert candidate(n = 500000000,target = 500000000) == 687500014
    assert candidate(n = 300,target = 301) == 67650
    assert candidate(n = 500000,target = 100000) == 499798971
    assert candidate(n = 30,target = 25) == 681
    assert candidate(n = 1000,target = 2000) == 500500
    assert candidate(n = 75,target = 100) == 4075
    assert candidate(n = 999999999,target = 999999999) == 750000049
    assert candidate(n = 1000000,target = 500000) == 499745191
    assert candidate(n = 200,target = 300) == 27550
    assert candidate(n = 5000000,target = 1000000) == 997896757
    assert candidate(n = 2,target = 5) == 3
    assert candidate(n = 300,target = 150) == 61800
    assert candidate(n = 50,target = 10) == 1455
    assert candidate(n = 25000000,target = 75000000) == 10312500
    assert candidate(n = 100000,target = 50000) == 874974958
    assert candidate(n = 999999999,target = 2) == 28
    assert candidate(n = 75,target = 150) == 2850
    assert candidate(n = 200,target = 150) == 29350
    assert candidate(n = 200000000,target = 800000000) == 960000007
    assert candidate(n = 500,target = 500) == 187500
    assert candidate(n = 50000,target = 25000) == 718737493
    assert candidate(n = 50,target = 20) == 1635
    assert candidate(n = 1000,target = 100) == 547050
    assert candidate(n = 750,target = 150) == 331575
    assert candidate(n = 25000000,target = 50000000) == 10312500
    assert candidate(n = 50,target = 25) == 1731
    assert candidate(n = 75000000,target = 25000000) == 949843757
    assert candidate(n = 150,target = 300) == 11325
    assert candidate(n = 500,target = 100) == 147300
    assert candidate(n = 250000000,target = 500000000) == 906250007
    assert candidate(n = 1000,target = 505) == 688996
    assert candidate(n = 1000000,target = 1000000) == 999994757
    assert candidate(n = 75,target = 75) == 4256
    assert candidate(n = 5000,target = 2000) == 16498500
    assert candidate(n = 100000000,target = 150000000) == 976875007
    assert candidate(n = 99999999,target = 100000000) == 797500008
    assert candidate(n = 5000,target = 5001) == 18752500
    assert candidate(n = 999999999,target = 500000000) == 687500050
    assert candidate(n = 90,target = 90) == 6075
    assert candidate(n = 100000,target = 100001) == 500049951
    assert candidate(n = 1,target = 1000000000) == 1
    assert candidate(n = 10,target = 11) == 80
    assert candidate(n = 50000000,target = 25000000) == 975468757
    assert candidate(n = 25,target = 15) == 451
    assert candidate(n = 150,target = 75) == 15506
    assert candidate(n = 10000,target = 10000) == 75000000
    assert candidate(n = 100000000,target = 1) == 15000000
    assert candidate(n = 500000000,target = 1000000000) == 375000007
    assert candidate(n = 500,target = 300) == 177400
    assert candidate(n = 150,target = 200) == 16275
    assert candidate(n = 1,target = 2) == 1
    assert candidate(n = 200,target = 200) == 30000
    assert candidate(n = 50,target = 30) == 1765
    assert candidate(n = 50000,target = 10000) == 474979993


