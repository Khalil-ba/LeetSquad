def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aooiiieeec",k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aooiiieeec",k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "happy",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "happy",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "rhythms",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rhythms",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "fluffy",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fluffy",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiou",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiou",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "beautiful",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "beautiful",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "rhythms",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rhythms",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbb",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbb",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abciiidef",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abciiidef",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "quartz",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quartz",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuu",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuu",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiuaooeiuaooeiuaooeiuaoo",k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiuaooeiuaooeiuaooeiuaoo",k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyz",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyz",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "understanding",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "understanding",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",k = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",k = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiou",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiou",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbaaaaa",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbaaaaa",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaeixixixixxxeiiixieeiix",k = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaeixixixixxxeiiixieeiix",k = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "uoieaouieaouieaouieaouieaouieao",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uoieaouieaouieaouieaouieaouieao",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiou",k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiou",k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "iouaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "iouaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 12) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 12) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzvowelsabcdefg",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzvowelsabcdefg",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisawesome",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisawesome",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "lovelaceeinstein",k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lovelaceeinstein",k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 13) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 13) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithsomevowelsinside",k = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithsomevowelsinside",k = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbbbbbbbcccccccc",k = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbbbbbbbcccccccc",k = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaeiooacaioiiceiue",k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaeiooacaioiiceiue",k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiou",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiou",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzz",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzz",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "uvvwxyz",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uvvwxyz",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "uoieaouieaouieaouieaouieaouiea",k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uoieaouieaouieaouieaouieaouiea",k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnoabcdeioufghijkl",k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnoabcdeioufghijkl",k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisaverygoodplatform",k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisaverygoodplatform",k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",k = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",k = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdafg",k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdafg",k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaa",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaa",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithseveralvowelsinside",k = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithseveralvowelsinside",k = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioiei",k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioiei",k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "uoieaouioeaouioeaouioe",k = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uoieaouioeaouioeaouioe",k = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiou",k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiou",k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbc",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbc",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "uqeiouqeiouqeiouqeiouqeiouqe",k = 11) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uqeiouqeiouqeiouqeiouqeiouqe",k = 11) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqwwweee",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqwwweee",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaeixoubb",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaeixoubb",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeiioooooooouuuuuuuuuuuaaaaaaaa",k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeiioooooooouuuuuuuuuuuaaaaaaaa",k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "bvflkqmbvkjgnqmfqlqjflvngqnvfkvnqjvfbvmqjbfvmlkjbfnvqjgbfnvqjbngfjkqnvbmfkqjbgfnjkbv",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bvflkqmbvkjgnqmfqlqjflvngqnvfkvnqjvfbvmqjbfvmlkjbfnvqjgbfnvqjbngfjkqnvbmfkqjbgfnjkbv",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelsarebeautiful",k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelsarebeautiful",k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbaaaaaa",k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbaaaaaa",k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiaaioaaaaeiiiiiiooooaauuaeiu",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaaioaaaaeiiiiiiooooaauuaeiu",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithlotsofvowelsandconsonants",k = 18) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithlotsofvowelsandconsonants",k = 18) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "environmentally",k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "environmentally",k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisacommunityforcoders",k = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisacommunityforcoders",k = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisfun",k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisfun",k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisawesome",k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisawesome",k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiii",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiii",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "uoieaooooieau",k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uoieaooooieau",k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abecidofugihanukleomnonuopqrstuvwxyz",k = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abecidofugihanukleomnonuopqrstuvwxyz",k = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiaaioaaaaeiiiiouuuu",k = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaaioaaaaeiiiiouuuu",k = 12) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aooiiieeec",k = 6) == 6
    assert candidate(s = "a",k = 1) == 1
    assert candidate(s = "happy",k = 2) == 1
    assert candidate(s = "rhythms",k = 5) == 0
    assert candidate(s = "fluffy",k = 2) == 1
    assert candidate(s = "leetcode",k = 3) == 2
    assert candidate(s = "aeiou",k = 2) == 2
    assert candidate(s = "beautiful",k = 4) == 3
    assert candidate(s = "rhythms",k = 4) == 0
    assert candidate(s = "bbbb",k = 2) == 0
    assert candidate(s = "aaaaaa",k = 5) == 5
    assert candidate(s = "abciiidef",k = 3) == 3
    assert candidate(s = "aabbccddeeff",k = 4) == 2
    assert candidate(s = "quartz",k = 3) == 2
    assert candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuu",k = 5) == 5
    assert candidate(s = "eiuaooeiuaooeiuaooeiuaoo",k = 8) == 8
    assert candidate(s = "bcdfghjklmnpqrstvwxyz",k = 3) == 0
    assert candidate(s = "understanding",k = 4) == 2
    assert candidate(s = "abacabadabacaba",k = 5) == 3
    assert candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",k = 100) == 50
    assert candidate(s = "aeiouaeiou",k = 1) == 1
    assert candidate(s = "bbbbbbaaaaa",k = 5) == 5
    assert candidate(s = "bbaeixixixixxxeiiixieeiix",k = 15) == 10
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 0
    assert candidate(s = "uoieaouieaouieaouieaouieaouieao",k = 15) == 15
    assert candidate(s = "mississippi",k = 4) == 2
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiou",k = 20) == 20
    assert candidate(s = "iouaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 50) == 50
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 12) == 4
    assert candidate(s = "xyzvowelsabcdefg",k = 5) == 2
    assert candidate(s = "leetcodeisawesome",k = 5) == 3
    assert candidate(s = "lovelaceeinstein",k = 7) == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 13) == 3
    assert candidate(s = "thisisaverylongstringwithsomevowelsinside",k = 20) == 8
    assert candidate(s = "aaaaaaaabbbbbbbbcccccccc",k = 12) == 8
    assert candidate(s = "bbaeiooacaioiiceiue",k = 11) == 10
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",k = 20) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 6
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiou",k = 10) == 10
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzz",k = 20) == 0
    assert candidate(s = "uvvwxyz",k = 3) == 1
    assert candidate(s = "abcdeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 15) == 15
    assert candidate(s = "uoieaouieaouieaouieaouieaouiea",k = 7) == 7
    assert candidate(s = "mnoabcdeioufghijkl",k = 7) == 4
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 15) == 4
    assert candidate(s = "leetcodeisaverygoodplatform",k = 10) == 6
    assert candidate(s = "ababababab",k = 5) == 3
    assert candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",k = 30) == 30
    assert candidate(s = "bcdafg",k = 6) == 1
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaa",k = 10) == 10
    assert candidate(s = "bcdfghjklmnpqrstvwxyz",k = 1) == 0
    assert candidate(s = "thisisaverylongstringwithseveralvowelsinside",k = 15) == 6
    assert candidate(s = "aiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioieiaioiei",k = 20) == 20
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",k = 15) == 15
    assert candidate(s = "uoieaouioeaouioeaouioe",k = 12) == 12
    assert candidate(s = "aeiouaeiouaeiouaeiou",k = 7) == 7
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbc",k = 7) == 0
    assert candidate(s = "uqeiouqeiouqeiouqeiouqeiouqe",k = 11) == 9
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 3
    assert candidate(s = "qqqwwweee",k = 4) == 3
    assert candidate(s = "bbaeixoubb",k = 5) == 4
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == 5
    assert candidate(s = "aeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeiioooooooouuuuuuuuuuuaaaaaaaa",k = 25) == 25
    assert candidate(s = "bvflkqmbvkjgnqmfqlqjflvngqnvfkvnqjvfbvmqjbfvmlkjbfnvqjgbfnvqjbngfjkqnvbmfkqjbgfnjkbv",k = 10) == 0
    assert candidate(s = "vowelsarebeautiful",k = 10) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 15) == 0
    assert candidate(s = "bcbcbcbcbcbaaaaaa",k = 10) == 6
    assert candidate(s = "aeiaaioaaaaeiiiiiiooooaauuaeiu",k = 15) == 15
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz",k = 8) == 0
    assert candidate(s = "thisisaverylongstringwithlotsofvowelsandconsonants",k = 18) == 7
    assert candidate(s = "environmentally",k = 10) == 4
    assert candidate(s = "leetcodeisacommunityforcoders",k = 8) == 5
    assert candidate(s = "leetcodeisfun",k = 7) == 4
    assert candidate(s = "leetcodeisawesome",k = 7) == 4
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 10) == 0
    assert candidate(s = "aaabbbcccdddeeefffggghhhiii",k = 5) == 3
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbc",k = 3) == 0
    assert candidate(s = "uoieaooooieau",k = 7) == 7
    assert candidate(s = "abecidofugihanukleomnonuopqrstuvwxyz",k = 20) == 10
    assert candidate(s = "aeiaaioaaaaeiiiiouuuu",k = 12) == 12


