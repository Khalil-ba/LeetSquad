def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "abddez") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abddez") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwpqrstuvwxyz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwpqrstuvwxyz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abecidof") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abecidof") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacaba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacaba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "acacacac") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acacacac") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnonmo") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnonmo") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "acxz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acxz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwert") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwert") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxyxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxyxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaabbaabbaabbaabbaabb") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaabbaabbaabbaabbaabb") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbccc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbccc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabbbbbaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabbbbbaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzyyxxwwvvuuttrrssqqppoonnllkkjjiihhggffeeddccbbaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzyyxxwwvvuuttrrssqqppoonnllkkjjiihhggffeeddccbbaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "abbbccddeeefffggghhhhiiiiijjjjkkkkllllmmmmmnnnnnooooo") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abbbccddeeefffggghhhhiiiiijjjjkkkkllllmmmmmnnnnnooooo") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaaa") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaaa") == 54: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "aazzbbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aazzbbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzyyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaaa") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzyyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaaa") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbcccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbcccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwerttyuiiooppllkkiijjhhggffeedcvvbbnnaassddffgghhjjiikkllppoouuyyttrewqq") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwerttyuiiooppllkkiijjhhggffeedcvvbbnnaassddffgghhjjiikkllppoouuyyttrewqq") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccaaaabbbbcccc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccaaaabbbbcccc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuuvvvvwwwwxxxxyyyyzzzz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuuvvvvwwwwxxxxyyyyzzzz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaaabbbaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaaabbbaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "banana") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "banana") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdeedcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdeedcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxzyxzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxzyxzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz") == 40: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeaabbccddee") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeaabbccddee") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababababababababababab") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababababababababababab") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrspqrstmnopqrspqrstmnopqrspqrst") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrspqrstmnopqrspqrstmnopqrspqrst") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabbbbbaaaaabbbbbaaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabbbbbaaaaabbbbbaaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccdddd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccdddd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "abzycxyxbwaxavauatassarapaoanamaalakajaiagafae") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abzycxyxbwaxavauatassarapaoanamaalakajaiagafae") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "abzabzabzabzabz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abzabzabzabzabz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaabbccddeeffaabbccddeeff") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaabbccddeeffaabbccddeeff") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabcabacabcabacabcabacabcabacabcabacabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabcabacabcabacabcabacabcabacabcabacabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadaba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadaba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcbaaaaaaaaaaaaa") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcbaaaaaaaaaaaaa") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabbbbbccccc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabbbbbccccc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzyyyxxxwwwwvvvuuuuttttssssrrrrqqqqppppllllooooiiiihhhhhgggggffffffeeeeeeeedddddccccbbbbaaa") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzyyyxxxwwwwvvvuuuuttttssssrrrrqqqqppppllllooooiiiihhhhhgggggffffffeeeeeeeedddddccccbbbbaaa") == 46: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "acxzacxzacxzacxzacxzacxz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acxzacxzacxzacxzacxzacxz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzyyxxwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzyyxxwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "zazazazazazazazazaza") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zazazazazazazazazaza") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababababababababababababababababababababab") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababababababababababababababababababababab") == 31: {e}')
    
    total += 1
    try:
        result = candidate(word = "bookkeeper") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bookkeeper") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababababababababababab") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababababababababababab") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababababababab") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababababababab") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "zazazazazazazazazaabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zazazazazazazazazaabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abczyxabczyxabczyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abczyxabczyxabczyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 41: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "abzabzabz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abzabzabz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacabad") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacabad") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcdabcdabcdabcd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcdabcdabcdabcd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacabadabacabad") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacabadabacabad") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "abddez") == 2
    assert candidate(word = "qrstuvwpqrstuvwxyz") == 8
    assert candidate(word = "abecidof") == 1
    assert candidate(word = "zzz") == 1
    assert candidate(word = "abacaba") == 2
    assert candidate(word = "abababab") == 4
    assert candidate(word = "acacacac") == 0
    assert candidate(word = "xyz") == 1
    assert candidate(word = "abcde") == 2
    assert candidate(word = "aabbcc") == 3
    assert candidate(word = "zzzzz") == 2
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26
    assert candidate(word = "abcdefg") == 3
    assert candidate(word = "a") == 0
    assert candidate(word = "mnonmo") == 2
    assert candidate(word = "abc") == 1
    assert candidate(word = "acxz") == 0
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 13
    assert candidate(word = "aaaaa") == 2
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 13
    assert candidate(word = "qwert") == 0
    assert candidate(word = "zyxyxyz") == 3
    assert candidate(word = "aabbaabbaabbaabbaabbaabb") == 12
    assert candidate(word = "aaabbbccc") == 4
    assert candidate(word = "aaaaabbbbbaaaa") == 7
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 39
    assert candidate(word = "zzzyyxxwwvvuuttrrssqqppoonnllkkjjiihhggffeeddccbbaa") == 25
    assert candidate(word = "abbbccddeeefffggghhhhiiiiijjjjkkkkllllmmmmmnnnnnooooo") == 26
    assert candidate(word = "mississippi") == 3
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 50
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaaa") == 54
    assert candidate(word = "aabbbcccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzz") == 52
    assert candidate(word = "aazzbbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27
    assert candidate(word = "zzzzyyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaaa") == 30
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(word = "aaaabbbbcccc") == 6
    assert candidate(word = "qwerttyuiiooppllkkiijjhhggffeedcvvbbnnaassddffgghhjjiikkllppoouuyyttrewqq") == 32
    assert candidate(word = "aaaabbbbccccaaaabbbbcccc") == 12
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuuvvvvwwwwxxxxyyyyzzzz") == 50
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 39
    assert candidate(word = "aabbaaabbbaaa") == 6
    assert candidate(word = "banana") == 1
    assert candidate(word = "abcabcabcabcabcabc") == 6
    assert candidate(word = "abcdeedcba") == 5
    assert candidate(word = "zyxzyxzyx") == 3
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 50
    assert candidate(word = "ababababababababababc") == 10
    assert candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 18
    assert candidate(word = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz") == 40
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(word = "aabbccddeeaabbccddee") == 10
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 27
    assert candidate(word = "ababababababababababababababababababababab") == 21
    assert candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyx") == 8
    assert candidate(word = "mnopqrspqrstmnopqrspqrstmnopqrspqrst") == 15
    assert candidate(word = "aaaaabbbbbaaaaabbbbbaaaa") == 12
    assert candidate(word = "aaaabbbbccccdddd") == 8
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 26
    assert candidate(word = "abzycxyxbwaxavauatassarapaoanamaalakajaiagafae") == 5
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 39
    assert candidate(word = "ababababab") == 5
    assert candidate(word = "abzabzabzabzabz") == 5
    assert candidate(word = "aabbaabbccddeeffaabbccddeeff") == 14
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 10
    assert candidate(word = "abacabcabacabcabacabcabacabcabacabcabacabc") == 12
    assert candidate(word = "abacabadabacabadaba") == 5
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcbaaaaaaaaaaaaa") == 19
    assert candidate(word = "aaaaabbbbbccccc") == 7
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb") == 25
    assert candidate(word = "zzzyyyxxxwwwwvvvuuuuttttssssrrrrqqqqppppllllooooiiiihhhhhgggggffffffeeeeeeeedddddccccbbbbaaa") == 46
    assert candidate(word = "abcabcabc") == 3
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
    assert candidate(word = "acxzacxzacxzacxzacxzacxz") == 0
    assert candidate(word = "zzzyyxxwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaa") == 27
    assert candidate(word = "zazazazazazazazazaza") == 0
    assert candidate(word = "ababababababababababababababababababababababababababababababab") == 31
    assert candidate(word = "bookkeeper") == 3
    assert candidate(word = "abababababababababababababababababab") == 18
    assert candidate(word = "abababababababababababababab") == 14
    assert candidate(word = "zazazazazazazazazaabc") == 2
    assert candidate(word = "abczyxabczyxabczyx") == 6
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 41
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 21
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa") == 27
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(word = "abzabzabz") == 3
    assert candidate(word = "abacabadabacabadabacabad") == 6
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 22
    assert candidate(word = "abcdabcdabcdabcdabcdabcd") == 12
    assert candidate(word = "abcabcabcabc") == 4
    assert candidate(word = "abacabadabacabadabacabadabacabad") == 8
    assert candidate(word = "abacabadabacaba") == 4
    assert candidate(word = "abababababababababab") == 10
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26


