def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 987654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 987654321: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 923456781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 923456781: {e}')
    
    total += 1
    try:
        result = candidate(num = 12) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12) == 21: {e}')
    
    total += 1
    try:
        result = candidate(num = 21) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 21) == 21: {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 98368) == 98863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98368) == 98863: {e}')
    
    total += 1
    try:
        result = candidate(num = 1099511628) == 9091511628
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1099511628) == 9091511628: {e}')
    
    total += 1
    try:
        result = candidate(num = 11111) == 11111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11111) == 11111: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(num = 9973) == 9973
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9973) == 9973: {e}')
    
    total += 1
    try:
        result = candidate(num = 1099511627776) == 9091511627776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1099511627776) == 9091511627776: {e}')
    
    total += 1
    try:
        result = candidate(num = 1993) == 9913
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1993) == 9913: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num = 2736) == 7236
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2736) == 7236: {e}')
    
    total += 1
    try:
        result = candidate(num = 1099511625) == 9091511625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1099511625) == 9091511625: {e}')
    
    total += 1
    try:
        result = candidate(num = 567894321) == 967854321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567894321) == 967854321: {e}')
    
    total += 1
    try:
        result = candidate(num = 654321789) == 954321786
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 654321789) == 954321786: {e}')
    
    total += 1
    try:
        result = candidate(num = 33221100) == 33221100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33221100) == 33221100: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765456789) == 99765456788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765456789) == 99765456788: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 199983) == 999183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199983) == 999183: {e}')
    
    total += 1
    try:
        result = candidate(num = 5639953) == 9639553
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5639953) == 9639553: {e}')
    
    total += 1
    try:
        result = candidate(num = 123321321) == 323321121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123321321) == 323321121: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876554321) == 9876554321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876554321) == 9876554321: {e}')
    
    total += 1
    try:
        result = candidate(num = 12321) == 32121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12321) == 32121: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101) == 111010100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101) == 111010100: {e}')
    
    total += 1
    try:
        result = candidate(num = 900000000) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 900000000) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 109090909) == 909090901
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 109090909) == 909090901: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222221) == 222222221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222221) == 222222221: {e}')
    
    total += 1
    try:
        result = candidate(num = 9834321) == 9843321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9834321) == 9843321: {e}')
    
    total += 1
    try:
        result = candidate(num = 199999) == 999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199999) == 999991: {e}')
    
    total += 1
    try:
        result = candidate(num = 98877665544332211) == 98877665544332211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98877665544332211) == 98877665544332211: {e}')
    
    total += 1
    try:
        result = candidate(num = 4201) == 4210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4201) == 4210: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111119) == 911111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111119) == 911111111: {e}')
    
    total += 1
    try:
        result = candidate(num = 32123) == 33122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32123) == 33122: {e}')
    
    total += 1
    try:
        result = candidate(num = 583214769) == 983214765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 583214769) == 983214765: {e}')
    
    total += 1
    try:
        result = candidate(num = 319872654) == 913872654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 319872654) == 913872654: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333) == 333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333) == 333333: {e}')
    
    total += 1
    try:
        result = candidate(num = 891234567) == 981234567
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 891234567) == 981234567: {e}')
    
    total += 1
    try:
        result = candidate(num = 22773388) == 82773382
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 22773388) == 82773382: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333) == 311222331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333) == 311222331: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765) == 98765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765) == 98765: {e}')
    
    total += 1
    try:
        result = candidate(num = 1119111) == 9111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1119111) == 9111111: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111112) == 211111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111112) == 211111111: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999990) == 999999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999990) == 999999990: {e}')
    
    total += 1
    try:
        result = candidate(num = 2736589) == 9736582
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2736589) == 9736582: {e}')
    
    total += 1
    try:
        result = candidate(num = 109890) == 909810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 109890) == 909810: {e}')
    
    total += 1
    try:
        result = candidate(num = 432109876) == 932104876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 432109876) == 932104876: {e}')
    
    total += 1
    try:
        result = candidate(num = 983476521) == 987436521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 983476521) == 987436521: {e}')
    
    total += 1
    try:
        result = candidate(num = 34521) == 54321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 34521) == 54321: {e}')
    
    total += 1
    try:
        result = candidate(num = 33333333) == 33333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33333333) == 33333333: {e}')
    
    total += 1
    try:
        result = candidate(num = 1098765432) == 9018765432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1098765432) == 9018765432: {e}')
    
    total += 1
    try:
        result = candidate(num = 239187654) == 932187654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 239187654) == 932187654: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321987654321) == 997654321887654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321987654321) == 997654321887654321: {e}')
    
    total += 1
    try:
        result = candidate(num = 227368) == 827362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 227368) == 827362: {e}')
    
    total += 1
    try:
        result = candidate(num = 1122334455) == 5122334451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1122334455) == 5122334451: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 564999) == 964995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 564999) == 964995: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 898989898) == 998989888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 898989898) == 998989888: {e}')
    
    total += 1
    try:
        result = candidate(num = 983210987) == 993210887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 983210987) == 993210887: {e}')
    
    total += 1
    try:
        result = candidate(num = 98769876) == 99768876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98769876) == 99768876: {e}')
    
    total += 1
    try:
        result = candidate(num = 765432198) == 965432178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 765432198) == 965432178: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222) == 222222222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222) == 222222222: {e}')
    
    total += 1
    try:
        result = candidate(num = 199321123) == 991321123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199321123) == 991321123: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 819293818) == 919283818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 819293818) == 919283818: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210) == 9876543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210) == 9876543210: {e}')
    
    total += 1
    try:
        result = candidate(num = 1999991) == 9999911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1999991) == 9999911: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333333) == 333333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333333) == 333333333: {e}')
    
    total += 1
    try:
        result = candidate(num = 323232323) == 333232322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 323232323) == 333232322: {e}')
    
    total += 1
    try:
        result = candidate(num = 53142) == 54132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 53142) == 54132: {e}')
    
    total += 1
    try:
        result = candidate(num = 100100) == 110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100100) == 110000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000001) == 110000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000001) == 110000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 3333333) == 3333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3333333) == 3333333: {e}')
    
    total += 1
    try:
        result = candidate(num = 3456432) == 6453432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3456432) == 6453432: {e}')
    
    total += 1
    try:
        result = candidate(num = 543210) == 543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 543210) == 543210: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999999) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999999) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 54321) == 54321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 54321) == 54321: {e}')
    
    total += 1
    try:
        result = candidate(num = 11234321) == 41231321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11234321) == 41231321: {e}')
    
    total += 1
    try:
        result = candidate(num = 333322221111) == 333322221111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333322221111) == 333322221111: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999991) == 999999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999991) == 999999991: {e}')
    
    total += 1
    try:
        result = candidate(num = 333321) == 333321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333321) == 333321: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233445566778899) == 912233445566778891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233445566778899) == 912233445566778891: {e}')
    
    total += 1
    try:
        result = candidate(num = 199999999) == 999999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199999999) == 999999991: {e}')
    
    total += 1
    try:
        result = candidate(num = 111122223333) == 311122223331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111122223333) == 311122223331: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321000) == 987654321000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321000) == 987654321000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9834765) == 9874365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9834765) == 9874365: {e}')
    
    total += 1
    try:
        result = candidate(num = 6789876) == 9786876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 6789876) == 9786876: {e}')
    
    total += 1
    try:
        result = candidate(num = 599432187) == 995432187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 599432187) == 995432187: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == 888888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == 888888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234321) == 4231321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234321) == 4231321: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111) == 1111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111) == 1111111111: {e}')
    
    total += 1
    try:
        result = candidate(num = 63879456) == 93876456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 63879456) == 93876456: {e}')
    
    total += 1
    try:
        result = candidate(num = 1928374655) == 9128374655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1928374655) == 9128374655: {e}')
    
    total += 1
    try:
        result = candidate(num = 2333333333) == 3333333332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2333333333) == 3333333332: {e}')
    
    total += 1
    try:
        result = candidate(num = 123321) == 323121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123321) == 323121: {e}')
    
    total += 1
    try:
        result = candidate(num = 387654321) == 837654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 387654321) == 837654321: {e}')
    
    total += 1
    try:
        result = candidate(num = 227362) == 722362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 227362) == 722362: {e}')
    
    total += 1
    try:
        result = candidate(num = 983210) == 983210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 983210) == 983210: {e}')
    
    total += 1
    try:
        result = candidate(num = 67899876) == 97896876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 67899876) == 97896876: {e}')
    
    total += 1
    try:
        result = candidate(num = 2376) == 7326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2376) == 7326: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890) == 9234567810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890) == 9234567810: {e}')
    
    total += 1
    try:
        result = candidate(num = 2345321) == 5342321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2345321) == 5342321: {e}')
    
    total += 1
    try:
        result = candidate(num = 892736) == 982736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 892736) == 982736: {e}')
    
    total += 1
    try:
        result = candidate(num = 983215) == 985213
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 983215) == 985213: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567899) == 9234567891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567899) == 9234567891: {e}')
    
    total += 1
    try:
        result = candidate(num = 3339333) == 9333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3339333) == 9333333: {e}')
    
    total += 1
    try:
        result = candidate(num = 88988) == 98888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88988) == 98888: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234554321) == 5234514321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234554321) == 5234514321: {e}')
    
    total += 1
    try:
        result = candidate(num = 371698542) == 971638542
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 371698542) == 971638542: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432100) == 98765432100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432100) == 98765432100: {e}')
    
    total += 1
    try:
        result = candidate(num = 19932) == 99132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 19932) == 99132: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000001) == 1100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000001) == 1100000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9832109876) == 9932108876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9832109876) == 9932108876: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654320) == 987654320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654320) == 987654320: {e}')
    
    total += 1
    try:
        result = candidate(num = 227349) == 927342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 227349) == 927342: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 9) == 9
    assert candidate(num = 987654321) == 987654321
    assert candidate(num = 123456789) == 923456781
    assert candidate(num = 12) == 21
    assert candidate(num = 21) == 21
    assert candidate(num = 0) == 0
    assert candidate(num = 98368) == 98863
    assert candidate(num = 1099511628) == 9091511628
    assert candidate(num = 11111) == 11111
    assert candidate(num = 1111) == 1111
    assert candidate(num = 9973) == 9973
    assert candidate(num = 1099511627776) == 9091511627776
    assert candidate(num = 1993) == 9913
    assert candidate(num = 100) == 100
    assert candidate(num = 2736) == 7236
    assert candidate(num = 1099511625) == 9091511625
    assert candidate(num = 567894321) == 967854321
    assert candidate(num = 654321789) == 954321786
    assert candidate(num = 33221100) == 33221100
    assert candidate(num = 98765456789) == 99765456788
    assert candidate(num = 1000000000) == 1000000000
    assert candidate(num = 199983) == 999183
    assert candidate(num = 5639953) == 9639553
    assert candidate(num = 123321321) == 323321121
    assert candidate(num = 9876554321) == 9876554321
    assert candidate(num = 12321) == 32121
    assert candidate(num = 101010101) == 111010100
    assert candidate(num = 900000000) == 900000000
    assert candidate(num = 109090909) == 909090901
    assert candidate(num = 222222221) == 222222221
    assert candidate(num = 9834321) == 9843321
    assert candidate(num = 199999) == 999991
    assert candidate(num = 98877665544332211) == 98877665544332211
    assert candidate(num = 4201) == 4210
    assert candidate(num = 111111119) == 911111111
    assert candidate(num = 32123) == 33122
    assert candidate(num = 583214769) == 983214765
    assert candidate(num = 319872654) == 913872654
    assert candidate(num = 333333) == 333333
    assert candidate(num = 891234567) == 981234567
    assert candidate(num = 22773388) == 82773382
    assert candidate(num = 111222333) == 311222331
    assert candidate(num = 98765) == 98765
    assert candidate(num = 1119111) == 9111111
    assert candidate(num = 111111112) == 211111111
    assert candidate(num = 999999990) == 999999990
    assert candidate(num = 2736589) == 9736582
    assert candidate(num = 109890) == 909810
    assert candidate(num = 432109876) == 932104876
    assert candidate(num = 983476521) == 987436521
    assert candidate(num = 34521) == 54321
    assert candidate(num = 33333333) == 33333333
    assert candidate(num = 1098765432) == 9018765432
    assert candidate(num = 239187654) == 932187654
    assert candidate(num = 987654321987654321) == 997654321887654321
    assert candidate(num = 227368) == 827362
    assert candidate(num = 1122334455) == 5122334451
    assert candidate(num = 999999999) == 999999999
    assert candidate(num = 564999) == 964995
    assert candidate(num = 1000000) == 1000000
    assert candidate(num = 898989898) == 998989888
    assert candidate(num = 983210987) == 993210887
    assert candidate(num = 98769876) == 99768876
    assert candidate(num = 765432198) == 965432178
    assert candidate(num = 222222222) == 222222222
    assert candidate(num = 199321123) == 991321123
    assert candidate(num = 100000000) == 100000000
    assert candidate(num = 819293818) == 919283818
    assert candidate(num = 9876543210) == 9876543210
    assert candidate(num = 1999991) == 9999911
    assert candidate(num = 333333333) == 333333333
    assert candidate(num = 323232323) == 333232322
    assert candidate(num = 53142) == 54132
    assert candidate(num = 100100) == 110000
    assert candidate(num = 1000) == 1000
    assert candidate(num = 100000001) == 110000000
    assert candidate(num = 3333333) == 3333333
    assert candidate(num = 3456432) == 6453432
    assert candidate(num = 543210) == 543210
    assert candidate(num = 99999999) == 99999999
    assert candidate(num = 54321) == 54321
    assert candidate(num = 11234321) == 41231321
    assert candidate(num = 333322221111) == 333322221111
    assert candidate(num = 999999991) == 999999991
    assert candidate(num = 333321) == 333321
    assert candidate(num = 112233445566778899) == 912233445566778891
    assert candidate(num = 199999999) == 999999991
    assert candidate(num = 111122223333) == 311122223331
    assert candidate(num = 987654321000) == 987654321000
    assert candidate(num = 9834765) == 9874365
    assert candidate(num = 6789876) == 9786876
    assert candidate(num = 599432187) == 995432187
    assert candidate(num = 888888888) == 888888888
    assert candidate(num = 1234321) == 4231321
    assert candidate(num = 1111111111) == 1111111111
    assert candidate(num = 63879456) == 93876456
    assert candidate(num = 1928374655) == 9128374655
    assert candidate(num = 2333333333) == 3333333332
    assert candidate(num = 123321) == 323121
    assert candidate(num = 387654321) == 837654321
    assert candidate(num = 227362) == 722362
    assert candidate(num = 983210) == 983210
    assert candidate(num = 67899876) == 97896876
    assert candidate(num = 2376) == 7326
    assert candidate(num = 1234567890) == 9234567810
    assert candidate(num = 2345321) == 5342321
    assert candidate(num = 892736) == 982736
    assert candidate(num = 983215) == 985213
    assert candidate(num = 1234567899) == 9234567891
    assert candidate(num = 3339333) == 9333333
    assert candidate(num = 88988) == 98888
    assert candidate(num = 1234554321) == 5234514321
    assert candidate(num = 371698542) == 971638542
    assert candidate(num = 98765432100) == 98765432100
    assert candidate(num = 19932) == 99132
    assert candidate(num = 1000001) == 1100000
    assert candidate(num = 9832109876) == 9932108876
    assert candidate(num = 987654320) == 987654320
    assert candidate(num = 227349) == 927342


