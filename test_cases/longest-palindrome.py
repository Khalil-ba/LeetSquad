def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aabbccc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccccdd") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccdd") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyyzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyyzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddee") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddee") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbccc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbccc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "Aa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Aa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbccc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbccc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadcb") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadcb") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcABC") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcABC") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbcccc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbcccc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abAB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abAB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiJJkkLLmmNNooPPqqRRssSStttUuuVvvWwwXxxYyyZzz") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiJJkkLLmmNNooPPqqRRssSStttUuuVvvWwwXxxYyyZzz") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcABCabcABCabcABC") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcABCabcABCabcABC") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeABCDEabcdeABCDEabcdeABCDEabcdeABCDE") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeABCDEabcdeABCDEabcdeABCDEabcdeABCDE") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcdabcabcdabcabcdabc") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcdabcabcdabcabcdabc") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "Aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAAAaaaBBBbbbCCCcccDDDdddEEEeeeFFFfffGGGgggHHHhhhIIIiiiJJJjjjKKKkkkLLLlllMMMmmmNNNnnnOOOoooPPPpppQQQqqqRRRrrrSSSsssTTTtttUUUuuuVVVvvvWWWwwwXXXxxxYYYyyyZZZzzz") == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAAAaaaBBBbbbCCCcccDDDdddEEEeeeFFFfffGGGgggHHHhhhIIIiiiJJJjjjKKKkkkLLLlllMMMmmmNNNnnnOOOoooPPPpppQQQqqqRRRrrrSSSsssTTTtttUUUuuuVVVvvvWWWwwwXXXxxxYYYyyyZZZzzz") == 157: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbaABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbaABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bAabA") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bAabA") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbcccdddd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbcccdddd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffffffgggg") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffffffgggg") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaaacccddeeefffggghhhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaaacccddeeefffggghhhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbacdfee") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbacdfee") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "AxA") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AxA") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbbcccc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbbcccc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisatest") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisatest") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "Aaaaaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Aaaaaaaa") == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aabbccc") == 7
    assert candidate(s = "abccccdd") == 7
    assert candidate(s = "zyyzzzzz") == 8
    assert candidate(s = "abcdedcba") == 9
    assert candidate(s = "aabbbb") == 6
    assert candidate(s = "aaaaa") == 5
    assert candidate(s = "aabbccddee") == 10
    assert candidate(s = "a") == 1
    assert candidate(s = "aaabbbaa") == 7
    assert candidate(s = "aabbbccc") == 7
    assert candidate(s = "aabbbbccc") == 9
    assert candidate(s = "zzzz") == 4
    assert candidate(s = "aabbc") == 5
    assert candidate(s = "") == 0
    assert candidate(s = "aabbb") == 5
    assert candidate(s = "abcde") == 1
    assert candidate(s = "Aa") == 1
    assert candidate(s = "racecar") == 7
    assert candidate(s = "aabb") == 4
    assert candidate(s = "abbccc") == 5
    assert candidate(s = "abcadcb") == 7
    assert candidate(s = "abcABC") == 1
    assert candidate(s = "abba") == 4
    assert candidate(s = "abc") == 1
    assert candidate(s = "aabbccddeeffgghhii") == 18
    assert candidate(s = "aabbccddeeff") == 12
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(s = "aabbbbcccc") == 10
    assert candidate(s = "zzzzzzzz") == 8
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
    assert candidate(s = "abcdefg") == 1
    assert candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 1
    assert candidate(s = "abAB") == 1
    assert candidate(s = "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiJJkkLLmmNNooPPqqRRssSStttUuuVvvWwwXxxYyyZzz") == 71
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 49
    assert candidate(s = "deified") == 7
    assert candidate(s = "AaBbCcDdEeFfGg") == 1
    assert candidate(s = "abcABCabcABCabcABC") == 13
    assert candidate(s = "abcdeABCDEabcdeABCDEabcdeABCDEabcdeABCDE") == 40
    assert candidate(s = "abcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcdabcabcdabcabcdabc") == 71
    assert candidate(s = "Aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 51
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 1
    assert candidate(s = "abacabadabacaba") == 15
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAAAaaaBBBbbbCCCcccDDDdddEEEeeeFFFfffGGGgggHHHhhhIIIiiiJJJjjjKKKkkkLLLlllMMMmmmNNNnnnOOOoooPPPpppQQQqqqRRRrrrSSSsssTTTtttUUUuuuVVVvvvWWWwwwXXXxxxYYYyyyZZZzzz") == 157
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1
    assert candidate(s = "abacabadabacabadabacabadabacabad") == 32
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbaABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1
    assert candidate(s = "bAabA") == 5
    assert candidate(s = "rotor") == 5
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == 51
    assert candidate(s = "noon") == 4
    assert candidate(s = "banana") == 5
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 56
    assert candidate(s = "abbcccdddd") == 9
    assert candidate(s = "aabbccddeeeffffffgggg") == 21
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(s = "bbaaaacccddeeefffggghhhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 55
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 71
    assert candidate(s = "abbacdfee") == 7
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 58
    assert candidate(s = "AxA") == 3
    assert candidate(s = "aaabbbbcccc") == 11
    assert candidate(s = "thisisatest") == 7
    assert candidate(s = "mississippi") == 11
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
    assert candidate(s = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 49
    assert candidate(s = "level") == 5
    assert candidate(s = "Aaaaaaaa") == 7


