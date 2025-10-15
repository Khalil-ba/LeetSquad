def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,k = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,k = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 30000,k = 10000) == 1358
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 30000,k = 10000) == 1358: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 3,k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 3,k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 6,k = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 6,k = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 30000,k = 100) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 30000,k = 100) == 28: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 30000,k = 15000) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 30000,k = 15000) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1,k = 500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1,k = 500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(m = 12345,n = 6789,k = 5000000) == 906384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12345,n = 6789,k = 5000000) == 906384: {e}')
    
    total += 1
    try:
        result = candidate(m = 12000,n = 12000,k = 71999999) == 26888084
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12000,n = 12000,k = 71999999) == 26888084: {e}')
    
    total += 1
    try:
        result = candidate(m = 9999,n = 9999,k = 99980001) == 99980001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9999,n = 9999,k = 99980001) == 99980001: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10,k = 5000) == 1709
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10,k = 5000) == 1709: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 1,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 1,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(m = 9999,n = 10000,k = 49995000) == 18671202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9999,n = 10000,k = 49995000) == 18671202: {e}')
    
    total += 1
    try:
        result = candidate(m = 5000,n = 5000,k = 12500000) == 4669497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5000,n = 5000,k = 12500000) == 4669497: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10000,k = 5000) == 1709
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10000,k = 5000) == 1709: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 15000,k = 11250000) == 1961750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 15000,k = 11250000) == 1961750: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,k = 50000000) == 18673076
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,k = 50000000) == 18673076: {e}')
    
    total += 1
    try:
        result = candidate(m = 8000,n = 8000,k = 39999999) == 17356893
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8000,n = 8000,k = 39999999) == 17356893: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 9,k = 45) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 9,k = 45) == 27: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 15,k = 45) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 15,k = 45) == 18: {e}')
    
    total += 1
    try:
        result = candidate(m = 25000,n = 25000,k = 6250000) == 821997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25000,n = 25000,k = 6250000) == 821997: {e}')
    
    total += 1
    try:
        result = candidate(m = 5000,n = 20000,k = 1000000) == 132820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5000,n = 20000,k = 1000000) == 132820: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 15000,k = 2000000) == 275724
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 15000,k = 2000000) == 275724: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,k = 99999999) == 99990000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,k = 99999999) == 99990000: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,k = 49) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,k = 49) == 49: {e}')
    
    total += 1
    try:
        result = candidate(m = 12345,n = 67890,k = 4567890) == 553668
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12345,n = 67890,k = 4567890) == 553668: {e}')
    
    total += 1
    try:
        result = candidate(m = 300,n = 100,k = 28000) == 19899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 300,n = 100,k = 28000) == 19899: {e}')
    
    total += 1
    try:
        result = candidate(m = 7500,n = 2500,k = 18749999) == 18747500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7500,n = 2500,k = 18749999) == 18747500: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 30000,k = 2999900) == 617430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 30000,k = 2999900) == 617430: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 1,k = 29999) == 29999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 1,k = 29999) == 29999: {e}')
    
    total += 1
    try:
        result = candidate(m = 200,n = 100,k = 19900) == 18145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 200,n = 100,k = 19900) == 18145: {e}')
    
    total += 1
    try:
        result = candidate(m = 250,n = 250,k = 12500) == 3210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 250,n = 250,k = 12500) == 3210: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 30000,k = 30000) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 30000,k = 30000) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 50,k = 2500) == 969
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 50,k = 2500) == 969: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 1000,k = 2999900) == 617430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 1000,k = 2999900) == 617430: {e}')
    
    total += 1
    try:
        result = candidate(m = 20000,n = 25000,k = 4000000) == 509960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20000,n = 25000,k = 4000000) == 509960: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 25000,k = 7500000) == 986034
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 25000,k = 7500000) == 986034: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 10,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 10,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 20000,k = 500000) == 53798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 20000,k = 500000) == 53798: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 20000,k = 900000) == 102087
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 20000,k = 900000) == 102087: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 30000,k = 8999999) == 1182788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 30000,k = 8999999) == 1182788: {e}')
    
    total += 1
    try:
        result = candidate(m = 3000,n = 1000,k = 2999000) == 2925000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3000,n = 1000,k = 2999000) == 2925000: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 20000,k = 1500000) == 180253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 20000,k = 1500000) == 180253: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 7,k = 28) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 7,k = 28) == 14: {e}')
    
    total += 1
    try:
        result = candidate(m = 2500,n = 2500,k = 3125000) == 1167987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2500,n = 2500,k = 3125000) == 1167987: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,k = 100000000) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,k = 100000000) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 1,k = 15000) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 1,k = 15000) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(m = 12345,n = 6789,k = 500000) == 62055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12345,n = 6789,k = 500000) == 62055: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,k = 9999999) == 2047629
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,k = 9999999) == 2047629: {e}')
    
    total += 1
    try:
        result = candidate(m = 8000,n = 4000,k = 3199999) == 655946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8000,n = 4000,k = 3199999) == 655946: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 15000,k = 449999999) == 449985000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 15000,k = 449999999) == 449985000: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 11,k = 45) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 11,k = 45) == 24: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 15000,k = 5625000) == 858635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 15000,k = 5625000) == 858635: {e}')
    
    total += 1
    try:
        result = candidate(m = 5000,n = 5000,k = 12345678) == 4578057
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5000,n = 5000,k = 12345678) == 4578057: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 25000,k = 500000) == 52647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 25000,k = 500000) == 52647: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,k = 99) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,k = 99) == 90: {e}')
    
    total += 1
    try:
        result = candidate(m = 20000,n = 20000,k = 39999999) == 8185453
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20000,n = 20000,k = 39999999) == 8185453: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 30,k = 400) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 30,k = 400) == 153: {e}')
    
    total += 1
    try:
        result = candidate(m = 20000,n = 15000,k = 2999999) == 395392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20000,n = 15000,k = 2999999) == 395392: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 25,k = 400) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 25,k = 400) == 234: {e}')
    
    total += 1
    try:
        result = candidate(m = 2500,n = 7500,k = 9375000) == 3502712
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2500,n = 7500,k = 9375000) == 3502712: {e}')
    
    total += 1
    try:
        result = candidate(m = 5000,n = 5000,k = 1250000) == 218673
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5000,n = 5000,k = 1250000) == 218673: {e}')
    
    total += 1
    try:
        result = candidate(m = 150,n = 200,k = 14999) == 5684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 150,n = 200,k = 14999) == 5684: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 50,k = 2499) == 968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 50,k = 2499) == 968: {e}')
    
    total += 1
    try:
        result = candidate(m = 12345,n = 6789,k = 83245678) == 74281625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12345,n = 6789,k = 83245678) == 74281625: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 200,k = 10000) == 3807
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 200,k = 10000) == 3807: {e}')
    
    total += 1
    try:
        result = candidate(m = 25000,n = 25000,k = 12500000) == 1833387
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25000,n = 25000,k = 12500000) == 1833387: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,k = 28) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,k = 28) == 14: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 10,k = 50) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 10,k = 50) == 30: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,k = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,k = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 75,k = 2000) == 810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 75,k = 2000) == 810: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 15000,k = 10000000) == 1701960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 15000,k = 10000000) == 1701960: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 30000,k = 25000) == 25000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 30000,k = 25000) == 25000: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 30000,k = 20000) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 30000,k = 20000) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(m = 20000,n = 15000,k = 200000000) == 91383084
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20000,n = 15000,k = 200000000) == 91383084: {e}')
    
    total += 1
    try:
        result = candidate(m = 3000,n = 2500,k = 7499999) == 7497500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3000,n = 2500,k = 7499999) == 7497500: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,k = 4950) == 1887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,k = 4950) == 1887: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20,k = 100) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20,k = 100) == 36: {e}')
    
    total += 1
    try:
        result = candidate(m = 20000,n = 15000,k = 1000000) == 114741
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20000,n = 15000,k = 1000000) == 114741: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 15000,k = 1000000) == 118734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 15000,k = 1000000) == 118734: {e}')
    
    total += 1
    try:
        result = candidate(m = 25000,n = 5000,k = 2000000) == 284382
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25000,n = 5000,k = 2000000) == 284382: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 30000,k = 9000000) == 1182788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 30000,k = 9000000) == 1182788: {e}')
    
    total += 1
    try:
        result = candidate(m = 30000,n = 1,k = 30000) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30000,n = 1,k = 30000) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(m = 15000,n = 20000,k = 2999999) == 395392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15000,n = 20000,k = 2999999) == 395392: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 500,k = 125000) == 46917
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 500,k = 125000) == 46917: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,k = 5000) == 1917
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,k = 5000) == 1917: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,k = 4900) == 1856
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,k = 4900) == 1856: {e}')
    
    total += 1
    try:
        result = candidate(m = 1500,n = 2000,k = 1500000) == 560898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1500,n = 2000,k = 1500000) == 560898: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 3,n = 3,k = 5) == 3
    assert candidate(m = 10,n = 10,k = 25) == 10
    assert candidate(m = 5,n = 5,k = 1) == 1
    assert candidate(m = 4,n = 4,k = 10) == 6
    assert candidate(m = 4,n = 4,k = 8) == 4
    assert candidate(m = 30000,n = 30000,k = 10000) == 1358
    assert candidate(m = 2,n = 3,k = 6) == 6
    assert candidate(m = 5,n = 6,k = 15) == 8
    assert candidate(m = 30000,n = 30000,k = 100) == 28
    assert candidate(m = 1,n = 1,k = 1) == 1
    assert candidate(m = 4,n = 4,k = 7) == 4
    assert candidate(m = 1,n = 30000,k = 15000) == 15000
    assert candidate(m = 1000,n = 1,k = 500) == 500
    assert candidate(m = 12345,n = 6789,k = 5000000) == 906384
    assert candidate(m = 12000,n = 12000,k = 71999999) == 26888084
    assert candidate(m = 9999,n = 9999,k = 99980001) == 99980001
    assert candidate(m = 10000,n = 10,k = 5000) == 1709
    assert candidate(m = 10,n = 1,k = 5) == 5
    assert candidate(m = 9999,n = 10000,k = 49995000) == 18671202
    assert candidate(m = 5000,n = 5000,k = 12500000) == 4669497
    assert candidate(m = 10,n = 10000,k = 5000) == 1709
    assert candidate(m = 15000,n = 15000,k = 11250000) == 1961750
    assert candidate(m = 10000,n = 10000,k = 50000000) == 18673076
    assert candidate(m = 8000,n = 8000,k = 39999999) == 17356893
    assert candidate(m = 7,n = 9,k = 45) == 27
    assert candidate(m = 10,n = 15,k = 45) == 18
    assert candidate(m = 25000,n = 25000,k = 6250000) == 821997
    assert candidate(m = 5000,n = 20000,k = 1000000) == 132820
    assert candidate(m = 10000,n = 15000,k = 2000000) == 275724
    assert candidate(m = 10000,n = 10000,k = 99999999) == 99990000
    assert candidate(m = 7,n = 7,k = 49) == 49
    assert candidate(m = 12345,n = 67890,k = 4567890) == 553668
    assert candidate(m = 300,n = 100,k = 28000) == 19899
    assert candidate(m = 7500,n = 2500,k = 18749999) == 18747500
    assert candidate(m = 1000,n = 30000,k = 2999900) == 617430
    assert candidate(m = 30000,n = 1,k = 29999) == 29999
    assert candidate(m = 200,n = 100,k = 19900) == 18145
    assert candidate(m = 250,n = 250,k = 12500) == 3210
    assert candidate(m = 1,n = 30000,k = 30000) == 30000
    assert candidate(m = 100,n = 50,k = 2500) == 969
    assert candidate(m = 30000,n = 1000,k = 2999900) == 617430
    assert candidate(m = 20000,n = 25000,k = 4000000) == 509960
    assert candidate(m = 30000,n = 25000,k = 7500000) == 986034
    assert candidate(m = 1,n = 10,k = 5) == 5
    assert candidate(m = 15000,n = 20000,k = 500000) == 53798
    assert candidate(m = 15000,n = 20000,k = 900000) == 102087
    assert candidate(m = 30000,n = 30000,k = 8999999) == 1182788
    assert candidate(m = 3000,n = 1000,k = 2999000) == 2925000
    assert candidate(m = 15000,n = 20000,k = 1500000) == 180253
    assert candidate(m = 8,n = 7,k = 28) == 14
    assert candidate(m = 2500,n = 2500,k = 3125000) == 1167987
    assert candidate(m = 10000,n = 10000,k = 100000000) == 100000000
    assert candidate(m = 30000,n = 1,k = 15000) == 15000
    assert candidate(m = 12345,n = 6789,k = 500000) == 62055
    assert candidate(m = 10000,n = 10000,k = 9999999) == 2047629
    assert candidate(m = 8000,n = 4000,k = 3199999) == 655946
    assert candidate(m = 30000,n = 15000,k = 449999999) == 449985000
    assert candidate(m = 7,n = 11,k = 45) == 24
    assert candidate(m = 15000,n = 15000,k = 5625000) == 858635
    assert candidate(m = 5000,n = 5000,k = 12345678) == 4578057
    assert candidate(m = 15000,n = 25000,k = 500000) == 52647
    assert candidate(m = 10,n = 10,k = 99) == 90
    assert candidate(m = 20000,n = 20000,k = 39999999) == 8185453
    assert candidate(m = 10000,n = 10000,k = 1) == 1
    assert candidate(m = 30,n = 30,k = 400) == 153
    assert candidate(m = 20000,n = 15000,k = 2999999) == 395392
    assert candidate(m = 20,n = 25,k = 400) == 234
    assert candidate(m = 2500,n = 7500,k = 9375000) == 3502712
    assert candidate(m = 5000,n = 5000,k = 1250000) == 218673
    assert candidate(m = 150,n = 200,k = 14999) == 5684
    assert candidate(m = 100,n = 50,k = 2499) == 968
    assert candidate(m = 12345,n = 6789,k = 83245678) == 74281625
    assert candidate(m = 100,n = 200,k = 10000) == 3807
    assert candidate(m = 25000,n = 25000,k = 12500000) == 1833387
    assert candidate(m = 7,n = 8,k = 28) == 14
    assert candidate(m = 7,n = 10,k = 50) == 30
    assert candidate(m = 10,n = 5,k = 20) == 10
    assert candidate(m = 50,n = 75,k = 2000) == 810
    assert candidate(m = 15000,n = 15000,k = 10000000) == 1701960
    assert candidate(m = 1,n = 30000,k = 25000) == 25000
    assert candidate(m = 1,n = 30000,k = 20000) == 20000
    assert candidate(m = 20000,n = 15000,k = 200000000) == 91383084
    assert candidate(m = 3000,n = 2500,k = 7499999) == 7497500
    assert candidate(m = 100,n = 100,k = 4950) == 1887
    assert candidate(m = 15,n = 20,k = 100) == 36
    assert candidate(m = 20000,n = 15000,k = 1000000) == 114741
    assert candidate(m = 15000,n = 15000,k = 1000000) == 118734
    assert candidate(m = 25000,n = 5000,k = 2000000) == 284382
    assert candidate(m = 30000,n = 30000,k = 9000000) == 1182788
    assert candidate(m = 30000,n = 1,k = 30000) == 30000
    assert candidate(m = 15000,n = 20000,k = 2999999) == 395392
    assert candidate(m = 500,n = 500,k = 125000) == 46917
    assert candidate(m = 100,n = 100,k = 5000) == 1917
    assert candidate(m = 100,n = 100,k = 4900) == 1856
    assert candidate(m = 1500,n = 2000,k = 1500000) == 560898


