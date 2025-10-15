def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DII") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DII") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDII") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDII") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDDDDDD") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDDDDDD") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDI") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDI") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDID") == 398885199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDID") == 398885199: {e}')
    
    total += 1
    try:
        result = candidate(s = "IID") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IID") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDID") == 185644928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDID") == 185644928: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDID") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDID") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDI") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDI") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DID") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DID") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDD") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDD") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDID") == 2702765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDID") == 2702765: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDI") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDI") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDII") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDII") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "D") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "D") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ID") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ID") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDID") == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDID") == 155: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDID") == 903757305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDID") == 903757305: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDID") == 955348527
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDID") == 955348527: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIID") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIID") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDI") == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDI") == 272: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDID") == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDID") == 272: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDD") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDD") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDII") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDII") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDID") == 791
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDID") == 791: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDID") == 50521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDID") == 50521: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDI") == 50521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDI") == 50521: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDID") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDID") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDID") == 353792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDID") == 353792: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDDD") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDDD") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "DD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DI") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DI") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDI") == 7936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDI") == 7936: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDD") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDD") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "II") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "II") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDID") == 391512012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDID") == 391512012: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDD") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDD") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "III") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "III") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDID") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDID") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDI") == 2702765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDI") == 2702765: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDID") == 199360981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDID") == 199360981: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDI") == 199360981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDI") == 199360981: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIII") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIII") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDID") == 884909216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDID") == 884909216: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDID") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDID") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDID") == 7936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDID") == 7936: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDD") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDD") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDI") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDI") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 372054302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 372054302: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIDDDID") == 23409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIDDDID") == 23409: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDIIIIIDIDIDID") == 673511962
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDIIIIIDIDIDID") == 673511962: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDID") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDID") == 77: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDD") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDD") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDIDIDIDDD") == 1222144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDIDIDIDDD") == 1222144: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIIDIIDIID") == 3052323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIIDIIDIID") == 3052323: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDIIDIIDII") == 1049476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDIIDIIDII") == 1049476: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 393265742
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 393265742: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDIIIDDDDDIIIDDDD") == 184972317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDIIIDDDDDIIIDDDD") == 184972317: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIII") == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIII") == 495: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIDDDDDDIIIIIIDDDDDDIIIIIIDDDDDDIIIIIID") == 462903546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIDDDDDDIIIIIIDDDDDDIIIIIIDDDDDDIIIIIID") == 462903546: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIDIIIDIIIDIIIDIIID") == 186469344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIDIIIDIIIDIIIDIIID") == 186469344: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDID") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDID") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDIIIIIIIIIIDDDDDDDDDIIIIIIII") == 441488323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDIIIIIIIIIIDDDDDDDDDIIIIIIII") == 441488323: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDD") == 89320108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDD") == 89320108: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIIIIIIIIII") == 184756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIIIIIIIIII") == 184756: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDID") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDID") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIDDDDDD") == 1715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIDDDDDD") == 1715: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDIDID") == 814891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDIDID") == 814891: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 68280442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 68280442: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDIIIDDDDDIIIDDDDDIIIDDDDDD") == 320107597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDIIIDDDDDIIIDDDDDIIIDDDDDD") == 320107597: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDID") == 22368256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDID") == 22368256: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 179476197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 179476197: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 211646917
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 211646917: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDDDDDDD") == 31824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDDDDDDD") == 31824: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDI") == 312030296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDI") == 312030296: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDD") == 792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDD") == 792: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDIDIDIDIDID") == 546532656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDIDIDIDIDID") == 546532656: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 916895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 916895: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDD") == 7124320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDD") == 7124320: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDDIIIIIDDDDDDDDDIIIIIDDDDDDDDDIIII") == 161680825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDDIIIIIDDDDDDDDDIIIIIDDDDDDDDDIIII") == 161680825: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDDDD") == 1681317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDDDD") == 1681317: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDD") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDD") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == 978143726
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == 978143726: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIII") == 924
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIII") == 924: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDDDDDDDD") == 48620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDDDDDDDD") == 48620: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDDDDDIIIIIIII") == 673511962
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDDDDDIIIIIIII") == 673511962: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIIIIIDDDDD") == 19483036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIIIIIDDDDD") == 19483036: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDIIIDDDIIIDDD") == 676402828
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDIIIDDDIIIDDD") == 676402828: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDD") == 802666207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDD") == 802666207: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIIIIIDIIIIIDIIIIID") == 397477620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIIIIIDIIIIIDIIIIID") == 397477620: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDI") == 903757305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDI") == 903757305: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDIDIDID") == 790362656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDIDIDID") == 790362656: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIIIIIIII") == 6435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIIIIIIII") == 6435: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIII") == 327757655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIII") == 327757655: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 559265847
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 559265847: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDD") == 251400487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDD") == 251400487: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDIDIDIDIDDD") == 103980032
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDIDIDIDIDDD") == 103980032: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 486231764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 486231764: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDD") == 586971725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDD") == 586971725: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIIDDIIDD") == 2020656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIIDDIIDD") == 2020656: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDDDDD") == 6435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDDDDD") == 6435: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIDDDIDDD") == 349504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIDDDIDDD") == 349504: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDIIIIIIIIIIIIIIIIII") == 604465316
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDIIIIIIIIIIIIIIIIII") == 604465316: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 514024747
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 514024747: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIII") == 476337793
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIII") == 476337793: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIDID") == 6721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIDID") == 6721: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDDDIDDDDDD") == 23947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDDDIDDDDDD") == 23947: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDD") == 9946124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDD") == 9946124: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIIDDD") == 11210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIIDDD") == 11210: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDIIIIIIIIIIIIIDDDDDDDDDDDIIIIIIIIIIIIIIIDDDDDDDDDDDIIIIII") == 844233887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDIIIIIIIIIIIIIDDDDDDDDDDDIIIIIIIIIIIIIIIDDDDDDDDDDDIIIIII") == 844233887: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIIDIDID") == 14253227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIIDIDID") == 14253227: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 469639504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 469639504: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIII") == 754901336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIII") == 754901336: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIIIIIDIDIDIDID") == 541113001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIIIIIDIDIDIDID") == 541113001: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID") == 1805
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID") == 1805: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIIIIIIIIIIIIIIIIIIIDIIIIIIIIIIIIIIIIIIIIID") == 444261561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIIIIIIIIIIIIIIIIIIIDIIIIIIIIIIIIIIIIIIIIID") == 444261561: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDIII") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDIII") == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIDIDDDI") == 1231021
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIDIDDDI") == 1231021: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDD") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDD") == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDDDII") == 38160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDDDII") == 38160: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDIDIDIDIDI") == 86657396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDIDIDIDIDI") == 86657396: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDDD") == 329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDDD") == 329: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIID") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIID") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDD") == 115670161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDD") == 115670161: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIDDDDDDDD") == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIDDDDDDDD") == 1650: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIIIIIIII") == 43758
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIIIIIIII") == 43758: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDDD") == 787128653
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDDD") == 787128653: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIII") == 116643020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIII") == 116643020: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 803806388
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 803806388: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDIIIIIDDD") == 16458940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDIIIIIDDD") == 16458940: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIIIIIIIIIDDDDDDIIIIIIIIIDDD") == 637084962
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIIIIIIIIIDDDDDDIIIIIIIIIDDD") == 637084962: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 89434740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 89434740: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDID") == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDID") == 430: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDIIIIIIIIII") == 43758
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDIIIIIIIIII") == 43758: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 752033767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 752033767: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDID") == 907695790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDID") == 907695790: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIDDDIDDDIDDDIDDD") == 447283659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIDDDIDDDIDDDIDDD") == 447283659: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIDID") == 9470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIDID") == 9470: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDD") == 537567622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDD") == 537567622: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 569787174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 569787174: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDDD") == 2983553
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDDD") == 2983553: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIID") == 671217372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIID") == 671217372: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDID") == 201939
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDID") == 201939: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 827971518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 827971518: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIID") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIID") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDIDDD") == 253949942
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDIDDD") == 253949942: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDIIII") == 3795
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDIIII") == 3795: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDID") == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDID") == 252: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIIID") == 1838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIIID") == 1838: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDID") == 616527580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDID") == 616527580: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDDD") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDDD") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 135751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 135751: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 634392057
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 634392057: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIID") == 282462203
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIID") == 282462203: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDD") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDD") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 595888523
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 595888523: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 399447831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 399447831: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDIDIDIDIDIDID") == 65867250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDIDIDIDIDIDID") == 65867250: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 210834483
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 210834483: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIDIDIDIIIIIIII") == 509306786
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIDIDIDIIIIIIII") == 509306786: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 233702287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 233702287: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDID") == 12767689
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDID") == 12767689: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIDDDIII") == 335765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIDDDIII") == 335765: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDDDDDIDDDDDIDDDDD") == 865768945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDDDDDIDDDDDIDDDDD") == 865768945: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIIDID") == 226291
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIIDID") == 226291: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIII") == 340633227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIII") == 340633227: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 277061441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 277061441: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 105648435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 105648435: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIIIIID") == 43043
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIIIIID") == 43043: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDD") == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDD") == 320: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDIDIDIDIDIDID") == 45651113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDIDIDIDIDIDID") == 45651113: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDDDDDDIIIII") == 945382435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDDDDDDIIIII") == 945382435: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 373242177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 373242177: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDIIIIIDDDDD") == 190033974
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDIIIIIDDDDD") == 190033974: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIIIIIIDDDDDIIIIIIIDDDDDIIIIIIIDDDDDII") == 8516027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIIIIIIDDDDDIIIIIIIDDDDDIIIIIIIDDDDDII") == 8516027: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDDDDDIIIIIII") == 103159144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDDDDDIIIIIII") == 103159144: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIDDDIDDDIDDDIDDDIDDDIDDDIDDDIDDD") == 456017217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIDDDIDDDIDDDIDDDIDDDIDDDIDDDIDDD") == 456017217: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDDDDDDDDDD") == 167960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDDDDDDDDDD") == 167960: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIII") == 553551576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIII") == 553551576: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDDDDD") == 256448604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDDDDD") == 256448604: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDDDDDIIIIIIIIIIIDDDDDDDDDDDDIIIIIIIIIIIDDDDDDDDDDDDIIII") == 249031970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDDDDDIIIIIIIIIIIDDDDDDDDDDDDIIIIIIIIIIIDDDDDDDDDDDDIIII") == 249031970: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDD") == 295177009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDD") == 295177009: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDID") == 896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDID") == 896: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDIIIIIII") == 286077
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDIIIIIII") == 286077: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIDDDDDIIID") == 882155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIDDDDDIIID") == 882155: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDIDDDDDDDDIDDDDDDDDIDDDDDDDDIDDDD") == 383124231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDIDDDDDDDDIDDDDDDDDIDDDDDDDDIDDDD") == 383124231: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDD") == 816732003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDD") == 816732003: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDIDDDDDIII") == 28546231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDIDDDDDIII") == 28546231: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDDDDD") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDDDDD") == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 717149364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 717149364: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDID") == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDID") == 768: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 840858142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 840858142: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDIIIDDDDDIIIDDDDDIIIDDDDDDID") == 643652602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDIIIDDDDDIIIDDDDDIIIDDDDDDID") == 643652602: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDD") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDD") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIID") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIID") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDIIIIIIIIIIIIII") == 319770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDIIIIIIIIIIIIII") == 319770: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDD") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDD") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDIDIDIDI") == 12767689
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDIDIDIDI") == 12767689: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIDIDDDD") == 973622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIDIDDDD") == 973622: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDIIIIIIIIIDDDDDDDIIIIIIIIIIIDDDDD") == 439575343
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDIIIIIIIIIDDDDDDDIIIIIIIIIIIDDDDD") == 439575343: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIII") == 396282384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIII") == 396282384: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 434494262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 434494262: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIDDDIIIIIDDD") == 322218808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIDDDIIIIIDDD") == 322218808: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIDDDDDDDDD") == 1623769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIDDDDDDDDD") == 1623769: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDID") == 437003601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDID") == 437003601: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 200684441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 200684441: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "DDDDDDDDDDDD") == 1
    assert candidate(s = "DII") == 3
    assert candidate(s = "IIDII") == 19
    assert candidate(s = "DIDDDDDD") == 35
    assert candidate(s = "IIIIIIIIIIII") == 1
    assert candidate(s = "DDI") == 3
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDID") == 398885199
    assert candidate(s = "IID") == 3
    assert candidate(s = "DIDIDIDIDIDIDIDIDID") == 185644928
    assert candidate(s = "DDDDDDDDDDDDD") == 1
    assert candidate(s = "IIDID") == 35
    assert candidate(s = "DIDI") == 16
    assert candidate(s = "IIIIIIIIIII") == 1
    assert candidate(s = "IIIIIIIIII") == 1
    assert candidate(s = "DID") == 5
    assert candidate(s = "IDDD") == 4
    assert candidate(s = "DIDIDIDIDID") == 2702765
    assert candidate(s = "DDDDDDDD") == 1
    assert candidate(s = "DDIDI") == 35
    assert candidate(s = "DDDDII") == 15
    assert candidate(s = "DDDDDDDDDDD") == 1
    assert candidate(s = "IIIIII") == 1
    assert candidate(s = "D") == 1
    assert candidate(s = "IIII") == 1
    assert candidate(s = "ID") == 2
    assert candidate(s = "DDIDID") == 155
    assert candidate(s = "DDDDDDD") == 1
    assert candidate(s = "IDIDIDIDIDIDID") == 903757305
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDID") == 955348527
    assert candidate(s = "DDDDDDDDD") == 1
    assert candidate(s = "IIIIID") == 6
    assert candidate(s = "DIDIDI") == 272
    assert candidate(s = "IDIDID") == 272
    assert candidate(s = "IIDIDD") == 90
    assert candidate(s = "IDII") == 9
    assert candidate(s = "IIDIDID") == 791
    assert candidate(s = "DIDIDIDID") == 50521
    assert candidate(s = "IDIDIDIDI") == 50521
    assert candidate(s = "DDID") == 9
    assert candidate(s = "IDIDIDIDID") == 353792
    assert candidate(s = "DDIDDD") == 34
    assert candidate(s = "DD") == 1
    assert candidate(s = "IIIIIIIII") == 1
    assert candidate(s = "DI") == 2
    assert candidate(s = "IIIIIIII") == 1
    assert candidate(s = "DIDIDIDI") == 7936
    assert candidate(s = "DDIIDD") == 71
    assert candidate(s = "II") == 1
    assert candidate(s = "DIDIDIDIDIDIDID") == 391512012
    assert candidate(s = "IDDDDD") == 6
    assert candidate(s = "III") == 1
    assert candidate(s = "IDID") == 16
    assert candidate(s = "DDDD") == 1
    assert candidate(s = "IDIDIDIDIDI") == 2702765
    assert candidate(s = "DIDIDIDIDIDID") == 199360981
    assert candidate(s = "IDIDIDIDIDIDI") == 199360981
    assert candidate(s = "DIII") == 4
    assert candidate(s = "IDIDIDIDIDIDIDIDID") == 884909216
    assert candidate(s = "DDDDID") == 20
    assert candidate(s = "IDIDIDID") == 7936
    assert candidate(s = "IIIIIII") == 1
    assert candidate(s = "IIIIIIIIIIIII") == 1
    assert candidate(s = "IDDDD") == 5
    assert candidate(s = "IDI") == 5
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 372054302
    assert candidate(s = "DDIIIDDDID") == 23409
    assert candidate(s = "DDDDDDDDIIIIIDIDIDID") == 673511962
    assert candidate(s = "DDDDDDDDDDID") == 77
    assert candidate(s = "IDDDDDDDDDDDDD") == 14
    assert candidate(s = "IIIDIDIDIDDD") == 1222144
    assert candidate(s = "IIDIIDIIDIID") == 3052323
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IIIDIIDIIDII") == 1049476
    assert candidate(s = "IIDDDDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 393265742
    assert candidate(s = "IIIDDDDDIIIDDDDDIIIDDDD") == 184972317
    assert candidate(s = "DDDDIIIIIIII") == 495
    assert candidate(s = "IIIIIIDDDDDDIIIIIIDDDDDDIIIIIIDDDDDDIIIIIID") == 462903546
    assert candidate(s = "DIIIDIIIDIIIDIIIDIIID") == 186469344
    assert candidate(s = "DDDDDDDDID") == 54
    assert candidate(s = "DDDDDDDDDIIIIIIIIIIDDDDDDDDDIIIIIIII") == 441488323
    assert candidate(s = "IDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDDDIDDDDDD") == 89320108
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "DDDDDDDDDDIIIIIIIIII") == 184756
    assert candidate(s = "DDDDDDDDDID") == 65
    assert candidate(s = "DDDDDIDDDDDD") == 1715
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDIDID") == 814891
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 68280442
    assert candidate(s = "IIDDDDDDIIIDDDDDIIIDDDDDIIIDDDDDD") == 320107597
    assert candidate(s = "IDIDIDIDIDID") == 22368256
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 179476197
    assert candidate(s = "IDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 211646917
    assert candidate(s = "IIIIIIIIIIIDDDDDDD") == 31824
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDI") == 312030296
    assert candidate(s = "IIIIIIIDDDDD") == 792
    assert candidate(s = "DDDDIDIDIDIDIDIDID") == 546532656
    assert candidate(s = "DDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 916895
    assert candidate(s = "IIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDD") == 7124320
    assert candidate(s = "IIIIIDDDDDDDDDIIIIIDDDDDDDDDIIIIIDDDDDDDDDIIII") == 161680825
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "DIDIDIDIDDDD") == 1681317
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IDDDDDDDDDDDD") == 13
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == 978143726
    assert candidate(s = "DDDDDDIIIIII") == 924
    assert candidate(s = "IIIIIIIIIDDDDDDDDD") == 48620
    assert candidate(s = "IDIDIDIDDDDDIIIIIIII") == 673511962
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "DDDDIIIIIIIIIIIDDDDD") == 19483036
    assert candidate(s = "IIIDDDIIIDDDIIIDDD") == 676402828
    assert candidate(s = "IIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDD") == 802666207
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "IIIIIDIIIIIDIIIIIDIIIIID") == 397477620
    assert candidate(s = "DIDIDIDIDIDIDI") == 903757305
    assert candidate(s = "DDIDIDIDIDIDIDID") == 790362656
    assert candidate(s = "DDDDDDDIIIIIIII") == 6435
    assert candidate(s = "DIDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIII") == 327757655
    assert candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 559265847
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDD") == 251400487
    assert candidate(s = "IIIDIDIDIDIDDD") == 103980032
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 486231764
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDD") == 586971725
    assert candidate(s = "IIDDIIDDIIDD") == 2020656
    assert candidate(s = "DDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IIIIIIIDDDDDDDD") == 6435
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "IDDDIDDDIDDD") == 349504
    assert candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDIIIIIIIIIIIIIIIIII") == 604465316
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 514024747
    assert candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIII") == 476337793
    assert candidate(s = "DDDDDDDDDDIDID") == 6721
    assert candidate(s = "DIDDDIDDDDDD") == 23947
    assert candidate(s = "IIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "IIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDDIIIIIIIDDDDDDD") == 9946124
    assert candidate(s = "IDDDIIIDDD") == 11210
    assert candidate(s = "IIIIIDDDDDIIIIIIIIIIIIIDDDDDDDDDDDIIIIIIIIIIIIIIIDDDDDDDDDDDIIIIII") == 844233887
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "DIDIDIIDIDID") == 14253227
    assert candidate(s = "DDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 469639504
    assert candidate(s = "IDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIII") == 754901336
    assert candidate(s = "IDIDIDIIIIIDIDIDIDID") == 541113001
    assert candidate(s = "DDDDDDDDDD") == 1
    assert candidate(s = "DIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID") == 1805
    assert candidate(s = "DIIIIIIIIIIIIIIIIIIIIIDIIIIIIIIIIIIIIIIIIIIID") == 444261561
    assert candidate(s = "DDDDDDDDDIII") == 220
    assert candidate(s = "IIDDDIDIDDDI") == 1231021
    assert candidate(s = "IIIIIIIIIDDD") == 220
    assert candidate(s = "DDIDIDDDII") == 38160
    assert candidate(s = "IIDIDIDIDIDIDI") == 86657396
    assert candidate(s = "DDDDDDIDDD") == 329
    assert candidate(s = "IIIIIIIIID") == 10
    assert candidate(s = "IIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDD") == 115670161
    assert candidate(s = "DIIIDDDDDDDD") == 1650
    assert candidate(s = "DDDDDDDDDDIIIIIIII") == 43758
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDDD") == 787128653
    assert candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIII") == 116643020
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 803806388
    assert candidate(s = "IIIIIIIIIIIDIIIIIDDD") == 16458940
    assert candidate(s = "DDDDDDDIIIIIIIIIDDDDDDIIIIIIIIIDDD") == 637084962
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 89434740
    assert candidate(s = "IDDDDDDDID") == 430
    assert candidate(s = "DDDDDDDDIIIIIIIIII") == 43758
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 752033767
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDID") == 907695790
    assert candidate(s = "IDDDIDDDIDDDIDDDIDDD") == 447283659
    assert candidate(s = "IDDDDDIDID") == 9470
    assert candidate(s = "IIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDD") == 537567622
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 569787174
    assert candidate(s = "DDIDIDIDIDDD") == 2983553
    assert candidate(s = "IIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIIDIIIIID") == 671217372
    assert candidate(s = "DDIDIDIDID") == 201939
    assert candidate(s = "DDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 827971518
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIID") == 22
    assert candidate(s = "DDIDIDIDIDIDDD") == 253949942
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IDDDDDDDIIII") == 3795
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDID") == 252
    assert candidate(s = "IIIIIDIIID") == 1838
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDID") == 616527580
    assert candidate(s = "IIIDDDDDDD") == 120
    assert candidate(s = "DDDDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 135751
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 634392057
    assert candidate(s = "DDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIIDDDIID") == 282462203
    assert candidate(s = "IDDDDDDDDDDD") == 12
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 595888523
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 399447831
    assert candidate(s = "DDDDIDIDIDIDIDIDIDID") == 65867250
    assert candidate(s = "IIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 210834483
    assert candidate(s = "IIIIIDIDIDIDIIIIIIII") == 509306786
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 233702287
    assert candidate(s = "DDIDIDIDIDID") == 12767689
    assert candidate(s = "IIDDDIDDDIII") == 335765
    assert candidate(s = "DDDDDDIDDDDDIDDDDDIDDDDD") == 865768945
    assert candidate(s = "DIDIDIIDID") == 226291
    assert candidate(s = "IIIIIIIIIIIIIII") == 1
    assert candidate(s = "DDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIII") == 340633227
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 277061441
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 105648435
    assert candidate(s = "DDDDDDIIIIIIIID") == 43043
    assert candidate(s = "IDIDDDDDDD") == 320
    assert candidate(s = "IIIDIDIDIDIDIDID") == 45651113
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDDDDDDIIIII") == 945382435
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "DDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 373242177
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IIIIIDDDDDIIIIIDDDDD") == 190033974
    assert candidate(s = "DDDDDIIIIIIIDDDDDIIIIIIIDDDDDIIIIIIIDDDDDII") == 8516027
    assert candidate(s = "IDIDIDDDDDIIIIIII") == 103159144
    assert candidate(s = "DDDIDDDIDDDIDDDIDDDIDDDIDDDIDDDIDDD") == 456017217
    assert candidate(s = "IIIIIIIIIDDDDDDDDDDD") == 167960
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "DDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIII") == 553551576
    assert candidate(s = "IDIDIDIDIDIDIDIDDDDD") == 256448604
    assert candidate(s = "IIIIIDDDDDDDDDDDDIIIIIIIIIIIDDDDDDDDDDDDIIIIIIIIIIIDDDDDDDDDDDDIIII") == 249031970
    assert candidate(s = "IIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDDIIIIIIIIIDDDDDDDD") == 295177009
    assert candidate(s = "IIIIIIIIIIIDID") == 896
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "IIIDDDDDIIIIIII") == 286077
    assert candidate(s = "DIIIDDDDDIIID") == 882155
    assert candidate(s = "IDDDDDDDDDDIDDDDDDDDIDDDDDDDDIDDDDDDDDIDDDD") == 383124231
    assert candidate(s = "DDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDDIDDDDD") == 816732003
    assert candidate(s = "IIDDDDDIDDDDDIII") == 28546231
    assert candidate(s = "IIIDDDDDDDDD") == 220
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 717149364
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "IDDDDDDDDDID") == 768
    assert candidate(s = "DDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDIIIIIDDDDD") == 840858142
    assert candidate(s = "IDDDDDDDIIIDDDDDIIIDDDDDIIIDDDDDDID") == 643652602
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII") == 1
    assert candidate(s = "IDDDDDDDDD") == 10
    assert candidate(s = "IIIIIIIIIIID") == 12
    assert candidate(s = "DDDDDDDDIIIIIIIIIIIIII") == 319770
    assert candidate(s = "IIDDDDDDDD") == 45
    assert candidate(s = "IIDIDIDIDIDI") == 12767689
    assert candidate(s = "IIDDDDIDIDDDD") == 973622
    assert candidate(s = "IIIIIDDDDDIIIIIIIIIDDDDDDDIIIIIIIIIIIDDDDD") == 439575343
    assert candidate(s = "IIIIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIII") == 396282384
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 434494262
    assert candidate(s = "DDDDIIIIIDDDIIIIIDDD") == 322218808
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == 1
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIIIDDDDDDDDD") == 1623769
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDID") == 437003601
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == 200684441


