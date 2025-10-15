def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aeiaaioaaaaeiiiiouuuooououuoiiiuuuuaeiou",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaaioaaaaeiiiiouuuooououuoiiiuuuuaeiou",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "baeyh",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baeyh",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaeaeaaeiou",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaeaeaaeiou",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdf",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdf",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiou",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiou",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsandconsonants",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsandconsonants",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba",k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba",k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebcde",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcde",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiou",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiou",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulstring",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulstring",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "consonantsandvowels",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consonantsandvowels",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsvowelsvowelsvowels",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsvowelsvowelsvowels",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithabunchoflettersandvariousvowelsandconsonants",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithabunchoflettersandvariousvowelsandconsonants",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbc",k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbc",k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebcdefghijklmnopqrstuvwxyz",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcdefghijklmnopqrstuvwxyz",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsandconsonants",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsandconsonants",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiou",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiou",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vwxyzvwxyzvwxyzvwxyz",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vwxyzvwxyzvwxyzvwxyz",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcd",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcd",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffff",k = 16) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffff",k = 16) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyzbcd",k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyzbcd",k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharactersaaaaaaaabbbbbbbbcccccccc",k = 16) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharactersaaaaaaaabbbbbbbbcccccccc",k = 16) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaeeiioouu",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaeeiioouu",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisalongstringwithvariousvowelsandconsonants",k = 36) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisalongstringwithvariousvowelsandconsonants",k = 36) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulstring",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulstring",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghefghijklmnopqrstuvwxyz",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghefghijklmnopqrstuvwxyz",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzaaaaabbbbbbccccccdddddd",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzaaaaabbbbbbccccccdddddd",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiou",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiou",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfg",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfg",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcaedfghioklmnpqrstuvwxyz",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcaedfghioklmnpqrstuvwxyz",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyzzzzzzzz",k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyzzzzzzzz",k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulstring",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulstring",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",k = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",k = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaeeiioouubbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaeeiioouubbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeeeeiiioouu",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeeeeiiioouu",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiou",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiou",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelvowelvowelvowelvowel",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelvowelvowelvowelvowel",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaabbbbbbbbbb",k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaabbbbbbbbbb",k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 2) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 2) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiouaeiouaeiouaeiou",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiouaeiouaeiouaeiou",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithvariouscharacters",k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithvariouscharacters",k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz",k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz",k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiaeiouaeiaeiouaeiaeiou",k = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaeiouaeiaeiouaeiaeiou",k = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz",k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz",k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "consonantconsonantconsonant",k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consonantconsonantconsonant",k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsconsonants",k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsconsonants",k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebcdeioufhgjk",k = 12) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcdeioufhgjk",k = 12) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcxyzabc",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcxyzabc",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbb",k = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbb",k = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsandconsonants",k = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsandconsonants",k = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyz",k = 26) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyz",k = 26) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbcccc",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbcccc",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulsubstring",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulsubstring",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abecidofug",k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abecidofug",k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewwq",k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewwq",k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiou",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiou",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaeeeeeeiiioooouuuu",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaeeeeeeiiioooouuuu",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "consonantsconsonantsconsonants",k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consonantsconsonantsconsonants",k = 9) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aeiaaioaaaaeiiiiouuuooououuoiiiuuuuaeiou",k = 10) == 0
    assert candidate(s = "aabbcc",k = 4) == 1
    assert candidate(s = "zzzzz",k = 1) == 0
    assert candidate(s = "",k = 1) == 0
    assert candidate(s = "baeyh",k = 2) == 2
    assert candidate(s = "bbaeaeaaeiou",k = 3) == 0
    assert candidate(s = "bcdf",k = 1) == 0
    assert candidate(s = "aeiou",k = 25) == 0
    assert candidate(s = "vowelsandconsonants",k = 10) == 0
    assert candidate(s = "",k = 3) == 0
    assert candidate(s = "abba",k = 1) == 3
    assert candidate(s = "abcdefghij",k = 2) == 0
    assert candidate(s = "aebcde",k = 3) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 7) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2) == 0
    assert candidate(s = "a",k = 1) == 0
    assert candidate(s = "aeiou",k = 5) == 0
    assert candidate(s = "beautifulstring",k = 7) == 0
    assert candidate(s = "aabbccddeeff",k = 4) == 4
    assert candidate(s = "aaabbbcccddd",k = 6) == 0
    assert candidate(s = "consonantsandvowels",k = 20) == 0
    assert candidate(s = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 12) == 0
    assert candidate(s = "vowelsvowelsvowelsvowels",k = 4) == 8
    assert candidate(s = "thisisaverylongstringwithabunchoflettersandvariousvowelsandconsonants",k = 10) == 0
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbc",k = 11) == 0
    assert candidate(s = "aebcdefghijklmnopqrstuvwxyz",k = 5) == 0
    assert candidate(s = "abacabadabacaba",k = 10) == 0
    assert candidate(s = "vowelsandconsonants",k = 6) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 100) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 13) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 20) == 0
    assert candidate(s = "aeiouaeiouaeiou",k = 25) == 0
    assert candidate(s = "vwxyzvwxyzvwxyzvwxyz",k = 20) == 0
    assert candidate(s = "abcdabcdabcdabcdabcdabcd",k = 9) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 0
    assert candidate(s = "aaaabbbbccccddddeeeeffff",k = 16) == 6
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",k = 3) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyzbcd",k = 15) == 0
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 11) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz",k = 20) == 0
    assert candidate(s = "abcdeffedcba",k = 4) == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 2) == 0
    assert candidate(s = "repeatedcharactersaaaaaaaabbbbbbbbcccccccc",k = 16) == 13
    assert candidate(s = "aaeeiioouu",k = 10) == 0
    assert candidate(s = "thisisalongstringwithvariousvowelsandconsonants",k = 36) == 6
    assert candidate(s = "beautifulstring",k = 3) == 2
    assert candidate(s = "abcdefghefghijklmnopqrstuvwxyz",k = 8) == 0
    assert candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 25) == 1
    assert candidate(s = "zzzzzaaaaabbbbbbccccccdddddd",k = 12) == 0
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0
    assert candidate(s = "aeiouaeiou",k = 5) == 0
    assert candidate(s = "aeioubcdfg",k = 5) == 1
    assert candidate(s = "bcaedfghioklmnpqrstuvwxyz",k = 7) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyzzzzzzzz",k = 11) == 0
    assert candidate(s = "beautifulstring",k = 2) == 5
    assert candidate(s = "abababababababababab",k = 6) == 9
    assert candidate(s = "aaeeiioouubbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 1
    assert candidate(s = "aeeeeiiioouu",k = 10) == 0
    assert candidate(s = "aeiouaeiouaeiou",k = 3) == 0
    assert candidate(s = "vowelvowelvowelvowelvowel",k = 10) == 0
    assert candidate(s = "aaaaaaaaaaabbbbbbbbbb",k = 1) == 10
    assert candidate(s = "abacabadabacaba",k = 2) == 24
    assert candidate(s = "aaaabbbbcccc",k = 10) == 0
    assert candidate(s = "eiouaeiouaeiouaeiou",k = 5) == 0
    assert candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 5) == 1
    assert candidate(s = "thisisaverylongstringwithvariouscharacters",k = 11) == 0
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 3) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz",k = 30) == 0
    assert candidate(s = "aeiaeiouaeiaeiouaeiaeiou",k = 18) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz",k = 50) == 0
    assert candidate(s = "consonantconsonantconsonant",k = 15) == 0
    assert candidate(s = "bcbcbcbcbcbcbc",k = 3) == 0
    assert candidate(s = "vowelsconsonants",k = 4) == 5
    assert candidate(s = "aebcdeioufhgjk",k = 12) == 1
    assert candidate(s = "xylophone",k = 2) == 2
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 25) == 0
    assert candidate(s = "xyzabcxyzabc",k = 9) == 0
    assert candidate(s = "thisisateststring",k = 7) == 0
    assert candidate(s = "aaaaaaaaaabbbbbbbbbb",k = 100) == 1
    assert candidate(s = "vowelsandconsonants",k = 18) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyz",k = 26) == 0
    assert candidate(s = "aabbbbcccc",k = 4) == 1
    assert candidate(s = "beautifulsubstring",k = 5) == 2
    assert candidate(s = "xyzxyzxyzxyz",k = 9) == 0
    assert candidate(s = "abecidofug",k = 8) == 3
    assert candidate(s = "xyzxyzxyzxyz",k = 3) == 0
    assert candidate(s = "aaaabbbbccccdddd",k = 8) == 1
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewwq",k = 11) == 0
    assert candidate(s = "aeiouaeiouaeiouaeiou",k = 25) == 0
    assert candidate(s = "aaaaaaaaaeeeeeeiiioooouuuu",k = 10) == 0
    assert candidate(s = "consonantsconsonantsconsonants",k = 9) == 3


