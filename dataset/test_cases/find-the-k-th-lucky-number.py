def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 1073741823) == "444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1073741823) == "444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4398046511103) == "444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4398046511103) == "444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 50) == "74477"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50) == "74477": {e}')
    
    total += 1
    try:
        result = candidate(k = 127) == "4444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 127) == "4444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 6) == "77"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6) == "77": {e}')
    
    total += 1
    try:
        result = candidate(k = 63) == "444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 63) == "444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1048575) == "44444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1048575) == "44444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1099511627775) == "4444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1099511627775) == "4444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 281474976710655) == "444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 281474976710655) == "444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1) == "4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1) == "4": {e}')
    
    total += 1
    try:
        result = candidate(k = 140737488355327) == "44444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 140737488355327) == "44444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 17179869183) == "4444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 17179869183) == "4444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 8191) == "4444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8191) == "4444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 68719476735) == "444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 68719476735) == "444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 262143) == "444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 262143) == "444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 65535) == "4444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65535) == "4444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 35184372088831) == "444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 35184372088831) == "444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 16383) == "44444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16383) == "44444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 750) == "477747777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 750) == "477747777": {e}')
    
    total += 1
    try:
        result = candidate(k = 1125899906842623) == "44444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1125899906842623) == "44444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2097151) == "444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2097151) == "444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 288230376151711743) == "4444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 288230376151711743) == "4444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 100) == "744747"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100) == "744747": {e}')
    
    total += 1
    try:
        result = candidate(k = 32767) == "444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 32767) == "444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2251799813685247) == "444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2251799813685247) == "444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000) == "77477744774747744747444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000) == "77477744774747744747444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 131071) == "44444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 131071) == "44444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2) == "7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2) == "7": {e}')
    
    total += 1
    try:
        result = candidate(k = 8388607) == "44444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8388607) == "44444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 17592186044415) == "44444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 17592186044415) == "44444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4503599627370495) == "4444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4503599627370495) == "4444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 9) == "474"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9) == "474": {e}')
    
    total += 1
    try:
        result = candidate(k = 10) == "477"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10) == "477": {e}')
    
    total += 1
    try:
        result = candidate(k = 562949953421311) == "4444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 562949953421311) == "4444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 549755813887) == "444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 549755813887) == "444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 36028797018963967) == "4444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 36028797018963967) == "4444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 144115188075855871) == "444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 144115188075855871) == "444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4095) == "444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4095) == "444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 15) == "4444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15) == "4444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2199023255551) == "44444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2199023255551) == "44444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 18014398509481983) == "444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 18014398509481983) == "444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 16777215) == "444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16777215) == "444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2147483647) == "4444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2147483647) == "4444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 31) == "44444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 31) == "44444": {e}')
    
    total += 1
    try:
        result = candidate(k = 8589934591) == "444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8589934591) == "444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 250) == "7777477"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 250) == "7777477": {e}')
    
    total += 1
    try:
        result = candidate(k = 274877906943) == "44444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 274877906943) == "44444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4294967295) == "44444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4294967295) == "44444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 16) == "4447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16) == "4447": {e}')
    
    total += 1
    try:
        result = candidate(k = 137438953471) == "4444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 137438953471) == "4444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 268435455) == "4444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 268435455) == "4444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 9007199254740991) == "44444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9007199254740991) == "44444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 8796093022207) == "4444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8796093022207) == "4444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2047) == "44444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2047) == "44444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 524287) == "4444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 524287) == "4444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 5) == "74"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5) == "74": {e}')
    
    total += 1
    try:
        result = candidate(k = 134217727) == "444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 134217727) == "444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4194303) == "4444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4194303) == "4444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 20) == "4747"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20) == "4747": {e}')
    
    total += 1
    try:
        result = candidate(k = 1152921504606846975) == "444444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1152921504606846975) == "444444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 576460752303423487) == "44444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 576460752303423487) == "44444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 999) == "777747444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999) == "777747444": {e}')
    
    total += 1
    try:
        result = candidate(k = 500) == "77774747"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500) == "77774747": {e}')
    
    total += 1
    try:
        result = candidate(k = 70368744177663) == "4444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 70368744177663) == "4444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4611686018427387903) == "44444444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4611686018427387903) == "44444444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 33554431) == "4444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 33554431) == "4444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 7) == "444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7) == "444": {e}')
    
    total += 1
    try:
        result = candidate(k = 4) == "47"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4) == "47": {e}')
    
    total += 1
    try:
        result = candidate(k = 2305843009213693951) == "4444444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2305843009213693951) == "4444444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 255) == "44444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 255) == "44444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 3) == "44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3) == "44": {e}')
    
    total += 1
    try:
        result = candidate(k = 67108863) == "44444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67108863) == "44444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 8) == "447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8) == "447": {e}')
    
    total += 1
    try:
        result = candidate(k = 34359738367) == "44444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 34359738367) == "44444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 72057594037927935) == "44444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 72057594037927935) == "44444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1023) == "4444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1023) == "4444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 9223372036854775807) == "444444444444444444444444444444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9223372036854775807) == "444444444444444444444444444444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 511) == "444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 511) == "444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1000) == "777747447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000) == "777747447": {e}')
    
    total += 1
    try:
        result = candidate(k = 536870911) == "44444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 536870911) == "44444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 2048) == "44444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2048) == "44444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 99999999) == "47777747477774444744444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99999999) == "47777747477774444744444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 1024) == "4444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1024) == "4444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 67108864) == "44444444444444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67108864) == "44444444444444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 100000000) == "47777747477774444744444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000000) == "47777747477774444744444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 999999) == "7774744447447444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999) == "7774744447447444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 9999999) == "44774447447477474444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9999999) == "44774447447477474444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 50000000) == "4777774747777444474444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50000000) == "4777774747777444474444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 12345) == "7444444777474"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12345) == "7444444777474": {e}')
    
    total += 1
    try:
        result = candidate(k = 1048576) == "44444444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1048576) == "44444444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 65536) == "4444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65536) == "4444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 98304) == "7444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 98304) == "7444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 5000) == "447774447447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5000) == "447774447447": {e}')
    
    total += 1
    try:
        result = candidate(k = 123) == "777744"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123) == "777744": {e}')
    
    total += 1
    try:
        result = candidate(k = 524288) == "4444444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 524288) == "4444444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999) == "77477744774747744747444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999) == "77477744774747744747444444444": {e}')
    
    total += 1
    try:
        result = candidate(k = 312500000) == "4474747444444747777744744447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 312500000) == "4474747444444747777744744447": {e}')
    
    total += 1
    try:
        result = candidate(k = 134217728) == "444444444444444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 134217728) == "444444444444444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 800000) == "7444477474744444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 800000) == "7444477474744444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 512) == "444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 512) == "444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 10000000) == "44774447447477474444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000000) == "44774447447477474444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 32768) == "444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 32768) == "444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 131072) == "44444444444444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 131072) == "44444444444444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 123456) == "7774447447444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456) == "7774447447444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 500000000) == "7747774477474774474744444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000000) == "7747774477474774474744444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 10000) == "4477744474447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000) == "4477744474447": {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000) == "7774744447447444447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000) == "7774744447447444447": {e}')
    
    total += 1
    try:
        result = candidate(k = 500000) == "777474444744744447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000) == "777474444744744447": {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321) == "77474774777744774744474774474"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321) == "77474774777744774744474774474": {e}')
    
    total += 1
    try:
        result = candidate(k = 100000) == "7444477474744447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000) == "7444477474744447": {e}')
    
    total += 1
    try:
        result = candidate(k = 50000) == "744447747474447"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50000) == "744447747474447": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 1073741823) == "444444444444444444444444444444"
    assert candidate(k = 4398046511103) == "444444444444444444444444444444444444444444"
    assert candidate(k = 50) == "74477"
    assert candidate(k = 127) == "4444444"
    assert candidate(k = 6) == "77"
    assert candidate(k = 63) == "444444"
    assert candidate(k = 1048575) == "44444444444444444444"
    assert candidate(k = 1099511627775) == "4444444444444444444444444444444444444444"
    assert candidate(k = 281474976710655) == "444444444444444444444444444444444444444444444444"
    assert candidate(k = 1) == "4"
    assert candidate(k = 140737488355327) == "44444444444444444444444444444444444444444444444"
    assert candidate(k = 17179869183) == "4444444444444444444444444444444444"
    assert candidate(k = 8191) == "4444444444444"
    assert candidate(k = 68719476735) == "444444444444444444444444444444444444"
    assert candidate(k = 262143) == "444444444444444444"
    assert candidate(k = 65535) == "4444444444444444"
    assert candidate(k = 35184372088831) == "444444444444444444444444444444444444444444444"
    assert candidate(k = 16383) == "44444444444444"
    assert candidate(k = 750) == "477747777"
    assert candidate(k = 1125899906842623) == "44444444444444444444444444444444444444444444444444"
    assert candidate(k = 2097151) == "444444444444444444444"
    assert candidate(k = 288230376151711743) == "4444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 100) == "744747"
    assert candidate(k = 32767) == "444444444444444"
    assert candidate(k = 2251799813685247) == "444444444444444444444444444444444444444444444444444"
    assert candidate(k = 1000000000) == "77477744774747744747444444447"
    assert candidate(k = 131071) == "44444444444444444"
    assert candidate(k = 2) == "7"
    assert candidate(k = 8388607) == "44444444444444444444444"
    assert candidate(k = 17592186044415) == "44444444444444444444444444444444444444444444"
    assert candidate(k = 4503599627370495) == "4444444444444444444444444444444444444444444444444444"
    assert candidate(k = 9) == "474"
    assert candidate(k = 10) == "477"
    assert candidate(k = 562949953421311) == "4444444444444444444444444444444444444444444444444"
    assert candidate(k = 549755813887) == "444444444444444444444444444444444444444"
    assert candidate(k = 36028797018963967) == "4444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 144115188075855871) == "444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 4095) == "444444444444"
    assert candidate(k = 15) == "4444"
    assert candidate(k = 2199023255551) == "44444444444444444444444444444444444444444"
    assert candidate(k = 18014398509481983) == "444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 16777215) == "444444444444444444444444"
    assert candidate(k = 2147483647) == "4444444444444444444444444444444"
    assert candidate(k = 31) == "44444"
    assert candidate(k = 8589934591) == "444444444444444444444444444444444"
    assert candidate(k = 250) == "7777477"
    assert candidate(k = 274877906943) == "44444444444444444444444444444444444444"
    assert candidate(k = 4294967295) == "44444444444444444444444444444444"
    assert candidate(k = 16) == "4447"
    assert candidate(k = 137438953471) == "4444444444444444444444444444444444444"
    assert candidate(k = 268435455) == "4444444444444444444444444444"
    assert candidate(k = 9007199254740991) == "44444444444444444444444444444444444444444444444444444"
    assert candidate(k = 8796093022207) == "4444444444444444444444444444444444444444444"
    assert candidate(k = 2047) == "44444444444"
    assert candidate(k = 524287) == "4444444444444444444"
    assert candidate(k = 5) == "74"
    assert candidate(k = 134217727) == "444444444444444444444444444"
    assert candidate(k = 4194303) == "4444444444444444444444"
    assert candidate(k = 20) == "4747"
    assert candidate(k = 1152921504606846975) == "444444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 576460752303423487) == "44444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 999) == "777747444"
    assert candidate(k = 500) == "77774747"
    assert candidate(k = 70368744177663) == "4444444444444444444444444444444444444444444444"
    assert candidate(k = 4611686018427387903) == "44444444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 33554431) == "4444444444444444444444444"
    assert candidate(k = 7) == "444"
    assert candidate(k = 4) == "47"
    assert candidate(k = 2305843009213693951) == "4444444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 255) == "44444444"
    assert candidate(k = 3) == "44"
    assert candidate(k = 67108863) == "44444444444444444444444444"
    assert candidate(k = 8) == "447"
    assert candidate(k = 34359738367) == "44444444444444444444444444444444444"
    assert candidate(k = 72057594037927935) == "44444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 1023) == "4444444444"
    assert candidate(k = 9223372036854775807) == "444444444444444444444444444444444444444444444444444444444444444"
    assert candidate(k = 511) == "444444444"
    assert candidate(k = 1000) == "777747447"
    assert candidate(k = 536870911) == "44444444444444444444444444444"
    assert candidate(k = 2048) == "44444444447"
    assert candidate(k = 99999999) == "47777747477774444744444444"
    assert candidate(k = 1024) == "4444444447"
    assert candidate(k = 67108864) == "44444444444444444444444447"
    assert candidate(k = 100000000) == "47777747477774444744444447"
    assert candidate(k = 999999) == "7774744447447444444"
    assert candidate(k = 9999999) == "44774447447477474444444"
    assert candidate(k = 50000000) == "4777774747777444474444447"
    assert candidate(k = 12345) == "7444444777474"
    assert candidate(k = 1048576) == "44444444444444444447"
    assert candidate(k = 65536) == "4444444444444447"
    assert candidate(k = 98304) == "7444444444444447"
    assert candidate(k = 5000) == "447774447447"
    assert candidate(k = 123) == "777744"
    assert candidate(k = 524288) == "4444444444444444447"
    assert candidate(k = 999999999) == "77477744774747744747444444444"
    assert candidate(k = 312500000) == "4474747444444747777744744447"
    assert candidate(k = 134217728) == "444444444444444444444444447"
    assert candidate(k = 800000) == "7444477474744444447"
    assert candidate(k = 512) == "444444447"
    assert candidate(k = 10000000) == "44774447447477474444447"
    assert candidate(k = 32768) == "444444444444447"
    assert candidate(k = 131072) == "44444444444444447"
    assert candidate(k = 123456) == "7774447447444447"
    assert candidate(k = 500000000) == "7747774477474774474744444447"
    assert candidate(k = 10000) == "4477744474447"
    assert candidate(k = 1000000) == "7774744447447444447"
    assert candidate(k = 500000) == "777474444744744447"
    assert candidate(k = 987654321) == "77474774777744774744474774474"
    assert candidate(k = 100000) == "7444477474744447"
    assert candidate(k = 50000) == "744447747474447"


