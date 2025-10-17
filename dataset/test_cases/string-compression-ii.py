def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabcccd",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabcccd",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcc",k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcc",k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccabcc",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccabcc",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnhoorq",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnhoorq",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaa",k = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaa",k = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbcccaaaa",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbcccaaaa",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabbbcabbbabbbb",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabbbcabbbabbbb",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababab",k = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababab",k = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbbaa",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbbaa",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcccccaaa",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcccccaaa",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijaaaaaaaaaaaaaa",k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijaaaaaaaaaaaaaa",k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",k = 25) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",k = 25) == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 30) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 30) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 35) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 35) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbccccddddeeeeffffgggghhhh",k = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbccccddddeeeeffffgggghhhh",k = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 15) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 15) == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",k = 30) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",k = 30) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddddeeefffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwww",k = 30) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddddeeefffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwww",k = 30) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbcccccccccccdddddddddd",k = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbcccccccccccdddddddddd",k = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopq",k = 10) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopq",k = 10) == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzz",k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzz",k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 25) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 25) == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaacaaadaaaeaaafaaagaaahaaaiaaa",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaacaaadaaaeaaafaaagaaahaaaiaaa",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 25) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 25) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcde",k = 25) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcde",k = 25) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyyxxxyyyxxxxzzzzzzz",k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyyxxxyyyxxxxzzzzzzz",k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 20) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 20) == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppppppppqqqqqqqqqqrrrrrrrrrrsssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",k = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppppppppqqqqqqqqqqrrrrrrrrrrsssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",k = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbcccdddeeeeeffgggghhhiiijjjjj",k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbcccdddeeeeeffgggghhhiiijjjjj",k = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaacccaaadd",k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaacccaaadd",k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbccccddee",k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbccccddee",k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababababababababababababababab",k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababababababababababababababab",k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeffffffffgggggggghhhhhhhhiiiiiiiiijjjjjjj",k = 25) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeffffffffgggggggghhhhhhhhiiiiiiiiijjjjjjj",k = 25) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 25) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 25) == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababab",k = 10) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababab",k = 10) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 30) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 30) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",k = 20) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",k = 20) == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcd",k = 12) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcd",k = 12) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",k = 45) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",k = 45) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabb",k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabb",k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 20) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 20) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz",k = 40) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz",k = 40) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaa",k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaa",k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbcccccdddddeeeeeeeeeeee",k = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbcccccdddddeeeeeeeeeeee",k = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 15) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 15) == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppppqqqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrsssssssssssttttttttttt",k = 30) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppppqqqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrsssssssssssttttttttttt",k = 30) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd",k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd",k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggg",k = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggg",k = 25) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcabcabc",k = 5) == 3
    assert candidate(s = "aaabcccd",k = 2) == 4
    assert candidate(s = "aabcc",k = 1) == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == 32
    assert candidate(s = "aabccabcc",k = 2) == 5
    assert candidate(s = "nnnhoorq",k = 2) == 5
    assert candidate(s = "aaaaaaaaaaa",k = 0) == 3
    assert candidate(s = "aabbaa",k = 2) == 2
    assert candidate(s = "abbbcccaaaa",k = 3) == 5
    assert candidate(s = "abbbabbbcabbbabbbb",k = 3) == 6
    assert candidate(s = "aabbccddeeff",k = 6) == 6
    assert candidate(s = "abababababababababababababababababababab",k = 15) == 12
    assert candidate(s = "a",k = 0) == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 10) == 3
    assert candidate(s = "aabbbcccbbaa",k = 3) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3
    assert candidate(s = "abcdabcdabcd",k = 6) == 5
    assert candidate(s = "a",k = 1) == 0
    assert candidate(s = "aabbcc",k = 1) == 5
    assert candidate(s = "aabcccccaaa",k = 2) == 5
    assert candidate(s = "abcde",k = 2) == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 15) == 21
    assert candidate(s = "aabbccddeeff",k = 4) == 8
    assert candidate(s = "abcdefghijaaaaaaaaaaaaaa",k = 5) == 8
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 23
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",k = 25) == 64
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 30) == 14
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 35) == 18
    assert candidate(s = "mississippi",k = 3) == 6
    assert candidate(s = "aaaaaabbbbccccddddeeeeffffgggghhhh",k = 8) == 12
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 15) == 58
    assert candidate(s = "abacabadabacaba",k = 5) == 6
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",k = 30) == 25
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 25) == 3
    assert candidate(s = "aaabbbcccddddeeefffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwww",k = 30) == 26
    assert candidate(s = "aabbaabbaabbaabbaabbaabbcccccccccccdddddddddd",k = 20) == 6
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 5) == 8
    assert candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopq",k = 10) == 75
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzz",k = 10) == 18
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 25) == 53
    assert candidate(s = "aaabaaaacaaadaaaeaaafaaagaaahaaaiaaa",k = 10) == 3
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 25) == 26
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 3
    assert candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcde",k = 25) == 60
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 10) == 16
    assert candidate(s = "abababababab",k = 3) == 7
    assert candidate(s = "zzzzzyyyyyxxxyyyxxxxzzzzzzz",k = 15) == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 20) == 55
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 26
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",k = 15) == 15
    assert candidate(s = "ppppppppppqqqqqqqqqqrrrrrrrrrrsssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",k = 50) == 3
    assert candidate(s = "abbbcccdddeeeeeffgggghhhiiijjjjj",k = 10) == 12
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 25) == 3
    assert candidate(s = "aabbaacccaaadd",k = 4) == 6
    assert candidate(s = "abbbccccddee",k = 4) == 5
    assert candidate(s = "abababababababababababababababababababababababababababababababababababababababababababab",k = 20) == 50
    assert candidate(s = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeffffffffgggggggghhhhhhhhiiiiiiiiijjjjjjj",k = 25) == 14
    assert candidate(s = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 30) == 3
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 25) == 27
    assert candidate(s = "ababababababababababababababababababababab",k = 10) == 24
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 15) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 30) == 3
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 5) == 24
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 30) == 26
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",k = 20) == 59
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcd",k = 12) == 13
    assert candidate(s = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",k = 45) == 3
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 52
    assert candidate(s = "abcdefg",k = 3) == 4
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3
    assert candidate(s = "aabbaabbaabbaabbaabbaabb",k = 10) == 4
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 0
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 20) == 52
    assert candidate(s = "abababababababababababababab",k = 10) == 10
    assert candidate(s = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 50) == 3
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz",k = 40) == 13
    assert candidate(s = "aaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaa",k = 10) == 11
    assert candidate(s = "aaaaaaaaaabbbbbbbbbcccccdddddeeeeeeeeeeee",k = 20) == 5
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 15) == 37
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee",k = 10) == 10
    assert candidate(s = "ppppppqqqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrsssssssssssttttttttttt",k = 30) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 3
    assert candidate(s = "aaaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd",k = 10) == 8
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggg",k = 25) == 10


