def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzz",c = "z") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",c = "z") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",c = "b") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",c = "b") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",c = "f") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",c = "f") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "",c = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",c = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",c = "a") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",c = "a") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",c = "l") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",c = "l") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",c = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",c = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa",c = "a") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa",c = "a") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",c = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",c = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",c = "c") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",c = "c") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",c = "a") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",c = "a") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abada",c = "a") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abada",c = "a") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",c = "i") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",c = "i") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "lalalalalalalala",c = "l") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lalalalalalalala",c = "l") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaacaaadaaae",c = "e") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaacaaadaaae",c = "e") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcb",c = "b") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcb",c = "b") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",c = "f") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",c = "f") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjkljkljkljklj",c = "k") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjkljkljkljklj",c = "k") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharactersrepeatedcharacters",c = "r") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharactersrepeatedcharacters",c = "r") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbcbcbc",c = "b") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbcbcbc",c = "b") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacbacbac",c = "a") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacbacbac",c = "a") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",c = "r") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",c = "r") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababa",c = "b") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababa",c = "b") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyzxzyz",c = "z") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyzxzyz",c = "z") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppppp",c = "p") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppppp",c = "p") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",c = "j") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",c = "j") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrsrqpqrsrqpqrs",c = "r") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrsrqpqrsrqpqrs",c = "r") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "bookkeeper",c = "e") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bookkeeper",c = "e") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbcccddd",c = "b") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbcccddd",c = "b") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon",c = "n") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon",c = "n") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxzyxzyxzyx",c = "y") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxzyxzyxzyx",c = "y") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaa",c = "a") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaa",c = "a") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",c = "g") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",c = "g") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",c = "a") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",c = "a") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "z") == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "z") == 990: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbaabbaa",c = "b") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbaabbaa",c = "b") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",c = "m") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",c = "m") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananabananabanana",c = "a") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananabananabanana",c = "a") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",c = "b") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",c = "b") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",c = "a") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",c = "a") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaa",c = "a") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaa",c = "a") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiop",c = "q") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiop",c = "q") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",c = "b") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",c = "b") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxzyx",c = "x") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxzyx",c = "x") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",c = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",c = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzz",c = "z") == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzz",c = "z") == 153: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",c = "o") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",c = "o") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",c = "o") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",c = "o") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg",c = "d") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg",c = "d") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqwweerrttyyuuiioopp",c = "q") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqwweerrttyyuuiioopp",c = "q") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacabaa",c = "a") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacabaa",c = "a") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjlkjlkjlkj",c = "l") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjlkjlkjlkj",c = "l") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaa",c = "a") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaa",c = "a") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",c = "d") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",c = "d") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",c = "c") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",c = "c") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcde",c = "d") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcde",c = "d") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbb",c = "b") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbb",c = "b") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "ananananananananana",c = "n") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ananananananananana",c = "n") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcababcabcab",c = "b") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcababcabcab",c = "b") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",c = "a") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",c = "a") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzxyxzyzx",c = "x") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzxyxzyzx",c = "x") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",c = "a") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",c = "a") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellobyehello",c = "o") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellobyehello",c = "o") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzz",c = "z") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzz",c = "z") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "aninterestingproblem",c = "n") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aninterestingproblem",c = "n") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",c = "i") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",c = "i") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "llllllllllllllllllllllllll",c = "l") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "llllllllllllllllllllllllll",c = "l") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcb",c = "b") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcb",c = "b") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababa",c = "b") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababa",c = "b") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghefghijklmnopqrstuvwxyz",c = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghefghijklmnopqrstuvwxyz",c = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",c = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",c = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaaa",c = "a") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaaa",c = "a") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "q") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "q") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",c = "j") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",c = "j") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithseveralcharacters",c = "t") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithseveralcharacters",c = "t") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyzxzyzxzyz",c = "z") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyzxzyzxzyz",c = "z") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",c = "z") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",c = "z") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzxzyzx",c = "x") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzxzyzx",c = "x") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "z") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "z") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",c = "x") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",c = "x") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadaba",c = "a") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadaba",c = "a") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",c = "m") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",c = "m") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa",c = "a") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa",c = "a") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "anananananan",c = "a") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anananananan",c = "a") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccc",c = "c") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccc",c = "c") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccc",c = "c") == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccc",c = "c") == 171: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",c = "z") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",c = "z") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazaz",c = "z") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazaz",c = "z") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "z") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "z") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaacaaadaaae",c = "a") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaacaaadaaae",c = "a") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbc",c = "b") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbc",c = "b") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff",c = "d") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff",c = "d") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",c = "f") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",c = "f") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",c = "a") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",c = "a") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaa",c = "a") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaa",c = "a") == 105: {e}')
    
    total += 1
    try:
        result = candidate(s = "popcornpopcorn",c = "p") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "popcornpopcorn",c = "p") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxy",c = "x") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxy",c = "x") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbbbbb",c = "b") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbbbbb",c = "b") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",c = "g") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",c = "g") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohello",c = "l") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohello",c = "l") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde",c = "a") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde",c = "a") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefhijklmnopqrstuvwxyz",c = "z") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefhijklmnopqrstuvwxyz",c = "z") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",c = "b") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",c = "b") == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzz",c = "z") == 6
    assert candidate(s = "abcabcabc",c = "b") == 6
    assert candidate(s = "abcdefg",c = "f") == 1
    assert candidate(s = "",c = "a") == 0
    assert candidate(s = "abcabcabc",c = "a") == 6
    assert candidate(s = "hello",c = "l") == 3
    assert candidate(s = "xyz",c = "a") == 0
    assert candidate(s = "aaaaa",c = "a") == 15
    assert candidate(s = "abc",c = "a") == 1
    assert candidate(s = "abcabcabc",c = "c") == 6
    assert candidate(s = "aaa",c = "a") == 6
    assert candidate(s = "abada",c = "a") == 6
    assert candidate(s = "mississippi",c = "i") == 10
    assert candidate(s = "lalalalalalalala",c = "l") == 36
    assert candidate(s = "aabaaacaaadaaae",c = "e") == 1
    assert candidate(s = "bcbcbcbcb",c = "b") == 15
    assert candidate(s = "aabbccddeeff",c = "f") == 3
    assert candidate(s = "lkjkljkljkljklj",c = "k") == 15
    assert candidate(s = "repeatedcharactersrepeatedcharacters",c = "r") == 21
    assert candidate(s = "abcbcbcbc",c = "b") == 10
    assert candidate(s = "acbacbacbacbacbac",c = "a") == 21
    assert candidate(s = "racecar",c = "r") == 3
    assert candidate(s = "abababababa",c = "b") == 15
    assert candidate(s = "xyzzyxzyzxzyz",c = "z") == 21
    assert candidate(s = "pppppppppppp",c = "p") == 78
    assert candidate(s = "abcdefghijk",c = "j") == 1
    assert candidate(s = "pqrsrqpqrsrqpqrs",c = "r") == 15
    assert candidate(s = "bookkeeper",c = "e") == 6
    assert candidate(s = "aaaabbbcccddd",c = "b") == 6
    assert candidate(s = "noonnoonnoon",c = "n") == 21
    assert candidate(s = "xyxzyxzyxzyxzyx",c = "y") == 15
    assert candidate(s = "aaaaabaaaa",c = "a") == 45
    assert candidate(s = "aabbccddeeffgg",c = "g") == 3
    assert candidate(s = "banana",c = "a") == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "z") == 990
    assert candidate(s = "bbaabbaabbaa",c = "b") == 21
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",c = "m") == 3
    assert candidate(s = "bananabananabanana",c = "a") == 45
    assert candidate(s = "aabbccddeeffgg",c = "b") == 3
    assert candidate(s = "abacabadabacaba",c = "a") == 36
    assert candidate(s = "aaaaabaaa",c = "a") == 36
    assert candidate(s = "qwertyuiop",c = "q") == 1
    assert candidate(s = "ababababab",c = "b") == 15
    assert candidate(s = "xyxzyxzyx",c = "x") == 10
    assert candidate(s = "abcdefghij",c = "a") == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzz",c = "z") == 153
    assert candidate(s = "hellohellohello",c = "o") == 6
    assert candidate(s = "hello",c = "o") == 1
    assert candidate(s = "abcdefgabcdefgabcdefg",c = "d") == 6
    assert candidate(s = "qqwweerrttyyuuiioopp",c = "q") == 3
    assert candidate(s = "aabacabaa",c = "a") == 21
    assert candidate(s = "lkjlkjlkjlkj",c = "l") == 10
    assert candidate(s = "aaabaaaabaaaa",c = "a") == 66
    assert candidate(s = "aabbccddeeff",c = "d") == 3
    assert candidate(s = "aabbccddeeff",c = "c") == 3
    assert candidate(s = "abcdabcde",c = "d") == 3
    assert candidate(s = "aaaaabbbbbb",c = "b") == 21
    assert candidate(s = "ananananananananana",c = "n") == 45
    assert candidate(s = "abcababcabcab",c = "b") == 15
    assert candidate(s = "abacaba",c = "a") == 10
    assert candidate(s = "xyxzxyxzyzx",c = "x") == 15
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",c = "a") == 351
    assert candidate(s = "hellohellobyehello",c = "o") == 6
    assert candidate(s = "zzzzzzzzzzzzz",c = "z") == 91
    assert candidate(s = "aninterestingproblem",c = "n") == 6
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",c = "i") == 6
    assert candidate(s = "llllllllllllllllllllllllll",c = "l") == 351
    assert candidate(s = "bcbcbcbcbcb",c = "b") == 21
    assert candidate(s = "bababababababa",c = "b") == 28
    assert candidate(s = "abcdefghefghijklmnopqrstuvwxyz",c = "a") == 1
    assert candidate(s = "abcdefghi",c = "a") == 1
    assert candidate(s = "aaaaabaaaaa",c = "a") == 55
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "q") == 3
    assert candidate(s = "abcdefghij",c = "j") == 1
    assert candidate(s = "thisisaverylongstringwithseveralcharacters",c = "t") == 10
    assert candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "a") == 1
    assert candidate(s = "xyzzzyzxzyzxzyz",c = "z") == 36
    assert candidate(s = "zzzzzzzzzz",c = "z") == 55
    assert candidate(s = "xyzyxzyzxzyzx",c = "x") == 10
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "z") == 3
    assert candidate(s = "xyzxyzxyzxyz",c = "x") == 10
    assert candidate(s = "abacabadaba",c = "a") == 21
    assert candidate(s = "programming",c = "m") == 3
    assert candidate(s = "aaabaaa",c = "a") == 21
    assert candidate(s = "anananananan",c = "a") == 21
    assert candidate(s = "cccccccccc",c = "c") == 55
    assert candidate(s = "cccccccccccccccccc",c = "c") == 171
    assert candidate(s = "xyzxyzxyz",c = "z") == 6
    assert candidate(s = "zazazazazaz",c = "z") == 21
    assert candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "z") == 1
    assert candidate(s = "aabaaacaaadaaae",c = "a") == 66
    assert candidate(s = "bcbcbcbc",c = "b") == 10
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "a") == 0
    assert candidate(s = "aabbccddeeffaabbccddeeff",c = "d") == 10
    assert candidate(s = "abcdefabcdefabcdef",c = "f") == 6
    assert candidate(s = "abracadabra",c = "a") == 15
    assert candidate(s = "aaaaaaaaaaaaaa",c = "a") == 105
    assert candidate(s = "popcornpopcorn",c = "p") == 10
    assert candidate(s = "xyxxyxyxy",c = "x") == 15
    assert candidate(s = "bbbbbbbbbb",c = "b") == 55
    assert candidate(s = "abcdefg",c = "g") == 1
    assert candidate(s = "hellohellohellohello",c = "l") == 36
    assert candidate(s = "abcdeabcdeabcde",c = "a") == 6
    assert candidate(s = "abcdefhijklmnopqrstuvwxyz",c = "z") == 1
    assert candidate(s = "aabbccddeeff",c = "b") == 3


