def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "acbd",pairs = [[0, 3], [1, 2]]) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbd",pairs = [[0, 3], [1, 2]]) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "cba",pairs = [[0, 1], [1, 2]]) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cba",pairs = [[0, 1], [1, 2]]) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",pairs = [[0, 1], [2, 3], [4, 5]]) == "aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",pairs = [[0, 1], [2, 3], [4, 5]]) == "aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyx",pairs = [[0, 1], [1, 2]]) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyx",pairs = [[0, 1], [1, 2]]) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",pairs = [[0, 1], [1, 2], [2, 3]]) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",pairs = [[0, 1], [1, 2], [2, 3]]) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode",pairs = [[0, 2], [1, 3]]) == "eeltcode"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode",pairs = [[0, 2], [1, 3]]) == "eeltcode": {e}')
    
    total += 1
    try:
        result = candidate(s = "dcab",pairs = [[0, 3], [1, 2]]) == "bacd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcab",pairs = [[0, 3], [1, 2]]) == "bacd": {e}')
    
    total += 1
    try:
        result = candidate(s = "dcab",pairs = [[0, 3], [1, 2], [0, 2]]) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcab",pairs = [[0, 3], [1, 2], [0, 2]]) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwe",pairs = [[0, 2]]) == "ewq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwe",pairs = [[0, 2]]) == "ewq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abdc",pairs = [[0, 3]]) == "abdc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abdc",pairs = [[0, 3]]) == "abdc": {e}')
    
    total += 1
    try:
        result = candidate(s = "vokh",pairs = [[0, 1], [1, 3], [0, 3]]) == "hokv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vokh",pairs = [[0, 1], [1, 3], [0, 3]]) == "hokv": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",pairs = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 6], [1, 5], [2, 4]]) == "abcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",pairs = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 6], [1, 5], [2, 4]]) == "abcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "jklmno",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 3]]) == "jklmno"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jklmno",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 3]]) == "jklmno": {e}')
    
    total += 1
    try:
        result = candidate(s = "dcabxy",pairs = [[0, 3], [1, 2], [4, 5], [0, 2]]) == "abcdxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcabxy",pairs = [[0, 3], [1, 2], [4, 5], [0, 2]]) == "abcdxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aazaa",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "aaaaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aazaa",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "aaaaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aefdcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == "aabcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aefdcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == "aabcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",pairs = [[0, 5], [1, 4], [2, 3], [0, 2]]) == "abcxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",pairs = [[0, 5], [1, 4], [2, 3], [0, 2]]) == "abcxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",pairs = [[0, 5], [1, 4], [2, 3]]) == "cbazyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",pairs = [[0, 5], [1, 4], [2, 3]]) == "cbazyx": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba",pairs = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [5, 7], [6, 7]]) == "abcdeeffdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba",pairs = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [5, 7], [6, 7]]) == "abcdeeffdcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13]]) == "mnbrcxuikjagdfshpolzytvewq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13]]) == "mnbrcxuikjagdfshpolzytvewq": {e}')
    
    total += 1
    try:
        result = candidate(s = "bdcagf",pairs = [[0, 3], [1, 4], [2, 5]]) == "adcbgf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bdcagf",pairs = [[0, 3], [1, 4], [2, 5]]) == "adcbgf": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",pairs = [[0, 6], [1, 5], [2, 4]]) == "racecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",pairs = [[0, 6], [1, 5], [2, 4]]) == "racecar": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",pairs = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10]]) == "abcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",pairs = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10]]) == "abcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",pairs = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",pairs = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode",pairs = [[0, 2], [1, 3], [4, 5], [6, 7]]) == "eeltcode"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode",pairs = [[0, 2], [1, 3], [4, 5], [6, 7]]) == "eeltcode": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyx",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == "xxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyx",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == "xxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",pairs = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == "abcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",pairs = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == "abcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad",pairs = [[0, 2], [1, 3], [4, 6], [5, 7]]) == "abacabad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad",pairs = [[0, 2], [1, 3], [4, 6], [5, 7]]) == "abacabad": {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjihgfedcba",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 5], [1, 6]]) == "bcdefghijkla"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjihgfedcba",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 5], [1, 6]]) == "bcdefghijkla": {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",pairs = [[0, 6], [1, 5], [2, 4], [3, 7]]) == "aighrltom"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",pairs = [[0, 6], [1, 5], [2, 4], [3, 7]]) == "aighrltom": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",pairs = [[0, 1], [1, 2], [2, 3], [0, 3], [1, 2]]) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",pairs = [[0, 1], [1, 2], [2, 3], [0, 3], [1, 2]]) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "acbdf",pairs = [[0, 1], [0, 2], [1, 2], [3, 4]]) == "abcdf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbdf",pairs = [[0, 1], [0, 2], [1, 2], [3, 4]]) == "abcdf": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]) == "aabbccddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]) == "aabbccddeeff": {e}')
    
    total += 1
    try:
        result = candidate(s = "stuvwx",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 3], [2, 4]]) == "stuvwx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "stuvwx",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 3], [2, 4]]) == "stuvwx": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",pairs = [[0, 1], [0, 4], [1, 2], [2, 3]]) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",pairs = [[0, 1], [0, 4], [1, 2], [2, 3]]) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "ympxz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "mpxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ympxz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "mpxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "ekzpz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "ekpzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ekzpz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "ekpzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21]]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21]]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [1, 13]]) == "aaaaaaabbbbccda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [1, 13]]) == "aaaaaaabbbbccda": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 2], [3, 4]]) == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 2], [3, 4]]) == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothereeveryone",pairs = [[0, 8], [1, 3], [2, 9], [5, 11], [6, 7], [12, 16], [13, 14], [15, 17]]) == "heelotehrleveryeno"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothereeveryone",pairs = [[0, 8], [1, 3], [2, 9], [5, 11], [6, 7], [12, 16], [13, 14], [15, 17]]) == "heelotehrleveryeno": {e}')
    
    total += 1
    try:
        result = candidate(s = "dcabxyz",pairs = [[0, 3], [1, 2], [3, 5], [4, 6]]) == "bacdxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcabxyz",pairs = [[0, 3], [1, 2], [3, 5], [4, 6]]) == "bacdxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzab",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 3]]) == "abxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzab",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 3]]) == "abxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "uvuuvuvuvu",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [2, 4], [4, 6], [6, 8], [1, 3], [3, 5], [5, 7], [7, 9], [0, 9]]) == "uuuuuuvvvv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uvuuvuvuvu",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [2, 4], [4, 6], [6, 8], [1, 3], [3, 5], [5, 7], [7, 9], [0, 9]]) == "uuuuuuvvvv": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "abcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "abcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "uvazyx",pairs = [[0, 5], [1, 4], [2, 3]]) == "uvazyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uvazyx",pairs = [[0, 5], [1, 4], [2, 3]]) == "uvazyx": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyz",pairs = [[0, 3], [1, 4], [2, 5]]) == "xyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyz",pairs = [[0, 3], [1, 4], [2, 5]]) == "xyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5]]) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5]]) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",pairs = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 9]]) == "immangorprg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",pairs = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 9]]) == "immangorprg": {e}')
    
    total += 1
    try:
        result = candidate(s = "ufyx",pairs = [[0, 3], [1, 2], [0, 2], [1, 3]]) == "fuxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ufyx",pairs = [[0, 3], [1, 2], [0, 2], [1, 3]]) == "fuxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjhgfedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "abcdefghjkl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjhgfedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "abcdefghjkl": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",pairs = [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [0, 4], [1, 5], [2, 6], [3, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == "aaaabbbbccccdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",pairs = [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [0, 4], [1, 5], [2, 6], [3, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == "aaaabbbbccccdddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]]) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]]) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "nmosq",pairs = [[0, 3], [1, 2], [2, 3], [3, 4]]) == "mnoqs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nmosq",pairs = [[0, 3], [1, 2], [2, 3], [3, 4]]) == "mnoqs": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",pairs = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 3], [1, 4]]) == "abcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",pairs = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 3], [1, 4]]) == "abcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "helloworld",pairs = [[0, 8], [1, 7], [2, 6], [3, 5]]) == "helloworld"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "helloworld",pairs = [[0, 8], [1, 7], [2, 6], [3, 5]]) == "helloworld": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 4], [2, 3], [0, 1], [8, 9]]) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 4], [2, 3], [0, 1], [8, 9]]) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadaba",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 5], [1, 4], [2, 3], [0, 1], [8, 9], [5, 6]]) == "aaaaaabbbcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadaba",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 5], [1, 4], [2, 3], [0, 1], [8, 9], [5, 6]]) == "aaaaaabbbcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",pairs = [[0, 8], [1, 7], [2, 6], [3, 5], [1, 9]]) == "immargonprg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",pairs = [[0, 8], [1, 7], [2, 6], [3, 5], [1, 9]]) == "immargonprg": {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmlkjhgfdsapoiuytrewq",pairs = [[0, 23], [1, 22], [2, 21], [3, 20], [4, 19], [5, 18], [6, 17], [7, 16], [8, 15], [9, 14], [10, 13], [11, 12]]) == "ercvbimlajdfghskponuytxzwq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmlkjhgfdsapoiuytrewq",pairs = [[0, 23], [1, 22], [2, 21], [3, 20], [4, 19], [5, 18], [6, 17], [7, 16], [8, 15], [9, 14], [10, 13], [11, 12]]) == "ercvbimlajdfghskponuytxzwq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",pairs = [[0, 1], [1, 2], [2, 0]]) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",pairs = [[0, 1], [1, 2], [2, 0]]) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xzy",pairs = [[0, 1], [1, 2], [0, 2], [1, 2], [0, 1]]) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xzy",pairs = [[0, 1], [1, 2], [0, 2], [1, 2], [0, 1]]) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == "abcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == "abcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13]]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13]]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13], [0, 13], [1, 14], [2, 15], [3, 16], [4, 17], [5, 18], [6, 19], [7, 20], [8, 21], [9, 22], [10, 23], [11, 24], [12, 25]]) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13], [0, 13], [1, 14], [2, 15], [3, 16], [4, 17], [5, 18], [6, 19], [7, 20], [8, 21], [9, 22], [10, 23], [11, 24], [12, 25]]) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7]]) == "abcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7]]) == "abcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",pairs = [[0, 1], [2, 3], [4, 5], [0, 5], [1, 4], [2, 8]]) == "aaabbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",pairs = [[0, 1], [2, 3], [4, 5], [0, 5], [1, 4], [2, 8]]) == "aaabbbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyz",pairs = [[0, 7], [1, 6], [2, 5], [3, 4]]) == "abcdexyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyz",pairs = [[0, 7], [1, 6], [2, 5], [3, 4]]) == "abcdexyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",pairs = [[0, 5], [1, 4], [2, 3]]) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",pairs = [[0, 5], [1, 4], [2, 3]]) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "acbd",pairs = [[0, 3], [1, 2]]) == "abcd"
    assert candidate(s = "cba",pairs = [[0, 1], [1, 2]]) == "abc"
    assert candidate(s = "aabbcc",pairs = [[0, 1], [2, 3], [4, 5]]) == "aabbcc"
    assert candidate(s = "zyx",pairs = [[0, 1], [1, 2]]) == "xyz"
    assert candidate(s = "abcd",pairs = [[0, 1], [1, 2], [2, 3]]) == "abcd"
    assert candidate(s = "leetcode",pairs = [[0, 2], [1, 3]]) == "eeltcode"
    assert candidate(s = "dcab",pairs = [[0, 3], [1, 2]]) == "bacd"
    assert candidate(s = "dcab",pairs = [[0, 3], [1, 2], [0, 2]]) == "abcd"
    assert candidate(s = "qwe",pairs = [[0, 2]]) == "ewq"
    assert candidate(s = "abdc",pairs = [[0, 3]]) == "abdc"
    assert candidate(s = "vokh",pairs = [[0, 1], [1, 3], [0, 3]]) == "hokv"
    assert candidate(s = "abcdefgh",pairs = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 6], [1, 5], [2, 4]]) == "abcdefgh"
    assert candidate(s = "jklmno",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 3]]) == "jklmno"
    assert candidate(s = "dcabxy",pairs = [[0, 3], [1, 2], [4, 5], [0, 2]]) == "abcdxy"
    assert candidate(s = "aazaa",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "aaaaz"
    assert candidate(s = "aefdcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == "aabcdef"
    assert candidate(s = "xyzabc",pairs = [[0, 5], [1, 4], [2, 3], [0, 2]]) == "abcxyz"
    assert candidate(s = "xyzabc",pairs = [[0, 5], [1, 4], [2, 3]]) == "cbazyx"
    assert candidate(s = "abcdeffedcba",pairs = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [5, 7], [6, 7]]) == "abcdeeffdcba"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13]]) == "mnbrcxuikjagdfshpolzytvewq"
    assert candidate(s = "bdcagf",pairs = [[0, 3], [1, 4], [2, 5]]) == "adcbgf"
    assert candidate(s = "racecar",pairs = [[0, 6], [1, 5], [2, 4]]) == "racecar"
    assert candidate(s = "abcdefghijk",pairs = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10]]) == "abcdefghijk"
    assert candidate(s = "abcdefg",pairs = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == "abcdefg"
    assert candidate(s = "leetcode",pairs = [[0, 2], [1, 3], [4, 5], [6, 7]]) == "eeltcode"
    assert candidate(s = "zyxzyx",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == "xxyyzz"
    assert candidate(s = "abcdefghijk",pairs = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == "abcdefghijk"
    assert candidate(s = "abacabad",pairs = [[0, 2], [1, 3], [4, 6], [5, 7]]) == "abacabad"
    assert candidate(s = "lkjihgfedcba",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 5], [1, 6]]) == "bcdefghijkla"
    assert candidate(s = "algorithm",pairs = [[0, 6], [1, 5], [2, 4], [3, 7]]) == "aighrltom"
    assert candidate(s = "abcd",pairs = [[0, 1], [1, 2], [2, 3], [0, 3], [1, 2]]) == "abcd"
    assert candidate(s = "acbdf",pairs = [[0, 1], [0, 2], [1, 2], [3, 4]]) == "abcdf"
    assert candidate(s = "aabbccddeeff",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]) == "aabbccddeeff"
    assert candidate(s = "stuvwx",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 3], [2, 4]]) == "stuvwx"
    assert candidate(s = "abcde",pairs = [[0, 1], [0, 4], [1, 2], [2, 3]]) == "abcde"
    assert candidate(s = "ympxz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "mpxyz"
    assert candidate(s = "ekzpz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4]]) == "ekpzz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21]]) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "fedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == "abcdef"
    assert candidate(s = "abacabadabacaba",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [1, 13]]) == "aaaaaaabbbbccda"
    assert candidate(s = "abcdefg",pairs = [[0, 3], [1, 4], [2, 5], [0, 5], [1, 2], [3, 4]]) == "abcdefg"
    assert candidate(s = "hellothereeveryone",pairs = [[0, 8], [1, 3], [2, 9], [5, 11], [6, 7], [12, 16], [13, 14], [15, 17]]) == "heelotehrleveryeno"
    assert candidate(s = "dcabxyz",pairs = [[0, 3], [1, 2], [3, 5], [4, 6]]) == "bacdxyz"
    assert candidate(s = "xyzab",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 3]]) == "abxyz"
    assert candidate(s = "uvuuvuvuvu",pairs = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [2, 4], [4, 6], [6, 8], [1, 3], [3, 5], [5, 7], [7, 9], [0, 9]]) == "uuuuuuvvvv"
    assert candidate(s = "abcdefghijk",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "abcdefghijk"
    assert candidate(s = "uvazyx",pairs = [[0, 5], [1, 4], [2, 3]]) == "uvazyx"
    assert candidate(s = "xyzxyz",pairs = [[0, 3], [1, 4], [2, 5]]) == "xyzxyz"
    assert candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5]]) == "abcdefghij"
    assert candidate(s = "programming",pairs = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 9]]) == "immangorprg"
    assert candidate(s = "ufyx",pairs = [[0, 3], [1, 2], [0, 2], [1, 3]]) == "fuxy"
    assert candidate(s = "lkjhgfedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "abcdefghjkl"
    assert candidate(s = "aaaabbbbccccdddd",pairs = [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [0, 4], [1, 5], [2, 6], [3, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == "aaaabbbbccccdddd"
    assert candidate(s = "abcdef",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]]) == "abcdef"
    assert candidate(s = "nmosq",pairs = [[0, 3], [1, 2], [2, 3], [3, 4]]) == "mnoqs"
    assert candidate(s = "abcdefgh",pairs = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 3], [1, 4]]) == "abcdefgh"
    assert candidate(s = "helloworld",pairs = [[0, 8], [1, 7], [2, 6], [3, 5]]) == "helloworld"
    assert candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [1, 4], [2, 3], [0, 1], [8, 9]]) == "abcdefghij"
    assert candidate(s = "abacabadaba",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 5], [1, 4], [2, 3], [0, 1], [8, 9], [5, 6]]) == "aaaaaabbbcd"
    assert candidate(s = "programming",pairs = [[0, 8], [1, 7], [2, 6], [3, 5], [1, 9]]) == "immargonprg"
    assert candidate(s = "zxcvbnmlkjhgfdsapoiuytrewq",pairs = [[0, 23], [1, 22], [2, 21], [3, 20], [4, 19], [5, 18], [6, 17], [7, 16], [8, 15], [9, 14], [10, 13], [11, 12]]) == "ercvbimlajdfghskponuytxzwq"
    assert candidate(s = "abcdefghij",pairs = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == "abcdefghij"
    assert candidate(s = "xyz",pairs = [[0, 1], [1, 2], [2, 0]]) == "xyz"
    assert candidate(s = "xzy",pairs = [[0, 1], [1, 2], [0, 2], [1, 2], [0, 1]]) == "xyz"
    assert candidate(s = "abcdefghijk",pairs = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == "abcdefghijk"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13]]) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pairs = [[0, 25], [1, 24], [2, 23], [3, 22], [4, 21], [5, 20], [6, 19], [7, 18], [8, 17], [9, 16], [10, 15], [11, 14], [12, 13], [0, 13], [1, 14], [2, 15], [3, 16], [4, 17], [5, 18], [6, 19], [7, 20], [8, 21], [9, 22], [10, 23], [11, 24], [12, 25]]) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "abcdefgh",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7]]) == "abcdefgh"
    assert candidate(s = "aaabbbccc",pairs = [[0, 1], [2, 3], [4, 5], [0, 5], [1, 4], [2, 8]]) == "aaabbbccc"
    assert candidate(s = "abcdexyz",pairs = [[0, 7], [1, 6], [2, 5], [3, 4]]) == "abcdexyz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "abcdefghij",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == "abcdefghij"
    assert candidate(s = "abcdef",pairs = [[0, 5], [1, 4], [2, 3]]) == "abcdef"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == "abcdefghijklmnopqrstuvwxyz"


