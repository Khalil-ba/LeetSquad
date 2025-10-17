def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,m = 7) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 7) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 200) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 200) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,m = 100000) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,m = 100000) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000,m = 25000) == 937500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000,m = 25000) == 937500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 11) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 11) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000,m = 75000) == 937500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000,m = 75000) == 937500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 99,m = 101) == 4999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99,m = 101) == 4999: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000,m = 40000) == 600000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000,m = 40000) == 600000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 200000) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 200000) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999,m = 2) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999,m = 2) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,m = 100000) == 2500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,m = 100000) == 2500000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 1000) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 1000) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 33333,m = 66667) == 1111105555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33333,m = 66667) == 1111105555: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 8) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 8) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 33333,m = 66666) == 1111088889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33333,m = 66666) == 1111088889: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000,m = 85000) == 3187500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000,m = 85000) == 3187500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999,m = 99999) == 4999900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999,m = 99999) == 4999900000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,m = 5000) == 25000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,m = 5000) == 25000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999,m = 100000) == 4999950000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999,m = 100000) == 4999950000: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 500) == 125000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 500) == 125000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 25) == 187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 25) == 187: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,m = 50000) == 1250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,m = 50000) == 1250000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 60000,m = 40000) == 1200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60000,m = 40000) == 1200000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000,m = 10000) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000,m = 10000) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,m = 5000) == 12500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,m = 5000) == 12500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 99999) == 49999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 99999) == 49999: {e}')
    
    total += 1
    try:
        result = candidate(n = 55,m = 88) == 2420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55,m = 88) == 2420: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 60) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 60) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 99999) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 99999) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 100000) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 100000) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 200) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 200) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000,m = 20000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000,m = 20000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,m = 1) == 25000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,m = 1) == 25000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 15) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 15) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 500) == 250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 500) == 250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000,m = 1) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000,m = 1) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000,m = 30000) == 300000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000,m = 30000) == 300000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,m = 300) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,m = 300) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,m = 150) == 11250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,m = 150) == 11250: {e}')
    
    total += 1
    try:
        result = candidate(n = 23456,m = 65432) == 767386496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23456,m = 65432) == 767386496: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000,m = 20000) == 300000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000,m = 20000) == 300000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 1500) == 750000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 1500) == 750000: {e}')
    
    total += 1
    try:
        result = candidate(n = 49999,m = 50001) == 1249999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49999,m = 50001) == 1249999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 80000,m = 20000) == 800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80000,m = 20000) == 800000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 30) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 30) == 375: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999,m = 1) == 49999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999,m = 1) == 49999: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,m = 10000) == 50000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,m = 10000) == 50000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345,m = 67890) == 419051025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345,m = 67890) == 419051025: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 15) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 15) == 112: {e}')
    
    total += 1
    try:
        result = candidate(n = 66667,m = 33333) == 1111105555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 66667,m = 33333) == 1111105555: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,m = 1) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,m = 1) == 50000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,m = 7) == 17
    assert candidate(n = 5,m = 4) == 10
    assert candidate(n = 1,m = 1) == 0
    assert candidate(n = 100,m = 200) == 10000
    assert candidate(n = 4,m = 3) == 6
    assert candidate(n = 100000,m = 100000) == 5000000000
    assert candidate(n = 3,m = 2) == 3
    assert candidate(n = 10,m = 10) == 50
    assert candidate(n = 5,m = 5) == 12
    assert candidate(n = 2,m = 2) == 2
    assert candidate(n = 75000,m = 25000) == 937500000
    assert candidate(n = 7,m = 11) == 38
    assert candidate(n = 25000,m = 75000) == 937500000
    assert candidate(n = 99,m = 101) == 4999
    assert candidate(n = 30000,m = 40000) == 600000000
    assert candidate(n = 1,m = 200000) == 100000
    assert candidate(n = 99999,m = 2) == 99999
    assert candidate(n = 50000,m = 100000) == 2500000000
    assert candidate(n = 10,m = 1) == 5
    assert candidate(n = 1000,m = 1000) == 500000
    assert candidate(n = 33333,m = 66667) == 1111105555
    assert candidate(n = 7,m = 8) == 28
    assert candidate(n = 33333,m = 66666) == 1111088889
    assert candidate(n = 75000,m = 85000) == 3187500000
    assert candidate(n = 99999,m = 99999) == 4999900000
    assert candidate(n = 10000,m = 5000) == 25000000
    assert candidate(n = 99999,m = 100000) == 4999950000
    assert candidate(n = 3,m = 3) == 4
    assert candidate(n = 500,m = 500) == 125000
    assert candidate(n = 100,m = 100) == 5000
    assert candidate(n = 15,m = 25) == 187
    assert candidate(n = 50000,m = 50000) == 1250000000
    assert candidate(n = 60000,m = 40000) == 1200000000
    assert candidate(n = 20000,m = 10000) == 100000000
    assert candidate(n = 5000,m = 5000) == 12500000
    assert candidate(n = 1,m = 99999) == 49999
    assert candidate(n = 55,m = 88) == 2420
    assert candidate(n = 1,m = 10) == 5
    assert candidate(n = 20,m = 15) == 150
    assert candidate(n = 50,m = 60) == 1500
    assert candidate(n = 2,m = 99999) == 99999
    assert candidate(n = 1,m = 100000) == 50000
    assert candidate(n = 300,m = 200) == 30000
    assert candidate(n = 20000,m = 20000) == 200000000
    assert candidate(n = 50000,m = 1) == 25000
    assert candidate(n = 10,m = 15) == 75
    assert candidate(n = 50,m = 50) == 1250
    assert candidate(n = 7,m = 5) == 17
    assert candidate(n = 1000,m = 500) == 250000
    assert candidate(n = 200000,m = 1) == 100000
    assert candidate(n = 20000,m = 30000) == 300000000
    assert candidate(n = 200,m = 300) == 30000
    assert candidate(n = 150,m = 150) == 11250
    assert candidate(n = 23456,m = 65432) == 767386496
    assert candidate(n = 30000,m = 20000) == 300000000
    assert candidate(n = 1000,m = 1500) == 750000
    assert candidate(n = 49999,m = 50001) == 1249999999
    assert candidate(n = 2,m = 3) == 3
    assert candidate(n = 80000,m = 20000) == 800000000
    assert candidate(n = 25,m = 30) == 375
    assert candidate(n = 99999,m = 1) == 49999
    assert candidate(n = 10000,m = 10000) == 50000000
    assert candidate(n = 12345,m = 67890) == 419051025
    assert candidate(n = 15,m = 15) == 112
    assert candidate(n = 66667,m = 33333) == 1111105555
    assert candidate(n = 100000,m = 1) == 50000


