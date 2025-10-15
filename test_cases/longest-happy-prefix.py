def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "prefixprefix") == "prefix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixprefix") == "prefix": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaa") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaa") == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == "abacaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == "abacaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == "abcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == "abcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == "abcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == "abcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbaaaa") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbaaaa") == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "happy") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "happy") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == "n"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == "n": {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccdd") == "aabbccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccdd") == "aabbccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "suffix") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "suffix") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab") == "abab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab") == "abab": {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == "l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == "l": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacababacab") == "abacab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacababacab") == "abacab": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababcababab") == "ababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababcababab") == "ababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba") == "abacabadabacaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba") == "abacabadabacaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == "abcdefghijabcdefghijabcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == "abcdefghijabcdefghijabcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabay") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabay") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == "abra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == "abra": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef") == "abcdefabcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef") == "abcdefabcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == "abacabadabacabadabacabad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == "abacabadabacabadabacabad": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aababaabaababaaba") == "aababaaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababaabaababaaba") == "aababaaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaa") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaa") == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazazazazazazaz") == "zazazazazazazazazaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazazazazazazaz") == "zazazazazazazazazaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabca") == "abcabcabcabcabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabca") == "abcabcabcabcabca": {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabbaabba") == "abbaabbaabbaabbaabba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabbaabba") == "abbaabbaabbaabbaabba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaabaaabaabaabaaabaabaab") == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaabaaabaabaabaaabaabaab") == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippimississippimis") == "mississippimississippimis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippimississippimis") == "mississippimississippimis": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcba") == "abcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcba") == "abcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabaaaaaab") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabaaaaaab") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccdddd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccdddd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "acacacacac") == "acacacac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acacacacac") == "acacacac": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz") == "xyzxyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz") == "xyzxyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippi") == "mississippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippi") == "mississippi": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbaaaaa") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbaaaaa") == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbbbaaaaa") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbbbaaaaa") == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabanana") == "banana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabanana") == "banana": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippimiss") == "mississippimiss"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippimiss") == "mississippimiss": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == "aabbaabbaabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == "aabbaabbaabb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacaba") == "abacabadabacabadabacabadabacaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacaba") == "abacabadabacabadabacabadabacaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc") == "abcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc") == "abcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazazaz") == "zazazazazaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazazaz") == "zazazazazaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh") == "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh") == "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcabababa") == "aba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcabababa") == "aba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaab") == "aaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaab") == "aaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaab") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaab") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabac") == "abacabac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabac") == "abacabac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippimississippi") == "mississippimississippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippimississippi") == "mississippimississippi": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzzxyzxyz") == "xyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzzxyzxyz") == "xyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcde") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcde") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbababbababbabab") == "ababbababbabab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbababbababbabab") == "ababbababbabab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcab") == "abcabcabcab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcab") == "abcabcabcab": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab") == "abababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab") == "abababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa") == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == "ababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == "ababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababab") == "abababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababab") == "abababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == "abcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == "abcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabaaaaaaaaa") == "aaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabaaaaaaaaa") == "aaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaaaa") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaaaa") == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh") == "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh") == "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab") == "ababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab") == "ababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecaracecarace") == "racecarace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecaracecarace") == "racecarace": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == "abcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == "abcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecaracecaracecar") == "racecaracecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecaracecaracecar") == "racecaracecar": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbaedcbaedcba") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbaedcbaedcba") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecaracecaracecarace") == "racecaracecarace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecaracecaracecarace") == "racecaracecarace": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababa") == "abababababababababababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababa") == "abababababababababababa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecaracecaracecaracecaracecarace") == "racecaracecaracecaracecarace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecaracecaracecaracecaracecarace") == "racecaracecaracecaracecarace": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabaaaaaab") == "aaaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabaaaaaab") == "aaaaaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxy") == "xyxyxyxyxyxyxyxyxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxy") == "xyxyxyxyxyxyxyxyxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxxyx") == "xyxxyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxxyx") == "xyxxyx": {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazazaza") == "zazazazazaza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazazaza") == "zazazazazaza": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffggaabbccddeeffgg") == "aabbccddeeffgg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffggaabbccddeeffgg") == "aabbccddeeffgg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaab") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaab") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabaaaaaaaa") == "aaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabaaaaaaaa") == "aaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvutsrqponm") == "m"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvutsrqponm") == "m": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg") == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg") == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabcd") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabcd") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde") == "abcdeabcdeabcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde") == "abcdeabcdeabcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabcabcabc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabcabcabc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcda") == "abcdabcdabcdabcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcda") == "abcdabcdabcdabcda": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabaaaaaaaaaa") == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabaaaaaaaaaa") == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabad": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == "aabbccddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == "aabbccddeeff": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabaaaaa") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabaaaaa") == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabcabcabcabcabcabc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabcabcabcabcabcabc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcab") == "abcabcabcabcabcabcab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcab") == "abcabcabcabcabcabcab": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababababababababab") == "abababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababababababababab") == "abababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabb") == "aabbaabbaabbaabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabb") == "aabbaabbaabbaabb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabananaananaba") == "bananaananaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabananaananaba") == "bananaananaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaabaaabaab") == "aabaaabaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaabaaabaab") == "aabaaabaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllkjihgfedcba") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllkjihgfedcba") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaab") == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaab") == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabaaaaaa") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabaaaaaa") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde") == "abcdeabcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde") == "abcdeabcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcde") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcde") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyxzyxyzxyxzyxzyz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyxzyxyzxyxzyxzyz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == "abababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == "abababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab") == "ababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab") == "ababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzxyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzxyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "axbyczdxcyzbyxa") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "axbyczdxcyzbyxa") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg") == "abcdefgabcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg") == "abcdefgabcdefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyzabcxyzabcxyz") == "abcxyzabcxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyzabcxyzabcxyz") == "abcxyzabcxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == "r"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == "r": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij") == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij") == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab") == "ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab") == "ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaabanana") == "banana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaabanana") == "banana": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaabaaabaabaab") == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaabaaabaabaab") == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcabcababc") == "ababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcabcababc") == "ababc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababcabababc") == "abababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababcabababc") == "abababc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == "abcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == "abcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabracadabrac") == "abracadabrac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabracadabrac") == "abracadabrac": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababab") == "abababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababab") == "abababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzyzyzxzyzyzyzyzyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzyzyzxzyzyzyzyzyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "papapapapapap") == "papapapapap"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "papapapapapap") == "papapapapap": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "prefixprefix") == "prefix"
    assert candidate(s = "abcdef") == ""
    assert candidate(s = "aaaaa") == "aaaa"
    assert candidate(s = "aaaaabaaaa") == "aaaa"
    assert candidate(s = "a") == ""
    assert candidate(s = "abacabadabacaba") == "abacaba"
    assert candidate(s = "abcabcabc") == "abcabc"
    assert candidate(s = "abcabcabcabc") == "abcabcabc"
    assert candidate(s = "aaaaaabbbaaaa") == "aaaa"
    assert candidate(s = "happy") == ""
    assert candidate(s = "noon") == "n"
    assert candidate(s = "banana") == ""
    assert candidate(s = "abc") == ""
    assert candidate(s = "aabbccddeeaabbccdd") == "aabbccdd"
    assert candidate(s = "abcd") == ""
    assert candidate(s = "aabbccddeeffgg") == ""
    assert candidate(s = "suffix") == ""
    assert candidate(s = "aaaa") == "aaa"
    assert candidate(s = "mississippi") == ""
    assert candidate(s = "abcdabc") == "abc"
    assert candidate(s = "ababab") == "abab"
    assert candidate(s = "level") == "l"
    assert candidate(s = "abacababacab") == "abacab"
    assert candidate(s = "ababababcababab") == "ababab"
    assert candidate(s = "abacabadabacabadabacaba") == "abacabadabacaba"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == "abcdefghijabcdefghijabcdefghij"
    assert candidate(s = "bananaananabay") == ""
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abracadabra") == "abra"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abcdefabcdefabcdef") == "abcdefabcdef"
    assert candidate(s = "abacabadabacabadabacabadabacabad") == "abacabadabacabadabacabad"
    assert candidate(s = "abcabcabcabcabcd") == ""
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzxyz"
    assert candidate(s = "aababaabaababaaba") == "aababaaba"
    assert candidate(s = "aaaabaaaa") == "aaaa"
    assert candidate(s = "zazazazazazazazazazaz") == "zazazazazazazazazaz"
    assert candidate(s = "abcabcabcabcabcabca") == "abcabcabcabcabca"
    assert candidate(s = "abbaabbaabbaabbaabbaabba") == "abbaabbaabbaabbaabba"
    assert candidate(s = "aabaaabaabaaabaabaabaaabaabaab") == "aab"
    assert candidate(s = "mississippimississippimississippimis") == "mississippimississippimis"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad"
    assert candidate(s = "abcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcba") == "abcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcbaabcdefghijkllkjihgfedcba"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "aaaaaaabaaaaaab") == ""
    assert candidate(s = "aaaaabbbbbccccdddd") == ""
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "acacacacac") == "acacacac"
    assert candidate(s = "xyzxyzxyzxyz") == "xyzxyzxyz"
    assert candidate(s = "mississippimississippi") == "mississippi"
    assert candidate(s = "aaaaaabbbaaaaa") == "aaaaa"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "aaaaabbbbbbbaaaaa") == "aaaaa"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "bananaananabanana") == "banana"
    assert candidate(s = "mississippimississippimiss") == "mississippimiss"
    assert candidate(s = "aabbaabbaabbaabb") == "aabbaabbaabb"
    assert candidate(s = "abacabadabacabadabacabadabacabadabacaba") == "abacabadabacabadabacabadabacaba"
    assert candidate(s = "abcabcabcabcabcabcabc") == "abcabcabcabcabcabc"
    assert candidate(s = "zazazazazazaz") == "zazazazazaz"
    assert candidate(s = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh") == "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh"
    assert candidate(s = "ababcabababa") == "aba"
    assert candidate(s = "aaabaaaab") == "aaab"
    assert candidate(s = "aaaaaaaab") == ""
    assert candidate(s = "abacabacabac") == "abacabac"
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcdabcdabcd"
    assert candidate(s = "mississippimississippimississippi") == "mississippimississippi"
    assert candidate(s = "xyzxyzzxyzxyz") == "xyzxyz"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "abcdabcde") == ""
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabc"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "ababbababbababbabab") == "ababbababbabab"
    assert candidate(s = "abcabcabcabcab") == "abcabcabcab"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "ababababababab") == "abababababab"
    assert candidate(s = "abcdeedcba") == "a"
    assert candidate(s = "aaaaaa") == "aaaaa"
    assert candidate(s = "abababababababab") == "ababababababab"
    assert candidate(s = "ababababababababab") == "abababababababab"
    assert candidate(s = "abcabcabcabcabcabc") == "abcabcabcabcabc"
    assert candidate(s = "aaaaaaaaaabaaaaaaaaa") == "aaaaaaaaa"
    assert candidate(s = "aaaaabaaaabaaaaaa") == "aaaaa"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "aaaaaaa") == "aaaaaa"
    assert candidate(s = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh") == "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh"
    assert candidate(s = "abababababababababababababab") == "ababababababababababababab"
    assert candidate(s = "racecaracecarace") == "racecarace"
    assert candidate(s = "abcdabcdabcdabcdabcd") == "abcdabcdabcdabcd"
    assert candidate(s = "racecaracecaracecar") == "racecaracecar"
    assert candidate(s = "abcdeedcbaedcbaedcba") == "a"
    assert candidate(s = "racecaracecaracecarace") == "racecaracecarace"
    assert candidate(s = "ababababababababababababa") == "abababababababababababa"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "racecaracecaracecaracecaracecarace") == "racecaracecaracecaracecarace"
    assert candidate(s = "aaaaaabaaaaaab") == "aaaaaab"
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxy") == "xyxyxyxyxyxyxyxyxy"
    assert candidate(s = "xyxxyxyxyxxyx") == "xyxxyx"
    assert candidate(s = "zazazazazazaza") == "zazazazazaza"
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad"
    assert candidate(s = "xyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyz"
    assert candidate(s = "aabbccddeeffggaabbccddeeffgg") == "aabbccddeeffgg"
    assert candidate(s = "abcdabcabc") == "abc"
    assert candidate(s = "aaaaaaaaaab") == ""
    assert candidate(s = "aaaaaaabaaaaaaaa") == "aaaaaaa"
    assert candidate(s = "mnopqrstuvutsrqponm") == "m"
    assert candidate(s = "ababababc") == ""
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "abcdefgabcdefg") == "abcdefg"
    assert candidate(s = "abcdabcabcabcd") == "abcd"
    assert candidate(s = "abcdeabcdeabcdeabcde") == "abcdeabcdeabcde"
    assert candidate(s = "aaaaaaabcabcabc") == ""
    assert candidate(s = "abcdabcdabcdabcdabcda") == "abcdabcdabcdabcda"
    assert candidate(s = "abcdabcabcabc") == "abc"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == ""
    assert candidate(s = "aaaaaaaaaabaaaaaaaaaa") == "aaaaaaaaaa"
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == "abacabadabacabadabacabadabacabadabacabad"
    assert candidate(s = "aabbccddeeffaabbccddeeff") == "aabbccddeeff"
    assert candidate(s = "aaaaaabaaaaa") == "aaaaa"
    assert candidate(s = "abcdabcabcabcabcabcabcabcabc") == "abc"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcd") == ""
    assert candidate(s = "abcabcabcabcabcabcabcab") == "abcabcabcabcabcabcab"
    assert candidate(s = "ababababababababababababababababababababababababababababababababababababababab") == "abababababababababababababababababababababababababababababababababababababab"
    assert candidate(s = "aabbaabbaabbaabbaabb") == "aabbaabbaabbaabb"
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcdabcd"
    assert candidate(s = "bananaananabananaananaba") == "bananaananaba"
    assert candidate(s = "aabaaabaabaaabaab") == "aabaaabaab"
    assert candidate(s = "abcdefghijkllkjihgfedcba") == "a"
    assert candidate(s = "aabaaab") == "aab"
    assert candidate(s = "aaaaaaabaaaaaa") == "aaaaaa"
    assert candidate(s = "abcdeabcdeabcde") == "abcdeabcde"
    assert candidate(s = "abcdabcabcde") == ""
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "zxyxzyxyzxyxzyxzyz") == "z"
    assert candidate(s = "ababababab") == "abababab"
    assert candidate(s = "abababababababababababab") == "ababababababababababab"
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzxyzxyz"
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == "abcdabcdabcdabcdabcdabcdabcd"
    assert candidate(s = "axbyczdxcyzbyxa") == "a"
    assert candidate(s = "abcdefgabcdefgabcdefg") == "abcdefgabcdefg"
    assert candidate(s = "abcxyzabcxyzabcxyz") == "abcxyzabcxyz"
    assert candidate(s = "abcdefghihgfedcba") == "a"
    assert candidate(s = "racecar") == "r"
    assert candidate(s = "abcdefghijabcdefghij") == "abcdefghij"
    assert candidate(s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab") == "ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(s = "abcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabc"
    assert candidate(s = "bananaabanana") == "banana"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "aabaaabaabaaabaabaab") == "aab"
    assert candidate(s = "ababcabcababc") == "ababc"
    assert candidate(s = "abababcabababc") == "abababc"
    assert candidate(s = "abcabcabcabcabc") == "abcabcabcabc"
    assert candidate(s = "abracadabracadabrac") == "abracadabrac"
    assert candidate(s = "ababababababababababababababababababab") == "abababababababababababababababababab"
    assert candidate(s = "xyzxyzyzyzxzyzyzyzyzyz") == ""
    assert candidate(s = "papapapapapap") == "papapapapap"


