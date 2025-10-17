def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "x5",k = 15) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x5",k = 15) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "y959q969u3hb22",k = 200) == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "y959q969u3hb22",k = 200) == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2d3",k = 7) == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2d3",k = 7) == "d": {e}')
    
    total += 1
    try:
        result = candidate(s = "y959q969u3hb22",k = 94921609) == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "y959q969u3hb22",k = 94921609) == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz4",k = 10) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz4",k = 10) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "y959q969u3hb22",k = 53563622) == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "y959q969u3hb22",k = 53563622) == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2345678999999999999999",k = 1) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2345678999999999999999",k = 1) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "v7",k = 6) == "v"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "v7",k = 6) == "v": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b2c2",k = 5) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b2c2",k = 5) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2",k = 2) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2",k = 2) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 1) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 1) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3",k = 6) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3",k = 6) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "x2y3",k = 5) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x2y3",k = 5) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "vzpp636m8y",k = 88699223) == "v"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vzpp636m8y",k = 88699223) == "v": {e}')
    
    total += 1
    try:
        result = candidate(s = "ha22",k = 5) == "h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ha22",k = 5) == "h": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3",k = 4) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3",k = 4) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2",k = 3) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2",k = 3) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "a9b9",k = 80) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a9b9",k = 80) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab2c3",k = 7) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab2c3",k = 7) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3",k = 7) == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3",k = 7) == "d": {e}')
    
    total += 1
    try:
        result = candidate(s = "x123",k = 3) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x123",k = 3) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet2code3",k = 10) == "o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet2code3",k = 10) == "o": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2",k = 7) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2",k = 7) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "vk7",k = 17) == "v"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vk7",k = 17) == "v": {e}')
    
    total += 1
    try:
        result = candidate(s = "large100string3",k = 250) == "i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "large100string3",k = 250) == "i": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b2c3d4e5f6g7h8i9j1k2l3m4n5o6p7q8r9s1t2u3v4w5x6y7z8",k = 1000000) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b2c3d4e5f6g7h8i9j1k2l3m4n5o6p7q8r9s1t2u3v4w5x6y7z8",k = 1000000) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc3xyz2",k = 13) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc3xyz2",k = 13) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello2world3",k = 19) == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello2world3",k = 19) == "l": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg8",k = 1000000000) == "f"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg8",k = 1000000000) == "f": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde2xyz3",k = 11) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde2xyz3",k = 11) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2efg3hij4",k = 50) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2efg3hij4",k = 50) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "nested2brackets3",k = 25) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nested2brackets3",k = 25) == "e": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2efg3hij4klm5nop6qrst7uvw8xyz9",k = 1000) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2efg3hij4klm5nop6qrst7uvw8xyz9",k = 1000) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh9",k = 999999999) == "g"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh9",k = 999999999) == "g": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab2cd3ef4gh5ij6kl7mn8op9qr0st1uv2wx3yz4",k = 750) == "v"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab2cd3ef4gh5ij6kl7mn8op9qr0st1uv2wx3yz4",k = 750) == "v": {e}')
    
    total += 1
    try:
        result = candidate(s = "z9y8x7w6v5u4t3s2r1",k = 362880) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z9y8x7w6v5u4t3s2r1",k = 362880) == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3ghi4jkl5",k = 90) == "i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3ghi4jkl5",k = 90) == "i": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet2code3xyz4",k = 25) == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet2code3xyz4",k = 25) == "l": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnop2qrst3uvw4",k = 75) == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnop2qrst3uvw4",k = 75) == "t": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello2world3",k = 18) == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello2world3",k = 18) == "l": {e}')
    
    total += 1
    try:
        result = candidate(s = "z9y8x7w6v5u4t3s2r1",k = 987654321) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z9y8x7w6v5u4t3s2r1",k = 987654321) == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b2c2d2e2f2g2h2i2j2",k = 20) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b2c2d2e2f2g2h2i2j2",k = 20) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b2c3d4e5f6g7h8i9j1",k = 500) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b2c3d4e5f6g7h8i9j1",k = 500) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello2world3",k = 17) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello2world3",k = 17) == "e": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16",k = 1000) == "j"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16",k = 1000) == "j": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab2c3d4e5f6",k = 200) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab2c3d4e5f6",k = 200) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeat2twice3",k = 27) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeat2twice3",k = 27) == "e": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz2abc3def4",k = 85) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz2abc3def4",k = 85) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz9",k = 25) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz9",k = 25) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "a9b8c7d6e5f4g3h2i1",k = 362880) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a9b8c7d6e5f4g3h2i1",k = 362880) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg2hijklm2nopqr2stuv2wxyz2",k = 50) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg2hijklm2nopqr2stuv2wxyz2",k = 50) == "e": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3ghi4",k = 46) == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3ghi4",k = 46) == "d": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz9abc8",k = 100) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz9abc8",k = 100) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet2code3",k = 15) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet2code3",k = 15) == "e": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet2code3",k = 20) == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet2code3",k = 20) == "t": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5",k = 50) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5",k = 50) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc123",k = 200) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc123",k = 200) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "complex2nested3structure4",k = 150) == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complex2nested3structure4",k = 150) == "l": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16p17q18r19s20t21u22v23w24x25y26z27",k = 2000) == "u"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16p17q18r19s20t21u22v23w24x25y26z27",k = 2000) == "u": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2efgh3ijkl4mnop5",k = 1000) == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2efgh3ijkl4mnop5",k = 1000) == "d": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh23456789",k = 876543210) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh23456789",k = 876543210) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg2hijklm3nopqr4stuv5wxyz6",k = 2000) == "k"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg2hijklm3nopqr4stuv5wxyz6",k = 2000) == "k": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello5world2",k = 45) == "o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello5world2",k = 45) == "o": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz9",k = 27) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz9",k = 27) == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeat2many3times4",k = 120) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeat2many3times4",k = 120) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3ghi4",k = 30) == "i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3ghi4",k = 30) == "i": {e}')
    
    total += 1
    try:
        result = candidate(s = "a12b3",k = 35) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a12b3",k = 35) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 1000) == "h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 1000) == "h": {e}')
    
    total += 1
    try:
        result = candidate(s = "x9y8z7",k = 200) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x9y8z7",k = 200) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "z9y8x7w6v5u4t3s2r1q9p8o7n6m5l4k3j2i1h9g8f7e6d5c4b3a2",k = 5000) == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z9y8x7w6v5u4t3s2r1q9p8o7n6m5l4k3j2i1h9g8f7e6d5c4b3a2",k = 5000) == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5",k = 11) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5",k = 11) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde2fghi3",k = 25) == "f"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde2fghi3",k = 25) == "f": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5e6",k = 50) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5e6",k = 50) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 3000) == "h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 3000) == "h": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3ghi4",k = 150) == "i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3ghi4",k = 150) == "i": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc3def4gh5",k = 100) == "h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc3def4gh5",k = 100) == "h": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz9abc3",k = 30) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz9abc3",k = 30) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4",k = 10) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4",k = 10) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc3def2ghi4",k = 40) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc3def2ghi4",k = 40) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab12c3",k = 20) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab12c3",k = 20) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7",k = 1000) == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7",k = 1000) == "t": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc123",k = 240) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc123",k = 240) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "xy2z3a4b5",k = 120) == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xy2z3a4b5",k = 120) == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5",k = 100) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5",k = 100) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "x9y8z7",k = 500) == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x9y8z7",k = 500) == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz12",k = 35) == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz12",k = 35) == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4d5",k = 40) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4d5",k = 40) == "c": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello5world3",k = 75) == "o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello5world3",k = 75) == "o": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3ghi4",k = 50) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3ghi4",k = 50) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2def3ghi4",k = 60) == "i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2def3ghi4",k = 60) == "i": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello2world2hello2world2",k = 20) == "o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello2world2hello2world2",k = 20) == "o": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr2stuv3wxyz4",k = 120) == "v"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr2stuv3wxyz4",k = 120) == "v": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet2code3abc4",k = 40) == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet2code3abc4",k = 40) == "l": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y2z2",k = 52) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y2z2",k = 52) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc123",k = 100) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc123",k = 100) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 500) == "d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 500) == "d": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet12code34",k = 100) == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet12code34",k = 100) == "t": {e}')
    
    total += 1
    try:
        result = candidate(s = "nested1nested2nested3",k = 1000) == "t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nested1nested2nested3",k = 1000) == "t": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2b3c4",k = 15) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2b3c4",k = 15) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab12cd34",k = 1234) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab12cd34",k = 1234) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello2world3",k = 14) == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello2world3",k = 14) == "l": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "x5",k = 15) == "x"
    assert candidate(s = "y959q969u3hb22",k = 200) == "y"
    assert candidate(s = "abc2d3",k = 7) == "d"
    assert candidate(s = "y959q969u3hb22",k = 94921609) == "y"
    assert candidate(s = "xyz4",k = 10) == "x"
    assert candidate(s = "y959q969u3hb22",k = 53563622) == "y"
    assert candidate(s = "a2345678999999999999999",k = 1) == "a"
    assert candidate(s = "v7",k = 6) == "v"
    assert candidate(s = "a2b2c2",k = 5) == "a"
    assert candidate(s = "abc2",k = 2) == "b"
    assert candidate(s = "abcd",k = 1) == "a"
    assert candidate(s = "abc2def3",k = 6) == "c"
    assert candidate(s = "x2y3",k = 5) == "x"
    assert candidate(s = "vzpp636m8y",k = 88699223) == "v"
    assert candidate(s = "ha22",k = 5) == "h"
    assert candidate(s = "a2b3",k = 4) == "a"
    assert candidate(s = "abc2",k = 3) == "c"
    assert candidate(s = "a9b9",k = 80) == "b"
    assert candidate(s = "ab2c3",k = 7) == "b"
    assert candidate(s = "abc2def3",k = 7) == "d"
    assert candidate(s = "x123",k = 3) == "x"
    assert candidate(s = "leet2code3",k = 10) == "o"
    assert candidate(s = "abcd2",k = 7) == "c"
    assert candidate(s = "vk7",k = 17) == "v"
    assert candidate(s = "large100string3",k = 250) == "i"
    assert candidate(s = "a2b2c3d4e5f6g7h8i9j1k2l3m4n5o6p7q8r9s1t2u3v4w5x6y7z8",k = 1000000) == "a"
    assert candidate(s = "abc3xyz2",k = 13) == "a"
    assert candidate(s = "hello2world3",k = 19) == "l"
    assert candidate(s = "abcdefg8",k = 1000000000) == "f"
    assert candidate(s = "abcde2xyz3",k = 11) == "x"
    assert candidate(s = "abcd2efg3hij4",k = 50) == "c"
    assert candidate(s = "nested2brackets3",k = 25) == "e"
    assert candidate(s = "abcd2efg3hij4klm5nop6qrst7uvw8xyz9",k = 1000) == "c"
    assert candidate(s = "abcdefgh9",k = 999999999) == "g"
    assert candidate(s = "ab2cd3ef4gh5ij6kl7mn8op9qr0st1uv2wx3yz4",k = 750) == "v"
    assert candidate(s = "z9y8x7w6v5u4t3s2r1",k = 362880) == "z"
    assert candidate(s = "abc2def3ghi4jkl5",k = 90) == "i"
    assert candidate(s = "leet2code3xyz4",k = 25) == "l"
    assert candidate(s = "mnop2qrst3uvw4",k = 75) == "t"
    assert candidate(s = "hello2world3",k = 18) == "l"
    assert candidate(s = "z9y8x7w6v5u4t3s2r1",k = 987654321) == "z"
    assert candidate(s = "a2b2c2d2e2f2g2h2i2j2",k = 20) == "a"
    assert candidate(s = "a2b2c3d4e5f6g7h8i9j1",k = 500) == "b"
    assert candidate(s = "hello2world3",k = 17) == "e"
    assert candidate(s = "a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16",k = 1000) == "j"
    assert candidate(s = "ab2c3d4e5f6",k = 200) == "c"
    assert candidate(s = "repeat2twice3",k = 27) == "e"
    assert candidate(s = "xyz2abc3def4",k = 85) == "a"
    assert candidate(s = "xyz9",k = 25) == "x"
    assert candidate(s = "a9b8c7d6e5f4g3h2i1",k = 362880) == "a"
    assert candidate(s = "abcdefg2hijklm2nopqr2stuv2wxyz2",k = 50) == "e"
    assert candidate(s = "abc2def3ghi4",k = 46) == "d"
    assert candidate(s = "xyz9abc8",k = 100) == "x"
    assert candidate(s = "leet2code3",k = 15) == "e"
    assert candidate(s = "leet2code3",k = 20) == "t"
    assert candidate(s = "a2b3c4d5",k = 50) == "b"
    assert candidate(s = "abc123",k = 200) == "b"
    assert candidate(s = "complex2nested3structure4",k = 150) == "l"
    assert candidate(s = "a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16p17q18r19s20t21u22v23w24x25y26z27",k = 2000) == "u"
    assert candidate(s = "abcd2efgh3ijkl4mnop5",k = 1000) == "d"
    assert candidate(s = "abcdefgh23456789",k = 876543210) == "b"
    assert candidate(s = "abcdefg2hijklm3nopqr4stuv5wxyz6",k = 2000) == "k"
    assert candidate(s = "hello5world2",k = 45) == "o"
    assert candidate(s = "xyz9",k = 27) == "z"
    assert candidate(s = "repeat2many3times4",k = 120) == "a"
    assert candidate(s = "abc2def3ghi4",k = 30) == "i"
    assert candidate(s = "a12b3",k = 35) == "a"
    assert candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 1000) == "h"
    assert candidate(s = "x9y8z7",k = 200) == "x"
    assert candidate(s = "z9y8x7w6v5u4t3s2r1q9p8o7n6m5l4k3j2i1h9g8f7e6d5c4b3a2",k = 5000) == "y"
    assert candidate(s = "a2b3c4d5",k = 11) == "a"
    assert candidate(s = "abcde2fghi3",k = 25) == "f"
    assert candidate(s = "a2b3c4d5e6",k = 50) == "b"
    assert candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 3000) == "h"
    assert candidate(s = "abc2def3ghi4",k = 150) == "i"
    assert candidate(s = "abc3def4gh5",k = 100) == "h"
    assert candidate(s = "xyz9abc3",k = 30) == "c"
    assert candidate(s = "a2b3c4",k = 10) == "c"
    assert candidate(s = "abc3def2ghi4",k = 40) == "a"
    assert candidate(s = "ab12c3",k = 20) == "c"
    assert candidate(s = "a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7",k = 1000) == "t"
    assert candidate(s = "abc123",k = 240) == "c"
    assert candidate(s = "xy2z3a4b5",k = 120) == "y"
    assert candidate(s = "a2b3c4d5",k = 100) == "a"
    assert candidate(s = "x9y8z7",k = 500) == "x"
    assert candidate(s = "xyz12",k = 35) == "y"
    assert candidate(s = "a2b3c4d5",k = 40) == "c"
    assert candidate(s = "hello5world3",k = 75) == "o"
    assert candidate(s = "abc2def3ghi4",k = 50) == "b"
    assert candidate(s = "abc2def3ghi4",k = 60) == "i"
    assert candidate(s = "hello2world2hello2world2",k = 20) == "o"
    assert candidate(s = "mnopqr2stuv3wxyz4",k = 120) == "v"
    assert candidate(s = "leet2code3abc4",k = 40) == "l"
    assert candidate(s = "a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y2z2",k = 52) == "b"
    assert candidate(s = "abc123",k = 100) == "a"
    assert candidate(s = "abcd2efgh3ijkl4mnop5qrst6uvw7xyz8",k = 500) == "d"
    assert candidate(s = "leet12code34",k = 100) == "t"
    assert candidate(s = "nested1nested2nested3",k = 1000) == "t"
    assert candidate(s = "a2b3c4",k = 15) == "a"
    assert candidate(s = "ab12cd34",k = 1234) == "b"
    assert candidate(s = "hello2world3",k = 14) == "l"


