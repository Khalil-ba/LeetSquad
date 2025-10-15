def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mainTank = 10,additionalTank = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 10,additionalTank = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 100,additionalTank = 100) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 100,additionalTank = 100) == 1240: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 3,additionalTank = 0) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 3,additionalTank = 0) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 7,additionalTank = 3) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 7,additionalTank = 3) == 80: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 0,additionalTank = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 0,additionalTank = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 1,additionalTank = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 1,additionalTank = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 0,additionalTank = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 0,additionalTank = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 10,additionalTank = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 10,additionalTank = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 0,additionalTank = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 0,additionalTank = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 20,additionalTank = 0) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 20,additionalTank = 0) == 200: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 20,additionalTank = 20) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 20,additionalTank = 20) == 240: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 0) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 0) == 50: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 45,additionalTank = 5) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 45,additionalTank = 5) == 500: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 80,additionalTank = 10) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 80,additionalTank = 10) == 900: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 55,additionalTank = 0) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 55,additionalTank = 0) == 550: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 15,additionalTank = 1) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 15,additionalTank = 1) == 160: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 1,additionalTank = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 1,additionalTank = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 3,additionalTank = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 3,additionalTank = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 50,additionalTank = 50) == 620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 50,additionalTank = 50) == 620: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 25,additionalTank = 30) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 25,additionalTank = 30) == 310: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 25,additionalTank = 10) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 25,additionalTank = 10) == 310: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 25) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 25) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 80,additionalTank = 20) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 80,additionalTank = 20) == 990: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 30,additionalTank = 3) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 30,additionalTank = 3) == 330: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 50,additionalTank = 15) == 620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 50,additionalTank = 15) == 620: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 49,additionalTank = 5) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 49,additionalTank = 5) == 540: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 45,additionalTank = 50) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 45,additionalTank = 50) == 560: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 3,additionalTank = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 3,additionalTank = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 30,additionalTank = 30) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 30,additionalTank = 30) == 370: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 7,additionalTank = 1) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 7,additionalTank = 1) == 80: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 99,additionalTank = 99) == 1230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 99,additionalTank = 99) == 1230: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 75,additionalTank = 15) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 75,additionalTank = 15) == 900: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 9,additionalTank = 3) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 9,additionalTank = 3) == 110: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 60,additionalTank = 30) == 740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 60,additionalTank = 30) == 740: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 9,additionalTank = 2) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 9,additionalTank = 2) == 110: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 15,additionalTank = 2) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 15,additionalTank = 2) == 170: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 50,additionalTank = 10) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 50,additionalTank = 10) == 600: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 75,additionalTank = 20) == 930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 75,additionalTank = 20) == 930: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 50) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 50) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 8,additionalTank = 1) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 8,additionalTank = 1) == 90: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 30,additionalTank = 0) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 30,additionalTank = 0) == 300: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 99,additionalTank = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 99,additionalTank = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 30,additionalTank = 8) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 30,additionalTank = 8) == 370: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 40,additionalTank = 30) == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 40,additionalTank = 30) == 490: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 10,additionalTank = 99) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 10,additionalTank = 99) == 120: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 80,additionalTank = 3) == 830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 80,additionalTank = 3) == 830: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 3,additionalTank = 7) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 3,additionalTank = 7) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 9,additionalTank = 10) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 9,additionalTank = 10) == 110: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 15,additionalTank = 0) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 15,additionalTank = 0) == 150: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 75,additionalTank = 25) == 930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 75,additionalTank = 25) == 930: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 49,additionalTank = 10) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 49,additionalTank = 10) == 590: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 25,additionalTank = 0) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 25,additionalTank = 0) == 250: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 75,additionalTank = 30) == 930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 75,additionalTank = 30) == 930: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 24,additionalTank = 6) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 24,additionalTank = 6) == 290: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 45,additionalTank = 30) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 45,additionalTank = 30) == 560: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 99,additionalTank = 100) == 1230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 99,additionalTank = 100) == 1230: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 25,additionalTank = 5) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 25,additionalTank = 5) == 300: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 45,additionalTank = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 45,additionalTank = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 80,additionalTank = 8) == 880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 80,additionalTank = 8) == 880: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 49,additionalTank = 2) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 49,additionalTank = 2) == 510: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 50,additionalTank = 25) == 620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 50,additionalTank = 25) == 620: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 30,additionalTank = 15) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 30,additionalTank = 15) == 370: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 100,additionalTank = 1) == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 100,additionalTank = 1) == 1010: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 25,additionalTank = 25) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 25,additionalTank = 25) == 310: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 25,additionalTank = 15) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 25,additionalTank = 15) == 310: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 60,additionalTank = 25) == 740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 60,additionalTank = 25) == 740: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 60,additionalTank = 0) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 60,additionalTank = 0) == 600: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 8,additionalTank = 7) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 8,additionalTank = 7) == 90: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 20) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 20) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 2,additionalTank = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 2,additionalTank = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 30,additionalTank = 10) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 30,additionalTank = 10) == 370: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 8,additionalTank = 3) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 8,additionalTank = 3) == 90: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 60,additionalTank = 15) == 740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 60,additionalTank = 15) == 740: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 10,additionalTank = 9) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 10,additionalTank = 9) == 120: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 100,additionalTank = 0) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 100,additionalTank = 0) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 5,additionalTank = 4) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 5,additionalTank = 4) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mainTank = 4,additionalTank = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mainTank = 4,additionalTank = 5) == 40: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mainTank = 10,additionalTank = 0) == 100
    assert candidate(mainTank = 100,additionalTank = 100) == 1240
    assert candidate(mainTank = 5,additionalTank = 10) == 60
    assert candidate(mainTank = 3,additionalTank = 0) == 30
    assert candidate(mainTank = 7,additionalTank = 3) == 80
    assert candidate(mainTank = 0,additionalTank = 5) == 0
    assert candidate(mainTank = 1,additionalTank = 2) == 10
    assert candidate(mainTank = 0,additionalTank = 10) == 0
    assert candidate(mainTank = 10,additionalTank = 5) == 120
    assert candidate(mainTank = 0,additionalTank = 50) == 0
    assert candidate(mainTank = 20,additionalTank = 0) == 200
    assert candidate(mainTank = 20,additionalTank = 20) == 240
    assert candidate(mainTank = 5,additionalTank = 0) == 50
    assert candidate(mainTank = 45,additionalTank = 5) == 500
    assert candidate(mainTank = 80,additionalTank = 10) == 900
    assert candidate(mainTank = 55,additionalTank = 0) == 550
    assert candidate(mainTank = 15,additionalTank = 1) == 160
    assert candidate(mainTank = 1,additionalTank = 50) == 10
    assert candidate(mainTank = 3,additionalTank = 20) == 30
    assert candidate(mainTank = 50,additionalTank = 50) == 620
    assert candidate(mainTank = 25,additionalTank = 30) == 310
    assert candidate(mainTank = 25,additionalTank = 10) == 310
    assert candidate(mainTank = 5,additionalTank = 25) == 60
    assert candidate(mainTank = 80,additionalTank = 20) == 990
    assert candidate(mainTank = 30,additionalTank = 3) == 330
    assert candidate(mainTank = 50,additionalTank = 15) == 620
    assert candidate(mainTank = 49,additionalTank = 5) == 540
    assert candidate(mainTank = 45,additionalTank = 50) == 560
    assert candidate(mainTank = 3,additionalTank = 4) == 30
    assert candidate(mainTank = 30,additionalTank = 30) == 370
    assert candidate(mainTank = 7,additionalTank = 1) == 80
    assert candidate(mainTank = 99,additionalTank = 99) == 1230
    assert candidate(mainTank = 75,additionalTank = 15) == 900
    assert candidate(mainTank = 9,additionalTank = 3) == 110
    assert candidate(mainTank = 60,additionalTank = 30) == 740
    assert candidate(mainTank = 9,additionalTank = 2) == 110
    assert candidate(mainTank = 15,additionalTank = 2) == 170
    assert candidate(mainTank = 50,additionalTank = 10) == 600
    assert candidate(mainTank = 75,additionalTank = 20) == 930
    assert candidate(mainTank = 5,additionalTank = 50) == 60
    assert candidate(mainTank = 8,additionalTank = 1) == 90
    assert candidate(mainTank = 30,additionalTank = 0) == 300
    assert candidate(mainTank = 99,additionalTank = 1) == 1000
    assert candidate(mainTank = 30,additionalTank = 8) == 370
    assert candidate(mainTank = 40,additionalTank = 30) == 490
    assert candidate(mainTank = 10,additionalTank = 99) == 120
    assert candidate(mainTank = 80,additionalTank = 3) == 830
    assert candidate(mainTank = 3,additionalTank = 7) == 30
    assert candidate(mainTank = 9,additionalTank = 10) == 110
    assert candidate(mainTank = 15,additionalTank = 0) == 150
    assert candidate(mainTank = 75,additionalTank = 25) == 930
    assert candidate(mainTank = 49,additionalTank = 10) == 590
    assert candidate(mainTank = 25,additionalTank = 0) == 250
    assert candidate(mainTank = 75,additionalTank = 30) == 930
    assert candidate(mainTank = 24,additionalTank = 6) == 290
    assert candidate(mainTank = 45,additionalTank = 30) == 560
    assert candidate(mainTank = 99,additionalTank = 100) == 1230
    assert candidate(mainTank = 25,additionalTank = 5) == 300
    assert candidate(mainTank = 45,additionalTank = 10) == 550
    assert candidate(mainTank = 80,additionalTank = 8) == 880
    assert candidate(mainTank = 49,additionalTank = 2) == 510
    assert candidate(mainTank = 50,additionalTank = 25) == 620
    assert candidate(mainTank = 30,additionalTank = 15) == 370
    assert candidate(mainTank = 100,additionalTank = 1) == 1010
    assert candidate(mainTank = 25,additionalTank = 25) == 310
    assert candidate(mainTank = 25,additionalTank = 15) == 310
    assert candidate(mainTank = 60,additionalTank = 25) == 740
    assert candidate(mainTank = 60,additionalTank = 0) == 600
    assert candidate(mainTank = 8,additionalTank = 7) == 90
    assert candidate(mainTank = 5,additionalTank = 20) == 60
    assert candidate(mainTank = 2,additionalTank = 10) == 20
    assert candidate(mainTank = 5,additionalTank = 5) == 60
    assert candidate(mainTank = 30,additionalTank = 10) == 370
    assert candidate(mainTank = 8,additionalTank = 3) == 90
    assert candidate(mainTank = 60,additionalTank = 15) == 740
    assert candidate(mainTank = 10,additionalTank = 9) == 120
    assert candidate(mainTank = 100,additionalTank = 0) == 1000
    assert candidate(mainTank = 5,additionalTank = 4) == 60
    assert candidate(mainTank = 4,additionalTank = 5) == 40


