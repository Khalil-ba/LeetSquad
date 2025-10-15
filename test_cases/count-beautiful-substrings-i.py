def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aeaeaeae",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeaeaeae",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyz",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyz",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebcdfe",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcdfe",k = 3) == 0: {e}')
    
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
        result = candidate(s = "aebcdeedaa",k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcdeedaa",k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdf",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdf",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 1) == 1: {e}')
    
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
        result = candidate(s = "bcdfgh",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfgh",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",k = 2) == 1: {e}')
    
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
        result = candidate(s = "aabb",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiou",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiou",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "b",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "b",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiou",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiou",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaeeiioouuccddffgg",k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaeeiioouuccddffgg",k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiou",k = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiou",k = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfgh",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfgh",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfghjklmnpqrstvwxyzaeioubcdfghjklmnpqrstvwxyz",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfghjklmnpqrstvwxyzaeioubcdfghjklmnpqrstvwxyz",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsandconsonantsareimportant",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsandconsonantsareimportant",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebcdfeab",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcdfeab",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdefghijklmnopqrstuvwxyz",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdefghijklmnopqrstuvwxyz",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsconsonantsvowelsconsonants",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsconsonantsvowelsconsonants",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == 0: {e}')
    
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
        result = candidate(s = "aabbccddeeffgg",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebcdefghijklmnopqrstuvwxyz",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebcdefghijklmnopqrstuvwxyz",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbbbbbbcccccccccc",k = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbbbbbbcccccccccc",k = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbaaaaeiiuuuccccc",k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbaaaaeiiuuuccccc",k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmixedcharacters",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmixedcharacters",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulstring",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulstring",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "consonantsandvowelsareequal",k = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consonantsandvowelsareequal",k = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzaaaaabbbbcccc",k = 16) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzaaaaabbbbcccc",k = 16) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfg",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfg",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfg",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfg",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiou",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiou",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiou",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiou",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaeebbeeaabbaa",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaeebbeeaabbaa",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 49) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 49) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaeeiioouubbbccddffgg",k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaeeiioouubbbccddffgg",k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsandconsonants",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsandconsonants",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophoneaeiouaeiou",k = 12) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophoneaeiouaeiou",k = 12) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "exampleexampleexample",k = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "exampleexampleexample",k = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophoneisfun",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophoneisfun",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulstringwithvowelsandconsonants",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulstringwithvowelsandconsonants",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiou",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiou",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouzzzzzzzzzz",k = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouzzzzzzzzzz",k = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaeeddbb",k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaeeddbb",k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "eeeeeeeeeeaaaaaaaaaaiiiiiiiiiiooooooooouuuuuuuuuu",k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eeeeeeeeeeaaaaaaaaaaiiiiiiiiiiooooooooouuuuuuuuuu",k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyyxxxx",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyyxxxx",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithvowelsandconsonants",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithvowelsandconsonants",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisbeautifulstringwithvariousvowelsandconsonants",k = 8) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisbeautifulstringwithvariousvowelsandconsonants",k = 8) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeioubcdfghjklmnpqrstvwxy",k = 11) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeioubcdfghjklmnpqrstvwxy",k = 11) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautifulstringwithvowelandconsonants",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautifulstringwithvowelandconsonants",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "consonantsconsonantsconsonants",k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consonantsconsonantsconsonants",k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamamamamamamamama",k = 2) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamamamamamamamama",k = 2) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmanyvowelsandconsonants",k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmanyvowelsandconsonants",k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsarebeautiful",k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsarebeautiful",k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyzaeiou",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyzaeiou",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeaeaeaeaeaeaeaeaeae",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeaeaeaeaeaeaeaeaeae",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiou",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiou",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaeeeiioouu",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaeeeiioouu",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxybcdfghjklmnpqrstvwxy",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxybcdfghjklmnpqrstvwxy",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 50) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aeaeaeae",k = 8) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyz",k = 2) == 0
    assert candidate(s = "aebcdfe",k = 3) == 0
    assert candidate(s = "",k = 1) == 0
    assert candidate(s = "baeyh",k = 2) == 2
    assert candidate(s = "aebcdeedaa",k = 4) == 6
    assert candidate(s = "bcdf",k = 1) == 0
    assert candidate(s = "abcd",k = 1) == 1
    assert candidate(s = "",k = 3) == 0
    assert candidate(s = "abba",k = 1) == 3
    assert candidate(s = "bcdfgh",k = 2) == 0
    assert candidate(s = "aabbccdd",k = 2) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2) == 0
    assert candidate(s = "a",k = 1) == 0
    assert candidate(s = "aabb",k = 2) == 1
    assert candidate(s = "aeiou",k = 5) == 0
    assert candidate(s = "abcdefgh",k = 4) == 0
    assert candidate(s = "b",k = 1) == 0
    assert candidate(s = "aabbccddeeff",k = 4) == 4
    assert candidate(s = "aeiouaeiouaeiouaeiou",k = 25) == 0
    assert candidate(s = "aabbaaeeiioouuccddffgg",k = 10) == 1
    assert candidate(s = "aeiouaeiouaeiouaeiou",k = 200) == 0
    assert candidate(s = "aeioubcdfgh",k = 5) == 1
    assert candidate(s = "aeioubcdfghjklmnpqrstvwxyzaeioubcdfghjklmnpqrstvwxyz",k = 12) == 0
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 7) == 0
    assert candidate(s = "vowelsandconsonantsareimportant",k = 12) == 0
    assert candidate(s = "abacabadabacaba",k = 3) == 14
    assert candidate(s = "aebcdfeab",k = 2) == 4
    assert candidate(s = "aeioubcdefghijklmnopqrstuvwxyz",k = 10) == 0
    assert candidate(s = "vowelsconsonantsvowelsconsonants",k = 8) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == 0
    assert candidate(s = "vowelsandconsonants",k = 6) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 100) == 0
    assert candidate(s = "aabbccddeeffgg",k = 12) == 0
    assert candidate(s = "aebcdefghijklmnopqrstuvwxyz",k = 7) == 0
    assert candidate(s = "aaaaaaaaaaaabbbbbbbbbbcccccccccc",k = 25) == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 7) == 0
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0
    assert candidate(s = "bbbbbbaaaaeiiuuuccccc",k = 15) == 0
    assert candidate(s = "thisisaverylongstringwithmixedcharacters",k = 7) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 12) == 0
    assert candidate(s = "beautifulstring",k = 3) == 2
    assert candidate(s = "abcdefghijabcdefghij",k = 20) == 0
    assert candidate(s = "consonantsandvowelsareequal",k = 14) == 0
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 2) == 0
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 25) == 0
    assert candidate(s = "zzzzzaaaaabbbbcccc",k = 16) == 2
    assert candidate(s = "aeioubcdfg",k = 5) == 1
    assert candidate(s = "bcdfg",k = 1) == 0
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 100) == 0
    assert candidate(s = "aeiouaeiou",k = 5) == 0
    assert candidate(s = "aeiou",k = 1) == 0
    assert candidate(s = "aabbaaeebbeeaabbaa",k = 3) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 49) == 0
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 3) == 0
    assert candidate(s = "aaeeiioouubbbccddffgg",k = 10) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 9) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 6) == 0
    assert candidate(s = "vowelsandconsonants",k = 10) == 0
    assert candidate(s = "xylophoneaeiouaeiou",k = 12) == 1
    assert candidate(s = "exampleexampleexample",k = 9) == 10
    assert candidate(s = "aabbccddeeff",k = 6) == 0
    assert candidate(s = "xylophoneisfun",k = 7) == 0
    assert candidate(s = "beautifulstringwithvowelsandconsonants",k = 20) == 0
    assert candidate(s = "aeiouaeiou",k = 25) == 0
    assert candidate(s = "aeiouzzzzzzzzzz",k = 200) == 0
    assert candidate(s = "aeioubcdfghjklmnpqrstvwxyz",k = 5) == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 21) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 0
    assert candidate(s = "bbaaeeddbb",k = 4) == 5
    assert candidate(s = "eeeeeeeeeeaaaaaaaaaaiiiiiiiiiiooooooooouuuuuuuuuu",k = 100) == 0
    assert candidate(s = "zzzzyyyyxxxx",k = 9) == 0
    assert candidate(s = "thisisaverylongstringwithvowelsandconsonants",k = 20) == 0
    assert candidate(s = "thisisbeautifulstringwithvariousvowelsandconsonants",k = 8) == 10
    assert candidate(s = "aeiouaeiouaeiouaeioubcdfghjklmnpqrstvwxy",k = 11) == 1
    assert candidate(s = "beautifulstringwithvowelandconsonants",k = 7) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 5) == 0
    assert candidate(s = "consonantsconsonantsconsonants",k = 30) == 0
    assert candidate(s = "mamamamamamamamama",k = 2) == 36
    assert candidate(s = "thisisaverylongstringwithmanyvowelsandconsonants",k = 12) == 0
    assert candidate(s = "vowelsarebeautiful",k = 6) == 3
    assert candidate(s = "bcdfghjklmnpqrstvwxyzaeiou",k = 10) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 8) == 0
    assert candidate(s = "aeaeaeaeaeaeaeaeaeae",k = 2) == 0
    assert candidate(s = "aeiouaeiouaeiouaeiou",k = 4) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 15) == 0
    assert candidate(s = "aaaeeeiioouu",k = 1) == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxybcdfghjklmnpqrstvwxy",k = 9) == 0
    assert candidate(s = "zzzzzzzzzz",k = 100) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 50) == 0


