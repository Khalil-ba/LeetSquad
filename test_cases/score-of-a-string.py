def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "python") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zaz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zaz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvut") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvut") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "qpqpqpqp") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpqpqpqp") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwerty") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwerty") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyui") == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyui") == 276: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkj") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkj") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "learning") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "learning") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "helloalibaba") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "helloalibaba") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithavarietyofcharacters") == 447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithavarietyofcharacters") == 447: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "code") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "code") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzyxwvutsrqponmlkjihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzyxwvutsrqponmlkjihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohellohello") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohellohello") == 93: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcda") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcda") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "data") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "data") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "challenge") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "challenge") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "artificial") == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "artificial") == 67: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstmnopqrstmnopqr") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstmnopqrstmnopqr") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellotherefriends") == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellotherefriends") == 119: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfoxjumpsoverthelazydog") == 282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfoxjumpsoverthelazydog") == 282: {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuvpqponmlkjihgfedcba") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuvpqponmlkjihgfedcba") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffff") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffff") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abczzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abczzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "science") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "science") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "thefiveboxingwizardsjumpquickly") == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thefiveboxingwizardsjumpquickly") == 295: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccdddddee") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccdddddee") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 212: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq") == 428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq") == 428: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazazazazazazazazazazazazazazazazazazazazaza") == 1225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazazazazazazazazazazazazazazazazazazazazaza") == 1225: {e}')
    
    total += 1
    try:
        result = candidate(s = "ejhjhehjhejhejhejhejhej") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ejhjhehjhejhejhejhejhej") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "developer") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "developer") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyza") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyza") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "solution") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "solution") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjasdlfkjsadlkfjasdlkfjasdlkfjasdlkfjsadlkfj") == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjasdlfkjsadlkfjasdlkfjasdlkfjasdlkfjsadlkfj") == 340: {e}')
    
    total += 1
    try:
        result = candidate(s = "qpwoeirutyalskdjfhgzmxcvbnm") == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpwoeirutyalskdjfhgzmxcvbnm") == 234: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfe_dcba") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfe_dcba") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "sdjfnwiehfuiwehfiuhweihufew") == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sdjfnwiehfuiwehfiuhweihufew") == 242: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithvariouscharacters") == 417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithvariouscharacters") == 417: {e}')
    
    total += 1
    try:
        result = candidate(s = "jfkienfehndsjdfhienfhisodfns") == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jfkienfehndsjdfhienfhisodfns") == 151: {e}')
    
    total += 1
    try:
        result = candidate(s = "intelligence") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "intelligence") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwen") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwen") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "alibabacloud") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alibabacloud") == 61: {e}')
    
    total += 1
    try:
        result = candidate(s = "fun") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fun") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothereitisacoldwinter") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothereitisacoldwinter") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "asciiisawesome") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "asciiisawesome") == 136: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertypoiuytrewq") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertypoiuytrewq") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "abczabcyabcbabczabcyabcbabcz") == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abczabcyabcbabczabcyabcbabcz") == 229: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatcontainsmanycharacters") == 461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatcontainsmanycharacters") == 461: {e}')
    
    total += 1
    try:
        result = candidate(s = "qazwsxedcrfvtgbyhnujmiklop") == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qazwsxedcrfvtgbyhnujmiklop") == 215: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmanycharacters") == 389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmanycharacters") == 389: {e}')
    
    total += 1
    try:
        result = candidate(s = "azbycxdwevfugthsijrkqlponm") == 314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "azbycxdwevfugthsijrkqlponm") == 314: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog") == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog") == 309: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstmnopqrst") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstmnopqrst") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "expert") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "expert") == 53: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
    assert candidate(s = "a") == 0
    assert candidate(s = "abracadabra") == 78
    assert candidate(s = "zzzz") == 0
    assert candidate(s = "zyx") == 2
    assert candidate(s = "mnopqr") == 5
    assert candidate(s = "python") == 34
    assert candidate(s = "aaa") == 0
    assert candidate(s = "abcdabcd") == 9
    assert candidate(s = "zzz") == 0
    assert candidate(s = "xyz") == 2
    assert candidate(s = "zaz") == 50
    assert candidate(s = "zyxwvut") == 6
    assert candidate(s = "abc") == 2
    assert candidate(s = "hello") == 13
    assert candidate(s = "aabbcc") == 2
    assert candidate(s = "mississippi") == 58
    assert candidate(s = "qpqpqpqp") == 7
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(s = "qwerty") == 44
    assert candidate(s = "aaaabbbbccccdddd") == 3
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyui") == 276
    assert candidate(s = "abcdabcdabcdabcdabcd") == 27
    assert candidate(s = "lkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkj") == 50
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 63
    assert candidate(s = "learning") == 49
    assert candidate(s = "helloalibaba") == 51
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 25
    assert candidate(s = "thisisaverylongstringwithavarietyofcharacters") == 447
    assert candidate(s = "abacabadabacaba") == 22
    assert candidate(s = "code") == 24
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzyxwvutsrqponmlkjihgfedcba") == 50
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 38
    assert candidate(s = "hellohellohellohellohello") == 93
    assert candidate(s = "abcdabcda") == 12
    assert candidate(s = "data") == 41
    assert candidate(s = "challenge") == 48
    assert candidate(s = "artificial") == 67
    assert candidate(s = "abcabcabcabc") == 14
    assert candidate(s = "mnopqrstmnopqrstmnopqr") == 33
    assert candidate(s = "hellotherefriends") == 119
    assert candidate(s = "quickbrownfoxjumpsoverthelazydog") == 282
    assert candidate(s = "qrstuvpqponmlkjihgfedcba") == 28
    assert candidate(s = "aaaabbbbccccddddeeeeffff") == 5
    assert candidate(s = "abczzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
    assert candidate(s = "science") == 48
    assert candidate(s = "thefiveboxingwizardsjumpquickly") == 295
    assert candidate(s = "aaaaabbbbbcccccdddddee") == 4
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 212
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq") == 428
    assert candidate(s = "zazazazazazazazazazazazazazazazazazazazazazazazaza") == 1225
    assert candidate(s = "ejhjhehjhejhejhejhejhej") == 69
    assert candidate(s = "developer") == 70
    assert candidate(s = "abababababababab") == 15
    assert candidate(s = "abcdefghijklmnopqrstuvwxyza") == 50
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 75
    assert candidate(s = "noon") == 2
    assert candidate(s = "solution") == 35
    assert candidate(s = "lkjasdlfkjsadlkfjasdlkfjasdlkfjasdlkfjsadlkfj") == 340
    assert candidate(s = "qpwoeirutyalskdjfhgzmxcvbnm") == 234
    assert candidate(s = "abcabcabcabcabcabc") == 22
    assert candidate(s = "abcdefgfe_dcba") == 22
    assert candidate(s = "algorithm") == 64
    assert candidate(s = "sdjfnwiehfuiwehfiuhweihufew") == 242
    assert candidate(s = "thisisaverylongstringwithvariouscharacters") == 417
    assert candidate(s = "jfkienfehndsjdfhienfhisodfns") == 151
    assert candidate(s = "intelligence") == 62
    assert candidate(s = "qwen") == 33
    assert candidate(s = "alibabacloud") == 61
    assert candidate(s = "fun") == 22
    assert candidate(s = "hellothereitisacoldwinter") == 210
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 25
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 25
    assert candidate(s = "asciiisawesome") == 136
    assert candidate(s = "programming") == 69
    assert candidate(s = "qwertypoiuytrewq") == 120
    assert candidate(s = "abczabcyabcbabczabcyabcbabcz") == 229
    assert candidate(s = "level") == 48
    assert candidate(s = "thisisaverylongstringthatcontainsmanycharacters") == 461
    assert candidate(s = "qazwsxedcrfvtgbyhnujmiklop") == 215
    assert candidate(s = "thisisaverylongstringwithmanycharacters") == 389
    assert candidate(s = "azbycxdwevfugthsijrkqlponm") == 314
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog") == 309
    assert candidate(s = "mnopqrstmnopqrst") == 21
    assert candidate(s = "abcdefg") == 6
    assert candidate(s = "expert") == 53


