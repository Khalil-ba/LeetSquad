def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aA") == "aA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aA") == "aA": {e}')
    
    total += 1
    try:
        result = candidate(s = "2a554442f544asf") == "4444455522aaffs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2a554442f544asf") == "4444455522aaffs": {e}')
    
    total += 1
    try:
        result = candidate(s = "2a554442f544asfasss") == "44444ssssaaa55522ff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2a554442f544asfasss") == "44444ssssaaa55522ff": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzZZZZ") == "zzzzZZZZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzZZZZ") == "zzzzZZZZ": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaccdd") == "bbaaccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaccdd") == "bbaaccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "1223334444") == "4444333221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1223334444") == "4444333221": {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaaa") == "cccaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaaa") == "cccaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "tree") == "eetr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tree") == "eetr": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaaaAaA") == "aaaaaAAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaaaAaA") == "aaaaaAAA": {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaaaAaaAAaAa") == "aaaaaaaaAAAAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaaaAaaAAaAa") == "aaaaaaaaAAAAA": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaaaAaaAA") == "aaaaaaAAAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaaaAaaAA") == "aaaaaaAAAA": {e}')
    
    total += 1
    try:
        result = candidate(s = "Aabb") == "bbAa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Aabb") == "bbAa": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890") == "1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890") == "1234567890": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaacc") == "bbaacc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaacc") == "bbaacc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiijjjjjjjjjkkkkkkkkkkllllllllllllmmmmmmmmmmmmm") == "mmmmmmmmmmmmmllllllllllllkkkkkkkkkkjjjjjjjjjiiiiiiiaaaabbbbccccddddeeeeffffgggghhhh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiijjjjjjjjjkkkkkkkkkkllllllllllllmmmmmmmmmmmmm") == "mmmmmmmmmmmmmllllllllllllkkkkkkkkkkjjjjjjjjjiiiiiiiaaaabbbbccccddddeeeeffffgggghhhh": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0") == "aaa111bbb222ccc333ddd444eee555fff666ggg777hhh888iii999jjj000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0") == "aaa111bbb222ccc333ddd444eee555fff666ggg777hhh888iii999jjj000": {e}')
    
    total += 1
    try:
        result = candidate(s = "eLeetCoDe") == "eeeeLtCoD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eLeetCoDe") == "eeeeLtCoD": {e}')
    
    total += 1
    try:
        result = candidate(s = "!!!!!!@@@@@@########$$$$$$$&&&&&&&&&&(((((()))))))") == "&&&&&&&&&&########$$$$$$$)))))))!!!!!!@@@@@@(((((("
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "!!!!!!@@@@@@########$$$$$$$&&&&&&&&&&(((((()))))))") == "&&&&&&&&&&########$$$$$$$)))))))!!!!!!@@@@@@((((((": {e}')
    
    total += 1
    try:
        result = candidate(s = "112233445566778899001122334455") == "111122223333444455556677889900"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "112233445566778899001122334455") == "111122223333444455556677889900": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcABC123abcABC123abcABC") == "aaabbbcccAAABBBCCC112233"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcABC123abcABC123abcABC") == "aaabbbcccAAABBBCCC112233": {e}')
    
    total += 1
    try:
        result = candidate(s = "anagram") == "aaangrm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anagram") == "aaangrm": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1b2c3d4e5f6g7h8i9j0A1B2C3D4E5F6G7H8I9J0") == "11223344556677889900abcdefghijABCDEFGHIJ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1b2c3d4e5f6g7h8i9j0A1B2C3D4E5F6G7H8I9J0") == "11223344556677889900abcdefghijABCDEFGHIJ": {e}')
    
    total += 1
    try:
        result = candidate(s = "frequencysorttestcase") == "eeeessstttrrccfqunyoa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "frequencysorttestcase") == "eeeessstttrrccfqunyoa": {e}')
    
    total += 1
    try:
        result = candidate(s = "frequencySort") == "rreefquncySot"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "frequencySort") == "rreefquncySot": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbccccdddd") == "aaaaaaaaaaccccddddbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbccccdddd") == "aaaaaaaaaaccccddddbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode") == "eeeltcod"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode") == "eeeltcod": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHIİJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZIİJ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHIİJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZIİJ": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongtestcasewithmixedcharacters1234567890!@#$%^&*()") == "tttttssssseeeeeiiiiaaaahhhrrrcccvylongwmxd1234567890!@#$%^&*()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongtestcasewithmixedcharacters1234567890!@#$%^&*()") == "tttttssssseeeeeiiiiaaaahhhrrrcccvylongwmxd1234567890!@#$%^&*()": {e}')
    
    total += 1
    try:
        result = candidate(s = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa1234567890") == "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa1234567890") == "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa1234567890": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcABC123xyzXYZ!@#") == "abcABC123xyzXYZ!@#"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcABC123xyzXYZ!@#") == "abcABC123xyzXYZ!@#": {e}')
    
    total += 1
    try:
        result = candidate(s = "01233210") == "00112233"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01233210") == "00112233": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCDEFGHIJKLMNOPQRSTUVWXYZ": {e}')
    
    total += 1
    try:
        result = candidate(s = "111222333444555666777888999000") == "111222333444555666777888999000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111222333444555666777888999000") == "111222333444555666777888999000": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharactersaretestedhere") == "eeeeeeeeerrrrraaaattttddcchhssp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharactersaretestedhere") == "eeeeeeeeerrrrraaaattttddcchhssp": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiIIjjJJkkKKllLLmmMMnnNNooppQQrrSSttUUvvWWxxYYzzZZ") == "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiIIjjJJkkKKllLLmmMMnnNNooppQQrrSSttUUvvWWxxYYzzZZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiIIjjJJkkKKllLLmmMMnnNNooppQQrrSSttUUvvWWxxYYzzZZ") == "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiIIjjJJkkKKllLLmmMMnnNNooppQQrrSSttUUvvWWxxYYzzZZ": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == "iiiissssppm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == "iiiissssppm": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "Mississippi") == "iiiissssppM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Mississippi") == "iiiissssppM": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "aaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "aaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAA": {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789012345678901234567890") == "111222333444555666777888999000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789012345678901234567890") == "111222333444555666777888999000": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aA") == "aA"
    assert candidate(s = "2a554442f544asf") == "4444455522aaffs"
    assert candidate(s = "2a554442f544asfasss") == "44444ssssaaa55522ff"
    assert candidate(s = "zzzzZZZZ") == "zzzzZZZZ"
    assert candidate(s = "bbaaccdd") == "bbaaccdd"
    assert candidate(s = "1223334444") == "4444333221"
    assert candidate(s = "cccaaa") == "cccaaa"
    assert candidate(s = "tree") == "eetr"
    assert candidate(s = "aAaaaAaA") == "aaaaaAAA"
    assert candidate(s = "a") == "a"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "") == ""
    assert candidate(s = "aAaaaAaaAAaAa") == "aaaaaaaaAAAAA"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "aAaaaAaaAA") == "aaaaaaAAAA"
    assert candidate(s = "Aabb") == "bbAa"
    assert candidate(s = "1234567890") == "1234567890"
    assert candidate(s = "bbaacc") == "bbaacc"
    assert candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiijjjjjjjjjkkkkkkkkkkllllllllllllmmmmmmmmmmmmm") == "mmmmmmmmmmmmmllllllllllllkkkkkkkkkkjjjjjjjjjiiiiiiiaaaabbbbccccddddeeeeffffgggghhhh"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA"
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    assert candidate(s = "a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0") == "aaa111bbb222ccc333ddd444eee555fff666ggg777hhh888iii999jjj000"
    assert candidate(s = "eLeetCoDe") == "eeeeLtCoD"
    assert candidate(s = "!!!!!!@@@@@@########$$$$$$$&&&&&&&&&&(((((()))))))") == "&&&&&&&&&&########$$$$$$$)))))))!!!!!!@@@@@@(((((("
    assert candidate(s = "112233445566778899001122334455") == "111122223333444455556677889900"
    assert candidate(s = "abcABC123abcABC123abcABC") == "aaabbbcccAAABBBCCC112233"
    assert candidate(s = "anagram") == "aaangrm"
    assert candidate(s = "a1b2c3d4e5f6g7h8i9j0A1B2C3D4E5F6G7H8I9J0") == "11223344556677889900abcdefghijABCDEFGHIJ"
    assert candidate(s = "frequencysorttestcase") == "eeeessstttrrccfqunyoa"
    assert candidate(s = "frequencySort") == "rreefquncySot"
    assert candidate(s = "aaaaaaaaaabbccccdddd") == "aaaaaaaaaaccccddddbb"
    assert candidate(s = "leetcode") == "eeeltcod"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHIİJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZIİJ"
    assert candidate(s = "thisisaverylongtestcasewithmixedcharacters1234567890!@#$%^&*()") == "tttttssssseeeeeiiiiaaaahhhrrrcccvylongwmxd1234567890!@#$%^&*()"
    assert candidate(s = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa1234567890") == "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa1234567890"
    assert candidate(s = "abcABC123xyzXYZ!@#") == "abcABC123xyzXYZ!@#"
    assert candidate(s = "01233210") == "00112233"
    assert candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert candidate(s = "111222333444555666777888999000") == "111222333444555666777888999000"
    assert candidate(s = "repeatedcharactersaretestedhere") == "eeeeeeeeerrrrraaaattttddcchhssp"
    assert candidate(s = "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiIIjjJJkkKKllLLmmMMnnNNooppQQrrSSttUUvvWWxxYYzzZZ") == "aaAAbbBBccCCddDDeeEEffFFggGGhhHHiiIIjjJJkkKKllLLmmMMnnNNooppQQrrSSttUUvvWWxxYYzzZZ"
    assert candidate(s = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert candidate(s = "mississippi") == "iiiissssppm"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890"
    assert candidate(s = "aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890") == "iiiaabbccddeeffgghhjjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "Mississippi") == "iiiissssppM"
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "aaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAA"
    assert candidate(s = "123456789012345678901234567890") == "111222333444555666777888999000"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba"


