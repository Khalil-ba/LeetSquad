def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dddbbbccccaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dddbbbccccaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xyzxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xyzxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abcabcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abcabcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "",target = "a") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "",target = "a") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "abcbc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "abcbc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "ababd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "ababd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "zzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "zzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "adbc",target = "abcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "adbc",target = "abcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xzyxz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xzyxz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "da") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "da") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "edcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "edcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "ab",target = "bab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ab",target = "bab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "cba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "cba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "aaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "aaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = "ab",target = "bababababa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ab",target = "bababababa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "aabbccdd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "aabbccdd") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "ab",target = "bba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ab",target = "bba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "ddcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "ddcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "acdbc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "acdbc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "zzz",target = "zzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zzz",target = "zzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "cbabcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "cbabcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "eabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "eabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "b") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "b") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "aabcbcbabccbaabbccba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "aabcbcbabccbaabbccba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnop",target = "ponmponmponmponm") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnop",target = "ponmponmponmponm") == 13: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xyzzxyzzxyzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xyzzxyzzxyzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "qwertyuiopasdfghjklzxcvbnm",target = "mlkjihgfedcbapoiuytrewq") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "qwertyuiopasdfghjklzxcvbnm",target = "mlkjihgfedcbapoiuytrewq") == 19: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abacabadabacaba",target = "abacabadabacabadabacabadabacabad") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abacabadabacaba",target = "abacabadabacabadabacabadabacabad") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "source",target = "target") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "source",target = "target") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dcbaabcdabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dcbaabcdabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "abababcbcbccba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "abababcbcbccba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = "zxy",target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zxy",target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 34: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "ddddccbbbaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "ddddccbbbaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "abac",target = "abacabacabac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abac",target = "abacabacabac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "mnopqrnopqrmonpqrmnopqrmno") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "mnopqrnopqrmonpqrmnopqrmno") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabc",target = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabc",target = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "gfedcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "gfedcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "qrpqrpmnopqm") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "qrpqrpmnopqm") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "hello",target = "hellohellohello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "hello",target = "hellohellohello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdabcd",target = "dcbaabcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdabcd",target = "dcbaabcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "ecbaecba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "ecbaecba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabc",target = "aaaaaaabbbbbbcccccc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabc",target = "aaaaaaabbbbbbcccccc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "acbacbacbacbacbacbacbacb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "acbacbacbacbacbacbacbacb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xzyzxzyzxzyzxzyzxzyz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xzyzxzyzxzyzxzyzxzyz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xyzxyzxyzxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xyzxyzxyzxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdabcd",target = "dcbaabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdabcd",target = "dcbaabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "gfedcbagfedcbagfedcbagfedcbagfedcba") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "gfedcbagfedcbagfedcbagfedcbagfedcba") == 31: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "qrstmnopqrnopqrmnqr") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "qrstmnopqrnopqrmnqr") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzzyx",target = "zyxzyxzyxzyxzyx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzzyx",target = "zyxzyxzyxzyxzyx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdabcdabcdabcd",target = "ddddccccbbbaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdabcdabcdabcd",target = "ddddccccbbbaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fedcbafedcbafedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fedcbafedcbafedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "gfedcbagfedcbagfedcbagfedcbagfedcbagfedcba") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "gfedcbagfedcbagfedcbagfedcbagfedcbagfedcba") == 37: {e}')
    
    total += 1
    try:
        result = candidate(source = "source",target = "targesourcetarge") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "source",target = "targesourcetarge") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "zzzzzz",target = "zzzzzzzzzzzzzzzzzzzzzzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zzzzzz",target = "zzzzzzzzzzzzzzzzzzzzzzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "cbbacbacbacbacbacbacbacb") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "cbbacbacbacbacbacbacbacb") == 17: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "zyxzyxzyxzyxzyxzyx") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "zyxzyxzyxzyxzyxzyx") == 13: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "ddddaaaabbbcc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "ddddaaaabbbcc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dddddddd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dddddddd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "mnopqrnopqr") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "mnopqrnopqr") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "aaaabbbcccdddeeee") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "aaaabbbcccdddeeee") == 13: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaa",target = "aaaaaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaa",target = "aaaaaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "aaaaaaaaaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "aaaaaaaaaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fedcbafedcba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fedcbafedcba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgh",target = "aehgfbcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgh",target = "aehgfbcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abracadabra",target = "cadabraabra") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abracadabra",target = "cadabraabra") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcb") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcb") == 66: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "gfedcbaabcdefgabcdefg") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "gfedcbaabcdefgabcdefg") == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabc",target = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabc",target = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "gfedcbaedcbafe") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "gfedcbaedcbafe") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "xyzxyzxyzxyzxyzxyzxyz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "xyzxyzxyzxyzxyzxyzxyz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "acbacbacb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "acbacbacb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzz",target = "xyzzxyzzxyzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzz",target = "xyzzxyzzxyzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "ggfeeedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "ggfeeedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(source = "qwerty",target = "rteyqwrteyqw") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "qwerty",target = "rteyqwrteyqw") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fedcbafedcbafedcbafedcba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fedcbafedcbafedcbafedcba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(source = "sourcestring",target = "targetstring") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "sourcestring",target = "targetstring") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "hello",target = "ohellhello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "hello",target = "ohellhello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "abcdefgabcdefgabcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "abcdefgabcdefgabcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "z",target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "z",target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 44: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "fgfedcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "fgfedcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "edcbaedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "edcbaedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzxyz",target = "zyxzyxzyxzyx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzxyz",target = "zyxzyxzyxzyx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "aabbccddeeffgghhiijj") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "aabbccddeeffgghhiijj") == 11: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaa",target = "aaaaab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaa",target = "aaaaab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaa",target = "aaaaaaaaaaaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaa",target = "aaaaaaaaaaaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "ababcbcababc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "ababcbcababc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "dcbadcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "dcbadcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fdecbaedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fdecbaedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "pqrs",target = "psqprqspqs") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "pqrs",target = "psqprqspqs") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "qwertyuiop",target = "yuiopqwertyuiop") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "qwertyuiop",target = "yuiopqwertyuiop") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgh",target = "hgfedcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgh",target = "hgfedcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "cababc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "cababc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccdd",target = "aabbccddaabbccddaabbccdd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccdd",target = "aabbccddaabbccddaabbccdd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "cabcabcabcabcabcabcabcabcabcabcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "cabcabcabcabcabcabcabcabcabcabcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "deabcdeabcdeabcde") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "deabcdeabcdeabcde") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyxyxyxyxy",target = "yyyyxxxxxx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyxyxyxyxy",target = "yyyyxxxxxx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 110: {e}')
    
    total += 1
    try:
        result = candidate(source = "qwertyuiop",target = "poiuytrewqpoiuytrewqpoiuytrewq") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "qwertyuiop",target = "poiuytrewqpoiuytrewqpoiuytrewq") == 28: {e}')
    
    total += 1
    try:
        result = candidate(source = "source",target = "sourcesourcesource") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "source",target = "sourcesourcesource") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "caabbcccbaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "caabbcccbaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "abcabcabcaabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "abcabcabcaabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "aaaaaaaaabbbbbbbbbbcccccccccc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "aaaaaaaaabbbbbbbbbbcccccccccc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "aaaaabbbbbcccc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "aaaaabbbbbcccc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "sourcestring",target = "stringsources") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "sourcestring",target = "stringsources") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "jihgfedcbaedcbafedcbaedcbafedcbaedcbaedcba") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "jihgfedcbaedcbafedcbaedcbafedcbaedcbaedcba") == 36: {e}')
    
    total += 1
    try:
        result = candidate(source = "abacabadabacaba",target = "abadabadabadaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abacabadabacaba",target = "abadabadabadaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "ababababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "ababababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "zzz",target = "zzzzzzzzzzzzzzzzzzzz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zzz",target = "zzzzzzzzzzzzzzzzzzzz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzxyzxyz",target = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzxyzxyz",target = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzz",target = "xyzzyxyzzxyzzy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzz",target = "xyzzyxyzzxyzzy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "qponmlqponml") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "qponmlqponml") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "nopqmnopqmonpqmonpqmonpq") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "nopqmnopqmonpqmonpqmonpq") == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "ponmqrponmqrponmqrponmr") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "ponmqrponmqrponmqrponmr") == 16: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnop",target = "mnonpmnmonponmpnonpmnon") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnop",target = "mnonpmnmonponmpnonpmnon") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "abccbaabccba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "abccbaabccba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = "ab",target = "bababababababab") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ab",target = "bababababababab") == 8: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "gfedcbaedcbaedcbaedcbaedcba") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "gfedcbaedcbaedcbaedcbaedcba") == 23: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdabcd",target = "abcdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdabcd",target = "abcdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "abacabacbacb") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "abacabacbacb") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "zyxwvutsrqponmlkjihgfedcba",target = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zyxwvutsrqponmlkjihgfedcba",target = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abcdabcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abcdabcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abcde") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abcde") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fedcbaabcdeffedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fedcbaabcdeffedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "abcabcabcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "abcabcabcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fdecbaabcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fdecbaabcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "mnopmnopqr") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "mnopmnopqr") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abdbacd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abdbacd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "ab",target = "abababababababababababababab") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ab",target = "abababababababababababababab") == 14: {e}')
    
    total += 1
    try:
        result = candidate(source = "a",target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "a",target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 40: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "edcbaedcbaedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "edcbaedcbaedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(source = "abc",target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abc",target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "pnmlqrpnmlqr") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "pnmlqrpnmlqr") == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "ab",target = "bababababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ab",target = "bababababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabc",target = "ccccbbbbaaaacccbbbbaaaacccbbbbaaaacccbbbbaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabc",target = "ccccbbbbaaaacccbbbbaaaacccbbbbaaaacccbbbbaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaabbbccc",target = "abcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaabbbccc",target = "abcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "acbacbacbacbacbacbacbacb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "acbacbacbacbacbacbacbacb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "ddbaccbbadab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "ddbaccbbadab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "jihgfedcbaabcdefghijabcdefghij") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "jihgfedcbaabcdefghijabcdefghij") == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyz",target = "zyxzyxzyx") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyz",target = "zyxzyxzyx") == 7: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "afgeabfg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "afgeabfg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabc",target = "abcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabc",target = "abcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabc",target = "abcabcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabc",target = "abcabcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "abcdabcdabcdabcdabcd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "abcdabcdabcdabcdabcd") == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(source = "abcd",target = "dddbbbccccaaa") == 12
    assert candidate(source = "a",target = "a") == 1
    assert candidate(source = "xyz",target = "xyzxyz") == 2
    assert candidate(source = "abcd",target = "abcabcdabcd") == 3
    assert candidate(source = "",target = "a") == -1
    assert candidate(source = "abcd",target = "dabcd") == 2
    assert candidate(source = "abc",target = "abcbc") == 2
    assert candidate(source = "abcd",target = "ababd") == 2
    assert candidate(source = "xyz",target = "zzz") == 3
    assert candidate(source = "adbc",target = "abcd") == 2
    assert candidate(source = "xyz",target = "xzyxz") == 3
    assert candidate(source = "abcd",target = "da") == 2
    assert candidate(source = "abcde",target = "edcba") == 5
    assert candidate(source = "ab",target = "bab") == 2
    assert candidate(source = "abcd",target = "a") == 1
    assert candidate(source = "abc",target = "") == 0
    assert candidate(source = "abc",target = "cba") == 3
    assert candidate(source = "a",target = "aaaa") == 4
    assert candidate(source = "abcd",target = "") == 0
    assert candidate(source = "ab",target = "bababababa") == 6
    assert candidate(source = "abcd",target = "abc") == 1
    assert candidate(source = "abcd",target = "aabbccdd") == 5
    assert candidate(source = "a",target = "aa") == 2
    assert candidate(source = "ab",target = "bba") == 3
    assert candidate(source = "abcd",target = "ddcba") == 5
    assert candidate(source = "abc",target = "acdbc") == -1
    assert candidate(source = "zzz",target = "zzzzz") == 2
    assert candidate(source = "abcde",target = "cbabcde") == 3
    assert candidate(source = "abcde",target = "eabcd") == 2
    assert candidate(source = "abcd",target = "dddd") == 4
    assert candidate(source = "a",target = "b") == -1
    assert candidate(source = "abcd",target = "abcabcabc") == 3
    assert candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == 25
    assert candidate(source = "abc",target = "aabcbcbabccbaabbccba") == 13
    assert candidate(source = "mnop",target = "ponmponmponmponm") == 13
    assert candidate(source = "xyz",target = "xyzzxyzzxyzz") == 6
    assert candidate(source = "qwertyuiopasdfghjklzxcvbnm",target = "mlkjihgfedcbapoiuytrewq") == 19
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3
    assert candidate(source = "abacabadabacaba",target = "abacabadabacabadabacabadabacabad") == 4
    assert candidate(source = "source",target = "target") == -1
    assert candidate(source = "abcd",target = "dcbaabcdabcd") == 6
    assert candidate(source = "aabbcc",target = "abababcbcbccba") == 7
    assert candidate(source = "xyz",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 10
    assert candidate(source = "zxy",target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 34
    assert candidate(source = "abcd",target = "ddddccbbbaaa") == 12
    assert candidate(source = "abac",target = "abacabacabac") == 3
    assert candidate(source = "mnopqr",target = "mnopqrnopqrmonpqrmnopqrmno") == 6
    assert candidate(source = "abcabcabcabc",target = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 17
    assert candidate(source = "abcdefg",target = "gfedcba") == 7
    assert candidate(source = "abcde",target = "abcabcabc") == 3
    assert candidate(source = "mnopqr",target = "qrpqrpmnopqm") == 5
    assert candidate(source = "hello",target = "hellohellohello") == 3
    assert candidate(source = "abcdabcd",target = "dcbaabcdabcd") == 3
    assert candidate(source = "abcde",target = "ecbaecba") == 7
    assert candidate(source = "abcabc",target = "aaaaaaabbbbbbcccccc") == 9
    assert candidate(source = "abc",target = "acbacbacbacbacbacbacbacb") == 16
    assert candidate(source = "xyz",target = "xzyzxzyzxzyzxzyzxzyz") == 10
    assert candidate(source = "xyz",target = "xyzxyzxyzxyz") == 4
    assert candidate(source = "abcdabcd",target = "dcbaabcd") == 3
    assert candidate(source = "abcdefg",target = "gfedcbagfedcbagfedcbagfedcbagfedcba") == 31
    assert candidate(source = "mnopqr",target = "qrstmnopqrnopqrmnqr") == -1
    assert candidate(source = "xyzzyx",target = "zyxzyxzyxzyxzyx") == 5
    assert candidate(source = "abcdabcdabcdabcd",target = "ddddccccbbbaaaa") == 4
    assert candidate(source = "abcdef",target = "fedcbafedcbafedcba") == 16
    assert candidate(source = "abcdefg",target = "gfedcbagfedcbagfedcbagfedcbagfedcbagfedcba") == 37
    assert candidate(source = "source",target = "targesourcetarge") == -1
    assert candidate(source = "zzzzzz",target = "zzzzzzzzzzzzzzzzzzzzzzzz") == 4
    assert candidate(source = "abc",target = "cbbacbacbacbacbacbacbacb") == 17
    assert candidate(source = "xyz",target = "zyxzyxzyxzyxzyxzyx") == 13
    assert candidate(source = "abcd",target = "ddddaaaabbbcc") == 11
    assert candidate(source = "abcd",target = "dddddddd") == 8
    assert candidate(source = "mnopqr",target = "mnopqrnopqr") == 2
    assert candidate(source = "abcde",target = "aaaabbbcccdddeeee") == 13
    assert candidate(source = "aaaaa",target = "aaaaaaaaaaa") == 3
    assert candidate(source = "a",target = "aaaaaaaaaa") == 10
    assert candidate(source = "abcdef",target = "fedcbafedcba") == 11
    assert candidate(source = "abcdefgh",target = "aehgfbcd") == 4
    assert candidate(source = "abracadabra",target = "cadabraabra") == 2
    assert candidate(source = "abcd",target = "dcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcbadcb") == 66
    assert candidate(source = "abcdefg",target = "gfedcbaabcdefgabcdefg") == 9
    assert candidate(source = "abcabcabc",target = "abc") == 1
    assert candidate(source = "abcdefg",target = "gfedcbaedcbafe") == 12
    assert candidate(source = "xyz",target = "xyzxyzxyzxyzxyzxyzxyz") == 7
    assert candidate(source = "abc",target = "acbacbacb") == 6
    assert candidate(source = "xyzz",target = "xyzzxyzzxyzz") == 3
    assert candidate(source = "abcdefg",target = "ggfeeedcba") == 10
    assert candidate(source = "qwerty",target = "rteyqwrteyqw") == 5
    assert candidate(source = "abcdef",target = "fedcbafedcbafedcbafedcba") == 21
    assert candidate(source = "sourcestring",target = "targetstring") == -1
    assert candidate(source = "hello",target = "ohellhello") == 3
    assert candidate(source = "abcdefg",target = "abcdefgabcdefgabcdefg") == 3
    assert candidate(source = "z",target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 44
    assert candidate(source = "abcdefg",target = "fgfedcba") == 7
    assert candidate(source = "abcde",target = "edcbaedcba") == 9
    assert candidate(source = "xyzxyz",target = "zyxzyxzyxzyx") == 5
    assert candidate(source = "abcdefghij",target = "aabbccddeeffgghhiijj") == 11
    assert candidate(source = "aaaa",target = "aaaaab") == -1
    assert candidate(source = "aabbcc",target = "abcabcabc") == 3
    assert candidate(source = "aaaa",target = "aaaaaaaaaaaaaa") == 4
    assert candidate(source = "abcde",target = "ababcbcababc") == 5
    assert candidate(source = "abcd",target = "dcbadcba") == 7
    assert candidate(source = "abcdef",target = "fdecbaedcba") == 9
    assert candidate(source = "pqrs",target = "psqprqspqs") == 5
    assert candidate(source = "qwertyuiop",target = "yuiopqwertyuiop") == 2
    assert candidate(source = "abcdefgh",target = "hgfedcba") == 8
    assert candidate(source = "abc",target = "cababc") == 3
    assert candidate(source = "aabbccdd",target = "aabbccddaabbccddaabbccdd") == 3
    assert candidate(source = "abc",target = "cabcabcabcabcabcabcabcabcabcabcabc") == 12
    assert candidate(source = "abcde",target = "deabcdeabcdeabcde") == 4
    assert candidate(source = "xyxyxyxyxy",target = "yyyyxxxxxx") == 2
    assert candidate(source = "a",target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 110
    assert candidate(source = "qwertyuiop",target = "poiuytrewqpoiuytrewqpoiuytrewq") == 28
    assert candidate(source = "source",target = "sourcesourcesource") == 3
    assert candidate(source = "abc",target = "caabbcccbaa") == 9
    assert candidate(source = "aabbcc",target = "abcabcabcaabbcc") == 4
    assert candidate(source = "abc",target = "aaaaaaaaabbbbbbbbbbcccccccccc") == 27
    assert candidate(source = "abc",target = "aaaaabbbbbcccc") == 12
    assert candidate(source = "sourcestring",target = "stringsources") == 2
    assert candidate(source = "abcdefghij",target = "jihgfedcbaedcbafedcbaedcbafedcbaedcbaedcba") == 36
    assert candidate(source = "abacabadabacaba",target = "abadabadabadaba") == 3
    assert candidate(source = "abcdef",target = "ababababab") == 5
    assert candidate(source = "zzz",target = "zzzzzzzzzzzzzzzzzzzz") == 7
    assert candidate(source = "xyzxyzxyz",target = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 7
    assert candidate(source = "xyzz",target = "xyzzyxyzzxyzzy") == 5
    assert candidate(source = "mnopqr",target = "qponmlqponml") == -1
    assert candidate(source = "mnopqr",target = "nopqmnopqmonpqmonpqmonpq") == 8
    assert candidate(source = "mnopqr",target = "ponmqrponmqrponmqrponmr") == 16
    assert candidate(source = "mnop",target = "mnonpmnmonponmpnonpmnon") == 12
    assert candidate(source = "abc",target = "abccbaabccba") == 8
    assert candidate(source = "ab",target = "bababababababab") == 8
    assert candidate(source = "abcdefg",target = "gfedcbaedcbaedcbaedcbaedcba") == 23
    assert candidate(source = "abcdabcd",target = "abcdabcdabcdabcd") == 2
    assert candidate(source = "aabbcc",target = "abacabacbacb") == 7
    assert candidate(source = "zyxwvutsrqponmlkjihgfedcba",target = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(source = "abcd",target = "abcdabcdabcd") == 3
    assert candidate(source = "abcd",target = "abcde") == -1
    assert candidate(source = "abcdef",target = "fedcbaabcdeffedcba") == 13
    assert candidate(source = "aabbcc",target = "abcabcabcabc") == 4
    assert candidate(source = "abcdef",target = "fdecbaabcdef") == 6
    assert candidate(source = "mnopqr",target = "mnopmnopqr") == 2
    assert candidate(source = "abcd",target = "abdbacd") == 3
    assert candidate(source = "ab",target = "abababababababababababababab") == 14
    assert candidate(source = "a",target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 40
    assert candidate(source = "abcde",target = "edcbaedcbaedcba") == 13
    assert candidate(source = "abc",target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(source = "mnopqr",target = "pnmlqrpnmlqr") == -1
    assert candidate(source = "ab",target = "bababababab") == 6
    assert candidate(source = "abcabcabcabc",target = "ccccbbbbaaaacccbbbbaaaacccbbbbaaaacccbbbbaaa") == 11
    assert candidate(source = "aaabbbccc",target = "abcabcabcabcabcabc") == 6
    assert candidate(source = "aabbcc",target = "acbacbacbacbacbacbacbacb") == 16
    assert candidate(source = "abcd",target = "ddbaccbbadab") == 9
    assert candidate(source = "abcdefghij",target = "jihgfedcbaabcdefghijabcdefghij") == 12
    assert candidate(source = "xyz",target = "zyxzyxzyx") == 7
    assert candidate(source = "abcdefg",target = "afgeabfg") == 3
    assert candidate(source = "abcabcabc",target = "abcabcabcabc") == 2
    assert candidate(source = "abcabcabc",target = "abcabcabcabcabc") == 2
    assert candidate(source = "abcd",target = "abcdabcdabcdabcdabcd") == 5


