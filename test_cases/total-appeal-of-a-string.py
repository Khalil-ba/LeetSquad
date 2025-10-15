def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 3276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 3276: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzaaa") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzaaa") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 357: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 109: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbca") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbca") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "python") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "world") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "world") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 244: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 1306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 1306: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 148: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "z") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 13078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 13078: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithvariouscharacters") == 3921
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithvariouscharacters") == 3921: {e}')
    
    total += 1
    try:
        result = candidate(s = "code") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "code") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 3276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 3276: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzz") == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzz") == 191: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeefffffffffgggggggggghhhhhhhhhh") == 11380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeefffffffffgggggggggghhhhhhhhhh") == 11380: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccaaabbbccc") == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccaaabbbccc") == 274: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 18730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 18730: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 6520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 6520: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaccddeeffgg") == 329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaccddeeffgg") == 329: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbccddeeefffggghhhiiijjjkkklllmnnnooopppqqqrrrsssttuuuuuuuuvvwxyz") == 26940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbccddeeefffggghhhiiijjjkkklllmnnnooopppqqqrrrsssttuuuuuuuuvvwxyz") == 26940: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 1306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 1306: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquecharacters") == 677
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquecharacters") == 677: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzz") == 23011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzz") == 23011: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 1008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 1008: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc") == 865
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc") == 865: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == 1838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == 1838: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababa") == 841
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababa") == 841: {e}')
    
    total += 1
    try:
        result = candidate(s = "ninetyninebottlesofbeer") == 1564
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ninetyninebottlesofbeer") == 1564: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdbcadbacdbac") == 646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdbcadbacdbac") == 646: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 1820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 1820: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 46306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 46306: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 5345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 5345: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 3276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 3276: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabc") == 1054
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabc") == 1054: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 256: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 21528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 21528: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxz") == 5105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxz") == 5105: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello") == 377: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 46120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 46120: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellobyebye") == 513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellobyebye") == 513: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 8230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 8230: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadaba") == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadaba") == 177: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1378: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisareallylongteststringwithmanydistinctcharactersandrepeatedones") == 25027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisareallylongteststringwithmanydistinctcharactersandrepeatedones") == 25027: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmanycopiesofthissubstringthissubstringthissubstring") == 35609
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmanycopiesofthissubstringthissubstringthissubstring") == 35609: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 2363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 2363: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc") == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyxzyzyzyxzyzyxzyzyzyzyxzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 4088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyxzyzyzyxzyzyxzyzyzyzyxzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 4088: {e}')
    
    total += 1
    try:
        result = candidate(s = "amazingappeal") == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amazingappeal") == 374: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1275: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccaaaabbbccc") == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccaaaabbbccc") == 309: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaabacabadabacaba") == 1555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaabacabadabacaba") == 1555: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 3276
    assert candidate(s = "zzzaaa") == 30
    assert candidate(s = "a") == 1
    assert candidate(s = "abacabadabacaba") == 357
    assert candidate(s = "abcabcabc") == 109
    assert candidate(s = "abbca") == 28
    assert candidate(s = "ababababab") == 100
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
    assert candidate(s = "aaa") == 6
    assert candidate(s = "python") == 56
    assert candidate(s = "abcabc") == 46
    assert candidate(s = "world") == 35
    assert candidate(s = "zzzzzzzzzz") == 55
    assert candidate(s = "abcdabcdabcd") == 244
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 1306
    assert candidate(s = "abc") == 10
    assert candidate(s = "abcd") == 20
    assert candidate(s = "aaaa") == 10
    assert candidate(s = "hello") == 29
    assert candidate(s = "mississippi") == 148
    assert candidate(s = "zzzzz") == 15
    assert candidate(s = "z") == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 13078
    assert candidate(s = "longstringwithvariouscharacters") == 3921
    assert candidate(s = "code") == 20
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 3276
    assert candidate(s = "xyzzxyzzxyzz") == 191
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeefffffffffgggggggggghhhhhhhhhh") == 11380
    assert candidate(s = "abcdefg") == 84
    assert candidate(s = "aabbccaaabbbccc") == 274
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 18730
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 6520
    assert candidate(s = "bbaaccddeeffgg") == 329
    assert candidate(s = "aabbaabbaabbccddeeefffggghhhiiijjjkkklllmnnnooopppqqqrrrsssttuuuuuuuuvvwxyz") == 26940
    assert candidate(s = "abracadabra") == 210
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 1306
    assert candidate(s = "uniquecharacters") == 677
    assert candidate(s = "aabbc") == 25
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzz") == 23011
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 1008
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc") == 865
    assert candidate(s = "abacabadabacabadabacabadabacabad") == 1838
    assert candidate(s = "ababababababababababababababa") == 841
    assert candidate(s = "ninetyninebottlesofbeer") == 1564
    assert candidate(s = "abcdabcdbcadbacdbac") == 646
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 1820
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 46306
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 5345
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 3276
    assert candidate(s = "abcabcabcabcabcabcabcabcabc") == 1054
    assert candidate(s = "abababababababab") == 256
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 21528
    assert candidate(s = "xyxzyzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxzyxzyzyxz") == 5105
    assert candidate(s = "hellohellohello") == 377
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 46120
    assert candidate(s = "banana") == 40
    assert candidate(s = "hellohellobyebye") == 513
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 8230
    assert candidate(s = "abacabadaba") == 177
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1378
    assert candidate(s = "thisisareallylongteststringwithmanydistinctcharactersandrepeatedones") == 25027
    assert candidate(s = "thisisaverylongstringwithmanycopiesofthissubstringthissubstringthissubstring") == 35609
    assert candidate(s = "xyxzyxyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 2363
    assert candidate(s = "aaaaabbbbbccccc") == 220
    assert candidate(s = "xyzzzyxzyzyzyxzyzyxzyzyzyzyxzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 4088
    assert candidate(s = "amazingappeal") == 374
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1275
    assert candidate(s = "aabbccaaaabbbccc") == 309
    assert candidate(s = "abacabadabacabaabacabadabacaba") == 1555


