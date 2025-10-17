def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "a123bc34d8ef34") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a123bc34d8ef34") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1a2a3a4a5a6a7a8a9a0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1a2a3a4a5a6a7a8a9a0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "100leetcode") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "100leetcode") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1a1a1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1a1a1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0a001b002") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0a001b002") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "12345") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "12345") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a2b3c4d5e6f7g8h9i0j") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a2b3c4d5e6f7g8h9i0j") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "00000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "00000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0a001b1c1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0a001b1c1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "111222333444555666777888999000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "111222333444555666777888999000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "leet1234code234") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "leet1234code234") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "1234567890") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1234567890") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "000111222333444555666777888999000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000111222333444555666777888999000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "11223344556677889900") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "11223344556677889900") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b1c1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b1c1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a2b3c4d5e6f7g8h9i0j1") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a2b3c4d5e6f7g8h9i0j1") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "22o22o22o") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "22o22o22o") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b01c001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b01c001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a001b002c003") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a001b002c003") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a001001b1001c001001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a001001b1001c001001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a2b3c4d5") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a2b3c4d5") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "0a0b0c0") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0a0b0c0") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0abc00abc000abc0000abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0abc00abc000abc0000abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a10a100a1000a10000a1") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a10a100a1000a10000a1") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc456def789ghi123jkl456mno789pqr") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc456def789ghi123jkl456mno789pqr") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123xyz456abc123xyz456abc123xyz456") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123xyz456abc123xyz456abc123xyz456") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "0001abc002def03ghi0004") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0001abc002def03ghi0004") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "same123same123same123same") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "same123same123same123same") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "mixed123with456numbers789") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mixed123with456numbers789") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "000111000222000333000444000555000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000111000222000333000444000555000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc456def789ghi123jkl456mno789pqr001s002t003u") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc456def789ghi123jkl456mno789pqr001s002t003u") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc321def234ghi432jkl543mno654pqrs765tuvw876xyz987") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc321def234ghi432jkl543mno654pqrs765tuvw876xyz987") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a11a111a1111a11111a111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a11a111a1111a11111a111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "9876543210a123456789b0987654321c") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "9876543210a123456789b0987654321c") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa123bbb123ccc123ddd123eee123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa123bbb123ccc123ddd123eee123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a0b00c000d0000e00000f000000g0000000h00000000i00000000j000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a0b00c000d0000e00000f000000g0000000h00000000i00000000j000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "z9z8z7z6z5z4z3z2z1z0z9z8z7z6z5z4z3z2z1z0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "z9z8z7z6z5z4z3z2z1z0z9z8z7z6z5z4z3z2z1z0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0a01b02c03d04e05f06g07h08i09j00") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0a01b02c03d04e05f06g07h08i09j00") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "a10000b1000c100d10e1f0g00h000i0000j00000k") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a10000b1000c100d10e1f0g00h000i0000j00000k") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a10a100a1000a10000a100000a1000000a10000000a100000000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a10a100a1000a10000a100000a1000000a10000000a100000000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "1000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "123xyz456xyz789xyz123xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123xyz456xyz789xyz123xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "100000a200000b300000c400000d500000e600000f700000g800000h900000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "100000a200000b300000c400000d500000e600000f700000g800000h900000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "leading0s123trailing0s456") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "leading0s123trailing0s456") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "0001000200030004000500060007000800090000000100020003") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0001000200030004000500060007000800090000000100020003") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "same123same123same123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "same123same123same123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a001b0001c00001d000001e0000001f00000001g000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a001b0001c00001d000001e0000001f00000001g000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaa111bbbb222cccc333dddd444") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaa111bbbb222cccc333dddd444") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "a0b00c000d0000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a0b00c000d0000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc0abc00abc000abc0000abc000000abc0000000abc00000000abc000000000abc0000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc0abc00abc000abc0000abc000000abc0000000abc00000000abc000000000abc0000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "leading000trailing") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "leading000trailing") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "many000123manymany000456many000789many") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "many000123manymany000456many000789many") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1000b1000c1000d1000e1000f1000g1000h1000i1000j1000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1000b1000c1000d1000e1000f1000g1000h1000i1000j1000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc0def00ghi000jkl0000mno00000pqr000000stu") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc0def00ghi000jkl0000mno00000pqr000000stu") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0000123456789000000000123456789000000012345678900000001234567890") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0000123456789000000000123456789000000012345678900000001234567890") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0abc00abc000abc0000abc00000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0abc00abc000abc0000abc00000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0001000000001000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0001000000001000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "12345abc54321abc12345") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "12345abc54321abc12345") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "repeated000repeated000repeated") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repeated000repeated000repeated") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "z999y999x999w998v997u996") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "z999y999x999w998v997u996") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc321def456ghi654jkl789mno987pqr012stu210vwx321yz456") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc321def456ghi654jkl789mno987pqr012stu210vwx321yz456") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b01c001d0001e00001f10g100") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b01c001d0001e00001f10g100") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "9a8b7c6d5e4f3g2h1i0j9k8l7m6n5o4p3q2r1s0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "9a8b7c6d5e4f3g2h1i0j9k8l7m6n5o4p3q2r1s0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "9876543210abcdefgh0987654321") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "9876543210abcdefgh0987654321") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "9876543210zyxwvutsrqponmlkjihgfedcba9876543210") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "9876543210zyxwvutsrqponmlkjihgfedcba9876543210") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz001abc002def003ghi004jkl005") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz001abc002def003ghi004jkl005") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "000000000012345678900000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000000000012345678900000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "000abc0000def1234gh5678") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000abc0000def1234gh5678") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0a00b002c003d004e005f006g007h008i009j000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0a00b002c003d004e005f006g007h008i009j000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b01c001d0001e00001f000001g0000001h00000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b01c001d0001e00001f000001g0000001h00000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a01b002c0003d00004e000005f0000006g00000007h000000008i0000000009j0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a01b002c0003d00004e000005f0000006g00000007h000000008i0000000009j0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc456def789ghi0jklm00nopqr000stu0000vwx00000yz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc456def789ghi0jklm00nopqr000stu0000vwx00000yz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123xyz456def789ghi10jkl11mno12pqr13stu14vwx15") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123xyz456def789ghi10jkl11mno12pqr13stu14vwx15") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "000001000002000003000004000005000006000007000008000009") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000001000002000003000004000005000006000007000008000009") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123xyz456def789ghi001jkl234mno567pqr890stu0vwx123y0z456") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123xyz456def789ghi001jkl234mno567pqr890stu0vwx123y0z456") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123xyz456def456ghi789") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123xyz456def456ghi789") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a0b00c000d0000e00000f") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a0b00c000d0000e00000f") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0a000b0002c0003d0004e0005f0006g0007h0008i0009j0000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0a000b0002c0003d0004e0005f0006g0007h0008i0009j0000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "99999zzz88888xxx7777yyy6666") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "99999zzz88888xxx7777yyy6666") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "12345678901234567890123456789012345678901234567890123456789012345678901234567890") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "12345678901234567890123456789012345678901234567890123456789012345678901234567890") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123xyz456abc123") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123xyz456abc123") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123xyz456def123") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123xyz456def123") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b10c100d1000e10000f100000g1000000h10000000i100000000j1000000000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b10c100d1000e10000f100000g1000000h10000000i100000000j1000000000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "1234567890abcdefghijklmnopqrstuvwxyz0987654321") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1234567890abcdefghijklmnopqrstuvwxyz0987654321") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "0000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "00000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "00000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "010abc0010def00010ghi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "010abc0010def00010ghi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc123def123ghi123jkl123mno123pqrs123tuvw123xyz123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc123def123ghi123jkl123mno123pqrs123tuvw123xyz123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123def456ghi789jkl0123") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123def456ghi789jkl0123") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "123456789a987654321b123456789c987654321d123456789e987654321f123456789g") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123456789a987654321b123456789c987654321d123456789e987654321f123456789g") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "00123456789000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "00123456789000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0a00b000c0000d00000e000000f0000000g00000000h000000000i000000000j0") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0a00b000c0000d00000e000000f0000000g00000000h000000000i000000000j0") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a0b00c000d0000e00000f000000g0000000h00000000i0") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a0b00c000d0000e00000f000000g0000000h00000000i0") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b01c001d100e0001f10") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b01c001d100e0001f10") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc001abc01abc1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc001abc01abc1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a100000000b100000001c100000002d100000003e100000004f100000005") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a100000000b100000001c100000002d100000003e100000004f100000005") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "100000000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "100000000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "0012300abc045600def0123") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0012300abc045600def0123") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "00123004560078900100000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "00123004560078900100000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "9876543210qwertyuiopasdfghjklzxcvbnm") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "9876543210qwertyuiopasdfghjklzxcvbnm") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a0b0c00d000e0000f00000g000000h0000000i00000000j000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a0b0c00d000e0000f00000g000000h0000000i00000000j000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "123abc456def789ghi0jkl123mno456pqr789stu0vwxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "123abc456def789ghi0jkl123mno456pqr789stu0vwxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc123456def654321ghi123456") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc123456def654321ghi123456") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc1def2ghi3jkl4mno5pqr6stu7vwx8yz90123456789") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc1def2ghi3jkl4mno5pqr6stu7vwx8yz90123456789") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "0a123b456c789d0123") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "0a123b456c789d0123") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "a123b456c789d012e345f678g901") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a123b456c789d012e345f678g901") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "00100a001b001c") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "00100a001b001c") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc1abc01abc001abc0001abc00001abc000001abc0000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc1abc01abc001abc0001abc00001abc000001abc0000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc001xyz01abc100") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc001xyz01abc100") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0") == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0") == 10
    assert candidate(word = "a123bc34d8ef34") == 3
    assert candidate(word = "a1a2a3a4a5a6a7a8a9a0") == 10
    assert candidate(word = "100leetcode") == 1
    assert candidate(word = "a1a1a1") == 1
    assert candidate(word = "0a001b002") == 3
    assert candidate(word = "12345") == 1
    assert candidate(word = "1a2b3c4d5e6f7g8h9i0j") == 10
    assert candidate(word = "00000") == 1
    assert candidate(word = "0a001b1c1") == 2
    assert candidate(word = "111222333444555666777888999000") == 1
    assert candidate(word = "leet1234code234") == 2
    assert candidate(word = "1234567890") == 1
    assert candidate(word = "000111222333444555666777888999000") == 1
    assert candidate(word = "11223344556677889900") == 1
    assert candidate(word = "a1b1c1") == 1
    assert candidate(word = "1a2b3c4d5e6f7g8h9i0j1") == 10
    assert candidate(word = "abc") == 0
    assert candidate(word = "22o22o22o") == 1
    assert candidate(word = "a1b01c001") == 1
    assert candidate(word = "a001b002c003") == 3
    assert candidate(word = "a001001b1001c001001") == 1
    assert candidate(word = "1a2b3c4d5") == 5
    assert candidate(word = "0a0b0c0") == 1
    assert candidate(word = "0abc00abc000abc0000abc") == 1
    assert candidate(word = "1a10a100a1000a10000a1") == 5
    assert candidate(word = "123abc456def789ghi123jkl456mno789pqr") == 3
    assert candidate(word = "abc123xyz456abc123xyz456abc123xyz456") == 2
    assert candidate(word = "0001abc002def03ghi0004") == 4
    assert candidate(word = "same123same123same123same") == 1
    assert candidate(word = "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1") == 1
    assert candidate(word = "mixed123with456numbers789") == 3
    assert candidate(word = "000111000222000333000444000555000") == 1
    assert candidate(word = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t") == 10
    assert candidate(word = "123abc456def789ghi123jkl456mno789pqr001s002t003u") == 6
    assert candidate(word = "123abc321def234ghi432jkl543mno654pqrs765tuvw876xyz987") == 9
    assert candidate(word = "1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a1a2a3a4a5a6a7a8a9a0a") == 10
    assert candidate(word = "1a11a111a1111a11111a111111") == 6
    assert candidate(word = "9876543210a123456789b0987654321c") == 3
    assert candidate(word = "aaa123bbb123ccc123ddd123eee123") == 1
    assert candidate(word = "a0b00c000d0000e00000f000000g0000000h00000000i00000000j000000000") == 1
    assert candidate(word = "z9z8z7z6z5z4z3z2z1z0z9z8z7z6z5z4z3z2z1z0") == 10
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0a01b02c03d04e05f06g07h08i09j00") == 10
    assert candidate(word = "a10000b1000c100d10e1f0g00h000i0000j00000k") == 6
    assert candidate(word = "1a10a100a1000a10000a100000a1000000a10000000a100000000") == 9
    assert candidate(word = "1000000000000000000000000000000") == 1
    assert candidate(word = "123xyz456xyz789xyz123xyz") == 3
    assert candidate(word = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1
    assert candidate(word = "100000a200000b300000c400000d500000e600000f700000g800000h900000") == 9
    assert candidate(word = "leading0s123trailing0s456") == 3
    assert candidate(word = "0001000200030004000500060007000800090000000100020003") == 1
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6") == 10
    assert candidate(word = "same123same123same123") == 1
    assert candidate(word = "1a001b0001c00001d000001e0000001f00000001g000000001") == 1
    assert candidate(word = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1
    assert candidate(word = "aaaa111bbbb222cccc333dddd444") == 4
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0") == 10
    assert candidate(word = "a0b00c000d0000") == 1
    assert candidate(word = "abc0abc00abc000abc0000abc000000abc0000000abc00000000abc000000000abc0000000000") == 1
    assert candidate(word = "leading000trailing") == 1
    assert candidate(word = "many000123manymany000456many000789many") == 3
    assert candidate(word = "a1000b1000c1000d1000e1000f1000g1000h1000i1000j1000") == 1
    assert candidate(word = "abc0def00ghi000jkl0000mno00000pqr000000stu") == 1
    assert candidate(word = "0000123456789000000000123456789000000012345678900000001234567890") == 1
    assert candidate(word = "0abc00abc000abc0000abc00000") == 1
    assert candidate(word = "0001000000001000000001") == 1
    assert candidate(word = "12345abc54321abc12345") == 2
    assert candidate(word = "repeated000repeated000repeated") == 1
    assert candidate(word = "z999y999x999w998v997u996") == 4
    assert candidate(word = "123abc321def456ghi654jkl789mno987pqr012stu210vwx321yz456") == 8
    assert candidate(word = "a1b01c001d0001e00001f10g100") == 3
    assert candidate(word = "000000000000000001") == 1
    assert candidate(word = "9a8b7c6d5e4f3g2h1i0j9k8l7m6n5o4p3q2r1s0") == 10
    assert candidate(word = "9876543210abcdefgh0987654321") == 2
    assert candidate(word = "9876543210zyxwvutsrqponmlkjihgfedcba9876543210") == 1
    assert candidate(word = "xyz001abc002def003ghi004jkl005") == 5
    assert candidate(word = "000000000012345678900000000") == 1
    assert candidate(word = "000abc0000def1234gh5678") == 3
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0a00b002c003d004e005f006g007h008i009j000") == 10
    assert candidate(word = "a1b01c001d0001e00001f000001g0000001h00000001") == 1
    assert candidate(word = "1a01b002c0003d00004e000005f0000006g00000007h000000008i0000000009j0") == 10
    assert candidate(word = "123abc456def789ghi0jklm00nopqr000stu0000vwx00000yz") == 4
    assert candidate(word = "abc123xyz456def789ghi10jkl11mno12pqr13stu14vwx15") == 9
    assert candidate(word = "000001000002000003000004000005000006000007000008000009") == 1
    assert candidate(word = "a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1") == 1
    assert candidate(word = "abc123xyz456def789ghi001jkl234mno567pqr890stu0vwx123y0z456") == 8
    assert candidate(word = "abc123xyz456def456ghi789") == 3
    assert candidate(word = "a0b00c000d0000e00000f") == 1
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0a000b0002c0003d0004e0005f0006g0007h0008i0009j0000") == 10
    assert candidate(word = "99999zzz88888xxx7777yyy6666") == 4
    assert candidate(word = "12345678901234567890123456789012345678901234567890123456789012345678901234567890") == 1
    assert candidate(word = "abc123xyz456abc123") == 2
    assert candidate(word = "abc123xyz456def123") == 2
    assert candidate(word = "a1b10c100d1000e10000f100000g1000000h10000000i100000000j1000000000") == 10
    assert candidate(word = "1234567890abcdefghijklmnopqrstuvwxyz0987654321") == 2
    assert candidate(word = "0000000000000000000000000") == 1
    assert candidate(word = "00000000000000000000000000000000000000000000000001") == 1
    assert candidate(word = "010abc0010def00010ghi") == 1
    assert candidate(word = "123abc123def123ghi123jkl123mno123pqrs123tuvw123xyz123") == 1
    assert candidate(word = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == 1
    assert candidate(word = "abc123def456ghi789jkl0123") == 3
    assert candidate(word = "123456789a987654321b123456789c987654321d123456789e987654321f123456789g") == 2
    assert candidate(word = "00123456789000") == 1
    assert candidate(word = "0a00b000c0000d00000e000000f0000000g00000000h000000000i000000000j0") == 1
    assert candidate(word = "a0b00c000d0000e00000f000000g0000000h00000000i0") == 1
    assert candidate(word = "a1b01c001d100e0001f10") == 3
    assert candidate(word = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999") == 1
    assert candidate(word = "abc001abc01abc1") == 1
    assert candidate(word = "a100000000b100000001c100000002d100000003e100000004f100000005") == 6
    assert candidate(word = "100000000000000000000000000000000000000000000000000000001") == 1
    assert candidate(word = "0012300abc045600def0123") == 3
    assert candidate(word = "00123004560078900100000000000000000000000000000000") == 1
    assert candidate(word = "9876543210qwertyuiopasdfghjklzxcvbnm") == 1
    assert candidate(word = "a0b0c00d000e0000f00000g000000h0000000i00000000j000000000") == 1
    assert candidate(word = "123abc456def789ghi0jkl123mno456pqr789stu0vwxyz") == 4
    assert candidate(word = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7") == 10
    assert candidate(word = "abc123456def654321ghi123456") == 2
    assert candidate(word = "abc1def2ghi3jkl4mno5pqr6stu7vwx8yz90123456789") == 9
    assert candidate(word = "0a123b456c789d0123") == 4
    assert candidate(word = "a123b456c789d012e345f678g901") == 7
    assert candidate(word = "00100a001b001c") == 2
    assert candidate(word = "abc1abc01abc001abc0001abc00001abc000001abc0000001") == 1
    assert candidate(word = "abc001xyz01abc100") == 2
    assert candidate(word = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0") == 10


