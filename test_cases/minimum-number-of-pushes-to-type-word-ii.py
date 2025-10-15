def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkkllllllllllllmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnoooooooppppppppppppppppqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrsssssssssssssssstttttttttttttttttuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwxxxxxxxxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzz") == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkkllllllllllllmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnoooooooppppppppppppppppqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrsssssssssssssssstttttttttttttttttuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwxxxxxxxxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzz") == 499: {e}')
    
    total += 1
    try:
        result = candidate(word = "hellohellohellohellohellohellohellohellohellohello") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hellohellohellohellohellohellohellohellohellohello") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 88: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzxyzxyzxyz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzxyzxyzxyz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 198: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababababababababababab") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababababababababababab") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiiiiii") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiiiiii") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 98: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 168: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word = "ppppppppppppppppppppppppppppppppppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ppppppppppppppppppppppppppppppppppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippimississippimississippimississippi") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippimississippimississippimississippi") == 44: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 162: {e}')
    
    total += 1
    try:
        result = candidate(word = "loremipsumdolorsitametconsecteturadipiscingelitloremipsumdolorsitametconsecteturadipiscingelitloremipsumdolorsitametconsecteturadipiscingelit") == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "loremipsumdolorsitametconsecteturadipiscingelitloremipsumdolorsitametconsecteturadipiscingelitloremipsumdolorsitametconsecteturadipiscingelit") == 183: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzz") == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzz") == 79: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 143: {e}')
    
    total += 1
    try:
        result = candidate(word = "onelongwordwithoutrepetitionsonelongwordwithoutrepetitions") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "onelongwordwithoutrepetitionsonelongwordwithoutrepetitions") == 70: {e}')
    
    total += 1
    try:
        result = candidate(word = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == 130: {e}')
    
    total += 1
    try:
        result = candidate(word = "uniquelettersabcdefghijklmnopqrstuvwxyzuniqueletters") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uniquelettersabcdefghijklmnopqrstuvwxyzuniqueletters") == 84: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeffffffffggggggghhhhhhhh") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeffffffffggggggghhhhhhhh") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "nnnnneeeeffffddddeeeeffffddddddddddddeeeeeeeeeeeeeeeeffffffddddddddddddddeeeeeeeeeeeeeeeeffffffdddddddddddddeeeeeeeeeeeeee") == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nnnnneeeeffffddddeeeeffffddddddddddddeeeeeeeeeeeeeeeeffffffddddddddddddddeeeeeeeeeeeeeeeeffffffdddddddddddddeeeeeeeeeeeeee") == 122: {e}')
    
    total += 1
    try:
        result = candidate(word = "equalprobabilityabcdefghijklmnopqrstuvwxyz") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "equalprobabilityabcdefghijklmnopqrstuvwxyz") == 76: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzz") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzz") == 136: {e}')
    
    total += 1
    try:
        result = candidate(word = "ppppoooolllliiiihhhhggggffffeeeeeeeedddddccccbbbaaa") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ppppoooolllliiiihhhhggggffffeeeeeeeedddddccccbbbaaa") == 65: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 114: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 112: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnbvcxzvbnmzxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnm") == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnbvcxzvbnmzxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnm") == 102: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 225: {e}')
    
    total += 1
    try:
        result = candidate(word = "repeatedrepeatedrepeatedrepeatedrepeatedrepeated") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repeatedrepeatedrepeatedrepeatedrepeatedrepeated") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcdeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcdeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 112: {e}')
    
    total += 1
    try:
        result = candidate(word = "frequencydistributionfrequencydistribution") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "frequencydistributionfrequencydistribution") == 54: {e}')
    
    total += 1
    try:
        result = candidate(word = "programmingproblemsolvingprogramming") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "programmingproblemsolvingprogramming") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop") == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop") == 132: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippiissippiissippi") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippiissippiissippi") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 170: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 108: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 120: {e}')
    
    total += 1
    try:
        result = candidate(word = "frequentfrequentfrequentfrequentfrequentfrequentfrequentfrequentfrequentfrequent") == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "frequentfrequentfrequentfrequentfrequentfrequentfrequentfrequentfrequentfrequent") == 80: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(word = "abcde") == 5
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 56
    assert candidate(word = "mississippi") == 11
    assert candidate(word = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 52
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkkllllllllllllmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnoooooooppppppppppppppppqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrsssssssssssssssstttttttttttttttttuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwxxxxxxxxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzz") == 499
    assert candidate(word = "hellohellohellohellohellohellohellohellohellohello") == 50
    assert candidate(word = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 88
    assert candidate(word = "xyzxyzxyzxyz") == 12
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 56
    assert candidate(word = "a") == 1
    assert candidate(word = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 198
    assert candidate(word = "ababababababababababababababababababababab") == 42
    assert candidate(word = "aabbccddeeffgghhiiiiii") == 24
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 98
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 168
    assert candidate(word = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 104
    assert candidate(word = "ppppppppppppppppppppppppppppppppppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 104
    assert candidate(word = "mississippimississippimississippimississippi") == 44
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 162
    assert candidate(word = "loremipsumdolorsitametconsecteturadipiscingelitloremipsumdolorsitametconsecteturadipiscingelitloremipsumdolorsitametconsecteturadipiscingelit") == 183
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzz") == 79
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 143
    assert candidate(word = "onelongwordwithoutrepetitionsonelongwordwithoutrepetitions") == 70
    assert candidate(word = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == 130
    assert candidate(word = "uniquelettersabcdefghijklmnopqrstuvwxyzuniqueletters") == 84
    assert candidate(word = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeffffffffggggggghhhhhhhh") == 64
    assert candidate(word = "nnnnneeeeffffddddeeeeffffddddddddddddeeeeeeeeeeeeeeeeffffffddddddddddddddeeeeeeeeeeeeeeeeffffffdddddddddddddeeeeeeeeeeeeee") == 122
    assert candidate(word = "equalprobabilityabcdefghijklmnopqrstuvwxyz") == 76
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzz") == 136
    assert candidate(word = "ppppoooolllliiiihhhhggggffffeeeeeeeedddddccccbbbaaa") == 65
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 114
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 112
    assert candidate(word = "mnbvcxzvbnmzxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnmxcvbnm") == 102
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 225
    assert candidate(word = "repeatedrepeatedrepeatedrepeatedrepeatedrepeated") == 48
    assert candidate(word = "aabbcdeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 104
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 112
    assert candidate(word = "frequencydistributionfrequencydistribution") == 54
    assert candidate(word = "programmingproblemsolvingprogramming") == 42
    assert candidate(word = "qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop") == 132
    assert candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 56
    assert candidate(word = "mississippiissippiissippi") == 25
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 170
    assert candidate(word = "abcdefghijklnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 108
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 120
    assert candidate(word = "frequentfrequentfrequentfrequentfrequentfrequentfrequentfrequentfrequentfrequent") == 80


