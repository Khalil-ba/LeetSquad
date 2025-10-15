def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "acbbaca",t = "aba") == "baca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbbaca",t = "aba") == "baca": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",t = "abc") == "abbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",t = "abc") == "abbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa",t = "aa") == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa",t = "aa") == "aa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "aa") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "aa") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "bd") == "bcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "bd") == "bcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",t = "b") == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",t = "b") == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "aa",t = "aa") == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa",t = "aa") == "aa": {e}')
    
    total += 1
    try:
        result = candidate(s = "ADOBECODEBANC",t = "ABC") == "BANC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ADOBECODEBANC",t = "ABC") == "BANC": {e}')
    
    total += 1
    try:
        result = candidate(s = "fgrheahtfeqcrha",t = "harf") == "fgrhea"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fgrheahtfeqcrha",t = "harf") == "fgrhea": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbcdd",t = "abcdd") == "abbbbbcdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbcdd",t = "abcdd") == "abbbbbcdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "f") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "f") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",t = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",t = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",t = "abab") == "abab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",t = "abab") == "abab": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "aafffrbb",t = "ffab") == "afffrb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aafffrbb",t = "ffab") == "afffrb": {e}')
    
    total += 1
    try:
        result = candidate(s = "bba",t = "ab") == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bba",t = "ab") == "ba": {e}')
    
    total += 1
    try:
        result = candidate(s = "cbbbaaaaabbbcccccbbaa",t = "aaabbbccc") == "aaabbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbbbaaaaabbbcccccbbaa",t = "aaabbbccc") == "aaabbbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "abc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "abc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "cabwefgewcwaefgcf",t = "cae") == "cwae"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cabwefgewcwaefgcf",t = "cae") == "cwae": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "aaa") == "abcabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "aaa") == "abcabca": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",t = "abc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",t = "abc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "aaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "aaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zjwsxeyrhtlnejzjwsxeyrhtlnej",t = "nejxyz") == "nejzjwsxey"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zjwsxeyrhtlnejzjwsxeyrhtlnej",t = "nejxyz") == "nejzjwsxey": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "jihgfedcba") == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "jihgfedcba") == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "abc") == "bac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "abc") == "bac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "cba") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "cba") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",t = "abcdefghi") == "abbccddeeffgghhi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",t = "abcdefghi") == "abbccddeeffgghhi": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbcccccc",t = "abc") == "abbbbbbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbcccccc",t = "abc") == "abbbbbbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "issip") == "issip"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "issip") == "issip": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzz",t = "zzz") == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzz",t = "zzz") == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxzyxzyxzyx",t = "xzy") == "yxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxzyxzyxzyx",t = "xzy") == "yxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "zyxwvutsrqponmlkjihgfedcba") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "zyxwvutsrqponmlkjihgfedcba") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxzyzxzyzzyzyxzyzyxzyzyx",t = "xyzzyxzyzyzx") == "xyzxzyzxzyzzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxzyzxzyzzyzyxzyzyxzyzyx",t = "xyzzyxzyzyzx") == "xyzxzyzxzyzzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaabbbccc",t = "aabbcc") == "aabbbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaabbbccc",t = "aabbcc") == "aabbbcc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzz",t = "z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzz",t = "z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdef") == "abbccddeef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdef") == "abbccddeef": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",t = "aabbccddeeffgghhii") == "aabbccddeeffgghhii"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",t = "aabbccddeeffgghhii") == "aabbccddeeffgghhii": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",t = "aabbcc") == "abcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",t = "aabbcc") == "abcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbbbbaabbbbaaabbbbaaabbababababab",t = "bbbbaaaa") == "aabbbbaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbbbbaabbbbaaabbbbaaabbababababab",t = "bbbbaaaa") == "aabbbbaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "issi") == "issi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "issi") == "issi": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbcccccccdddeee",t = "abcde") == "abbcccccccddde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbcccccccdddeee",t = "abcde") == "abbcccccccddde": {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmasdfghjklqwertyuiop",t = "opq") == "qwertyuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmasdfghjklqwertyuiop",t = "opq") == "qwertyuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbbcccccccc",t = "abc") == "abbbbbbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbbcccccccc",t = "abc") == "abbbbbbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",t = "cba") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",t = "cba") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzz",t = "xyz") == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzz",t = "xyz") == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbbbbbbbcccccccccc",t = "abc") == "abbbbbbbbbbbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbbbbbbbcccccccccc",t = "abc") == "abbbbbbbbbbbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyxzyxzyxzyxzy",t = "zyxzyxz") == "xyzzzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyxzyxzyxzyxzy",t = "zyxzyxz") == "xyzzzyx": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",t = "abba") == "abab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",t = "abba") == "abab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdf",t = "abcfed") == "eabcdf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdf",t = "abcfed") == "eabcdf": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",t = "aabbcc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",t = "aabbcc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "xyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "xyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",t = "aabbcc") == "aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",t = "aabbcc") == "aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcabcabcabcabcabcabcabcabcabcabcabc",t = "abcabcabc") == "abcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcabcabcabcabcabcabcabcabcabcabcabc",t = "abcabcabc") == "abcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",t = "lle") == "ell"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",t = "lle") == "ell": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "sadjhasjhdjahsjdhasjhadsjhsahjdahjdsjahjdhasjdhajsdhasjdhajsdjasdhasjdhsa",t = "hasjdh") == "hasjhd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sadjhasjhdjahsjdhasjhadsjhsahjdahjdsjahjdhasjdhajsdhasjdhajsdjasdhasjdhsa",t = "hasjdh") == "hasjhd": {e}')
    
    total += 1
    try:
        result = candidate(s = "bancbbancbbanc",t = "abc") == "banc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bancbbancbbanc",t = "abc") == "banc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz",t = "abcdefghijklmnopqrstuvwxyz") == "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz",t = "abcdefghijklmnopqrstuvwxyz") == "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatweneedtolookinto",t = "tin") == "int"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatweneedtolookinto",t = "tin") == "int": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzz") == "zzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzz") == "zzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaaaaaabbbbcccc",t = "aabbbccc") == "aabbbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaaaaaabbbbcccc",t = "aabbbccc") == "aabbbbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",t = "abab") == "abab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",t = "abab") == "abab": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "mnopqrstuvwxyz") == "mnnooppqqrrssttuuvvwwxxyyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "mnopqrstuvwxyz") == "mnnooppqqrrssttuuvvwwxxyyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopzxcvbnm") == "zxcvbnmqwertyuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopzxcvbnm") == "zxcvbnmqwertyuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyzyxzyzxzyzxzyxzyzyxzyx",t = "xyz") == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyzyxzyzxzyzxzyxzyzyxzyx",t = "xyz") == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacbacbac",t = "acbcba") == "abcbac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacbacbac",t = "acbcba") == "abcbac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaacz",t = "abc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaacz",t = "abc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",t = "rac") == "rac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",t = "rac") == "rac": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",t = "abc") == "abbbbbbbbbbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",t = "abc") == "abbbbbbbbbbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaacccaaaabbbccc",t = "aabbbccc") == "aabbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaacccaaaabbbccc",t = "aabbbccc") == "aabbbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bancancode",t = "abc") == "banc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bancancode",t = "abc") == "banc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",t = "abcd") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",t = "abcd") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiop") == "qwertyuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiop") == "qwertyuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",t = "aaa") == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",t = "aaa") == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababab",t = "aba") == "aba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababab",t = "aba") == "aba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccc",t = "abc") == "abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccc",t = "abc") == "abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffeghijk",t = "efg") == "feg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffeghijk",t = "efg") == "feg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",t = "cba") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",t = "cba") == "abc": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "acbbaca",t = "aba") == "baca"
    assert candidate(s = "aabbcc",t = "abc") == "abbc"
    assert candidate(s = "aaaaaaa",t = "aa") == "aa"
    assert candidate(s = "a",t = "aa") == ""
    assert candidate(s = "abcd",t = "bd") == "bcd"
    assert candidate(s = "ab",t = "b") == "b"
    assert candidate(s = "aa",t = "aa") == "aa"
    assert candidate(s = "ADOBECODEBANC",t = "ABC") == "BANC"
    assert candidate(s = "fgrheahtfeqcrha",t = "harf") == "fgrhea"
    assert candidate(s = "aaaaaaaaaaaabbbbbcdd",t = "abcdd") == "abbbbbcdd"
    assert candidate(s = "abcde",t = "f") == ""
    assert candidate(s = "ab",t = "a") == "a"
    assert candidate(s = "abababab",t = "abab") == "abab"
    assert candidate(s = "a",t = "a") == "a"
    assert candidate(s = "aafffrbb",t = "ffab") == "afffrb"
    assert candidate(s = "bba",t = "ab") == "ba"
    assert candidate(s = "cbbbaaaaabbbcccccbbaa",t = "aaabbbccc") == "aaabbbccc"
    assert candidate(s = "abcabcabc",t = "abc") == "abc"
    assert candidate(s = "cabwefgewcwaefgcf",t = "cae") == "cwae"
    assert candidate(s = "abcabcabc",t = "aaa") == "abcabca"
    assert candidate(s = "abc",t = "abc") == "abc"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "aaaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "zjwsxeyrhtlnejzjwsxeyrhtlnej",t = "nejxyz") == "nejzjwsxey"
    assert candidate(s = "abcdefghijk",t = "jihgfedcba") == "abcdefghij"
    assert candidate(s = "abacabadabacaba",t = "abc") == "bac"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "cba") == "abc"
    assert candidate(s = "aabbccddeeffgghhii",t = "abcdefghi") == "abbccddeeffgghhi"
    assert candidate(s = "aaaaaaaaaabbbbbbcccccc",t = "abc") == "abbbbbbc"
    assert candidate(s = "mississippi",t = "issip") == "issip"
    assert candidate(s = "zzzzzzzzzzzzzzzzz",t = "zzz") == "zzz"
    assert candidate(s = "xyxzyxzyxzyxzyx",t = "xzy") == "yxz"
    assert candidate(s = "abcdefg",t = "zyxwvutsrqponmlkjihgfedcba") == ""
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
    assert candidate(s = "xyzxzyzxzyzzyzyxzyzyxzyzyx",t = "xyzzyxzyzyzx") == "xyzxzyzxzyzzy"
    assert candidate(s = "aaabbbaaabbbccc",t = "aabbcc") == "aabbbcc"
    assert candidate(s = "zzzzzzzzzzz",t = "z") == "z"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdef") == "abbccddeef"
    assert candidate(s = "aabbccddeeffgghhii",t = "aabbccddeeffgghhii") == "aabbccddeeffgghhii"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",t = "aabbcc") == "abcabc"
    assert candidate(s = "bbaabbbbbaabbbbaaabbbbaaabbababababab",t = "bbbbaaaa") == "aabbbbaa"
    assert candidate(s = "mississippi",t = "issi") == "issi"
    assert candidate(s = "aaabbcccccccdddeee",t = "abcde") == "abbcccccccddde"
    assert candidate(s = "zxcvbnmasdfghjklqwertyuiop",t = "opq") == "qwertyuiop"
    assert candidate(s = "aaaaaaaaaaaabbbbbbcccccccc",t = "abc") == "abbbbbbc"
    assert candidate(s = "abcabcabcabcabcabc",t = "cba") == "abc"
    assert candidate(s = "xyzzxyzzxyzz",t = "xyz") == "xyz"
    assert candidate(s = "aaaaaaaaaaaabbbbbbbbbbbcccccccccc",t = "abc") == "abbbbbbbbbbbc"
    assert candidate(s = "xyzzzyxzyxzyxzyxzy",t = "zyxzyxz") == "xyzzzyx"
    assert candidate(s = "ababababababab",t = "abba") == "abab"
    assert candidate(s = "abcdabcdeabcdf",t = "abcfed") == "eabcdf"
    assert candidate(s = "abababababababababab",t = "aabbcc") == ""
    assert candidate(s = "abcdefg",t = "xyz") == ""
    assert candidate(s = "aabbccddeeffgghhii",t = "aabbcc") == "aabbcc"
    assert candidate(s = "ababcabcabcabcabcabcabcabcabcabcabcabc",t = "abcabcabc") == "abcabcabc"
    assert candidate(s = "hellohellohello",t = "lle") == "ell"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "sadjhasjhdjahsjdhasjhadsjhsahjdahjdsjahjdhasjdhajsdhasjdhajsdjasdhasjdhsa",t = "hasjdh") == "hasjhd"
    assert candidate(s = "bancbbancbbanc",t = "abc") == "banc"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz",t = "abcdefghijklmnopqrstuvwxyz") == "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
    assert candidate(s = "thisisaverylongstringthatweneedtolookinto",t = "tin") == "int"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzz") == "zzzzzzzz"
    assert candidate(s = "bbaaaaaaabbbbcccc",t = "aabbbccc") == "aabbbbccc"
    assert candidate(s = "abababababababab",t = "abab") == "abab"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == ""
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "mnopqrstuvwxyz") == "mnnooppqqrrssttuuvvwwxxyyz"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopzxcvbnm") == "zxcvbnmqwertyuiop"
    assert candidate(s = "xyzzyxzyzyxzyzxzyzxzyxzyzyxzyx",t = "xyz") == "xyz"
    assert candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacbacbac",t = "acbcba") == "abcbac"
    assert candidate(s = "abccbaacz",t = "abc") == "abc"
    assert candidate(s = "abracadabra",t = "rac") == "rac"
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",t = "abc") == "abbbbbbbbbbc"
    assert candidate(s = "bbaaacccaaaabbbccc",t = "aabbbccc") == "aabbbccc"
    assert candidate(s = "bancancode",t = "abc") == "banc"
    assert candidate(s = "abcdefgabcdefg",t = "abcd") == "abcd"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiop") == "qwertyuiop"
    assert candidate(s = "aaaaaaaaaa",t = "aaa") == "aaa"
    assert candidate(s = "ababababababababababababababababababab",t = "aba") == "aba"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccc",t = "abc") == "abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc"
    assert candidate(s = "abcdeffeghijk",t = "efg") == "feg"
    assert candidate(s = "abcabcabcabcabc",t = "cba") == "abc"


