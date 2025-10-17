def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "bcbcbc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbacdcdcdbacdbad") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbacdcdcdbacdbad") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiou") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiou") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaeeeeeiioooouuuu") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaeeeeeiioooouuuu") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuu") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuu") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaeeiioouu") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaeeiioouu") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiou") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiou") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisgreat") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisgreat") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiaaioaaaaeiiiiouuuooaaaaea") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaaioaaaaeiiiiouuuooaaaaea") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeeeeeiiiiioooouuuu") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeeeeeiiiiioooouuuu") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiijkeilmnopqrstuvwxyzaeiou") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiijkeilmnopqrstuvwxyzaeiou") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbeeaabbeeaabb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbeeaabbeeaabb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiouaeiouaeiou") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiouaeiouaeiou") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "eleetminicoworoep") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eleetminicoworoep") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaeixaaaaooxu") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaeixaaaaooxu") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aioieu") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aioieu") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcdfghjklmnpqrstvwxyz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcdfghjklmnpqrstvwxyz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiaaioaaaaeiiiiiioooeeeauuaeuia") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaaioaaaaeiiiiiioooeeeauuaeuia") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeleetcode") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeleetcode") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmlkjhgfdsapoiuytrewq") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmlkjhgfdsapoiuytrewq") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiouxyzuvwaeiouaeiouaeiou") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiouxyzuvwaeiouaeiouaeiou") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "eeioouuuaeeioouuua") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eeioouuuaeeioouuua") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiou") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiou") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxebecixodeoxou") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxebecixodeoxou") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithvariousvowels") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithvariousvowels") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "uoieaouioeaoieauoi") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uoieaouioeaoieauoi") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamad") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamad") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeleetcodeleetcode") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeleetcodeleetcode") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaccddeeffgg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaccddeeffgg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiouaeiouaieouaeiouaeiouaeiou") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiouaeiouaieouaeiouaeiouaeiou") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzuvwaeiouaeiouxyzuvwaeiouaeiouxyzuvwaeiouaeiou") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzuvwaeiouaeiouxyzuvwaeiouaeiouxyzuvwaeiouaeiou") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouabcdeffedcbaaeiouaeiou") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouabcdeffedcbaaeiouaeiou") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdeiouaeiouabcdeiouaeiouxyz") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdeiouaeiouabcdeiouaeiouxyz") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbaeibcbcbcbaeibcbcbc") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbaeibcbcbcbaeibcbcbc") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeeeeiiiooouuuuuuuuu") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeeeeiiiooouuuuuuuuu") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcabcabcabcabcabcabc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcabcabcabcabcabcabc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxebecixodeoxouabacaxebecixodeoxou") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxebecixodeoxouabacaxebecixodeoxou") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzaeizzzaeiouzzzaeiouzzz") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzaeizzzaeiouzzzaeiouzzz") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouabcdefghijklmnopqrstuvwxyzaeiou") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouabcdefghijklmnopqrstuvwxyzaeiou") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "uvceeaieeaaceeaiaa") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uvceeaieeaaceeaiaa") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebecixodeoxouaebecixodeoxou") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebecixodeoxouaebecixodeoxou") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "vvvvvvvvvvvvvvvvvv") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vvvvvvvvvvvvvvvvvv") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aebecidofugoeiaoeiu") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aebecidofugoeiaoeiu") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouabcdeffedcbaaeiouaeiou") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouabcdeffedcbaaeiouaeiou") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzaeiouaeiouaeiou") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzaeiouaeiouaeiou") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisgreataeiou") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisgreataeiou") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouxyzuvw") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouxyzuvw") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcbabcdeffedcbabcdeffedcbabcdeffedcb") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcbabcdeffedcbabcdeffedcbabcdeffedcb") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzuvwaeiouxyzuvwaeiou") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzuvwaeiouxyzuvwaeiou") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmaeiouaeiou") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmaeiouaeiou") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "vwxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vwxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "eleetminicoworoepzzzzzzzzzz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eleetminicoworoepzzzzzzzzzz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abecidofug") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abecidofug") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiouaieouaieoua") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiouaieouaieoua") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiaoeiuioeiuaeiaoeiuioeiuaeiaoeiuioeiaoeiu") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiaoeiuioeiuaeiaoeiuioeiuaeiaoeiuioeiaoeiu") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "eiouaeiouaeiouaeiouaeiouaeiou") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eiouaeiouaeiouaeiouaeiouaeiou") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "eleetminicoworoepaeiou") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eleetminicoworoepaeiou") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "eeioouuuaeeioouuuaeeioouuuaeeioouuua") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eeioouuuaeeioouuuaeeioouuuaeeioouuua") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisgreatleetcodeisgreatleetcodeisgreat") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisgreatleetcodeisgreatleetcodeisgreat") == 35: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "bcbcbc") == 6
    assert candidate(s = "cbacdcdcdbacdbad") == 14
    assert candidate(s = "aeiouaeiouaeiouaeiou") == 20
    assert candidate(s = "aaaaaeeeeeiioooouuuu") == 14
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 5
    assert candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuu") == 26
    assert candidate(s = "aaeeiioouu") == 10
    assert candidate(s = "aeiou") == 0
    assert candidate(s = "aaaaa") == 4
    assert candidate(s = "a") == 0
    assert candidate(s = "leetcodeisgreat") == 5
    assert candidate(s = "abacabadabacaba") == 15
    assert candidate(s = "aeiaaioaaaaeiiiiouuuooaaaaea") == 18
    assert candidate(s = "") == 0
    assert candidate(s = "aeeeeeiiiiioooouuuu") == 12
    assert candidate(s = "xyz") == 3
    assert candidate(s = "abcdefghiijkeilmnopqrstuvwxyzaeiou") == 12
    assert candidate(s = "aabbeeaabbeeaabb") == 16
    assert candidate(s = "eiouaeiouaeiou") == 10
    assert candidate(s = "eleetminicoworoep") == 13
    assert candidate(s = "bbaeixaaaaooxu") == 8
    assert candidate(s = "aioieu") == 0
    assert candidate(s = "bcdfghjklmnpqrstvwxyz") == 21
    assert candidate(s = "aeiaaioaaaaeiiiiiioooeeeauuaeuia") == 28
    assert candidate(s = "aabbccddeeff") == 12
    assert candidate(s = "leetcodeleetcode") == 16
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
    assert candidate(s = "zxcvbnmlkjhgfdsapoiuytrewq") == 15
    assert candidate(s = "aaaaaaaa") == 8
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiouxyzuvwaeiouaeiouaeiou") == 45
    assert candidate(s = "eeioouuuaeeioouuua") == 18
    assert candidate(s = "aeiouaeiouaeiou") == 10
    assert candidate(s = "abacaxebecixodeoxou") == 9
    assert candidate(s = "thisisaverylongstringwithvariousvowels") == 13
    assert candidate(s = "eiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 40
    assert candidate(s = "uoieaouioeaoieauoi") == 12
    assert candidate(s = "mamad") == 5
    assert candidate(s = "leetcodeleetcodeleetcode") == 21
    assert candidate(s = "bbaaccddeeffgg") == 14
    assert candidate(s = "eiouaeiouaieouaeiouaeiouaeiou") == 20
    assert candidate(s = "xyzuvwaeiouaeiouxyzuvwaeiouaeiouxyzuvwaeiouaeiou") == 47
    assert candidate(s = "abcdeabcdeabcde") == 13
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouabcdeffedcbaaeiouaeiou") == 52
    assert candidate(s = "xyzabcdeiouaeiouabcdeiouaeiouxyz") == 32
    assert candidate(s = "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 50
    assert candidate(s = "bcbcbcbaeibcbcbcbaeibcbcbc") == 26
    assert candidate(s = "aeeeeiiiooouuuuuuuuu") == 10
    assert candidate(s = "bcbcbcabcabcabcabcabcabc") == 24
    assert candidate(s = "abacaxebecixodeoxouabacaxebecixodeoxou") == 38
    assert candidate(s = "zzzaeizzzaeiouzzzaeiouzzz") == 19
    assert candidate(s = "aeiouabcdefghijklmnopqrstuvwxyzaeiou") == 31
    assert candidate(s = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 52
    assert candidate(s = "uvceeaieeaaceeaiaa") == 17
    assert candidate(s = "aebecixodeoxouaebecixodeoxou") == 28
    assert candidate(s = "vvvvvvvvvvvvvvvvvv") == 18
    assert candidate(s = "aebecidofugoeiaoeiu") == 4
    assert candidate(s = "aeiouaeiouabcdeffedcbaaeiouaeiou") == 32
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzaeiouaeiouaeiou") == 41
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(s = "leetcodeisgreataeiou") == 17
    assert candidate(s = "aeiouaeiouaeiouxyzuvw") == 17
    assert candidate(s = "abcdeffedcbabcdeffedcbabcdeffedcbabcdeffedcb") == 44
    assert candidate(s = "xyzuvwaeiouxyzuvwaeiou") == 22
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmaeiouaeiou") == 31
    assert candidate(s = "vwxyz") == 5
    assert candidate(s = "aabbccddeeffgg") == 14
    assert candidate(s = "eleetminicoworoepzzzzzzzzzz") == 13
    assert candidate(s = "abecidofug") == 1
    assert candidate(s = "eiouaieouaieoua") == 10
    assert candidate(s = "aeiaoeiuioeiuaeiaoeiuioeiuaeiaoeiuioeiaoeiu") == 26
    assert candidate(s = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 50
    assert candidate(s = "eiouaeiouaeiouaeiouaeiouaeiou") == 20
    assert candidate(s = "eleetminicoworoepaeiou") == 13
    assert candidate(s = "eeioouuuaeeioouuuaeeioouuuaeeioouuua") == 36
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 50
    assert candidate(s = "aabbccddeeffaabbccddeeff") == 24
    assert candidate(s = "leetcodeisgreatleetcodeisgreatleetcodeisgreat") == 35


