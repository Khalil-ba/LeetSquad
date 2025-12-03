def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0

    total += 1
    try:
        result = candidate(s = "abba") == "abba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == "abba": {e}')

    total += 1
    try:
        result = candidate(s = "aaaa") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == "aaaa": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == "aba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == "aba": {e}')

    total += 1
    try:
        result = candidate(s = "ac") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ac") == "a": {e}')

    total += 1
    try:
        result = candidate(s = "babad") == "aba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babad") == "aba": {e}')

    total += 1
    try:
        result = candidate(s = "noon") == "noon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == "noon": {e}')

    total += 1
    try:
        result = candidate(s = "cbbd") == "bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbbd") == "bb": {e}')

    total += 1
    try:
        result = candidate(s = "abcba") == "abcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == "abcba": {e}')

    total += 1
    try:
        result = candidate(s = "bcbabcbabcba") == "bcbabcbabcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbabcbabcba") == "bcbabcbabcb": {e}')

    total += 1
    try:
        result = candidate(s = "noonhighnoon") == "noon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == "noon": {e}')

    total += 1
    try:
        result = candidate(s = "forgeeksskeegfor") == "geeksskeeg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "forgeeksskeegfor") == "geeksskeeg": {e}')

    total += 1
    try:
        result = candidate(s = "aaabaaaa") == "aaabaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaa") == "aaabaaa": {e}')

    total += 1
    try:
        result = candidate(s = "abcdedcba") == "abcdedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == "abcdedcba": {e}')

    total += 1
    try:
        result = candidate(s = "aaa") == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == "aaa": {e}')

    total += 1
    try:
        result = candidate(s = "aaaaa") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == "aaaaa": {e}')

    total += 1
    try:
        result = candidate(s = "racecar") == "racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == "racecar": {e}')

    total += 1
    try:
        result = candidate(s = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == "a": {e}')

    total += 1
    try:
        result = candidate(s = "abcdefg") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == "a": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgg") == "eee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgg") == "eee": {e}')

    total += 1
    try:
        result = candidate(s = "abcdedcba12321") == "abcdedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba12321") == "abcdedcba": {e}')

    total += 1
    try:
        result = candidate(s = "xxyyyxyxyxyxyxyxxyyxyxyxyxyxyx") == "xyxyxyxyxyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyyxyxyxyxyxyxxyyxyxyxyxyxyx") == "xyxyxyxyxyx": {e}')

    total += 1
    try:
        result = candidate(s = "thisisanexamplewithlongestpalindromeonyxdxyxdx") == "xdxyxdx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisanexamplewithlongestpalindromeonyxdxyxdx") == "xdxyxdx": {e}')

    total += 1
    try:
        result = candidate(s = "12345678987654321") == "12345678987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345678987654321") == "12345678987654321": {e}')

    total += 1
    try:
        result = candidate(s = "xyzaaazyxzyzyxyz") == "xyzaaazyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzaaazyxzyzyxyz") == "xyzaaazyx": {e}')

    total += 1
    try:
        result = candidate(s = "12321abcdcba45654") == "abcdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12321abcdcba45654") == "abcdcba": {e}')

    total += 1
    try:
        result = candidate(s = "012210") == "012210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "012210") == "012210": {e}')

    total += 1
    try:
        result = candidate(s = "tattarrattat") == "tattarrattat"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tattarrattat") == "tattarrattat": {e}')

    total += 1
    try:
        result = candidate(s = "aabbabbaa") == "aabbabbaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabbaa") == "aabbabbaa": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcaba12321") == "12321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba12321") == "12321": {e}')

    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyxyxyx") == "xyxyxyxyxyxyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyxyxyx") == "xyxyxyxyxyxyx": {e}')

    total += 1
    try:
        result = candidate(s = "1234321abcdefghgfedcba") == "abcdefghgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234321abcdefghgfedcba") == "abcdefghgfedcba": {e}')

    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababab") == "bababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababab") == "bababababababababababababababababababababababababababababababab": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcabaxxxabcdcba") == "abcdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaxxxabcdcba") == "abcdcba": {e}')

    total += 1
    try:
        result = candidate(s = "12321abccba45654") == "abccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12321abccba45654") == "abccba": {e}')

    total += 1
    try:
        result = candidate(s = "12321abcdedcbavcvcv") == "abcdedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12321abcdedcbavcvcv") == "abcdedcba": {e}')

    total += 1
    try:
        result = candidate(s = "abcbaekayakecivic") == "ekayake"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaekayakecivic") == "ekayake": {e}')

    total += 1
    try:
        result = candidate(s = "noonmoonnoon") == "oonnoo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoon") == "oonnoo": {e}')

    total += 1
    try:
        result = candidate(s = "abcbaxxxxxabcdcba") == "cbaxxxxxabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaxxxxxabcdcba") == "cbaxxxxxabc": {e}')

    total += 1
    try:
        result = candidate(s = "noonhighnoonnoon") == "noonnoon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoonnoon") == "noonnoon": {e}')

    total += 1
    try:
        result = candidate(s = "noonmidnightnoon") == "noon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmidnightnoon") == "noon": {e}')

    total += 1
    try:
        result = candidate(s = "abcba12321defedcba") == "defed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba12321defedcba") == "defed": {e}')

    total += 1
    try:
        result = candidate(s = "aabbabaaaabbaaabaaabbbbbaaaaaabbbaaaabbbbaaabbaabbbaaaabbbaaabbbbaaabbaabbaabbab") == "bbaaabbbbaaabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabaaaabbaaabaaabbbbbaaaaaabbbaaaabbbbaaabbaabbbaaaabbbaaabbbbaaabbaabbaabbab") == "bbaaabbbbaaabb": {e}')

    total += 1
    try:
        result = candidate(s = "ababababababababa") == "ababababababababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababa") == "ababababababababa": {e}')

    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoonnoonnoon") == "noonnoonnoonnoonnoonnoon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoonnoonnoon") == "noonnoonnoonnoonnoonnoon": {e}')

    total += 1
    try:
        result = candidate(s = "abccbaabacdfgdcaba") == "abccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabacdfgdcaba") == "abccba": {e}')

    total += 1
    try:
        result = candidate(s = "racecarxracecar") == "racecarxracecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarxracecar") == "racecarxracecar": {e}')

    total += 1
    try:
        result = candidate(s = "madamracecarlevel") == "racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecarlevel") == "racecar": {e}')

    total += 1
    try:
        result = candidate(s = "babcbabcbabcba") == "abcbabcbabcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babcbabcbabcba") == "abcbabcbabcba": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcabaabacdfgdcaba") == "dcabaabacd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaabacdfgdcaba") == "dcabaabacd": {e}')

    total += 1
    try:
        result = candidate(s = "madamintanimadaminabba") == "animadamina"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamintanimadaminabba") == "animadamina": {e}')

    total += 1
    try:
        result = candidate(s = "noonracecarracecar") == "racecarracecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonracecarracecar") == "racecarracecar": {e}')

    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz") == "zzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz") == "zzzzzzzzzzzz": {e}')

    total += 1
    try:
        result = candidate(s = "racecar2racecar") == "racecar2racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar2racecar") == "racecar2racecar": {e}')

    total += 1
    try:
        result = candidate(s = "zxyabcddcbaabczyx") == "abcddcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyabcddcbaabczyx") == "abcddcba": {e}')

    total += 1
    try:
        result = candidate(s = "deeee") == "eeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == "eeee": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcabacdfgdcaba") == "dcabacd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabacdfgdcaba") == "dcabacd": {e}')

    total += 1
    try:
        result = candidate(s = "1234543216789876") == "123454321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234543216789876") == "123454321": {e}')

    total += 1
    try:
        result = candidate(s = "abcbaaabcba") == "abcbaaabcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaaabcba") == "abcbaaabcba": {e}')

    total += 1
    try:
        result = candidate(s = "abcdedcbaefghihgfexyzzyx") == "efghihgfe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaefghihgfexyzzyx") == "efghihgfe": {e}')

    total += 1
    try:
        result = candidate(s = "abcdefgfebac") == "efgfe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfebac") == "efgfe": {e}')

    total += 1
    try:
        result = candidate(s = "levelhannahlevel") == "levelhannahlevel"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelhannahlevel") == "levelhannahlevel": {e}')

    total += 1
    try:
        result = candidate(s = "xxyyzzzyyxx") == "xxyyzzzyyxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyzzzyyxx") == "xxyyzzzyyxx": {e}')

    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcbaxyzzyx") == "abcddcbaabcddcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcbaxyzzyx") == "abcddcbaabcddcba": {e}')

    total += 1
    try:
        result = candidate(s = "racecar12321racecar") == "racecar12321racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar12321racecar") == "racecar12321racecar": {e}')

    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == "abcdeffedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == "abcdeffedcba": {e}')

    total += 1
    try:
        result = candidate(s = "civicracecar") == "racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicracecar") == "racecar": {e}')

    total += 1
    try:
        result = candidate(s = "levelmadammadam") == "madammadam"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelmadammadam") == "madammadam": {e}')

    total += 1
    try:
        result = candidate(s = "zxyaxzyaz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyaxzyaz") == "z": {e}')

    total += 1
    try:
        result = candidate(s = "abcdefedcba") == "abcdefedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba") == "abcdefedcba": {e}')

    total += 1
    try:
        result = candidate(s = "12321321321321321") == "12321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12321321321321321") == "12321": {e}')

    total += 1
    try:
        result = candidate(s = "xyzzyxcbaapqrqpabczyzyx") == "apqrqpa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxcbaapqrqpabczyzyx") == "apqrqpa": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcaba123321") == "123321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba123321") == "123321": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcabaxxxxxabcdcba") == "baxxxxxab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaxxxxxabcdcba") == "baxxxxxab": {e}')

    total += 1
    try:
        result = candidate(s = "aabcdcbadefedcbaa") == "abcdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcdcbadefedcbaa") == "abcdcba": {e}')

    total += 1
    try:
        result = candidate(s = "abcdefghijiklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == "klmnopqrstuvwxyzzyxwvutsrqponmlk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijiklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == "klmnopqrstuvwxyzzyxwvutsrqponmlk": {e}')

    total += 1
    try:
        result = candidate(s = "bananaananab") == "bananaananab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananab") == "bananaananab": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeedcba") == "deed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeedcba") == "deed": {e}')

    total += 1
    try:
        result = candidate(s = "noonhighnoonnoonhighnoon") == "hnoonnoonh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoonnoonhighnoon") == "hnoonnoonh": {e}')

    total += 1
    try:
        result = candidate(s = "babaddabba") == "baddab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaddabba") == "baddab": {e}')

    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababbababa") == "babababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababbababa") == "babababababababababababababababababababababababababababababab": {e}')

    total += 1
    try:
        result = candidate(s = "abcdeedcba1234321xyzzyx") == "abcdeedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba1234321xyzzyx") == "abcdeedcba": {e}')

    total += 1
    try:
        result = candidate(s = "aabb") == "bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == "bb": {e}')

    total += 1
    try:
        result = candidate(s = "mamamamamamamamama") == "amamamamamamamama"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamamamamamamamama") == "amamamamamamamama": {e}')

    total += 1
    try:
        result = candidate(s = "abcdefgfedcba") == "abcdefgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcba") == "abcdefgfedcba": {e}')

    total += 1
    try:
        result = candidate(s = "abcbabcba") == "abcbabcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba") == "abcbabcba": {e}')

    total += 1
    try:
        result = candidate(s = "xyzzzzyxabcdefedcba") == "abcdefedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzyxabcdefedcba") == "abcdefedcba": {e}')

    total += 1
    try:
        result = candidate(s = "banana") == "anana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == "anana": {e}')

    total += 1
    try:
        result = candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcb") == "bcbcbcbcbcbcbcbcbcbcbcbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcb") == "bcbcbcbcbcbcbcbcbcbcbcbcb": {e}')

    total += 1
    try:
        result = candidate(s = "anana") == "anana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anana") == "anana": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeeeeddccbbbaa") == "bbccddeeeeddccbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeeddccbbbaa") == "bbccddeeeeddccbb": {e}')

    total += 1
    try:
        result = candidate(s = "12321abcdedcba45654") == "abcdedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12321abcdedcba45654") == "abcdedcba": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == "gg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == "gg": {e}')

    total += 1
    try:
        result = candidate(s = "levelracecardeifiedracecar") == "racecardeifiedracecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelracecardeifiedracecar") == "racecardeifiedracecar": {e}')

    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaa") == "aaaabbbbbaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaa") == "aaaabbbbbaaaa": {e}')

    total += 1
    try:
        result = candidate(s = "abccba") == "abccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == "abccba": {e}')

    total += 1
    try:
        result = candidate(s = "abcdcba12321xyzzyx") == "abcdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba12321xyzzyx") == "abcdcba": {e}')

    total += 1
    try:
        result = candidate(s = "12321abcba21321") == "abcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12321abcba21321") == "abcba": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "zz": {e}')

    total += 1
    try:
        result = candidate(s = "abcdcbaxxxabcdcbaabcdcbaxxxabcdcba") == "abcdcbaxxxabcdcbaabcdcbaxxxabcdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaxxxabcdcbaabcdcbaxxxabcdcba") == "abcdcbaxxxabcdcbaabcdcbaxxxabcdcba": {e}')

    total += 1
    try:
        result = candidate(s = "xyzabcbaxyz") == "abcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcbaxyz") == "abcba": {e}')

    total += 1
    try:
        result = candidate(s = "racecarannakayak") == "racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == "racecar": {e}')

    total += 1
    try:
        result = candidate(s = "abacdfgdcab") == "aba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcab") == "aba": {e}')

    total += 1
    try:
        result = candidate(s = "abcdeedcbafedcbe") == "abcdeedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbafedcbe") == "abcdeedcba": {e}')

    total += 1
    try:
        result = candidate(s = "a1b2c3d4c3b2a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1b2c3d4c3b2a") == "a": {e}')

    total += 1
    try:
        result = candidate(s = "abccccba") == "abccccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccba") == "abccccba": {e}')

    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == "noonnoonnoon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == "noonnoonnoon": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeeeedddccbaa") == "ddeeeedd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeedddccbaa") == "ddeeeedd": {e}')

    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "A": {e}')

    total += 1
    try:
        result = candidate(s = "acbbac") == "bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbbac") == "bb": {e}')

    total += 1
    try:
        result = candidate(s = "noonlevelnoon") == "noonlevelnoon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonlevelnoon") == "noonlevelnoon": {e}')

    total += 1
    try:
        result = candidate(s = "abbaabba") == "abbaabba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba") == "abbaabba": {e}')

    total += 1
    try:
        result = candidate(s = "rotor1234321rotor") == "rotor1234321rotor"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor1234321rotor") == "rotor1234321rotor": {e}')

    total += 1
    try:
        result = candidate(s = "aaaaabaaa") == "aaabaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaa") == "aaabaaa": {e}')

    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == "abcdefghihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == "abcdefghihgfedcba": {e}')

    total += 1
    try:
        result = candidate(s = "civicdeifiedrotorlevel") == "deified"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicdeifiedrotorlevel") == "deified": {e}')

    total += 1
    try:
        result = candidate(s = "aquickbrownfoxjumpsoverthelazydog") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aquickbrownfoxjumpsoverthelazydog") == "a": {e}')

    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == "z": {e}')

    total += 1
    try:
        result = candidate(s = "aabcddeffedcba") == "deffed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcddeffedcba") == "deffed": {e}')

    total += 1
    try:
        result = candidate(s = "pppppppppppppppppppppppppppppppp") == "pppppppppppppppppppppppppppppppp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppppppppppppppppppppppppp") == "pppppppppppppppppppppppppppppppp": {e}')

    total += 1
    try:
        result = candidate(s = "aabbccddeeeedddccbbaa") == "ddeeeedd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeedddccbbaa") == "ddeeeedd": {e}')

    total += 1
    try:
        result = candidate(s = "a1b2c3d4e5f6g7h8i9j0j9i8h7g6f5e4d3c2b1a") == "a1b2c3d4e5f6g7h8i9j0j9i8h7g6f5e4d3c2b1a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1b2c3d4e5f6g7h8i9j0j9i8h7g6f5e4d3c2b1a") == "a1b2c3d4e5f6g7h8i9j0j9i8h7g6f5e4d3c2b1a": {e}')

    total += 1
    try:
        result = candidate(s = "mississippi") == "ississi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == "ississi": {e}')

    total += 1
    try:
        result = candidate(s = "zxcvbnmlkjhgfdsapoiuytrewqpoiuytrewqpoiuytrewqpoiuytrewq") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmlkjhgfdsapoiuytrewqpoiuytrewqpoiuytrewqpoiuytrewq") == "z": {e}')

    total += 1
    try:
        result = candidate(s = "deifiedrotorlevel") == "deified"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedrotorlevel") == "deified": {e}')

    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abba") == "abba"
    assert candidate(s = "aaaa") == "aaaa"
    assert candidate(s = "abacdfgdcaba") == "aba"
    assert candidate(s = "ac") == "a"
    assert candidate(s = "babad") == "aba"
    assert candidate(s = "noon") == "noon"
    assert candidate(s = "cbbd") == "bb"
    assert candidate(s = "abcba") == "abcba"
    assert candidate(s = "bcbabcbabcba") == "bcbabcbabcb"
    assert candidate(s = "noonhighnoon") == "noon"
    assert candidate(s = "forgeeksskeegfor") == "geeksskeeg"
    assert candidate(s = "aaabaaaa") == "aaabaaa"
    assert candidate(s = "abcdedcba") == "abcdedcba"
    assert candidate(s = "aaa") == "aaa"
    assert candidate(s = "aaaaa") == "aaaaa"
    assert candidate(s = "racecar") == "racecar"
    assert candidate(s = "a") == "a"
    assert candidate(s = "abcdefg") == "a"
    assert candidate(s = "aabbccddeeeffgg") == "eee"
    assert candidate(s = "abcdedcba12321") == "abcdedcba"
    assert candidate(s = "xxyyyxyxyxyxyxyxxyyxyxyxyxyxyx") == "xyxyxyxyxyx"
    assert candidate(s = "thisisanexamplewithlongestpalindromeonyxdxyxdx") == "xdxyxdx"
    assert candidate(s = "12345678987654321") == "12345678987654321"
    assert candidate(s = "xyzaaazyxzyzyxyz") == "xyzaaazyx"
    assert candidate(s = "12321abcdcba45654") == "abcdcba"
    assert candidate(s = "012210") == "012210"
    assert candidate(s = "tattarrattat") == "tattarrattat"
    assert candidate(s = "aabbabbaa") == "aabbabbaa"
    assert candidate(s = "abacdfgdcaba12321") == "12321"
    assert candidate(s = "xyxxyxyxyxyxyxyx") == "xyxyxyxyxyxyx"
    assert candidate(s = "1234321abcdefghgfedcba") == "abcdefghgfedcba"
    assert candidate(s = "abababababababababababababababababababababababababababababababab") == "bababababababababababababababababababababababababababababababab"
    assert candidate(s = "abacdfgdcabaxxxabcdcba") == "abcdcba"
    assert candidate(s = "12321abccba45654") == "abccba"
    assert candidate(s = "12321abcdedcbavcvcv") == "abcdedcba"
    assert candidate(s = "abcbaekayakecivic") == "ekayake"
    assert candidate(s = "noonmoonnoon") == "oonnoo"
    assert candidate(s = "abcbaxxxxxabcdcba") == "cbaxxxxxabc"
    assert candidate(s = "noonhighnoonnoon") == "noonnoon"
    assert candidate(s = "noonmidnightnoon") == "noon"
    assert candidate(s = "abcba12321defedcba") == "defed"
    assert candidate(s = "aabbabaaaabbaaabaaabbbbbaaaaaabbbaaaabbbbaaabbaabbbaaaabbbaaabbbbaaabbaabbaabbab") == "bbaaabbbbaaabb"
    assert candidate(s = "ababababababababa") == "ababababababababa"
    assert candidate(s = "noonnoonnoonnoonnoonnoon") == "noonnoonnoonnoonnoonnoon"
    assert candidate(s = "abccbaabacdfgdcaba") == "abccba"
    assert candidate(s = "racecarxracecar") == "racecarxracecar"
    assert candidate(s = "madamracecarlevel") == "racecar"
    assert candidate(s = "babcbabcbabcba") == "abcbabcbabcba"
    assert candidate(s = "abacdfgdcabaabacdfgdcaba") == "dcabaabacd"
    assert candidate(s = "madamintanimadaminabba") == "animadamina"
    assert candidate(s = "noonracecarracecar") == "racecarracecar"
    assert candidate(s = "zzzzzzzzzzzz") == "zzzzzzzzzzzz"
    assert candidate(s = "racecar2racecar") == "racecar2racecar"
    assert candidate(s = "zxyabcddcbaabczyx") == "abcddcba"
    assert candidate(s = "deeee") == "eeee"
    assert candidate(s = "abacdfgdcabacdfgdcaba") == "dcabacd"
    assert candidate(s = "1234543216789876") == "123454321"
    assert candidate(s = "abcbaaabcba") == "abcbaaabcba"
    assert candidate(s = "abcdedcbaefghihgfexyzzyx") == "efghihgfe"
    assert candidate(s = "abcdefgfebac") == "efgfe"
    assert candidate(s = "levelhannahlevel") == "levelhannahlevel"
    assert candidate(s = "xxyyzzzyyxx") == "xxyyzzzyyxx"
    assert candidate(s = "abcddcbaabcddcbaxyzzyx") == "abcddcbaabcddcba"
    assert candidate(s = "racecar12321racecar") == "racecar12321racecar"
    assert candidate(s = "abcdeffedcba") == "abcdeffedcba"
    assert candidate(s = "civicracecar") == "racecar"
    assert candidate(s = "levelmadammadam") == "madammadam"
    assert candidate(s = "zxyaxzyaz") == "z"
    assert candidate(s = "abcdefedcba") == "abcdefedcba"
    assert candidate(s = "12321321321321321") == "12321"
    assert candidate(s = "xyzzyxcbaapqrqpabczyzyx") == "apqrqpa"
    assert candidate(s = "abacdfgdcaba123321") == "123321"
    assert candidate(s = "abacdfgdcabaxxxxxabcdcba") == "baxxxxxab"
    assert candidate(s = "aabcdcbadefedcbaa") == "abcdcba"
    assert candidate(s = "abcdefghijiklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == "klmnopqrstuvwxyzzyxwvutsrqponmlk"
    assert candidate(s = "bananaananab") == "bananaananab"
    assert candidate(s = "aabbccddeedcba") == "deed"
    assert candidate(s = "noonhighnoonnoonhighnoon") == "hnoonnoonh"
    assert candidate(s = "babaddabba") == "baddab"
    assert candidate(s = "abababababababababababababababababababababababababababababababbababa") == "babababababababababababababababababababababababababababababab"
    assert candidate(s = "abcdeedcba1234321xyzzyx") == "abcdeedcba"
    assert candidate(s = "aabb") == "bb"
    assert candidate(s = "mamamamamamamamama") == "amamamamamamamama"
    assert candidate(s = "abcdefgfedcba") == "abcdefgfedcba"
    assert candidate(s = "abcbabcba") == "abcbabcba"
    assert candidate(s = "xyzzzzyxabcdefedcba") == "abcdefedcba"
    assert candidate(s = "banana") == "anana"
    assert candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcb") == "bcbcbcbcbcbcbcbcbcbcbcbcb"
    assert candidate(s = "anana") == "anana"
    assert candidate(s = "aabbccddeeeeddccbbbaa") == "bbccddeeeeddccbb"
    assert candidate(s = "12321abcdedcba45654") == "abcdedcba"
    assert candidate(s = "aabbccddeeffgg") == "gg"
    assert candidate(s = "levelracecardeifiedracecar") == "racecardeifiedracecar"
    assert candidate(s = "aaaaabbbbbaaaa") == "aaaabbbbbaaaa"
    assert candidate(s = "abccba") == "abccba"
    assert candidate(s = "abcdcba12321xyzzyx") == "abcdcba"
    assert candidate(s = "12321abcba21321") == "abcba"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "zz"
    assert candidate(s = "abcdcbaxxxabcdcbaabcdcbaxxxabcdcba") == "abcdcbaxxxabcdcbaabcdcbaxxxabcdcba"
    assert candidate(s = "xyzabcbaxyz") == "abcba"
    assert candidate(s = "racecarannakayak") == "racecar"
    assert candidate(s = "abacdfgdcab") == "aba"
    assert candidate(s = "abcdeedcbafedcbe") == "abcdeedcba"
    assert candidate(s = "a1b2c3d4c3b2a") == "a"
    assert candidate(s = "abccccba") == "abccccba"
    assert candidate(s = "noonnoonnoon") == "noonnoonnoon"
    assert candidate(s = "aabbccddeeeedddccbaa") == "ddeeeedd"
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "A"
    assert candidate(s = "acbbac") == "bb"
    assert candidate(s = "noonlevelnoon") == "noonlevelnoon"
    assert candidate(s = "abbaabba") == "abbaabba"
    assert candidate(s = "rotor1234321rotor") == "rotor1234321rotor"
    assert candidate(s = "aaaaabaaa") == "aaabaaa"
    assert candidate(s = "abcdefghihgfedcba") == "abcdefghihgfedcba"
    assert candidate(s = "civicdeifiedrotorlevel") == "deified"
    assert candidate(s = "aquickbrownfoxjumpsoverthelazydog") == "a"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == "z"
    assert candidate(s = "aabcddeffedcba") == "deffed"
    assert candidate(s = "pppppppppppppppppppppppppppppppp") == "pppppppppppppppppppppppppppppppp"
    assert candidate(s = "aabbccddeeeedddccbbaa") == "ddeeeedd"
    assert candidate(s = "a1b2c3d4e5f6g7h8i9j0j9i8h7g6f5e4d3c2b1a") == "a1b2c3d4e5f6g7h8i9j0j9i8h7g6f5e4d3c2b1a"
    assert candidate(s = "mississippi") == "ississi"
    assert candidate(s = "zxcvbnmlkjhgfdsapoiuytrewqpoiuytrewqpoiuytrewqpoiuytrewq") == "z"
    assert candidate(s = "deifiedrotorlevel") == "deified"

