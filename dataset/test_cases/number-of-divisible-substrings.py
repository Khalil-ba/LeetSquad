def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aaabbbccc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbccc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "z") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "z") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "bdh") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bdh") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "asdf") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "asdf") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "world") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "world") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "lmnopqrs") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lmnopqrs") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "hello") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hello") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiop") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiop") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqr") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqr") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 95: {e}')
    
    total += 1
    try:
        result = candidate(word = "programming") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "programming") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 95: {e}')
    
    total += 1
    try:
        result = candidate(word = "hellohellohellohellohello") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hellohellohellohellohello") == 66: {e}')
    
    total += 1
    try:
        result = candidate(word = "noon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "noon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzmnopqrstuvwxyzabcdefghij") == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzmnopqrstuvwxyzabcdefghij") == 380: {e}')
    
    total += 1
    try:
        result = candidate(word = "divisible") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "divisible") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "bananabanana") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bananabanana") == 34: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "xzyxzyxzyxzy") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xzyxzyxzyxzy") == 78: {e}')
    
    total += 1
    try:
        result = candidate(word = "amazingrace") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "amazingrace") == 31: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 60: {e}')
    
    total += 1
    try:
        result = candidate(word = "racecar") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "racecar") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "civic") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "civic") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "hellohellohellohello") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hellohellohellohello") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "alphanumericmappings") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alphanumericmappings") == 53: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 700: {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisateststring") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisateststring") == 47: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzwvutsrqponmlkjihgfedcba") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzwvutsrqponmlkjihgfedcba") == 95: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzz") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzz") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgabcdefgabcdefg") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgabcdefgabcdefg") == 105: {e}')
    
    total += 1
    try:
        result = candidate(word = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp") == 4656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp") == 4656: {e}')
    
    total += 1
    try:
        result = candidate(word = "level") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "level") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyzabcdefghijkl") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyzabcdefghijkl") == 84: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzxyz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzxyz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcdabcd") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcdabcd") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "banana") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "banana") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "deified") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "deified") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "thequickbrownfoxjumpsoverthelazydog") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thequickbrownfoxjumpsoverthelazydog") == 114: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrnopqrmnopqr") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrnopqrmnopqr") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "example") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "example") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklnmopqrstuvwxyz") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklnmopqrstuvwxyz") == 95: {e}')
    
    total += 1
    try:
        result = candidate(word = "supercalifragilisticexpialidocious") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "supercalifragilisticexpialidocious") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word = "kayak") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "kayak") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aquickbrownfoxjumpsoverthelazydog") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aquickbrownfoxjumpsoverthelazydog") == 106: {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisaverylongwordthatshouldhavemanydivisiblesubstrings") == 187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisaverylongwordthatshouldhavemanydivisiblesubstrings") == 187: {e}')
    
    total += 1
    try:
        result = candidate(word = "rotor") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rotor") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvmnopqrstuv") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvmnopqrstuv") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 222: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 4656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 4656: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnm") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnm") == 85: {e}')
    
    total += 1
    try:
        result = candidate(word = "divisibilitycheck") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "divisibilitycheck") == 38: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1378: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrst") == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrst") == 192: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababab") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababab") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 210: {e}')
    
    total += 1
    try:
        result = candidate(word = "perfectprogramming") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "perfectprogramming") == 43: {e}')
    
    total += 1
    try:
        result = candidate(word = "alibabacloud") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alibabacloud") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzxyzxyz") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzxyzxyz") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 266: {e}')
    
    total += 1
    try:
        result = candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis") == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis") == 134: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertypoiuzxcvbnmnbvcxzpoiuytrewq") == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertypoiuzxcvbnmnbvcxzpoiuytrewq") == 127: {e}')
    
    total += 1
    try:
        result = candidate(word = "xzyxzyxzy") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xzyxzyxzy") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "substring") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "substring") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababababababababababababababababababababababababababababababababababab") == 3570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababababababababababababababababababababababababababababababababababab") == 3570: {e}')
    
    total += 1
    try:
        result = candidate(word = "hellohellohello") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hellohellohello") == 34: {e}')
    
    total += 1
    try:
        result = candidate(word = "helloprogrammingworld") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "helloprogrammingworld") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghij") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghij") == 82: {e}')
    
    total += 1
    try:
        result = candidate(word = "pythonprogramming") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pythonprogramming") == 46: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 232: {e}')
    
    total += 1
    try:
        result = candidate(word = "xylophone") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xylophone") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "abracadabra") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abracadabra") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 903: {e}')
    
    total += 1
    try:
        result = candidate(word = "repeatedcharacterssssssss") == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repeatedcharacterssssssss") == 101: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabbbbccccdddd") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabbbbccccdddd") == 81: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababab") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababab") == 78: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabcxyzabcxyzabc") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabcxyzabcxyzabc") == 46: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "repeatedrepeatedrepeated") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repeatedrepeatedrepeated") == 61: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 224: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aaabbbccc") == 27
    assert candidate(word = "aaa") == 6
    assert candidate(word = "z") == 1
    assert candidate(word = "bdh") == 4
    assert candidate(word = "abcdefghij") == 22
    assert candidate(word = "asdf") == 6
    assert candidate(word = "zzz") == 6
    assert candidate(word = "world") == 10
    assert candidate(word = "zzzz") == 10
    assert candidate(word = "xyz") == 6
    assert candidate(word = "lmnopqrs") == 17
    assert candidate(word = "hello") == 7
    assert candidate(word = "qwertyuiop") == 25
    assert candidate(word = "abcd") == 6
    assert candidate(word = "abcdefg") == 14
    assert candidate(word = "abcabcabc") == 12
    assert candidate(word = "a") == 1
    assert candidate(word = "mnopqr") == 11
    assert candidate(word = "abc") == 4
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 95
    assert candidate(word = "programming") == 22
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 95
    assert candidate(word = "hellohellohellohellohello") == 66
    assert candidate(word = "noon") == 5
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzmnopqrstuvwxyzabcdefghij") == 380
    assert candidate(word = "divisible") == 18
    assert candidate(word = "bananabanana") == 34
    assert candidate(word = "mississippi") == 28
    assert candidate(word = "xzyxzyxzyxzy") == 78
    assert candidate(word = "amazingrace") == 31
    assert candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 60
    assert candidate(word = "racecar") == 14
    assert candidate(word = "civic") == 10
    assert candidate(word = "hellohellohellohello") == 50
    assert candidate(word = "alphanumericmappings") == 53
    assert candidate(word = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 700
    assert candidate(word = "thisisateststring") == 47
    assert candidate(word = "xyzwvutsrqponmlkjihgfedcba") == 95
    assert candidate(word = "zzzzzzzzzz") == 55
    assert candidate(word = "abcdefgabcdefgabcdefg") == 105
    assert candidate(word = "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp") == 4656
    assert candidate(word = "level") == 10
    assert candidate(word = "mnopqrstuvwxyzabcdefghijkl") == 84
    assert candidate(word = "xyzxyz") == 21
    assert candidate(word = "abcdabcdabcdabcd") == 24
    assert candidate(word = "banana") == 14
    assert candidate(word = "deified") == 16
    assert candidate(word = "thequickbrownfoxjumpsoverthelazydog") == 114
    assert candidate(word = "mnopqrnopqrmnopqr") == 64
    assert candidate(word = "example") == 12
    assert candidate(word = "abcdefghijklnmopqrstuvwxyz") == 95
    assert candidate(word = "supercalifragilisticexpialidocious") == 104
    assert candidate(word = "kayak") == 7
    assert candidate(word = "aquickbrownfoxjumpsoverthelazydog") == 106
    assert candidate(word = "thisisaverylongwordthatshouldhavemanydivisiblesubstrings") == 187
    assert candidate(word = "rotor") == 5
    assert candidate(word = "mnopqrstuvmnopqrstuv") == 52
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 222
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 4656
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm") == 85
    assert candidate(word = "divisibilitycheck") == 38
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1378
    assert candidate(word = "mnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrstopqrstmnopqrst") == 192
    assert candidate(word = "ababababab") == 55
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzz") == 210
    assert candidate(word = "perfectprogramming") == 43
    assert candidate(word = "alibabacloud") == 28
    assert candidate(word = "xyzxyzxyz") == 45
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 266
    assert candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis") == 134
    assert candidate(word = "qwertypoiuzxcvbnmnbvcxzpoiuytrewq") == 127
    assert candidate(word = "xzyxzyxzy") == 45
    assert candidate(word = "substring") == 20
    assert candidate(word = "abababababababababababababababababababababababababababababababababababababababababab") == 3570
    assert candidate(word = "hellohellohello") == 34
    assert candidate(word = "helloprogrammingworld") == 63
    assert candidate(word = "abcdefghijabcdefghijabcdefghij") == 82
    assert candidate(word = "pythonprogramming") == 46
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 232
    assert candidate(word = "xylophone") == 18
    assert candidate(word = "abracadabra") == 24
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 903
    assert candidate(word = "repeatedcharacterssssssss") == 101
    assert candidate(word = "aaaaabbbbccccdddd") == 81
    assert candidate(word = "abababababab") == 78
    assert candidate(word = "xyzabcxyzabcxyzabc") == 46
    assert candidate(word = "zzzzzz") == 21
    assert candidate(word = "repeatedrepeatedrepeated") == 61
    assert candidate(word = "abacabadabacaba") == 27
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 224


