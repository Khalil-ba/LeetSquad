def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcac",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcac",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopqwertyuiopqwertyuiop",k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopqwertyuiopqwertyuiop",k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbccdd",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbccdd",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcbafedcba",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcbafedcba",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcd",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcd",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyz",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyz",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde",k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde",k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "level",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmlloo",k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmlloo",k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccba",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccba",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra",k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra",k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "redder",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redder",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababaabab",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababaabab",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdef",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdef",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiabcdefghiabcdefghi",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiabcdefghiabcdefghi",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyz",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyz",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaa",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaa",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddaaa",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddaaa",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxzyxzyxzyxzyx",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxzyxzyxzyxzyx",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxy",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxy",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefghabcdefgh",k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefghabcdefgh",k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggfedcba",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggfedcba",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnoopp",k = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnoopp",k = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaabaaabaaab",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaabaaabaaab",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrnopqr",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrnopqr",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc",k = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc",k = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklnmopqrstuvwxyz",k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklnmopqrstuvwxyz",k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyxzyx",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyxzyx",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccdddd",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccdddd",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggg",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggg",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc",k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc",k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaaabaaa",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaaabaaa",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbcccc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbcccc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrsmno",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrsmno",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzaaaabbbccc",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzaaaabbbccc",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrspqrspqr",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrspqrspqr",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadaba",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadaba",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyzzzzzz",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyzzzzzz",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxy",k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxy",k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaa",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaa",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyzzzzz",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyzzzzz",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdef",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdef",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdef",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdef",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "anana",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anana",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij",k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij",k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyz",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyz",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwx",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwx",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzyyyzzzzzyyy",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzyyyzzzzzyyy",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "reviled",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "reviled",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbbccccaaa",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbbccccaaa",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyz",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyz",k = 4) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aabbcc",k = 3) == 0
    assert candidate(s = "abccba",k = 2) == 2
    assert candidate(s = "aabbccdd",k = 4) == 0
    assert candidate(s = "abcabcabc",k = 4) == 4
    assert candidate(s = "aaaaaa",k = 2) == 0
    assert candidate(s = "abcabcabcabc",k = 4) == 3
    assert candidate(s = "abccba",k = 1) == 0
    assert candidate(s = "aabbaa",k = 3) == 0
    assert candidate(s = "racecar",k = 1) == 0
    assert candidate(s = "abcac",k = 2) == 1
    assert candidate(s = "zzzzzz",k = 2) == 0
    assert candidate(s = "abcdabc",k = 2) == 2
    assert candidate(s = "abcdefg",k = 2) == 3
    assert candidate(s = "abcdcba",k = 3) == 2
    assert candidate(s = "abcdefg",k = 3) == 3
    assert candidate(s = "abcabcabc",k = 3) == 3
    assert candidate(s = "aaaa",k = 2) == 0
    assert candidate(s = "abcdabc",k = 3) == 3
    assert candidate(s = "abcabc",k = 3) == 3
    assert candidate(s = "abcdef",k = 2) == 2
    assert candidate(s = "abccba",k = 3) == 2
    assert candidate(s = "ababab",k = 3) == 3
    assert candidate(s = "qwertyuiopqwertyuiopqwertyuiop",k = 6) == 5
    assert candidate(s = "aabbccddeeaabbccddeeaabbccdd",k = 6) == 2
    assert candidate(s = "abcdefedcbafedcba",k = 3) == 1
    assert candidate(s = "abcdabcdabcdabcdabcdabcd",k = 5) == 2
    assert candidate(s = "abcdabcdabcdabcd",k = 4) == 2
    assert candidate(s = "xyzxyzxyzxyz",k = 4) == 3
    assert candidate(s = "xyzxyzxyzxyzxyz",k = 3) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",k = 5) == 4
    assert candidate(s = "abcdeabcdeabcde",k = 4) == 5
    assert candidate(s = "level",k = 1) == 0
    assert candidate(s = "banana",k = 2) == 1
    assert candidate(s = "aabbaabbaabbaabb",k = 4) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmlloo",k = 5) == 6
    assert candidate(s = "abccbaabccbaabccba",k = 4) == 2
    assert candidate(s = "abracadabraabracadabra",k = 4) == 5
    assert candidate(s = "redder",k = 2) == 2
    assert candidate(s = "repaper",k = 2) == 3
    assert candidate(s = "abababaabab",k = 3) == 0
    assert candidate(s = "abcdefghij",k = 2) == 4
    assert candidate(s = "abcdefabcdef",k = 4) == 4
    assert candidate(s = "abcdefghiabcdefghiabcdefghi",k = 4) == 3
    assert candidate(s = "xyzxyzxyzxyzxyz",k = 5) == 4
    assert candidate(s = "aabbaaabbbaa",k = 3) == 1
    assert candidate(s = "aaabbbcccdddaaa",k = 4) == 2
    assert candidate(s = "abcdefgabcdefg",k = 4) == 5
    assert candidate(s = "xyxzyxzyxzyxzyxzyx",k = 4) == 1
    assert candidate(s = "xyxyxyxyxyxyxy",k = 3) == 0
    assert candidate(s = "aaaaabbbbbcccc",k = 3) == 0
    assert candidate(s = "ababababababab",k = 3) == 0
    assert candidate(s = "abcdefghabcdefghabcdefgh",k = 6) == 5
    assert candidate(s = "mississippi",k = 2) == 2
    assert candidate(s = "abccbaabccba",k = 2) == 0
    assert candidate(s = "abcdefabcdefabcdef",k = 6) == 6
    assert candidate(s = "abcdefggfedcba",k = 2) == 5
    assert candidate(s = "noonnoonnoon",k = 3) == 0
    assert candidate(s = "aabbccddeeffgghhiijj",k = 5) == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnoopp",k = 6) == 8
    assert candidate(s = "aaabaaabaaabaaab",k = 5) == 1
    assert candidate(s = "aabbccddeeff",k = 3) == 4
    assert candidate(s = "abcdefgabcdefg",k = 2) == 5
    assert candidate(s = "racecar",k = 3) == 2
    assert candidate(s = "abababab",k = 3) == 1
    assert candidate(s = "ababababababab",k = 5) == 1
    assert candidate(s = "abcabcabcabcabcabc",k = 6) == 5
    assert candidate(s = "mnopqrnopqr",k = 3) == 4
    assert candidate(s = "deified",k = 1) == 0
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",k = 5) == 4
    assert candidate(s = "abcabcabcabcabcabcabc",k = 7) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 7) == 0
    assert candidate(s = "abcdefghij",k = 5) == 5
    assert candidate(s = "noon",k = 1) == 0
    assert candidate(s = "aaaaaaaaaa",k = 5) == 0
    assert candidate(s = "abcdefghijklnmopqrstuvwxyz",k = 5) == 9
    assert candidate(s = "abcdefghij",k = 3) == 4
    assert candidate(s = "racecar",k = 2) == 3
    assert candidate(s = "rotor",k = 1) == 0
    assert candidate(s = "abracadabraabracadabra",k = 5) == 4
    assert candidate(s = "xyzyxzyxzyx",k = 4) == 3
    assert candidate(s = "aaaaabbbbccccdddd",k = 4) == 0
    assert candidate(s = "aaabbbcccdddeeefffggg",k = 5) == 3
    assert candidate(s = "aaaabbbbccccdddd",k = 4) == 0
    assert candidate(s = "abcabcabcabcabcabcabcabc",k = 6) == 3
    assert candidate(s = "ababababab",k = 3) == 0
    assert candidate(s = "aabaaabaaabaaa",k = 4) == 1
    assert candidate(s = "aabbccddeeffgg",k = 4) == 4
    assert candidate(s = "aaaaabbbbcccc",k = 3) == 0
    assert candidate(s = "mnopqrsmnopqrsmno",k = 3) == 6
    assert candidate(s = "aabbccddeeffgg",k = 6) == 2
    assert candidate(s = "zzzaaaabbbccc",k = 4) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10) == 10
    assert candidate(s = "abababababababab",k = 4) == 0
    assert candidate(s = "mnopqrspqrspqr",k = 3) == 2
    assert candidate(s = "abacabadaba",k = 3) == 1
    assert candidate(s = "mississippi",k = 3) == 1
    assert candidate(s = "abacabadabacaba",k = 5) == 2
    assert candidate(s = "abacabadabacaba",k = 3) == 0
    assert candidate(s = "zzzzzyzzzzzz",k = 5) == 0
    assert candidate(s = "xyxyxyxyxyxy",k = 6) == 6
    assert candidate(s = "abcdeedcba",k = 2) == 4
    assert candidate(s = "abcdabcdabcdabcdabcd",k = 4) == 1
    assert candidate(s = "abcdefedcba",k = 5) == 4
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaa",k = 5) == 0
    assert candidate(s = "zzzzzyzzzzz",k = 2) == 0
    assert candidate(s = "abcabcabcabcabc",k = 5) == 4
    assert candidate(s = "abcdefabcdef",k = 2) == 1
    assert candidate(s = "abcdefabcdefabcdefabcdef",k = 5) == 3
    assert candidate(s = "anana",k = 1) == 0
    assert candidate(s = "abcdefghijabcdefghij",k = 5) == 7
    assert candidate(s = "aaaabbbb",k = 2) == 0
    assert candidate(s = "xyzyzyzyz",k = 4) == 3
    assert candidate(s = "mnopqrstuvwx",k = 4) == 4
    assert candidate(s = "zzzzzzyyyzzzzzyyy",k = 2) == 0
    assert candidate(s = "reviled",k = 2) == 3
    assert candidate(s = "aaabbbbccccaaa",k = 3) == 3
    assert candidate(s = "abacabadabacaba",k = 4) == 1
    assert candidate(s = "aabbccddeeff",k = 4) == 2
    assert candidate(s = "xyzxyzxyzxyzxyz",k = 4) == 3


