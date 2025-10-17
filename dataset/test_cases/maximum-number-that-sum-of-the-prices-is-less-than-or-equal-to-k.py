def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 15,x = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,x = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,x = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,x = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000000000000,x = 8) == 40104798005951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000000000000,x = 8) == 40104798005951: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,x = 6) == 1011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,x = 6) == 1011: {e}')
    
    total += 1
    try:
        result = candidate(k = 20,x = 2) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20,x = 2) == 23: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,x = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,x = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 15,x = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,x = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,x = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,x = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,x = 4) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,x = 4) == 153: {e}')
    
    total += 1
    try:
        result = candidate(k = 15,x = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,x = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,x = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,x = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,x = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,x = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,x = 7) == 2023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,x = 7) == 2023: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,x = 6) == 2023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,x = 6) == 2023: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000000000,x = 8) == 343778878348159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000000000,x = 8) == 343778878348159: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,x = 5) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,x = 5) == 211: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 8) == 1016223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 8) == 1016223: {e}')
    
    total += 1
    try:
        result = candidate(k = 9876543210,x = 2) == 1335770905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9876543210,x = 2) == 1335770905: {e}')
    
    total += 1
    try:
        result = candidate(k = 75000000000000,x = 5) == 18535653792058
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75000000000000,x = 5) == 18535653792058: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 2) == 229535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 2) == 229535: {e}')
    
    total += 1
    try:
        result = candidate(k = 37500000000000,x = 6) == 11028437048759
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 37500000000000,x = 6) == 11028437048759: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,x = 8) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,x = 8) == 135: {e}')
    
    total += 1
    try:
        result = candidate(k = 200000000000000,x = 4) == 36505448274943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 200000000000000,x = 4) == 36505448274943: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,x = 8) == 2023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,x = 8) == 2023: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321,x = 5) == 396332511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321,x = 5) == 396332511: {e}')
    
    total += 1
    try:
        result = candidate(k = 65536,x = 2) == 19343
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65536,x = 2) == 19343: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789,x = 7) == 82565716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789,x = 7) == 82565716: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321,x = 3) == 225159917
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321,x = 3) == 225159917: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,x = 4) == 505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,x = 4) == 505: {e}')
    
    total += 1
    try:
        result = candidate(k = 876543210,x = 4) == 252864144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 876543210,x = 4) == 252864144: {e}')
    
    total += 1
    try:
        result = candidate(k = 300,x = 2) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 300,x = 2) == 174: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,x = 7) == 202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,x = 7) == 202: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321,x = 7) == 502583375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321,x = 7) == 502583375: {e}')
    
    total += 1
    try:
        result = candidate(k = 10000,x = 5) == 10079
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000,x = 5) == 10079: {e}')
    
    total += 1
    try:
        result = candidate(k = 67890,x = 4) == 40389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67890,x = 4) == 40389: {e}')
    
    total += 1
    try:
        result = candidate(k = 888888888,x = 1) == 68597981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 888888888,x = 1) == 68597981: {e}')
    
    total += 1
    try:
        result = candidate(k = 750,x = 6) == 1517
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 750,x = 6) == 1517: {e}')
    
    total += 1
    try:
        result = candidate(k = 89,x = 4) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89,x = 4) == 144: {e}')
    
    total += 1
    try:
        result = candidate(k = 512,x = 5) == 687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 512,x = 5) == 687: {e}')
    
    total += 1
    try:
        result = candidate(k = 25000,x = 4) == 16839
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25000,x = 4) == 16839: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000000000000,x = 1) == 4779296144709
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000000000000,x = 1) == 4779296144709: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000000,x = 2) == 112964310932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000000,x = 2) == 112964310932: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,x = 5) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,x = 5) == 113: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999999999,x = 6) == 253657567778409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999999999,x = 6) == 253657567778409: {e}')
    
    total += 1
    try:
        result = candidate(k = 150000000000000,x = 4) == 27972811528487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 150000000000000,x = 4) == 27972811528487: {e}')
    
    total += 1
    try:
        result = candidate(k = 500000000,x = 5) == 200231279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000000,x = 5) == 200231279: {e}')
    
    total += 1
    try:
        result = candidate(k = 3000000000,x = 7) == 1522191359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3000000000,x = 7) == 1522191359: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 4) == 505131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 4) == 505131: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,x = 3) == 751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,x = 3) == 751: {e}')
    
    total += 1
    try:
        result = candidate(k = 1023,x = 1) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1023,x = 1) == 254: {e}')
    
    total += 1
    try:
        result = candidate(k = 456789123456789,x = 5) == 101944274868895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 456789123456789,x = 5) == 101944274868895: {e}')
    
    total += 1
    try:
        result = candidate(k = 111111111111111,x = 7) == 37402810498266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 111111111111111,x = 7) == 37402810498266: {e}')
    
    total += 1
    try:
        result = candidate(k = 500000000000000,x = 2) == 44975429102831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000000000000,x = 2) == 44975429102831: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789012345,x = 7) == 41467248081098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789012345,x = 7) == 41467248081098: {e}')
    
    total += 1
    try:
        result = candidate(k = 35791,x = 6) == 36150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 35791,x = 6) == 36150: {e}')
    
    total += 1
    try:
        result = candidate(k = 99999999999999,x = 8) == 40104798005950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99999999999999,x = 8) == 40104798005950: {e}')
    
    total += 1
    try:
        result = candidate(k = 50000000000000,x = 7) == 16799267244329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50000000000000,x = 7) == 16799267244329: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,x = 1) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,x = 1) == 22: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000000000,x = 7) == 320446066360319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000000000,x = 7) == 320446066360319: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,x = 5) == 675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,x = 5) == 675: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000000000000,x = 5) == 23566547569891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000000000000,x = 5) == 23566547569891: {e}')
    
    total += 1
    try:
        result = candidate(k = 86420,x = 1) == 12978
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 86420,x = 1) == 12978: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 1) == 120205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 1) == 120205: {e}')
    
    total += 1
    try:
        result = candidate(k = 9375000000000,x = 8) == 3858234249087
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9375000000000,x = 8) == 3858234249087: {e}')
    
    total += 1
    try:
        result = candidate(k = 125,x = 8) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 125,x = 8) == 252: {e}')
    
    total += 1
    try:
        result = candidate(k = 5000,x = 6) == 5927
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5000,x = 6) == 5927: {e}')
    
    total += 1
    try:
        result = candidate(k = 200,x = 5) == 407
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 200,x = 5) == 407: {e}')
    
    total += 1
    try:
        result = candidate(k = 12345678912345,x = 7) == 4155872352796
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12345678912345,x = 7) == 4155872352796: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,x = 2) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,x = 2) == 41: {e}')
    
    total += 1
    try:
        result = candidate(k = 500000000000000,x = 6) == 142592321015807
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000000000000,x = 6) == 142592321015807: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000,x = 6) == 500668855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000,x = 6) == 500668855: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,x = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,x = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 897654321000,x = 3) == 151072975789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 897654321000,x = 3) == 151072975789: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789,x = 2) == 20934568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789,x = 2) == 20934568: {e}')
    
    total += 1
    try:
        result = candidate(k = 87654321098765,x = 5) == 21067518135670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 87654321098765,x = 5) == 21067518135670: {e}')
    
    total += 1
    try:
        result = candidate(k = 150,x = 5) == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 150,x = 5) == 309: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000,x = 5) == 400458607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000,x = 5) == 400458607: {e}')
    
    total += 1
    try:
        result = candidate(k = 7777777777777,x = 8) == 3142572550626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7777777777777,x = 8) == 3142572550626: {e}')
    
    total += 1
    try:
        result = candidate(k = 1024,x = 6) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1024,x = 6) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000000,x = 7) == 66778015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000000,x = 7) == 66778015: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,x = 3) == 379
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,x = 3) == 379: {e}')
    
    total += 1
    try:
        result = candidate(k = 500000000000000,x = 8) == 183136759108959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000000000000,x = 8) == 183136759108959: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999999999,x = 8) == 343778878348158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999999999,x = 8) == 343778878348158: {e}')
    
    total += 1
    try:
        result = candidate(k = 8000000000000,x = 6) == 2550830257769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8000000000000,x = 6) == 2550830257769: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,x = 2) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,x = 2) == 504: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,x = 7) == 1011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,x = 7) == 1011: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 7) == 1000639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 7) == 1000639: {e}')
    
    total += 1
    try:
        result = candidate(k = 64,x = 4) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 64,x = 4) == 127: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999999999,x = 7) == 320446066360318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999999999,x = 7) == 320446066360318: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321,x = 2) == 150736664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321,x = 2) == 150736664: {e}')
    
    total += 1
    try:
        result = candidate(k = 300000000000000,x = 3) == 40423774188390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 300000000000000,x = 3) == 40423774188390: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,x = 6) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,x = 6) == 56: {e}')
    
    total += 1
    try:
        result = candidate(k = 99999999999999,x = 1) == 4779296144709
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99999999999999,x = 1) == 4779296144709: {e}')
    
    total += 1
    try:
        result = candidate(k = 256,x = 3) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 256,x = 3) == 255: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 3) == 350061
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 3) == 350061: {e}')
    
    total += 1
    try:
        result = candidate(k = 128,x = 2) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 128,x = 2) == 95: {e}')
    
    total += 1
    try:
        result = candidate(k = 333333333333333,x = 5) == 74563043705932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 333333333333333,x = 5) == 74563043705932: {e}')
    
    total += 1
    try:
        result = candidate(k = 200,x = 6) == 423
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 200,x = 6) == 423: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000000000,x = 1) == 44470852534271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000000000,x = 1) == 44470852534271: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789012345,x = 2) == 11594690512161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789012345,x = 2) == 11594690512161: {e}')
    
    total += 1
    try:
        result = candidate(k = 10000000000000,x = 2) == 1010190497191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000000000000,x = 2) == 1010190497191: {e}')
    
    total += 1
    try:
        result = candidate(k = 97531,x = 7) == 97788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 97531,x = 7) == 97788: {e}')
    
    total += 1
    try:
        result = candidate(k = 2048,x = 7) == 4159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2048,x = 7) == 4159: {e}')
    
    total += 1
    try:
        result = candidate(k = 800000000000000,x = 1) == 35598682963967
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 800000000000000,x = 1) == 35598682963967: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321,x = 4) == 284658738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321,x = 4) == 284658738: {e}')
    
    total += 1
    try:
        result = candidate(k = 75319,x = 8) == 85174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75319,x = 8) == 85174: {e}')
    
    total += 1
    try:
        result = candidate(k = 43210,x = 2) == 12987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 43210,x = 2) == 12987: {e}')
    
    total += 1
    try:
        result = candidate(k = 250000000,x = 8) == 166950655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 250000000,x = 8) == 166950655: {e}')
    
    total += 1
    try:
        result = candidate(k = 24680,x = 5) == 20551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 24680,x = 5) == 20551: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,x = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,x = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789,x = 5) == 52351833
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789,x = 5) == 52351833: {e}')
    
    total += 1
    try:
        result = candidate(k = 4096,x = 8) == 8319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4096,x = 8) == 8319: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 5) == 611931
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 5) == 611931: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000,x = 6) == 696703
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000,x = 6) == 696703: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,x = 3) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,x = 3) == 109: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,x = 8) == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,x = 8) == 137: {e}')
    
    total += 1
    try:
        result = candidate(k = 12345,x = 3) == 6589
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12345,x = 3) == 6589: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789,x = 3) == 31193134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789,x = 3) == 31193134: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,x = 8) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,x = 8) == 128: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789,x = 6) == 62823067
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789,x = 6) == 62823067: {e}')
    
    total += 1
    try:
        result = candidate(k = 2000000000,x = 6) == 846978196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2000000000,x = 6) == 846978196: {e}')
    
    total += 1
    try:
        result = candidate(k = 23,x = 3) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 23,x = 3) == 36: {e}')
    
    total += 1
    try:
        result = candidate(k = 2147483647,x = 7) == 1073741822
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2147483647,x = 7) == 1073741822: {e}')
    
    total += 1
    try:
        result = candidate(k = 30,x = 3) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 30,x = 3) == 41: {e}')
    
    total += 1
    try:
        result = candidate(k = 18750000000000,x = 7) == 6615951850383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 18750000000000,x = 7) == 6615951850383: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,x = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,x = 1) == 30: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 15,x = 1) == 9
    assert candidate(k = 5,x = 2) == 8
    assert candidate(k = 100000000000000,x = 8) == 40104798005951
    assert candidate(k = 500,x = 6) == 1011
    assert candidate(k = 20,x = 2) == 23
    assert candidate(k = 5,x = 1) == 4
    assert candidate(k = 15,x = 4) == 30
    assert candidate(k = 7,x = 2) == 9
    assert candidate(k = 100,x = 4) == 153
    assert candidate(k = 15,x = 3) == 30
    assert candidate(k = 10,x = 3) == 21
    assert candidate(k = 9,x = 1) == 6
    assert candidate(k = 1000,x = 7) == 2023
    assert candidate(k = 1000,x = 6) == 2023
    assert candidate(k = 1000000000000000,x = 8) == 343778878348159
    assert candidate(k = 100,x = 5) == 211
    assert candidate(k = 1000000,x = 8) == 1016223
    assert candidate(k = 9876543210,x = 2) == 1335770905
    assert candidate(k = 75000000000000,x = 5) == 18535653792058
    assert candidate(k = 1000000,x = 2) == 229535
    assert candidate(k = 37500000000000,x = 6) == 11028437048759
    assert candidate(k = 8,x = 8) == 135
    assert candidate(k = 200000000000000,x = 4) == 36505448274943
    assert candidate(k = 1000,x = 8) == 2023
    assert candidate(k = 987654321,x = 5) == 396332511
    assert candidate(k = 65536,x = 2) == 19343
    assert candidate(k = 123456789,x = 7) == 82565716
    assert candidate(k = 987654321,x = 3) == 225159917
    assert candidate(k = 500,x = 4) == 505
    assert candidate(k = 876543210,x = 4) == 252864144
    assert candidate(k = 300,x = 2) == 174
    assert candidate(k = 75,x = 7) == 202
    assert candidate(k = 987654321,x = 7) == 502583375
    assert candidate(k = 10000,x = 5) == 10079
    assert candidate(k = 67890,x = 4) == 40389
    assert candidate(k = 888888888,x = 1) == 68597981
    assert candidate(k = 750,x = 6) == 1517
    assert candidate(k = 89,x = 4) == 144
    assert candidate(k = 512,x = 5) == 687
    assert candidate(k = 25000,x = 4) == 16839
    assert candidate(k = 100000000000000,x = 1) == 4779296144709
    assert candidate(k = 1000000000000,x = 2) == 112964310932
    assert candidate(k = 50,x = 5) == 113
    assert candidate(k = 999999999999999,x = 6) == 253657567778409
    assert candidate(k = 150000000000000,x = 4) == 27972811528487
    assert candidate(k = 500000000,x = 5) == 200231279
    assert candidate(k = 3000000000,x = 7) == 1522191359
    assert candidate(k = 1000000,x = 4) == 505131
    assert candidate(k = 1000,x = 3) == 751
    assert candidate(k = 1023,x = 1) == 254
    assert candidate(k = 456789123456789,x = 5) == 101944274868895
    assert candidate(k = 111111111111111,x = 7) == 37402810498266
    assert candidate(k = 500000000000000,x = 2) == 44975429102831
    assert candidate(k = 123456789012345,x = 7) == 41467248081098
    assert candidate(k = 35791,x = 6) == 36150
    assert candidate(k = 99999999999999,x = 8) == 40104798005950
    assert candidate(k = 50000000000000,x = 7) == 16799267244329
    assert candidate(k = 50,x = 1) == 22
    assert candidate(k = 1000000000000000,x = 7) == 320446066360319
    assert candidate(k = 500,x = 5) == 675
    assert candidate(k = 100000000000000,x = 5) == 23566547569891
    assert candidate(k = 86420,x = 1) == 12978
    assert candidate(k = 1000000,x = 1) == 120205
    assert candidate(k = 9375000000000,x = 8) == 3858234249087
    assert candidate(k = 125,x = 8) == 252
    assert candidate(k = 5000,x = 6) == 5927
    assert candidate(k = 200,x = 5) == 407
    assert candidate(k = 12345678912345,x = 7) == 4155872352796
    assert candidate(k = 50,x = 2) == 41
    assert candidate(k = 500000000000000,x = 6) == 142592321015807
    assert candidate(k = 1000000000,x = 6) == 500668855
    assert candidate(k = 2,x = 1) == 2
    assert candidate(k = 897654321000,x = 3) == 151072975789
    assert candidate(k = 123456789,x = 2) == 20934568
    assert candidate(k = 87654321098765,x = 5) == 21067518135670
    assert candidate(k = 150,x = 5) == 309
    assert candidate(k = 1000000000,x = 5) == 400458607
    assert candidate(k = 7777777777777,x = 8) == 3142572550626
    assert candidate(k = 1024,x = 6) == 2047
    assert candidate(k = 100000000,x = 7) == 66778015
    assert candidate(k = 500,x = 3) == 379
    assert candidate(k = 500000000000000,x = 8) == 183136759108959
    assert candidate(k = 999999999999999,x = 8) == 343778878348158
    assert candidate(k = 8000000000000,x = 6) == 2550830257769
    assert candidate(k = 1000,x = 2) == 504
    assert candidate(k = 500,x = 7) == 1011
    assert candidate(k = 1000000,x = 7) == 1000639
    assert candidate(k = 64,x = 4) == 127
    assert candidate(k = 999999999999999,x = 7) == 320446066360318
    assert candidate(k = 987654321,x = 2) == 150736664
    assert candidate(k = 300000000000000,x = 3) == 40423774188390
    assert candidate(k = 25,x = 6) == 56
    assert candidate(k = 99999999999999,x = 1) == 4779296144709
    assert candidate(k = 256,x = 3) == 255
    assert candidate(k = 1000000,x = 3) == 350061
    assert candidate(k = 128,x = 2) == 95
    assert candidate(k = 333333333333333,x = 5) == 74563043705932
    assert candidate(k = 200,x = 6) == 423
    assert candidate(k = 1000000000000000,x = 1) == 44470852534271
    assert candidate(k = 123456789012345,x = 2) == 11594690512161
    assert candidate(k = 10000000000000,x = 2) == 1010190497191
    assert candidate(k = 97531,x = 7) == 97788
    assert candidate(k = 2048,x = 7) == 4159
    assert candidate(k = 800000000000000,x = 1) == 35598682963967
    assert candidate(k = 987654321,x = 4) == 284658738
    assert candidate(k = 75319,x = 8) == 85174
    assert candidate(k = 43210,x = 2) == 12987
    assert candidate(k = 250000000,x = 8) == 166950655
    assert candidate(k = 24680,x = 5) == 20551
    assert candidate(k = 1,x = 1) == 1
    assert candidate(k = 123456789,x = 5) == 52351833
    assert candidate(k = 4096,x = 8) == 8319
    assert candidate(k = 1000000,x = 5) == 611931
    assert candidate(k = 1000000,x = 6) == 696703
    assert candidate(k = 100,x = 3) == 109
    assert candidate(k = 10,x = 8) == 137
    assert candidate(k = 12345,x = 3) == 6589
    assert candidate(k = 123456789,x = 3) == 31193134
    assert candidate(k = 1,x = 8) == 128
    assert candidate(k = 123456789,x = 6) == 62823067
    assert candidate(k = 2000000000,x = 6) == 846978196
    assert candidate(k = 23,x = 3) == 36
    assert candidate(k = 2147483647,x = 7) == 1073741822
    assert candidate(k = 30,x = 3) == 41
    assert candidate(k = 18750000000000,x = 7) == 6615951850383
    assert candidate(k = 75,x = 1) == 30


