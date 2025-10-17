def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "pppppppppppppppppppppppppppppppppppppp") == "9p9p9p9p2p"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pppppppppppppppppppppppppppppppppppppp") == "9p9p9p9p2p": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde") == "1a1b1c1d1e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde") == "1a1b1c1d1e": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcc") == "2a2b2c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcc") == "2a2b2c": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaabb") == "9a5a2b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaabb") == "9a5a2b": {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababab") == "1a1b1a1b1a1b1a1b1a1b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababab") == "1a1b1a1b1a1b1a1b1a1b": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbbccccccccddddddddd") == "9a1a9b8c9d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbbccccccccddddddddd") == "9a1a9b8c9d": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabcccccaaa") == "2a1b5c3a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabcccccaaa") == "2a1b5c3a": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "2a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y2z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "2a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y2z": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijj") == "2a2b2c2d2e2f2g2h2i2j"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijj") == "2a2b2c2d2e2f2g2h2i2j": {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzz") == "9z1z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzz") == "9z1z": {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "9z9z9z9z9z5z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "9z9z9z9z9z5z": {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == "1a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == "1a": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == "2a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y9z1z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == "2a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y9z1z": {e}')
    
    total += 1
    try:
        result = candidate(word = "mmmmmmmmmmnnnnnnnnnnoooooooooollllllllkkkkkkkkkjjjjjjjjjiiiiiiiii") == "9m1m9n1n9o1o8l9k9j9i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mmmmmmmmmmnnnnnnnnnnoooooooooollllllllkkkkkkkkkjjjjjjjjjiiiiiiiii") == "9m1m9n1n9o1o8l9k9j9i": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxzyz") == "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1z1y1z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxzyz") == "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1z1y1z": {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababab") == "1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababab") == "1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b": {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiggggffffeeeeddddccccbbbbaaa") == "4z4y4x4w4v4u4t4s4r4q4p4l4k4j2i4g4f4e4d4c4b3a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiggggffffeeeeddddccccbbbbaaa") == "4z4y4x4w4v4u4t4s4r4q4p4l4k4j2i4g4f4e4d4c4b3a": {e}')
    
    total += 1
    try:
        result = candidate(word = "a9b9c9d9e9f9g9h9i9j9k9l9m9n9o9p9q9r9s9t9u9v9w9x9y9z9") == "1a191b191c191d191e191f191g191h191i191j191k191l191m191n191o191p191q191r191s191t191u191v191w191x191y191z19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a9b9c9d9e9f9g9h9i9j9k9l9m9n9o9p9q9r9s9t9u9v9w9x9y9z9") == "1a191b191c191d191e191f191g191h191i191j191k191l191m191n191o191p191q191r191s191t191u191v191w191x191y191z19": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz") == "9a1a9b8c8d9e1e9f1f9g1g9h1h9i1i9j1j9k1k9l1l9m1m9n1n9o1o9p1p9q1q9r1r9s1s9t1t9u1u9v1v9w1w9x2x9y1y9z1z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz") == "9a1a9b8c8d9e1e9f1f9g1g9h1h9i1i9j1j9k1k9l1l9m1m9n1n9o1o9p1p9q1q9r1r9s1s9t1t9u1u9v1v9w1w9x2x9y1y9z1z": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaabbccccddeeeeeeffffgggghhhhiiiiiijjjjkkkkklllllmmmmmnnnnooooo") == "6a2b4c2d6e4f4g4h6i4j5k5l5m4n5o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaabbccccddeeeeeeffffgggghhhhiiiiiijjjjkkkkklllllmmmmmnnnnooooo") == "6a2b4c2d6e4f4g4h6i4j5k5l5m4n5o": {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababababababababababababab") == "1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababababababababababababab") == "1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbcccddd") == "3a3b3c3d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbcccddd") == "3a3b3c3d": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh") == "9a1a9b1b9c1c9d9e1e9f1f9g1g9h1h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh") == "9a1a9b1b9c1c9d9e1e9f1f9g1g9h1h": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "9a9a9a9a9a9a9a9a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "9a9a9a9a9a9a9a9a": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "pppppppppppppppppppppppppppppppppppppp") == "9p9p9p9p2p"
    assert candidate(word = "abcde") == "1a1b1c1d1e"
    assert candidate(word = "aabbcc") == "2a2b2c"
    assert candidate(word = "aaaaaaaaaaaaaabb") == "9a5a2b"
    assert candidate(word = "ababababab") == "1a1b1a1b1a1b1a1b1a1b"
    assert candidate(word = "aaaaaaaaaabbbbbbbbbccccccccddddddddd") == "9a1a9b8c9d"
    assert candidate(word = "aabcccccaaa") == "2a1b5c3a"
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "2a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y2z"
    assert candidate(word = "aabbccddeeffgghhiijj") == "2a2b2c2d2e2f2g2h2i2j"
    assert candidate(word = "zzzzzzzzzz") == "9z1z"
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "9z9z9z9z9z5z"
    assert candidate(word = "a") == "1a"
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == "2a2b2c2d2e2f2g2h2i2j2k2l2m2n2o2p2q2r2s2t2u2v2w2x2y9z1z"
    assert candidate(word = "mmmmmmmmmmnnnnnnnnnnoooooooooollllllllkkkkkkkkkjjjjjjjjjiiiiiiiii") == "9m1m9n1n9o1o8l9k9j9i"
    assert candidate(word = "abcdefghijklmnopqrstuvwxzyz") == "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1z1y1z"
    assert candidate(word = "abababababababababab") == "1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b"
    assert candidate(word = "zzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiggggffffeeeeddddccccbbbbaaa") == "4z4y4x4w4v4u4t4s4r4q4p4l4k4j2i4g4f4e4d4c4b3a"
    assert candidate(word = "a9b9c9d9e9f9g9h9i9j9k9l9m9n9o9p9q9r9s9t9u9v9w9x9y9z9") == "1a191b191c191d191e191f191g191h191i191j191k191l191m191n191o191p191q191r191s191t191u191v191w191x191y191z19"
    assert candidate(word = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz") == "9a1a9b8c8d9e1e9f1f9g1g9h1h9i1i9j1j9k1k9l1l9m1m9n1n9o1o9p1p9q1q9r1r9s1s9t1t9u1u9v1v9w1w9x2x9y1y9z1z"
    assert candidate(word = "aaaaaabbccccddeeeeeeffffgggghhhhiiiiiijjjjkkkkklllllmmmmmnnnnooooo") == "6a2b4c2d6e4f4g4h6i4j5k5l5m4n5o"
    assert candidate(word = "abababababababababababababababababababab") == "1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b1a1b"
    assert candidate(word = "aaabbbcccddd") == "3a3b3c3d"
    assert candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh") == "9a1a9b1b9c1c9d9e1e9f1f9g1g9h1h"
    assert candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "9a9a9a9a9a9a9a9a"
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z"


