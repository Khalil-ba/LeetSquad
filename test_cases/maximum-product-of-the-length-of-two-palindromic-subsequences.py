def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "xyzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "accbcaxxcxx") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "accbcaxxcxx") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodecom") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodecom") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "bb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "refer") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refer") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "palindromeabcdcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "palindromeabcdcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyzzxxyyzz") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyzzxxyyzz") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababababab") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababababab") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyzy") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyzy") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelmadam") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelmadam") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "babadab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babadab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "referrefer") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "referrefer") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotor") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotor") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "mammam") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mammam") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonbedalabamoon") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonbedalabamoon") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelonelevel") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelonelevel") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "redderredder") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redderredder") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "redivider") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redivider") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyzzyyzzyzz") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyzzyyzzyzz") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonabbadammadam") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonabbadammadam") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdzdcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdzdcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelup") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelup") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorositor") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorositor") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamracecarmadam") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecarmadam") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcba") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcba") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcba") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcba") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyxzyxzyx") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyxzyxzyx") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzyx") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzyx") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonappaloopnoon") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonappaloopnoon") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaaabbbb") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaaabbbb") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefff") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefff") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeeevee") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeeevee") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevel") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevel") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamatadammadamada") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamatadammadamada") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzazxy") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzazxy") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyx") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyx") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelracecarlevel") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelracecarlevel") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyxzyx") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyxzyx") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelracecara") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelracecara") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "optimization") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "optimization") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabc") == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "xyzyx") == 6
    assert candidate(s = "aabbcc") == 4
    assert candidate(s = "aaaa") == 4
    assert candidate(s = "accbcaxxcxx") == 25
    assert candidate(s = "madam") == 6
    assert candidate(s = "noon") == 4
    assert candidate(s = "racecar") == 12
    assert candidate(s = "deified") == 12
    assert candidate(s = "noonhighnoon") == 35
    assert candidate(s = "abcdcba") == 12
    assert candidate(s = "abacaba") == 12
    assert candidate(s = "level") == 6
    assert candidate(s = "abcdedcba") == 20
    assert candidate(s = "abcde") == 1
    assert candidate(s = "rotor") == 6
    assert candidate(s = "leetcodecom") == 9
    assert candidate(s = "bb") == 1
    assert candidate(s = "refer") == 6
    assert candidate(s = "palindromeabcdcba") == 20
    assert candidate(s = "aaabbbccc") == 9
    assert candidate(s = "xxyyzzxxyyzz") == 36
    assert candidate(s = "noonnoonnoon") == 36
    assert candidate(s = "repaper") == 12
    assert candidate(s = "abbaabbaabba") == 36
    assert candidate(s = "xyzzyxzyxz") == 25
    assert candidate(s = "aababababab") == 30
    assert candidate(s = "xyzyzyzyzyzy") == 30
    assert candidate(s = "racecarlevelmadam") == 45
    assert candidate(s = "aabbbbaa") == 16
    assert candidate(s = "abababa") == 12
    assert candidate(s = "babadab") == 9
    assert candidate(s = "referrefer") == 25
    assert candidate(s = "rotorrotor") == 25
    assert candidate(s = "abracadabra") == 25
    assert candidate(s = "abacdfgdcaba") == 35
    assert candidate(s = "mammam") == 9
    assert candidate(s = "noonbedalabamoon") == 35
    assert candidate(s = "levelonelevel") == 35
    assert candidate(s = "abccbaabcba") == 30
    assert candidate(s = "redderredder") == 36
    assert candidate(s = "redivider") == 20
    assert candidate(s = "zzzyzzyyzzyzz") == 42
    assert candidate(s = "racecarabc") == 15
    assert candidate(s = "noonabbadammadam") == 32
    assert candidate(s = "noonnoon") == 16
    assert candidate(s = "abcdzdcba") == 20
    assert candidate(s = "abcdefghihgfedcba") == 72
    assert candidate(s = "levelup") == 6
    assert candidate(s = "rotorositor") == 25
    assert candidate(s = "madamracecarmadam") == 72
    assert candidate(s = "abcddcbaabcddcba") == 64
    assert candidate(s = "abcdefgfedcba") == 42
    assert candidate(s = "zyxzyxzyxzyxzyx") == 49
    assert candidate(s = "zzzzzzzzzzzz") == 36
    assert candidate(s = "xyzyxzyzyx") == 25
    assert candidate(s = "deeee") == 4
    assert candidate(s = "noonappaloopnoon") == 56
    assert candidate(s = "abcabcabcabcabcabc") == 81
    assert candidate(s = "abcbaabcba") == 25
    assert candidate(s = "aabbbaaaabbbb") == 42
    assert candidate(s = "aabbccddeeffgg") == 4
    assert candidate(s = "aabbccddeeefff") == 9
    assert candidate(s = "deeeevee") == 12
    assert candidate(s = "aaabaaa") == 12
    assert candidate(s = "aabbccddeeff") == 4
    assert candidate(s = "levellevel") == 25
    assert candidate(s = "madamimadam") == 30
    assert candidate(s = "mississippi") == 24
    assert candidate(s = "madamatadammadamada") == 81
    assert candidate(s = "xyzzazxy") == 15
    assert candidate(s = "xyxxyxyxyxyx") == 35
    assert candidate(s = "levelracecarlevel") == 72
    assert candidate(s = "programming") == 12
    assert candidate(s = "zyxzyxzyxzyx") == 36
    assert candidate(s = "levelracecara") == 35
    assert candidate(s = "zzzzzyzzzz") == 25
    assert candidate(s = "racecarannakayak") == 40
    assert candidate(s = "aabbaabbaa") == 25
    assert candidate(s = "xyzabcdcba") == 12
    assert candidate(s = "optimization") == 15
    assert candidate(s = "abccbaabc") == 15


