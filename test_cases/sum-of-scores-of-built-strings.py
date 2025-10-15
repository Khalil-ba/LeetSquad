def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "babab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "azbazbzaz") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "azbazbzaz") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazaz") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazaz") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabb") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabb") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbb") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbb") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcb") == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcb") == 180: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxy") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxy") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyzyxzyxzyxzyxzyxzyxzyx") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyzyxzyxzyxzyxzyxzyxzyx") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccaaaabbbbcccc") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccaaaabbbbcccc") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippimississippimississippi") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippimississippimississippi") == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabaaaa") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabaaaa") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotor") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotor") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcd") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcd") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzz") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzz") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkiijjhhggffeeddccbbbaaa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkiijjhhggffeeddccbbbaaa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabaaaaaaaaab") == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabaaaaaaaaab") == 111: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabca") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabca") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabca") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabca") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabad") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabad") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab") == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab") == 272: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccdddd") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccdddd") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccdddd") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccdddd") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccddddeeeee") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccddddeeeee") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == 234: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcbafedcbafedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcbafedcbafedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippi") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippi") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == 273
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == 273: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 630: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabanana") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabanana") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcab") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcab") == 77: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 612
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 612: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopqwertyuiop") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopqwertyuiop") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 145: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghjihgfedcba") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghjihgfedcba") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "acabacabacabacabacabacabacabacabacabacab") == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acabacabacabacabacabacabacabacabacabacab") == 230: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 165: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 360: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcab") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcab") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 408: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcba") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcba") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbaabcdeedcba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbaabcdeedcba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababab") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababab") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevel") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevel") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaa") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaa") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopqwertyuiopqwertyuiopqwertyuiop") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopqwertyuiopqwertyuiopqwertyuiop") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananab") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananab") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 666: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 315: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyzxzyzxzyzxzyz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyzxzyzxzyzxzyz") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == 272: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyzyxzyxzyxzyxzyx") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyzyxzyxzyxzyxzyx") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaabcdedcba") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaabcdedcba") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbafedcbafedcbafedcbafedcba") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbafedcbafedcbafedcbafedcba") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbccddeeffgg") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbccddeeffgg") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaa") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaa") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecar") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecar") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 525: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbccccc") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbccccc") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbccccdddd") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbccccdddd") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcba") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcba") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababcabababa") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababcabababa") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdbabc") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdbabc") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab") == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab") == 156: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacab") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacab") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "civic") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civic") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabc") == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabc") == 135: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazbzcbzazbzcb") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazbzcbzazbzcb") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 108: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == 198: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcab") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcab") == 57: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 2211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 2211: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdeabcdeabc") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdeabcdeabc") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohello") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohello") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzy") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzy") == 60: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "xyzxyzxyz") == 18
    assert candidate(s = "abcabcabc") == 18
    assert candidate(s = "aabbcc") == 7
    assert candidate(s = "abacabadabacaba") == 32
    assert candidate(s = "zzzzz") == 15
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "abacaba") == 12
    assert candidate(s = "babab") == 9
    assert candidate(s = "azbazbzaz") == 14
    assert candidate(s = "abcde") == 5
    assert candidate(s = "zazazaz") == 16
    assert candidate(s = "aaaaa") == 15
    assert candidate(s = "aabbaabb") == 14
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "a") == 1
    assert candidate(s = "abcdefg") == 7
    assert candidate(s = "aabbccddeeff") == 13
    assert candidate(s = "aaaaaaaaaabbbbbbbbbb") == 65
    assert candidate(s = "abacabadabacabadabacaba") == 60
    assert candidate(s = "abcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcb") == 180
    assert candidate(s = "xyxyxyxyxyxyxyxy") == 72
    assert candidate(s = "zxyzyxzyxzyxzyxzyxzyxzyx") == 31
    assert candidate(s = "aaaabbbbccccaaaabbbbcccc") == 48
    assert candidate(s = "mississippimississippimississippimississippi") == 110
    assert candidate(s = "aaaaaaaaaabaaaa") == 70
    assert candidate(s = "rotorrotor") == 17
    assert candidate(s = "abracadabra") == 18
    assert candidate(s = "abcabcabcabc") == 30
    assert candidate(s = "abcabcabcabcabcd") == 46
    assert candidate(s = "zzzzzzzzzzzzzzz") == 120
    assert candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkiijjhhggffeeddccbbbaaa") == 55
    assert candidate(s = "aaaaaaaaaabaaaaaaaaab") == 111
    assert candidate(s = "abcabcabcabcabcabca") == 70
    assert candidate(s = "abcabcabcabca") == 35
    assert candidate(s = "abcdabcdabcd") == 24
    assert candidate(s = "abacabadabacabad") == 34
    assert candidate(s = "abababababababababababababababab") == 272
    assert candidate(s = "aaaaabbbbccccdddd") == 27
    assert candidate(s = "aaaaabbbbbccccdddd") == 28
    assert candidate(s = "aaaaabbbbb") == 20
    assert candidate(s = "aaaaabbbbccccddddeeeee") == 32
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == 234
    assert candidate(s = "abcdefedcbafedcbafedcba") == 26
    assert candidate(s = "mississippimississippi") == 33
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == 273
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 630
    assert candidate(s = "aabbaabbaabbaabb") == 44
    assert candidate(s = "bananaananabanana") == 23
    assert candidate(s = "abcabcabcabcabcabcab") == 77
    assert candidate(s = "abcabcabcabcabcabcabc") == 84
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 612
    assert candidate(s = "qwertyuiopqwertyuiop") == 30
    assert candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 145
    assert candidate(s = "abcdefghjihgfedcba") == 19
    assert candidate(s = "acabacabacabacabacabacabacabacabacabacab") == 230
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 165
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 360
    assert candidate(s = "abcabcabcab") == 26
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 408
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26
    assert candidate(s = "abcdefedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcbafedcba") == 75
    assert candidate(s = "abcdeedcbaabcdeedcba") == 32
    assert candidate(s = "ababababababab") == 56
    assert candidate(s = "abcdeedcba") == 11
    assert candidate(s = "abababababababab") == 72
    assert candidate(s = "noon") == 5
    assert candidate(s = "abababababab") == 42
    assert candidate(s = "ababababababababab") == 90
    assert candidate(s = "abcabcabcabcabcabc") == 63
    assert candidate(s = "aabbccddeeffgghhii") == 19
    assert candidate(s = "abcdabcdabcdabcd") == 40
    assert candidate(s = "level") == 6
    assert candidate(s = "levellevellevel") == 33
    assert candidate(s = "abcdabcdabcdabcdabcd") == 60
    assert candidate(s = "abcdefghijk") == 11
    assert candidate(s = "aaaaaaaaaaa") == 66
    assert candidate(s = "qwertyuiopqwertyuiopqwertyuiopqwertyuiop") == 100
    assert candidate(s = "bananaananab") == 13
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 666
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 315
    assert candidate(s = "banana") == 6
    assert candidate(s = "zzyzxzyzxzyzxzyz") == 24
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == 272
    assert candidate(s = "zxyzyxzyxzyxzyxzyx") == 23
    assert candidate(s = "abracadabraabracadabra") == 47
    assert candidate(s = "abcdedcbaabcdedcba") == 29
    assert candidate(s = "abcdefghij") == 10
    assert candidate(s = "abcdedcbafedcbafedcbafedcbafedcba") == 38
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 53
    assert candidate(s = "aabbccddeeffgghhiijj") == 21
    assert candidate(s = "aabbccddeeffaabbccddeeff") == 38
    assert candidate(s = "aaaaaabbccddeeffgg") == 33
    assert candidate(s = "aaaaabbbbbaaaaa") == 40
    assert candidate(s = "racecarracecar") == 23
    assert candidate(s = "abacabadabacabadabacabad") == 63
    assert candidate(s = "deified") == 8
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 525
    assert candidate(s = "aaaaaabbbbbccccc") == 31
    assert candidate(s = "aaaaaabbbbccccdddd") == 33
    assert candidate(s = "abcbaabcbaabcba") == 33
    assert candidate(s = "ababababcabababa") == 44
    assert candidate(s = "abcdabcdbabc") == 19
    assert candidate(s = "abababababababababababab") == 156
    assert candidate(s = "ababababab") == 30
    assert candidate(s = "abacabadabacabadabacab") == 55
    assert candidate(s = "civic") == 6
    assert candidate(s = "rotor") == 6
    assert candidate(s = "racecar") == 8
    assert candidate(s = "abcabcabcabcabcabcabcabcabc") == 135
    assert candidate(s = "abcdefghijabcdefghij") == 30
    assert candidate(s = "zazbzcbzazbzcb") == 25
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 108
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 46
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == 198
    assert candidate(s = "abcabcabcabcabcab") == 57
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 2211
    assert candidate(s = "abcdefabcdeabcdeabc") == 32
    assert candidate(s = "mississippi") == 11
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz") == 71
    assert candidate(s = "hellohellohellohello") == 50
    assert candidate(s = "abcabcabcabcabc") == 45
    assert candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzy") == 60


