def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(lowLimit = 999,highLimit = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 999,highLimit = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1000,highLimit = 10000) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1000,highLimit = 10000) == 615: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 50000,highLimit = 50500) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 50000,highLimit = 50500) == 44: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99,highLimit = 999) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99,highLimit = 999) == 70: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 500,highLimit = 550) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 500,highLimit = 550) == 6: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 9999,highLimit = 100000) == 5520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 9999,highLimit = 100000) == 5520: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1,highLimit = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1,highLimit = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 100,highLimit = 200) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 100,highLimit = 200) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99,highLimit = 199) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99,highLimit = 199) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1,highLimit = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1,highLimit = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1,highLimit = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1,highLimit = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 10,highLimit = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 10,highLimit = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 50,highLimit = 150) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 50,highLimit = 150) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 5,highLimit = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 5,highLimit = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 19,highLimit = 28) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 19,highLimit = 28) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 45678,highLimit = 98765) == 3544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 45678,highLimit = 98765) == 3544: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 40000,highLimit = 50000) == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 40000,highLimit = 50000) == 670: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 10000,highLimit = 20000) == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 10000,highLimit = 20000) == 670: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 33333,highLimit = 44444) == 782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 33333,highLimit = 44444) == 782: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 67890,highLimit = 67990) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 67890,highLimit = 67990) == 11: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 54321,highLimit = 54421) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 54321,highLimit = 54421) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 88888,highLimit = 88988) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 88888,highLimit = 88988) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 100,highLimit = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 100,highLimit = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99999,highLimit = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99999,highLimit = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 9995,highLimit = 10005) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 9995,highLimit = 10005) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 43210,highLimit = 43250) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 43210,highLimit = 43250) == 5: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99995,highLimit = 100005) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99995,highLimit = 100005) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 30000,highLimit = 35000) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 30000,highLimit = 35000) == 365: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 98765,highLimit = 98865) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 98765,highLimit = 98865) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 54321,highLimit = 54341) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 54321,highLimit = 54341) == 3: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 11111,highLimit = 11115) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 11111,highLimit = 11115) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 10000,highLimit = 99999) == 5520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 10000,highLimit = 99999) == 5520: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 66666,highLimit = 66766) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 66666,highLimit = 66766) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 77777,highLimit = 77800) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 77777,highLimit = 77800) == 3: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99990,highLimit = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99990,highLimit = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 11111,highLimit = 11200) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 11111,highLimit = 11200) == 9: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 5000,highLimit = 6000) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 5000,highLimit = 6000) == 75: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 56789,highLimit = 56800) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 56789,highLimit = 56800) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 55555,highLimit = 66666) == 782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 55555,highLimit = 66666) == 782: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 9990,highLimit = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 9990,highLimit = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 12345,highLimit = 54321) == 2854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 12345,highLimit = 54321) == 2854: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 50000,highLimit = 50100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 50000,highLimit = 50100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 23456,highLimit = 23460) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 23456,highLimit = 23460) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 500,highLimit = 5000) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 500,highLimit = 5000) == 340: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 5000,highLimit = 5100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 5000,highLimit = 5100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 90000,highLimit = 95000) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 90000,highLimit = 95000) == 365: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 10000,highLimit = 100000) == 5520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 10000,highLimit = 100000) == 5520: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 9999,highLimit = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 9999,highLimit = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 999,highLimit = 1009) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 999,highLimit = 1009) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 12345,highLimit = 12395) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 12345,highLimit = 12395) == 6: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1,highLimit = 99999) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1,highLimit = 99999) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 12345,highLimit = 12345) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 12345,highLimit = 12345) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1,highLimit = 1000) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1,highLimit = 1000) == 75: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 22222,highLimit = 22322) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 22222,highLimit = 22322) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 12345,highLimit = 67890) == 3699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 12345,highLimit = 67890) == 3699: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 56789,highLimit = 56799) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 56789,highLimit = 56799) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 100,highLimit = 1000) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 100,highLimit = 1000) == 70: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 11111,highLimit = 22222) == 754
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 11111,highLimit = 22222) == 754: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 77777,highLimit = 77877) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 77777,highLimit = 77877) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 100000,highLimit = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 100000,highLimit = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 250,highLimit = 750) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 250,highLimit = 750) == 46: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 30000,highLimit = 40000) == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 30000,highLimit = 40000) == 670: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99900,highLimit = 100100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99900,highLimit = 100100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 100000,highLimit = 100050) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 100000,highLimit = 100050) == 6: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 12345,highLimit = 12445) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 12345,highLimit = 12445) == 11: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 5000,highLimit = 5050) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 5000,highLimit = 5050) == 6: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 995,highLimit = 1005) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 995,highLimit = 1005) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1000,highLimit = 1050) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1000,highLimit = 1050) == 6: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 33333,highLimit = 33433) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 33333,highLimit = 33433) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1234,highLimit = 5678) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1234,highLimit = 5678) == 344: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 8888,highLimit = 8900) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 8888,highLimit = 8900) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 11111,highLimit = 11211) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 11111,highLimit = 11211) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 999,highLimit = 1001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 999,highLimit = 1001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 67890,highLimit = 78900) == 749
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 67890,highLimit = 78900) == 749: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 20000,highLimit = 30000) == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 20000,highLimit = 30000) == 670: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 50000,highLimit = 51000) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 50000,highLimit = 51000) == 75: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 99,highLimit = 101) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 99,highLimit = 101) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 88888,highLimit = 99999) == 736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 88888,highLimit = 99999) == 736: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 1234,highLimit = 1244) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 1234,highLimit = 1244) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 44444,highLimit = 55555) == 785
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 44444,highLimit = 55555) == 785: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 300,highLimit = 600) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 300,highLimit = 600) == 28: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 12345,highLimit = 12355) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 12345,highLimit = 12355) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 70000,highLimit = 80000) == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 70000,highLimit = 80000) == 670: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 88888,highLimit = 88999) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 88888,highLimit = 88999) == 11: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 20000,highLimit = 25000) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 20000,highLimit = 25000) == 365: {e}')
    
    total += 1
    try:
        result = candidate(lowLimit = 123,highLimit = 456) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lowLimit = 123,highLimit = 456) == 33: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(lowLimit = 999,highLimit = 1000) == 1
    assert candidate(lowLimit = 1000,highLimit = 10000) == 615
    assert candidate(lowLimit = 50000,highLimit = 50500) == 44
    assert candidate(lowLimit = 99,highLimit = 999) == 70
    assert candidate(lowLimit = 500,highLimit = 550) == 6
    assert candidate(lowLimit = 9999,highLimit = 100000) == 5520
    assert candidate(lowLimit = 1,highLimit = 10) == 2
    assert candidate(lowLimit = 100,highLimit = 200) == 10
    assert candidate(lowLimit = 99,highLimit = 199) == 10
    assert candidate(lowLimit = 1,highLimit = 100) == 10
    assert candidate(lowLimit = 1,highLimit = 20) == 3
    assert candidate(lowLimit = 10,highLimit = 100) == 9
    assert candidate(lowLimit = 50,highLimit = 150) == 10
    assert candidate(lowLimit = 5,highLimit = 15) == 2
    assert candidate(lowLimit = 19,highLimit = 28) == 2
    assert candidate(lowLimit = 45678,highLimit = 98765) == 3544
    assert candidate(lowLimit = 40000,highLimit = 50000) == 670
    assert candidate(lowLimit = 10000,highLimit = 20000) == 670
    assert candidate(lowLimit = 33333,highLimit = 44444) == 782
    assert candidate(lowLimit = 67890,highLimit = 67990) == 11
    assert candidate(lowLimit = 54321,highLimit = 54421) == 10
    assert candidate(lowLimit = 88888,highLimit = 88988) == 10
    assert candidate(lowLimit = 100,highLimit = 100) == 1
    assert candidate(lowLimit = 99999,highLimit = 100000) == 1
    assert candidate(lowLimit = 9995,highLimit = 10005) == 1
    assert candidate(lowLimit = 43210,highLimit = 43250) == 5
    assert candidate(lowLimit = 99995,highLimit = 100005) == 1
    assert candidate(lowLimit = 30000,highLimit = 35000) == 365
    assert candidate(lowLimit = 98765,highLimit = 98865) == 10
    assert candidate(lowLimit = 54321,highLimit = 54341) == 3
    assert candidate(lowLimit = 11111,highLimit = 11115) == 1
    assert candidate(lowLimit = 10000,highLimit = 99999) == 5520
    assert candidate(lowLimit = 66666,highLimit = 66766) == 10
    assert candidate(lowLimit = 77777,highLimit = 77800) == 3
    assert candidate(lowLimit = 99990,highLimit = 100000) == 1
    assert candidate(lowLimit = 11111,highLimit = 11200) == 9
    assert candidate(lowLimit = 5000,highLimit = 6000) == 75
    assert candidate(lowLimit = 56789,highLimit = 56800) == 2
    assert candidate(lowLimit = 55555,highLimit = 66666) == 782
    assert candidate(lowLimit = 9990,highLimit = 10000) == 1
    assert candidate(lowLimit = 12345,highLimit = 54321) == 2854
    assert candidate(lowLimit = 50000,highLimit = 50100) == 10
    assert candidate(lowLimit = 23456,highLimit = 23460) == 1
    assert candidate(lowLimit = 500,highLimit = 5000) == 340
    assert candidate(lowLimit = 5000,highLimit = 5100) == 10
    assert candidate(lowLimit = 90000,highLimit = 95000) == 365
    assert candidate(lowLimit = 10000,highLimit = 100000) == 5520
    assert candidate(lowLimit = 9999,highLimit = 10000) == 1
    assert candidate(lowLimit = 999,highLimit = 1009) == 1
    assert candidate(lowLimit = 12345,highLimit = 12395) == 6
    assert candidate(lowLimit = 1,highLimit = 99999) == 6000
    assert candidate(lowLimit = 12345,highLimit = 12345) == 1
    assert candidate(lowLimit = 1,highLimit = 1000) == 75
    assert candidate(lowLimit = 22222,highLimit = 22322) == 10
    assert candidate(lowLimit = 12345,highLimit = 67890) == 3699
    assert candidate(lowLimit = 56789,highLimit = 56799) == 2
    assert candidate(lowLimit = 100,highLimit = 1000) == 70
    assert candidate(lowLimit = 11111,highLimit = 22222) == 754
    assert candidate(lowLimit = 77777,highLimit = 77877) == 10
    assert candidate(lowLimit = 100000,highLimit = 100000) == 1
    assert candidate(lowLimit = 250,highLimit = 750) == 46
    assert candidate(lowLimit = 30000,highLimit = 40000) == 670
    assert candidate(lowLimit = 99900,highLimit = 100100) == 10
    assert candidate(lowLimit = 100000,highLimit = 100050) == 6
    assert candidate(lowLimit = 12345,highLimit = 12445) == 11
    assert candidate(lowLimit = 5000,highLimit = 5050) == 6
    assert candidate(lowLimit = 995,highLimit = 1005) == 1
    assert candidate(lowLimit = 1000,highLimit = 1050) == 6
    assert candidate(lowLimit = 33333,highLimit = 33433) == 10
    assert candidate(lowLimit = 1234,highLimit = 5678) == 344
    assert candidate(lowLimit = 8888,highLimit = 8900) == 2
    assert candidate(lowLimit = 11111,highLimit = 11211) == 10
    assert candidate(lowLimit = 999,highLimit = 1001) == 1
    assert candidate(lowLimit = 67890,highLimit = 78900) == 749
    assert candidate(lowLimit = 20000,highLimit = 30000) == 670
    assert candidate(lowLimit = 50000,highLimit = 51000) == 75
    assert candidate(lowLimit = 99,highLimit = 101) == 1
    assert candidate(lowLimit = 88888,highLimit = 99999) == 736
    assert candidate(lowLimit = 1234,highLimit = 1244) == 2
    assert candidate(lowLimit = 44444,highLimit = 55555) == 785
    assert candidate(lowLimit = 300,highLimit = 600) == 28
    assert candidate(lowLimit = 12345,highLimit = 12355) == 2
    assert candidate(lowLimit = 70000,highLimit = 80000) == 670
    assert candidate(lowLimit = 88888,highLimit = 88999) == 11
    assert candidate(lowLimit = 20000,highLimit = 25000) == 365
    assert candidate(lowLimit = 123,highLimit = 456) == 33


