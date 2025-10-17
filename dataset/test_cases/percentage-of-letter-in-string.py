def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "jjjj",letter = "k") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jjjj",letter = "k") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "foobar",letter = "o") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "foobar",letter = "o") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",letter = "i") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",letter = "i") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",letter = "y") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",letter = "y") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",letter = "a") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",letter = "a") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",letter = "l") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",letter = "l") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "world",letter = "d") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "world",letter = "d") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "b",letter = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "b",letter = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "solution",letter = "o") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "solution",letter = "o") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",letter = "b") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",letter = "b") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",letter = "a") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",letter = "a") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",letter = "h") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",letter = "h") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",letter = "b") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",letter = "b") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",letter = "c") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",letter = "c") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",letter = "a") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",letter = "a") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",letter = "x") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",letter = "x") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "characterization",letter = "c") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "characterization",letter = "c") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "examplewithrepeatedletterzzzz",letter = "z") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "examplewithrepeatedletterzzzz",letter = "z") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertypoiuytrewqasdfghjklzxcvbnmasdfghjklzxcvbnm",letter = "q") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertypoiuytrewqasdfghjklzxcvbnmasdfghjklzxcvbnm",letter = "q") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "oneletterone",letter = "n") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneletterone",letter = "n") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "parameter",letter = "r") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "parameter",letter = "r") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "alphabet",letter = "p") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alphabet",letter = "p") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "determinethepercentage",letter = "e") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "determinethepercentage",letter = "e") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",letter = "m") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",letter = "m") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "supercalifragilisticexpialidocious",letter = "i") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "supercalifragilisticexpialidocious",letter = "i") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",letter = "a") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",letter = "a") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "development",letter = "e") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "development",letter = "e") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",letter = "a") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",letter = "a") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",letter = "a") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",letter = "a") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",letter = "j") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",letter = "j") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "visualization",letter = "i") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "visualization",letter = "i") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",letter = "g") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",letter = "g") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "development",letter = "d") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "development",letter = "d") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "charactercounting",letter = "c") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "charactercounting",letter = "c") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "percentage",letter = "e") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "percentage",letter = "e") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "classification",letter = "f") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "classification",letter = "f") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "environment",letter = "n") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "environment",letter = "n") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",letter = "z") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",letter = "z") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "charactercountexample",letter = "e") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "charactercountexample",letter = "e") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "testtesttesttest",letter = "t") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testtesttesttest",letter = "t") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "computation",letter = "i") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "computation",letter = "i") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "performance",letter = "n") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "performance",letter = "n") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "understanding",letter = "d") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "understanding",letter = "d") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "consistencyiskey",letter = "i") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consistencyiskey",letter = "i") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyz",letter = "y") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyz",letter = "y") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",letter = "g") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",letter = "g") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "representation",letter = "r") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "representation",letter = "r") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "communication",letter = "m") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "communication",letter = "m") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",letter = "z") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",letter = "z") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",letter = "s") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",letter = "s") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithrandomcharacters",letter = "t") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithrandomcharacters",letter = "t") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "variable",letter = "b") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "variable",letter = "b") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "pythonprogramming",letter = "p") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pythonprogramming",letter = "p") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzz",letter = "z") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzz",letter = "z") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",letter = "a") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",letter = "a") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",letter = "m") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",letter = "m") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",letter = "p") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",letter = "p") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "characterization",letter = "t") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "characterization",letter = "t") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "synchronous",letter = "s") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "synchronous",letter = "s") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "congratulations",letter = "t") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "congratulations",letter = "t") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",letter = "x") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",letter = "x") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "example",letter = "a") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "example",letter = "a") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "development",letter = "l") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "development",letter = "l") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "averylongstringwithvariouscharacters",letter = "a") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "averylongstringwithvariouscharacters",letter = "a") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",letter = "z") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",letter = "z") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog",letter = "e") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog",letter = "e") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquecharacters",letter = "u") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquecharacters",letter = "u") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello world",letter = "l") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello world",letter = "l") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellotheregeneralkenobi",letter = "l") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellotheregeneralkenobi",letter = "l") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "asynchronous",letter = "y") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "asynchronous",letter = "y") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "helloalibabacloud",letter = "a") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "helloalibabacloud",letter = "a") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "mathematics",letter = "a") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mathematics",letter = "a") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "function",letter = "u") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "function",letter = "u") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "expression",letter = "s") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "expression",letter = "s") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatshouldtestthemaximumlengthoftheinputwhichisonehundredcharacters",letter = "s") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatshouldtestthemaximumlengthoftheinputwhichisonehundredcharacters",letter = "s") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjashdflkjhaskldjfhlasjdhflkajshdfjklsahjfdlkjahs",letter = "l") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjashdflkjhaskldjfhlasjdhflkajshdfjklsahjfdlkjahs",letter = "l") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxy",letter = "x") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxy",letter = "x") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "programminglanguage",letter = "g") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programminglanguage",letter = "g") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",letter = "m") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",letter = "m") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "percentageletter",letter = "t") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "percentageletter",letter = "t") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "encyclopedia",letter = "o") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "encyclopedia",letter = "o") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "alphanumericcharacters123",letter = "a") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alphanumericcharacters123",letter = "a") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringindeedtoseeifitworks",letter = "s") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringindeedtoseeifitworks",letter = "s") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "alphabet",letter = "z") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alphabet",letter = "z") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "programminglanguage",letter = "a") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programminglanguage",letter = "a") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "statistics",letter = "s") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "statistics",letter = "s") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",letter = "x") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",letter = "x") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "encyclopedia",letter = "e") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "encyclopedia",letter = "e") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "nolettersmatch",letter = "z") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nolettersmatch",letter = "z") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "elephant",letter = "l") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elephant",letter = "l") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "character",letter = "c") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "character",letter = "c") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",letter = "a") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",letter = "a") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "congratulations",letter = "o") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "congratulations",letter = "o") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithvariouscharacters",letter = "v") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithvariouscharacters",letter = "v") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",letter = "l") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",letter = "l") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",letter = "b") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",letter = "b") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "alabama",letter = "b") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alabama",letter = "b") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",letter = "z") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",letter = "z") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "sequence",letter = "q") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sequence",letter = "q") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",letter = "n") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",letter = "n") == 33: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "jjjj",letter = "k") == 0
    assert candidate(s = "foobar",letter = "o") == 33
    assert candidate(s = "mississippi",letter = "i") == 36
    assert candidate(s = "python",letter = "y") == 16
    assert candidate(s = "abcabcabc",letter = "a") == 33
    assert candidate(s = "hello",letter = "l") == 40
    assert candidate(s = "world",letter = "d") == 20
    assert candidate(s = "zzzz",letter = "z") == 100
    assert candidate(s = "b",letter = "a") == 0
    assert candidate(s = "solution",letter = "o") == 25
    assert candidate(s = "aaaaabbbbb",letter = "b") == 50
    assert candidate(s = "a",letter = "a") == 100
    assert candidate(s = "abcdefg",letter = "h") == 0
    assert candidate(s = "zzzzzz",letter = "z") == 100
    assert candidate(s = "aabbcc",letter = "b") == 33
    assert candidate(s = "aabbccddeeff",letter = "c") == 16
    assert candidate(s = "abcdefg",letter = "a") == 14
    assert candidate(s = "zzzzzzzzz",letter = "z") == 100
    assert candidate(s = "abcdefg",letter = "x") == 0
    assert candidate(s = "characterization",letter = "c") == 12
    assert candidate(s = "examplewithrepeatedletterzzzz",letter = "z") == 13
    assert candidate(s = "qwertypoiuytrewqasdfghjklzxcvbnmasdfghjklzxcvbnm",letter = "q") == 4
    assert candidate(s = "oneletterone",letter = "n") == 16
    assert candidate(s = "parameter",letter = "r") == 22
    assert candidate(s = "alphabet",letter = "p") == 12
    assert candidate(s = "determinethepercentage",letter = "e") == 31
    assert candidate(s = "programming",letter = "m") == 18
    assert candidate(s = "supercalifragilisticexpialidocious",letter = "i") == 20
    assert candidate(s = "abracadabra",letter = "a") == 45
    assert candidate(s = "development",letter = "e") == 27
    assert candidate(s = "abcdefghij",letter = "a") == 10
    assert candidate(s = "abcdefghijk",letter = "a") == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
    assert candidate(s = "abcdefghij",letter = "j") == 10
    assert candidate(s = "visualization",letter = "i") == 23
    assert candidate(s = "programming",letter = "g") == 18
    assert candidate(s = "development",letter = "d") == 9
    assert candidate(s = "charactercounting",letter = "c") == 17
    assert candidate(s = "percentage",letter = "e") == 30
    assert candidate(s = "classification",letter = "f") == 7
    assert candidate(s = "environment",letter = "n") == 27
    assert candidate(s = "xyz",letter = "z") == 33
    assert candidate(s = "charactercountexample",letter = "e") == 14
    assert candidate(s = "testtesttesttest",letter = "t") == 50
    assert candidate(s = "computation",letter = "i") == 9
    assert candidate(s = "performance",letter = "n") == 9
    assert candidate(s = "understanding",letter = "d") == 15
    assert candidate(s = "consistencyiskey",letter = "i") == 12
    assert candidate(s = "xyxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyzxzyzyz",letter = "y") == 33
    assert candidate(s = "algorithm",letter = "g") == 11
    assert candidate(s = "representation",letter = "r") == 14
    assert candidate(s = "communication",letter = "m") == 15
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",letter = "z") == 3
    assert candidate(s = "mississippi",letter = "s") == 36
    assert candidate(s = "thisisaverylongstringwithrandomcharacters",letter = "t") == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
    assert candidate(s = "variable",letter = "b") == 12
    assert candidate(s = "pythonprogramming",letter = "p") == 11
    assert candidate(s = "xyzzxyzz",letter = "z") == 50
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",letter = "a") == 3
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",letter = "m") == 3
    assert candidate(s = "xylophone",letter = "p") == 11
    assert candidate(s = "characterization",letter = "t") == 12
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",letter = "z") == 100
    assert candidate(s = "synchronous",letter = "s") == 18
    assert candidate(s = "congratulations",letter = "t") == 13
    assert candidate(s = "mississippi",letter = "x") == 0
    assert candidate(s = "example",letter = "a") == 14
    assert candidate(s = "development",letter = "l") == 9
    assert candidate(s = "averylongstringwithvariouscharacters",letter = "a") == 11
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",letter = "z") == 3
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",letter = "e") == 8
    assert candidate(s = "uniquecharacters",letter = "u") == 12
    assert candidate(s = "hello world",letter = "l") == 27
    assert candidate(s = "hellotheregeneralkenobi",letter = "l") == 13
    assert candidate(s = "asynchronous",letter = "y") == 8
    assert candidate(s = "helloalibabacloud",letter = "a") == 17
    assert candidate(s = "mathematics",letter = "a") == 18
    assert candidate(s = "function",letter = "u") == 12
    assert candidate(s = "expression",letter = "s") == 20
    assert candidate(s = "thisisaverylongstringthatshouldtestthemaximumlengthoftheinputwhichisonehundredcharacters",letter = "s") == 7
    assert candidate(s = "lkjashdflkjhaskldjfhlasjdhflkajshdfjklsahjfdlkjahs",letter = "l") == 14
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxy",letter = "x") == 50
    assert candidate(s = "programminglanguage",letter = "g") == 21
    assert candidate(s = "abcdefghij",letter = "m") == 0
    assert candidate(s = "percentageletter",letter = "t") == 18
    assert candidate(s = "encyclopedia",letter = "o") == 8
    assert candidate(s = "alphanumericcharacters123",letter = "a") == 16
    assert candidate(s = "thisisaverylongstringindeedtoseeifitworks",letter = "s") == 12
    assert candidate(s = "alphabet",letter = "z") == 0
    assert candidate(s = "programminglanguage",letter = "a") == 15
    assert candidate(s = "statistics",letter = "s") == 30
    assert candidate(s = "xylophone",letter = "x") == 11
    assert candidate(s = "encyclopedia",letter = "e") == 16
    assert candidate(s = "nolettersmatch",letter = "z") == 0
    assert candidate(s = "elephant",letter = "l") == 12
    assert candidate(s = "character",letter = "c") == 22
    assert candidate(s = "banana",letter = "a") == 50
    assert candidate(s = "congratulations",letter = "o") == 13
    assert candidate(s = "longstringwithvariouscharacters",letter = "v") == 3
    assert candidate(s = "algorithm",letter = "l") == 11
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",letter = "b") == 33
    assert candidate(s = "alabama",letter = "b") == 14
    assert candidate(s = "zzzzzzzzzz",letter = "z") == 100
    assert candidate(s = "sequence",letter = "q") == 12
    assert candidate(s = "banana",letter = "n") == 33


