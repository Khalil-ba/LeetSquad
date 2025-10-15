def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,a = 6,b = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,a = 6,b = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 3,b = 7) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 3,b = 7) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 2,b = 3) == 499999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 2,b = 3) == 499999993: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 7,b = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 7,b = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,a = 3,b = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,a = 3,b = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,a = 7,b = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,a = 7,b = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 3,b = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 3,b = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 40000,b = 40001) == 249930000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 40000,b = 40001) == 249930000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,a = 2,b = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,a = 2,b = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 7,b = 11) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 7,b = 11) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,a = 2,b = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,a = 2,b = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 12,b = 18) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 12,b = 18) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 40000,b = 40000) == 999720007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 40000,b = 40000) == 999720007: {e}')
    
    total += 1
    try:
        result = candidate(n = 234567890,a = 66666,b = 99999) == 277133959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234567890,a = 66666,b = 99999) == 277133959: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000,a = 8000,b = 16000) == 999958007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000,a = 8000,b = 16000) == 999958007: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,a = 29,b = 37) == 904615333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,a = 29,b = 37) == 904615333: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 10000,b = 10000) == 999965007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 10000,b = 10000) == 999965007: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 234,b = 567) == 16848
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 234,b = 567) == 16848: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 33333,b = 44444) == 999922230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 33333,b = 44444) == 999922230: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,a = 100,b = 300) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,a = 100,b = 300) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 39999,b = 40000) == 999860007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 39999,b = 40000) == 999860007: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 3,b = 11) == 538461521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 3,b = 11) == 538461521: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000,a = 20001,b = 30002) == 689943000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000,a = 20001,b = 30002) == 689943000: {e}')
    
    total += 1
    try:
        result = candidate(n = 120000000,a = 11,b = 23) == 920000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120000000,a = 11,b = 23) == 920000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 900000000,a = 89,b = 127) == 314883394
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900000000,a = 89,b = 127) == 314883394: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 3,b = 5) == 142857126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 3,b = 5) == 142857126: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,a = 12345,b = 67890) == 754478652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,a = 12345,b = 67890) == 754478652: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,a = 7999,b = 8000) == 999977607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,a = 7999,b = 8000) == 999977607: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,a = 789,b = 321) == 30893061
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,a = 789,b = 321) == 30893061: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000000,a = 8888,b = 9999) == 962497382
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000000,a = 8888,b = 9999) == 962497382: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 23,b = 47) == 833333281
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 23,b = 47) == 833333281: {e}')
    
    total += 1
    try:
        result = candidate(n = 400000000,a = 13579,b = 24680) == 891663244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000000,a = 13579,b = 24680) == 891663244: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,a = 11111,b = 22222) == 299976669
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,a = 11111,b = 22222) == 299976669: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000,a = 50000,b = 50001) == 124956250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000,a = 50000,b = 50001) == 124956250: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 10000,b = 10001) == 249982500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 10000,b = 10001) == 249982500: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000,a = 3456,b = 7890) == 22857132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000,a = 3456,b = 7890) == 22857132: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,a = 23456,b = 34567) == 814186778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,a = 23456,b = 34567) == 814186778: {e}')
    
    total += 1
    try:
        result = candidate(n = 654321098,a = 55555,b = 88888) == 872244777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 654321098,a = 55555,b = 88888) == 872244777: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,a = 5000,b = 5001) == 299989500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,a = 5000,b = 5001) == 299989500: {e}')
    
    total += 1
    try:
        result = candidate(n = 900000000,a = 13,b = 19) == 170967696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900000000,a = 13,b = 19) == 170967696: {e}')
    
    total += 1
    try:
        result = candidate(n = 345678901,a = 11111,b = 22222) == 838242131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345678901,a = 11111,b = 22222) == 838242131: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,a = 3,b = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,a = 3,b = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000,a = 89756,b = 34213) == 771543424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000,a = 89756,b = 34213) == 771543424: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 2,b = 2) == 999999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 2,b = 2) == 999999993: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 2,b = 5) == 833333334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 2,b = 5) == 833333334: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,a = 10000,b = 20000) == 999993007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,a = 10000,b = 20000) == 999993007: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,a = 27182,b = 31415) == 137264409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,a = 27182,b = 31415) == 137264409: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 33333,b = 66666) == 999733343
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 33333,b = 66666) == 999733343: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000,a = 11,b = 29) == 134615346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000,a = 11,b = 29) == 134615346: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,a = 4321,b = 9876) == 119975644
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,a = 4321,b = 9876) == 119975644: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 37,b = 41) == 701298547
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 37,b = 41) == 701298547: {e}')
    
    total += 1
    try:
        result = candidate(n = 456789012,a = 14142,b = 17320) == 441321430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789012,a = 14142,b = 17320) == 441321430: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 12345,b = 67890) == 544786471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 12345,b = 67890) == 544786471: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 29,b = 31) == 237288036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 29,b = 31) == 237288036: {e}')
    
    total += 1
    try:
        result = candidate(n = 400000000,a = 34567,b = 45678) == 751276078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000000,a = 34567,b = 45678) == 751276078: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 11111,b = 22222) == 111099993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 11111,b = 22222) == 111099993: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000000,a = 40000,b = 40003) == 149973375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000000,a = 40000,b = 40003) == 149973375: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000,a = 456,b = 789) == 260868172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000,a = 456,b = 789) == 260868172: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 37,b = 100) == 205882140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 37,b = 100) == 205882140: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,a = 11111,b = 22222) == 99992223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,a = 11111,b = 22222) == 99992223: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,a = 100,b = 101) == 99999930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,a = 100,b = 101) == 99999930: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,a = 1234,b = 5678) == 183610385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,a = 1234,b = 5678) == 183610385: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000000,a = 11111,b = 22222) == 649988338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000000,a = 11111,b = 22222) == 649988338: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,a = 111,b = 222) == 599999538
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,a = 111,b = 222) == 599999538: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 2,b = 3) == 499999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 2,b = 3) == 499999991: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000001,a = 8000,b = 8001) == 249994000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000001,a = 8000,b = 8001) == 249994000: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,a = 15000,b = 17000) == 161273485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,a = 15000,b = 17000) == 161273485: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 10000,b = 12345) == 981180666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 10000,b = 12345) == 981180666: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 2,b = 3) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 2,b = 3) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000,a = 10000,b = 10003) == 249963753
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000,a = 10000,b = 10003) == 249963753: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,a = 34567,b = 98765) == 656326046
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,a = 34567,b = 98765) == 656326046: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,a = 15000,b = 16000) == 999983207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,a = 15000,b = 16000) == 999983207: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000000,a = 17,b = 23) == 503846139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000000,a = 17,b = 23) == 503846139: {e}')
    
    total += 1
    try:
        result = candidate(n = 789012345,a = 1111,b = 2222) == 592709163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789012345,a = 1111,b = 2222) == 592709163: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 37337,b = 49249) == 524562485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 37337,b = 49249) == 524562485: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,a = 9000,b = 18000) == 999962207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,a = 9000,b = 18000) == 999962207: {e}')
    
    total += 1
    try:
        result = candidate(n = 400000000,a = 20001,b = 20002) == 399972000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000000,a = 20001,b = 20002) == 399972000: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,a = 12345,b = 67890) == 35841519
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,a = 12345,b = 67890) == 35841519: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,a = 12345,b = 54321) == 944440755
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,a = 12345,b = 54321) == 944440755: {e}')
    
    total += 1
    try:
        result = candidate(n = 678901234,a = 12345,b = 12346) == 857288152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 678901234,a = 12345,b = 12346) == 857288152: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,a = 12345,b = 67890) == 820330907
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,a = 12345,b = 67890) == 820330907: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000,a = 23456,b = 78901) == 617619200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000,a = 23456,b = 78901) == 617619200: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 10001,b = 10007) == 124765147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 10001,b = 10007) == 124765147: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000,a = 789,b = 1234) == 75815670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000,a = 789,b = 1234) == 75815670: {e}')
    
    total += 1
    try:
        result = candidate(n = 650000000,a = 46810,b = 57921) == 397052571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650000000,a = 46810,b = 57921) == 397052571: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 40000,b = 40001) == 499860000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 40000,b = 40001) == 499860000: {e}')
    
    total += 1
    try:
        result = candidate(n = 345678912,a = 2345,b = 6789) == 570799481
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345678912,a = 2345,b = 6789) == 570799481: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 12345,b = 67890) == 772393239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 12345,b = 67890) == 772393239: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210,a = 23456,b = 78901) == 803519554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210,a = 23456,b = 78901) == 803519554: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,a = 13579,b = 24680) == 448025793
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,a = 13579,b = 24680) == 448025793: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000,a = 10000,b = 10001) == 24998250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000,a = 10000,b = 10001) == 24998250: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,a = 10001,b = 10002) == 99996500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,a = 10001,b = 10002) == 99996500: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 10000,b = 10001) == 499955000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 10000,b = 10001) == 499955000: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,a = 41,b = 53) == 692472990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,a = 41,b = 53) == 692472990: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 1234,b = 5678) == 13987665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 1234,b = 5678) == 13987665: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,a = 12345,b = 23456) == 516628373
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,a = 12345,b = 23456) == 516628373: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000,a = 50000,b = 75000) == 999934382
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000,a = 50000,b = 75000) == 999934382: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,a = 20000,b = 30000) == 851827043
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,a = 20000,b = 30000) == 851827043: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 4,b = 6) == 499999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 4,b = 6) == 499999993: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 10001,b = 10002) == 500100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 10001,b = 10002) == 500100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 765432109,a = 33333,b = 44444) == 432218246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 765432109,a = 33333,b = 44444) == 432218246: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,a = 10001,b = 20002) == 799944000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,a = 10001,b = 20002) == 799944000: {e}')
    
    total += 1
    try:
        result = candidate(n = 456789123,a = 2020,b = 3030) == 35515996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789123,a = 2020,b = 3030) == 35515996: {e}')
    
    total += 1
    try:
        result = candidate(n = 450000000,a = 17,b = 29) == 929999972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450000000,a = 17,b = 29) == 929999972: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,a = 6,b = 5) == 15
    assert candidate(n = 10,a = 3,b = 7) == 24
    assert candidate(n = 1000000000,a = 2,b = 3) == 499999993
    assert candidate(n = 10,a = 7,b = 3) == 24
    assert candidate(n = 5,a = 3,b = 5) == 10
    assert candidate(n = 5,a = 7,b = 5) == 15
    assert candidate(n = 10,a = 3,b = 5) == 21
    assert candidate(n = 500000000,a = 40000,b = 40001) == 249930000
    assert candidate(n = 4,a = 2,b = 3) == 6
    assert candidate(n = 10,a = 7,b = 11) == 44
    assert candidate(n = 1,a = 2,b = 3) == 2
    assert candidate(n = 10,a = 12,b = 18) == 90
    assert candidate(n = 1000000000,a = 40000,b = 40000) == 999720007
    assert candidate(n = 234567890,a = 66666,b = 99999) == 277133959
    assert candidate(n = 750000000,a = 8000,b = 16000) == 999958007
    assert candidate(n = 600000000,a = 29,b = 37) == 904615333
    assert candidate(n = 500000000,a = 10000,b = 10000) == 999965007
    assert candidate(n = 100,a = 234,b = 567) == 16848
    assert candidate(n = 500000000,a = 33333,b = 44444) == 999922230
    assert candidate(n = 500,a = 100,b = 300) == 50000
    assert candidate(n = 1000000000,a = 39999,b = 40000) == 999860007
    assert candidate(n = 999999999,a = 3,b = 11) == 538461521
    assert candidate(n = 750000000,a = 20001,b = 30002) == 689943000
    assert candidate(n = 120000000,a = 11,b = 23) == 920000000
    assert candidate(n = 900000000,a = 89,b = 127) == 314883394
    assert candidate(n = 999999999,a = 3,b = 5) == 142857126
    assert candidate(n = 100000000,a = 12345,b = 67890) == 754478652
    assert candidate(n = 800000000,a = 7999,b = 8000) == 999977607
    assert candidate(n = 800000000,a = 789,b = 321) == 30893061
    assert candidate(n = 75000000,a = 8888,b = 9999) == 962497382
    assert candidate(n = 500000000,a = 23,b = 47) == 833333281
    assert candidate(n = 400000000,a = 13579,b = 24680) == 891663244
    assert candidate(n = 300000000,a = 11111,b = 22222) == 299976669
    assert candidate(n = 250000000,a = 50000,b = 50001) == 124956250
    assert candidate(n = 500000000,a = 10000,b = 10001) == 249982500
    assert candidate(n = 5000000,a = 3456,b = 7890) == 22857132
    assert candidate(n = 200000000,a = 23456,b = 34567) == 814186778
    assert candidate(n = 654321098,a = 55555,b = 88888) == 872244777
    assert candidate(n = 600000000,a = 5000,b = 5001) == 299989500
    assert candidate(n = 900000000,a = 13,b = 19) == 170967696
    assert candidate(n = 345678901,a = 11111,b = 22222) == 838242131
    assert candidate(n = 1,a = 3,b = 5) == 3
    assert candidate(n = 250000000,a = 89756,b = 34213) == 771543424
    assert candidate(n = 1000000000,a = 2,b = 2) == 999999993
    assert candidate(n = 500000000,a = 2,b = 5) == 833333334
    assert candidate(n = 100000000,a = 10000,b = 20000) == 999993007
    assert candidate(n = 987654321,a = 27182,b = 31415) == 137264409
    assert candidate(n = 999999999,a = 33333,b = 66666) == 999733343
    assert candidate(n = 750000000,a = 11,b = 29) == 134615346
    assert candidate(n = 123456789,a = 4321,b = 9876) == 119975644
    assert candidate(n = 999999999,a = 37,b = 41) == 701298547
    assert candidate(n = 456789012,a = 14142,b = 17320) == 441321430
    assert candidate(n = 999999999,a = 12345,b = 67890) == 544786471
    assert candidate(n = 1000000000,a = 29,b = 31) == 237288036
    assert candidate(n = 400000000,a = 34567,b = 45678) == 751276078
    assert candidate(n = 100000,a = 11111,b = 22222) == 111099993
    assert candidate(n = 150000000,a = 40000,b = 40003) == 149973375
    assert candidate(n = 750000000,a = 456,b = 789) == 260868172
    assert candidate(n = 999999999,a = 37,b = 100) == 205882140
    assert candidate(n = 100000000,a = 11111,b = 22222) == 99992223
    assert candidate(n = 200000000,a = 100,b = 101) == 99999930
    assert candidate(n = 123456789,a = 1234,b = 5678) == 183610385
    assert candidate(n = 150000000,a = 11111,b = 22222) == 649988338
    assert candidate(n = 600000000,a = 111,b = 222) == 599999538
    assert candidate(n = 999999999,a = 2,b = 3) == 499999991
    assert candidate(n = 500000001,a = 8000,b = 8001) == 249994000
    assert candidate(n = 200000000,a = 15000,b = 17000) == 161273485
    assert candidate(n = 500000000,a = 10000,b = 12345) == 981180666
    assert candidate(n = 1000,a = 2,b = 3) == 1500
    assert candidate(n = 250000000,a = 10000,b = 10003) == 249963753
    assert candidate(n = 300000000,a = 34567,b = 98765) == 656326046
    assert candidate(n = 300000000,a = 15000,b = 16000) == 999983207
    assert candidate(n = 150000000,a = 17,b = 23) == 503846139
    assert candidate(n = 789012345,a = 1111,b = 2222) == 592709163
    assert candidate(n = 500000000,a = 37337,b = 49249) == 524562485
    assert candidate(n = 600000000,a = 9000,b = 18000) == 999962207
    assert candidate(n = 400000000,a = 20001,b = 20002) == 399972000
    assert candidate(n = 800000000,a = 12345,b = 67890) == 35841519
    assert candidate(n = 100000000,a = 12345,b = 54321) == 944440755
    assert candidate(n = 678901234,a = 12345,b = 12346) == 857288152
    assert candidate(n = 123456789,a = 12345,b = 67890) == 820330907
    assert candidate(n = 600000000,a = 23456,b = 78901) == 617619200
    assert candidate(n = 500000000,a = 10001,b = 10007) == 124765147
    assert candidate(n = 50000000,a = 789,b = 1234) == 75815670
    assert candidate(n = 650000000,a = 46810,b = 57921) == 397052571
    assert candidate(n = 1000000000,a = 40000,b = 40001) == 499860000
    assert candidate(n = 345678912,a = 2345,b = 6789) == 570799481
    assert candidate(n = 500000000,a = 12345,b = 67890) == 772393239
    assert candidate(n = 876543210,a = 23456,b = 78901) == 803519554
    assert candidate(n = 123456789,a = 13579,b = 24680) == 448025793
    assert candidate(n = 50000000,a = 10000,b = 10001) == 24998250
    assert candidate(n = 100000000,a = 10001,b = 10002) == 99996500
    assert candidate(n = 999999999,a = 10000,b = 10001) == 499955000
    assert candidate(n = 800000000,a = 41,b = 53) == 692472990
    assert candidate(n = 1000000,a = 1234,b = 5678) == 13987665
    assert candidate(n = 300000000,a = 12345,b = 23456) == 516628373
    assert candidate(n = 250000000,a = 50000,b = 75000) == 999934382
    assert candidate(n = 123456789,a = 20000,b = 30000) == 851827043
    assert candidate(n = 500000000,a = 4,b = 6) == 499999993
    assert candidate(n = 100000,a = 10001,b = 10002) == 500100000
    assert candidate(n = 765432109,a = 33333,b = 44444) == 432218246
    assert candidate(n = 800000000,a = 10001,b = 20002) == 799944000
    assert candidate(n = 456789123,a = 2020,b = 3030) == 35515996
    assert candidate(n = 450000000,a = 17,b = 29) == 929999972


