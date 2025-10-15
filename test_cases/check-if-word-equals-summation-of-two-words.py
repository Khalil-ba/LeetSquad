def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(firstWord = "ij",secondWord = "ji",targetWord = "ii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ij",secondWord = "ji",targetWord = "ii") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "fgh",secondWord = "ghf",targetWord = "ggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "fgh",secondWord = "ghf",targetWord = "ggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ij",secondWord = "ji",targetWord = "jjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ij",secondWord = "ji",targetWord = "jjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "b",secondWord = "c",targetWord = "d") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "b",secondWord = "c",targetWord = "d") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "i",secondWord = "j",targetWord = "ji") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "i",secondWord = "j",targetWord = "ji") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ab",secondWord = "ba",targetWord = "bb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ab",secondWord = "ba",targetWord = "bb") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "j",secondWord = "j",targetWord = "i") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "j",secondWord = "j",targetWord = "i") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "a",secondWord = "a",targetWord = "b") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "a",secondWord = "a",targetWord = "b") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aaa",secondWord = "a",targetWord = "aab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aaa",secondWord = "a",targetWord = "aab") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aaa",secondWord = "a",targetWord = "aaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aaa",secondWord = "a",targetWord = "aaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "acb",secondWord = "cba",targetWord = "cdb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "acb",secondWord = "cba",targetWord = "cdb") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "j",secondWord = "j",targetWord = "jj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "j",secondWord = "j",targetWord = "jj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "acacacac",secondWord = "bdbdbdbd",targetWord = "cececece") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "acacacac",secondWord = "bdbdbdbd",targetWord = "cececece") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aaaabbbb",secondWord = "ccccdddd",targetWord = "aaaabbbbccccdddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aaaabbbb",secondWord = "ccccdddd",targetWord = "aaaabbbbccccdddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijijijij",secondWord = "jijijiji",targetWord = "jjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijijijij",secondWord = "jijijiji",targetWord = "jjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijijij",secondWord = "jijiji",targetWord = "jjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijijij",secondWord = "jijiji",targetWord = "jjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "j",secondWord = "jj",targetWord = "jjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "j",secondWord = "jj",targetWord = "jjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "aaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "aaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "babcbabcba",secondWord = "cbabcbabcb",targetWord = "bbbbbbaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "babcbabcba",secondWord = "cbabcbabcb",targetWord = "bbbbbbaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jihgfedcba",secondWord = "abcdefghij",targetWord = "aaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jihgfedcba",secondWord = "abcdefghij",targetWord = "aaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "jjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "jjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijkl",secondWord = "lkji",targetWord = "jjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijkl",secondWord = "lkji",targetWord = "jjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijijij",secondWord = "ijijij",targetWord = "jjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijijij",secondWord = "ijijij",targetWord = "jjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "hjihj",secondWord = "ihjih",targetWord = "jjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "hjihj",secondWord = "ihjih",targetWord = "jjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aabbcc",secondWord = "ddeeff",targetWord = "gggggh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aabbcc",secondWord = "ddeeff",targetWord = "gggggh") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "hhhhhhhh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "hhhhhhhh") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "babababa",secondWord = "babababa",targetWord = "cacacaca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "babababa",secondWord = "babababa",targetWord = "cacacaca") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aaa",secondWord = "bbb",targetWord = "ccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aaa",secondWord = "bbb",targetWord = "ccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "iiii",secondWord = "jjjj",targetWord = "jjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "iiii",secondWord = "jjjj",targetWord = "jjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghi",secondWord = "j",targetWord = "abcdefghij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghi",secondWord = "j",targetWord = "abcdefghij") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "jjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "jjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghijabcdefghij",secondWord = "abcdefghijabcdefghij",targetWord = "jjjjjjjjjjjjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghijabcdefghij",secondWord = "abcdefghijabcdefghij",targetWord = "jjjjjjjjjjjjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "aaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "aaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "abcdefghhgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "abcdefghhgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "ggggggggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "ggggggggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abc",secondWord = "def",targetWord = "defabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abc",secondWord = "def",targetWord = "defabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "abcdefghijj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "abcdefghijj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "aaaaaaaaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "aaaaaaaaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aabbccddeeff",secondWord = "ffeeddccbbaa",targetWord = "feebbaaccdd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aabbccddeeff",secondWord = "ffeeddccbbaa",targetWord = "feebbaaccdd") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "a",secondWord = "b",targetWord = "c") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "a",secondWord = "b",targetWord = "c") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "jjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "jjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcd",secondWord = "efgh",targetWord = "ijkl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcd",secondWord = "efgh",targetWord = "ijkl") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jjjjj",secondWord = "jjjjj",targetWord = "jjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jjjjj",secondWord = "jjjjj",targetWord = "jjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aaaaaaaa",secondWord = "bbbbbbbb",targetWord = "cccccccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aaaaaaaa",secondWord = "bbbbbbbb",targetWord = "cccccccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aabbccdd",secondWord = "dccbbaaa",targetWord = "dddddddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aabbccdd",secondWord = "dccbbaaa",targetWord = "dddddddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "iiiiiiiiii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "iiiiiiiiii") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcabcabc",secondWord = "cbacbacba",targetWord = "bbbcccbbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcabcabc",secondWord = "cbacbacba",targetWord = "bbbcccbbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "iiii",secondWord = "jjjj",targetWord = "jjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "iiii",secondWord = "jjjj",targetWord = "jjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghi",secondWord = "abcdefghj",targetWord = "jjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghi",secondWord = "abcdefghj",targetWord = "jjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijijijijij",secondWord = "jijijijiji",targetWord = "jjjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijijijijij",secondWord = "jijijijiji",targetWord = "jjjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcde",secondWord = "edcba",targetWord = "abcdeedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcde",secondWord = "edcba",targetWord = "abcdeedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijijijij",secondWord = "hghghghg",targetWord = "gggggggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijijijij",secondWord = "hghghghg",targetWord = "gggggggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghija",targetWord = "jjjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghija",targetWord = "jjjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jijij",secondWord = "ijiji",targetWord = "jjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jijij",secondWord = "ijiji",targetWord = "jjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "abcdefghijabcdefghij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "abcdefghijabcdefghij") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "ijijij",secondWord = "jijiji",targetWord = "jjjjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "ijijij",secondWord = "jijiji",targetWord = "jjjjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaab") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "abcdefghij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "abcdefghij") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaabbbbbbbbbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaabbbbbbbbbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghi",secondWord = "hgfedcba",targetWord = "jjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghi",secondWord = "hgfedcba",targetWord = "jjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jihgfedcba",secondWord = "abcdefghij",targetWord = "jjjjjjjjjj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jihgfedcba",secondWord = "abcdefghij",targetWord = "jjjjjjjjjj") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "ijijijijij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "ijijijijij") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jijijijijij",secondWord = "jijijijijij",targetWord = "jjjjjjjjjjjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jijijijijij",secondWord = "jijijijijij",targetWord = "jjjjjjjjjjjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aabbccddeeffgg",secondWord = "hhiijjkkllmm",targetWord = "jjjjjjjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aabbccddeeffgg",secondWord = "hhiijjkkllmm",targetWord = "jjjjjjjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaaab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaaab") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "jjjjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "jjjjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "abcde",secondWord = "edcba",targetWord = "jjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "abcde",secondWord = "edcba",targetWord = "jjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "hgfedcba",secondWord = "abcdefgh",targetWord = "iiiiiiii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "hgfedcba",secondWord = "abcdefgh",targetWord = "iiiiiiii") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jijij",secondWord = "ijiji",targetWord = "jjjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jijij",secondWord = "ijiji",targetWord = "jjjjj") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "j",secondWord = "ij",targetWord = "ji") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "j",secondWord = "ij",targetWord = "ji") == True: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "aabbccdd",secondWord = "ddeeffgg",targetWord = "hhiijjkk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "aabbccdd",secondWord = "ddeeffgg",targetWord = "hhiijjkk") == False: {e}')
    
    total += 1
    try:
        result = candidate(firstWord = "jij",secondWord = "iji",targetWord = "jjjj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstWord = "jij",secondWord = "iji",targetWord = "jjjj") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(firstWord = "ij",secondWord = "ji",targetWord = "ii") == False
    assert candidate(firstWord = "fgh",secondWord = "ghf",targetWord = "ggg") == False
    assert candidate(firstWord = "ij",secondWord = "ji",targetWord = "jjj") == False
    assert candidate(firstWord = "b",secondWord = "c",targetWord = "d") == True
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaa") == False
    assert candidate(firstWord = "i",secondWord = "j",targetWord = "ji") == False
    assert candidate(firstWord = "ab",secondWord = "ba",targetWord = "bb") == True
    assert candidate(firstWord = "j",secondWord = "j",targetWord = "i") == False
    assert candidate(firstWord = "a",secondWord = "a",targetWord = "b") == False
    assert candidate(firstWord = "aaa",secondWord = "a",targetWord = "aab") == False
    assert candidate(firstWord = "aaa",secondWord = "a",targetWord = "aaaa") == True
    assert candidate(firstWord = "acb",secondWord = "cba",targetWord = "cdb") == True
    assert candidate(firstWord = "j",secondWord = "j",targetWord = "jj") == False
    assert candidate(firstWord = "acacacac",secondWord = "bdbdbdbd",targetWord = "cececece") == False
    assert candidate(firstWord = "aaaabbbb",secondWord = "ccccdddd",targetWord = "aaaabbbbccccdddd") == False
    assert candidate(firstWord = "ijijijij",secondWord = "jijijiji",targetWord = "jjjjjjjjjj") == False
    assert candidate(firstWord = "ijijij",secondWord = "jijiji",targetWord = "jjjjjjjj") == False
    assert candidate(firstWord = "j",secondWord = "jj",targetWord = "jjj") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "aaaaaaaaaa") == False
    assert candidate(firstWord = "babcbabcba",secondWord = "cbabcbabcb",targetWord = "bbbbbbaaaa") == False
    assert candidate(firstWord = "jihgfedcba",secondWord = "abcdefghij",targetWord = "aaaaaaaaaa") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "jjjjjjjjjj") == False
    assert candidate(firstWord = "ijkl",secondWord = "lkji",targetWord = "jjjjjj") == False
    assert candidate(firstWord = "ijijij",secondWord = "ijijij",targetWord = "jjjjjjjj") == False
    assert candidate(firstWord = "hjihj",secondWord = "ihjih",targetWord = "jjjjj") == False
    assert candidate(firstWord = "aabbcc",secondWord = "ddeeff",targetWord = "gggggh") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "hhhhhhhh") == False
    assert candidate(firstWord = "babababa",secondWord = "babababa",targetWord = "cacacaca") == True
    assert candidate(firstWord = "aaa",secondWord = "bbb",targetWord = "ccc") == False
    assert candidate(firstWord = "iiii",secondWord = "jjjj",targetWord = "jjjjjjjj") == False
    assert candidate(firstWord = "abcdefghi",secondWord = "j",targetWord = "abcdefghij") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "jjjjjjjjj") == False
    assert candidate(firstWord = "abcdefghijabcdefghij",secondWord = "abcdefghijabcdefghij",targetWord = "jjjjjjjjjjjjjjjjjjjj") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "aaaaaaaaaa") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "abcdefghhgfedcba") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "ggggggggg") == False
    assert candidate(firstWord = "abc",secondWord = "def",targetWord = "defabc") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghi",targetWord = "abcdefghijj") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "abcdefgh",targetWord = "aaaaaaaaaaaaaaaa") == False
    assert candidate(firstWord = "aabbccddeeff",secondWord = "ffeeddccbbaa",targetWord = "feebbaaccdd") == False
    assert candidate(firstWord = "a",secondWord = "b",targetWord = "c") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "jjjjjjjj") == False
    assert candidate(firstWord = "abcd",secondWord = "efgh",targetWord = "ijkl") == False
    assert candidate(firstWord = "jjjjj",secondWord = "jjjjj",targetWord = "jjjjjjj") == False
    assert candidate(firstWord = "aaaaaaaa",secondWord = "bbbbbbbb",targetWord = "cccccccc") == False
    assert candidate(firstWord = "aabbccdd",secondWord = "dccbbaaa",targetWord = "dddddddd") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "iiiiiiiiii") == False
    assert candidate(firstWord = "abcabcabc",secondWord = "cbacbacba",targetWord = "bbbcccbbb") == False
    assert candidate(firstWord = "iiii",secondWord = "jjjj",targetWord = "jjjjjj") == False
    assert candidate(firstWord = "abcdefghi",secondWord = "abcdefghj",targetWord = "jjjjjjjjj") == False
    assert candidate(firstWord = "ijijijijij",secondWord = "jijijijiji",targetWord = "jjjjjjjjjjj") == False
    assert candidate(firstWord = "abcde",secondWord = "edcba",targetWord = "abcdeedcba") == False
    assert candidate(firstWord = "ijijijij",secondWord = "hghghghg",targetWord = "gggggggg") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghija",targetWord = "jjjjjjjjjjj") == False
    assert candidate(firstWord = "jijij",secondWord = "ijiji",targetWord = "jjjjjjj") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "abcdefghijabcdefghij") == False
    assert candidate(firstWord = "ijijij",secondWord = "jijiji",targetWord = "jjjjjjjjjjjj") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaab") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "abcdefghij") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaabbbbbbbbbb") == False
    assert candidate(firstWord = "abcdefghi",secondWord = "hgfedcba",targetWord = "jjjjjjjjj") == False
    assert candidate(firstWord = "jihgfedcba",secondWord = "abcdefghij",targetWord = "jjjjjjjjjj") == True
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "ijijijijij") == False
    assert candidate(firstWord = "jijijijijij",secondWord = "jijijijijij",targetWord = "jjjjjjjjjjjjjjjjjjj") == False
    assert candidate(firstWord = "aabbccddeeffgg",secondWord = "hhiijjkkllmm",targetWord = "jjjjjjjjjjjj") == False
    assert candidate(firstWord = "abcdefghij",secondWord = "abcdefghij",targetWord = "aaaaaaaaaaab") == False
    assert candidate(firstWord = "abcdefgh",secondWord = "hgfedcba",targetWord = "jjjjjjj") == False
    assert candidate(firstWord = "abcde",secondWord = "edcba",targetWord = "jjjjj") == False
    assert candidate(firstWord = "hgfedcba",secondWord = "abcdefgh",targetWord = "iiiiiiii") == False
    assert candidate(firstWord = "jijij",secondWord = "ijiji",targetWord = "jjjjj") == False
    assert candidate(firstWord = "j",secondWord = "ij",targetWord = "ji") == True
    assert candidate(firstWord = "aabbccdd",secondWord = "ddeeffgg",targetWord = "hhiijjkk") == False
    assert candidate(firstWord = "jij",secondWord = "iji",targetWord = "jjjj") == False


