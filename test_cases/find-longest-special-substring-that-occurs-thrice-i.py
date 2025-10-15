def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopmnopmnopmnop") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopmnopmnopmnop") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbaaaaaaabbaaaaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbaaaaaaabbaaaaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddaaaabbbcccddd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddaaaabbbcccddd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabaabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabaabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgggaaaabbbcccddd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgggaaaabbbcccddd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccaabbcccaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccaabbcccaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbaaaaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbaaaaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "hhhhhhhhhhhhhhhhhiiiiiiiihhhhiiiiiii") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hhhhhhhhhhhhhhhhhiiiiiiiihhhhiiiiiii") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccccc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccccc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccaaaabbbccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccaaaabbbccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyyxxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyyxxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaabbbaaabb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaabbbaaabb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyxxyyxxyy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyxxyyxxyy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzyzzzzz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzyzzzzz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzzxyzyzyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzzxyzyzyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbbbccccccbbbaabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbbbccccccbbbaabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabaaaaabaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabaaaaabaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqppqqqqqqpp") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqppqqqqqqpp") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnmmmnnnmmmnnnmmmm") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnmmmnnnmmmnnnmmmm") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbbbbbbbbb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbbbbbbbbb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaabbb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaabbb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbcccaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbcccaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffff") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffff") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccaaaabbb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccaaaabbb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzz") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzz") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaabbbbaaabbbbaaabbb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaabbbbaaabbbbaaabbb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt") == 74: {e}')
    
    total += 1
    try:
        result = candidate(s = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbaaaaaaaaabbbaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbaaaaaaaaabbbaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppqqqqqrrrrrppqqrr") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppqqqqqrrrrrppqqrr") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbaaabbaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbaaabbaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "kkkkkllllllmmmmm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kkkkkllllllmmmmm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkllkkkklllllllllllkkk") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkllkkkklllllllllllkkk") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqpppqqqpppp") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqpppqqqpppp") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddcccbbbcccbbbcccaaacccaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddcccbbbcccbbbcccaaacccaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffgggaaaabbbcccddd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffgggaaaabbbcccddd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccbbbbbbaaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccbbbbbbaaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmmmmnnnnooooo") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmmmnnnnooooo") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "tttttttttttttttttttttttttt") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tttttttttttttttttttttttttt") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabaaaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabaaaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbcccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbcccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xzyxzyxzyxzyxzyxzy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xzyxzyxzyxzyxzyxzy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 48: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzzzzzzzz") == 7
    assert candidate(s = "abcabcabc") == 1
    assert candidate(s = "aaabbbccc") == 1
    assert candidate(s = "aabbcc") == -1
    assert candidate(s = "aaaabbbbcccc") == 2
    assert candidate(s = "abcabcabcabc") == 1
    assert candidate(s = "aaaaaa") == 4
    assert candidate(s = "ababab") == 1
    assert candidate(s = "zzzzzz") == 4
    assert candidate(s = "abcaba") == 1
    assert candidate(s = "zzzzyzzzz") == 3
    assert candidate(s = "abcdef") == -1
    assert candidate(s = "aabbaabbaa") == 2
    assert candidate(s = "abcabc") == -1
    assert candidate(s = "aaaabb") == 2
    assert candidate(s = "aaabbb") == 1
    assert candidate(s = "aaaa") == 2
    assert candidate(s = "aaaabaaa") == 3
    assert candidate(s = "mnopmnopmnopmnop") == 1
    assert candidate(s = "aaaaaaaabbaaaaaaabbaaaaaaa") == 7
    assert candidate(s = "aaabbbcccdddaaaabbbcccddd") == 3
    assert candidate(s = "aabbaaabaabb") == 2
    assert candidate(s = "abcdefabcdefabcdef") == 1
    assert candidate(s = "abacabadabacabadabacabadabacabad") == 1
    assert candidate(s = "aabbccddeeefffgggaaaabbbcccddd") == 2
    assert candidate(s = "zzzzzzzzzzzzzzz") == 13
    assert candidate(s = "aabbbcccaabbcccaa") == 2
    assert candidate(s = "aaaaaaaabbaaaaaaa") == 7
    assert candidate(s = "hhhhhhhhhhhhhhhhhiiiiiiiihhhhiiiiiii") == 15
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 30
    assert candidate(s = "abcddcbaabcddcba") == 1
    assert candidate(s = "cccccccccccccccccccc") == 18
    assert candidate(s = "ccccaaaabbbccc") == 3
    assert candidate(s = "aaabbbcccddd") == 1
    assert candidate(s = "abacabadabacab") == 1
    assert candidate(s = "zzzzyyyyxxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaaa") == 2
    assert candidate(s = "aabbaabbaabbaabb") == 2
    assert candidate(s = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 44
    assert candidate(s = "aaabbbaaabbbaaabb") == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 1
    assert candidate(s = "xxyyxxyyxxyy") == 2
    assert candidate(s = "ababababababababababababababab") == 1
    assert candidate(s = "zzzzzzyzzzzz") == 5
    assert candidate(s = "zzzzzzzzzzzz") == 10
    assert candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 44
    assert candidate(s = "abababababab") == 1
    assert candidate(s = "abcabcabcabcabcabc") == 1
    assert candidate(s = "xyzxyzzxyzyzyx") == 1
    assert candidate(s = "aabbbcccbbbccccccbbbaabbcc") == 4
    assert candidate(s = "aaaaaabaaaaabaaaaa") == 5
    assert candidate(s = "mnopqrstuvwxyzaaa") == 1
    assert candidate(s = "abcdabcdabcdabcd") == 1
    assert candidate(s = "aaaaaaa") == 5
    assert candidate(s = "ppppqqppqqqqqqpp") == 4
    assert candidate(s = "abcdabcdabcdabcdabcd") == 1
    assert candidate(s = "abababababababababab") == 1
    assert candidate(s = "abababab") == 1
    assert candidate(s = "nnnmmmnnnmmmnnnmmmm") == 3
    assert candidate(s = "aaaaaaaabbbbbbbbbb") == 8
    assert candidate(s = "abacabadabacaba") == 1
    assert candidate(s = "aabbaaabbbaaaabbb") == 3
    assert candidate(s = "aabbccddeeefffggg") == 1
    assert candidate(s = "aaaaaabbbcccaabb") == 4
    assert candidate(s = "aaaabbbbccccddddeeeeffff") == 2
    assert candidate(s = "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv") == 58
    assert candidate(s = "aaabbbcccaaaabbb") == 3
    assert candidate(s = "xyxyxyxyxyxyxyx") == 1
    assert candidate(s = "zzzzzzzzzzzzz") == 11
    assert candidate(s = "aaabbbaaabbbbaaabbbbaaabbb") == 3
    assert candidate(s = "tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt") == 74
    assert candidate(s = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk") == 48
    assert candidate(s = "aaaaabbbaaaaaaaaabbbaaaa") == 7
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1
    assert candidate(s = "pppppqqqqqrrrrrppqqrr") == 3
    assert candidate(s = "aaabbaaabbaa") == 2
    assert candidate(s = "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss") == 62
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 8
    assert candidate(s = "kkkkkllllllmmmmm") == 4
    assert candidate(s = "lkllkkkklllllllllllkkk") == 9
    assert candidate(s = "ppppqpppqqqpppp") == 3
    assert candidate(s = "aaabbbcccdddcccbbbcccbbbcccaaacccaaa") == 3
    assert candidate(s = "aaabbbcccdddeeefffgggaaaabbbcccddd") == 3
    assert candidate(s = "abcddcba") == -1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == -1
    assert candidate(s = "cccccbbbbbbaaaaa") == 4
    assert candidate(s = "mmmmmnnnnooooo") == 3
    assert candidate(s = "abcabcabcabcabcab") == 1
    assert candidate(s = "tttttttttttttttttttttttttt") == 24
    assert candidate(s = "aaaaaaaabaaaaaa") == 6
    assert candidate(s = "aaaaabbbbcccc") == 3
    assert candidate(s = "xzyxzyxzyxzyxzyxzy") == 1
    assert candidate(s = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww") == 46
    assert candidate(s = "abcabcabcabcabc") == 1
    assert candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 52
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 48


