def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(left = 5,right = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5,right = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 100,right = 105) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100,right = 105) == 96: {e}')
    
    total += 1
    try:
        result = candidate(left = 16,right = 31) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16,right = 31) == 16: {e}')
    
    total += 1
    try:
        result = candidate(left = 123456,right = 654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 123456,right = 654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 8,right = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8,right = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = 0,right = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 0,right = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 33,right = 35) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 33,right = 35) == 32: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 8,right = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8,right = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = 10,right = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10,right = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = 100,right = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100,right = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 4194304,right = 4194305) == 4194304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 4194304,right = 4194305) == 4194304: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000010) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000010) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(left = 4095,right = 8191) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 4095,right = 8191) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 8388608,right = 8388608) == 8388608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8388608,right = 8388608) == 8388608: {e}')
    
    total += 1
    try:
        result = candidate(left = 134217728,right = 134217729) == 134217728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 134217728,right = 134217729) == 134217728: {e}')
    
    total += 1
    try:
        result = candidate(left = 536870912,right = 536870913) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 536870912,right = 536870913) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(left = 32768,right = 32769) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 32768,right = 32769) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(left = 32,right = 33) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 32,right = 33) == 32: {e}')
    
    total += 1
    try:
        result = candidate(left = 1024,right = 2047) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1024,right = 2047) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1073741824) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1073741824) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 16777215,right = 16777216) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16777215,right = 16777216) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000000,right = 1000000100) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000000,right = 1000000100) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(left = 512,right = 1023) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 512,right = 1023) == 512: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000000,right = 200000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000000,right = 200000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 65536,right = 131071) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 65536,right = 131071) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(left = 123456,right = 123458) == 123456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 123456,right = 123458) == 123456: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 1024,right = 1025) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1024,right = 1025) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(left = 131072,right = 131073) == 131072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 131072,right = 131073) == 131072: {e}')
    
    total += 1
    try:
        result = candidate(left = 1073741824,right = 1073741825) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1073741824,right = 1073741825) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(left = 536870912,right = 1073741823) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 536870912,right = 1073741823) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 16384,right = 32767) == 16384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16384,right = 32767) == 16384: {e}')
    
    total += 1
    try:
        result = candidate(left = 512,right = 513) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 512,right = 513) == 512: {e}')
    
    total += 1
    try:
        result = candidate(left = 32768,right = 65535) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 32768,right = 65535) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(left = 16384,right = 16385) == 16384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16384,right = 16385) == 16384: {e}')
    
    total += 1
    try:
        result = candidate(left = 67108864,right = 67108865) == 67108864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 67108864,right = 67108865) == 67108864: {e}')
    
    total += 1
    try:
        result = candidate(left = 256,right = 257) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 256,right = 257) == 256: {e}')
    
    total += 1
    try:
        result = candidate(left = 64,right = 65) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 64,right = 65) == 64: {e}')
    
    total += 1
    try:
        result = candidate(left = 262144,right = 262145) == 262144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 262144,right = 262145) == 262144: {e}')
    
    total += 1
    try:
        result = candidate(left = 2097152,right = 2097153) == 2097152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2097152,right = 2097153) == 2097152: {e}')
    
    total += 1
    try:
        result = candidate(left = 16,right = 17) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16,right = 17) == 16: {e}')
    
    total += 1
    try:
        result = candidate(left = 536870912,right = 536870919) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 536870912,right = 536870919) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(left = 16777216,right = 33554431) == 16777216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16777216,right = 33554431) == 16777216: {e}')
    
    total += 1
    try:
        result = candidate(left = 2048,right = 2049) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2048,right = 2049) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(left = 512,right = 768) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 512,right = 768) == 512: {e}')
    
    total += 1
    try:
        result = candidate(left = 2147483644,right = 2147483647) == 2147483644
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2147483644,right = 2147483647) == 2147483644: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000100) == 999936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000100) == 999936: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000000,right = 500000100) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000000,right = 500000100) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(left = 4096,right = 4096) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 4096,right = 4096) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(left = 1048576,right = 1048577) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1048576,right = 1048577) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(left = 33554432,right = 33554433) == 33554432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 33554432,right = 33554433) == 33554432: {e}')
    
    total += 1
    try:
        result = candidate(left = 1073741824,right = 2147483647) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1073741824,right = 2147483647) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(left = 4,right = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 4,right = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 2147483646,right = 2147483647) == 2147483646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2147483646,right = 2147483647) == 2147483646: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 16777216,right = 16777217) == 16777216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16777216,right = 16777217) == 16777216: {e}')
    
    total += 1
    try:
        result = candidate(left = 268435456,right = 268435457) == 268435456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 268435456,right = 268435457) == 268435456: {e}')
    
    total += 1
    try:
        result = candidate(left = 32,right = 63) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 32,right = 63) == 32: {e}')
    
    total += 1
    try:
        result = candidate(left = 524288,right = 524289) == 524288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 524288,right = 524289) == 524288: {e}')
    
    total += 1
    try:
        result = candidate(left = 256,right = 511) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 256,right = 511) == 256: {e}')
    
    total += 1
    try:
        result = candidate(left = 1023,right = 1024) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1023,right = 1024) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 8192,right = 8193) == 8192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8192,right = 8193) == 8192: {e}')
    
    total += 1
    try:
        result = candidate(left = 2147483645,right = 2147483647) == 2147483644
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2147483645,right = 2147483647) == 2147483644: {e}')
    
    total += 1
    try:
        result = candidate(left = 512,right = 1024) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 512,right = 1024) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 268435456,right = 268435460) == 268435456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 268435456,right = 268435460) == 268435456: {e}')
    
    total += 1
    try:
        result = candidate(left = 1073741824,right = 1073741827) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1073741824,right = 1073741827) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(left = 130,right = 135) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 130,right = 135) == 128: {e}')
    
    total += 1
    try:
        result = candidate(left = 8388608,right = 8388609) == 8388608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8388608,right = 8388609) == 8388608: {e}')
    
    total += 1
    try:
        result = candidate(left = 134217728,right = 268435455) == 134217728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 134217728,right = 268435455) == 134217728: {e}')
    
    total += 1
    try:
        result = candidate(left = 1024,right = 2048) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1024,right = 2048) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 50,right = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 50,right = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 33554432,right = 67108863) == 33554432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 33554432,right = 67108863) == 33554432: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100099) == 99840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100099) == 99840: {e}')
    
    total += 1
    try:
        result = candidate(left = 1048576,right = 2097151) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1048576,right = 2097151) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(left = 268435456,right = 536870911) == 268435456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 268435456,right = 536870911) == 268435456: {e}')
    
    total += 1
    try:
        result = candidate(left = 4096,right = 4097) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 4096,right = 4097) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(left = 16777215,right = 16777219) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16777215,right = 16777219) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 16777215,right = 16777215) == 16777215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16777215,right = 16777215) == 16777215: {e}')
    
    total += 1
    try:
        result = candidate(left = 123456,right = 123479) == 123456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 123456,right = 123479) == 123456: {e}')
    
    total += 1
    try:
        result = candidate(left = 33554431,right = 33554432) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 33554431,right = 33554432) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 65536,right = 65537) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 65536,right = 65537) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(left = 8,right = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8,right = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = 8191,right = 8192) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8191,right = 8192) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 1048576,right = 1049087) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1048576,right = 1049087) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(left = 1048576,right = 1048580) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1048576,right = 1048580) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000000,right = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000000,right = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 2,right = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2,right = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(left = 1023,right = 2047) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1023,right = 2047) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 128,right = 128) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 128,right = 128) == 128: {e}')
    
    total += 1
    try:
        result = candidate(left = 123456,right = 123500) == 123456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 123456,right = 123500) == 123456: {e}')
    
    total += 1
    try:
        result = candidate(left = 128,right = 255) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 128,right = 255) == 128: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = 128,right = 129) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 128,right = 129) == 128: {e}')
    
    total += 1
    try:
        result = candidate(left = 16777216,right = 16777232) == 16777216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 16777216,right = 16777232) == 16777216: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(left = 5,right = 7) == 4
    assert candidate(left = 100,right = 105) == 96
    assert candidate(left = 16,right = 31) == 16
    assert candidate(left = 123456,right = 654321) == 0
    assert candidate(left = 8,right = 12) == 8
    assert candidate(left = 0,right = 0) == 0
    assert candidate(left = 33,right = 35) == 32
    assert candidate(left = 1,right = 1) == 1
    assert candidate(left = 1,right = 2147483647) == 0
    assert candidate(left = 8,right = 8) == 8
    assert candidate(left = 10,right = 15) == 8
    assert candidate(left = 100,right = 200) == 0
    assert candidate(left = 4194304,right = 4194305) == 4194304
    assert candidate(left = 1000000,right = 1000010) == 1000000
    assert candidate(left = 4095,right = 8191) == 0
    assert candidate(left = 8388608,right = 8388608) == 8388608
    assert candidate(left = 134217728,right = 134217729) == 134217728
    assert candidate(left = 536870912,right = 536870913) == 536870912
    assert candidate(left = 32768,right = 32769) == 32768
    assert candidate(left = 32,right = 33) == 32
    assert candidate(left = 1024,right = 2047) == 1024
    assert candidate(left = 1,right = 1073741824) == 0
    assert candidate(left = 16777215,right = 16777216) == 0
    assert candidate(left = 1000000000,right = 1000000100) == 1000000000
    assert candidate(left = 512,right = 1023) == 512
    assert candidate(left = 100000000,right = 200000000) == 0
    assert candidate(left = 65536,right = 131071) == 65536
    assert candidate(left = 123456,right = 123458) == 123456
    assert candidate(left = 1,right = 3) == 0
    assert candidate(left = 1024,right = 1025) == 1024
    assert candidate(left = 131072,right = 131073) == 131072
    assert candidate(left = 1073741824,right = 1073741825) == 1073741824
    assert candidate(left = 536870912,right = 1073741823) == 536870912
    assert candidate(left = 1,right = 10) == 0
    assert candidate(left = 16384,right = 32767) == 16384
    assert candidate(left = 512,right = 513) == 512
    assert candidate(left = 32768,right = 65535) == 32768
    assert candidate(left = 16384,right = 16385) == 16384
    assert candidate(left = 67108864,right = 67108865) == 67108864
    assert candidate(left = 256,right = 257) == 256
    assert candidate(left = 64,right = 65) == 64
    assert candidate(left = 262144,right = 262145) == 262144
    assert candidate(left = 2097152,right = 2097153) == 2097152
    assert candidate(left = 16,right = 17) == 16
    assert candidate(left = 536870912,right = 536870919) == 536870912
    assert candidate(left = 16777216,right = 33554431) == 16777216
    assert candidate(left = 2048,right = 2049) == 2048
    assert candidate(left = 512,right = 768) == 512
    assert candidate(left = 2147483644,right = 2147483647) == 2147483644
    assert candidate(left = 1000000,right = 1000100) == 999936
    assert candidate(left = 500000000,right = 500000100) == 500000000
    assert candidate(left = 4096,right = 4096) == 4096
    assert candidate(left = 1048576,right = 1048577) == 1048576
    assert candidate(left = 33554432,right = 33554433) == 33554432
    assert candidate(left = 1073741824,right = 2147483647) == 1073741824
    assert candidate(left = 4,right = 7) == 4
    assert candidate(left = 2147483646,right = 2147483647) == 2147483646
    assert candidate(left = 1,right = 1000) == 0
    assert candidate(left = 16777216,right = 16777217) == 16777216
    assert candidate(left = 268435456,right = 268435457) == 268435456
    assert candidate(left = 32,right = 63) == 32
    assert candidate(left = 524288,right = 524289) == 524288
    assert candidate(left = 256,right = 511) == 256
    assert candidate(left = 1023,right = 1024) == 0
    assert candidate(left = 8192,right = 8193) == 8192
    assert candidate(left = 2147483645,right = 2147483647) == 2147483644
    assert candidate(left = 512,right = 1024) == 0
    assert candidate(left = 268435456,right = 268435460) == 268435456
    assert candidate(left = 1073741824,right = 1073741827) == 1073741824
    assert candidate(left = 130,right = 135) == 128
    assert candidate(left = 8388608,right = 8388609) == 8388608
    assert candidate(left = 134217728,right = 268435455) == 134217728
    assert candidate(left = 1024,right = 2048) == 0
    assert candidate(left = 50,right = 100) == 0
    assert candidate(left = 33554432,right = 67108863) == 33554432
    assert candidate(left = 100000,right = 100099) == 99840
    assert candidate(left = 1048576,right = 2097151) == 1048576
    assert candidate(left = 268435456,right = 536870911) == 268435456
    assert candidate(left = 4096,right = 4097) == 4096
    assert candidate(left = 16777215,right = 16777219) == 0
    assert candidate(left = 16777215,right = 16777215) == 16777215
    assert candidate(left = 123456,right = 123479) == 123456
    assert candidate(left = 33554431,right = 33554432) == 0
    assert candidate(left = 65536,right = 65537) == 65536
    assert candidate(left = 8,right = 15) == 8
    assert candidate(left = 8191,right = 8192) == 0
    assert candidate(left = 1048576,right = 1049087) == 1048576
    assert candidate(left = 1048576,right = 1048580) == 1048576
    assert candidate(left = 500000000,right = 1000000000) == 0
    assert candidate(left = 2,right = 3) == 2
    assert candidate(left = 1023,right = 2047) == 0
    assert candidate(left = 128,right = 128) == 128
    assert candidate(left = 123456,right = 123500) == 123456
    assert candidate(left = 128,right = 255) == 128
    assert candidate(left = 1,right = 1000000000) == 0
    assert candidate(left = 128,right = 129) == 128
    assert candidate(left = 16777216,right = 16777232) == 16777216


