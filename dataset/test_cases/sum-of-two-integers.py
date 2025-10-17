def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 1000,b = -1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000,b = -1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -2,b = -3) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -2,b = -3) == -5: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = 500) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = 500) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -5,b = -5) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -5,b = -5) == -10: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = 999,b = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 999,b = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -5,b = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -5,b = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -1000,b = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1000,b = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -500,b = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -500,b = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -500,b = -500) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -500,b = -500) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -1,b = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1,b = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = -999,b = -1) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -999,b = -1) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -7,b = -13) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -7,b = -13) == -20: {e}')
    
    total += 1
    try:
        result = candidate(a = -999,b = 1) == -998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -999,b = 1) == -998: {e}')
    
    total += 1
    try:
        result = candidate(a = -128,b = 256) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -128,b = 256) == 128: {e}')
    
    total += 1
    try:
        result = candidate(a = -999,b = 999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -999,b = 999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 1234,b = -5678) == -4444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1234,b = -5678) == -4444: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 13) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 13) == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = -7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = -7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 256,b = 255) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 256,b = 255) == 511: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = -1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = -1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = -223,b = -777) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -223,b = -777) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -1000,b = -999) == -1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1000,b = -999) == -1999: {e}')
    
    total += 1
    try:
        result = candidate(a = -1234,b = 5678) == 4444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1234,b = 5678) == 4444: {e}')
    
    total += 1
    try:
        result = candidate(a = -123,b = 456) == 333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -123,b = 456) == 333: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = -3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = -3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = 678,b = 322) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 678,b = 322) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = 501) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = 501) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(a = -789,b = 321) == -468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -789,b = 321) == -468: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 999) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 999) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 456,b = 123) == 579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 456,b = 123) == 579: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = -1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = -1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = -13) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = -13) == -6: {e}')
    
    total += 1
    try:
        result = candidate(a = 512,b = -512) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 512,b = -512) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -314,b = 157) == -157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -314,b = 157) == -157: {e}')
    
    total += 1
    try:
        result = candidate(a = 499,b = 500) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 499,b = 500) == 999: {e}')
    
    total += 1
    try:
        result = candidate(a = 256,b = 256) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 256,b = 256) == 512: {e}')
    
    total += 1
    try:
        result = candidate(a = 314,b = -157) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 314,b = -157) == 157: {e}')
    
    total += 1
    try:
        result = candidate(a = 223,b = -777) == -554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 223,b = -777) == -554: {e}')
    
    total += 1
    try:
        result = candidate(a = 1234,b = -1234) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1234,b = -1234) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -1,b = -999) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1,b = -999) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 456,b = -789) == -333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 456,b = -789) == -333: {e}')
    
    total += 1
    try:
        result = candidate(a = 456,b = -234) == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 456,b = -234) == 222: {e}')
    
    total += 1
    try:
        result = candidate(a = -777,b = -223) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -777,b = -223) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -678,b = -322) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -678,b = -322) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 789,b = -321) == 468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 789,b = -321) == 468: {e}')
    
    total += 1
    try:
        result = candidate(a = -333,b = -667) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -333,b = -667) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = -1000) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = -1000) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -7,b = 3) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -7,b = 3) == -4: {e}')
    
    total += 1
    try:
        result = candidate(a = -456,b = -123) == -579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -456,b = -123) == -579: {e}')
    
    total += 1
    try:
        result = candidate(a = -500,b = 250) == -250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -500,b = 250) == -250: {e}')
    
    total += 1
    try:
        result = candidate(a = 345,b = 678) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 345,b = 678) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000,b = 0) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000,b = 0) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -321,b = 654) == 333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -321,b = 654) == 333: {e}')
    
    total += 1
    try:
        result = candidate(a = 333,b = 667) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 333,b = 667) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -256,b = -256) == -512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -256,b = -256) == -512: {e}')
    
    total += 1
    try:
        result = candidate(a = -777,b = 223) == -554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -777,b = 223) == -554: {e}')
    
    total += 1
    try:
        result = candidate(a = -1000,b = 0) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1000,b = 0) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -123,b = -456) == -579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -123,b = -456) == -579: {e}')
    
    total += 1
    try:
        result = candidate(a = -456,b = 123) == -333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -456,b = 123) == -333: {e}')
    
    total += 1
    try:
        result = candidate(a = 777,b = 223) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 777,b = 223) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = -789,b = 456) == -333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -789,b = 456) == -333: {e}')
    
    total += 1
    try:
        result = candidate(a = 63,b = 127) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 63,b = 127) == 190: {e}')
    
    total += 1
    try:
        result = candidate(a = -500,b = -499) == -999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -500,b = -499) == -999: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = -100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = -100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -1,b = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -1,b = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = 999,b = -999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 999,b = -999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000,b = -999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000,b = -999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 456) == 579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 456) == 579: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000,b = 999) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000,b = 999) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = -456) == -333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = -456) == -333: {e}')
    
    total += 1
    try:
        result = candidate(a = -256,b = -255) == -511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -256,b = -255) == -511: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = -250) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = -250) == 250: {e}')
    
    total += 1
    try:
        result = candidate(a = 1024,b = -1024) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1024,b = -1024) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = -7,b = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = -7,b = 13) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 1000,b = -1000) == 0
    assert candidate(a = -2,b = -3) == -5
    assert candidate(a = 0,b = 5) == 5
    assert candidate(a = 500,b = 500) == 1000
    assert candidate(a = -5,b = -5) == -10
    assert candidate(a = 1,b = 2) == 3
    assert candidate(a = 999,b = 1) == 1000
    assert candidate(a = -5,b = 5) == 0
    assert candidate(a = -1000,b = 1000) == 0
    assert candidate(a = -500,b = 500) == 0
    assert candidate(a = -500,b = -500) == -1000
    assert candidate(a = 0,b = 0) == 0
    assert candidate(a = -1,b = 1) == 0
    assert candidate(a = 2,b = 3) == 5
    assert candidate(a = -999,b = -1) == -1000
    assert candidate(a = -7,b = -13) == -20
    assert candidate(a = -999,b = 1) == -998
    assert candidate(a = -128,b = 256) == 128
    assert candidate(a = -999,b = 999) == 0
    assert candidate(a = 1234,b = -5678) == -4444
    assert candidate(a = 7,b = 13) == 20
    assert candidate(a = 7,b = -7) == 0
    assert candidate(a = 256,b = 255) == 511
    assert candidate(a = 0,b = -1) == -1
    assert candidate(a = -223,b = -777) == -1000
    assert candidate(a = -1000,b = -999) == -1999
    assert candidate(a = -1234,b = 5678) == 4444
    assert candidate(a = -123,b = 456) == 333
    assert candidate(a = 1,b = 0) == 1
    assert candidate(a = 7,b = -3) == 4
    assert candidate(a = 678,b = 322) == 1000
    assert candidate(a = 500,b = 501) == 1001
    assert candidate(a = -789,b = 321) == -468
    assert candidate(a = 1,b = 999) == 1000
    assert candidate(a = 456,b = 123) == 579
    assert candidate(a = 1,b = -1) == 0
    assert candidate(a = 7,b = -13) == -6
    assert candidate(a = 512,b = -512) == 0
    assert candidate(a = -314,b = 157) == -157
    assert candidate(a = 499,b = 500) == 999
    assert candidate(a = 256,b = 256) == 512
    assert candidate(a = 314,b = -157) == 157
    assert candidate(a = 223,b = -777) == -554
    assert candidate(a = 1234,b = -1234) == 0
    assert candidate(a = -1,b = -999) == -1000
    assert candidate(a = 456,b = -789) == -333
    assert candidate(a = 456,b = -234) == 222
    assert candidate(a = -777,b = -223) == -1000
    assert candidate(a = -678,b = -322) == -1000
    assert candidate(a = 789,b = -321) == 468
    assert candidate(a = -333,b = -667) == -1000
    assert candidate(a = 0,b = -1000) == -1000
    assert candidate(a = -7,b = 3) == -4
    assert candidate(a = -456,b = -123) == -579
    assert candidate(a = -500,b = 250) == -250
    assert candidate(a = 345,b = 678) == 1023
    assert candidate(a = 1000,b = 0) == 1000
    assert candidate(a = -321,b = 654) == 333
    assert candidate(a = 333,b = 667) == 1000
    assert candidate(a = 0,b = 1000) == 1000
    assert candidate(a = -256,b = -256) == -512
    assert candidate(a = -777,b = 223) == -554
    assert candidate(a = -1000,b = 0) == -1000
    assert candidate(a = -123,b = -456) == -579
    assert candidate(a = -456,b = 123) == -333
    assert candidate(a = 777,b = 223) == 1000
    assert candidate(a = -789,b = 456) == -333
    assert candidate(a = 63,b = 127) == 190
    assert candidate(a = -500,b = -499) == -999
    assert candidate(a = 100,b = -100) == 0
    assert candidate(a = -1,b = 0) == -1
    assert candidate(a = 999,b = -999) == 0
    assert candidate(a = 1000,b = -999) == 1
    assert candidate(a = 123,b = 456) == 579
    assert candidate(a = 1000,b = 999) == 1999
    assert candidate(a = 123,b = -456) == -333
    assert candidate(a = -256,b = -255) == -511
    assert candidate(a = 500,b = -250) == 250
    assert candidate(a = 1024,b = -1024) == 0
    assert candidate(a = -7,b = 13) == 6


