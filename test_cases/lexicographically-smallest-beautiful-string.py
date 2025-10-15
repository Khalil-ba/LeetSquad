def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 5) == "abce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 5) == "abce": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 6) == "aabbcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 6) == "aabbcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyx",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyx",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcz",k = 26) == "abda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcz",k = 26) == "abda": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",k = 4) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",k = 4) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s = "dc",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dc",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aab",k = 3) == "aac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aab",k = 3) == "aac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 4) == "abda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 4) == "abda": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",k = 26) == "xza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",k = 26) == "xza": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyx",k = 3) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyx",k = 3) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb",k = 4) == "aabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb",k = 4) == "aabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "azzzz",k = 26) == "bacba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "azzzz",k = 26) == "bacba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 3) == "acbacbacbacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 3) == "acbacbacbacb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabca",k = 26) == "abcabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabca",k = 26) == "abcabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababa",k = 6) == "aabababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababa",k = 6) == "aabababc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 26) == "abcabcabcabd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 26) == "abcabcabcabd": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyxzyx",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyxzyx",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "wxyz",k = 26) == "wxza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wxyz",k = 26) == "wxza": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvw",k = 21) == "mnopqrsuabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvw",k = 21) == "mnopqrsuabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsr",k = 19) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsr",k = 19) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 7) == "abcdega"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 7) == "abcdega": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",k = 26) == "abcdefghijklmnoq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",k = 26) == "abcdefghijklmnoq": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",k = 18) == "mnopra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",k = 18) == "mnopra": {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjihgf",k = 12) == "lkjihgi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjihgf",k = 12) == "lkjihgi": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc",k = 3) == "acbacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc",k = 3) == "acbacb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 10) == "abcdefghja"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 10) == "abcdefghja": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccba",k = 15) == "aabccbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccba",k = 15) == "aabccbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 26) == "mnbvcxzlkjhgfdsapoiuytrewr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 26) == "mnbvcxzlkjhgfdsapoiuytrewr": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",k = 3) == "ababababababac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",k = 3) == "ababababababac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",k = 3) == "acbacbacbacbacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",k = 3) == "acbacbacbacbacb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyza",k = 26) == "abcdefghijklmnopqrstuvwxyzb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyza",k = 26) == "abcdefghijklmnopqrstuvwxyzb": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrstabcabcabcabcab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrstabcabcabcabcab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuv",k = 21) == "abcdefghijklmnopqrsuab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuv",k = 21) == "abcdefghijklmnopqrsuab": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyzab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyzab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",k = 4) == "abcdabda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",k = 4) == "abcdabda": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaabcd",k = 26) == "abcaabce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaabcd",k = 26) == "abcaabce": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrlmno",k = 14) == "mnopqrlnab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrlmno",k = 14) == "mnopqrlnab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba",k = 10) == "abcdcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba",k = 10) == "abcdcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxzz",k = 26) == "abcdefghijklmnopqrstuvwyab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxzz",k = 26) == "abcdefghijklmnopqrstuvwyab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 12) == "abcdefghijl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 12) == "abcdefghijl": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 11) == "abcdefghika"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 11) == "abcdefghika": {e}')
    
    total += 1
    try:
        result = candidate(s = "abba",k = 26) == "abbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba",k = 26) == "abbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",k = 26) == "abababababac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",k = 26) == "abababababac": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",k = 26) == "aaaabbbbccccddde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",k = 26) == "aaaabbbbccccddde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 3) == "acbacbacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 3) == "acbacbacb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba",k = 26) == "abcdcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba",k = 26) == "abcdcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyz",k = 26) == "abcdexza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyz",k = 26) == "abcdexza": {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrs",k = 18) == "prab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrs",k = 18) == "prab": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 26) == "qwertyuiopasdfghjklzxcvbno"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 26) == "qwertyuiopasdfghjklzxcvbno": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",k = 26) == "xyzabd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",k = 26) == "xyzabd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 26) == "abacabadabacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 26) == "abacabadabacabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",k = 6) == "aabbccde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",k = 6) == "aabbccde": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabb",k = 6) == "aabbaabbaabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabb",k = 6) == "aabbaabbaabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 5) == "abcea"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 5) == "abcea": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvw",k = 22) == "mnopqrstvab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvw",k = 22) == "mnopqrstvab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyzabcd",k = 26) == "abcdexyzabce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyzabcd",k = 26) == "abcdexyzabce": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacaba",k = 3) == "abacabacabacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacaba",k = 3) == "abacabacabacabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabc",k = 26) == "abacabadabd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabc",k = 26) == "abacabadabd": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",k = 26) == "xzabcabcabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",k = 26) == "xzabcabcabca": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba",k = 3) == "abcbacbac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba",k = 3) == "abcbacbac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 26) == "abcdefghik"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 26) == "abcdefghik": {e}')
    
    total += 1
    try:
        result = candidate(s = "abac",k = 4) == "abad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abac",k = 4) == "abad": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 26) == "abcabcabd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 26) == "abcabcabd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba",k = 3) == "acbac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba",k = 3) == "acbac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",k = 10) == "abcdefghj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",k = 10) == "abcdefghj": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa",k = 6) == "aabbac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa",k = 6) == "aabbac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",k = 9) == "abcdefgia"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",k = 9) == "abcdefgia": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxcba",k = 6) == "zyxcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxcba",k = 6) == "zyxcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzz",k = 26) == "mnopqrstuvwxzab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzz",k = 26) == "mnopqrstuvwxzab": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",k = 6) == "aabbccddefabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 6) == "aabbccddefabca": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 15) == "abacabadabacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 15) == "abacabadabacabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxy",k = 26) == "abcdefghijklmnopqrstuvwxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxy",k = 26) == "abcdefghijklmnopqrstuvwxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc",k = 26) == "abcdabd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc",k = 26) == "abcdabd": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcba",k = 6) == "fedcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcba",k = 6) == "fedcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",k = 10) == "aabbccddeeffgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 10) == "aabbccddeeffgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstu",k = 20) == "mnopqrtab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstu",k = 20) == "mnopqrtab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 8) == "abcdefh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 8) == "abcdefh": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",k = 2) == "baababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",k = 2) == "baababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba",k = 20) == "abcddcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba",k = 20) == "abcddcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",k = 7) == "abacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",k = 7) == "abacabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 3) == "abacabadabacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 3) == "abacabadabacabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",k = 20) == "abcdefghijklmnoq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",k = 20) == "abcdefghijklmnoq": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababacababaca",k = 26) == "aabababacababacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababacababaca",k = 26) == "aabababacababacb": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhaaggeeffddccbb",k = 26) == "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhaaggeeffddccbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhaaggeeffddccbb",k = 26) == "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhaaggeeffddccbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad",k = 4) == "abacabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad",k = 4) == "abacabca": {e}')
    
    total += 1
    try:
        result = candidate(s = "acb",k = 3) == "bac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acb",k = 3) == "bac": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyx",k = 26) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyx",k = 26) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 26) == "aabbccddeefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 26) == "aabbccddeefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbac",k = 26) == "abcbad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbac",k = 26) == "abcbad": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",k = 16) == "abcdefghijklmnpa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",k = 16) == "abcdefghijklmnpa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 6) == "abcabcabcabd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 6) == "abcabcabcabd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",k = 26) == "abacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",k = 26) == "abacabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbac",k = 5) == "abacbacbad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbac",k = 5) == "abacbacbad": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba",k = 5) == "abcdcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba",k = 5) == "abcdcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",k = 26) == "abcdefgabcdefh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",k = 26) == "abcdefgabcdefh": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 4) == "abcdabcdabda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 4) == "abcdabcdabda": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == "zyxwvutsrqponmlkjihgfedcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == "zyxwvutsrqponmlkjihgfedcbd": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcd",k = 5) == "abce"
    assert candidate(s = "aabbcc",k = 6) == "aabbcd"
    assert candidate(s = "zyx",k = 26) == ""
    assert candidate(s = "abcz",k = 26) == "abda"
    assert candidate(s = "aaa",k = 4) == "aab"
    assert candidate(s = "dc",k = 4) == ""
    assert candidate(s = "aab",k = 3) == "aac"
    assert candidate(s = "abcd",k = 4) == "abda"
    assert candidate(s = "xyz",k = 26) == "xza"
    assert candidate(s = "zyx",k = 3) == ""
    assert candidate(s = "aabb",k = 4) == "aabc"
    assert candidate(s = "azzzz",k = 26) == "bacba"
    assert candidate(s = "abcabcabcabc",k = 3) == "acbacbacbacb"
    assert candidate(s = "abcabca",k = 26) == "abcabcd"
    assert candidate(s = "aabababa",k = 6) == "aabababc"
    assert candidate(s = "zzzzz",k = 26) == ""
    assert candidate(s = "abcabcabcabc",k = 26) == "abcabcabcabd"
    assert candidate(s = "zyxzyxzyxzyx",k = 26) == ""
    assert candidate(s = "wxyz",k = 26) == "wxza"
    assert candidate(s = "zzzzzzzzzz",k = 26) == ""
    assert candidate(s = "mnopqrstuvw",k = 21) == "mnopqrsuabc"
    assert candidate(s = "zyxwvutsr",k = 19) == ""
    assert candidate(s = "abcdefg",k = 7) == "abcdega"
    assert candidate(s = "abcdefghijklmnop",k = 26) == "abcdefghijklmnoq"
    assert candidate(s = "mnopqr",k = 18) == "mnopra"
    assert candidate(s = "lkjihgf",k = 12) == "lkjihgi"
    assert candidate(s = "abcabc",k = 3) == "acbacb"
    assert candidate(s = "abcdefghij",k = 10) == "abcdefghja"
    assert candidate(s = "aabccba",k = 15) == "aabccbd"
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 26) == "mnbvcxzlkjhgfdsapoiuytrewr"
    assert candidate(s = "ababababababab",k = 3) == "ababababababac"
    assert candidate(s = "abcabcabcabcabc",k = 3) == "acbacbacbacbacb"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyza",k = 26) == "abcdefghijklmnopqrstuvwxyzb"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrstabcabcabcabcab"
    assert candidate(s = "abcdefghijklmnopqrstuv",k = 21) == "abcdefghijklmnopqrsuab"
    assert candidate(s = "zzzzzz",k = 4) == ""
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyzab"
    assert candidate(s = "abcdabcd",k = 4) == "abcdabda"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz",k = 26) == ""
    assert candidate(s = "abcaabcd",k = 26) == "abcaabce"
    assert candidate(s = "mnopqrlmno",k = 14) == "mnopqrlnab"
    assert candidate(s = "abcdcba",k = 10) == "abcdcbd"
    assert candidate(s = "abcdefghijklmnopqrstuvwxzz",k = 26) == "abcdefghijklmnopqrstuvwyab"
    assert candidate(s = "abcdefghijk",k = 12) == "abcdefghijl"
    assert candidate(s = "abcdefghijk",k = 11) == "abcdefghika"
    assert candidate(s = "abba",k = 26) == "abbc"
    assert candidate(s = "abababababab",k = 26) == "abababababac"
    assert candidate(s = "aaaabbbbccccdddd",k = 26) == "aaaabbbbccccddde"
    assert candidate(s = "abcabcabc",k = 3) == "acbacbacb"
    assert candidate(s = "abcdcba",k = 26) == "abcdcbd"
    assert candidate(s = "abcdexyz",k = 26) == "abcdexza"
    assert candidate(s = "pqrs",k = 18) == "prab"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 26) == "qwertyuiopasdfghjklzxcvbno"
    assert candidate(s = "xyzabc",k = 26) == "xyzabd"
    assert candidate(s = "abacabadabacaba",k = 26) == "abacabadabacabc"
    assert candidate(s = "aabbccdd",k = 6) == "aabbccde"
    assert candidate(s = "zzzz",k = 4) == ""
    assert candidate(s = "aabbaabbaabb",k = 6) == "aabbaabbaabc"
    assert candidate(s = "abcde",k = 5) == "abcea"
    assert candidate(s = "mnopqrstuvw",k = 22) == "mnopqrstvab"
    assert candidate(s = "abcdexyzabcd",k = 26) == "abcdexyzabce"
    assert candidate(s = "abacabacabacaba",k = 3) == "abacabacabacabc"
    assert candidate(s = "abacabadabc",k = 26) == "abacabadabd"
    assert candidate(s = "xyzxyzxyzxyz",k = 26) == "xzabcabcabca"
    assert candidate(s = "abcbabcba",k = 3) == "abcbacbac"
    assert candidate(s = "abcdefghij",k = 26) == "abcdefghik"
    assert candidate(s = "abac",k = 4) == "abad"
    assert candidate(s = "abcabcabc",k = 26) == "abcabcabd"
    assert candidate(s = "abcba",k = 3) == "acbac"
    assert candidate(s = "abcdefghi",k = 10) == "abcdefghj"
    assert candidate(s = "aabbaa",k = 6) == "aabbac"
    assert candidate(s = "abcdefghi",k = 9) == "abcdefgia"
    assert candidate(s = "zyxcba",k = 6) == "zyxcbd"
    assert candidate(s = "mnopqrstuvwxyzz",k = 26) == "mnopqrstuvwxzab"
    assert candidate(s = "zzzzzzzzz",k = 26) == ""
    assert candidate(s = "aabbccddeeffgg",k = 6) == "aabbccddefabca"
    assert candidate(s = "abacabadabacaba",k = 15) == "abacabadabacabc"
    assert candidate(s = "abcdefghijklmnopqrstuvwxy",k = 26) == "abcdefghijklmnopqrstuvwxz"
    assert candidate(s = "abcdabc",k = 26) == "abcdabd"
    assert candidate(s = "fedcba",k = 6) == "fedcbd"
    assert candidate(s = "aabbccddeeffgg",k = 10) == "aabbccddeeffgh"
    assert candidate(s = "mnopqrstu",k = 20) == "mnopqrtab"
    assert candidate(s = "abcdefg",k = 8) == "abcdefh"
    assert candidate(s = "abababababab",k = 2) == "baababababab"
    assert candidate(s = "abcddcba",k = 20) == "abcddcbd"
    assert candidate(s = "abacaba",k = 7) == "abacabc"
    assert candidate(s = "abacabadabacaba",k = 3) == "abacabadabacabc"
    assert candidate(s = "abcdefghijklmnop",k = 20) == "abcdefghijklmnoq"
    assert candidate(s = "aabababacababaca",k = 26) == "aabababacababacb"
    assert candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhaaggeeffddccbb",k = 26) == "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhaaggeeffddccbd"
    assert candidate(s = "abacabad",k = 4) == "abacabca"
    assert candidate(s = "acb",k = 3) == "bac"
    assert candidate(s = "zyxzyxzyx",k = 26) == ""
    assert candidate(s = "aabbccddeeff",k = 26) == "aabbccddeefg"
    assert candidate(s = "abcbac",k = 26) == "abcbad"
    assert candidate(s = "abcdefghijklmnop",k = 16) == "abcdefghijklmnpa"
    assert candidate(s = "abcabcabcabc",k = 6) == "abcabcabcabd"
    assert candidate(s = "abacaba",k = 26) == "abacabc"
    assert candidate(s = "abacbacbac",k = 5) == "abacbacbad"
    assert candidate(s = "abcdcba",k = 5) == "abcdcbd"
    assert candidate(s = "abcdefgabcdefg",k = 26) == "abcdefgabcdefh"
    assert candidate(s = "abcdabcdabcd",k = 4) == "abcdabcdabda"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == "zyxwvutsrqponmlkjihgfedcbd"


