def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(p = 2,q = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 2,q = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 10,q = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 10,q = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 6,q = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 6,q = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 4,q = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 4,q = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 10,q = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 10,q = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 5,q = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 5,q = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 3,q = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 3,q = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 7,q = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 7,q = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 5,q = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 5,q = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 6,q = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 6,q = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 10,q = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 10,q = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 72,q = 27) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 72,q = 27) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 75,q = 33) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 75,q = 33) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 500,q = 250) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 500,q = 250) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 720,q = 180) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 720,q = 180) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 499) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 499) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 333) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 333) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 997,q = 333) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 997,q = 333) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 450,q = 135) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 450,q = 135) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 500,q = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 500,q = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 500,q = 249) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 500,q = 249) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 64,q = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 64,q = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 421) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 421) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 1000,q = 333) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 1000,q = 333) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 123,q = 45) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 123,q = 45) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 640,q = 160) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 640,q = 160) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 100,q = 37) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 100,q = 37) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 998) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 998) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 888,q = 352) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 888,q = 352) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 100,q = 33) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 100,q = 33) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 667,q = 222) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 667,q = 222) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 600,q = 150) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 600,q = 150) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 1000,q = 500) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 1000,q = 500) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 300,q = 220) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 300,q = 220) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 85,q = 21) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 85,q = 21) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 199,q = 71) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 199,q = 71) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 987,q = 123) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 987,q = 123) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 500,q = 450) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 500,q = 450) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 800,q = 300) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 800,q = 300) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 97,q = 42) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 97,q = 42) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 550,q = 110) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 550,q = 110) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 360,q = 121) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 360,q = 121) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 81,q = 27) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 81,q = 27) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 777,q = 388) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 777,q = 388) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 600,q = 161) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 600,q = 161) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 720,q = 199) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 720,q = 199) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 625,q = 125) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 625,q = 125) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 997,q = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 997,q = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 400,q = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 400,q = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 45,q = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 45,q = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 725,q = 297) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 725,q = 297) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 750,q = 250) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 750,q = 250) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 20,q = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 20,q = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 501,q = 167) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 501,q = 167) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 880,q = 198) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 880,q = 198) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 450,q = 125) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 450,q = 125) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 777,q = 333) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 777,q = 333) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 120,q = 49) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 120,q = 49) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 450,q = 225) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 450,q = 225) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 450,q = 181) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 450,q = 181) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 25,q = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 25,q = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 999,q = 777) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 999,q = 777) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 450,q = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 450,q = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 15,q = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 15,q = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 50,q = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 50,q = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 700,q = 175) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 700,q = 175) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 555,q = 111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 555,q = 111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 819,q = 273) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 819,q = 273) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 256,q = 192) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 256,q = 192) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 100,q = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 100,q = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 80,q = 21) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 80,q = 21) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 99,q = 66) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 99,q = 66) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 576,q = 384) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 576,q = 384) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 200,q = 77) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 200,q = 77) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 500,q = 125) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 500,q = 125) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 729,q = 243) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 729,q = 243) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 600,q = 400) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 600,q = 400) == 0: {e}')
    
    total += 1
    try:
        result = candidate(p = 450,q = 113) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 450,q = 113) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 600,q = 200) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 600,q = 200) == 1: {e}')
    
    total += 1
    try:
        result = candidate(p = 800,q = 150) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 800,q = 150) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 256,q = 128) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 256,q = 128) == 2: {e}')
    
    total += 1
    try:
        result = candidate(p = 256,q = 93) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(p = 256,q = 93) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(p = 2,q = 1) == 2
    assert candidate(p = 10,q = 3) == 2
    assert candidate(p = 6,q = 2) == 1
    assert candidate(p = 4,q = 2) == 2
    assert candidate(p = 10,q = 4) == 0
    assert candidate(p = 5,q = 3) == 1
    assert candidate(p = 3,q = 1) == 1
    assert candidate(p = 7,q = 5) == 1
    assert candidate(p = 5,q = 2) == 0
    assert candidate(p = 6,q = 4) == 0
    assert candidate(p = 10,q = 7) == 2
    assert candidate(p = 72,q = 27) == 2
    assert candidate(p = 75,q = 33) == 1
    assert candidate(p = 500,q = 250) == 2
    assert candidate(p = 720,q = 180) == 2
    assert candidate(p = 999,q = 499) == 1
    assert candidate(p = 999,q = 333) == 1
    assert candidate(p = 999,q = 1) == 1
    assert candidate(p = 997,q = 333) == 1
    assert candidate(p = 450,q = 135) == 2
    assert candidate(p = 500,q = 200) == 0
    assert candidate(p = 500,q = 249) == 2
    assert candidate(p = 64,q = 15) == 2
    assert candidate(p = 999,q = 421) == 1
    assert candidate(p = 1000,q = 333) == 2
    assert candidate(p = 123,q = 45) == 1
    assert candidate(p = 640,q = 160) == 2
    assert candidate(p = 100,q = 37) == 2
    assert candidate(p = 999,q = 998) == 0
    assert candidate(p = 888,q = 352) == 0
    assert candidate(p = 100,q = 33) == 2
    assert candidate(p = 667,q = 222) == 0
    assert candidate(p = 600,q = 150) == 2
    assert candidate(p = 1000,q = 500) == 2
    assert candidate(p = 300,q = 220) == 1
    assert candidate(p = 85,q = 21) == 1
    assert candidate(p = 199,q = 71) == 1
    assert candidate(p = 987,q = 123) == 1
    assert candidate(p = 500,q = 450) == 2
    assert candidate(p = 800,q = 300) == 2
    assert candidate(p = 97,q = 42) == 0
    assert candidate(p = 550,q = 110) == 1
    assert candidate(p = 999,q = 999) == 1
    assert candidate(p = 360,q = 121) == 2
    assert candidate(p = 81,q = 27) == 1
    assert candidate(p = 777,q = 388) == 0
    assert candidate(p = 600,q = 161) == 2
    assert candidate(p = 720,q = 199) == 2
    assert candidate(p = 625,q = 125) == 1
    assert candidate(p = 997,q = 1) == 1
    assert candidate(p = 400,q = 100) == 2
    assert candidate(p = 45,q = 18) == 0
    assert candidate(p = 725,q = 297) == 1
    assert candidate(p = 750,q = 250) == 1
    assert candidate(p = 20,q = 3) == 2
    assert candidate(p = 501,q = 167) == 1
    assert candidate(p = 880,q = 198) == 2
    assert candidate(p = 450,q = 125) == 2
    assert candidate(p = 777,q = 333) == 1
    assert candidate(p = 120,q = 49) == 2
    assert candidate(p = 450,q = 225) == 2
    assert candidate(p = 450,q = 181) == 2
    assert candidate(p = 25,q = 15) == 1
    assert candidate(p = 999,q = 777) == 1
    assert candidate(p = 450,q = 150) == 1
    assert candidate(p = 15,q = 6) == 0
    assert candidate(p = 50,q = 12) == 0
    assert candidate(p = 700,q = 175) == 2
    assert candidate(p = 555,q = 111) == 1
    assert candidate(p = 819,q = 273) == 1
    assert candidate(p = 256,q = 192) == 2
    assert candidate(p = 100,q = 1) == 2
    assert candidate(p = 80,q = 21) == 2
    assert candidate(p = 99,q = 66) == 0
    assert candidate(p = 576,q = 384) == 0
    assert candidate(p = 200,q = 77) == 2
    assert candidate(p = 500,q = 125) == 2
    assert candidate(p = 729,q = 243) == 1
    assert candidate(p = 600,q = 400) == 0
    assert candidate(p = 450,q = 113) == 2
    assert candidate(p = 600,q = 200) == 1
    assert candidate(p = 800,q = 150) == 2
    assert candidate(p = 256,q = 128) == 2
    assert candidate(p = 256,q = 93) == 2


