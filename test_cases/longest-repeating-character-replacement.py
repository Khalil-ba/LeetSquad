def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "ABABABAB",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABAB",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAABBBAABBCCDDEE",k = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAABBBAABBCCDDEE",k = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBCCDD",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBCCDD",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "A",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABAABBBCCCC",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABAABBBCCCC",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABBBB",k = 0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABBBB",k = 0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCCDEEEEE",k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCCDEEEEE",k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABAB",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABAB",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBB",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBB",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ZYXWVUTSRQPONMLKJIHGFEDCBA",k = 25) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ZYXWVUTSRQPONMLKJIHGFEDCBA",k = 25) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABACBCAB",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABACBCAB",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABBB",k = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABBB",k = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABBB",k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABBB",k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDE",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDE",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABABBA",k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABABBA",k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCC",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCC",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAA",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAA",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDE",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDE",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDE",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDE",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBBBCCDDDDD",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBBBCCDDDDD",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ACBACBACBACBACBACBACBACBACBACBAC",k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ACBACBACBACBACBACBACBACBACBACBAC",k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 0) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 0) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDD",k = 15) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDD",k = 15) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAA",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAA",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCABCABCABCABCABCABCABCABCABC",k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCABCABCABCABCABCABCABCABCABC",k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAABBBBCCCC",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAABBBBCCCC",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABAB",k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABAB",k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",k = 25) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",k = 25) == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDDAAABBBCCCDDD",k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDDAAABBBCCCDDD",k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWERTYUIOPASDFGHJKLZXCVBNM",k = 24) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWERTYUIOPASDFGHJKLZXCVBNM",k = 24) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAABBBCCCCCCAAAAAAAAAAA",k = 6) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAABBBCCCCCCAAAAAAAAAAA",k = 6) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBAABBCCDDDDDDDEEFFGGHHIIJJJKKKLLLMMMNNN",k = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBAABBCCDDDDDDDEEFFGGHHIIJJJKKKLLLMMMNNN",k = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAABBBBBBBBBBBCCCCCCDDDDDDDDDDD",k = 25) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAABBBBBBBBBBBCCCCCCDDDDDDDDDDD",k = 25) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMMNNNNOOOO",k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMMNNNNOOOO",k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAABBB",k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAABBB",k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABABABABAB",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABABABABAB",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABABABABABABABABABAB",k = 15) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABABABABABABABABABAB",k = 15) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABACABAACBACABCABACBACABCABACBACABCABACBACABCABACBACAB",k = 20) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABACABAACBACABCABACBACABCABACBACABCABACBACABCABACBACAB",k = 20) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAABBBBBBBBCCCCCCCCCC",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAABBBBBBBBCCCCCCCCCC",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEABCDEABCDEABCDEABCDE",k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEABCDEABCDEABCDEABCDE",k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABBCCCDDDDEEEEEFFFFFF",k = 6) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABBCCCDDDDEEEEEFFFFFF",k = 6) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABAB",k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABAB",k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABACABACABACABACABACABACABACABACABACABAC",k = 15) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABACABACABACABACABACABACABACABACABACABAC",k = 15) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABABABABABABABABABABABABAB",k = 15) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABABABABABABABABABABABABAB",k = 15) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABABABABABABABABAB",k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABABABABABABABABAB",k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABABABABABABABABABABABABABABABAB",k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABABABABABABABABABABABABABABABAB",k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABCABCABCABCABCABC",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABCABCABCABCABCABC",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "BAAAAAAAAAABAAAAAAAAAAB",k = 5) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BAAAAAAAAAABAAAAAAAAAAB",k = 5) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBCCDDEEFFGG",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBCCDDEEFFGG",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ACACACACACACAC",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ACACACACACACAC",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD",k = 20) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD",k = 20) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB",k = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB",k = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABACABACABACABACABACABACABACABAC",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABACABACABACABACABACABACABACABAC",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDD",k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDD",k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "XYZXYZXYZXYZXYZXYZXYZXYZ",k = 15) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XYZXYZXYZXYZXYZXYZXYZXYZ",k = 15) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEABCDEABCDEABCDEABCDEABCDE",k = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEABCDEABCDEABCDEABCDEABCDE",k = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABBBABAABBBBBBBBAAABBB",k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABBBABAABBBBBBBBAAABBB",k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 100) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 100) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAABBBBBBBBBBB",k = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAABBBBBBBBBBB",k = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABAB",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABAB",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBCCDDEEFFF",k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBCCDDEEFFF",k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAB",k = 1) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAB",k = 1) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "XYZXYZXYZXYZ",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XYZXYZXYZXYZ",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",k = 26) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",k = 26) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABAB",k = 8) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABAB",k = 8) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAAAAAA",k = 0) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAAAAAA",k = 0) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBBCCCDDDDDEEEEFFFFFFGGGGGGHHHHHIIIJJJKKKLLLLMMMMNNNNOOOOPPPP",k = 30) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBBCCCDDDDDEEEEFFFFFFGGGGGGHHHHHIIIJJJKKKLLLLMMMMNNNNOOOOPPPP",k = 30) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "BBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAA",k = 5) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAA",k = 5) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABABBAACCCDDDEEE",k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABABBAACCCDDDEEE",k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",k = 0) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",k = 0) == 106: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAABBBBBBBB",k = 0) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAABBBBBBBB",k = 0) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABAB",k = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABAB",k = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVWWWXXXXYYYYZZZZ",k = 50) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVWWWXXXXYYYYZZZZ",k = 50) == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB",k = 50) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB",k = 50) == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",k = 100) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",k = 100) == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCABCABCABCABCABCABCABC",k = 15) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCABCABCABCABCABCABCABC",k = 15) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBBCCDDEE",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBBCCDDEE",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",k = 1000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",k = 1000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 100) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 100) == 108: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ",k = 20) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ",k = 20) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDD",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDD",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAA",k = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAA",k = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBBCCCDDDD",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBBCCCDDDD",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDDEEEFFF",k = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDDEEEFFF",k = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAABBBBBBBBCCCCCCCCCC",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAABBBBBBBBCCCCCCCCCC",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "BBBAAAABBBAAAABBBAAAABBB",k = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BBBAAAABBBAAAABBBAAAABBB",k = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABABAB",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABABAB",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "ACACACACACACACACACACACAC",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ACACACACACACACACACACACAC",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABACABACABAC",k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABACABACABAC",k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABABABABABABABABABAB",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABABABABABABABABABAB",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAABBBCCCDDDDDD",k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAABBBCCCDDDDDD",k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "BBBBAAAACCCD",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BBBBAAAACCCD",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWERTYUIOPASDFGHJKLZXCVBNM",k = 26) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWERTYUIOPASDFGHJKLZXCVBNM",k = 26) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "XYZXYZXYZXYZXYZXYZ",k = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XYZXYZXYZXYZXYZXYZ",k = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAABBBBCCCCCDDDD",k = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAABBBBCCCCCDDDD",k = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "BBBBAAAACCCCDDDD",k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BBBBAAAACCCCDDDD",k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "XYZXYZXYZXYZXYZXYZXYZXYZ",k = 20) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XYZXYZXYZXYZXYZXYZXYZXYZ",k = 20) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAABBBBBBBB",k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAABBBBBBBB",k = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAAAAAAAAAAAAAAABBB",k = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAAAAAAAAAAAAAAABBB",k = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "XYZXYZXYZ",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XYZXYZXYZ",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBCDEEFGHIJKLLMNOPQRSTUVWXYZ",k = 25) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBCDEEFGHIJKLLMNOPQRSTUVWXYZ",k = 25) == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABABBAABBCCDDEEFFGG",k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABABBAABBCCDDEEFFGG",k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ",k = 25) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ",k = 25) == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "AAABBBCCCDDD",k = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AAABBBCCCDDD",k = 6) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "ABABABAB",k = 3) == 7
    assert candidate(s = "AAAAAAAAAAAAABBBAABBCCDDEE",k = 5) == 20
    assert candidate(s = "AABBCCDD",k = 2) == 4
    assert candidate(s = "",k = 0) == 0
    assert candidate(s = "A",k = 1) == 1
    assert candidate(s = "AABAABBBCCCC",k = 3) == 7
    assert candidate(s = "ABBBB",k = 0) == 4
    assert candidate(s = "ABCCDEEEEE",k = 3) == 8
    assert candidate(s = "ABAB",k = 2) == 4
    assert candidate(s = "AABBB",k = 2) == 5
    assert candidate(s = "ZYXWVUTSRQPONMLKJIHGFEDCBA",k = 25) == 26
    assert candidate(s = "ABACBCAB",k = 2) == 4
    assert candidate(s = "ABBB",k = 0) == 3
    assert candidate(s = "ABBB",k = 1) == 4
    assert candidate(s = "ABCDE",k = 1) == 2
    assert candidate(s = "AABABBA",k = 1) == 4
    assert candidate(s = "AAABBBCCC",k = 3) == 6
    assert candidate(s = "AAAA",k = 2) == 4
    assert candidate(s = "ABCDE",k = 3) == 4
    assert candidate(s = "ABCDE",k = 2) == 3
    assert candidate(s = "AABBBBCCDDDDD",k = 2) == 7
    assert candidate(s = "ACBACBACBACBACBACBACBACBACBACBAC",k = 5) == 8
    assert candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 0) == 40
    assert candidate(s = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDD",k = 15) == 26
    assert candidate(s = "AAAAAAAAAA",k = 5) == 10
    assert candidate(s = "ABCABCABCABCABCABCABCABCABCABC",k = 10) == 16
    assert candidate(s = "AAAAAAAAAAAABBBBCCCC",k = 10) == 20
    assert candidate(s = "ABABABAB",k = 1) == 3
    assert candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",k = 25) == 27
    assert candidate(s = "AAABBBCCCDDDAAABBBCCCDDD",k = 7) == 10
    assert candidate(s = "QWERTYUIOPASDFGHJKLZXCVBNM",k = 24) == 25
    assert candidate(s = "AAAAAAAAAAAABBBCCCCCCAAAAAAAAAAA",k = 6) == 18
    assert candidate(s = "AAABBBAABBCCDDDDDDDEEFFGGHHIIJJJKKKLLLMMMNNN",k = 25) == 32
    assert candidate(s = "AAAAAAAAAABBBBBBBBBBBCCCCCCDDDDDDDDDDD",k = 25) == 36
    assert candidate(s = "MMMMNNNNOOOO",k = 5) == 9
    assert candidate(s = "AAAAAAAAABBB",k = 2) == 11
    assert candidate(s = "AABABABABAB",k = 5) == 11
    assert candidate(s = "ABABABABABABABABABABABABABABABABAB",k = 15) == 31
    assert candidate(s = "ABACABAACBACABCABACBACABCABACBACABCABACBACABCABACBACAB",k = 20) == 36
    assert candidate(s = "AAAAAAAAAABBBBBBBBCCCCCCCCCC",k = 10) == 20
    assert candidate(s = "ABCDEABCDEABCDEABCDEABCDE",k = 10) == 13
    assert candidate(s = "ABBCCCDDDDEEEEEFFFFFF",k = 6) == 12
    assert candidate(s = "ABABABABABABABABAB",k = 10) == 18
    assert candidate(s = "ABACABACABACABACABACABACABACABACABACABAC",k = 15) == 31
    assert candidate(s = "ABABABABABABABABABABABABABABABABABABABAB",k = 15) == 31
    assert candidate(s = "ABABABABABABABABABABABABABABABAB",k = 0) == 1
    assert candidate(s = "AABABABABABABABABABABABABABABABAB",k = 5) == 12
    assert candidate(s = "AABCABCABCABCABCABC",k = 4) == 8
    assert candidate(s = "BAAAAAAAAAABAAAAAAAAAAB",k = 5) == 23
    assert candidate(s = "AABBCCDDEEFFGG",k = 3) == 5
    assert candidate(s = "ACACACACACACAC",k = 2) == 5
    assert candidate(s = "AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD",k = 20) == 29
    assert candidate(s = "ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB",k = 10) == 21
    assert candidate(s = "ABACABACABACABACABACABACABACABAC",k = 5) == 11
    assert candidate(s = "AAABBBCCCDDD",k = 4) == 7
    assert candidate(s = "XYZXYZXYZXYZXYZXYZXYZXYZ",k = 15) == 23
    assert candidate(s = "ABCDEABCDEABCDEABCDEABCDEABCDE",k = 6) == 8
    assert candidate(s = "ABBBABAABBBBBBBBAAABBB",k = 5) == 17
    assert candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 100) == 60
    assert candidate(s = "AAAAAAAAAAABBBBBBBBBBB",k = 10) == 21
    assert candidate(s = "ABABABABAB",k = 5) == 10
    assert candidate(s = "AAABBCCDDEEFFF",k = 4) == 7
    assert candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAB",k = 1) == 24
    assert candidate(s = "XYZXYZXYZXYZ",k = 3) == 5
    assert candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",k = 26) == 26
    assert candidate(s = "ABABABABABABABAB",k = 8) == 16
    assert candidate(s = "AAAAAAAAAAAAAAAAAAAA",k = 0) == 20
    assert candidate(s = "AABBBCCCDDDDDEEEEFFFFFFGGGGGGHHHHHIIIJJJKKKLLLLMMMMNNNNOOOOPPPP",k = 30) == 36
    assert candidate(s = "BBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAA",k = 5) == 26
    assert candidate(s = "AABABBAACCCDDDEEE",k = 3) == 8
    assert candidate(s = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",k = 0) == 106
    assert candidate(s = "AAAAAAAABBBBBBBB",k = 0) == 8
    assert candidate(s = "ABABABABABABAB",k = 7) == 14
    assert candidate(s = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVWWWXXXXYYYYZZZZ",k = 50) == 54
    assert candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB",k = 50) == 41
    assert candidate(s = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",k = 100) == 44
    assert candidate(s = "ABCABCABCABCABCABCABCABC",k = 15) == 23
    assert candidate(s = "AABBBCCDDEE",k = 2) == 5
    assert candidate(s = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",k = 1000) == 31
    assert candidate(s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",k = 100) == 108
    assert candidate(s = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ",k = 20) == 22
    assert candidate(s = "AAABBBCCCDDD",k = 3) == 6
    assert candidate(s = "AAAAA",k = 0) == 5
    assert candidate(s = "AABBBCCCDDDD",k = 3) == 7
    assert candidate(s = "AAABBBCCCDDDEEEFFF",k = 6) == 9
    assert candidate(s = "AAAAAAAAABBBBBBBBCCCCCCCCCC",k = 10) == 20
    assert candidate(s = "BBBAAAABBBAAAABBBAAAABBB",k = 5) == 13
    assert candidate(s = "ABABABABABABABABABAB",k = 5) == 11
    assert candidate(s = "ACACACACACACACACACACACAC",k = 5) == 11
    assert candidate(s = "ABACABACABAC",k = 4) == 9
    assert candidate(s = "ABABABABABABABABABAB",k = 10) == 20
    assert candidate(s = "AAAAAAABBBCCCDDDDDD",k = 5) == 12
    assert candidate(s = "BBBBAAAACCCD",k = 4) == 8
    assert candidate(s = "QWERTYUIOPASDFGHJKLZXCVBNM",k = 26) == 26
    assert candidate(s = "XYZXYZXYZXYZXYZXYZ",k = 6) == 10
    assert candidate(s = "AAAAAAAAAAABBBBCCCCCDDDD",k = 10) == 21
    assert candidate(s = "BBBBAAAACCCCDDDD",k = 5) == 9
    assert candidate(s = "XYZXYZXYZXYZXYZXYZXYZXYZ",k = 20) == 24
    assert candidate(s = "AAAAAAAABBBBBBBB",k = 3) == 11
    assert candidate(s = "AAAAAAAAAAAAAAAABBB",k = 2) == 18
    assert candidate(s = "XYZXYZXYZ",k = 3) == 5
    assert candidate(s = "AABBCDEEFGHIJKLLMNOPQRSTUVWXYZ",k = 25) == 27
    assert candidate(s = "AABABBAABBCCDDEEFFGG",k = 4) == 9
    assert candidate(s = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ",k = 25) == 27
    assert candidate(s = "AAABBBCCCDDD",k = 6) == 9


