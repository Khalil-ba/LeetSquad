def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 13,k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,k = 50000) == 54998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,k = 50000) == 54998: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 100000) == 189998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 100000) == 189998: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 150) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 150) == 53: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 100) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 100) == 188: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,k = 500000000) == 549999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,k = 500000000) == 549999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 999) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 999) == 999: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999,k = 50000) == 54999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999,k = 50000) == 54999: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,k = 100000000) == 189999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,k = 100000000) == 189999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,k = 123456789) == 211111103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,k = 123456789) == 211111103: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,k = 999999999) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,k = 999999999) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 50) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 50) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,k = 9876) == 9887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,k = 9876) == 9887: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765,k = 87654) == 88888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765,k = 87654) == 88888: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111,k = 55555555) == 49999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111,k = 55555555) == 49999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999990,k = 500000000) == 549999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999990,k = 500000000) == 549999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,k = 456789012) == 511110104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,k = 456789012) == 511110104: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,k = 123456789) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,k = 123456789) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,k = 500000000) == 549999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,k = 500000000) == 549999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333,k = 111111111) == 199999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333,k = 111111111) == 199999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 897654321,k = 123456789) == 211111103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897654321,k = 123456789) == 211111103: {e}')
    
    total += 1
    try:
        result = candidate(n = 456789123,k = 222222222) == 299999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789123,k = 222222222) == 299999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,k = 987654320) == 99999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,k = 987654320) == 99999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 700000000,k = 700000000) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700000000,k = 700000000) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777777,k = 333333333) == 399999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777777,k = 333333333) == 399999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111,k = 33333333) == 29999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111,k = 33333333) == 29999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,k = 150000000) == 54999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,k = 150000000) == 54999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 323: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,k = 5000) == 5498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,k = 5000) == 5498: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777777,k = 222222222) == 299999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777777,k = 222222222) == 299999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999998,k = 999999998) == 999999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999998,k = 999999998) == 999999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,k = 300000000) == 369999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,k = 300000000) == 369999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210,k = 123456789) == 211111103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210,k = 123456789) == 211111103: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,k = 123456789) == 211111103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,k = 123456789) == 211111103: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999990,k = 999999990) == 999999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999990,k = 999999990) == 999999990: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,k = 1073741823) == 1966367637
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,k = 1073741823) == 1966367637: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 666666666,k = 333333333) == 399999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666666666,k = 333333333) == 399999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,k = 98765432) == 77777776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,k = 98765432) == 77777776: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765,k = 45678) == 51107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765,k = 45678) == 51107: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,k = 1000) == 1898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,k = 1000) == 1898: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,k = 250000000) == 324999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,k = 250000000) == 324999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,k = 9999) == 9998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,k = 9999) == 9998: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 499) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 499) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,k = 123456789) == 211111102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,k = 123456789) == 211111102: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210,k = 543210987) == 588889887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210,k = 543210987) == 588889887: {e}')
    
    total += 1
    try:
        result = candidate(n = 400000000,k = 200000000) == 279999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000000,k = 200000000) == 279999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,k = 500000000) == 549999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,k = 500000000) == 549999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210,k = 432109876) == 488898887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210,k = 432109876) == 488898887: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,k = 99999999) == 99999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,k = 99999999) == 99999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,k = 123456789) == 211111103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,k = 123456789) == 211111103: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555,k = 277777777) == 349999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555,k = 277777777) == 349999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,k = 87654321) == 178888887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,k = 87654321) == 178888887: {e}')
    
    total += 1
    try:
        result = candidate(n = 87654321,k = 5000000) == 14499998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87654321,k = 5000000) == 14499998: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 1000000) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 1000000) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888,k = 444444444) == 499999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888,k = 444444444) == 499999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210,k = 345678901) == 411111004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210,k = 345678901) == 411111004: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999,k = 50000000) == 54999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999,k = 50000000) == 54999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,k = 999999998) == 999999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,k = 999999998) == 999999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333,k = 166666666) == 249999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333,k = 166666666) == 249999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,k = 999999) == 788887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,k = 999999) == 788887: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,k = 10000000) == 18999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,k = 10000000) == 18999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,k = 50000000) == 54999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,k = 50000000) == 54999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,k = 99999) == 99998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,k = 99999) == 99998: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 500) == 548
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 500) == 548: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,k = 345678) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,k = 345678) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,k = 67890123) == 49989999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,k = 67890123) == 49989999: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999,k = 500000) == 549999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999,k = 500000) == 549999: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,k = 400000000) == 459999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,k = 400000000) == 459999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,k = 678901) == 499899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,k = 678901) == 499899: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,k = 100000000) == 189999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,k = 100000000) == 189999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,k = 75000) == 77498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,k = 75000) == 77498: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,k = 1000000000) == 1899999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,k = 1000000000) == 1899999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,k = 150000000) == 234999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,k = 150000000) == 234999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 900000000,k = 800000000) == 819999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900000000,k = 800000000) == 819999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,k = 100000000) == 189999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,k = 100000000) == 189999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 899999999,k = 500000000) == 549999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899999999,k = 500000000) == 549999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 999999) == 999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 999999) == 999998: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765,k = 12345) == 21107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765,k = 12345) == 21107: {e}')
    
    total += 1
    try:
        result = candidate(n = 234567890,k = 123456789) == 211111103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234567890,k = 123456789) == 211111103: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,k = 1500000000) == 417264712
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,k = 1500000000) == 417264712: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,k = 300000000) == 369999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,k = 300000000) == 369999999: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 13,k = 2) == 10
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 100000,k = 50000) == 54998
    assert candidate(n = 10,k = 10) == 9
    assert candidate(n = 1000000,k = 100000) == 189998
    assert candidate(n = 200,k = 150) == 53
    assert candidate(n = 10,k = 1) == 1
    assert candidate(n = 1000,k = 100) == 188
    assert candidate(n = 999999999,k = 500000000) == 549999999
    assert candidate(n = 999,k = 999) == 999
    assert candidate(n = 99999,k = 50000) == 54999
    assert candidate(n = 2,k = 1) == 1
    assert candidate(n = 100,k = 10) == 17
    assert candidate(n = 1000000000,k = 100000000) == 189999998
    assert candidate(n = 20,k = 15) == 4
    assert candidate(n = 999999999,k = 123456789) == 211111103
    assert candidate(n = 999999999,k = 999999999) == 999999999
    assert candidate(n = 1000,k = 50) == 142
    assert candidate(n = 50,k = 25) == 31
    assert candidate(n = 10000,k = 9876) == 9887
    assert candidate(n = 98765,k = 87654) == 88888
    assert candidate(n = 111111111,k = 55555555) == 49999998
    assert candidate(n = 999999990,k = 500000000) == 549999999
    assert candidate(n = 987654321,k = 456789012) == 511110104
    assert candidate(n = 123456789,k = 123456789) == 99999999
    assert candidate(n = 1000000000,k = 500000000) == 549999998
    assert candidate(n = 1000000000,k = 1) == 1
    assert candidate(n = 333333333,k = 111111111) == 199999999
    assert candidate(n = 897654321,k = 123456789) == 211111103
    assert candidate(n = 456789123,k = 222222222) == 299999999
    assert candidate(n = 999999999,k = 1) == 1
    assert candidate(n = 987654321,k = 987654320) == 99999998
    assert candidate(n = 700000000,k = 700000000) == 99999999
    assert candidate(n = 777777777,k = 333333333) == 399999999
    assert candidate(n = 111111111,k = 33333333) == 29999998
    assert candidate(n = 200000000,k = 150000000) == 54999998
    assert candidate(n = 500,k = 250) == 323
    assert candidate(n = 500000000,k = 1) == 1
    assert candidate(n = 123456789,k = 1) == 1
    assert candidate(n = 10000,k = 5000) == 5498
    assert candidate(n = 777777777,k = 222222222) == 299999999
    assert candidate(n = 999999998,k = 999999998) == 999999998
    assert candidate(n = 500000000,k = 300000000) == 369999999
    assert candidate(n = 876543210,k = 123456789) == 211111103
    assert candidate(n = 987654321,k = 123456789) == 211111103
    assert candidate(n = 999999990,k = 999999990) == 999999990
    assert candidate(n = 2147483647,k = 1073741823) == 1966367637
    assert candidate(n = 500,k = 1) == 1
    assert candidate(n = 666666666,k = 333333333) == 399999999
    assert candidate(n = 123456789,k = 98765432) == 77777776
    assert candidate(n = 98765,k = 45678) == 51107
    assert candidate(n = 10000,k = 1000) == 1898
    assert candidate(n = 500000000,k = 250000000) == 324999998
    assert candidate(n = 10000,k = 9999) == 9998
    assert candidate(n = 500,k = 499) == 98
    assert candidate(n = 1000000000,k = 123456789) == 211111102
    assert candidate(n = 876543210,k = 543210987) == 588889887
    assert candidate(n = 400000000,k = 200000000) == 279999999
    assert candidate(n = 600000000,k = 500000000) == 549999999
    assert candidate(n = 876543210,k = 432109876) == 488898887
    assert candidate(n = 100000000,k = 99999999) == 99999998
    assert candidate(n = 800000000,k = 123456789) == 211111103
    assert candidate(n = 555555555,k = 277777777) == 349999998
    assert candidate(n = 987654321,k = 87654321) == 178888887
    assert candidate(n = 87654321,k = 5000000) == 14499998
    assert candidate(n = 1000000,k = 1000000) == 999999
    assert candidate(n = 888888888,k = 444444444) == 499999999
    assert candidate(n = 876543210,k = 345678901) == 411111004
    assert candidate(n = 987654321,k = 1) == 1
    assert candidate(n = 99999999,k = 50000000) == 54999999
    assert candidate(n = 999999999,k = 999999998) == 999999998
    assert candidate(n = 333333333,k = 166666666) == 249999998
    assert candidate(n = 1234567,k = 999999) == 788887
    assert candidate(n = 100000000,k = 10000000) == 18999998
    assert candidate(n = 100000000,k = 50000000) == 54999998
    assert candidate(n = 100000,k = 99999) == 99998
    assert candidate(n = 1000,k = 500) == 548
    assert candidate(n = 1234567,k = 345678) == 199998
    assert candidate(n = 123456789,k = 67890123) == 49989999
    assert candidate(n = 999999,k = 500000) == 549999
    assert candidate(n = 800000000,k = 400000000) == 459999999
    assert candidate(n = 1234567,k = 678901) == 499899
    assert candidate(n = 200000000,k = 100000000) == 189999999
    assert candidate(n = 100000,k = 75000) == 77498
    assert candidate(n = 2147483647,k = 1000000000) == 1899999999
    assert candidate(n = 300000000,k = 150000000) == 234999998
    assert candidate(n = 900000000,k = 800000000) == 819999999
    assert candidate(n = 300000000,k = 100000000) == 189999999
    assert candidate(n = 899999999,k = 500000000) == 549999999
    assert candidate(n = 1000000,k = 999999) == 999998
    assert candidate(n = 98765,k = 12345) == 21107
    assert candidate(n = 234567890,k = 123456789) == 211111103
    assert candidate(n = 2147483647,k = 1500000000) == 417264712
    assert candidate(n = 600000000,k = 300000000) == 369999999


