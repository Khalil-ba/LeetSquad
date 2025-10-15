def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "level") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "level") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "zyxzyxzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zyxzyxzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "madam") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madam") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "merchant") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "merchant") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeedccbbaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeedccbbaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "repaper") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repaper") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "ghiabcdefhelloadamhelloabcdefghi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ghiabcdefhelloadamhelloabcdefghi") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "antaprezatepzapreanta") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "antaprezatepzapreanta") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdabcdabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdabcdabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacaba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacaba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcddcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcddcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotor") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotor") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "refer") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "refer") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "redder") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "redder") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "peep") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "peep") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecar") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecar") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "civic") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "civic") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzyxxyzzyx") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzyxxyzzyx") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "noon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "deified") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deified") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelracecar") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelracecar") == 19: {e}')
    
    total += 1
    try:
        result = candidate(text = "deed") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deed") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abccba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abccba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeddccbbaa") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeddccbbaa") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "levellevel") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levellevel") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "bananaananabayananabanana") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bananaananabayananabanana") == 13: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcabcabcabcd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcabcabcabcd") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarannakayakracecar") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarannakayakracecar") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabcabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabcabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "xxyyxxyyxyyxxyyxxyy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xxyyxxyyxyyxxyyxxyy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "xylophonephoneyloxyxylophonephoneyloxy") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xylophonephoneyloxyxylophonephoneyloxy") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "leveloneleveltwolevelonelevel") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leveloneleveltwolevelonelevel") == 23: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabaaaabaaaa") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabaaaabaaaa") == 13: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacababacaba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacababacaba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotorcarrot") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotorcarrot") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "leveloneonetwothreefourthreefourtwoonelevel") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leveloneonetwothreefourthreefourtwoonelevel") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabaaaabaaaaaaaabaaaaabaaaabaaaa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabaaaabaaaaaaaabaaaaabaaaabaaaa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoonnoonnoonnoon") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoonnoonnoonnoon") == 24: {e}')
    
    total += 1
    try:
        result = candidate(text = "annakayakannakayakannakayakannakayakannakayak") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "annakayakannakayakannakayakannakayakannakayak") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghihgfedcbaabcdefghihgfedcba") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghihgfedcbaabcdefghihgfedcba") == 34: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefgfedcbaabcdefgfedcbaabcdefgfedcba") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefgfedcbaabcdefgfedcbaabcdefgfedcba") == 39: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabaabacaba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabaabacaba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "qwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewq") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewq") == 52: {e}')
    
    total += 1
    try:
        result = candidate(text = "madamimadamimadam") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madamimadamimadam") == 17: {e}')
    
    total += 1
    try:
        result = candidate(text = "kayak") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "kayak") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "thisisaverylongstringwhichdoesnotrepeatthisisaverylongstring") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "thisisaverylongstringwhichdoesnotrepeatthisisaverylongstring") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "deifiedrotorcarcaretordeified") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deifiedrotorcarcaretordeified") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "madamimadamimadamimadamimadam") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madamimadamimadamimadamimadam") == 29: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoonnoonnoonnoonnoonnoon") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoonnoonnoonnoonnoonnoon") == 32: {e}')
    
    total += 1
    try:
        result = candidate(text = "deifiedrotordeified") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deifiedrotordeified") == 19: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonracecarnoon") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonracecarnoon") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "madamimadam") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madamimadam") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "repaperdeified") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repaperdeified") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "deededeed") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deededeed") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "ananaananaananananananananananana") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ananaananaananananananananananana") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelracecarlevelracecarlevel") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelracecarlevelracecarlevel") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelmadamracecar") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelmadamracecar") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "leveloneonelevel") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leveloneonelevel") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzyxzyzyxzyzyxzyx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzyxzyzyxzyzyxzyx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghihgfedcba") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghihgfedcba") == 17: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbaabbaabbaabbaabba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbaabbaabbaabbaabba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabaabacabaabacaba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabaabacabaabacaba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdeedcbadcbabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdeedcbadcbabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abccbaabccba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abccbaabccba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabra") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabra") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "madammadam") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madammadam") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaabbbbbbbbbbbbbbbccccccccccccccccccccdd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaabbbbbbbbbbbbbbbccccccccccccccccccccdd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "deifiedrotorleveldeified") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deifiedrotorleveldeified") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelracecarlevelracecarlevelracecarlevel") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelracecarlevelracecarlevelracecarlevel") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "madaminnadammadam") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madaminnadammadam") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "leveldeifiedmadamdeifiedlevel") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leveldeifiedmadamdeifiedlevel") == 29: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabacabacabac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabacabacabac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbccccaaaabbbbcccc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbccccaaaabbbbcccc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoon") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoon") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzyxzyzyxzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyx") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzyxzyzyxzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyx") == 33: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefgabcdefgabcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefgabcdefgabcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabraabracadabra") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabraabracadabra") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "civiccivic") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "civiccivic") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "annakayakannakayakannakayakannakayakannakayakannakayakannakayak") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "annakayakannakayakannakayakannakayakannakayakannakayakannakayak") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotorcarrots") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotorcarrots") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabraacarab") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabraacarab") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "kayakkayakkayak") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "kayakkayakkayak") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "nun") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "nun") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "annakayakannakayakannakayak") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "annakayakannakayakannakayak") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotorlevelrotor") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotorlevelrotor") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeddccbaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeddccbaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbaabbaabba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbaabbaabba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzxyzxyzxyzxyzxyzxyzxyz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzxyzxyzxyzxyzxyzxyzxyz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "levellevellevellevel") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levellevellevellevel") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "abccbaabccbaabccba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abccbaabccbaabccba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeedcbaabcdeedcbaabcdeedcba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeedcbaabcdeedcbaabcdeedcba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefgfedcbaabcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefgfedcbaabcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "levelmadamlevel") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levelmadamlevel") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacabaabacabadabacaba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacabaabacabadabacaba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotorcarcaretor") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotorcarcaretor") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "annakayakannakayakannakayakannakayak") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "annakayakannakayakannakayakannakayak") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "levellevellevellevellevellevellevellevellevellevellevellevel") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levellevellevellevellevellevellevellevellevellevellevellevel") == 60: {e}')
    
    total += 1
    try:
        result = candidate(text = "levellevellevellevellevellevel") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levellevellevellevellevellevel") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabbbbbaaaabbbbbaaaaa") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabbbbbaaaabbbbbaaaaa") == 24: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcabcabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcabcabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbccccbbbbaaaa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbccccbbbbaaaa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "madamimadamimadamimadamimadamimadamimadamimadam") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madamimadamimadamimadamimadamimadamimadamimadam") == 47: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdxyzyxzyxcddcbaabcdxyzyxzyxcddcba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdxyzyxzyxcddcbaabcdxyzyxzyxcddcba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacabadabacaba") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacabadabacaba") == 23: {e}')
    
    total += 1
    try:
        result = candidate(text = "deifieddeified") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deifieddeified") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "deifiedracecardeified") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deifiedracecardeified") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoonnoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoonnoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "radar") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "radar") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacaba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacaba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "annakayakannakayak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "annakayakannakayak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdefgabcdefgdcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdefgabcdefgdcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarannakayak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarannakayak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 44: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacabad") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacabad") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotorrotor") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotorrotor") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabracadabra") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabracadabra") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "levellevellevellevellevel") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levellevellevellevellevel") == 25: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaabaaaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaabaaaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeedcbaabbccdd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeedcbaabbccdd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "hellohellobellohellobellohello") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "hellohellobellohellobellohello") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzxyzzxyzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzxyzzxyzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "xxyyzzzyyxxyyyzzzzyyxx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xxyyzzzyyxxyyyzzzzyyxx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeeedddccbbaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeeedddccbbaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "deifiedrotor") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "deifiedrotor") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeedcbaabcdeedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeedcbaabcdeedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababab") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababab") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabaabacabaabacabaabacaba") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabaabacabaabacabaabacaba") == 28: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbccccddddeeeeffffeeeeggggccccbbbbaaaaffff") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbccccddddeeeeffffeeeeggggccccbbbbaaaaffff") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "wow") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "wow") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabccbaabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabccbaabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabcabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabcabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcxyzzyxcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcxyzzyxcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelracecarlevelracecarlevelracecarlevelracecarlevel") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelracecarlevelracecarlevelracecarlevelracecarlevel") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "madamimadamimadamimadamimadamimadam") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madamimadamimadamimadamimadamimadam") == 35: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonabbadacabbaaddaabbnoon") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonabbadacabbaaddaabbnoon") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzyxzyxzyxzyxzyxzyxzyxyz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzyxzyxzyxzyxzyxzyxzyxyz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "levellevellevellevellevellevellevellevel") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "levellevellevellevellevellevellevellevel") == 40: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababababababab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababababababab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "mississippiississimississimississippi") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mississippiississimississimississippi") == 17: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeedcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzyxzyzyxzyx") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzyxzyzyxzyx") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdcdeabcdcdeabcdcdeabcd") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdcdeabcdcdeabcdcdeabcd") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarracecar") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarracecar") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "rotorrotorrotor") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "rotorrotorrotor") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelracecarlevel") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelracecarlevel") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "kayakkayak") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "kayakkayak") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarlevelmadamracecarlevelmadam") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarlevelmadamracecarlevelmadam") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcxyzzyxcbaabcxyzzyxcba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcxyzzyxcbaabcxyzzyxcba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(text = "redividerrotorredivider") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "redividerrotorredivider") == 23: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababababababababababababababab") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababababababababababababababab") == 17: {e}')
    
    total += 1
    try:
        result = candidate(text = "referrefer") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "referrefer") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoonnoonnoonnoonnoonnoonnoonnoon") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoonnoonnoonnoonnoonnoonnoonnoon") == 40: {e}')
    
    total += 1
    try:
        result = candidate(text = "madamimadamimadamimadam") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "madamimadamimadamimadam") == 23: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbaabbaabbaabba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbaabbaabbaabba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "mississippi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mississippi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeedccbbaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeedccbbaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeabcdeabcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeabcdeabcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecarracecarracecar") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecarracecarracecar") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "redivider") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "redivider") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "thisisaverylongstringwithnorepeatedpattern") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "thisisaverylongstringwithnorepeatedpattern") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "abcabc") == 2
    assert candidate(text = "abcabcabc") == 3
    assert candidate(text = "level") == 5
    assert candidate(text = "zyxzyxzyx") == 3
    assert candidate(text = "madam") == 5
    assert candidate(text = "aaaaa") == 5
    assert candidate(text = "merchant") == 1
    assert candidate(text = "aabbccddeedccbbaa") == 15
    assert candidate(text = "repaper") == 7
    assert candidate(text = "ghiabcdefhelloadamhelloabcdefghi") == 7
    assert candidate(text = "aaa") == 3
    assert candidate(text = "antaprezatepzapreanta") == 11
    assert candidate(text = "abcdabcdabcdabcd") == 4
    assert candidate(text = "abacaba") == 7
    assert candidate(text = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(text = "xyzzyx") == 6
    assert candidate(text = "abcddcba") == 8
    assert candidate(text = "rotor") == 5
    assert candidate(text = "abcdedcba") == 9
    assert candidate(text = "refer") == 5
    assert candidate(text = "redder") == 6
    assert candidate(text = "peep") == 4
    assert candidate(text = "abba") == 4
    assert candidate(text = "racecar") == 7
    assert candidate(text = "civic") == 5
    assert candidate(text = "abcdabcd") == 2
    assert candidate(text = "a") == 1
    assert candidate(text = "abcabcabcabcabcabc") == 6
    assert candidate(text = "xyzzyxxyzzyx") == 12
    assert candidate(text = "noon") == 4
    assert candidate(text = "deified") == 7
    assert candidate(text = "racecarlevelracecar") == 19
    assert candidate(text = "deed") == 4
    assert candidate(text = "abccba") == 6
    assert candidate(text = "abab") == 2
    assert candidate(text = "aabbccddeeddccbbaa") == 18
    assert candidate(text = "abcba") == 5
    assert candidate(text = "abcdeedcba") == 10
    assert candidate(text = "levellevel") == 10
    assert candidate(text = "ababababab") == 5
    assert candidate(text = "bananaananabayananabanana") == 13
    assert candidate(text = "abcdabcabcabcabcd") == 5
    assert candidate(text = "racecarannakayakracecar") == 15
    assert candidate(text = "abcabcabcabcabcabcabc") == 7
    assert candidate(text = "xxyyxxyyxyyxxyyxxyy") == 5
    assert candidate(text = "xylophonephoneyloxyxylophonephoneyloxy") == 10
    assert candidate(text = "leveloneleveltwolevelonelevel") == 23
    assert candidate(text = "aaaaabaaaabaaaa") == 13
    assert candidate(text = "abacababacaba") == 13
    assert candidate(text = "rotorcarrot") == 3
    assert candidate(text = "leveloneonetwothreefourthreefourtwoonelevel") == 15
    assert candidate(text = "aaaaabaaaabaaaaaaaabaaaaabaaaabaaaa") == 27
    assert candidate(text = "noonnoonnoonnoonnoonnoon") == 24
    assert candidate(text = "annakayakannakayakannakayakannakayakannakayak") == 5
    assert candidate(text = "abcdefghihgfedcbaabcdefghihgfedcba") == 34
    assert candidate(text = "abcdefgfedcbaabcdefgfedcbaabcdefgfedcba") == 39
    assert candidate(text = "abacabaabacaba") == 14
    assert candidate(text = "qwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewq") == 52
    assert candidate(text = "madamimadamimadam") == 17
    assert candidate(text = "kayak") == 5
    assert candidate(text = "thisisaverylongstringwhichdoesnotrepeatthisisaverylongstring") == 3
    assert candidate(text = "deifiedrotorcarcaretordeified") == 21
    assert candidate(text = "madamimadamimadamimadamimadam") == 29
    assert candidate(text = "noonnoonnoonnoonnoonnoonnoonnoon") == 32
    assert candidate(text = "deifiedrotordeified") == 19
    assert candidate(text = "noonracecarnoon") == 15
    assert candidate(text = "madamimadam") == 11
    assert candidate(text = "repaperdeified") == 1
    assert candidate(text = "deededeed") == 9
    assert candidate(text = "ananaananaananananananananananana") == 15
    assert candidate(text = "racecarlevelracecarlevelracecarlevel") == 3
    assert candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 18
    assert candidate(text = "racecarlevelmadamracecar") == 15
    assert candidate(text = "leveloneonelevel") == 12
    assert candidate(text = "xyzyxzyzyxzyzyxzyx") == 15
    assert candidate(text = "abcdefghihgfedcba") == 17
    assert candidate(text = "abbaabbaabbaabbaabba") == 20
    assert candidate(text = "abacabaabacabaabacaba") == 21
    assert candidate(text = "abcdabcdeedcbadcbabcd") == 3
    assert candidate(text = "abccbaabccba") == 12
    assert candidate(text = "abracadabra") == 7
    assert candidate(text = "madammadam") == 10
    assert candidate(text = "aaaaaaaaabbbbbbbbbbbbbbbccccccccccccccccccccdd") == 1
    assert candidate(text = "deifiedrotorleveldeified") == 15
    assert candidate(text = "racecarlevelracecarlevelracecarlevelracecarlevel") == 4
    assert candidate(text = "madaminnadammadam") == 11
    assert candidate(text = "leveldeifiedmadamdeifiedlevel") == 29
    assert candidate(text = "abacabacabacabac") == 4
    assert candidate(text = "aaaabbbbccccaaaabbbbcccc") == 2
    assert candidate(text = "noonnoonnoon") == 12
    assert candidate(text = "xyzyxzyzyxzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyx") == 33
    assert candidate(text = "abcdefgabcdefgabcdefg") == 3
    assert candidate(text = "abracadabraabracadabra") == 14
    assert candidate(text = "civiccivic") == 10
    assert candidate(text = "annakayakannakayakannakayakannakayakannakayakannakayakannakayak") == 7
    assert candidate(text = "rotorcarrots") == 1
    assert candidate(text = "abracadabraacarab") == 11
    assert candidate(text = "kayakkayakkayak") == 15
    assert candidate(text = "nun") == 3
    assert candidate(text = "annakayakannakayakannakayak") == 3
    assert candidate(text = "rotorlevelrotor") == 15
    assert candidate(text = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 2
    assert candidate(text = "aabbccddeeddccbaa") == 7
    assert candidate(text = "abbaabbaabba") == 12
    assert candidate(text = "xyzxyzxyzxyzxyzxyzxyzxyz") == 8
    assert candidate(text = "levellevellevellevel") == 20
    assert candidate(text = "abccbaabccbaabccba") == 18
    assert candidate(text = "abcdeedcbaabcdeedcbaabcdeedcba") == 30
    assert candidate(text = "abcdefgfedcbaabcdefg") == 3
    assert candidate(text = "levelmadamlevel") == 15
    assert candidate(text = "abcabcabcabc") == 4
    assert candidate(text = "abacabadabacabaabacabadabacaba") == 30
    assert candidate(text = "rotorcarcaretor") == 7
    assert candidate(text = "annakayakannakayakannakayakannakayak") == 4
    assert candidate(text = "levellevellevellevellevellevellevellevellevellevellevellevel") == 60
    assert candidate(text = "levellevellevellevellevellevel") == 30
    assert candidate(text = "aaaaabbbbbaaaabbbbbaaaaa") == 24
    assert candidate(text = "abcdabcabcabcd") == 4
    assert candidate(text = "aaaabbbbccccbbbbaaaa") == 20
    assert candidate(text = "madamimadamimadamimadamimadamimadamimadamimadam") == 47
    assert candidate(text = "abcdxyzyxzyxcddcbaabcdxyzyxzyxcddcba") == 18
    assert candidate(text = "abacabadabacabadabacaba") == 23
    assert candidate(text = "deifieddeified") == 14
    assert candidate(text = "deifiedracecardeified") == 21
    assert candidate(text = "noonnoonnoonnoon") == 16
    assert candidate(text = "radar") == 5
    assert candidate(text = "abacabadabacaba") == 15
    assert candidate(text = "annakayakannakayak") == 2
    assert candidate(text = "abcdabcdefgabcdefgdcba") == 10
    assert candidate(text = "racecarannakayak") == 1
    assert candidate(text = "abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 44
    assert candidate(text = "abacabadabacabad") == 2
    assert candidate(text = "rotorrotor") == 10
    assert candidate(text = "abcabcabcabcabc") == 5
    assert candidate(text = "abracadabracadabra") == 11
    assert candidate(text = "levellevellevellevellevel") == 25
    assert candidate(text = "aaaaaabaaaaa") == 11
    assert candidate(text = "aabbccddeedcbaabbccdd") == 3
    assert candidate(text = "hellohellobellohellobellohello") == 4
    assert candidate(text = "xyzzxyzzxyzz") == 3
    assert candidate(text = "xxyyzzzyyxxyyyzzzzyyxx") == 15
    assert candidate(text = "aabbccddeeeedddccbbaaa") == 5
    assert candidate(text = "deifiedrotor") == 1
    assert candidate(text = "abcdeedcbaabcdeedcba") == 20
    assert candidate(text = "abababababababab") == 8
    assert candidate(text = "abacabaabacabaabacabaabacaba") == 28
    assert candidate(text = "aaaabbbbccccddddeeeeffffeeeeggggccccbbbbaaaaffff") == 1
    assert candidate(text = "wow") == 3
    assert candidate(text = "abcdabccbaabcd") == 8
    assert candidate(text = "abcabcabcabcabcabcabcd") == 1
    assert candidate(text = "abcxyzzyxcba") == 12
    assert candidate(text = "racecarlevelracecarlevelracecarlevelracecarlevelracecarlevel") == 5
    assert candidate(text = "madamimadamimadamimadamimadamimadam") == 35
    assert candidate(text = "noonabbadacabbaaddaabbnoon") == 15
    assert candidate(text = "xyzzyxzyxzyxzyxzyxzyxzyxyz") == 15
    assert candidate(text = "levellevellevellevellevellevellevellevel") == 40
    assert candidate(text = "abababababababababababab") == 12
    assert candidate(text = "mississippiississimississimississippi") == 17
    assert candidate(text = "aabbccddeedcba") == 3
    assert candidate(text = "xyzyxzyzyxzyx") == 11
    assert candidate(text = "aaaaabaaa") == 7
    assert candidate(text = "abcdcdeabcdcdeabcdcdeabcd") == 7
    assert candidate(text = "racecarracecar") == 14
    assert candidate(text = "rotorrotorrotor") == 15
    assert candidate(text = "racecarlevelracecarlevel") == 2
    assert candidate(text = "kayakkayak") == 10
    assert candidate(text = "noonnoon") == 8
    assert candidate(text = "racecarlevelmadamracecarlevelmadam") == 2
    assert candidate(text = "abcxyzzyxcbaabcxyzzyxcba") == 24
    assert candidate(text = "redividerrotorredivider") == 23
    assert candidate(text = "ababababababababababababababababab") == 17
    assert candidate(text = "referrefer") == 10
    assert candidate(text = "noonnoonnoonnoonnoonnoonnoonnoonnoonnoon") == 40
    assert candidate(text = "madamimadamimadamimadam") == 23
    assert candidate(text = "abbaabbaabbaabba") == 16
    assert candidate(text = "mississippi") == 1
    assert candidate(text = "aabbccddeedccbbaaa") == 5
    assert candidate(text = "abcdeabcdeabcde") == 3
    assert candidate(text = "racecarracecarracecar") == 21
    assert candidate(text = "redivider") == 9
    assert candidate(text = "thisisaverylongstringwithnorepeatedpattern") == 1


