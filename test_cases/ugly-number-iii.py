def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,a = 2,b = 3,c = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,a = 2,b = 3,c = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,a = 1000000000,b = 1000000000,c = 1000000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,a = 1000000000,b = 1000000000,c = 1000000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,a = 2,b = 3,c = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,a = 2,b = 3,c = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,a = 2,b = 3,c = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,a = 2,b = 3,c = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 2,b = 7,c = 13) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 2,b = 7,c = 13) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 5,b = 7,c = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 5,b = 7,c = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 6,b = 8,c = 14) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 6,b = 8,c = 14) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,a = 2,b = 11,c = 13) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,a = 2,b = 11,c = 13) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 217983653,c = 336916467) == 2000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 217983653,c = 336916467) == 2000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 6,b = 7,c = 8) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 6,b = 7,c = 8) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 11,b = 17,c = 19) == 5279350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 11,b = 17,c = 19) == 5279350: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 15,b = 25,c = 35) == 925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 15,b = 25,c = 35) == 925: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,a = 41,b = 89,c = 97) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,a = 41,b = 89,c = 97) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 10,b = 20,c = 30) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 10,b = 20,c = 30) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,a = 17,b = 23,c = 29) == 3822991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,a = 17,b = 23,c = 29) == 3822991: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 7,b = 17,c = 19) == 4242027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 7,b = 17,c = 19) == 4242027: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,a = 7,b = 11,c = 13) == 1782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,a = 7,b = 11,c = 13) == 1782: {e}')
    
    total += 1
    try:
        result = candidate(n = 89,a = 23,b = 31,c = 41) == 902
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89,a = 23,b = 31,c = 41) == 902: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,a = 7,b = 11,c = 13) == 1781136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,a = 7,b = 11,c = 13) == 1781136: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 13,b = 17,c = 19) == 5651417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 13,b = 17,c = 19) == 5651417: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 23,b = 47,c = 83) == 1328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 23,b = 47,c = 83) == 1328: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,a = 12,b = 18,c = 30) == 204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,a = 12,b = 18,c = 30) == 204: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000,a = 89,b = 97,c = 101) == 6427123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000,a = 89,b = 97,c = 101) == 6427123: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 11,c = 17) == 1747664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 11,c = 17) == 1747664: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,a = 11,b = 19,c = 29) == 59367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,a = 11,b = 19,c = 29) == 59367: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 17,c = 19) == 2465649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 17,c = 19) == 2465649: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999,a = 5,b = 6,c = 7) == 2333330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999,a = 5,b = 6,c = 7) == 2333330: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500,a = 2,b = 5,c = 17) == 2405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500,a = 2,b = 5,c = 17) == 2405: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 11,c = 17) == 2327802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 11,c = 17) == 2327802: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 10,b = 15,c = 20) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 10,b = 15,c = 20) == 750: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 13,b = 17,c = 19) == 565148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 13,b = 17,c = 19) == 565148: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 999999937,b = 999999931,c = 999999929) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 999999937,b = 999999931,c = 999999929) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 5,b = 7,c = 11) == 265518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 5,b = 7,c = 11) == 265518: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 11,b = 13,c = 17) == 475735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 11,b = 13,c = 17) == 475735: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,a = 11,b = 19,c = 23) == 2838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,a = 11,b = 19,c = 23) == 2838: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 5,b = 11,c = 13) == 3042555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 5,b = 11,c = 13) == 3042555: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 7,c = 13) == 2116281
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 7,c = 13) == 2116281: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000,a = 29,b = 61,c = 67) == 155073912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000,a = 29,b = 61,c = 67) == 155073912: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,a = 17,b = 23,c = 29) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,a = 17,b = 23,c = 29) == 374: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,a = 3,b = 5,c = 7) == 2274202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,a = 3,b = 5,c = 7) == 2274202: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 11,b = 13,c = 19) == 4877917
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 11,b = 13,c = 19) == 4877917: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000,a = 47,b = 53,c = 61) == 4505704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000,a = 47,b = 53,c = 61) == 4505704: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,a = 11,b = 13,c = 17) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,a = 11,b = 13,c = 17) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,a = 4,b = 6,c = 8) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,a = 4,b = 6,c = 8) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000,a = 13,b = 17,c = 19) == 1130285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000,a = 13,b = 17,c = 19) == 1130285: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999,a = 2,b = 3,c = 4) == 1499998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999,a = 2,b = 3,c = 4) == 1499998: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 31,b = 37,c = 41) == 1228811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 31,b = 37,c = 41) == 1228811: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,a = 3,b = 1000000000,c = 1000000001) == 1500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,a = 3,b = 1000000000,c = 1000000001) == 1500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 7,b = 13,c = 17) == 391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 7,b = 13,c = 17) == 391: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000,a = 31,b = 37,c = 41) == 9216182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000,a = 31,b = 37,c = 41) == 9216182: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000,a = 3,b = 5,c = 7) == 18421053
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000,a = 3,b = 5,c = 7) == 18421053: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,a = 2,b = 3,c = 5) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,a = 2,b = 3,c = 5) == 205: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,a = 2,b = 217983653,c = 336916467) == 999999994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,a = 2,b = 217983653,c = 336916467) == 999999994: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 7,b = 14,c = 21) == 7000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 7,b = 14,c = 21) == 7000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 4,b = 6,c = 8) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 4,b = 6,c = 8) == 300: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,a = 19,b = 23,c = 29) == 399779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,a = 19,b = 23,c = 29) == 399779: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,a = 4,b = 6,c = 8) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,a = 4,b = 6,c = 8) == 750: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 11,b = 13,c = 17) == 4757346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 11,b = 13,c = 17) == 4757346: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654,a = 1000000,b = 2000000,c = 3000000) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654,a = 1000000,b = 2000000,c = 3000000) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,a = 17,b = 23,c = 29) == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,a = 17,b = 23,c = 29) == 230: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000,a = 11,b = 19,c = 29) == 11872682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000,a = 11,b = 19,c = 29) == 11872682: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,a = 10,b = 15,c = 20) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,a = 10,b = 15,c = 20) == 375: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000,a = 37,b = 79,c = 83) == 981984141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000,a = 37,b = 79,c = 83) == 981984141: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,a = 6,b = 14,c = 21) == 3150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,a = 6,b = 14,c = 21) == 3150: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 2,b = 3,c = 5) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 2,b = 3,c = 5) == 136: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 4,c = 8) == 2000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 4,c = 8) == 2000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,a = 13,b = 17,c = 19) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,a = 13,b = 17,c = 19) == 285: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000,a = 13,b = 17,c = 19) == 847717
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000,a = 13,b = 17,c = 19) == 847717: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 999999937,b = 999999931,c = 999999919) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 999999937,b = 999999931,c = 999999919) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,a = 3,b = 5,c = 7) == 92105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,a = 3,b = 5,c = 7) == 92105: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 3,b = 7,c = 11) == 2082
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 3,b = 7,c = 11) == 2082: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 3,c = 7) == 1400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 3,c = 7) == 1400000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 5,c = 7) == 1521738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 5,c = 7) == 1521738: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999,a = 23,b = 31,c = 41) == 10318743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999,a = 23,b = 31,c = 41) == 10318743: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 2,b = 3,c = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 2,b = 3,c = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,a = 3,b = 5,c = 7) == 1842105261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,a = 3,b = 5,c = 7) == 1842105261: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 7,b = 11,c = 13) == 3562279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 7,b = 11,c = 13) == 3562279: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000,a = 3,b = 5,c = 7) == 3684212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000,a = 3,b = 5,c = 7) == 3684212: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,a = 9,b = 21,c = 28) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,a = 9,b = 21,c = 28) == 180: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,a = 25,b = 45,c = 65) == 7276125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,a = 25,b = 45,c = 65) == 7276125: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 1000000000,b = 1000000000,c = 1000000000) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 1000000000,b = 1000000000,c = 1000000000) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000,a = 123456789,b = 987654321,c = 1122334455) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000,a = 123456789,b = 987654321,c = 1122334455) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 17,c = 19) == 1804468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 17,c = 19) == 1804468: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 13,c = 19) == 1776978
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 13,c = 19) == 1776978: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,a = 17,b = 37,c = 41) == 46904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,a = 17,b = 37,c = 41) == 46904: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 6,c = 9) == 3000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 6,c = 9) == 3000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 123,b = 456,c = 789) == 86838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 123,b = 456,c = 789) == 86838: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,a = 6,b = 10,c = 15) == 1875000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,a = 6,b = 10,c = 15) == 1875000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 4,b = 9,c = 25) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 4,b = 9,c = 25) == 276: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000,a = 59,b = 61,c = 67) == 12632448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000,a = 59,b = 61,c = 67) == 12632448: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000,a = 3,b = 5,c = 11) == 582354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000,a = 3,b = 5,c = 11) == 582354: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,a = 3,b = 3,c = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,a = 3,b = 3,c = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 5,c = 11) == 1941177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 5,c = 11) == 1941177: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,a = 2,b = 2,c = 3) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,a = 2,b = 2,c = 3) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,a = 5,b = 7,c = 11) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,a = 5,b = 7,c = 11) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000,a = 2,b = 3,c = 6) == 1125000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000,a = 2,b = 3,c = 6) == 1125000: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,a = 2,b = 2,c = 3) == 750000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,a = 2,b = 2,c = 3) == 750000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 11,b = 22,c = 33) == 11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 11,b = 22,c = 33) == 11000: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,a = 4,b = 6,c = 8) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,a = 4,b = 6,c = 8) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 1000000000,b = 999999999,c = 999999998) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 1000000000,b = 999999999,c = 999999998) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,a = 7,b = 11,c = 13) == 714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,a = 7,b = 11,c = 13) == 714: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,a = 3,b = 5,c = 7) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,a = 3,b = 5,c = 7) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,a = 9,b = 14,c = 21) == 26250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,a = 9,b = 14,c = 21) == 26250: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 7,c = 13) == 1654546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 7,c = 13) == 1654546: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,a = 100,b = 200,c = 300) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,a = 100,b = 200,c = 300) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 13,c = 19) == 2398058
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 13,c = 19) == 2398058: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 5,b = 10,c = 15) == 5000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 5,b = 10,c = 15) == 5000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,a = 2,b = 4,c = 8) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,a = 2,b = 4,c = 8) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 23,b = 53,c = 59) == 12914523
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 23,b = 53,c = 59) == 12914523: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 5,b = 7,c = 11) == 2655170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 5,b = 7,c = 11) == 2655170: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 5,b = 17,c = 19) == 3488125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 5,b = 17,c = 19) == 3488125: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000,a = 17,b = 23,c = 29) == 5734491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000,a = 17,b = 23,c = 29) == 5734491: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500,a = 8,b = 15,c = 20) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500,a = 8,b = 15,c = 20) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 1000000000,b = 1000000000,c = 1000000000) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 1000000000,b = 1000000000,c = 1000000000) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,a = 5,b = 17,c = 19) == 1745
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,a = 5,b = 17,c = 19) == 1745: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000,a = 29,b = 31,c = 37) == 8802636
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000,a = 29,b = 31,c = 37) == 8802636: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,a = 19,b = 43,c = 47) == 1059864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,a = 19,b = 43,c = 47) == 1059864: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,a = 7,b = 11,c = 13) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,a = 7,b = 11,c = 13) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000000,a = 31,b = 71,c = 73) == 339223049
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000000,a = 31,b = 71,c = 73) == 339223049: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,a = 2,b = 3,c = 5) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,a = 2,b = 3,c = 5) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000,a = 1000000,b = 1000001,c = 1000002) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000,a = 1000000,b = 1000001,c = 1000002) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,a = 4,b = 6,c = 8) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,a = 4,b = 6,c = 8) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 2,b = 5,c = 11) == 1571428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 2,b = 5,c = 11) == 1571428: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 7,b = 13,c = 17) == 3916458
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 7,b = 13,c = 17) == 3916458: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,a = 11,b = 13,c = 17) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,a = 11,b = 13,c = 17) == 117: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 13,b = 29,c = 31) == 7280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 13,b = 29,c = 31) == 7280: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,a = 10,b = 11,c = 12) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,a = 10,b = 11,c = 12) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,a = 7,b = 11,c = 13) == 35623
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,a = 7,b = 11,c = 13) == 35623: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 3,b = 5,c = 7) == 1842106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 3,b = 5,c = 7) == 1842106: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000,a = 5,b = 10,c = 15) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000,a = 5,b = 10,c = 15) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,a = 4,b = 6,c = 8) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,a = 4,b = 6,c = 8) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,a = 5,b = 13,c = 17) == 3278930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,a = 5,b = 13,c = 17) == 3278930: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,a = 10,b = 15,c = 20) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,a = 10,b = 15,c = 20) == 45: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,a = 2,b = 3,c = 4) == 6
    assert candidate(n = 1,a = 1000000000,b = 1000000000,c = 1000000000) == 1000000000
    assert candidate(n = 1,a = 2,b = 3,c = 5) == 2
    assert candidate(n = 3,a = 2,b = 3,c = 5) == 4
    assert candidate(n = 10,a = 2,b = 7,c = 13) == 16
    assert candidate(n = 10,a = 5,b = 7,c = 15) == 30
    assert candidate(n = 10,a = 6,b = 8,c = 14) == 32
    assert candidate(n = 5,a = 2,b = 11,c = 13) == 10
    assert candidate(n = 1000000,a = 2,b = 217983653,c = 336916467) == 2000000
    assert candidate(n = 10,a = 6,b = 7,c = 8) == 28
    assert candidate(n = 1000000,a = 11,b = 17,c = 19) == 5279350
    assert candidate(n = 100,a = 15,b = 25,c = 35) == 925
    assert candidate(n = 100000000,a = 41,b = 89,c = 97) == 2000000000
    assert candidate(n = 1000,a = 10,b = 20,c = 30) == 10000
    assert candidate(n = 500000,a = 17,b = 23,c = 29) == 3822991
    assert candidate(n = 1000000,a = 7,b = 17,c = 19) == 4242027
    assert candidate(n = 500,a = 7,b = 11,c = 13) == 1782
    assert candidate(n = 89,a = 23,b = 31,c = 41) == 902
    assert candidate(n = 500000,a = 7,b = 11,c = 13) == 1781136
    assert candidate(n = 1000000,a = 13,b = 17,c = 19) == 5651417
    assert candidate(n = 100,a = 23,b = 47,c = 83) == 1328
    assert candidate(n = 25,a = 12,b = 18,c = 30) == 204
    assert candidate(n = 200000,a = 89,b = 97,c = 101) == 6427123
    assert candidate(n = 1000000,a = 2,b = 11,c = 17) == 1747664
    assert candidate(n = 10000,a = 11,b = 19,c = 29) == 59367
    assert candidate(n = 1000000,a = 3,b = 17,c = 19) == 2465649
    assert candidate(n = 999999,a = 5,b = 6,c = 7) == 2333330
    assert candidate(n = 1500,a = 2,b = 5,c = 17) == 2405
    assert candidate(n = 1000000,a = 3,b = 11,c = 17) == 2327802
    assert candidate(n = 100,a = 10,b = 15,c = 20) == 750
    assert candidate(n = 100000,a = 13,b = 17,c = 19) == 565148
    assert candidate(n = 1000000,a = 999999937,b = 999999931,c = 999999929) == 2000000000
    assert candidate(n = 100000,a = 5,b = 7,c = 11) == 265518
    assert candidate(n = 100000,a = 11,b = 13,c = 17) == 475735
    assert candidate(n = 500,a = 11,b = 19,c = 23) == 2838
    assert candidate(n = 1000000,a = 5,b = 11,c = 13) == 3042555
    assert candidate(n = 1000000,a = 3,b = 7,c = 13) == 2116281
    assert candidate(n = 10000000,a = 29,b = 61,c = 67) == 155073912
    assert candidate(n = 50,a = 17,b = 23,c = 29) == 374
    assert candidate(n = 1234567,a = 3,b = 5,c = 7) == 2274202
    assert candidate(n = 1000000,a = 11,b = 13,c = 19) == 4877917
    assert candidate(n = 250000,a = 47,b = 53,c = 61) == 4505704
    assert candidate(n = 7,a = 11,b = 13,c = 17) == 34
    assert candidate(n = 30,a = 4,b = 6,c = 8) == 90
    assert candidate(n = 200000,a = 13,b = 17,c = 19) == 1130285
    assert candidate(n = 999999,a = 2,b = 3,c = 4) == 1499998
    assert candidate(n = 100000,a = 31,b = 37,c = 41) == 1228811
    assert candidate(n = 500000,a = 3,b = 1000000000,c = 1000000001) == 1500000
    assert candidate(n = 100,a = 7,b = 13,c = 17) == 391
    assert candidate(n = 750000,a = 31,b = 37,c = 41) == 9216182
    assert candidate(n = 10000000,a = 3,b = 5,c = 7) == 18421053
    assert candidate(n = 150,a = 2,b = 3,c = 5) == 205
    assert candidate(n = 500000000,a = 2,b = 217983653,c = 336916467) == 999999994
    assert candidate(n = 1000000,a = 7,b = 14,c = 21) == 7000000
    assert candidate(n = 100,a = 4,b = 6,c = 8) == 300
    assert candidate(n = 50000,a = 19,b = 23,c = 29) == 399779
    assert candidate(n = 250,a = 4,b = 6,c = 8) == 750
    assert candidate(n = 1000000,a = 11,b = 13,c = 17) == 4757346
    assert candidate(n = 987654,a = 1000000,b = 2000000,c = 3000000) == 2000000000
    assert candidate(n = 30,a = 17,b = 23,c = 29) == 230
    assert candidate(n = 2000000,a = 11,b = 19,c = 29) == 11872682
    assert candidate(n = 50,a = 10,b = 15,c = 20) == 375
    assert candidate(n = 50000000,a = 37,b = 79,c = 83) == 981984141
    assert candidate(n = 750,a = 6,b = 14,c = 21) == 3150
    assert candidate(n = 100,a = 2,b = 3,c = 5) == 136
    assert candidate(n = 1000000,a = 2,b = 4,c = 8) == 2000000
    assert candidate(n = 50,a = 13,b = 17,c = 19) == 285
    assert candidate(n = 150000,a = 13,b = 17,c = 19) == 847717
    assert candidate(n = 100000,a = 999999937,b = 999999931,c = 999999919) == 2000000000
    assert candidate(n = 50000,a = 3,b = 5,c = 7) == 92105
    assert candidate(n = 1000,a = 3,b = 7,c = 11) == 2082
    assert candidate(n = 1000000,a = 2,b = 3,c = 7) == 1400000
    assert candidate(n = 1000000,a = 2,b = 5,c = 7) == 1521738
    assert candidate(n = 999999,a = 23,b = 31,c = 41) == 10318743
    assert candidate(n = 10,a = 2,b = 3,c = 5) == 14
    assert candidate(n = 999999999,a = 3,b = 5,c = 7) == 1842105261
    assert candidate(n = 1000000,a = 7,b = 11,c = 13) == 3562279
    assert candidate(n = 2000000,a = 3,b = 5,c = 7) == 3684212
    assert candidate(n = 30,a = 9,b = 21,c = 28) == 180
    assert candidate(n = 500000,a = 25,b = 45,c = 65) == 7276125
    assert candidate(n = 1000000,a = 1000000000,b = 1000000000,c = 1000000000) == 2000000000
    assert candidate(n = 2000000,a = 123456789,b = 987654321,c = 1122334455) == 2000000000
    assert candidate(n = 1000000,a = 2,b = 17,c = 19) == 1804468
    assert candidate(n = 1000000,a = 2,b = 13,c = 19) == 1776978
    assert candidate(n = 5000,a = 17,b = 37,c = 41) == 46904
    assert candidate(n = 1000000,a = 3,b = 6,c = 9) == 3000000
    assert candidate(n = 1000,a = 123,b = 456,c = 789) == 86838
    assert candidate(n = 500000,a = 6,b = 10,c = 15) == 1875000
    assert candidate(n = 100,a = 4,b = 9,c = 25) == 276
    assert candidate(n = 600000,a = 59,b = 61,c = 67) == 12632448
    assert candidate(n = 300000,a = 3,b = 5,c = 11) == 582354
    assert candidate(n = 10,a = 3,b = 3,c = 3) == 30
    assert candidate(n = 1000000,a = 3,b = 5,c = 11) == 1941177
    assert candidate(n = 100,a = 2,b = 2,c = 3) == 150
    assert candidate(n = 7,a = 5,b = 7,c = 11) == 20
    assert candidate(n = 750000,a = 2,b = 3,c = 6) == 1125000
    assert candidate(n = 500000,a = 2,b = 2,c = 3) == 750000
    assert candidate(n = 1000,a = 11,b = 22,c = 33) == 11000
    assert candidate(n = 50,a = 4,b = 6,c = 8) == 150
    assert candidate(n = 1000000000,a = 1000000000,b = 999999999,c = 999999998) == 2000000000
    assert candidate(n = 200,a = 7,b = 11,c = 13) == 714
    assert candidate(n = 20,a = 3,b = 5,c = 7) == 36
    assert candidate(n = 5000,a = 9,b = 14,c = 21) == 26250
    assert candidate(n = 1000000,a = 2,b = 7,c = 13) == 1654546
    assert candidate(n = 500,a = 100,b = 200,c = 300) == 50000
    assert candidate(n = 1000000,a = 3,b = 13,c = 19) == 2398058
    assert candidate(n = 1000000,a = 5,b = 10,c = 15) == 5000000
    assert candidate(n = 50,a = 2,b = 4,c = 8) == 100
    assert candidate(n = 1000000,a = 23,b = 53,c = 59) == 12914523
    assert candidate(n = 1000000,a = 5,b = 7,c = 11) == 2655170
    assert candidate(n = 1000000,a = 5,b = 17,c = 19) == 3488125
    assert candidate(n = 750000,a = 17,b = 23,c = 29) == 5734491
    assert candidate(n = 2500,a = 8,b = 15,c = 20) == 12500
    assert candidate(n = 1000,a = 1000000000,b = 1000000000,c = 1000000000) == 2000000000
    assert candidate(n = 500,a = 5,b = 17,c = 19) == 1745
    assert candidate(n = 800000,a = 29,b = 31,c = 37) == 8802636
    assert candidate(n = 100000,a = 19,b = 43,c = 47) == 1059864
    assert candidate(n = 30,a = 7,b = 11,c = 13) == 105
    assert candidate(n = 20000000,a = 31,b = 71,c = 73) == 339223049
    assert candidate(n = 20,a = 2,b = 3,c = 5) == 27
    assert candidate(n = 10000000,a = 1000000,b = 1000001,c = 1000002) == 2000000000
    assert candidate(n = 15,a = 4,b = 6,c = 8) == 44
    assert candidate(n = 1000000,a = 2,b = 5,c = 11) == 1571428
    assert candidate(n = 1000000,a = 7,b = 13,c = 17) == 3916458
    assert candidate(n = 25,a = 11,b = 13,c = 17) == 117
    assert candidate(n = 1000,a = 13,b = 29,c = 31) == 7280
    assert candidate(n = 1000000000,a = 10,b = 11,c = 12) == 2000000000
    assert candidate(n = 10000,a = 7,b = 11,c = 13) == 35623
    assert candidate(n = 1000000,a = 3,b = 5,c = 7) == 1842106
    assert candidate(n = 2000000,a = 5,b = 10,c = 15) == 10000000
    assert candidate(n = 1000,a = 4,b = 6,c = 8) == 3000
    assert candidate(n = 1000000,a = 5,b = 13,c = 17) == 3278930
    assert candidate(n = 6,a = 10,b = 15,c = 20) == 45


