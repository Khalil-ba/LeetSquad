def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 2,target = 123456) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,target = 123456) == 44: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 81) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 81) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 1001) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 1001) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,target = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,target = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,target = 100) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,target = 100) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 501) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 501) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 63) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 63) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 10000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 10000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,target = 127) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,target = 127) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 19) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 19) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,target = 1250) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,target = 1250) == 24: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 49) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 49) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,target = 2500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,target = 2500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,target = 100000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,target = 100000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 300) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 300) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 41,target = 753195728) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 41,target = 753195728) == 246: {e}')
    
    total += 1
    try:
        result = candidate(x = 37,target = 1874161) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 37,target = 1874161) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 1111111111) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 1111111111) == 88: {e}')
    
    total += 1
    try:
        result = candidate(x = 13,target = 31254) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13,target = 31254) == 17: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 1234567) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 1234567) == 66: {e}')
    
    total += 1
    try:
        result = candidate(x = 6,target = 999999) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,target = 999999) == 73: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 1000000) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 1000000) == 35: {e}')
    
    total += 1
    try:
        result = candidate(x = 6,target = 7776) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,target = 7776) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 41,target = 2825761) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 41,target = 2825761) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 343) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 343) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 214358881) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 214358881) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 13,target = 169) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13,target = 169) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 512) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 512) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 1023) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 1023) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 361) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 361) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 123456789012) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 123456789012) == 207: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 1000000001) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 1000000001) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 97,target = 22138067) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 97,target = 22138067) == 231: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 6561) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 6561) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 23,target = 123456) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 23,target = 123456) == 60: {e}')
    
    total += 1
    try:
        result = candidate(x = 49,target = 1174711139839679) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 49,target = 1174711139839679) == 325: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,target = 987654321098) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,target = 987654321098) == 265: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 625) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 625) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 10000000) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 10000000) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 243) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 243) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 67,target = 3521614606207) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 67,target = 3521614606207) == 405: {e}')
    
    total += 1
    try:
        result = candidate(x = 6,target = 216000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,target = 216000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,target = 87654321) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,target = 87654321) == 95: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 200000) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 200000) == 28: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 10000000) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 10000000) == 38: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 3430) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 3430) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 2048) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 2048) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 1771561) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 1771561) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 65536) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 65536) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 65535) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 65535) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 97,target = 88629381196525010959293) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 97,target = 88629381196525010959293) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(x = 59,target = 511116753300699300624) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 59,target = 511116753300699300624) == 340: {e}')
    
    total += 1
    try:
        result = candidate(x = 99,target = 11032558) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99,target = 11032558) == 144: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 121121) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 121121) == 25: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 123456) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 123456) == 45: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 99999) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 99999) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,target = 1000000) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,target = 1000000) == 61: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,target = 299999) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,target = 299999) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 32768) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 32768) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 83,target = 44349085) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 83,target = 44349085) == 172: {e}')
    
    total += 1
    try:
        result = candidate(x = 12,target = 1728) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 12,target = 1728) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,target = 999999) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,target = 999999) == 40: {e}')
    
    total += 1
    try:
        result = candidate(x = 31,target = 887503681) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 31,target = 887503681) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,target = 1048575) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,target = 1048575) == 21: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 100000000) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 100000000) == 86: {e}')
    
    total += 1
    try:
        result = candidate(x = 80,target = 9876543210987654) == 341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 80,target = 9876543210987654) == 341: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 5000000) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 5000000) == 60: {e}')
    
    total += 1
    try:
        result = candidate(x = 17,target = 1444) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 17,target = 1444) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 17,target = 2458624) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 17,target = 2458624) == 72: {e}')
    
    total += 1
    try:
        result = candidate(x = 17,target = 24137569) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 17,target = 24137569) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 146410) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 146410) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 59,target = 420746139) == 269
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 59,target = 420746139) == 269: {e}')
    
    total += 1
    try:
        result = candidate(x = 29,target = 87654321) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 29,target = 87654321) == 78: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 98765) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 98765) == 34: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 123456) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 123456) == 31: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 1000) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 1000) == 15: {e}')
    
    total += 1
    try:
        result = candidate(x = 37,target = 864197532) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 37,target = 864197532) == 157: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,target = 1000000000) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,target = 1000000000) == 104: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 987654321) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 987654321) == 153: {e}')
    
    total += 1
    try:
        result = candidate(x = 67,target = 208653121) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 67,target = 208653121) == 188: {e}')
    
    total += 1
    try:
        result = candidate(x = 73,target = 66560103) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 73,target = 66560103) == 142: {e}')
    
    total += 1
    try:
        result = candidate(x = 12,target = 9876543210) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 12,target = 9876543210) == 121: {e}')
    
    total += 1
    try:
        result = candidate(x = 31,target = 1999999999) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 31,target = 1999999999) == 139: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 81000) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 81000) == 27: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 999) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 999) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 53,target = 418195493) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 53,target = 418195493) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 12345) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 12345) == 16: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 97654321) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 97654321) == 65: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 1024) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 1024) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 5000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 5000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 8100) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 8100) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 4913) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 4913) == 15: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 9765625) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 9765625) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 387420489) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 387420489) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 987654) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 987654) == 65: {e}')
    
    total += 1
    try:
        result = candidate(x = 6,target = 7777) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,target = 7777) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 47,target = 642839175) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 47,target = 642839175) == 146: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,target = 12345678901234) == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,target = 12345678901234) == 251: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 123) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 123) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 60,target = 98765432109876) == 523
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 60,target = 98765432109876) == 523: {e}')
    
    total += 1
    try:
        result = candidate(x = 61,target = 309699630) == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 61,target = 309699630) == 232: {e}')
    
    total += 1
    try:
        result = candidate(x = 79,target = 55454594) == 233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 79,target = 55454594) == 233: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 99999) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 99999) == 35: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,target = 200000) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,target = 200000) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 56789) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 56789) == 31: {e}')
    
    total += 1
    try:
        result = candidate(x = 23,target = 2222222222) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 23,target = 2222222222) == 121: {e}')
    
    total += 1
    try:
        result = candidate(x = 6,target = 129600) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,target = 129600) == 30: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 87654321) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 87654321) == 59: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 100000) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 100000) == 52: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,target = 123456789) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,target = 123456789) == 99: {e}')
    
    total += 1
    try:
        result = candidate(x = 13,target = 16913) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13,target = 16913) == 27: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 4096) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 4096) == 25: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 9876543210) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 9876543210) == 138: {e}')
    
    total += 1
    try:
        result = candidate(x = 71,target = 1804229351) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 71,target = 1804229351) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 17,target = 256256256) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 17,target = 256256256) == 140: {e}')
    
    total += 1
    try:
        result = candidate(x = 23,target = 279841) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 23,target = 279841) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 88888888) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 88888888) == 81: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 98765) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 98765) == 41: {e}')
    
    total += 1
    try:
        result = candidate(x = 70,target = 1234567890123456) == 435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 70,target = 1234567890123456) == 435: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 59049) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 59049) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 13,target = 16901) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13,target = 16901) == 28: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,target = 9999999) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,target = 9999999) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 100000) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 100000) == 22: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 200) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 200) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 2476099) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 2476099) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,target = 499) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,target = 499) == 13: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 40) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 40) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 6,target = 46655) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,target = 46655) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,target = 10000000) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,target = 10000000) == 65: {e}')
    
    total += 1
    try:
        result = candidate(x = 9,target = 88888) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,target = 88888) == 48: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 12345) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 12345) == 29: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 923521) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 923521) == 65: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 123456789) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 123456789) == 101: {e}')
    
    total += 1
    try:
        result = candidate(x = 19,target = 999999999) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 19,target = 999999999) == 88: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,target = 987654) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,target = 987654) == 73: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,target = 123456789) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,target = 123456789) == 185: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,target = 987654) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,target = 987654) == 60: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 625000) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 625000) == 37: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,target = 16777216) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,target = 16777216) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 13,target = 13131313) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13,target = 13131313) == 69: {e}')
    
    total += 1
    try:
        result = candidate(x = 31,target = 28829) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 31,target = 28829) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,target = 123456) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,target = 123456) == 51: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,target = 275) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,target = 275) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 23,target = 345345345) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 23,target = 345345345) == 105: {e}')
    
    total += 1
    try:
        result = candidate(x = 13,target = 1690) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13,target = 1690) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 89,target = 33243576) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 89,target = 33243576) == 225: {e}')
    
    total += 1
    try:
        result = candidate(x = 17,target = 1234567890) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 17,target = 1234567890) == 109: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 134217728) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 134217728) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 29,target = 40353607) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 29,target = 40353607) == 64: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,target = 15625000) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,target = 15625000) == 49: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,target = 1000000) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,target = 1000000) == 38: {e}')
    
    total += 1
    try:
        result = candidate(x = 8,target = 1048576) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,target = 1048576) == 23: {e}')
    
    total += 1
    try:
        result = candidate(x = 53,target = 531792648) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 53,target = 531792648) == 196: {e}')
    
    total += 1
    try:
        result = candidate(x = 71,target = 107606612) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 71,target = 107606612) == 148: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 2,target = 123456) == 44
    assert candidate(x = 2,target = 3) == 2
    assert candidate(x = 3,target = 81) == 3
    assert candidate(x = 10,target = 1001) == 4
    assert candidate(x = 2,target = 10) == 3
    assert candidate(x = 2,target = 100) == 12
    assert candidate(x = 4,target = 30) == 7
    assert candidate(x = 5,target = 1) == 1
    assert candidate(x = 5,target = 501) == 8
    assert candidate(x = 4,target = 63) == 4
    assert candidate(x = 10,target = 10000) == 3
    assert candidate(x = 2,target = 127) == 8
    assert candidate(x = 3,target = 19) == 5
    assert candidate(x = 50,target = 1250) == 24
    assert candidate(x = 7,target = 49) == 1
    assert candidate(x = 50,target = 2500) == 1
    assert candidate(x = 100,target = 100000000) == 3
    assert candidate(x = 10,target = 1000) == 2
    assert candidate(x = 10,target = 1000000) == 5
    assert candidate(x = 3,target = 1) == 1
    assert candidate(x = 7,target = 300) == 7
    assert candidate(x = 41,target = 753195728) == 246
    assert candidate(x = 37,target = 1874161) == 3
    assert candidate(x = 11,target = 1111111111) == 88
    assert candidate(x = 13,target = 31254) == 17
    assert candidate(x = 7,target = 100) == 7
    assert candidate(x = 3,target = 1234567) == 66
    assert candidate(x = 6,target = 999999) == 73
    assert candidate(x = 4,target = 1000000) == 35
    assert candidate(x = 6,target = 7776) == 4
    assert candidate(x = 41,target = 2825761) == 3
    assert candidate(x = 7,target = 343) == 2
    assert candidate(x = 11,target = 214358881) == 7
    assert candidate(x = 13,target = 169) == 1
    assert candidate(x = 8,target = 512) == 2
    assert candidate(x = 4,target = 1023) == 6
    assert candidate(x = 19,target = 361) == 1
    assert candidate(x = 25,target = 123456789012) == 207
    assert candidate(x = 10,target = 1000000001) == 10
    assert candidate(x = 97,target = 22138067) == 231
    assert candidate(x = 9,target = 6561) == 3
    assert candidate(x = 23,target = 123456) == 60
    assert candidate(x = 49,target = 1174711139839679) == 325
    assert candidate(x = 30,target = 987654321098) == 265
    assert candidate(x = 25,target = 625) == 1
    assert candidate(x = 7,target = 10000000) == 50
    assert candidate(x = 5,target = 243) == 10
    assert candidate(x = 67,target = 3521614606207) == 405
    assert candidate(x = 6,target = 216000) == 32
    assert candidate(x = 20,target = 87654321) == 95
    assert candidate(x = 8,target = 200000) == 28
    assert candidate(x = 25,target = 10000000) == 38
    assert candidate(x = 7,target = 3430) == 12
    assert candidate(x = 8,target = 2048) == 11
    assert candidate(x = 11,target = 1771561) == 5
    assert candidate(x = 4,target = 65536) == 7
    assert candidate(x = 4,target = 65535) == 9
    assert candidate(x = 97,target = 88629381196525010959293) == 1536
    assert candidate(x = 59,target = 511116753300699300624) == 340
    assert candidate(x = 99,target = 11032558) == 144
    assert candidate(x = 11,target = 121121) == 25
    assert candidate(x = 5,target = 123456) == 45
    assert candidate(x = 10,target = 99999) == 6
    assert candidate(x = 15,target = 1000000) == 61
    assert candidate(x = 30,target = 299999) == 50
    assert candidate(x = 8,target = 32768) == 4
    assert candidate(x = 83,target = 44349085) == 172
    assert candidate(x = 12,target = 1728) == 2
    assert candidate(x = 20,target = 999999) == 40
    assert candidate(x = 31,target = 887503681) == 5
    assert candidate(x = 2,target = 1048575) == 21
    assert candidate(x = 4,target = 100000000) == 86
    assert candidate(x = 80,target = 9876543210987654) == 341
    assert candidate(x = 8,target = 5000000) == 60
    assert candidate(x = 17,target = 1444) == 11
    assert candidate(x = 17,target = 2458624) == 72
    assert candidate(x = 17,target = 24137569) == 5
    assert candidate(x = 11,target = 146410) == 8
    assert candidate(x = 59,target = 420746139) == 269
    assert candidate(x = 29,target = 87654321) == 78
    assert candidate(x = 9,target = 98765) == 34
    assert candidate(x = 7,target = 123456) == 31
    assert candidate(x = 3,target = 1000) == 15
    assert candidate(x = 37,target = 864197532) == 157
    assert candidate(x = 15,target = 1000000000) == 104
    assert candidate(x = 11,target = 987654321) == 153
    assert candidate(x = 67,target = 208653121) == 188
    assert candidate(x = 73,target = 66560103) == 142
    assert candidate(x = 12,target = 9876543210) == 121
    assert candidate(x = 31,target = 1999999999) == 139
    assert candidate(x = 9,target = 81000) == 27
    assert candidate(x = 5,target = 999) == 14
    assert candidate(x = 53,target = 418195493) == 4
    assert candidate(x = 5,target = 12345) == 16
    assert candidate(x = 25,target = 97654321) == 65
    assert candidate(x = 4,target = 1024) == 4
    assert candidate(x = 8,target = 5000) == 14
    assert candidate(x = 9,target = 8100) == 11
    assert candidate(x = 7,target = 4913) == 15
    assert candidate(x = 25,target = 9765625) == 4
    assert candidate(x = 9,target = 387420489) == 8
    assert candidate(x = 19,target = 987654) == 65
    assert candidate(x = 6,target = 7777) == 6
    assert candidate(x = 47,target = 642839175) == 146
    assert candidate(x = 40,target = 12345678901234) == 251
    assert candidate(x = 5,target = 123) == 6
    assert candidate(x = 60,target = 98765432109876) == 523
    assert candidate(x = 61,target = 309699630) == 232
    assert candidate(x = 79,target = 55454594) == 233
    assert candidate(x = 19,target = 99999) == 35
    assert candidate(x = 20,target = 200000) == 18
    assert candidate(x = 8,target = 56789) == 31
    assert candidate(x = 23,target = 2222222222) == 121
    assert candidate(x = 6,target = 129600) == 30
    assert candidate(x = 9,target = 87654321) == 59
    assert candidate(x = 3,target = 100000) == 52
    assert candidate(x = 15,target = 123456789) == 99
    assert candidate(x = 13,target = 16913) == 27
    assert candidate(x = 3,target = 4096) == 25
    assert candidate(x = 19,target = 9876543210) == 138
    assert candidate(x = 71,target = 1804229351) == 4
    assert candidate(x = 17,target = 256256256) == 140
    assert candidate(x = 23,target = 279841) == 3
    assert candidate(x = 9,target = 88888888) == 81
    assert candidate(x = 3,target = 98765) == 41
    assert candidate(x = 70,target = 1234567890123456) == 435
    assert candidate(x = 9,target = 59049) == 4
    assert candidate(x = 13,target = 16901) == 28
    assert candidate(x = 10,target = 9999999) == 8
    assert candidate(x = 5,target = 100000) == 22
    assert candidate(x = 7,target = 200) == 14
    assert candidate(x = 19,target = 2476099) == 4
    assert candidate(x = 7,target = 499) == 13
    assert candidate(x = 3,target = 40) == 7
    assert candidate(x = 6,target = 46655) == 7
    assert candidate(x = 15,target = 10000000) == 65
    assert candidate(x = 9,target = 88888) == 48
    assert candidate(x = 3,target = 12345) == 29
    assert candidate(x = 19,target = 923521) == 65
    assert candidate(x = 5,target = 123456789) == 101
    assert candidate(x = 19,target = 999999999) == 88
    assert candidate(x = 3,target = 987654) == 73
    assert candidate(x = 50,target = 123456789) == 185
    assert candidate(x = 5,target = 987654) == 60
    assert candidate(x = 25,target = 625000) == 37
    assert candidate(x = 4,target = 16777216) == 11
    assert candidate(x = 13,target = 13131313) == 69
    assert candidate(x = 31,target = 28829) == 6
    assert candidate(x = 20,target = 123456) == 51
    assert candidate(x = 11,target = 275) == 6
    assert candidate(x = 23,target = 345345345) == 105
    assert candidate(x = 13,target = 1690) == 8
    assert candidate(x = 89,target = 33243576) == 225
    assert candidate(x = 17,target = 1234567890) == 109
    assert candidate(x = 8,target = 134217728) == 8
    assert candidate(x = 29,target = 40353607) == 64
    assert candidate(x = 25,target = 15625000) == 49
    assert candidate(x = 20,target = 1000000) == 38
    assert candidate(x = 8,target = 1048576) == 23
    assert candidate(x = 53,target = 531792648) == 196
    assert candidate(x = 71,target = 107606612) == 148


