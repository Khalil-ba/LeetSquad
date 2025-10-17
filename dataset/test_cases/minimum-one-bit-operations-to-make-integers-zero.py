def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 756249599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 756249599: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 682: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 344: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097152) == 4194303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097152) == 4194303: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 896) == 767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 896) == 767: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == 87381
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == 87381: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108864) == 134217727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108864) == 134217727: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == 44739242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == 44739242: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 1431655765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 1431655765: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 21845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 21845: {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == 341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == 341: {e}')
    
    total += 1
    try:
        result = candidate(n = 262143) == 174762
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262143) == 174762: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == 1365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == 1365: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435456) == 536870911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435456) == 536870911: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == 10922
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == 10922: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == 32767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == 32767: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287) == 349525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287) == 349525: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 662532
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 662532: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455) == 178956970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455) == 178956970: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777216) == 33554431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777216) == 33554431: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303) == 2796202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303) == 2796202: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == 89478485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == 89478485: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 127: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == 5592405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == 5592405: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151) == 1398101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151) == 1398101: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194304) == 8388607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194304) == 8388607: {e}')
    
    total += 1
    try:
        result = candidate(n = 192) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 192) == 128: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == 268435455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == 268435455: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == 715827882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == 715827882: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554432) == 67108863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554432) == 67108863: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 11184810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 11184810: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == 2730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == 2730: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 255: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 66752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 66752: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == 170: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == 2097151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == 2097151: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 16383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 16383: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == 5461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == 5461: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 131071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 131071: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 511: {e}')
    
    total += 1
    try:
        result = candidate(n = 262144) == 524287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262144) == 524287: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 43690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 43690: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 85: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 747917089
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 747917089: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 699050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 699050: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 378124799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 378124799: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == 357913941
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == 357913941: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 687231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 687231: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 93489638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 93489638: {e}')
    
    total += 1
    try:
        result = candidate(n = 1047552) == 698368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1047552) == 698368: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 82816
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 82816: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == 22369621
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == 22369621: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 38945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 38945: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 8) == 15
    assert candidate(n = 3) == 2
    assert candidate(n = 100) == 71
    assert candidate(n = 15) == 10
    assert candidate(n = 16) == 31
    assert candidate(n = 31) == 21
    assert candidate(n = 1000000000) == 756249599
    assert candidate(n = 32) == 63
    assert candidate(n = 6) == 4
    assert candidate(n = 1023) == 682
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 344
    assert candidate(n = 7) == 5
    assert candidate(n = 10) == 12
    assert candidate(n = 1024) == 2047
    assert candidate(n = 2097152) == 4194303
    assert candidate(n = 63) == 42
    assert candidate(n = 896) == 767
    assert candidate(n = 131071) == 87381
    assert candidate(n = 67108864) == 134217727
    assert candidate(n = 4096) == 8191
    assert candidate(n = 67108863) == 44739242
    assert candidate(n = 2147483647) == 1431655765
    assert candidate(n = 32767) == 21845
    assert candidate(n = 511) == 341
    assert candidate(n = 262143) == 174762
    assert candidate(n = 2047) == 1365
    assert candidate(n = 268435456) == 536870911
    assert candidate(n = 16383) == 10922
    assert candidate(n = 16384) == 32767
    assert candidate(n = 524287) == 349525
    assert candidate(n = 987654) == 662532
    assert candidate(n = 268435455) == 178956970
    assert candidate(n = 16777216) == 33554431
    assert candidate(n = 4194303) == 2796202
    assert candidate(n = 134217727) == 89478485
    assert candidate(n = 64) == 127
    assert candidate(n = 8388607) == 5592405
    assert candidate(n = 2097151) == 1398101
    assert candidate(n = 4194304) == 8388607
    assert candidate(n = 192) == 128
    assert candidate(n = 134217728) == 268435455
    assert candidate(n = 1073741823) == 715827882
    assert candidate(n = 33554432) == 67108863
    assert candidate(n = 16777215) == 11184810
    assert candidate(n = 1073741824) == 2147483647
    assert candidate(n = 4095) == 2730
    assert candidate(n = 128) == 255
    assert candidate(n = 100000) == 66752
    assert candidate(n = 255) == 170
    assert candidate(n = 1048576) == 2097151
    assert candidate(n = 8192) == 16383
    assert candidate(n = 8191) == 5461
    assert candidate(n = 2048) == 4095
    assert candidate(n = 65536) == 131071
    assert candidate(n = 256) == 511
    assert candidate(n = 262144) == 524287
    assert candidate(n = 65535) == 43690
    assert candidate(n = 127) == 85
    assert candidate(n = 987654321) == 747917089
    assert candidate(n = 1048575) == 699050
    assert candidate(n = 500000000) == 378124799
    assert candidate(n = 536870911) == 357913941
    assert candidate(n = 1000000) == 687231
    assert candidate(n = 512) == 1023
    assert candidate(n = 123456789) == 93489638
    assert candidate(n = 1047552) == 698368
    assert candidate(n = 123456) == 82816
    assert candidate(n = 33554431) == 22369621
    assert candidate(n = 54321) == 38945


