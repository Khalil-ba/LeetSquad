def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(jewels = "aA",stones = "aAAbbbb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aA",stones = "aAAbbbb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyz",stones = "aabbcc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyz",stones = "aabbcc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyz",stones = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyz",stones = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "aA",stones = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aA",stones = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefg",stones = "aghfbadcegf") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefg",stones = "aghfbadcegf") == 10: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefg",stones = "aghgfedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefg",stones = "aghgfedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "",stones = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "",stones = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "XYZ",stones = "xyzbxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "XYZ",stones = "xyzbxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdef",stones = "fedcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdef",stones = "fedcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "J",stones = "jjjjjJ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "J",stones = "jjjjjJ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "aBcD",stones = "abCdEfGhIjKlMnOpQrStUvWxYz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aBcD",stones = "abCdEfGhIjKlMnOpQrStUvWxYz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "A",stones = "aAaAaA") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "A",stones = "aAaAaA") == 3: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "XYZ",stones = "xyzXYZxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "XYZ",stones = "xyzXYZxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "J",stones = "Jjjjjjjjjjj") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "J",stones = "Jjjjjjjjjjj") == 1: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "A",stones = "aA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "A",stones = "aA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyz",stones = "xyzzxyzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyz",stones = "xyzzxyzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "",stones = "aAAbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "",stones = "aAAbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "z",stones = "ZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "z",stones = "ZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abc",stones = "acbacba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abc",stones = "acbacba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abc",stones = "aaabbbccc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abc",stones = "aaabbbccc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefg",stones = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefg",stones = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyz",stones = "xyzzzyx") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyz",stones = "xyzzzyx") == 7: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ABC",stones = "abcABC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ABC",stones = "abcABC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abc",stones = "aabbcc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abc",stones = "aabbcc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "zyxwvutsrqponmlkjihgfedcbaZXCVBNMLKJIHGFEDCBA") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "zyxwvutsrqponmlkjihgfedcbaZXCVBNMLKJIHGFEDCBA") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ABCDEFGHIJK",stones = "ABCDEFGHIJKabcdefghijk") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ABCDEFGHIJK",stones = "ABCDEFGHIJKabcdefghijk") == 11: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqr",stones = "mnopqrzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqr",stones = "mnopqrzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdef",stones = "aabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdef",stones = "aabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqr",stones = "mnopqrstuvwxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqr",stones = "mnopqrstuvwxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ABCDEFGHIJKL",stones = "LJKIHFEDCBA") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ABCDEFGHIJKL",stones = "LJKIHFEDCBA") == 11: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqr",stones = "rstuvwrstuvwrstuvwrstuvw") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqr",stones = "rstuvwrstuvwrstuvwrstuvw") == 4: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "JKLMNO",stones = "PQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKL") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "JKLMNO",stones = "PQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKL") == 27: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "yza",stones = "yzayzayzayza") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "yza",stones = "yzayzayzayza") == 12: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "1234567890",stones = "09876543210123456789") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "1234567890",stones = "09876543210123456789") == 20: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "LMNOPQ",stones = "mnopqrLMNOPQ") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "LMNOPQ",stones = "mnopqrLMNOPQ") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "LMNOPQRSTU",stones = "LMNOPQRSTULMNOPQRSTUVWXYZ") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "LMNOPQRSTU",stones = "LMNOPQRSTULMNOPQRSTUVWXYZ") == 20: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "QWERTY",stones = "qwertyuiopasdfghjklzxcvbnmQWERTY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "QWERTY",stones = "qwertyuiopasdfghjklzxcvbnmQWERTY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "aAbBcC",stones = "aabbccAAzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aAbBcC",stones = "aabbccAAzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "pythonPYTHON",stones = "pythooonPYTHOOONpy") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "pythonPYTHON",stones = "pythooonPYTHOOONpy") == 18: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ABCDEFGHIJKL",stones = "abcdefghijlkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ABCDEFGHIJKL",stones = "abcdefghijlkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "javaJAVA",stones = "jjjaaaaavvvaaaAAAVVVAAA") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "javaJAVA",stones = "jjjaaaaavvvaaaAAAVVVAAA") == 23: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefghij",stones = "zzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefghij",stones = "zzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "AEIOU",stones = "aeiouAEIOUaeiouAEIOU") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "AEIOU",stones = "aeiouAEIOUaeiouAEIOU") == 10: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "fghij",stones = "jihgf") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "fghij",stones = "jihgf") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "zzzzzyyyxXxXyYy") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "zzzzzyyyxXxXyYy") == 15: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "pqrst",stones = "tsrpq") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "pqrst",stones = "tsrpq") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefghijk",stones = "ABCDEFGHIJKabcdefghijk") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefghijk",stones = "ABCDEFGHIJKabcdefghijk") == 11: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ghijkl",stones = "lkjihg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ghijkl",stones = "lkjihg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefg",stones = "abcdefgabcdefgabcdefg") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefg",stones = "abcdefgabcdefgabcdefg") == 21: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcde",stones = "edcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcde",stones = "edcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "QRSTUVWXYZ",stones = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "QRSTUVWXYZ",stones = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 10: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "123456",stones = "111222333444555666") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "123456",stones = "111222333444555666") == 18: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "z",stones = "zzzzzzzzzzzzzzzzzzzz") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "z",stones = "zzzzzzzzzzzzzzzzzzzz") == 20: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqr",stones = "mnopqrnopqrxyz") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqr",stones = "mnopqrnopqrxyz") == 11: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "aAbBcC",stones = "aAbBcCxxxyyyzzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aAbBcC",stones = "aAbBcCxxxyyyzzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "uvwxy",stones = "yxwvu") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "uvwxy",stones = "yxwvu") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "aAbBcC",stones = "abcABCabcABC") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aAbBcC",stones = "abcABCabcABC") == 12: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqr",stones = "mnoqrpmnopqrmmmnopqr") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqr",stones = "mnoqrpmnopqrmmmnopqr") == 20: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "QWJRTY",stones = "QWJRTYqwerty") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "QWJRTY",stones = "QWJRTYqwerty") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "Z",stones = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "Z",stones = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "JKLM",stones = "ABCDEFGHIJKLmnopqrstu") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "JKLM",stones = "ABCDEFGHIJKLmnopqrstu") == 3: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcABC",stones = "aAbBcCabcABC") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcABC",stones = "aAbBcCabcABC") == 12: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "qwertyuiopASDFGHJKLZXCVBNM",stones = "qwertyuiopASDFGHJKLZXCVBNMqwertyuiopASDFGHJKLZXCVBNM") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "qwertyuiopASDFGHJKLZXCVBNM",stones = "qwertyuiopASDFGHJKLZXCVBNMqwertyuiopASDFGHJKLZXCVBNM") == 52: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "",stones = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "",stones = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "QRSTU",stones = "UTSRQ") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "QRSTU",stones = "UTSRQ") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefgABCDEFG",stones = "gfedcbaGFEDCBAgfedcba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefgABCDEFG",stones = "gfedcbaGFEDCBAgfedcba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "LMNOPQ",stones = "PQLNOM") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "LMNOPQ",stones = "PQLNOM") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcABC",stones = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcABC",stones = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 3: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "zyxZYXzyxZYXzyxZYX") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "zyxZYXzyxZYXzyxZYX") == 18: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdef",stones = "fedcbafedcbafedcba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdef",stones = "fedcbafedcbafedcba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "xyzzzzyyxXXYYZZZ") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "xyzzzzyyxXXYYZZZ") == 16: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefg",stones = "hijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefg",stones = "hijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "MNOPQR",stones = "ZYXWVUTSRQPONMLKJIHGFEDCBA") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "MNOPQR",stones = "ZYXWVUTSRQPONMLKJIHGFEDCBA") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefghijkABCDEFGHIJK",stones = "abcdefghijkABCDEFGHIJK") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefghijkABCDEFGHIJK",stones = "abcdefghijkABCDEFGHIJK") == 22: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "GHIJKL",stones = "ghijklGHJKLMN") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "GHIJKL",stones = "ghijklGHJKLMN") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "aAbBcCxyzXYZ") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "aAbBcCxyzXYZ") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdef",stones = "abcdefabcdefabcdefabcdef") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdef",stones = "abcdefabcdefabcdefabcdef") == 24: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "klmnopqrKLMNOPQR",stones = "klmnopqrKLMNOPQR") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "klmnopqrKLMNOPQR",stones = "klmnopqrKLMNOPQR") == 16: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqr",stones = "mnopqrstoopqrmmn") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqr",stones = "mnopqrstoopqrmmn") == 14: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefghijABCDEFGHIJ",stones = "abcdefghijABCDEFGHIJ") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefghijABCDEFGHIJ",stones = "abcdefghijABCDEFGHIJ") == 20: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqrstuvwxyz",stones = "abcdefghijklmnopqrstuvwxyz") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqrstuvwxyz",stones = "abcdefghijklmnopqrstuvwxyz") == 14: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "mnopqrstuv",stones = "mlkjihgfdsazxcvbnm") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "mnopqrstuv",stones = "mlkjihgfdsazxcvbnm") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "klmno",stones = "onmlk") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "klmno",stones = "onmlk") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "123456",stones = "112233445566") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "123456",stones = "112233445566") == 12: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "rstuvw",stones = "vwutsr") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "rstuvw",stones = "vwutsr") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcABC",stones = "abcABCabcABC") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcABC",stones = "abcABCabcABC") == 12: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "stuvwxyzSTUVWXYZ",stones = "stuvwxyzSTUVWXYZ") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "stuvwxyzSTUVWXYZ",stones = "stuvwxyzSTUVWXYZ") == 16: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "",stones = "abcdefgABCDEFG") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "",stones = "abcdefgABCDEFG") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "xyzzzXXYyyZZZ") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "xyzzzXXYyyZZZ") == 13: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "worldWORLD",stones = "wwoorrllddWWOOORRLLDD") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "worldWORLD",stones = "wwoorrllddWWOOORRLLDD") == 21: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "qrstuv",stones = "qwertyuiopasdfghjklzxcvbnm") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "qrstuv",stones = "qwertyuiopasdfghjklzxcvbnm") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdef",stones = "fedcbaghijklmnopqrstuvwxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdef",stones = "fedcbaghijklmnopqrstuvwxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ",stones = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ",stones = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 52: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ABCDEFG",stones = "abcdefgABCDEFG") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ABCDEFG",stones = "abcdefgABCDEFG") == 7: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "xyzXYZ",stones = "xYzXyZxYzXyZxYzXyZ") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "xyzXYZ",stones = "xYzXyZxYzXyZxYzXyZ") == 18: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "helloHELLO",stones = "hheelloollleeHHHELLO") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "helloHELLO",stones = "hheelloollleeHHHELLO") == 20: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "ABCDEFGHIJ",stones = "ABCDEFGHIJabcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "ABCDEFGHIJ",stones = "ABCDEFGHIJabcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "asdfghjklzxcvbnm",stones = "qwertyuiopzxcvbnmasdfghjklqwertyuiop") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "asdfghjklzxcvbnm",stones = "qwertyuiopzxcvbnmasdfghjklqwertyuiop") == 16: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "VWXYZ",stones = "ZYXWV") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "VWXYZ",stones = "ZYXWV") == 5: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "hijklmnopqrstuvwxyz",stones = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "hijklmnopqrstuvwxyz",stones = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "abcdefghijklmnopqrstuvwxyz",stones = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "abcdefghijklmnopqrstuvwxyz",stones = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(jewels = "12345",stones = "5432167890") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jewels = "12345",stones = "5432167890") == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(jewels = "aA",stones = "aAAbbbb") == 3
    assert candidate(jewels = "xyz",stones = "aabbcc") == 0
    assert candidate(jewels = "xyz",stones = "") == 0
    assert candidate(jewels = "aA",stones = "") == 0
    assert candidate(jewels = "abcdefg",stones = "aghfbadcegf") == 10
    assert candidate(jewels = "abcdefg",stones = "aghgfedcba") == 9
    assert candidate(jewels = "",stones = "abcdefg") == 0
    assert candidate(jewels = "XYZ",stones = "xyzbxyz") == 0
    assert candidate(jewels = "abcdef",stones = "fedcba") == 6
    assert candidate(jewels = "J",stones = "jjjjjJ") == 1
    assert candidate(jewels = "aBcD",stones = "abCdEfGhIjKlMnOpQrStUvWxYz") == 1
    assert candidate(jewels = "A",stones = "aAaAaA") == 3
    assert candidate(jewels = "XYZ",stones = "xyzXYZxyz") == 3
    assert candidate(jewels = "J",stones = "Jjjjjjjjjjj") == 1
    assert candidate(jewels = "A",stones = "aA") == 1
    assert candidate(jewels = "xyz",stones = "xyzzxyzz") == 8
    assert candidate(jewels = "",stones = "aAAbbbb") == 0
    assert candidate(jewels = "z",stones = "ZZ") == 0
    assert candidate(jewels = "abc",stones = "acbacba") == 7
    assert candidate(jewels = "abc",stones = "aaabbbccc") == 9
    assert candidate(jewels = "abcdefg",stones = "") == 0
    assert candidate(jewels = "xyz",stones = "xyzzzyx") == 7
    assert candidate(jewels = "ABC",stones = "abcABC") == 3
    assert candidate(jewels = "abc",stones = "aabbcc") == 6
    assert candidate(jewels = "xyzXYZ",stones = "zyxwvutsrqponmlkjihgfedcbaZXCVBNMLKJIHGFEDCBA") == 5
    assert candidate(jewels = "xyzXYZ",stones = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 6
    assert candidate(jewels = "ABCDEFGHIJK",stones = "ABCDEFGHIJKabcdefghijk") == 11
    assert candidate(jewels = "mnopqr",stones = "mnopqrzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 6
    assert candidate(jewels = "abcdef",stones = "aabbccddeeff") == 12
    assert candidate(jewels = "mnopqr",stones = "mnopqrstuvwxyz") == 6
    assert candidate(jewels = "ABCDEFGHIJKL",stones = "LJKIHFEDCBA") == 11
    assert candidate(jewels = "mnopqr",stones = "rstuvwrstuvwrstuvwrstuvw") == 4
    assert candidate(jewels = "JKLMNO",stones = "PQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKLMNOPQRSTUJKL") == 27
    assert candidate(jewels = "yza",stones = "yzayzayzayza") == 12
    assert candidate(jewels = "1234567890",stones = "09876543210123456789") == 20
    assert candidate(jewels = "LMNOPQ",stones = "mnopqrLMNOPQ") == 6
    assert candidate(jewels = "LMNOPQRSTU",stones = "LMNOPQRSTULMNOPQRSTUVWXYZ") == 20
    assert candidate(jewels = "QWERTY",stones = "qwertyuiopasdfghjklzxcvbnmQWERTY") == 6
    assert candidate(jewels = "aAbBcC",stones = "aabbccAAzz") == 8
    assert candidate(jewels = "pythonPYTHON",stones = "pythooonPYTHOOONpy") == 18
    assert candidate(jewels = "ABCDEFGHIJKL",stones = "abcdefghijlkjihgfedcba") == 0
    assert candidate(jewels = "javaJAVA",stones = "jjjaaaaavvvaaaAAAVVVAAA") == 23
    assert candidate(jewels = "abcdefghij",stones = "zzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(jewels = "AEIOU",stones = "aeiouAEIOUaeiouAEIOU") == 10
    assert candidate(jewels = "fghij",stones = "jihgf") == 5
    assert candidate(jewels = "xyzXYZ",stones = "zzzzzyyyxXxXyYy") == 15
    assert candidate(jewels = "pqrst",stones = "tsrpq") == 5
    assert candidate(jewels = "abcdefghijk",stones = "ABCDEFGHIJKabcdefghijk") == 11
    assert candidate(jewels = "ghijkl",stones = "lkjihg") == 6
    assert candidate(jewels = "abcdefg",stones = "abcdefgabcdefgabcdefg") == 21
    assert candidate(jewels = "abcde",stones = "edcba") == 5
    assert candidate(jewels = "QRSTUVWXYZ",stones = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 10
    assert candidate(jewels = "123456",stones = "111222333444555666") == 18
    assert candidate(jewels = "z",stones = "zzzzzzzzzzzzzzzzzzzz") == 20
    assert candidate(jewels = "mnopqr",stones = "mnopqrnopqrxyz") == 11
    assert candidate(jewels = "aAbBcC",stones = "aAbBcCxxxyyyzzz") == 6
    assert candidate(jewels = "uvwxy",stones = "yxwvu") == 5
    assert candidate(jewels = "aAbBcC",stones = "abcABCabcABC") == 12
    assert candidate(jewels = "mnopqr",stones = "mnoqrpmnopqrmmmnopqr") == 20
    assert candidate(jewels = "QWJRTY",stones = "QWJRTYqwerty") == 6
    assert candidate(jewels = "Z",stones = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(jewels = "JKLM",stones = "ABCDEFGHIJKLmnopqrstu") == 3
    assert candidate(jewels = "abcABC",stones = "aAbBcCabcABC") == 12
    assert candidate(jewels = "qwertyuiopASDFGHJKLZXCVBNM",stones = "qwertyuiopASDFGHJKLZXCVBNMqwertyuiopASDFGHJKLZXCVBNM") == 52
    assert candidate(jewels = "",stones = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(jewels = "QRSTU",stones = "UTSRQ") == 5
    assert candidate(jewels = "abcdefgABCDEFG",stones = "gfedcbaGFEDCBAgfedcba") == 21
    assert candidate(jewels = "LMNOPQ",stones = "PQLNOM") == 6
    assert candidate(jewels = "abcABC",stones = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 3
    assert candidate(jewels = "xyzXYZ",stones = "zyxZYXzyxZYXzyxZYX") == 18
    assert candidate(jewels = "abcdef",stones = "fedcbafedcbafedcba") == 18
    assert candidate(jewels = "xyzXYZ",stones = "xyzzzzyyxXXYYZZZ") == 16
    assert candidate(jewels = "abcdefg",stones = "hijklmnopqrstuvwxyz") == 0
    assert candidate(jewels = "MNOPQR",stones = "ZYXWVUTSRQPONMLKJIHGFEDCBA") == 6
    assert candidate(jewels = "abcdefghijkABCDEFGHIJK",stones = "abcdefghijkABCDEFGHIJK") == 22
    assert candidate(jewels = "GHIJKL",stones = "ghijklGHJKLMN") == 5
    assert candidate(jewels = "xyzXYZ",stones = "aAbBcCxyzXYZ") == 6
    assert candidate(jewels = "abcdef",stones = "abcdefabcdefabcdefabcdef") == 24
    assert candidate(jewels = "klmnopqrKLMNOPQR",stones = "klmnopqrKLMNOPQR") == 16
    assert candidate(jewels = "mnopqr",stones = "mnopqrstoopqrmmn") == 14
    assert candidate(jewels = "abcdefghijABCDEFGHIJ",stones = "abcdefghijABCDEFGHIJ") == 20
    assert candidate(jewels = "mnopqrstuvwxyz",stones = "abcdefghijklmnopqrstuvwxyz") == 14
    assert candidate(jewels = "mnopqrstuv",stones = "mlkjihgfdsazxcvbnm") == 5
    assert candidate(jewels = "klmno",stones = "onmlk") == 5
    assert candidate(jewels = "123456",stones = "112233445566") == 12
    assert candidate(jewels = "rstuvw",stones = "vwutsr") == 6
    assert candidate(jewels = "abcABC",stones = "abcABCabcABC") == 12
    assert candidate(jewels = "stuvwxyzSTUVWXYZ",stones = "stuvwxyzSTUVWXYZ") == 16
    assert candidate(jewels = "",stones = "abcdefgABCDEFG") == 0
    assert candidate(jewels = "xyzXYZ",stones = "xyzzzXXYyyZZZ") == 13
    assert candidate(jewels = "worldWORLD",stones = "wwoorrllddWWOOORRLLDD") == 21
    assert candidate(jewels = "qrstuv",stones = "qwertyuiopasdfghjklzxcvbnm") == 6
    assert candidate(jewels = "abcdef",stones = "fedcbaghijklmnopqrstuvwxyz") == 6
    assert candidate(jewels = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ",stones = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 52
    assert candidate(jewels = "ABCDEFG",stones = "abcdefgABCDEFG") == 7
    assert candidate(jewels = "xyzXYZ",stones = "xYzXyZxYzXyZxYzXyZ") == 18
    assert candidate(jewels = "helloHELLO",stones = "hheelloollleeHHHELLO") == 20
    assert candidate(jewels = "ABCDEFGHIJ",stones = "ABCDEFGHIJabcdefghij") == 10
    assert candidate(jewels = "asdfghjklzxcvbnm",stones = "qwertyuiopzxcvbnmasdfghjklqwertyuiop") == 16
    assert candidate(jewels = "VWXYZ",stones = "ZYXWV") == 5
    assert candidate(jewels = "hijklmnopqrstuvwxyz",stones = "abcdefg") == 0
    assert candidate(jewels = "abcdefghijklmnopqrstuvwxyz",stones = "") == 0
    assert candidate(jewels = "12345",stones = "5432167890") == 5


