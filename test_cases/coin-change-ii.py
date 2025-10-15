def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(amount = 20,coins = [1, 5, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 20,coins = [1, 5, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1,coins = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1,coins = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(amount = 0,coins = [1, 2, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 0,coins = [1, 2, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5000,coins = [1, 5, 10, 25, 50]) == 432699251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5000,coins = [1, 5, 10, 25, 50]) == 432699251: {e}')
    
    total += 1
    try:
        result = candidate(amount = 100,coins = [3, 7, 40, 9]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 100,coins = [3, 7, 40, 9]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(amount = 6249,coins = [186, 419, 83, 408]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 6249,coins = [186, 419, 83, 408]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(amount = 15,coins = [1, 3, 5, 7]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 15,coins = [1, 3, 5, 7]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(amount = 10,coins = [1, 3, 4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 10,coins = [1, 3, 4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(amount = 10,coins = [10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 10,coins = [10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(amount = 50,coins = [1, 18, 27, 34, 50]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 50,coins = [1, 18, 27, 34, 50]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5000,coins = [3, 5, 7, 8, 9, 10]) == 351757492460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5000,coins = [3, 5, 7, 8, 9, 10]) == 351757492460: {e}')
    
    total += 1
    try:
        result = candidate(amount = 100,coins = [3, 6, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 100,coins = [3, 6, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3,coins = [2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3,coins = [2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 25,coins = [1, 2, 5]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 25,coins = [1, 2, 5]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5,coins = [1, 2, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5,coins = [1, 2, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(amount = 100,coins = [1, 2, 5, 10, 20, 50]) == 4562
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 100,coins = [1, 2, 5, 10, 20, 50]) == 4562: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1000,coins = [3, 5, 7, 8, 9, 10, 11]) == 1952879228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1000,coins = [3, 5, 7, 8, 9, 10, 11]) == 1952879228: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [4, 12, 23, 34, 51]) == 1913606
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [4, 12, 23, 34, 51]) == 1913606: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1800,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 120836624716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1800,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 120836624716: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3500,coins = [50, 100, 150, 200, 250, 300, 350]) == 94425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3500,coins = [50, 100, 150, 200, 250, 300, 350]) == 94425: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2500,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2500,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2500,coins = [13, 17, 19, 23, 29, 31]) == 10673219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2500,coins = [13, 17, 19, 23, 29, 31]) == 10673219: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4500,coins = [23, 47, 61, 83, 97, 101]) == 358270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4500,coins = [23, 47, 61, 83, 97, 101]) == 358270: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4200,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4200,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [3, 9, 18, 36, 72, 144]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [3, 9, 18, 36, 72, 144]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 8000,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 8000,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3333,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 186150339220814
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3333,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 186150339220814: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1200,coins = [2, 5, 10, 25, 50, 100]) == 2459925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1200,coins = [2, 5, 10, 25, 50, 100]) == 2459925: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4500,coins = [11, 22, 33, 44, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4500,coins = [11, 22, 33, 44, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [11, 17, 29, 31]) == 8465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [11, 17, 29, 31]) == 8465: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [4, 9, 15, 25, 30, 50, 75]) == 816870821
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [4, 9, 15, 25, 30, 50, 75]) == 816870821: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3750,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 6877248457909551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3750,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 6877248457909551: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4800,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 402020904793077
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4800,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 402020904793077: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3500,coins = [1, 2, 5, 10, 20, 50, 100]) == 298945088016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3500,coins = [1, 2, 5, 10, 20, 50, 100]) == 298945088016: {e}')
    
    total += 1
    try:
        result = candidate(amount = 10000,coins = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 11569288968418829417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 10000,coins = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 11569288968418829417: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3750,coins = [125, 250, 500, 1000, 2000]) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3750,coins = [125, 250, 500, 1000, 2000]) == 166: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2750,coins = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49]) == 1980385268761
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2750,coins = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49]) == 1980385268761: {e}')
    
    total += 1
    try:
        result = candidate(amount = 6000,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1608946754650872
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 6000,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1608946754650872: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4500,coins = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]) == 17776167706
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4500,coins = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]) == 17776167706: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4500,coins = [5, 10, 20, 50, 100, 200]) == 94862488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4500,coins = [5, 10, 20, 50, 100, 200]) == 94862488: {e}')
    
    total += 1
    try:
        result = candidate(amount = 6000,coins = [11, 22, 33, 44, 55, 66]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 6000,coins = [11, 22, 33, 44, 55, 66]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5555,coins = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5555,coins = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2048,coins = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2320518947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2048,coins = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2320518947: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [1, 11, 13, 19, 21, 31, 37]) == 95941704933
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [1, 11, 13, 19, 21, 31, 37]) == 95941704933: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2700,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 385226325096527
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2700,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 385226325096527: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4999,coins = [1, 2, 5, 10, 25, 50, 100, 200, 500]) == 14978475244405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4999,coins = [1, 2, 5, 10, 25, 50, 100, 200, 500]) == 14978475244405: {e}')
    
    total += 1
    try:
        result = candidate(amount = 700,coins = [3, 7, 11, 13, 17, 19, 23, 29]) == 45005473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 700,coins = [3, 7, 11, 13, 17, 19, 23, 29]) == 45005473: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4500,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 171076578684392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4500,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 171076578684392: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2500,coins = [2, 3, 5, 7, 11, 13]) == 28227697415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2500,coins = [2, 3, 5, 7, 11, 13]) == 28227697415: {e}')
    
    total += 1
    try:
        result = candidate(amount = 500,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 500,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3500,coins = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1916917910649679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3500,coins = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1916917910649679: {e}')
    
    total += 1
    try:
        result = candidate(amount = 500,coins = [11, 22, 33, 44, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 500,coins = [11, 22, 33, 44, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 8000,coins = [1, 2, 5, 10, 20, 50, 100]) == 39042657518121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 8000,coins = [1, 2, 5, 10, 20, 50, 100]) == 39042657518121: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [3, 5, 7, 11, 13, 17, 19, 23]) == 38017360391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [3, 5, 7, 11, 13, 17, 19, 23]) == 38017360391: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3500,coins = [17, 23, 29, 31, 37]) == 519429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3500,coins = [17, 23, 29, 31, 37]) == 519429: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2700,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 35818551286815
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2700,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 35818551286815: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [50, 200, 500, 1000]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [50, 200, 500, 1000]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(amount = 500,coins = [11, 19, 29, 37, 47, 59, 71, 83]) == 3292
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 500,coins = [11, 19, 29, 37, 47, 59, 71, 83]) == 3292: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [1, 3, 7, 11]) == 5867703
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [1, 3, 7, 11]) == 5867703: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [15, 25, 35, 45, 55]) == 582580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [15, 25, 35, 45, 55]) == 582580: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5000,coins = [1, 4, 9, 16, 25, 36, 49]) == 928443384056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5000,coins = [1, 4, 9, 16, 25, 36, 49]) == 928443384056: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2500,coins = [7, 17, 27, 37, 47, 57, 67, 77]) == 115681732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2500,coins = [7, 17, 27, 37, 47, 57, 67, 77]) == 115681732: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [1, 3, 4, 12, 24, 48]) == 1799991438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [1, 3, 4, 12, 24, 48]) == 1799991438: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [2, 5, 10, 20, 50, 100]) == 238303231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [2, 5, 10, 20, 50, 100]) == 238303231: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5000,coins = [20, 25, 50, 100, 200, 500]) == 831886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5000,coins = [20, 25, 50, 100, 200, 500]) == 831886: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 19131722793601739
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 19131722793601739: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [33, 66, 99, 132, 165, 198, 231, 264, 297]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [33, 66, 99, 132, 165, 198, 231, 264, 297]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2222,coins = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 186150339220814
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2222,coins = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 186150339220814: {e}')
    
    total += 1
    try:
        result = candidate(amount = 200,coins = [1, 3, 5, 7, 9]) == 89740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 200,coins = [1, 3, 5, 7, 9]) == 89740: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4567,coins = [2, 5, 10, 20, 50]) == 188174063
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4567,coins = [2, 5, 10, 20, 50]) == 188174063: {e}')
    
    total += 1
    try:
        result = candidate(amount = 800,coins = [10, 20, 50, 100, 200, 500]) == 2064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 800,coins = [10, 20, 50, 100, 200, 500]) == 2064: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3333,coins = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103]) == 3570286683
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3333,coins = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103]) == 3570286683: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [10, 25, 50, 100, 200, 500]) == 29674
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [10, 25, 50, 100, 200, 500]) == 29674: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [5, 11, 17, 23, 29]) == 378081
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [5, 11, 17, 23, 29]) == 378081: {e}')
    
    total += 1
    try:
        result = candidate(amount = 6000,coins = [1, 2, 3, 5, 11, 23, 37, 41]) == 5179949524521356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 6000,coins = [1, 2, 3, 5, 11, 23, 37, 41]) == 5179949524521356: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [1, 10, 25, 50, 100, 200]) == 11051256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [1, 10, 25, 50, 100, 200]) == 11051256: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4999,coins = [1, 3, 9, 27, 81, 243, 729, 2187, 6561]) == 3946672836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4999,coins = [1, 3, 9, 27, 81, 243, 729, 2187, 6561]) == 3946672836: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1200,coins = [4, 8, 15, 16, 23, 42]) == 3481694
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1200,coins = [4, 8, 15, 16, 23, 42]) == 3481694: {e}')
    
    total += 1
    try:
        result = candidate(amount = 999,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 528165615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 999,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 528165615: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1111,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 1122054398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1111,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 1122054398: {e}')
    
    total += 1
    try:
        result = candidate(amount = 6666,coins = [1, 2, 3, 5, 8, 13, 21, 34, 55]) == 858790214643388609
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 6666,coins = [1, 2, 3, 5, 8, 13, 21, 34, 55]) == 858790214643388609: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [3, 5, 7, 9, 11, 13, 15]) == 2941614132296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [3, 5, 7, 9, 11, 13, 15]) == 2941614132296: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1234,coins = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 10948
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1234,coins = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 10948: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3500,coins = [1, 2, 4, 8, 16, 32, 64]) == 1356535733168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3500,coins = [1, 2, 4, 8, 16, 32, 64]) == 1356535733168: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 23221589514
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 23221589514: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1200,coins = [5, 15, 25, 50, 100, 200]) == 115862
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1200,coins = [5, 15, 25, 50, 100, 200]) == 115862: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [1, 3, 4, 10, 20, 50]) == 18144427661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [1, 3, 4, 10, 20, 50]) == 18144427661: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [2, 5, 11, 23, 47]) == 30080239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [2, 5, 11, 23, 47]) == 30080239: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3456,coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 35362292367933393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3456,coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 35362292367933393: {e}')
    
    total += 1
    try:
        result = candidate(amount = 800,coins = [5, 10, 20, 50, 100, 200]) == 38835
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 800,coins = [5, 10, 20, 50, 100, 200]) == 38835: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1234,coins = [1, 2, 5, 10, 20, 50, 100]) == 754797589
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1234,coins = [1, 2, 5, 10, 20, 50, 100]) == 754797589: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [11, 22, 33, 44, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [11, 22, 33, 44, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [7, 11, 13, 17, 19, 23]) == 40067247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [7, 11, 13, 17, 19, 23]) == 40067247: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1800,coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1067122993784732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1800,coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1067122993784732: {e}')
    
    total += 1
    try:
        result = candidate(amount = 7000,coins = [1, 5, 10, 25, 50, 100, 200, 500]) == 399576201827
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 7000,coins = [1, 5, 10, 25, 50, 100, 200, 500]) == 399576201827: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [8, 16, 24, 32, 40, 48, 56]) == 5078412464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [8, 16, 24, 32, 40, 48, 56]) == 5078412464: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [2, 5, 11, 25, 40, 60]) == 12079534
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [2, 5, 11, 25, 40, 60]) == 12079534: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1800,coins = [2, 6, 12, 18, 24, 30]) == 192387751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1800,coins = [2, 6, 12, 18, 24, 30]) == 192387751: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [7, 11, 13, 17, 19]) == 712518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [7, 11, 13, 17, 19]) == 712518: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3500,coins = [5, 15, 25, 35, 45, 55, 65, 75]) == 10998232465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3500,coins = [5, 15, 25, 35, 45, 55, 65, 75]) == 10998232465: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1234,coins = [3, 5, 7, 11, 13, 17, 19]) == 1209189166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1234,coins = [3, 5, 7, 11, 13, 17, 19]) == 1209189166: {e}')
    
    total += 1
    try:
        result = candidate(amount = 750,coins = [7, 14, 21, 28, 35, 42]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 750,coins = [7, 14, 21, 28, 35, 42]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [1, 3, 5, 7, 9, 11, 13]) == 707531982781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [1, 3, 5, 7, 9, 11, 13]) == 707531982781: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]) == 7799502297011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]) == 7799502297011: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [5, 10, 25, 50, 100]) == 9370181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [5, 10, 25, 50, 100]) == 9370181: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1800,coins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 79077323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1800,coins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 79077323: {e}')
    
    total += 1
    try:
        result = candidate(amount = 7777,coins = [13, 26, 39, 52, 65, 78, 91, 104, 117]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 7777,coins = [13, 26, 39, 52, 65, 78, 91, 104, 117]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 9000,coins = [15, 25, 35, 45, 55, 65]) == 1244874855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 9000,coins = [15, 25, 35, 45, 55, 65]) == 1244874855: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4000,coins = [7, 14, 21, 28, 35]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4000,coins = [7, 14, 21, 28, 35]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4321,coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8412107116918783059141522248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4321,coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8412107116918783059141522248: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [101, 103, 107, 109]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [101, 103, 107, 109]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2500,coins = [2, 5, 11, 17, 23, 29, 35, 41, 47]) == 623719935720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2500,coins = [2, 5, 11, 17, 23, 29, 35, 41, 47]) == 623719935720: {e}')
    
    total += 1
    try:
        result = candidate(amount = 500,coins = [1, 2, 5, 10, 20, 50, 100]) == 5824071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 500,coins = [1, 2, 5, 10, 20, 50, 100]) == 5824071: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5000,coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]) == 18682149631801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5000,coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]) == 18682149631801: {e}')
    
    total += 1
    try:
        result = candidate(amount = 2000,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 264830889564
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 2000,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 264830889564: {e}')
    
    total += 1
    try:
        result = candidate(amount = 4500,coins = [7, 13, 19, 23, 37, 41]) == 275308289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 4500,coins = [7, 13, 19, 23, 37, 41]) == 275308289: {e}')
    
    total += 1
    try:
        result = candidate(amount = 8888,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 15453068500547
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 8888,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 15453068500547: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1500,coins = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1500,coins = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 7000,coins = [3, 5, 7, 11, 13, 17, 19]) == 34788754338474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 7000,coins = [3, 5, 7, 11, 13, 17, 19]) == 34788754338474: {e}')
    
    total += 1
    try:
        result = candidate(amount = 3000,coins = [1, 3, 5, 10, 25, 50]) == 11669586691
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 3000,coins = [1, 3, 5, 10, 25, 50]) == 11669586691: {e}')
    
    total += 1
    try:
        result = candidate(amount = 1999,coins = [111, 222, 333, 444, 555, 666, 777, 888]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 1999,coins = [111, 222, 333, 444, 555, 666, 777, 888]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = 999,coins = [1, 2, 4, 8, 16, 32, 64]) == 944362512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 999,coins = [1, 2, 4, 8, 16, 32, 64]) == 944362512: {e}')
    
    total += 1
    try:
        result = candidate(amount = 6000,coins = [3, 6, 12, 24, 48, 96]) == 8807842176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 6000,coins = [3, 6, 12, 24, 48, 96]) == 8807842176: {e}')
    
    total += 1
    try:
        result = candidate(amount = 5000,coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 1027087367648016934506457070508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = 5000,coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 1027087367648016934506457070508: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(amount = 20,coins = [1, 5, 10]) == 9
    assert candidate(amount = 1,coins = [1]) == 1
    assert candidate(amount = 0,coins = [1, 2, 5]) == 1
    assert candidate(amount = 5000,coins = [1, 5, 10, 25, 50]) == 432699251
    assert candidate(amount = 100,coins = [3, 7, 40, 9]) == 48
    assert candidate(amount = 6249,coins = [186, 419, 83, 408]) == 19
    assert candidate(amount = 15,coins = [1, 3, 5, 7]) == 19
    assert candidate(amount = 10,coins = [1, 3, 4, 5]) == 12
    assert candidate(amount = 10,coins = [10]) == 1
    assert candidate(amount = 50,coins = [1, 18, 27, 34, 50]) == 7
    assert candidate(amount = 5000,coins = [3, 5, 7, 8, 9, 10]) == 351757492460
    assert candidate(amount = 100,coins = [3, 6, 9]) == 0
    assert candidate(amount = 3,coins = [2]) == 0
    assert candidate(amount = 25,coins = [1, 2, 5]) == 42
    assert candidate(amount = 5,coins = [1, 2, 5]) == 4
    assert candidate(amount = 100,coins = [1, 2, 5, 10, 20, 50]) == 4562
    assert candidate(amount = 1000,coins = [3, 5, 7, 8, 9, 10, 11]) == 1952879228
    assert candidate(amount = 3000,coins = [4, 12, 23, 34, 51]) == 1913606
    assert candidate(amount = 1800,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 120836624716
    assert candidate(amount = 3500,coins = [50, 100, 150, 200, 250, 300, 350]) == 94425
    assert candidate(amount = 2500,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
    assert candidate(amount = 2500,coins = [13, 17, 19, 23, 29, 31]) == 10673219
    assert candidate(amount = 4500,coins = [23, 47, 61, 83, 97, 101]) == 358270
    assert candidate(amount = 4200,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
    assert candidate(amount = 4000,coins = [3, 9, 18, 36, 72, 144]) == 0
    assert candidate(amount = 8000,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 0
    assert candidate(amount = 3333,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 186150339220814
    assert candidate(amount = 1200,coins = [2, 5, 10, 25, 50, 100]) == 2459925
    assert candidate(amount = 4500,coins = [11, 22, 33, 44, 55]) == 0
    assert candidate(amount = 2000,coins = [11, 17, 29, 31]) == 8465
    assert candidate(amount = 3000,coins = [4, 9, 15, 25, 30, 50, 75]) == 816870821
    assert candidate(amount = 3750,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 6877248457909551
    assert candidate(amount = 4800,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 402020904793077
    assert candidate(amount = 3500,coins = [1, 2, 5, 10, 20, 50, 100]) == 298945088016
    assert candidate(amount = 10000,coins = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 11569288968418829417
    assert candidate(amount = 3750,coins = [125, 250, 500, 1000, 2000]) == 166
    assert candidate(amount = 2750,coins = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49]) == 1980385268761
    assert candidate(amount = 6000,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1608946754650872
    assert candidate(amount = 4500,coins = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]) == 17776167706
    assert candidate(amount = 4500,coins = [5, 10, 20, 50, 100, 200]) == 94862488
    assert candidate(amount = 6000,coins = [11, 22, 33, 44, 55, 66]) == 0
    assert candidate(amount = 5555,coins = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 0
    assert candidate(amount = 2048,coins = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2320518947
    assert candidate(amount = 4000,coins = [1, 11, 13, 19, 21, 31, 37]) == 95941704933
    assert candidate(amount = 2700,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 385226325096527
    assert candidate(amount = 4999,coins = [1, 2, 5, 10, 25, 50, 100, 200, 500]) == 14978475244405
    assert candidate(amount = 700,coins = [3, 7, 11, 13, 17, 19, 23, 29]) == 45005473
    assert candidate(amount = 4500,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 171076578684392
    assert candidate(amount = 2500,coins = [2, 3, 5, 7, 11, 13]) == 28227697415
    assert candidate(amount = 500,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 0
    assert candidate(amount = 3500,coins = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1916917910649679
    assert candidate(amount = 500,coins = [11, 22, 33, 44, 55]) == 0
    assert candidate(amount = 8000,coins = [1, 2, 5, 10, 20, 50, 100]) == 39042657518121
    assert candidate(amount = 1500,coins = [3, 5, 7, 11, 13, 17, 19, 23]) == 38017360391
    assert candidate(amount = 3500,coins = [17, 23, 29, 31, 37]) == 519429
    assert candidate(amount = 2700,coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 35818551286815
    assert candidate(amount = 1500,coins = [50, 200, 500, 1000]) == 22
    assert candidate(amount = 500,coins = [11, 19, 29, 37, 47, 59, 71, 83]) == 3292
    assert candidate(amount = 2000,coins = [1, 3, 7, 11]) == 5867703
    assert candidate(amount = 3000,coins = [15, 25, 35, 45, 55]) == 582580
    assert candidate(amount = 5000,coins = [1, 4, 9, 16, 25, 36, 49]) == 928443384056
    assert candidate(amount = 2500,coins = [7, 17, 27, 37, 47, 57, 67, 77]) == 115681732
    assert candidate(amount = 2000,coins = [1, 3, 4, 12, 24, 48]) == 1799991438
    assert candidate(amount = 3000,coins = [2, 5, 10, 20, 50, 100]) == 238303231
    assert candidate(amount = 5000,coins = [20, 25, 50, 100, 200, 500]) == 831886
    assert candidate(amount = 4000,coins = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 19131722793601739
    assert candidate(amount = 3000,coins = [33, 66, 99, 132, 165, 198, 231, 264, 297]) == 0
    assert candidate(amount = 2222,coins = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 186150339220814
    assert candidate(amount = 200,coins = [1, 3, 5, 7, 9]) == 89740
    assert candidate(amount = 4567,coins = [2, 5, 10, 20, 50]) == 188174063
    assert candidate(amount = 800,coins = [10, 20, 50, 100, 200, 500]) == 2064
    assert candidate(amount = 3333,coins = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103]) == 3570286683
    assert candidate(amount = 2000,coins = [10, 25, 50, 100, 200, 500]) == 29674
    assert candidate(amount = 1500,coins = [5, 11, 17, 23, 29]) == 378081
    assert candidate(amount = 6000,coins = [1, 2, 3, 5, 11, 23, 37, 41]) == 5179949524521356
    assert candidate(amount = 3000,coins = [1, 10, 25, 50, 100, 200]) == 11051256
    assert candidate(amount = 4999,coins = [1, 3, 9, 27, 81, 243, 729, 2187, 6561]) == 3946672836
    assert candidate(amount = 1200,coins = [4, 8, 15, 16, 23, 42]) == 3481694
    assert candidate(amount = 999,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 528165615
    assert candidate(amount = 1111,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 1122054398
    assert candidate(amount = 6666,coins = [1, 2, 3, 5, 8, 13, 21, 34, 55]) == 858790214643388609
    assert candidate(amount = 4000,coins = [3, 5, 7, 9, 11, 13, 15]) == 2941614132296
    assert candidate(amount = 1234,coins = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 10948
    assert candidate(amount = 3500,coins = [1, 2, 4, 8, 16, 32, 64]) == 1356535733168
    assert candidate(amount = 1500,coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 23221589514
    assert candidate(amount = 1200,coins = [5, 15, 25, 50, 100, 200]) == 115862
    assert candidate(amount = 3000,coins = [1, 3, 4, 10, 20, 50]) == 18144427661
    assert candidate(amount = 3000,coins = [2, 5, 11, 23, 47]) == 30080239
    assert candidate(amount = 3456,coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 35362292367933393
    assert candidate(amount = 800,coins = [5, 10, 20, 50, 100, 200]) == 38835
    assert candidate(amount = 1234,coins = [1, 2, 5, 10, 20, 50, 100]) == 754797589
    assert candidate(amount = 4000,coins = [11, 22, 33, 44, 55]) == 0
    assert candidate(amount = 2000,coins = [7, 11, 13, 17, 19, 23]) == 40067247
    assert candidate(amount = 1800,coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1067122993784732
    assert candidate(amount = 7000,coins = [1, 5, 10, 25, 50, 100, 200, 500]) == 399576201827
    assert candidate(amount = 4000,coins = [8, 16, 24, 32, 40, 48, 56]) == 5078412464
    assert candidate(amount = 1500,coins = [2, 5, 11, 25, 40, 60]) == 12079534
    assert candidate(amount = 1800,coins = [2, 6, 12, 18, 24, 30]) == 192387751
    assert candidate(amount = 1500,coins = [7, 11, 13, 17, 19]) == 712518
    assert candidate(amount = 3500,coins = [5, 15, 25, 35, 45, 55, 65, 75]) == 10998232465
    assert candidate(amount = 1234,coins = [3, 5, 7, 11, 13, 17, 19]) == 1209189166
    assert candidate(amount = 750,coins = [7, 14, 21, 28, 35, 42]) == 0
    assert candidate(amount = 2000,coins = [1, 3, 5, 7, 9, 11, 13]) == 707531982781
    assert candidate(amount = 4000,coins = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]) == 7799502297011
    assert candidate(amount = 4000,coins = [5, 10, 25, 50, 100]) == 9370181
    assert candidate(amount = 1800,coins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 79077323
    assert candidate(amount = 7777,coins = [13, 26, 39, 52, 65, 78, 91, 104, 117]) == 0
    assert candidate(amount = 9000,coins = [15, 25, 35, 45, 55, 65]) == 1244874855
    assert candidate(amount = 4000,coins = [7, 14, 21, 28, 35]) == 0
    assert candidate(amount = 4321,coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8412107116918783059141522248
    assert candidate(amount = 2000,coins = [101, 103, 107, 109]) == 0
    assert candidate(amount = 2500,coins = [2, 5, 11, 17, 23, 29, 35, 41, 47]) == 623719935720
    assert candidate(amount = 500,coins = [1, 2, 5, 10, 20, 50, 100]) == 5824071
    assert candidate(amount = 5000,coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]) == 18682149631801
    assert candidate(amount = 2000,coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 264830889564
    assert candidate(amount = 4500,coins = [7, 13, 19, 23, 37, 41]) == 275308289
    assert candidate(amount = 8888,coins = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 15453068500547
    assert candidate(amount = 1500,coins = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 0
    assert candidate(amount = 7000,coins = [3, 5, 7, 11, 13, 17, 19]) == 34788754338474
    assert candidate(amount = 3000,coins = [1, 3, 5, 10, 25, 50]) == 11669586691
    assert candidate(amount = 1999,coins = [111, 222, 333, 444, 555, 666, 777, 888]) == 0
    assert candidate(amount = 999,coins = [1, 2, 4, 8, 16, 32, 64]) == 944362512
    assert candidate(amount = 6000,coins = [3, 6, 12, 24, 48, 96]) == 8807842176
    assert candidate(amount = 5000,coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 1027087367648016934506457070508


