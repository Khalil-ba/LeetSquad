def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "attack",s2 = "defend") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "attack",s2 = "defend") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "bank",s2 = "kanb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "bank",s2 = "kanb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "abced") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "abced") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abdc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abdc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",s2 = "aaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",s2 = "aaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "kelb",s2 = "kelb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "kelb",s2 = "kelb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabb",s2 = "abab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabb",s2 = "abab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "logarithm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "logarithm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "almost",s2 = "almost") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "almost",s2 = "almost") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "ghfedcb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "ghfedcb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzabc",s2 = "yzabxc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzabc",s2 = "yzabxc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "fedcbag") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "fedcbag") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefx") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbb",s2 = "bbbbaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbb",s2 = "bbbbaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbaab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbaab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbbc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbbc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "babacabadabacab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "babacabadabacab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "missisppi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "missisppi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "programminj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "programminj") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "samestr",s2 = "strsame") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "samestr",s2 = "strsame") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "hlelo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "hlelo") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "gfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "gfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababab",s2 = "babababa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababab",s2 = "babababa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "abracadabrb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "abracadabrb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "mississipsp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "mississipsp") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "palindrome",s2 = "lpadnrimoe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "palindrome",s2 = "lpadnrimoe") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccabba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccabba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "mississipip") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "mississipip") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbaacc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbaacc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdexyz",s2 = "xyzabcde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdexyz",s2 = "xyzabcde") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyz",s2 = "abczyxd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyz",s2 = "abczyxd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "abcde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "abcde") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "banana",s2 = "anana") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "banana",s2 = "anana") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "ba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "ba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "olleh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "olleh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "hallo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "hallo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcfed") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcfed") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiop",s2 = "qewrtyuipo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiop",s2 = "qewrtyuipo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "mississippa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "mississippa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "prorgamming") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "prorgamming") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abdecfg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abdecfg") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "noon",s2 = "nnon") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "noon",s2 = "nnon") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "ohell") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "ohell") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "hxllo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "hxllo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbb",s2 = "bbbbaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbb",s2 = "bbbbaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "acb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "acb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "lehho") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "lehho") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdexyz",s2 = "abcdefyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdexyz",s2 = "abcdefyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python",s2 = "pythno") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python",s2 = "pythno") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "abracadabra") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "abracadabra") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "bcadefgh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "bcadefgh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "abacabadabacaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "abacabadabacaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "bello") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "bello") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "heoll") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "heoll") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghjk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghjk") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique",s2 = "unqieu") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique",s2 = "unqieu") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacax",s2 = "abacxa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacax",s2 = "abacxa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "algorithn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "algorithn") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "aloritghm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "aloritghm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdegf") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdegf") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aaccbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aaccbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "almost",s2 = "alosmt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "almost",s2 = "alosmt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "racecar",s2 = "racecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "racecar",s2 = "racecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "mmissisippi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "mmissisippi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "efghabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "efghabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "zzxy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "zzxy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "palindrome",s2 = "palindorme") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "palindrome",s2 = "palindorme") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "ab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "ab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdeg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdeg") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "oneone",s2 = "noonoe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "oneone",s2 = "noonoe") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcxyz",s2 = "xyzabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcxyz",s2 = "xyzabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abac",s2 = "caba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abac",s2 = "caba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "abracadbrba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "abracadbrba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abac",s2 = "abca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abac",s2 = "abca") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same",s2 = "same") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same",s2 = "same") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghji") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghji") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "edcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "edcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "swapping",s2 = "swapgnip") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "swapping",s2 = "swapgnip") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",s2 = "ddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",s2 = "ddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "zyzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "zyzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "algorjthm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "algorjthm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "zyxz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "zyxz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbdc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbdc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "abcdefghijl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "abcdefghijl") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababab",s2 = "bababa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababab",s2 = "bababa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abab",s2 = "baba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abab",s2 = "baba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mambo",s2 = "mambp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mambo",s2 = "mambp") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdfe") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdfe") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abdc",s2 = "abcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abdc",s2 = "abcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "zyzx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "zyzx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabb",s2 = "bbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabb",s2 = "bbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same",s2 = "emsa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same",s2 = "emsa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyz",s2 = "abcdzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyz",s2 = "abcdzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "mmississippi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "mmississippi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python",s2 = "ytonph") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python",s2 = "ytonph") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyz",s2 = "zyxzyx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyz",s2 = "zyxzyx") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaa",s2 = "aaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaa",s2 = "aaaa") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "attack",s2 = "defend") == False
    assert candidate(s1 = "bank",s2 = "kanb") == True
    assert candidate(s1 = "abcde",s2 = "abced") == True
    assert candidate(s1 = "abcd",s2 = "abdc") == True
    assert candidate(s1 = "aaa",s2 = "aaa") == True
    assert candidate(s1 = "kelb",s2 = "kelb") == True
    assert candidate(s1 = "aabb",s2 = "abab") == True
    assert candidate(s1 = "abcd",s2 = "dcba") == False
    assert candidate(s1 = "algorithm",s2 = "logarithm") == False
    assert candidate(s1 = "almost",s2 = "almost") == True
    assert candidate(s1 = "abcdefg",s2 = "ghfedcb") == False
    assert candidate(s1 = "xyzabc",s2 = "yzabxc") == False
    assert candidate(s1 = "abcdefg",s2 = "fedcbag") == False
    assert candidate(s1 = "abcdefg",s2 = "abcdefx") == False
    assert candidate(s1 = "aaaaabbbb",s2 = "bbbbaaaa") == False
    assert candidate(s1 = "aabbcc",s2 = "ccbaab") == False
    assert candidate(s1 = "aabbcc",s2 = "aabbbc") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "babacabadabacab") == False
    assert candidate(s1 = "mississippi",s2 = "missisppi") == False
    assert candidate(s1 = "aabbcc",s2 = "ccbbaa") == False
    assert candidate(s1 = "programming",s2 = "programminj") == False
    assert candidate(s1 = "samestr",s2 = "strsame") == False
    assert candidate(s1 = "hello",s2 = "hlelo") == True
    assert candidate(s1 = "abcdefg",s2 = "gfedcba") == False
    assert candidate(s1 = "abababab",s2 = "babababa") == False
    assert candidate(s1 = "abracadabra",s2 = "abracadabrb") == False
    assert candidate(s1 = "mississippi",s2 = "mississipsp") == False
    assert candidate(s1 = "palindrome",s2 = "lpadnrimoe") == False
    assert candidate(s1 = "aabbcc",s2 = "ccabba") == False
    assert candidate(s1 = "mississippi",s2 = "mississipip") == True
    assert candidate(s1 = "abcdefg",s2 = "abcdefg") == True
    assert candidate(s1 = "aabbcc",s2 = "bbaacc") == False
    assert candidate(s1 = "abcdexyz",s2 = "xyzabcde") == False
    assert candidate(s1 = "abcdxyz",s2 = "abczyxd") == False
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcba") == False
    assert candidate(s1 = "abcde",s2 = "abcde") == True
    assert candidate(s1 = "banana",s2 = "anana") == False
    assert candidate(s1 = "ab",s2 = "ba") == True
    assert candidate(s1 = "hello",s2 = "olleh") == False
    assert candidate(s1 = "hello",s2 = "hallo") == False
    assert candidate(s1 = "abcdef",s2 = "abcfed") == True
    assert candidate(s1 = "abcdefg",s2 = "abcdefgh") == True
    assert candidate(s1 = "qwertyuiop",s2 = "qewrtyuipo") == False
    assert candidate(s1 = "mississippi",s2 = "mississippa") == False
    assert candidate(s1 = "programming",s2 = "prorgamming") == True
    assert candidate(s1 = "abcdefg",s2 = "abdecfg") == False
    assert candidate(s1 = "noon",s2 = "nnon") == False
    assert candidate(s1 = "hello",s2 = "ohell") == False
    assert candidate(s1 = "hello",s2 = "hxllo") == False
    assert candidate(s1 = "aaaabbbb",s2 = "bbbbaaaa") == False
    assert candidate(s1 = "abc",s2 = "acb") == True
    assert candidate(s1 = "hello",s2 = "lehho") == False
    assert candidate(s1 = "abcdexyz",s2 = "abcdefyz") == False
    assert candidate(s1 = "python",s2 = "pythno") == True
    assert candidate(s1 = "abracadabra",s2 = "abracadabra") == True
    assert candidate(s1 = "abcdefgh",s2 = "bcadefgh") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "abacabadabacaba") == True
    assert candidate(s1 = "hello",s2 = "bello") == False
    assert candidate(s1 = "hello",s2 = "heoll") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghjk") == False
    assert candidate(s1 = "unique",s2 = "unqieu") == False
    assert candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == False
    assert candidate(s1 = "abacax",s2 = "abacxa") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
    assert candidate(s1 = "algorithm",s2 = "algorithn") == False
    assert candidate(s1 = "algorithm",s2 = "aloritghm") == False
    assert candidate(s1 = "abcdefg",s2 = "abcdegf") == True
    assert candidate(s1 = "aabbcc",s2 = "aaccbb") == False
    assert candidate(s1 = "almost",s2 = "alosmt") == False
    assert candidate(s1 = "racecar",s2 = "racecar") == True
    assert candidate(s1 = "mississippi",s2 = "mmissisippi") == False
    assert candidate(s1 = "abcdefgh",s2 = "efghabcd") == False
    assert candidate(s1 = "xyzz",s2 = "zzxy") == False
    assert candidate(s1 = "palindrome",s2 = "palindorme") == True
    assert candidate(s1 = "abcdef",s2 = "abcdef") == True
    assert candidate(s1 = "ab",s2 = "ab") == True
    assert candidate(s1 = "abcdef",s2 = "abcdeg") == False
    assert candidate(s1 = "oneone",s2 = "noonoe") == False
    assert candidate(s1 = "abcxyz",s2 = "xyzabc") == False
    assert candidate(s1 = "abac",s2 = "caba") == False
    assert candidate(s1 = "xyz",s2 = "zyx") == True
    assert candidate(s1 = "abracadabra",s2 = "abracadbrba") == False
    assert candidate(s1 = "abac",s2 = "abca") == True
    assert candidate(s1 = "same",s2 = "same") == True
    assert candidate(s1 = "abcdefgh",s2 = "abcdefgh") == True
    assert candidate(s1 = "abcdef",s2 = "fedcba") == False
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghji") == True
    assert candidate(s1 = "abcde",s2 = "edcba") == False
    assert candidate(s1 = "swapping",s2 = "swapgnip") == False
    assert candidate(s1 = "aabbccdd",s2 = "ddccbbaa") == False
    assert candidate(s1 = "xyzz",s2 = "zyzz") == False
    assert candidate(s1 = "algorithm",s2 = "algorjthm") == False
    assert candidate(s1 = "xyzz",s2 = "zyxz") == True
    assert candidate(s1 = "aabbcc",s2 = "aabbdc") == False
    assert candidate(s1 = "abcdefghijk",s2 = "abcdefghijl") == False
    assert candidate(s1 = "ababab",s2 = "bababa") == False
    assert candidate(s1 = "abab",s2 = "baba") == False
    assert candidate(s1 = "mambo",s2 = "mambp") == False
    assert candidate(s1 = "abcdef",s2 = "abcdfe") == True
    assert candidate(s1 = "abdc",s2 = "abcd") == True
    assert candidate(s1 = "xyzz",s2 = "zyzx") == True
    assert candidate(s1 = "aabb",s2 = "bbaa") == False
    assert candidate(s1 = "same",s2 = "emsa") == False
    assert candidate(s1 = "abcdxyz",s2 = "abcdzyx") == True
    assert candidate(s1 = "mississippi",s2 = "mmississippi") == False
    assert candidate(s1 = "python",s2 = "ytonph") == False
    assert candidate(s1 = "xyzxyz",s2 = "zyxzyx") == False
    assert candidate(s1 = "aaaa",s2 = "aaaa") == True


