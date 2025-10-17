def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 7,m = 3,k = 6,source = [2, 1],dest = [5, 3]) == 11742
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 3,k = 6,source = [2, 1],dest = [5, 3]) == 11742: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 4,source = [1, 1],dest = [5, 5]) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 4,source = [1, 1],dest = [5, 5]) == 158: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 4,k = 3,source = [1, 2],dest = [2, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 4,k = 3,source = [1, 2],dest = [2, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 5,source = [3, 3],dest = [7, 7]) == 18240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 5,source = [3, 3],dest = [7, 7]) == 18240: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 10,source = [50, 50],dest = [60, 60]) == 240690551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 10,source = [50, 50],dest = [60, 60]) == 240690551: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 2,k = 2,source = [1, 1],dest = [2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 2,k = 2,source = [1, 1],dest = [2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,k = 20,source = [3, 3],dest = [15, 1]) == 741151508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,k = 20,source = [3, 3],dest = [15, 1]) == 741151508: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 1,source = [5, 5],dest = [5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 1,source = [5, 5],dest = [5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 10,source = [3, 3],dest = [3, 3]) == 42969224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 10,source = [3, 3],dest = [3, 3]) == 42969224: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 10,k = 20,source = [1, 5],dest = [1, 10]) == 395327121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 10,k = 20,source = [1, 5],dest = [1, 10]) == 395327121: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 6,k = 9,source = [1, 6],dest = [6, 1]) == 27763200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 6,k = 9,source = [1, 6],dest = [6, 1]) == 27763200: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 500,k = 150,source = [100, 50],dest = [900, 450]) == 384932960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 500,k = 150,source = [100, 50],dest = [900, 450]) == 384932960: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,m = 18,k = 14,source = [9, 9],dest = [18, 18]) == 985314051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,m = 18,k = 14,source = [9, 9],dest = [18, 18]) == 985314051: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,k = 10,source = [1, 9],dest = [9, 1]) == 567242851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,k = 10,source = [1, 9],dest = [9, 1]) == 567242851: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 30,k = 15,source = [15, 15],dest = [1, 1]) == 15377518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 30,k = 15,source = [15, 15],dest = [1, 1]) == 15377518: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 2,k = 100000,source = [1, 1],dest = [2, 2]) == 303861760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 2,k = 100000,source = [1, 1],dest = [2, 2]) == 303861760: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 10,k = 20,source = [5, 5],dest = [15, 10]) == 767227553
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 10,k = 20,source = [5, 5],dest = [15, 10]) == 767227553: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 7,k = 5,source = [2, 2],dest = [7, 7]) == 6435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 7,k = 5,source = [2, 2],dest = [7, 7]) == 6435: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 5,source = [1, 1],dest = [10, 10]) == 18240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 5,source = [1, 1],dest = [10, 10]) == 18240: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,k = 5,source = [1, 1],dest = [9, 9]) == 12530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,k = 5,source = [1, 1],dest = [9, 9]) == 12530: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 30,k = 100,source = [1, 1],dest = [30, 30]) == 783181632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 30,k = 100,source = [1, 1],dest = [30, 30]) == 783181632: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 25,k = 15,source = [25, 25],dest = [1, 1]) == 7372625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 25,k = 15,source = [25, 25],dest = [1, 1]) == 7372625: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 1,k = 20,source = [5, 1],dest = [10, 1]) == 395327121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 1,k = 20,source = [5, 1],dest = [10, 1]) == 395327121: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 30,k = 20,source = [1, 30],dest = [30, 1]) == 841565469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 30,k = 20,source = [1, 30],dest = [30, 1]) == 841565469: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,k = 15,source = [5, 5],dest = [15, 15]) == 31798627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,k = 15,source = [5, 5],dest = [15, 15]) == 31798627: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,k = 10,source = [10, 10],dest = [1, 1]) == 677174101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,k = 10,source = [10, 10],dest = [1, 1]) == 677174101: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 20,k = 8,source = [3, 4],dest = [12, 15]) == 648576396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 20,k = 8,source = [3, 4],dest = [12, 15]) == 648576396: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 5,k = 7,source = [3, 2],dest = [12, 5]) == 7326256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 5,k = 7,source = [3, 2],dest = [12, 5]) == 7326256: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 20,source = [3, 3],dest = [1, 1]) == 582555057
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 20,source = [3, 3],dest = [1, 1]) == 582555057: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 8,k = 10,source = [4, 4],dest = [8, 8]) == 517714404
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 8,k = 10,source = [4, 4],dest = [8, 8]) == 517714404: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 50,source = [1, 1],dest = [10, 10]) == 976259384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 50,source = [1, 1],dest = [10, 10]) == 976259384: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 25,source = [5, 5],dest = [10, 10]) == 485296658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 25,source = [5, 5],dest = [10, 10]) == 485296658: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 8,k = 15,source = [4, 4],dest = [1, 1]) == 782794384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 8,k = 15,source = [4, 4],dest = [1, 1]) == 782794384: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 500,k = 200,source = [250, 250],dest = [300, 300]) == 667798111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 500,k = 200,source = [250, 250],dest = [300, 300]) == 667798111: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 10,source = [1, 1],dest = [10, 10]) == 683197195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 10,source = [1, 1],dest = [10, 10]) == 683197195: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,m = 1000000000,k = 100000,source = [500000000, 500000000],dest = [600000000, 600000000]) == 965895368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,m = 1000000000,k = 100000,source = [500000000, 500000000],dest = [600000000, 600000000]) == 965895368: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 5,k = 8,source = [4, 3],dest = [1, 2]) == 672910184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 5,k = 8,source = [4, 3],dest = [1, 2]) == 672910184: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 100,source = [50, 50],dest = [25, 25]) == 271334151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 100,source = [50, 50],dest = [25, 25]) == 271334151: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 500,k = 5000,source = [250, 200],dest = [750, 300]) == 491803560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 500,k = 5000,source = [250, 200],dest = [750, 300]) == 491803560: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 15,k = 12,source = [6, 7],dest = [3, 3]) == 923740061
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 15,k = 12,source = [6, 7],dest = [3, 3]) == 923740061: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7,k = 10,source = [1, 7],dest = [7, 1]) == 263221095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7,k = 10,source = [1, 7],dest = [7, 1]) == 263221095: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 20,source = [25, 25],dest = [45, 45]) == 231517492
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 20,source = [25, 25],dest = [45, 45]) == 231517492: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 1,source = [10, 10],dest = [90, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 1,source = [10, 10],dest = [90, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 12,k = 25,source = [6, 6],dest = [12, 12]) == 90226411
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 12,k = 25,source = [6, 6],dest = [12, 12]) == 90226411: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 1,k = 5,source = [1, 1],dest = [10, 1]) == 5905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 1,k = 5,source = [1, 1],dest = [10, 1]) == 5905: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 25,source = [3, 3],dest = [1, 1]) == 401190346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 25,source = [3, 3],dest = [1, 1]) == 401190346: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 20,source = [3, 3],dest = [3, 3]) == 977897956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 20,source = [3, 3],dest = [3, 3]) == 977897956: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 20,k = 15,source = [4, 5],dest = [12, 18]) == 102993973
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 20,k = 15,source = [4, 5],dest = [12, 18]) == 102993973: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 1,k = 3,source = [1, 1],dest = [10, 1]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 1,k = 3,source = [1, 1],dest = [10, 1]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,k = 30,source = [1, 1],dest = [20, 15]) == 655472210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,k = 30,source = [1, 1],dest = [20, 15]) == 655472210: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 100,source = [2, 2],dest = [4, 4]) == 141053546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 100,source = [2, 2],dest = [4, 4]) == 141053546: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,k = 20,source = [10, 10],dest = [1, 1]) == 871858354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,k = 20,source = [10, 10],dest = [1, 1]) == 871858354: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 25,k = 25,source = [1, 1],dest = [25, 25]) == 412879981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 25,k = 25,source = [1, 1],dest = [25, 25]) == 412879981: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 1,source = [1, 1],dest = [5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 1,source = [1, 1],dest = [5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,k = 20,source = [1, 1],dest = [20, 15]) == 741151508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,k = 20,source = [1, 1],dest = [20, 15]) == 741151508: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,k = 5,source = [15, 15],dest = [5, 5]) == 188640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,k = 5,source = [15, 15],dest = [5, 5]) == 188640: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [25, 25]) == 507115071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [25, 25]) == 507115071: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 10,k = 10,source = [1, 1],dest = [1, 10]) == 348678440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 10,k = 10,source = [1, 1],dest = [1, 10]) == 348678440: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,k = 50,source = [1, 1],dest = [9, 9]) == 897765280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,k = 50,source = [1, 1],dest = [9, 9]) == 897765280: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 500,k = 100,source = [100, 100],dest = [400, 400]) == 883888844
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 500,k = 100,source = [100, 100],dest = [400, 400]) == 883888844: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 100000,source = [50, 50],dest = [1, 1]) == 946728093
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 100000,source = [50, 50],dest = [1, 1]) == 946728093: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,m = 1000000000,k = 100000,source = [1, 1],dest = [1000000000, 1000000000]) == 965895368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,m = 1000000000,k = 100000,source = [1, 1],dest = [1000000000, 1000000000]) == 965895368: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 15,source = [25, 25],dest = [40, 40]) == 17666803
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 15,source = [25, 25],dest = [40, 40]) == 17666803: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 10,source = [3, 3],dest = [1, 1]) == 42944990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 10,source = [3, 3],dest = [1, 1]) == 42944990: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [40, 40]) == 33487513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [40, 40]) == 33487513: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 15,k = 12,source = [1, 1],dest = [10, 15]) == 716494581
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 15,k = 12,source = [1, 1],dest = [10, 15]) == 716494581: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [1, 1]) == 33487513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [1, 1]) == 33487513: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,k = 10,source = [3, 3],dest = [7, 7]) == 567242851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,k = 10,source = [3, 3],dest = [7, 7]) == 567242851: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,m = 100000,k = 5000,source = [1, 1],dest = [100000, 100000]) == 540993502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,m = 100000,k = 5000,source = [1, 1],dest = [100000, 100000]) == 540993502: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 30,k = 25,source = [10, 10],dest = [20, 20]) == 768390149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 30,k = 25,source = [10, 10],dest = [20, 20]) == 768390149: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 50,source = [10, 10],dest = [90, 90]) == 223177367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 50,source = [10, 10],dest = [90, 90]) == 223177367: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,k = 100,source = [10, 10],dest = [1, 1]) == 89970184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,k = 100,source = [10, 10],dest = [1, 1]) == 89970184: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,m = 1000000000,k = 100000,source = [250000000, 500000000],dest = [350000000, 750000000]) == 68996267
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,m = 1000000000,k = 100000,source = [250000000, 500000000],dest = [350000000, 750000000]) == 68996267: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 1,k = 10,source = [1, 1],dest = [10, 1]) == 348678440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 1,k = 10,source = [1, 1],dest = [10, 1]) == 348678440: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,m = 1000000,k = 100000,source = [500000, 500000],dest = [500001, 500001]) == 851939950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,m = 1000000,k = 100000,source = [500000, 500000],dest = [500001, 500001]) == 851939950: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 15,source = [1, 1],dest = [100, 100]) == 70248680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 15,source = [1, 1],dest = [100, 100]) == 70248680: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 50000,source = [1, 1],dest = [100, 100]) == 828829667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 50000,source = [1, 1],dest = [100, 100]) == 828829667: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,m = 10000,k = 1000,source = [5000, 5000],dest = [7500, 7500]) == 922475845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,m = 10000,k = 1000,source = [5000, 5000],dest = [7500, 7500]) == 922475845: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,k = 100,source = [1, 1],dest = [100, 100]) == 271334151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,k = 100,source = [1, 1],dest = [100, 100]) == 271334151: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 1000,k = 1000,source = [500, 500],dest = [1, 1]) == 75187626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 1000,k = 1000,source = [500, 500],dest = [1, 1]) == 75187626: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 25,k = 12,source = [1, 25],dest = [25, 1]) == 483870578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 25,k = 12,source = [1, 25],dest = [25, 1]) == 483870578: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 50,source = [10, 10],dest = [40, 40]) == 33487513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 50,source = [10, 10],dest = [40, 40]) == 33487513: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,k = 12,source = [5, 5],dest = [10, 10]) == 912731589
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,k = 12,source = [5, 5],dest = [10, 10]) == 912731589: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 20,source = [1, 1],dest = [10, 10]) == 322125842
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 20,source = [1, 1],dest = [10, 10]) == 322125842: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 15,source = [1, 1],dest = [10, 10]) == 5072566
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 15,source = [1, 1],dest = [10, 10]) == 5072566: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 7,k = 8,source = [1, 7],dest = [8, 1]) == 14529656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 7,k = 8,source = [1, 7],dest = [8, 1]) == 14529656: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,m = 1000,k = 200,source = [1, 1],dest = [2000, 1000]) == 429645884
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,m = 1000,k = 200,source = [1, 1],dest = [2000, 1000]) == 429645884: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 25,k = 200,source = [5, 5],dest = [20, 20]) == 199868308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 25,k = 200,source = [5, 5],dest = [20, 20]) == 199868308: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 10,k = 3,source = [1, 1],dest = [1, 10]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 10,k = 3,source = [1, 1],dest = [1, 10]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,m = 1000000000,k = 100000,source = [1, 1],dest = [1000000000, 1000000000]) == 965895368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,m = 1000000000,k = 100000,source = [1, 1],dest = [1000000000, 1000000000]) == 965895368: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 25,k = 20,source = [25, 13],dest = [10, 20]) == 479759219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 25,k = 20,source = [25, 13],dest = [10, 20]) == 479759219: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,k = 9,source = [1, 9],dest = [9, 1]) == 847392210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,k = 9,source = [1, 9],dest = [9, 1]) == 847392210: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 10,k = 5,source = [1, 1],dest = [1, 10]) == 5905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 10,k = 5,source = [1, 1],dest = [1, 10]) == 5905: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 15,k = 5,source = [2, 2],dest = [14, 14]) == 73190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 15,k = 5,source = [2, 2],dest = [14, 14]) == 73190: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 8,k = 10,source = [6, 4],dest = [2, 7]) == 87570173
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 8,k = 10,source = [6, 4],dest = [2, 7]) == 87570173: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 5,k = 20,source = [3, 2],dest = [7, 4]) == 920636278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 5,k = 20,source = [3, 2],dest = [7, 4]) == 920636278: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 2,k = 4,source = [1, 1],dest = [2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 2,k = 4,source = [1, 1],dest = [2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,k = 10,source = [1, 1],dest = [5, 5]) == 42944990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,k = 10,source = [1, 1],dest = [5, 5]) == 42944990: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 1000,source = [25, 25],dest = [1, 1]) == 168759391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 1000,source = [25, 25],dest = [1, 1]) == 168759391: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 30,k = 20,source = [1, 1],dest = [30, 30]) == 841565469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 30,k = 20,source = [1, 1],dest = [30, 30]) == 841565469: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,k = 5,source = [25, 25],dest = [25, 25]) == 13603968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,k = 5,source = [25, 25],dest = [25, 25]) == 13603968: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 1000,k = 100,source = [500, 500],dest = [600, 600]) == 126893258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 1000,k = 100,source = [500, 500],dest = [600, 600]) == 126893258: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,k = 20,source = [5, 5],dest = [5, 5]) == 630244005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,k = 20,source = [5, 5],dest = [5, 5]) == 630244005: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 12,k = 8,source = [6, 6],dest = [1, 1]) == 379693568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 12,k = 8,source = [6, 6],dest = [1, 1]) == 379693568: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 7,m = 3,k = 6,source = [2, 1],dest = [5, 3]) == 11742
    assert candidate(n = 5,m = 5,k = 4,source = [1, 1],dest = [5, 5]) == 158
    assert candidate(n = 3,m = 4,k = 3,source = [1, 2],dest = [2, 3]) == 9
    assert candidate(n = 10,m = 10,k = 5,source = [3, 3],dest = [7, 7]) == 18240
    assert candidate(n = 100,m = 100,k = 10,source = [50, 50],dest = [60, 60]) == 240690551
    assert candidate(n = 3,m = 2,k = 2,source = [1, 1],dest = [2, 2]) == 2
    assert candidate(n = 20,m = 15,k = 20,source = [3, 3],dest = [15, 1]) == 741151508
    assert candidate(n = 10,m = 10,k = 1,source = [5, 5],dest = [5, 5]) == 0
    assert candidate(n = 5,m = 5,k = 10,source = [3, 3],dest = [3, 3]) == 42969224
    assert candidate(n = 1,m = 10,k = 20,source = [1, 5],dest = [1, 10]) == 395327121
    assert candidate(n = 6,m = 6,k = 9,source = [1, 6],dest = [6, 1]) == 27763200
    assert candidate(n = 1000,m = 500,k = 150,source = [100, 50],dest = [900, 450]) == 384932960
    assert candidate(n = 18,m = 18,k = 14,source = [9, 9],dest = [18, 18]) == 985314051
    assert candidate(n = 9,m = 9,k = 10,source = [1, 9],dest = [9, 1]) == 567242851
    assert candidate(n = 30,m = 30,k = 15,source = [15, 15],dest = [1, 1]) == 15377518
    assert candidate(n = 2,m = 2,k = 100000,source = [1, 1],dest = [2, 2]) == 303861760
    assert candidate(n = 15,m = 10,k = 20,source = [5, 5],dest = [15, 10]) == 767227553
    assert candidate(n = 8,m = 7,k = 5,source = [2, 2],dest = [7, 7]) == 6435
    assert candidate(n = 10,m = 10,k = 5,source = [1, 1],dest = [10, 10]) == 18240
    assert candidate(n = 9,m = 9,k = 5,source = [1, 1],dest = [9, 9]) == 12530
    assert candidate(n = 30,m = 30,k = 100,source = [1, 1],dest = [30, 30]) == 783181632
    assert candidate(n = 25,m = 25,k = 15,source = [25, 25],dest = [1, 1]) == 7372625
    assert candidate(n = 10,m = 1,k = 20,source = [5, 1],dest = [10, 1]) == 395327121
    assert candidate(n = 30,m = 30,k = 20,source = [1, 30],dest = [30, 1]) == 841565469
    assert candidate(n = 20,m = 20,k = 15,source = [5, 5],dest = [15, 15]) == 31798627
    assert candidate(n = 20,m = 20,k = 10,source = [10, 10],dest = [1, 1]) == 677174101
    assert candidate(n = 15,m = 20,k = 8,source = [3, 4],dest = [12, 15]) == 648576396
    assert candidate(n = 15,m = 5,k = 7,source = [3, 2],dest = [12, 5]) == 7326256
    assert candidate(n = 5,m = 5,k = 20,source = [3, 3],dest = [1, 1]) == 582555057
    assert candidate(n = 8,m = 8,k = 10,source = [4, 4],dest = [8, 8]) == 517714404
    assert candidate(n = 10,m = 10,k = 50,source = [1, 1],dest = [10, 10]) == 976259384
    assert candidate(n = 10,m = 10,k = 25,source = [5, 5],dest = [10, 10]) == 485296658
    assert candidate(n = 8,m = 8,k = 15,source = [4, 4],dest = [1, 1]) == 782794384
    assert candidate(n = 500,m = 500,k = 200,source = [250, 250],dest = [300, 300]) == 667798111
    assert candidate(n = 10,m = 10,k = 10,source = [1, 1],dest = [10, 10]) == 683197195
    assert candidate(n = 1000000000,m = 1000000000,k = 100000,source = [500000000, 500000000],dest = [600000000, 600000000]) == 965895368
    assert candidate(n = 20,m = 5,k = 8,source = [4, 3],dest = [1, 2]) == 672910184
    assert candidate(n = 100,m = 100,k = 100,source = [50, 50],dest = [25, 25]) == 271334151
    assert candidate(n = 1000,m = 500,k = 5000,source = [250, 200],dest = [750, 300]) == 491803560
    assert candidate(n = 12,m = 15,k = 12,source = [6, 7],dest = [3, 3]) == 923740061
    assert candidate(n = 7,m = 7,k = 10,source = [1, 7],dest = [7, 1]) == 263221095
    assert candidate(n = 50,m = 50,k = 20,source = [25, 25],dest = [45, 45]) == 231517492
    assert candidate(n = 100,m = 100,k = 1,source = [10, 10],dest = [90, 90]) == 0
    assert candidate(n = 12,m = 12,k = 25,source = [6, 6],dest = [12, 12]) == 90226411
    assert candidate(n = 10,m = 1,k = 5,source = [1, 1],dest = [10, 1]) == 5905
    assert candidate(n = 5,m = 5,k = 25,source = [3, 3],dest = [1, 1]) == 401190346
    assert candidate(n = 5,m = 5,k = 20,source = [3, 3],dest = [3, 3]) == 977897956
    assert candidate(n = 15,m = 20,k = 15,source = [4, 5],dest = [12, 18]) == 102993973
    assert candidate(n = 10,m = 1,k = 3,source = [1, 1],dest = [10, 1]) == 73
    assert candidate(n = 20,m = 15,k = 30,source = [1, 1],dest = [20, 15]) == 655472210
    assert candidate(n = 5,m = 5,k = 100,source = [2, 2],dest = [4, 4]) == 141053546
    assert candidate(n = 20,m = 20,k = 20,source = [10, 10],dest = [1, 1]) == 871858354
    assert candidate(n = 25,m = 25,k = 25,source = [1, 1],dest = [25, 25]) == 412879981
    assert candidate(n = 5,m = 5,k = 1,source = [1, 1],dest = [5, 5]) == 0
    assert candidate(n = 20,m = 15,k = 20,source = [1, 1],dest = [20, 15]) == 741151508
    assert candidate(n = 20,m = 20,k = 5,source = [15, 15],dest = [5, 5]) == 188640
    assert candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [25, 25]) == 507115071
    assert candidate(n = 1,m = 10,k = 10,source = [1, 1],dest = [1, 10]) == 348678440
    assert candidate(n = 9,m = 9,k = 50,source = [1, 1],dest = [9, 9]) == 897765280
    assert candidate(n = 500,m = 500,k = 100,source = [100, 100],dest = [400, 400]) == 883888844
    assert candidate(n = 100,m = 100,k = 100000,source = [50, 50],dest = [1, 1]) == 946728093
    assert candidate(n = 1000000000,m = 1000000000,k = 100000,source = [1, 1],dest = [1000000000, 1000000000]) == 965895368
    assert candidate(n = 50,m = 50,k = 15,source = [25, 25],dest = [40, 40]) == 17666803
    assert candidate(n = 5,m = 5,k = 10,source = [3, 3],dest = [1, 1]) == 42944990
    assert candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [40, 40]) == 33487513
    assert candidate(n = 10,m = 15,k = 12,source = [1, 1],dest = [10, 15]) == 716494581
    assert candidate(n = 50,m = 50,k = 50,source = [25, 25],dest = [1, 1]) == 33487513
    assert candidate(n = 9,m = 9,k = 10,source = [3, 3],dest = [7, 7]) == 567242851
    assert candidate(n = 100000,m = 100000,k = 5000,source = [1, 1],dest = [100000, 100000]) == 540993502
    assert candidate(n = 30,m = 30,k = 25,source = [10, 10],dest = [20, 20]) == 768390149
    assert candidate(n = 100,m = 100,k = 50,source = [10, 10],dest = [90, 90]) == 223177367
    assert candidate(n = 20,m = 20,k = 100,source = [10, 10],dest = [1, 1]) == 89970184
    assert candidate(n = 500000000,m = 1000000000,k = 100000,source = [250000000, 500000000],dest = [350000000, 750000000]) == 68996267
    assert candidate(n = 10,m = 1,k = 10,source = [1, 1],dest = [10, 1]) == 348678440
    assert candidate(n = 1000000,m = 1000000,k = 100000,source = [500000, 500000],dest = [500001, 500001]) == 851939950
    assert candidate(n = 100,m = 100,k = 15,source = [1, 1],dest = [100, 100]) == 70248680
    assert candidate(n = 100,m = 100,k = 50000,source = [1, 1],dest = [100, 100]) == 828829667
    assert candidate(n = 10000,m = 10000,k = 1000,source = [5000, 5000],dest = [7500, 7500]) == 922475845
    assert candidate(n = 100,m = 100,k = 100,source = [1, 1],dest = [100, 100]) == 271334151
    assert candidate(n = 1000,m = 1000,k = 1000,source = [500, 500],dest = [1, 1]) == 75187626
    assert candidate(n = 25,m = 25,k = 12,source = [1, 25],dest = [25, 1]) == 483870578
    assert candidate(n = 50,m = 50,k = 50,source = [10, 10],dest = [40, 40]) == 33487513
    assert candidate(n = 20,m = 15,k = 12,source = [5, 5],dest = [10, 10]) == 912731589
    assert candidate(n = 10,m = 10,k = 20,source = [1, 1],dest = [10, 10]) == 322125842
    assert candidate(n = 10,m = 10,k = 15,source = [1, 1],dest = [10, 10]) == 5072566
    assert candidate(n = 8,m = 7,k = 8,source = [1, 7],dest = [8, 1]) == 14529656
    assert candidate(n = 2000,m = 1000,k = 200,source = [1, 1],dest = [2000, 1000]) == 429645884
    assert candidate(n = 25,m = 25,k = 200,source = [5, 5],dest = [20, 20]) == 199868308
    assert candidate(n = 1,m = 10,k = 3,source = [1, 1],dest = [1, 10]) == 73
    assert candidate(n = 1000000000,m = 1000000000,k = 100000,source = [1, 1],dest = [1000000000, 1000000000]) == 965895368
    assert candidate(n = 50,m = 25,k = 20,source = [25, 13],dest = [10, 20]) == 479759219
    assert candidate(n = 9,m = 9,k = 9,source = [1, 9],dest = [9, 1]) == 847392210
    assert candidate(n = 1,m = 10,k = 5,source = [1, 1],dest = [1, 10]) == 5905
    assert candidate(n = 15,m = 15,k = 5,source = [2, 2],dest = [14, 14]) == 73190
    assert candidate(n = 12,m = 8,k = 10,source = [6, 4],dest = [2, 7]) == 87570173
    assert candidate(n = 10,m = 5,k = 20,source = [3, 2],dest = [7, 4]) == 920636278
    assert candidate(n = 2,m = 2,k = 4,source = [1, 1],dest = [2, 2]) == 8
    assert candidate(n = 5,m = 5,k = 10,source = [1, 1],dest = [5, 5]) == 42944990
    assert candidate(n = 50,m = 50,k = 1000,source = [25, 25],dest = [1, 1]) == 168759391
    assert candidate(n = 30,m = 30,k = 20,source = [1, 1],dest = [30, 30]) == 841565469
    assert candidate(n = 50,m = 50,k = 5,source = [25, 25],dest = [25, 25]) == 13603968
    assert candidate(n = 1000,m = 1000,k = 100,source = [500, 500],dest = [600, 600]) == 126893258
    assert candidate(n = 10,m = 10,k = 20,source = [5, 5],dest = [5, 5]) == 630244005
    assert candidate(n = 12,m = 12,k = 8,source = [6, 6],dest = [1, 1]) == 379693568


