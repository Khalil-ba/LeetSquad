def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 9) == "010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == "010": {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == "011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == "011": {e}')
    
    total += 1
    try:
        result = candidate(num = 4) == "01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4) == "01": {e}')
    
    total += 1
    try:
        result = candidate(num = 107) == "101100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 107) == "101100": {e}')
    
    total += 1
    try:
        result = candidate(num = 31) == "00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 31) == "00000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == "11011100110101100101000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == "11011100110101100101000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 5) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5) == "10": {e}')
    
    total += 1
    try:
        result = candidate(num = 500) == "11110101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500) == "11110101": {e}')
    
    total += 1
    try:
        result = candidate(num = 1000) == "111101001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000) == "111101001": {e}')
    
    total += 1
    try:
        result = candidate(num = 23) == "1000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 23) == "1000": {e}')
    
    total += 1
    try:
        result = candidate(num = 7) == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7) == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == "": {e}')
    
    total += 1
    try:
        result = candidate(num = 6) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 6) == "11": {e}')
    
    total += 1
    try:
        result = candidate(num = 2) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2) == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == "0": {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == "100101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == "100101": {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == "11011100110101100101000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == "11011100110101100101000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == "1110100001001000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == "1110100001001000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 8) == "001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8) == "001": {e}')
    
    total += 1
    try:
        result = candidate(num = 3) == "00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3) == "00": {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == "0000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == "0000": {e}')
    
    total += 1
    try:
        result = candidate(num = 999999998) == "11011100110101100100111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999998) == "11011100110101100100111111111": {e}')
    
    total += 1
    try:
        result = candidate(num = 2305843009213693951) == "0000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2305843009213693951) == "0000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1152921504606846975) == "000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1152921504606846975) == "000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 604462909807314587353087) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 604462909807314587353087) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 17179869183) == "0000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 17179869183) == "0000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 34359738367) == "00000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 34359738367) == "00000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2417851639229258349412351) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2417851639229258349412351) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 16383) == "00000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16383) == "00000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 256) == "00000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 256) == "00000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 536870912) == "00000000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 536870912) == "00000000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 154742504910672534362390527) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 154742504910672534362390527) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 274877906943) == "00000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 274877906943) == "00000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 255) == "00000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 255) == "00000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 549755813887) == "000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 549755813887) == "000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 16777216) == "000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16777216) == "000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 262143) == "000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 262143) == "000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 32) == "00001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32) == "00001": {e}')
    
    total += 1
    try:
        result = candidate(num = 32767) == "000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32767) == "000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 73786976294838206463) == "000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 73786976294838206463) == "000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 288230376151711743) == "0000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 288230376151711743) == "0000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 67108863) == "00000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 67108863) == "00000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == "0000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == "0000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 512) == "000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 512) == "000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967295) == "00000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967295) == "00000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 576460752303423487) == "00000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 576460752303423487) == "00000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1180591620717411303423) == "0000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1180591620717411303423) == "0000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4095) == "000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4095) == "000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 618970019642690137449562111) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 618970019642690137449562111) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 16384) == "00000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16384) == "00000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 8192) == "0000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8192) == "0000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 68719476735) == "000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 68719476735) == "000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 19342813113834066795298815) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 19342813113834066795298815) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4835703278458516698824703) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4835703278458516698824703) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 500000000) == "1101110011010110010100000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000000) == "1101110011010110010100000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 302231454903657293676543) == "000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 302231454903657293676543) == "000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 9223372036854775807) == "000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9223372036854775807) == "000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 131071) == "00000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 131071) == "00000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 16777215) == "000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16777215) == "000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 18014398509481983) == "000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18014398509481983) == "000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2047) == "00000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2047) == "00000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4096) == "000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4096) == "000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 511) == "000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 511) == "000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2251799813685247) == "000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2251799813685247) == "000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 281474976710655) == "000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 281474976710655) == "000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 295147905179352825855) == "00000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 295147905179352825855) == "00000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 17592186044415) == "00000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 17592186044415) == "00000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1024) == "0000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024) == "0000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 4194304) == "0000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4194304) == "0000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 100000) == "1000011010100001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000) == "1000011010100001": {e}')
    
    total += 1
    try:
        result = candidate(num = 151115727451828646838271) == "00000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 151115727451828646838271) == "00000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 524287) == "0000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 524287) == "0000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1237940039285380274899124223) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1237940039285380274899124223) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1099511627775) == "0000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1099511627775) == "0000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 536870911) == "00000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 536870911) == "00000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 18446744073709551615) == "0000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18446744073709551615) == "0000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1073741824) == "000000000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1073741824) == "000000000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 2199023255551) == "00000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2199023255551) == "00000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 8191) == "0000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8191) == "0000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 128) == "0000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 128) == "0000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 500000) == "111010000100100001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000) == "111010000100100001": {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000) == "01111101011110000100000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000) == "01111101011110000100000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 2097152) == "000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2097152) == "000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000) == "00110001001011010000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000) == "00110001001011010000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 77371252455336267181195263) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 77371252455336267181195263) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4611686018427387903) == "00000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4611686018427387903) == "00000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 36028797018963967) == "0000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 36028797018963967) == "0000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 127) == "0000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 127) == "0000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 147573952589676412927) == "0000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 147573952589676412927) == "0000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 309485009821345068724781055) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 309485009821345068724781055) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1048575) == "00000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048575) == "00000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 32768) == "000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32768) == "000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 144115188075855871) == "000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 144115188075855871) == "000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2361183241434822606847) == "00000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2361183241434822606847) == "00000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 134217728) == "000000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 134217728) == "000000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 1048576) == "00000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048576) == "00000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 35184372088831) == "000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 35184372088831) == "000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 8388607) == "00000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8388607) == "00000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 33554432) == "0000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33554432) == "0000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 1073741823) == "000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1073741823) == "000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 38685626227668133590597631) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 38685626227668133590597631) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 67108864) == "00000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 67108864) == "00000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 1208925819614629174706175) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1208925819614629174706175) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 65536) == "0000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65536) == "0000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 2048) == "00000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2048) == "00000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 8796093022207) == "0000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8796093022207) == "0000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 33554431) == "0000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33554431) == "0000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 8388608) == "00000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8388608) == "00000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 9671406556917033397649407) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9671406556917033397649407) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 9007199254740991) == "00000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9007199254740991) == "00000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1023) == "0000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1023) == "0000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 140737488355327) == "00000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 140737488355327) == "00000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 72057594037927935) == "00000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 72057594037927935) == "00000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4722366482869645213695) == "000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4722366482869645213695) == "000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4398046511103) == "000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4398046511103) == "000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 590295810358705651711) == "000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 590295810358705651711) == "000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 65535) == "0000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65535) == "0000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 63) == "000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 63) == "000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2097151) == "000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2097151) == "000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 75557863725914323419135) == "0000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 75557863725914323419135) == "0000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4194303) == "0000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4194303) == "0000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 9444732965739290427391) == "0000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9444732965739290427391) == "0000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 8589934591) == "000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8589934591) == "000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 268435456) == "0000000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 268435456) == "0000000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 70368744177663) == "0000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 70368744177663) == "0000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 137438953471) == "0000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 137438953471) == "0000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1125899906842623) == "00000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1125899906842623) == "00000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 37778931862957161709567) == "000000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 37778931862957161709567) == "000000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 268435455) == "0000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 268435455) == "0000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 18889465931478580854783) == "00000000000000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18889465931478580854783) == "00000000000000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 999999) == "1110100001001000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999) == "1110100001001000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 64) == "000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 64) == "000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 134217727) == "000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 134217727) == "000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 562949953421311) == "0000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 562949953421311) == "0000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4503599627370495) == "0000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4503599627370495) == "0000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 36893488147419103231) == "00000000000000000000000000000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 36893488147419103231) == "00000000000000000000000000000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 750000000) == "01100101101000001011110000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 750000000) == "01100101101000001011110000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 10000) == "0011100010001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000) == "0011100010001": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 9) == "010"
    assert candidate(num = 10) == "011"
    assert candidate(num = 4) == "01"
    assert candidate(num = 107) == "101100"
    assert candidate(num = 31) == "00000"
    assert candidate(num = 1000000000) == "11011100110101100101000000001"
    assert candidate(num = 5) == "10"
    assert candidate(num = 500) == "11110101"
    assert candidate(num = 1000) == "111101001"
    assert candidate(num = 23) == "1000"
    assert candidate(num = 7) == "000"
    assert candidate(num = 0) == ""
    assert candidate(num = 6) == "11"
    assert candidate(num = 2) == "1"
    assert candidate(num = 1) == "0"
    assert candidate(num = 100) == "100101"
    assert candidate(num = 999999999) == "11011100110101100101000000000"
    assert candidate(num = 1000000) == "1110100001001000001"
    assert candidate(num = 8) == "001"
    assert candidate(num = 3) == "00"
    assert candidate(num = 15) == "0000"
    assert candidate(num = 999999998) == "11011100110101100100111111111"
    assert candidate(num = 2305843009213693951) == "0000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 1152921504606846975) == "000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 604462909807314587353087) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 17179869183) == "0000000000000000000000000000000000"
    assert candidate(num = 34359738367) == "00000000000000000000000000000000000"
    assert candidate(num = 2417851639229258349412351) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 16383) == "00000000000000"
    assert candidate(num = 256) == "00000001"
    assert candidate(num = 536870912) == "00000000000000000000000000001"
    assert candidate(num = 154742504910672534362390527) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 274877906943) == "00000000000000000000000000000000000000"
    assert candidate(num = 255) == "00000000"
    assert candidate(num = 549755813887) == "000000000000000000000000000000000000000"
    assert candidate(num = 16777216) == "000000000000000000000001"
    assert candidate(num = 262143) == "000000000000000000"
    assert candidate(num = 32) == "00001"
    assert candidate(num = 32767) == "000000000000000"
    assert candidate(num = 73786976294838206463) == "000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 288230376151711743) == "0000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 67108863) == "00000000000000000000000000"
    assert candidate(num = 2147483647) == "0000000000000000000000000000000"
    assert candidate(num = 512) == "000000001"
    assert candidate(num = 4294967295) == "00000000000000000000000000000000"
    assert candidate(num = 576460752303423487) == "00000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 1180591620717411303423) == "0000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 4095) == "000000000000"
    assert candidate(num = 618970019642690137449562111) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 16384) == "00000000000001"
    assert candidate(num = 8192) == "0000000000001"
    assert candidate(num = 68719476735) == "000000000000000000000000000000000000"
    assert candidate(num = 19342813113834066795298815) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 4835703278458516698824703) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 500000000) == "1101110011010110010100000001"
    assert candidate(num = 302231454903657293676543) == "000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 9223372036854775807) == "000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 131071) == "00000000000000000"
    assert candidate(num = 16777215) == "000000000000000000000000"
    assert candidate(num = 18014398509481983) == "000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 2047) == "00000000000"
    assert candidate(num = 4096) == "000000000001"
    assert candidate(num = 511) == "000000000"
    assert candidate(num = 2251799813685247) == "000000000000000000000000000000000000000000000000000"
    assert candidate(num = 281474976710655) == "000000000000000000000000000000000000000000000000"
    assert candidate(num = 295147905179352825855) == "00000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 17592186044415) == "00000000000000000000000000000000000000000000"
    assert candidate(num = 1024) == "0000000001"
    assert candidate(num = 4194304) == "0000000000000000000001"
    assert candidate(num = 100000) == "1000011010100001"
    assert candidate(num = 151115727451828646838271) == "00000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 524287) == "0000000000000000000"
    assert candidate(num = 1237940039285380274899124223) == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 1099511627775) == "0000000000000000000000000000000000000000"
    assert candidate(num = 536870911) == "00000000000000000000000000000"
    assert candidate(num = 18446744073709551615) == "0000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 1073741824) == "000000000000000000000000000001"
    assert candidate(num = 2199023255551) == "00000000000000000000000000000000000000000"
    assert candidate(num = 8191) == "0000000000000"
    assert candidate(num = 128) == "0000001"
    assert candidate(num = 500000) == "111010000100100001"
    assert candidate(num = 100000000) == "01111101011110000100000001"
    assert candidate(num = 2097152) == "000000000000000000001"
    assert candidate(num = 10000000) == "00110001001011010000001"
    assert candidate(num = 77371252455336267181195263) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 4611686018427387903) == "00000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 36028797018963967) == "0000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 127) == "0000000"
    assert candidate(num = 147573952589676412927) == "0000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 309485009821345068724781055) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 1048575) == "00000000000000000000"
    assert candidate(num = 32768) == "000000000000001"
    assert candidate(num = 144115188075855871) == "000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 2361183241434822606847) == "00000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 134217728) == "000000000000000000000000001"
    assert candidate(num = 1048576) == "00000000000000000001"
    assert candidate(num = 35184372088831) == "000000000000000000000000000000000000000000000"
    assert candidate(num = 8388607) == "00000000000000000000000"
    assert candidate(num = 33554432) == "0000000000000000000000001"
    assert candidate(num = 1073741823) == "000000000000000000000000000000"
    assert candidate(num = 38685626227668133590597631) == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 67108864) == "00000000000000000000000001"
    assert candidate(num = 1208925819614629174706175) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 65536) == "0000000000000001"
    assert candidate(num = 2048) == "00000000001"
    assert candidate(num = 8796093022207) == "0000000000000000000000000000000000000000000"
    assert candidate(num = 33554431) == "0000000000000000000000000"
    assert candidate(num = 8388608) == "00000000000000000000001"
    assert candidate(num = 9671406556917033397649407) == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 9007199254740991) == "00000000000000000000000000000000000000000000000000000"
    assert candidate(num = 1023) == "0000000000"
    assert candidate(num = 140737488355327) == "00000000000000000000000000000000000000000000000"
    assert candidate(num = 72057594037927935) == "00000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 4722366482869645213695) == "000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 4398046511103) == "000000000000000000000000000000000000000000"
    assert candidate(num = 590295810358705651711) == "000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 65535) == "0000000000000000"
    assert candidate(num = 63) == "000000"
    assert candidate(num = 2097151) == "000000000000000000000"
    assert candidate(num = 75557863725914323419135) == "0000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 4194303) == "0000000000000000000000"
    assert candidate(num = 9444732965739290427391) == "0000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 8589934591) == "000000000000000000000000000000000"
    assert candidate(num = 268435456) == "0000000000000000000000000001"
    assert candidate(num = 70368744177663) == "0000000000000000000000000000000000000000000000"
    assert candidate(num = 137438953471) == "0000000000000000000000000000000000000"
    assert candidate(num = 1125899906842623) == "00000000000000000000000000000000000000000000000000"
    assert candidate(num = 37778931862957161709567) == "000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 268435455) == "0000000000000000000000000000"
    assert candidate(num = 18889465931478580854783) == "00000000000000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 999999) == "1110100001001000000"
    assert candidate(num = 64) == "000001"
    assert candidate(num = 134217727) == "000000000000000000000000000"
    assert candidate(num = 562949953421311) == "0000000000000000000000000000000000000000000000000"
    assert candidate(num = 4503599627370495) == "0000000000000000000000000000000000000000000000000000"
    assert candidate(num = 36893488147419103231) == "00000000000000000000000000000000000000000000000000000000000000000"
    assert candidate(num = 750000000) == "01100101101000001011110000001"
    assert candidate(num = 10000) == "0011100010001"


