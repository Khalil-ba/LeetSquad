def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['world']) == "hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['world']) == "hello": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['issi', 'issip', 'is', 'i']) == "m<b>ississip</b>p<b>i</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['issi', 'issip', 'is', 'i']) == "m<b>ississip</b>p<b>i</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['e', 'f', 'g']) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['e', 'f', 'g']) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['ll', 'o']) == "he<b>llo</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['ll', 'o']) == "he<b>llo</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "",words = ['a']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",words = ['a']) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",words = ['zz']) == "<b>zzzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",words = ['zz']) == "<b>zzzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['a', 'b', 'c', 'd']) == "<b>abcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['a', 'b', 'c', 'd']) == "<b>abcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",words = ['abc', 'cab']) == "<b>abcabcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",words = ['abc', 'cab']) == "<b>abcabcabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothere",words = ['he', 'lo']) == "<b>he</b>l<b>lo</b>t<b>he</b>re"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothere",words = ['he', 'lo']) == "<b>he</b>l<b>lo</b>t<b>he</b>re": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyz123",words = ['abc', '123']) == "<b>abc</b>xyz<b>123</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyz123",words = ['abc', '123']) == "<b>abc</b>xyz<b>123</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa",words = ['a', 'aa']) == "<b>aaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa",words = ['a', 'aa']) == "<b>aaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbb",words = ['aa', 'b']) == "<b>aaabbb</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbb",words = ['aa', 'b']) == "<b>aaabbb</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['issi', 'issipp']) == "m<b>ississipp</b>i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['issi', 'issipp']) == "m<b>ississipp</b>i": {e}')
    
    total += 1
    try:
        result = candidate(s = "complexity",words = ['com', 'plex', 'ity', 'ityt', 'ex']) == "<b>complexity</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complexity",words = ['com', 'plex', 'ity', 'ityt', 'ex']) == "<b>complexity</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaa",words = ['aaa', 'bbbb', 'aaabbbbbaaa']) == "<b>aaaaabbbbbaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaa",words = ['aaa', 'bbbb', 'aaabbbbbaaa']) == "<b>aaaaabbbbbaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiissippi",words = ['issi', 'issipp', 'ippi', 'miss', 'ippii', 'ssippi']) == "<b>mississippiissippi</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiissippi",words = ['issi', 'issipp', 'ippi', 'miss', 'ippii', 'ssippi']) == "<b>mississippiissippi</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",words = ['this', 'test', 'string', 'is']) == "<b>thisis</b>a<b>teststring</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",words = ['this', 'test', 'string', 'is']) == "<b>thisis</b>a<b>teststring</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",words = ['aa', 'bbcc', 'ccdd', 'ddeeff', 'efff', 'ff']) == "<b>aabbccddeeff</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",words = ['aa', 'bbcc', 'ccdd', 'ddeeff', 'efff', 'ff']) == "<b>aabbccddeeff</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",words = ['xy', 'yz', 'zxy']) == "<b>xyzxyzxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",words = ['xy', 'yz', 'zxy']) == "<b>xyzxyzxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",words = ['abc', 'cde', 'efg', 'abcd']) == "<b>abcdefgabcdefg</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",words = ['abc', 'cde', 'efg', 'abcd']) == "<b>abcdefgabcdefg</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde",words = ['abc', 'deabc', 'cde']) == "<b>abcdeabcdeabcde</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde",words = ['abc', 'deabc', 'cde']) == "<b>abcdeabcdeabcde</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbaaaaa",words = ['aaa', 'bbb']) == "<b>aaaaaabbbbbaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbaaaaa",words = ['aaa', 'bbb']) == "<b>aaaaaabbbbbaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",words = ['this', 'is', 'test', 'string', 'a']) == "<b>thisisateststring</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",words = ['this', 'is', 'test', 'string', 'a']) == "<b>thisisateststring</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "nestedboldboldnested",words = ['nestedbold', 'boldbold', 'bold']) == "<b>nestedboldbold</b>nested"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nestedboldboldnested",words = ['nestedbold', 'boldbold', 'bold']) == "<b>nestedboldbold</b>nested": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlapexample",words = ['over', 'lap', 'example', 'exam']) == "<b>overlapexample</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlapexample",words = ['over', 'lap', 'example', 'exam']) == "<b>overlapexample</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "nestedboldtags",words = ['nest', 'sted', 'bold', 'tags', 'edta']) == "<b>nestedboldtags</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nestedboldtags",words = ['nest', 'sted', 'bold', 'tags', 'edta']) == "<b>nestedboldtags</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlappingboldtags",words = ['overlap', 'ping', 'bold', 'tags', 'pinging']) == "<b>overlappingboldtags</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlappingboldtags",words = ['overlap', 'ping', 'bold', 'tags', 'pinging']) == "<b>overlappingboldtags</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcxyzabcxyz",words = ['xyz', 'abc', 'ab', 'bc', 'yz', 'xy']) == "<b>xyzabcxyzabcxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcxyzabcxyz",words = ['xyz', 'abc', 'ab', 'bc', 'yz', 'xy']) == "<b>xyzabcxyzabcxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",words = ['aba', 'bab', 'ab', 'ba']) == "<b>abababababab</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",words = ['aba', 'bab', 'ab', 'ba']) == "<b>abababababab</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "oneonetwoonetwoonetwoonetwoonetwoone",words = ['one', 'onetwo', 'two', 'onetwone', 'oneto']) == "<b>oneonetwoonetwoonetwoonetwoonetwoone</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneonetwoonetwoonetwoonetwoonetwoone",words = ['one', 'onetwo', 'two', 'onetwone', 'oneto']) == "<b>oneonetwoonetwoonetwoonetwoonetwoone</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa",words = ['aa', 'aaa']) == "<b>aaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa",words = ['aa', 'aaa']) == "<b>aaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababa",words = ['aba', 'bab']) == "<b>abababababa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababa",words = ['aba', 'bab']) == "<b>abababababa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",words = ['abc', 'defg', 'bcde', 'fgh']) == "<b>abcdefgabcdefg</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",words = ['abc', 'defg', 'bcde', 'fgh']) == "<b>abcdefgabcdefg</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababa",words = ['aba', 'bab', 'aba', 'abb']) == "<b>abababababa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababa",words = ['aba', 'bab', 'aba', 'abb']) == "<b>abababababa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",words = ['abcd', 'bcd', 'cd', 'd', 'a', 'ab', 'bc', 'cd', 'abc', 'bca', 'cab', 'dabcd', 'abcdabc', 'bcdbca']) == "<b>abcdabcdabcdabcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",words = ['abcd', 'bcd', 'cd', 'd', 'a', 'ab', 'bc', 'cd', 'abc', 'bca', 'cab', 'dabcd', 'abcdabc', 'bcdbca']) == "<b>abcdabcdabcdabcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",words = ['xy', 'yz', 'zxy', 'xyz']) == "<b>xyzxyzxyzxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",words = ['xy', 'yz', 'zxy', 'xyz']) == "<b>xyzxyzxyzxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlappingboldtags",words = ['lap', 'bold', 'tag', 'pingb', 'lapin']) == "over<b>lappingboldtag</b>s"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlappingboldtags",words = ['lap', 'bold', 'tag', 'pingb', 'lapin']) == "over<b>lappingboldtag</b>s": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaabababa",words = ['aba', 'bab', 'abaabababa']) == "<b>ababaabababa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaabababa",words = ['aba', 'bab', 'abaabababa']) == "<b>ababaabababa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzz",words = ['xyz', 'zzx', 'xy', 'yz']) == "<b>xyzzxyzzxyz</b>z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzz",words = ['xyz', 'zzx', 'xy', 'yz']) == "<b>xyzzxyzzxyz</b>z": {e}')
    
    total += 1
    try:
        result = candidate(s = "mixednumbersandletters123",words = ['123', 'and', 'num', 'bers', 'mixed']) == "<b>mixednumbersand</b>letters<b>123</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mixednumbersandletters123",words = ['123', 'and', 'num', 'bers', 'mixed']) == "<b>mixednumbersand</b>letters<b>123</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aabbcc', 'ddeeff', 'gghhii']) == "<b>aabbccddeeffgghhii</b>jjkkllmmnnooppqqrrssttuuvvwwxxy<b>yz</b>z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aabbcc', 'ddeeff', 'gghhii']) == "<b>aabbccddeeffgghhii</b>jjkkllmmnnooppqqrrssttuuvvwwxxy<b>yz</b>z": {e}')
    
    total += 1
    try:
        result = candidate(s = "consecutiveboldboldbold",words = ['consecutive', 'boldbold', 'bold']) == "<b>consecutiveboldboldbold</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consecutiveboldboldbold",words = ['consecutive', 'boldbold', 'bold']) == "<b>consecutiveboldboldbold</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcxyzabc",words = ['abc', 'xyz', 'xy']) == "<b>xyzabcxyzabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcxyzabc",words = ['abc', 'xyz', 'xy']) == "<b>xyzabcxyzabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlaplap",words = ['lap', 'laplap', 'over']) == "<b>overlaplap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlaplap",words = ['lap', 'laplap', 'over']) == "<b>overlaplap</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",words = ['test', 'this', 'string', 'est', 'ing']) == "<b>this</b>isa<b>teststring</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",words = ['test', 'this', 'string', 'est', 'ing']) == "<b>this</b>isa<b>teststring</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaa",words = ['aa', 'aaa', 'aaaa']) == "<b>aaaaa</b>b<b>aaaa</b>b<b>aaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaa",words = ['aa', 'aaa', 'aaaa']) == "<b>aaaaa</b>b<b>aaaa</b>b<b>aaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabbbbbbcccccc",words = ['aaa', 'bbb', 'ccc', 'aabb', 'bbcc', 'aabbcc']) == "<b>aaaaaaabbbbbbcccccc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabbbbbbcccccc",words = ['aaa', 'bbb', 'ccc', 'aabb', 'bbcc', 'aabbcc']) == "<b>aaaaaaabbbbbbcccccc</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890",words = ['12', '23', '34', '45', '56', '67', '78', '89', '90']) == "<b>1234567890</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890",words = ['12', '23', '34', '45', '56', '67', '78', '89', '90']) == "<b>1234567890</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzz",words = ['zzzz', 'zzz', 'zz', 'z']) == "<b>zzzzzzzzzzzzzzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzz",words = ['zzzz', 'zzz', 'zz', 'z']) == "<b>zzzzzzzzzzzzzzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",words = ['a', 'aa', 'aaa', 'aaaa']) == "<b>aaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",words = ['a', 'aa', 'aaa', 'aaaa']) == "<b>aaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",words = ['bra', 'cad', 'ra']) == "a<b>bracad</b>a<b>bra</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",words = ['bra', 'cad', 'ra']) == "a<b>bracad</b>a<b>bra</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "nestedboldtags",words = ['nest', 'sted', 'bold', 'tags', 'boldt', 'tagsn']) == "<b>nestedboldtags</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nestedboldtags",words = ['nest', 'sted', 'bold', 'tags', 'boldt', 'tagsn']) == "<b>nestedboldtags</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedpatterns",words = ['re', 'pe', 'at', 'te', 'ed', 'pattern', 'terns']) == "<b>repeatedpatterns</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedpatterns",words = ['re', 'pe', 'at', 'te', 'ed', 'pattern', 'terns']) == "<b>repeatedpatterns</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890",words = ['12', '234', '456', '678', '890']) == "<b>1234567890</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890",words = ['12', '234', '456', '678', '890']) == "<b>1234567890</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",words = ['test', 'is', 'this', 'string']) == "<b>thisis</b>a<b>teststring</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",words = ['test', 'is', 'this', 'string']) == "<b>thisis</b>a<b>teststring</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",words = ['xyz', 'xy', 'yz', 'zxy']) == "<b>xyzxyzxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",words = ['xyz', 'xy', 'yz', 'zxy']) == "<b>xyzxyzxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcd",words = ['abc', 'de', 'bcd']) == "<b>abcdabcdeabcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcd",words = ['abc', 'de', 'bcd']) == "<b>abcdabcdeabcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890",words = ['123', '456', '789', '0']) == "<b>1234567890</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890",words = ['123', '456', '789', '0']) == "<b>1234567890</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithmanywords",words = ['long', 'string', 'with', 'many', 'words', 'longstring', 'stringwith', 'withman']) == "<b>longstringwithmanywords</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithmanywords",words = ['long', 'string', 'with', 'many', 'words', 'longstring', 'stringwith', 'withman']) == "<b>longstringwithmanywords</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345678901234567890",words = ['123', '234', '4567', '890']) == "<b>12345678901234567890</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345678901234567890",words = ['123', '234', '4567', '890']) == "<b>12345678901234567890</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1b2c3d4e5f6g7h8i9j0",words = ['a1b2', 'b2c3', 'c3d4', 'd4e5', 'e5f6', 'f6g7', 'g7h8', 'h8i9', 'i9j0']) == "<b>a1b2c3d4e5f6g7h8i9j0</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1b2c3d4e5f6g7h8i9j0",words = ['a1b2', 'b2c3', 'c3d4', 'd4e5', 'e5f6', 'f6g7', 'g7h8', 'h8i9', 'i9j0']) == "<b>a1b2c3d4e5f6g7h8i9j0</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbcccc",words = ['aa', 'bbb', 'cccc', 'aabbb', 'bbccc']) == "<b>aaaaaabbbbcccc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbcccc",words = ['aa', 'bbb', 'cccc', 'aabbb', 'bbccc']) == "<b>aaaaaabbbbcccc</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "multiplewordsinsequence",words = ['mul', 'ple', 'word', 'in', 'seq', 'uence']) == "<b>mul</b>ti<b>pleword</b>s<b>insequence</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "multiplewordsinsequence",words = ['mul', 'ple', 'word', 'in', 'seq', 'uence']) == "<b>mul</b>ti<b>pleword</b>s<b>insequence</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde",words = ['abc', 'de', 'cde', 'abcde', 'bcde', 'cdea']) == "<b>abcdeabcdeabcdeabcde</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde",words = ['abc', 'de', 'cde', 'abcde', 'bcde', 'cdea']) == "<b>abcdeabcdeabcdeabcde</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",words = ['xyz', 'zyx', 'xy', 'yx']) == "<b>xyzxyzxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",words = ['xyz', 'zyx', 'xy', 'yx']) == "<b>xyzxyzxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "consecutiveconsecutiveconsecutive",words = ['con', 'consec', 'consecutive', 'sec']) == "<b>consecutiveconsecutiveconsecutive</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consecutiveconsecutiveconsecutive",words = ['con', 'consec', 'consecutive', 'sec']) == "<b>consecutiveconsecutiveconsecutive</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "consecutivesubstrings",words = ['con', 'sec', 'cut', 'utive', 'sub', 'strings']) == "<b>consecutivesubstrings</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consecutivesubstrings",words = ['con', 'sec', 'cut', 'utive', 'sub', 'strings']) == "<b>consecutivesubstrings</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbaaaa",words = ['aaa', 'bbb']) == "<b>aaaaaabbbbbaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbaaaa",words = ['aaa', 'bbb']) == "<b>aaaaaabbbbbaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststringfortestingboldtags",words = ['test', 'this', 'that', 'for', 'bold', 'tags', 'string']) == "<b>this</b>isa<b>teststringfortest</b>ing<b>boldtags</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststringfortestingboldtags",words = ['test', 'this', 'that', 'for', 'bold', 'tags', 'string']) == "<b>this</b>isa<b>teststringfortest</b>ing<b>boldtags</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345678901234567890",words = ['123', '456', '789', '012', '345', '678', '901']) == "<b>1234567890123456789</b>0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345678901234567890",words = ['123', '456', '789', '012', '345', '678', '901']) == "<b>1234567890123456789</b>0": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",words = ['abc', 'def', 'gab', 'efg']) == "<b>abcdefgabcdefg</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",words = ['abc', 'def', 'gab', 'efg']) == "<b>abcdefgabcdefg</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == "<b>aaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == "<b>aaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzz",words = ['zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == "<b>zzzzzzzzzzzzzzzzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzz",words = ['zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == "<b>zzzzzzzzzzzzzzzzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaababa",words = ['aba', 'baa']) == "<b>ababaababa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaababa",words = ['aba', 'baa']) == "<b>ababaababa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890",words = ['123', '456', '789', '012', '34567890']) == "<b>1234567890</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890",words = ['123', '456', '789', '012', '34567890']) == "<b>1234567890</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedrepeatedrepeated",words = ['re', 'rep', 'peat', 'repeated']) == "<b>repeatedrepeatedrepeated</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedrepeatedrepeated",words = ['re', 'rep', 'peat', 'repeated']) == "<b>repeatedrepeatedrepeated</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj",words = ['abc', 'def', 'gh', 'ij', 'bb', 'cc']) == "aa<b>bbcc</b>ddeeffg<b>gh</b>hi<b>ij</b>j"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj",words = ['abc', 'def', 'gh', 'ij', 'bb', 'cc']) == "aa<b>bbcc</b>ddeeffg<b>gh</b>hi<b>ij</b>j": {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquestringsareunique",words = ['unique', 'strings', 'are']) == "<b>uniquestringsareunique</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquestringsareunique",words = ['unique', 'strings', 'are']) == "<b>uniquestringsareunique</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello123world456",words = ['123', 'world', '456', 'hello']) == "<b>hello123world456</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello123world456",words = ['123', 'world', '456', 'hello']) == "<b>hello123world456</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",words = ['test', 'string', 'is', 'a', 'this', 'ing', 'est']) == "<b>thisisateststring</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",words = ['test', 'string', 'is', 'a', 'this', 'ing', 'est']) == "<b>thisisateststring</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == "a<b>abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz</b>z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == "a<b>abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz</b>z": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaababa",words = ['aba', 'abaab']) == "<b>ababaababa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaababa",words = ['aba', 'abaab']) == "<b>ababaababa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",words = ['aba', 'bab', 'ab', 'baba', 'abab']) == "<b>ababababab</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",words = ['aba', 'bab', 'ab', 'baba', 'abab']) == "<b>ababababab</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",words = ['xy', 'yz', 'zxy', 'zyx']) == "<b>xyzxyzxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",words = ['xy', 'yz', 'zxy', 'zyx']) == "<b>xyzxyzxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "consecutivetags",words = ['con', 'sec', 'secu', 'utive', 'tags', 'ag']) == "<b>consecutivetags</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consecutivetags",words = ['con', 'sec', 'secu', 'utive', 'tags', 'ag']) == "<b>consecutivetags</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345678901234567890",words = ['123', '456', '789', '012', '345', '678', '901']) == "<b>1234567890123456789</b>0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345678901234567890",words = ['123', '456', '789', '012', '345', '678', '901']) == "<b>1234567890123456789</b>0": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlaplaplaplaplaplaplaplaplaplaplaplaplaplaplaplap",words = ['lap', 'overlap', 'laplap', 'laplaplaplap']) == "<b>overlaplaplaplaplaplaplaplaplaplaplaplaplaplaplaplap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlaplaplaplaplaplaplaplaplaplaplaplaplaplaplaplap",words = ['lap', 'overlap', 'laplap', 'laplaplaplap']) == "<b>overlaplaplaplaplaplaplaplaplaplaplaplaplaplaplaplap</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",words = ['abcabc', 'bcabcabc', 'cabcab', 'abc', 'ab', 'bc', 'ca']) == "<b>abcabcabcabcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",words = ['abcabc', 'bcabcabc', 'cabcab', 'abc', 'ab', 'bc', 'ca']) == "<b>abcabcabcabcabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlapoverlap",words = ['over', 'lap', 'lapo', 'olap']) == "<b>overlapoverlap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlapoverlap",words = ['over', 'lap', 'lapo', 'olap']) == "<b>overlapoverlap</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",words = ['aba', 'bab', 'abab']) == "<b>ababababab</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",words = ['aba', 'bab', 'abab']) == "<b>ababababab</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquecharacters",words = ['unique', 'char', 'acter', 'ers', 's']) == "<b>uniquecharacters</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquecharacters",words = ['unique', 'char', 'acter', 'ers', 's']) == "<b>uniquecharacters</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",words = ['hello', 'hell', 'lohe', 'ellhe']) == "<b>hellohellohello</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",words = ['hello', 'hell', 'lohe', 'ellhe']) == "<b>hellohellohello</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",words = ['aba', 'bab', 'aab', 'abb']) == "<b>ababababab</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",words = ['aba', 'bab', 'aab', 'abb']) == "<b>ababababab</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "consecutivewordwordword",words = ['word', 'consecutive', 'consecutiveword']) == "<b>consecutivewordwordword</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consecutivewordwordword",words = ['word', 'consecutive', 'consecutiveword']) == "<b>consecutivewordwordword</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippissippi",words = ['miss', 'issi', 'issipp']) == "<b>mississippissipp</b>i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippissippi",words = ['miss', 'issi', 'issipp']) == "<b>mississippissipp</b>i": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaa",words = ['aaa', 'bbb', 'aaaaabbbbbaaaaa']) == "<b>aaaaabbbbbaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaa",words = ['aaa', 'bbb', 'aaaaabbbbbaaaaa']) == "<b>aaaaabbbbbaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",words = ['aba', 'bac', 'dab']) == "<b>abacabadabacaba</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",words = ['aba', 'bac', 'dab']) == "<b>abacabadabacaba</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",words = ['ab', 'bc', 'cd', 'de']) == "a<b>abbccdde</b>eff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",words = ['ab', 'bc', 'cd', 'de']) == "a<b>abbccdde</b>eff": {e}')
    
    total += 1
    try:
        result = candidate(s = "consecutiveconsecutive",words = ['consec', 'sec', 'secutive', 'con', 'consecutiveconsecutive']) == "<b>consecutiveconsecutive</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consecutiveconsecutive",words = ['consec', 'sec', 'secutive', 'con', 'consecutiveconsecutive']) == "<b>consecutiveconsecutive</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlapoverlap",words = ['lap', 'over', 'lapover', 'overlaplap']) == "<b>overlapoverlap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlapoverlap",words = ['lap', 'over', 'lapover', 'overlaplap']) == "<b>overlapoverlap</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",words = ['abcabc', 'bcabcabc', 'cabcab']) == "<b>abcabcabcabcabcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",words = ['abcabc', 'bcabcabc', 'cabcab']) == "<b>abcabcabcabcabcabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz",words = ['zz', 'zzz']) == "<b>zzzzzzzzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz",words = ['zz', 'zzz']) == "<b>zzzzzzzzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmultiplesubstrings",words = ['this', 'is', 'averylong', 'substring', 'stringwithmultiplesubstrings']) == "<b>thisisaverylongstringwithmultiplesubstrings</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmultiplesubstrings",words = ['this', 'is', 'averylong', 'substring', 'stringwithmultiplesubstrings']) == "<b>thisisaverylongstringwithmultiplesubstrings</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlappingboldtags",words = ['overlapping', 'lappingb', 'boldtags', 'olap', 'tags']) == "<b>overlappingboldtags</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlappingboldtags",words = ['overlapping', 'lappingb', 'boldtags', 'olap', 'tags']) == "<b>overlappingboldtags</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "overlapoverlapping",words = ['over', 'lap', 'lapping']) == "<b>overlapoverlapping</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlapoverlapping",words = ['over', 'lap', 'lapping']) == "<b>overlapoverlapping</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "multiplewordswithmultipleoccurrences",words = ['word', 'with', 'multiple', 'occurrences', 'mu', 'ple', 'pleo']) == "<b>multipleword</b>s<b>withmultipleoccurrences</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "multiplewordswithmultipleoccurrences",words = ['word', 'with', 'multiple', 'occurrences', 'mu', 'ple', 'pleo']) == "<b>multipleword</b>s<b>withmultipleoccurrences</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "nestedboldnested",words = ['bold', 'nest', 'nested']) == "<b>nestedboldnested</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nestedboldnested",words = ['bold', 'nest', 'nested']) == "<b>nestedboldnested</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",words = ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abcd', 'bcda', 'cdab', 'dabc']) == "<b>abcdabcdabcdabcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",words = ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abcd', 'bcda', 'cdab', 'dabc']) == "<b>abcdabcdabcdabcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "multipleoccurrences",words = ['mul', 'ple', 'occ', 'cur', 'rences', 'en']) == "<b>mul</b>ti<b>pleoccurrences</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "multipleoccurrences",words = ['mul', 'ple', 'occ', 'cur', 'rences', 'en']) == "<b>mul</b>ti<b>pleoccurrences</b>": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",words = ['abcabc', 'bcab', 'cabc']) == "<b>abcabcabcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",words = ['abcabc', 'bcab', 'cabc']) == "<b>abcabcabcabc</b>": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "hello",words = ['world']) == "hello"
    assert candidate(s = "mississippi",words = ['issi', 'issip', 'is', 'i']) == "m<b>ississip</b>p<b>i</b>"
    assert candidate(s = "abcd",words = ['e', 'f', 'g']) == "abcd"
    assert candidate(s = "hello",words = ['ll', 'o']) == "he<b>llo</b>"
    assert candidate(s = "",words = ['a']) == ""
    assert candidate(s = "zzzz",words = ['zz']) == "<b>zzzz</b>"
    assert candidate(s = "abcd",words = ['a', 'b', 'c', 'd']) == "<b>abcd</b>"
    assert candidate(s = "abcabcabc",words = ['abc', 'cab']) == "<b>abcabcabc</b>"
    assert candidate(s = "hellothere",words = ['he', 'lo']) == "<b>he</b>l<b>lo</b>t<b>he</b>re"
    assert candidate(s = "abcxyz123",words = ['abc', '123']) == "<b>abc</b>xyz<b>123</b>"
    assert candidate(s = "aaaaa",words = ['a', 'aa']) == "<b>aaaaa</b>"
    assert candidate(s = "aaabbb",words = ['aa', 'b']) == "<b>aaabbb</b>"
    assert candidate(s = "mississippi",words = ['issi', 'issipp']) == "m<b>ississipp</b>i"
    assert candidate(s = "complexity",words = ['com', 'plex', 'ity', 'ityt', 'ex']) == "<b>complexity</b>"
    assert candidate(s = "aaaaabbbbbaaaaa",words = ['aaa', 'bbbb', 'aaabbbbbaaa']) == "<b>aaaaabbbbbaaaaa</b>"
    assert candidate(s = "mississippiissippi",words = ['issi', 'issipp', 'ippi', 'miss', 'ippii', 'ssippi']) == "<b>mississippiissippi</b>"
    assert candidate(s = "thisisateststring",words = ['this', 'test', 'string', 'is']) == "<b>thisis</b>a<b>teststring</b>"
    assert candidate(s = "aabbccddeeff",words = ['aa', 'bbcc', 'ccdd', 'ddeeff', 'efff', 'ff']) == "<b>aabbccddeeff</b>"
    assert candidate(s = "xyzxyzxyz",words = ['xy', 'yz', 'zxy']) == "<b>xyzxyzxyz</b>"
    assert candidate(s = "abcdefgabcdefg",words = ['abc', 'cde', 'efg', 'abcd']) == "<b>abcdefgabcdefg</b>"
    assert candidate(s = "abcdeabcdeabcde",words = ['abc', 'deabc', 'cde']) == "<b>abcdeabcdeabcde</b>"
    assert candidate(s = "aaaaaabbbbbaaaaa",words = ['aaa', 'bbb']) == "<b>aaaaaabbbbbaaaaa</b>"
    assert candidate(s = "thisisateststring",words = ['this', 'is', 'test', 'string', 'a']) == "<b>thisisateststring</b>"
    assert candidate(s = "nestedboldboldnested",words = ['nestedbold', 'boldbold', 'bold']) == "<b>nestedboldbold</b>nested"
    assert candidate(s = "overlapexample",words = ['over', 'lap', 'example', 'exam']) == "<b>overlapexample</b>"
    assert candidate(s = "nestedboldtags",words = ['nest', 'sted', 'bold', 'tags', 'edta']) == "<b>nestedboldtags</b>"
    assert candidate(s = "overlappingboldtags",words = ['overlap', 'ping', 'bold', 'tags', 'pinging']) == "<b>overlappingboldtags</b>"
    assert candidate(s = "xyzabcxyzabcxyz",words = ['xyz', 'abc', 'ab', 'bc', 'yz', 'xy']) == "<b>xyzabcxyzabcxyz</b>"
    assert candidate(s = "abababababab",words = ['aba', 'bab', 'ab', 'ba']) == "<b>abababababab</b>"
    assert candidate(s = "oneonetwoonetwoonetwoonetwoonetwoone",words = ['one', 'onetwo', 'two', 'onetwone', 'oneto']) == "<b>oneonetwoonetwoonetwoonetwoonetwoone</b>"
    assert candidate(s = "aaaaaaa",words = ['aa', 'aaa']) == "<b>aaaaaaa</b>"
    assert candidate(s = "abababababa",words = ['aba', 'bab']) == "<b>abababababa</b>"
    assert candidate(s = "abcdefgabcdefg",words = ['abc', 'defg', 'bcde', 'fgh']) == "<b>abcdefgabcdefg</b>"
    assert candidate(s = "abababababa",words = ['aba', 'bab', 'aba', 'abb']) == "<b>abababababa</b>"
    assert candidate(s = "abcdabcdabcdabcd",words = ['abcd', 'bcd', 'cd', 'd', 'a', 'ab', 'bc', 'cd', 'abc', 'bca', 'cab', 'dabcd', 'abcdabc', 'bcdbca']) == "<b>abcdabcdabcdabcd</b>"
    assert candidate(s = "xyzxyzxyzxyz",words = ['xy', 'yz', 'zxy', 'xyz']) == "<b>xyzxyzxyzxyz</b>"
    assert candidate(s = "overlappingboldtags",words = ['lap', 'bold', 'tag', 'pingb', 'lapin']) == "over<b>lappingboldtag</b>s"
    assert candidate(s = "ababaabababa",words = ['aba', 'bab', 'abaabababa']) == "<b>ababaabababa</b>"
    assert candidate(s = "xyzzxyzzxyzz",words = ['xyz', 'zzx', 'xy', 'yz']) == "<b>xyzzxyzzxyz</b>z"
    assert candidate(s = "mixednumbersandletters123",words = ['123', 'and', 'num', 'bers', 'mixed']) == "<b>mixednumbersand</b>letters<b>123</b>"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aabbcc', 'ddeeff', 'gghhii']) == "<b>aabbccddeeffgghhii</b>jjkkllmmnnooppqqrrssttuuvvwwxxy<b>yz</b>z"
    assert candidate(s = "consecutiveboldboldbold",words = ['consecutive', 'boldbold', 'bold']) == "<b>consecutiveboldboldbold</b>"
    assert candidate(s = "xyzabcxyzabc",words = ['abc', 'xyz', 'xy']) == "<b>xyzabcxyzabc</b>"
    assert candidate(s = "overlaplap",words = ['lap', 'laplap', 'over']) == "<b>overlaplap</b>"
    assert candidate(s = "thisisateststring",words = ['test', 'this', 'string', 'est', 'ing']) == "<b>this</b>isa<b>teststring</b>"
    assert candidate(s = "aaaaabaaaabaaaa",words = ['aa', 'aaa', 'aaaa']) == "<b>aaaaa</b>b<b>aaaa</b>b<b>aaaa</b>"
    assert candidate(s = "aaaaaaabbbbbbcccccc",words = ['aaa', 'bbb', 'ccc', 'aabb', 'bbcc', 'aabbcc']) == "<b>aaaaaaabbbbbbcccccc</b>"
    assert candidate(s = "1234567890",words = ['12', '23', '34', '45', '56', '67', '78', '89', '90']) == "<b>1234567890</b>"
    assert candidate(s = "zzzzzzzzzzzzzzz",words = ['zzzz', 'zzz', 'zz', 'z']) == "<b>zzzzzzzzzzzzzzz</b>"
    assert candidate(s = "aaaaaa",words = ['a', 'aa', 'aaa', 'aaaa']) == "<b>aaaaaa</b>"
    assert candidate(s = "abracadabra",words = ['bra', 'cad', 'ra']) == "a<b>bracad</b>a<b>bra</b>"
    assert candidate(s = "nestedboldtags",words = ['nest', 'sted', 'bold', 'tags', 'boldt', 'tagsn']) == "<b>nestedboldtags</b>"
    assert candidate(s = "repeatedpatterns",words = ['re', 'pe', 'at', 'te', 'ed', 'pattern', 'terns']) == "<b>repeatedpatterns</b>"
    assert candidate(s = "1234567890",words = ['12', '234', '456', '678', '890']) == "<b>1234567890</b>"
    assert candidate(s = "thisisateststring",words = ['test', 'is', 'this', 'string']) == "<b>thisis</b>a<b>teststring</b>"
    assert candidate(s = "xyzxyzxyz",words = ['xyz', 'xy', 'yz', 'zxy']) == "<b>xyzxyzxyz</b>"
    assert candidate(s = "abcdabcdeabcd",words = ['abc', 'de', 'bcd']) == "<b>abcdabcdeabcd</b>"
    assert candidate(s = "1234567890",words = ['123', '456', '789', '0']) == "<b>1234567890</b>"
    assert candidate(s = "longstringwithmanywords",words = ['long', 'string', 'with', 'many', 'words', 'longstring', 'stringwith', 'withman']) == "<b>longstringwithmanywords</b>"
    assert candidate(s = "12345678901234567890",words = ['123', '234', '4567', '890']) == "<b>12345678901234567890</b>"
    assert candidate(s = "a1b2c3d4e5f6g7h8i9j0",words = ['a1b2', 'b2c3', 'c3d4', 'd4e5', 'e5f6', 'f6g7', 'g7h8', 'h8i9', 'i9j0']) == "<b>a1b2c3d4e5f6g7h8i9j0</b>"
    assert candidate(s = "aaaaaabbbbcccc",words = ['aa', 'bbb', 'cccc', 'aabbb', 'bbccc']) == "<b>aaaaaabbbbcccc</b>"
    assert candidate(s = "multiplewordsinsequence",words = ['mul', 'ple', 'word', 'in', 'seq', 'uence']) == "<b>mul</b>ti<b>pleword</b>s<b>insequence</b>"
    assert candidate(s = "abcdeabcdeabcdeabcde",words = ['abc', 'de', 'cde', 'abcde', 'bcde', 'cdea']) == "<b>abcdeabcdeabcdeabcde</b>"
    assert candidate(s = "xyzxyzxyz",words = ['xyz', 'zyx', 'xy', 'yx']) == "<b>xyzxyzxyz</b>"
    assert candidate(s = "consecutiveconsecutiveconsecutive",words = ['con', 'consec', 'consecutive', 'sec']) == "<b>consecutiveconsecutiveconsecutive</b>"
    assert candidate(s = "consecutivesubstrings",words = ['con', 'sec', 'cut', 'utive', 'sub', 'strings']) == "<b>consecutivesubstrings</b>"
    assert candidate(s = "aaaaaabbbbbaaaa",words = ['aaa', 'bbb']) == "<b>aaaaaabbbbbaaaa</b>"
    assert candidate(s = "thisisateststringfortestingboldtags",words = ['test', 'this', 'that', 'for', 'bold', 'tags', 'string']) == "<b>this</b>isa<b>teststringfortest</b>ing<b>boldtags</b>"
    assert candidate(s = "12345678901234567890",words = ['123', '456', '789', '012', '345', '678', '901']) == "<b>1234567890123456789</b>0"
    assert candidate(s = "abcdefgabcdefg",words = ['abc', 'def', 'gab', 'efg']) == "<b>abcdefgabcdefg</b>"
    assert candidate(s = "aaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == "<b>aaaaa</b>"
    assert candidate(s = "zzzzzzzzzzzzzzzzz",words = ['zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == "<b>zzzzzzzzzzzzzzzzz</b>"
    assert candidate(s = "ababaababa",words = ['aba', 'baa']) == "<b>ababaababa</b>"
    assert candidate(s = "1234567890",words = ['123', '456', '789', '012', '34567890']) == "<b>1234567890</b>"
    assert candidate(s = "repeatedrepeatedrepeated",words = ['re', 'rep', 'peat', 'repeated']) == "<b>repeatedrepeatedrepeated</b>"
    assert candidate(s = "aabbccddeeffgghhiijj",words = ['abc', 'def', 'gh', 'ij', 'bb', 'cc']) == "aa<b>bbcc</b>ddeeffg<b>gh</b>hi<b>ij</b>j"
    assert candidate(s = "uniquestringsareunique",words = ['unique', 'strings', 'are']) == "<b>uniquestringsareunique</b>"
    assert candidate(s = "hello123world456",words = ['123', 'world', '456', 'hello']) == "<b>hello123world456</b>"
    assert candidate(s = "thisisateststring",words = ['test', 'string', 'is', 'a', 'this', 'ing', 'est']) == "<b>thisisateststring</b>"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == "a<b>abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz</b>z"
    assert candidate(s = "ababaababa",words = ['aba', 'abaab']) == "<b>ababaababa</b>"
    assert candidate(s = "ababababab",words = ['aba', 'bab', 'ab', 'baba', 'abab']) == "<b>ababababab</b>"
    assert candidate(s = "xyzxyzxyz",words = ['xy', 'yz', 'zxy', 'zyx']) == "<b>xyzxyzxyz</b>"
    assert candidate(s = "consecutivetags",words = ['con', 'sec', 'secu', 'utive', 'tags', 'ag']) == "<b>consecutivetags</b>"
    assert candidate(s = "12345678901234567890",words = ['123', '456', '789', '012', '345', '678', '901']) == "<b>1234567890123456789</b>0"
    assert candidate(s = "overlaplaplaplaplaplaplaplaplaplaplaplaplaplaplaplap",words = ['lap', 'overlap', 'laplap', 'laplaplaplap']) == "<b>overlaplaplaplaplaplaplaplaplaplaplaplaplaplaplaplap</b>"
    assert candidate(s = "abcabcabcabcabc",words = ['abcabc', 'bcabcabc', 'cabcab', 'abc', 'ab', 'bc', 'ca']) == "<b>abcabcabcabcabc</b>"
    assert candidate(s = "overlapoverlap",words = ['over', 'lap', 'lapo', 'olap']) == "<b>overlapoverlap</b>"
    assert candidate(s = "ababababab",words = ['aba', 'bab', 'abab']) == "<b>ababababab</b>"
    assert candidate(s = "uniquecharacters",words = ['unique', 'char', 'acter', 'ers', 's']) == "<b>uniquecharacters</b>"
    assert candidate(s = "hellohellohello",words = ['hello', 'hell', 'lohe', 'ellhe']) == "<b>hellohellohello</b>"
    assert candidate(s = "ababababab",words = ['aba', 'bab', 'aab', 'abb']) == "<b>ababababab</b>"
    assert candidate(s = "consecutivewordwordword",words = ['word', 'consecutive', 'consecutiveword']) == "<b>consecutivewordwordword</b>"
    assert candidate(s = "mississippissippi",words = ['miss', 'issi', 'issipp']) == "<b>mississippissipp</b>i"
    assert candidate(s = "aaaaabbbbbaaaaa",words = ['aaa', 'bbb', 'aaaaabbbbbaaaaa']) == "<b>aaaaabbbbbaaaaa</b>"
    assert candidate(s = "abacabadabacaba",words = ['aba', 'bac', 'dab']) == "<b>abacabadabacaba</b>"
    assert candidate(s = "aabbccddeeff",words = ['ab', 'bc', 'cd', 'de']) == "a<b>abbccdde</b>eff"
    assert candidate(s = "consecutiveconsecutive",words = ['consec', 'sec', 'secutive', 'con', 'consecutiveconsecutive']) == "<b>consecutiveconsecutive</b>"
    assert candidate(s = "overlapoverlap",words = ['lap', 'over', 'lapover', 'overlaplap']) == "<b>overlapoverlap</b>"
    assert candidate(s = "abcabcabcabcabcabc",words = ['abcabc', 'bcabcabc', 'cabcab']) == "<b>abcabcabcabcabcabc</b>"
    assert candidate(s = "zzzzzzzzz",words = ['zz', 'zzz']) == "<b>zzzzzzzzz</b>"
    assert candidate(s = "thisisaverylongstringwithmultiplesubstrings",words = ['this', 'is', 'averylong', 'substring', 'stringwithmultiplesubstrings']) == "<b>thisisaverylongstringwithmultiplesubstrings</b>"
    assert candidate(s = "overlappingboldtags",words = ['overlapping', 'lappingb', 'boldtags', 'olap', 'tags']) == "<b>overlappingboldtags</b>"
    assert candidate(s = "overlapoverlapping",words = ['over', 'lap', 'lapping']) == "<b>overlapoverlapping</b>"
    assert candidate(s = "multiplewordswithmultipleoccurrences",words = ['word', 'with', 'multiple', 'occurrences', 'mu', 'ple', 'pleo']) == "<b>multipleword</b>s<b>withmultipleoccurrences</b>"
    assert candidate(s = "nestedboldnested",words = ['bold', 'nest', 'nested']) == "<b>nestedboldnested</b>"
    assert candidate(s = "abcdabcdabcdabcd",words = ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abcd', 'bcda', 'cdab', 'dabc']) == "<b>abcdabcdabcdabcd</b>"
    assert candidate(s = "multipleoccurrences",words = ['mul', 'ple', 'occ', 'cur', 'rences', 'en']) == "<b>mul</b>ti<b>pleoccurrences</b>"
    assert candidate(s = "abcabcabcabc",words = ['abcabc', 'bcab', 'cabc']) == "<b>abcabcabcabc</b>"


