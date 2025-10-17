def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "e") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "e") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiou") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiou") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiuiauuuuaeioaaaaeaiaioieoieiieoioioieouieiiaiaeiieoieouuiooaoaaiiaeiieeiooieiei") == 209934
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiuiauuuuaeioaaaaeaiaioieoieiieoioioieouieiiaiaeiieoieouuiooaoaaiiaeiieeiooieiei") == 209934: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcbcbcbcbc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcbcbcbcbc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 4960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 4960: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiuiaoiuuaeiuuaieiiaaaeeiuuoiuuuuuuu") == 43680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiuiaoiuuaeiuuaieiiaaaeeiuuoiuuuuuuu") == 43680: {e}')
    
    total += 1
    try:
        result = candidate(word = "ltcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ltcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "u") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "u") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 604: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "o") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "o") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "i") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "i") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbaaeekkeeaabbaaeekkeeaabbaaeekkeeaabb") == 6576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbaaeekkeeaabbaaeekkeeaabbaaeekkeeaabb") == 6576: {e}')
    
    total += 1
    try:
        result = candidate(word = "uvijqet") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uvijqet") == 34: {e}')
    
    total += 1
    try:
        result = candidate(word = "aieouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 16215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aieouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 16215: {e}')
    
    total += 1
    try:
        result = candidate(word = "uuygqijetbvrcw") == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uuygqijetbvrcw") == 150: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi") == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi") == 98: {e}')
    
    total += 1
    try:
        result = candidate(word = "vowels") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vowels") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiou") == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiou") == 680: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghij") == 3412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghij") == 3412: {e}')
    
    total += 1
    try:
        result = candidate(word = "cccccdcccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cccccdcccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aovnwqoeirqoweoirqoweoirquw") == 1949
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aovnwqoeirqoweoirqoweoirquw") == 1949: {e}')
    
    total += 1
    try:
        result = candidate(word = "congratulations") == 299
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "congratulations") == 299: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzaeiouxyzaeiouxyz") == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzaeiouxyzaeiouxyz") == 820: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcbcbcbcbcbcbcbcbcbc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcbcbcbcbcbcbcbcbcbc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "vvvuuuooooiiiaaaaeeeee") == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vvvuuuooooiiiaaaaeeeee") == 1900: {e}')
    
    total += 1
    try:
        result = candidate(word = "consonants") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "consonants") == 76: {e}')
    
    total += 1
    try:
        result = candidate(word = "vowelvowelvowel") == 278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vowelvowelvowel") == 278: {e}')
    
    total += 1
    try:
        result = candidate(word = "supercalifragilisticexpialidocious") == 3282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "supercalifragilisticexpialidocious") == 3282: {e}')
    
    total += 1
    try:
        result = candidate(word = "aquickbrownfoxjumpsoverthelazydog") == 2016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aquickbrownfoxjumpsoverthelazydog") == 2016: {e}')
    
    total += 1
    try:
        result = candidate(word = "leetcode") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "leetcode") == 58: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 3860
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 3860: {e}')
    
    total += 1
    try:
        result = candidate(word = "sequence") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sequence") == 62: {e}')
    
    total += 1
    try:
        result = candidate(word = "aovvoaoaueuioeaueoaiouaoieaouioeaouioiea") == 11218
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aovvoaoaueuioeaueoaiouaoieaouioeaouioiea") == 11218: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeeee") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeeee") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioouaeiou") == 286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioouaeiou") == 286: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbbbbbbbbbbbbbbbbbbbbba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbbbbbbbbbbbbbbbbbbbbba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "hello") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hello") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "uoiea") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uoiea") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdfghjklmnpqrstvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdfghjklmnpqrstvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ffaaabbbccc") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ffaaabbbccc") == 94: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 2925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 2925: {e}')
    
    total += 1
    try:
        result = candidate(word = "qweoiauoieqweoiauoieqweoiauoie") == 4016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qweoiauoieqweoiauoieqweoiauoie") == 4016: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 4562
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 4562: {e}')
    
    total += 1
    try:
        result = candidate(word = "rhythms") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rhythms") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbbbebbbb") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbbbebbbb") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeeffgg") == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeeffgg") == 221: {e}')
    
    total += 1
    try:
        result = candidate(word = "beautiful") == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "beautiful") == 101: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiou") == 4960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiou") == 4960: {e}')
    
    total += 1
    try:
        result = candidate(word = "dddddeoeddd") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dddddeoeddd") == 103: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiou") == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiou") == 1540: {e}')
    
    total += 1
    try:
        result = candidate(word = "vowel") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vowel") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "xylophone") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xylophone") == 54: {e}')
    
    total += 1
    try:
        result = candidate(word = "repetitiveeeee") == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repetitiveeeee") == 350: {e}')
    
    total += 1
    try:
        result = candidate(word = "repetition") == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repetition") == 118: {e}')
    
    total += 1
    try:
        result = candidate(word = "characters") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "characters") == 78: {e}')
    
    total += 1
    try:
        result = candidate(word = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 13244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 13244: {e}')
    
    total += 1
    try:
        result = candidate(word = "uvaeiouz") == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uvaeiouz") == 98: {e}')
    
    total += 1
    try:
        result = candidate(word = "aovylqjwhepfuciphg") == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aovylqjwhepfuciphg") == 280: {e}')
    
    total += 1
    try:
        result = candidate(word = "uoieaoueioauoiea") == 816
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uoieaoueioauoiea") == 816: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "eeeeeaeeee") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eeeeeaeeee") == 220: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabaaaaa") == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabaaaaa") == 250: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacaxabayabac") == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacaxabayabac") == 280: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiou") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiou") == 220: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "programming") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "programming") == 90: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaoeiaoeiaoeiaoeiaoeiaoeiaoeiaoeiaoei") == 10660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaoeiaoeiaoeiaoeiaoeiaoeiaoeiaoeiaoei") == 10660: {e}')
    
    total += 1
    try:
        result = candidate(word = "ouqofyrcjgz") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ouqofyrcjgz") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaeaieaa") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaeaieaa") == 220: {e}')
    
    total += 1
    try:
        result = candidate(word = "vowelsarefun") == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vowelsarefun") == 158: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 4718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 4718: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "e") == 1
    assert candidate(word = "aeiou") == 35
    assert candidate(word = "abc") == 3
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiuiauuuuaeioaaaaeaiaioieoieiieoioioieouieiiaiaeiieoieouuiooaoaaiiaeiieeiooieiei") == 209934
    assert candidate(word = "bcbcbcbcbc") == 0
    assert candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 4960
    assert candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiuiaoiuuaeiuuaieiiaaaeeiuuoiuuuuuuu") == 43680
    assert candidate(word = "ltcd") == 0
    assert candidate(word = "aba") == 6
    assert candidate(word = "u") == 1
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 604
    assert candidate(word = "a") == 1
    assert candidate(word = "o") == 1
    assert candidate(word = "b") == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(word = "i") == 1
    assert candidate(word = "") == 0
    assert candidate(word = "bbaaeekkeeaabbaaeekkeeaabbaaeekkeeaabb") == 6576
    assert candidate(word = "uvijqet") == 34
    assert candidate(word = "aieouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 16215
    assert candidate(word = "uuygqijetbvrcw") == 150
    assert candidate(word = "mississippi") == 98
    assert candidate(word = "vowels") == 22
    assert candidate(word = "aeiouaeiouaeiou") == 680
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghij") == 3412
    assert candidate(word = "cccccdcccc") == 0
    assert candidate(word = "aovnwqoeirqoweoirqoweoirquw") == 1949
    assert candidate(word = "congratulations") == 299
    assert candidate(word = "xyzaeiouxyzaeiouxyz") == 820
    assert candidate(word = "bcbcbcbcbcbcbcbcbcbc") == 0
    assert candidate(word = "vvvuuuooooiiiaaaaeeeee") == 1900
    assert candidate(word = "consonants") == 76
    assert candidate(word = "vowelvowelvowel") == 278
    assert candidate(word = "supercalifragilisticexpialidocious") == 3282
    assert candidate(word = "aquickbrownfoxjumpsoverthelazydog") == 2016
    assert candidate(word = "leetcode") == 58
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 3860
    assert candidate(word = "sequence") == 62
    assert candidate(word = "aovvoaoaueuioeaueoaiouaoieaouioeaouioiea") == 11218
    assert candidate(word = "aeeee") == 35
    assert candidate(word = "aeioouaeiou") == 286
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(word = "bbbbbbbbbbbbbbbbbbbbbbba") == 24
    assert candidate(word = "hello") == 13
    assert candidate(word = "uoiea") == 35
    assert candidate(word = "bcdfghjklmnpqrstvwxyz") == 0
    assert candidate(word = "ffaaabbbccc") == 94
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 2925
    assert candidate(word = "qweoiauoieqweoiauoieqweoiauoie") == 4016
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 4562
    assert candidate(word = "rhythms") == 0
    assert candidate(word = "bbbbbebbbb") == 30
    assert candidate(word = "aabbccddeeeffgg") == 221
    assert candidate(word = "beautiful") == 101
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiou") == 4960
    assert candidate(word = "dddddeoeddd") == 103
    assert candidate(word = "aeiouaeiouaeiouaeiou") == 1540
    assert candidate(word = "vowel") == 16
    assert candidate(word = "xylophone") == 54
    assert candidate(word = "repetitiveeeee") == 350
    assert candidate(word = "repetition") == 118
    assert candidate(word = "characters") == 78
    assert candidate(word = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 13244
    assert candidate(word = "uvaeiouz") == 98
    assert candidate(word = "aovylqjwhepfuciphg") == 280
    assert candidate(word = "uoieaoueioauoiea") == 816
    assert candidate(word = "zzzzzzzzzzz") == 0
    assert candidate(word = "eeeeeaeeee") == 220
    assert candidate(word = "aaaaabaaaaa") == 250
    assert candidate(word = "abacaxabayabac") == 280
    assert candidate(word = "aeiouaeiou") == 220
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(word = "programming") == 90
    assert candidate(word = "aeiaoeiaoeiaoeiaoeiaoeiaoeiaoeiaoeiaoei") == 10660
    assert candidate(word = "ouqofyrcjgz") == 63
    assert candidate(word = "aeiaeaieaa") == 220
    assert candidate(word = "vowelsarefun") == 158
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 4718


