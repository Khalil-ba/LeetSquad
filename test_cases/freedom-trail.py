def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(ring = "caotmcaataijjxi",key = "oatjiioijjjxxxcx") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "caotmcaataijjxi",key = "oatjiioijjjxxxcx") == 42: {e}')
    
    total += 1
    try:
        result = candidate(ring = "godding",key = "gd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "godding",key = "gd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(ring = "pqwcx",key = "cpqwx") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "pqwcx",key = "cpqwx") == 13: {e}')
    
    total += 1
    try:
        result = candidate(ring = "edcba",key = "abc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "edcba",key = "abc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(ring = "ababcabc",key = "abc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "ababcabc",key = "abc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(ring = "iotfo",key = "fio") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "iotfo",key = "fio") == 8: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "zyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "zyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(ring = "iaadddfef",key = "dd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "iaadddfef",key = "dd") == 5: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "cba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "cba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefg",key = "fa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefg",key = "fa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(ring = "iaejfhfihjdghfihdddddddhddcfjghjgddf",key = "did") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "iaejfhfihjdghfihdddddddhddcfjghjgddf",key = "did") == 9: {e}')
    
    total += 1
    try:
        result = candidate(ring = "xyxzyzyxy",key = "xzyxz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "xyxzyzyxy",key = "xzyxz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(ring = "godding",key = "godding") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "godding",key = "godding") == 13: {e}')
    
    total += 1
    try:
        result = candidate(ring = "caotmcaataijjxi",key = "oatjiioijia") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "caotmcaataijjxi",key = "oatjiioijia") == 35: {e}')
    
    total += 1
    try:
        result = candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 66: {e}')
    
    total += 1
    try:
        result = candidate(ring = "lkjhgfedcbazyxwvutsrqponml",key = "abcdefghijklmnopqrstuvwxyz") == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "lkjhgfedcbazyxwvutsrqponml",key = "abcdefghijklmnopqrstuvwxyz") == inf: {e}')
    
    total += 1
    try:
        result = candidate(ring = "mississippi",key = "ppiiisssmm") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "mississippi",key = "ppiiisssmm") == 18: {e}')
    
    total += 1
    try:
        result = candidate(ring = "uniquecharacters",key = "unique") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "uniquecharacters",key = "unique") == 11: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zyxwvutsrqponmlkjihgfedcba") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zyxwvutsrqponmlkjihgfedcba") == 77: {e}')
    
    total += 1
    try:
        result = candidate(ring = "mississippi",key = "missis") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "mississippi",key = "missis") == 10: {e}')
    
    total += 1
    try:
        result = candidate(ring = "noonnoonnoonnoonnoonnoon",key = "noonnoon") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "noonnoonnoonnoonnoonnoon",key = "noonnoon") == 12: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abacabadabacabadabacabadabacabad",key = "badabadabacaba") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abacabadabacabadabacabadabacabad",key = "badabadabacaba") == 28: {e}')
    
    total += 1
    try:
        result = candidate(ring = "thistimeitsshouldbeaveryunusualring",key = "unusualring") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "thistimeitsshouldbeaveryunusualring",key = "unusualring") == 30: {e}')
    
    total += 1
    try:
        result = candidate(ring = "thisisaverylongringwithmanysamecharacters",key = "thisisaverylongring") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "thisisaverylongringwithmanysamecharacters",key = "thisisaverylongring") == 37: {e}')
    
    total += 1
    try:
        result = candidate(ring = "encyclopedia",key = "pediaencyclopedia") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "encyclopedia",key = "pediaencyclopedia") == 38: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",key = "ac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",key = "ac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(ring = "rotor",key = "rotorrotor") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "rotor",key = "rotorrotor") == 18: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg",key = "gfedcba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg",key = "gfedcba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",key = "zzzaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",key = "zzzaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",key = "zyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",key = "zyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abababababababababab",key = "bababa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abababababababababab",key = "bababa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abacabadabacaba",key = "abcabcabc") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abacabadabacaba",key = "abcabcabc") == 20: {e}')
    
    total += 1
    try:
        result = candidate(ring = "rhythms",key = "rhythmrhythmsrhythmrhythms") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "rhythms",key = "rhythmrhythmsrhythmrhythms") == 53: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijklmnopqrstuvwxyzaabcdefghijklmnopqrstuvwxyza",key = "abcdefghijklmnopqrstuvwxyz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijklmnopqrstuvwxyzaabcdefghijklmnopqrstuvwxyza",key = "abcdefghijklmnopqrstuvwxyz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(ring = "floccinaucinihilipilification",key = "floccinaucinihilipilification") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "floccinaucinihilipilification",key = "floccinaucinihilipilification") == 57: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijabcdefghijabcdefghij",key = "jjiihhggffeeddccba") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijabcdefghijabcdefghij",key = "jjiihhggffeeddccba") == 28: {e}')
    
    total += 1
    try:
        result = candidate(ring = "bcaacbcaacbcaac",key = "abcabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "bcaacbcaacbcaac",key = "abcabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(ring = "qwertyuiopasdfghjklzxcvbnm",key = "lkjhgfdsa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "qwertyuiopasdfghjklzxcvbnm",key = "lkjhgfdsa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcabcabcabcabcabcabcabc",key = "abcabcabc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcabcabcabcabcabcabcabc",key = "abcabcabc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(ring = "ringwithrepeatedcharactersrrrr",key = "ringwithrepeatedcharacters") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "ringwithrepeatedcharactersrrrr",key = "ringwithrepeatedcharacters") == 51: {e}')
    
    total += 1
    try:
        result = candidate(ring = "repetition",key = "rep") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "repetition",key = "rep") == 5: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefgabcdefgabcdefgabcdefgabcdefg",key = "abcdefgabcdefgabcdefgabcdefg") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefgabcdefgabcdefgabcdefgabcdefg",key = "abcdefgabcdefgabcdefgabcdefg") == 55: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zzzyyxxwvuttsrqponmlkjihgfedcba") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zzzyyxxwvuttsrqponmlkjihgfedcba") == 82: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zzyyxxwvuttsrqponmlkjihgfedcba") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zzyyxxwvuttsrqponmlkjihgfedcba") == 81: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abracadabra",key = "abcabcabc") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abracadabra",key = "abcabcabc") == 25: {e}')
    
    total += 1
    try:
        result = candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",key = "programming") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",key = "programming") == 87: {e}')
    
    total += 1
    try:
        result = candidate(ring = "thisisaverylongstringthatweneedtocheckanditsrepeatedthisisaverylongstringthatweneedtocheck",key = "check") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "thisisaverylongstringthatweneedtocheckanditsrepeatedthisisaverylongstringthatweneedtocheck",key = "check") == 12: {e}')
    
    total += 1
    try:
        result = candidate(ring = "thisisaverylongstringthatweneedtocheck",key = "string") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "thisisaverylongstringthatweneedtocheck",key = "string") == 26: {e}')
    
    total += 1
    try:
        result = candidate(ring = "rhythm",key = "myrhth") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "rhythm",key = "myrhth") == 16: {e}')
    
    total += 1
    try:
        result = candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(ring = "pqrsyzxcvbnmlkjhgfedwatpoiuy",key = "python") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "pqrsyzxcvbnmlkjhgfedwatpoiuy",key = "python") == 42: {e}')
    
    total += 1
    try:
        result = candidate(ring = "mnbvcxzlkjhgfdsapoiuytrewq",key = "qwertyuiop") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "mnbvcxzlkjhgfdsapoiuytrewq",key = "qwertyuiop") == 20: {e}')
    
    total += 1
    try:
        result = candidate(ring = "mississippi",key = "mississippimississippi") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "mississippi",key = "mississippimississippi") == 41: {e}')
    
    total += 1
    try:
        result = candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",key = "mnbvcxzlkjhgfdsapoiuytrewq") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",key = "mnbvcxzlkjhgfdsapoiuytrewq") == 52: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefgabcdefgabcdefgabcdefg",key = "aceg") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefgabcdefgabcdefgabcdefg",key = "aceg") == 10: {e}')
    
    total += 1
    try:
        result = candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(ring = "repeatedrepeatedrepeated",key = "repeat") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "repeatedrepeatedrepeated",key = "repeat") == 11: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aaabbbcccdddeeefffggghhhiii",key = "abcdefghi") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aaabbbcccdddeeefffggghhhiii",key = "abcdefghi") == 33: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiii",key = "abcdefghi") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiii",key = "abcdefghi") == 49: {e}')
    
    total += 1
    try:
        result = candidate(ring = "rotorrotorrotor",key = "rotor") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "rotorrotorrotor",key = "rotor") == 9: {e}')
    
    total += 1
    try:
        result = candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",key = "qzam") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",key = "qzam") == 31: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "abcdefghijklmnopqrstuvwxyz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "abcdefghijklmnopqrstuvwxyz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aaabbbbccccddddeeeeffffgggg",key = "abcdefg") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aaabbbbccccddddeeeeffffgggg",key = "abcdefg") == 30: {e}')
    
    total += 1
    try:
        result = candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 60: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef",key = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef",key = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 83: {e}')
    
    total += 1
    try:
        result = candidate(ring = "abacabadabacabadabacabad",key = "abad") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "abacabadabacabadabacabad",key = "abad") == 7: {e}')
    
    total += 1
    try:
        result = candidate(ring = "lmnopqrstuvwxyzabcdefghijkl",key = "key") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "lmnopqrstuvwxyzabcdefghijkl",key = "key") == 17: {e}')
    
    total += 1
    try:
        result = candidate(ring = "xylophone",key = "oxylphoen") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "xylophone",key = "oxylphoen") == 24: {e}')
    
    total += 1
    try:
        result = candidate(ring = "aaaaabbbbcccccdddddeeeeeffffffggggghhhhhhiiiiijjjjjjkkkkkkllllllmmmmmmnnnnnnooooooppppppqqqqqqrrrrrrssssssttttttuuuuuuvvvvvvwwwwwwwxxxxxxxxxyyyyyyyzzzzzzz",key = "zyxwvutsrqponmlkjihgfedcba") == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "aaaaabbbbcccccdddddeeeeeffffffggggghhhhhhiiiiijjjjjjkkkkkkllllllmmmmmmnnnnnnooooooppppppqqqqqqrrrrrrssssssttttttuuuuuuvvvvvvwwwwwwwxxxxxxxxxyyyyyyyzzzzzzz",key = "zyxwvutsrqponmlkjihgfedcba") == 176: {e}')
    
    total += 1
    try:
        result = candidate(ring = "mississippi",key = "issi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ring = "mississippi",key = "issi") == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(ring = "caotmcaataijjxi",key = "oatjiioijjjxxxcx") == 42
    assert candidate(ring = "godding",key = "gd") == 4
    assert candidate(ring = "pqwcx",key = "cpqwx") == 13
    assert candidate(ring = "edcba",key = "abc") == 6
    assert candidate(ring = "ababcabc",key = "abc") == 6
    assert candidate(ring = "iotfo",key = "fio") == 8
    assert candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "zyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(ring = "iaadddfef",key = "dd") == 5
    assert candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "cba") == 7
    assert candidate(ring = "abcdefg",key = "fa") == 6
    assert candidate(ring = "iaejfhfihjdghfihdddddddhddcfjghjgddf",key = "did") == 9
    assert candidate(ring = "xyxzyzyxy",key = "xzyxz") == 12
    assert candidate(ring = "godding",key = "godding") == 13
    assert candidate(ring = "caotmcaataijjxi",key = "oatjiioijia") == 35
    assert candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 66
    assert candidate(ring = "lkjhgfedcbazyxwvutsrqponml",key = "abcdefghijklmnopqrstuvwxyz") == inf
    assert candidate(ring = "mississippi",key = "ppiiisssmm") == 18
    assert candidate(ring = "uniquecharacters",key = "unique") == 11
    assert candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zyxwvutsrqponmlkjihgfedcba") == 77
    assert candidate(ring = "mississippi",key = "missis") == 10
    assert candidate(ring = "noonnoonnoonnoonnoonnoon",key = "noonnoon") == 12
    assert candidate(ring = "abacabadabacabadabacabadabacabad",key = "badabadabacaba") == 28
    assert candidate(ring = "thistimeitsshouldbeaveryunusualring",key = "unusualring") == 30
    assert candidate(ring = "thisisaverylongringwithmanysamecharacters",key = "thisisaverylongring") == 37
    assert candidate(ring = "encyclopedia",key = "pediaencyclopedia") == 38
    assert candidate(ring = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",key = "ac") == 3
    assert candidate(ring = "rotor",key = "rotorrotor") == 18
    assert candidate(ring = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg",key = "gfedcba") == 14
    assert candidate(ring = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",key = "zzzaa") == 7
    assert candidate(ring = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",key = "zyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(ring = "abababababababababab",key = "bababa") == 12
    assert candidate(ring = "abacabadabacaba",key = "abcabcabc") == 20
    assert candidate(ring = "rhythms",key = "rhythmrhythmsrhythmrhythms") == 53
    assert candidate(ring = "abcdefghijklmnopqrstuvwxyzaabcdefghijklmnopqrstuvwxyza",key = "abcdefghijklmnopqrstuvwxyz") == 51
    assert candidate(ring = "floccinaucinihilipilification",key = "floccinaucinihilipilification") == 57
    assert candidate(ring = "abcdefghijabcdefghijabcdefghij",key = "jjiihhggffeeddccba") == 28
    assert candidate(ring = "bcaacbcaacbcaac",key = "abcabc") == 15
    assert candidate(ring = "qwertyuiopasdfghjklzxcvbnm",key = "lkjhgfdsa") == 25
    assert candidate(ring = "abcabcabcabcabcabcabcabc",key = "abcabcabc") == 17
    assert candidate(ring = "ringwithrepeatedcharactersrrrr",key = "ringwithrepeatedcharacters") == 51
    assert candidate(ring = "repetition",key = "rep") == 5
    assert candidate(ring = "abcdefgabcdefgabcdefgabcdefgabcdefg",key = "abcdefgabcdefgabcdefgabcdefg") == 55
    assert candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zzzyyxxwvuttsrqponmlkjihgfedcba") == 82
    assert candidate(ring = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",key = "zzyyxxwvuttsrqponmlkjihgfedcba") == 81
    assert candidate(ring = "abracadabra",key = "abcabcabc") == 25
    assert candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",key = "programming") == 87
    assert candidate(ring = "thisisaverylongstringthatweneedtocheckanditsrepeatedthisisaverylongstringthatweneedtocheck",key = "check") == 12
    assert candidate(ring = "thisisaverylongstringthatweneedtocheck",key = "string") == 26
    assert candidate(ring = "rhythm",key = "myrhth") == 16
    assert candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(ring = "pqrsyzxcvbnmlkjhgfedwatpoiuy",key = "python") == 42
    assert candidate(ring = "mnbvcxzlkjhgfdsapoiuytrewq",key = "qwertyuiop") == 20
    assert candidate(ring = "mississippi",key = "mississippimississippi") == 41
    assert candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",key = "mnbvcxzlkjhgfdsapoiuytrewq") == 52
    assert candidate(ring = "abcdefgabcdefgabcdefgabcdefg",key = "aceg") == 10
    assert candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzz") == 3
    assert candidate(ring = "repeatedrepeatedrepeated",key = "repeat") == 11
    assert candidate(ring = "aaabbbcccdddeeefffggghhhiii",key = "abcdefghi") == 33
    assert candidate(ring = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiii",key = "abcdefghi") == 49
    assert candidate(ring = "rotorrotorrotor",key = "rotor") == 9
    assert candidate(ring = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",key = "qzam") == 31
    assert candidate(ring = "abcdefghijklmnopqrstuvwxyz",key = "abcdefghijklmnopqrstuvwxyz") == 51
    assert candidate(ring = "aaabbbbccccddddeeeeffffgggg",key = "abcdefg") == 30
    assert candidate(ring = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 60
    assert candidate(ring = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef",key = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 83
    assert candidate(ring = "abacabadabacabadabacabad",key = "abad") == 7
    assert candidate(ring = "lmnopqrstuvwxyzabcdefghijkl",key = "key") == 17
    assert candidate(ring = "xylophone",key = "oxylphoen") == 24
    assert candidate(ring = "aaaaabbbbcccccdddddeeeeeffffffggggghhhhhhiiiiijjjjjjkkkkkkllllllmmmmmmnnnnnnooooooppppppqqqqqqrrrrrrssssssttttttuuuuuuvvvvvvwwwwwwwxxxxxxxxxyyyyyyyzzzzzzz",key = "zyxwvutsrqponmlkjihgfedcba") == 176
    assert candidate(ring = "mississippi",key = "issi") == 7


