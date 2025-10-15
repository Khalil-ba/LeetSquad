def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 789,b = 890) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 789,b = 890) == 74: {e}')
    
    total += 1
    try:
        result = candidate(a = 300,b = 400) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 300,b = 400) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 150) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 150) == 33: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 200) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 200) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 59) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 59) == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = 9,b = 19) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 9,b = 19) == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = 750,b = 780) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 750,b = 780) == 17: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(a = 333,b = 444) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 333,b = 444) == 80: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 300) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 300) == 144: {e}')
    
    total += 1
    try:
        result = candidate(a = 450,b = 455) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 450,b = 455) == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1000) == 738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1000) == 738: {e}')
    
    total += 1
    try:
        result = candidate(a = 80,b = 120) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 80,b = 120) == 27: {e}')
    
    total += 1
    try:
        result = candidate(a = 200,b = 300) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 200,b = 300) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 100) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 100) == 81: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 150) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 150) == 24: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = 600) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = 600) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 456) == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 456) == 244: {e}')
    
    total += 1
    try:
        result = candidate(a = 990,b = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 990,b = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 234,b = 324) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 234,b = 324) == 73: {e}')
    
    total += 1
    try:
        result = candidate(a = 890,b = 987) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 890,b = 987) == 80: {e}')
    
    total += 1
    try:
        result = candidate(a = 900,b = 990) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 900,b = 990) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 99,b = 1000) == 648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99,b = 1000) == 648: {e}')
    
    total += 1
    try:
        result = candidate(a = 800,b = 899) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 800,b = 899) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 200,b = 500) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 200,b = 500) == 216: {e}')
    
    total += 1
    try:
        result = candidate(a = 654,b = 678) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 654,b = 678) == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = 890,b = 899) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 890,b = 899) == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = 999,b = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 999,b = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 567,b = 765) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 567,b = 765) == 153: {e}')
    
    total += 1
    try:
        result = candidate(a = 345,b = 355) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 345,b = 355) == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = 300,b = 399) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 300,b = 399) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 345,b = 543) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 345,b = 543) == 153: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 100) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 100) == 90: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 150) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 150) == 78: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 110) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 110) == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = 400,b = 500) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 400,b = 500) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 111,b = 1111) == 696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 111,b = 1111) == 696: {e}')
    
    total += 1
    try:
        result = candidate(a = 110,b = 120) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 110,b = 120) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 111,b = 111) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 111,b = 111) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 111,b = 222) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 111,b = 222) == 80: {e}')
    
    total += 1
    try:
        result = candidate(a = 300,b = 333) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 300,b = 333) == 24: {e}')
    
    total += 1
    try:
        result = candidate(a = 333,b = 666) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 333,b = 666) == 240: {e}')
    
    total += 1
    try:
        result = candidate(a = 456,b = 654) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 456,b = 654) == 153: {e}')
    
    total += 1
    try:
        result = candidate(a = 300,b = 303) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 300,b = 303) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = 550) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = 550) == 40: {e}')
    
    total += 1
    try:
        result = candidate(a = 987,b = 1087) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 987,b = 1087) == 49: {e}')
    
    total += 1
    try:
        result = candidate(a = 987,b = 1023) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 987,b = 1023) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = 599) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = 599) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 678,b = 876) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 678,b = 876) == 153: {e}')
    
    total += 1
    try:
        result = candidate(a = 888,b = 899) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 888,b = 899) == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = 888,b = 999) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 888,b = 999) == 80: {e}')
    
    total += 1
    try:
        result = candidate(a = 110,b = 110) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 110,b = 110) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 234,b = 432) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 234,b = 432) == 153: {e}')
    
    total += 1
    try:
        result = candidate(a = 789,b = 987) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 789,b = 987) == 153: {e}')
    
    total += 1
    try:
        result = candidate(a = 111,b = 123) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 111,b = 123) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 987,b = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 987,b = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 899,b = 999) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 899,b = 999) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 111,b = 999) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 111,b = 999) == 640: {e}')
    
    total += 1
    try:
        result = candidate(a = 150,b = 350) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 150,b = 350) == 145: {e}')
    
    total += 1
    try:
        result = candidate(a = 600,b = 699) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 600,b = 699) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 678,b = 789) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 678,b = 789) == 82: {e}')
    
    total += 1
    try:
        result = candidate(a = 56,b = 560) == 369
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 56,b = 560) == 369: {e}')
    
    total += 1
    try:
        result = candidate(a = 101,b = 1010) == 648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 101,b = 1010) == 648: {e}')
    
    total += 1
    try:
        result = candidate(a = 600,b = 900) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 600,b = 900) == 216: {e}')
    
    total += 1
    try:
        result = candidate(a = 400,b = 499) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 400,b = 499) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 400,b = 444) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 400,b = 444) == 32: {e}')
    
    total += 1
    try:
        result = candidate(a = 99,b = 101) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99,b = 101) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 444,b = 777) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 444,b = 777) == 240: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 123) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 123) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 200,b = 299) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 200,b = 299) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 700,b = 799) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 700,b = 799) == 72: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 133) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 133) == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000,b = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000,b = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = 1234,b = 1234) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1234,b = 1234) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 345,b = 345) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 345,b = 345) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 900) == 576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 900) == 576: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 321) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 321) == 153: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 789,b = 890) == 74
    assert candidate(a = 300,b = 400) == 72
    assert candidate(a = 100,b = 150) == 33
    assert candidate(a = 100,b = 200) == 72
    assert candidate(a = 50,b = 59) == 9
    assert candidate(a = 9,b = 19) == 10
    assert candidate(a = 750,b = 780) == 17
    assert candidate(a = 1,b = 20) == 19
    assert candidate(a = 333,b = 444) == 80
    assert candidate(a = 100,b = 300) == 144
    assert candidate(a = 450,b = 455) == 4
    assert candidate(a = 1,b = 1000) == 738
    assert candidate(a = 80,b = 120) == 27
    assert candidate(a = 200,b = 300) == 72
    assert candidate(a = 10,b = 100) == 81
    assert candidate(a = 123,b = 150) == 24
    assert candidate(a = 500,b = 600) == 72
    assert candidate(a = 123,b = 456) == 244
    assert candidate(a = 990,b = 1000) == 0
    assert candidate(a = 234,b = 324) == 73
    assert candidate(a = 890,b = 987) == 80
    assert candidate(a = 900,b = 990) == 72
    assert candidate(a = 99,b = 1000) == 648
    assert candidate(a = 800,b = 899) == 72
    assert candidate(a = 200,b = 500) == 216
    assert candidate(a = 654,b = 678) == 11
    assert candidate(a = 890,b = 899) == 8
    assert candidate(a = 999,b = 1000) == 0
    assert candidate(a = 100,b = 100) == 0
    assert candidate(a = 567,b = 765) == 153
    assert candidate(a = 345,b = 355) == 9
    assert candidate(a = 300,b = 399) == 72
    assert candidate(a = 345,b = 543) == 153
    assert candidate(a = 1,b = 100) == 90
    assert candidate(a = 50,b = 150) == 78
    assert candidate(a = 100,b = 110) == 8
    assert candidate(a = 400,b = 500) == 72
    assert candidate(a = 111,b = 1111) == 696
    assert candidate(a = 110,b = 120) == 1
    assert candidate(a = 111,b = 111) == 0
    assert candidate(a = 111,b = 222) == 80
    assert candidate(a = 300,b = 333) == 24
    assert candidate(a = 333,b = 666) == 240
    assert candidate(a = 456,b = 654) == 153
    assert candidate(a = 300,b = 303) == 2
    assert candidate(a = 500,b = 550) == 40
    assert candidate(a = 987,b = 1087) == 49
    assert candidate(a = 987,b = 1023) == 2
    assert candidate(a = 500,b = 599) == 72
    assert candidate(a = 678,b = 876) == 153
    assert candidate(a = 888,b = 899) == 8
    assert candidate(a = 888,b = 999) == 80
    assert candidate(a = 110,b = 110) == 0
    assert candidate(a = 234,b = 432) == 153
    assert candidate(a = 789,b = 987) == 153
    assert candidate(a = 111,b = 123) == 2
    assert candidate(a = 987,b = 999) == 1
    assert candidate(a = 899,b = 999) == 72
    assert candidate(a = 111,b = 999) == 640
    assert candidate(a = 150,b = 350) == 145
    assert candidate(a = 600,b = 699) == 72
    assert candidate(a = 678,b = 789) == 82
    assert candidate(a = 56,b = 560) == 369
    assert candidate(a = 101,b = 1010) == 648
    assert candidate(a = 600,b = 900) == 216
    assert candidate(a = 400,b = 499) == 72
    assert candidate(a = 400,b = 444) == 32
    assert candidate(a = 99,b = 101) == 0
    assert candidate(a = 444,b = 777) == 240
    assert candidate(a = 123,b = 123) == 1
    assert candidate(a = 200,b = 299) == 72
    assert candidate(a = 700,b = 799) == 72
    assert candidate(a = 123,b = 133) == 9
    assert candidate(a = 1000,b = 1000) == 0
    assert candidate(a = 1234,b = 1234) == 1
    assert candidate(a = 345,b = 345) == 1
    assert candidate(a = 100,b = 900) == 576
    assert candidate(a = 123,b = 321) == 153


