def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 3,fill = "x") == ['abc', 'def', 'ghi', 'jxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 3,fill = "x") == ['abc', 'def', 'ghi', 'jxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 2,fill = "z") == ['ab', 'cd', 'ef', 'gz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 2,fill = "z") == ['ab', 'cd', 'ef', 'gz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",k = 3,fill = "x") == ['abc', 'def', 'ghi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",k = 3,fill = "x") == ['abc', 'def', 'ghi']: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1,fill = "y") == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1,fill = "y") == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",k = 6,fill = "q") == ['python']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",k = 6,fill = "q") == ['python']: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello world",k = 4,fill = "_") == ['hell', 'o wo', 'rld_']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello world",k = 4,fill = "_") == ['hell', 'o wo', 'rld_']: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",k = 1,fill = "a") == ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",k = 1,fill = "a") == ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello world",k = 2,fill = "_") == ['he', 'll', 'o ', 'wo', 'rl', 'd_']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello world",k = 2,fill = "_") == ['he', 'll', 'o ', 'wo', 'rl', 'd_']: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 3,fill = "b") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 3,fill = "b") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",k = 2,fill = "q") == ['he', 'll', 'oq']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",k = 2,fill = "q") == ['he', 'll', 'oq']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",k = 5,fill = "z") == ['abczz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 5,fill = "z") == ['abczz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 5,fill = "y") == ['ayyyy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 5,fill = "y") == ['ayyyy']: {e}')
    
    total += 1
    try:
        result = candidate(s = "boundarycase",k = 8,fill = "b") == ['boundary', 'casebbbb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "boundarycase",k = 8,fill = "b") == ['boundary', 'casebbbb']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstring",k = 5,fill = "p") == ['thisi', 'saver', 'ylong', 'strin', 'gpppp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstring",k = 5,fill = "p") == ['thisi', 'saver', 'ylong', 'strin', 'gpppp']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyz",k = 2,fill = "g") == ['ab', 'cd', 'ex', 'yz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyz",k = 2,fill = "g") == ['ab', 'cd', 'ex', 'yz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharacters",k = 7,fill = "e") == ['repeate', 'dcharac', 'terseee']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharacters",k = 7,fill = "e") == ['repeate', 'dcharac', 'terseee']: {e}')
    
    total += 1
    try:
        result = candidate(s = "interview",k = 2,fill = "z") == ['in', 'te', 'rv', 'ie', 'wz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "interview",k = 2,fill = "z") == ['in', 'te', 'rv', 'ie', 'wz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 7,fill = "z") == ['abcdefg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 7,fill = "z") == ['abcdefg']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 5,fill = "m") == ['abcde', 'fghij', 'kmmmm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 5,fill = "m") == ['abcde', 'fghij', 'kmmmm']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 8,fill = "n") == ['abcdefnn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 8,fill = "n") == ['abcdefnn']: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",k = 3,fill = "a") == ['pro', 'gra', 'mmi', 'nga']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",k = 3,fill = "a") == ['pro', 'gra', 'mmi', 'nga']: {e}')
    
    total += 1
    try:
        result = candidate(s = "complexstringwithfill",k = 9,fill = "r") == ['complexst', 'ringwithf', 'illrrrrrr']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complexstringwithfill",k = 9,fill = "r") == ['complexst', 'ringwithf', 'illrrrrrr']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 5,fill = "t") == ['abcdt']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 5,fill = "t") == ['abcdt']: {e}')
    
    total += 1
    try:
        result = candidate(s = "almostfill",k = 9,fill = "l") == ['almostfil', 'lllllllll']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "almostfill",k = 9,fill = "l") == ['almostfil', 'lllllllll']: {e}')
    
    total += 1
    try:
        result = candidate(s = "partitioning",k = 3,fill = "z") == ['par', 'tit', 'ion', 'ing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partitioning",k = 3,fill = "z") == ['par', 'tit', 'ion', 'ing']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyz",k = 1,fill = "m") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'y', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyz",k = 1,fill = "m") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'y', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 1,fill = "d") == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 1,fill = "d") == ['a', 'b', 'c', 'd', 'e', 'f', 'g']: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",k = 4,fill = "o") == ['hell', 'oooo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",k = 4,fill = "o") == ['hell', 'oooo']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij",k = 11,fill = "c") == ['abcdefghija', 'bcdefghijcc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij",k = 11,fill = "c") == ['abcdefghija', 'bcdefghijcc']: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatthispattern",k = 8,fill = "m") == ['repeatth', 'ispatter', 'nmmmmmmm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatthispattern",k = 8,fill = "m") == ['repeatth', 'ispatter', 'nmmmmmmm']: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",k = 2,fill = "l") == ['ab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",k = 2,fill = "l") == ['ab']: {e}')
    
    total += 1
    try:
        result = candidate(s = "example",k = 2,fill = "z") == ['ex', 'am', 'pl', 'ez']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "example",k = 2,fill = "z") == ['ex', 'am', 'pl', 'ez']: {e}')
    
    total += 1
    try:
        result = candidate(s = "fill",k = 1,fill = "f") == ['f', 'i', 'l', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fill",k = 1,fill = "f") == ['f', 'i', 'l', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatneedstobedivided",k = 5,fill = "a") == ['thisi', 'saver', 'ylong', 'strin', 'gthat', 'needs', 'tobed', 'ivide', 'daaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatneedstobedivided",k = 5,fill = "a") == ['thisi', 'saver', 'ylong', 'strin', 'gthat', 'needs', 'tobed', 'ivide', 'daaaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 1,fill = "m") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 1,fill = "m") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']: {e}')
    
    total += 1
    try:
        result = candidate(s = "short",k = 5,fill = "q") == ['short']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "short",k = 5,fill = "q") == ['short']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstring",k = 5,fill = "m") == ['thisi', 'saver', 'ylong', 'strin', 'gmmmm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstring",k = 5,fill = "m") == ['thisi', 'saver', 'ylong', 'strin', 'gmmmm']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 2,fill = "w") == ['ab', 'cd', 'ef', 'gh', 'ij']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 2,fill = "w") == ['ab', 'cd', 'ef', 'gh', 'ij']: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",k = 4,fill = "p") == ['hell', 'oppp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",k = 4,fill = "p") == ['hell', 'oppp']: {e}')
    
    total += 1
    try:
        result = candidate(s = "almostfullgroup",k = 10,fill = "a") == ['almostfull', 'groupaaaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "almostfullgroup",k = 10,fill = "a") == ['almostfull', 'groupaaaaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwen",k = 2,fill = "q") == ['qw', 'en']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwen",k = 2,fill = "q") == ['qw', 'en']: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",k = 1,fill = "b") == ['h', 'e', 'l', 'l', 'o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",k = 1,fill = "b") == ['h', 'e', 'l', 'l', 'o']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 2,fill = "p") == ['ab', 'cd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 2,fill = "p") == ['ab', 'cd']: {e}')
    
    total += 1
    try:
        result = candidate(s = "partitioning",k = 5,fill = "p") == ['parti', 'tioni', 'ngppp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partitioning",k = 5,fill = "p") == ['parti', 'tioni', 'ngppp']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisanexample",k = 3,fill = "y") == ['thi', 'sis', 'ane', 'xam', 'ple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisanexample",k = 3,fill = "y") == ['thi', 'sis', 'ane', 'xam', 'ple']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 10,fill = "q") == ['abcdefgqqq']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 10,fill = "q") == ['abcdefgqqq']: {e}')
    
    total += 1
    try:
        result = candidate(s = "samecharacter",k = 2,fill = "s") == ['sa', 'me', 'ch', 'ar', 'ac', 'te', 'rs']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "samecharacter",k = 2,fill = "s") == ['sa', 'me', 'ch', 'ar', 'ac', 'te', 'rs']: {e}')
    
    total += 1
    try:
        result = candidate(s = "fillingwithx",k = 7,fill = "x") == ['filling', 'withxxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fillingwithx",k = 7,fill = "x") == ['filling', 'withxxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "longerstring",k = 6,fill = "p") == ['longer', 'string']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longerstring",k = 6,fill = "p") == ['longer', 'string']: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",k = 4,fill = "m") == ['algo', 'rith', 'mmmm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",k = 4,fill = "m") == ['algo', 'rith', 'mmmm']: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",k = 6,fill = "o") == ['xyloph', 'oneooo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",k = 6,fill = "o") == ['xyloph', 'oneooo']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatneedstobedivided",k = 5,fill = "x") == ['thisi', 'saver', 'ylong', 'strin', 'gthat', 'needs', 'tobed', 'ivide', 'dxxxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatneedstobedivided",k = 5,fill = "x") == ['thisi', 'saver', 'ylong', 'strin', 'gthat', 'needs', 'tobed', 'ivide', 'dxxxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdea",k = 4,fill = "w") == ['abcd', 'eabc', 'deab', 'cdea']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdea",k = 4,fill = "w") == ['abcd', 'eabc', 'deab', 'cdea']: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",k = 1,fill = "v") == ['x', 'y', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",k = 1,fill = "v") == ['x', 'y', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(s = "evenlydivisible",k = 2,fill = "q") == ['ev', 'en', 'ly', 'di', 'vi', 'si', 'bl', 'eq']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "evenlydivisible",k = 2,fill = "q") == ['ev', 'en', 'ly', 'di', 'vi', 'si', 'bl', 'eq']: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",k = 3,fill = "w") == ['pro', 'gra', 'mmi', 'ngw']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",k = 3,fill = "w") == ['pro', 'gra', 'mmi', 'ngw']: {e}')
    
    total += 1
    try:
        result = candidate(s = "boundarycase",k = 9,fill = "b") == ['boundaryc', 'asebbbbbb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "boundarycase",k = 9,fill = "b") == ['boundaryc', 'asebbbbbb']: {e}')
    
    total += 1
    try:
        result = candidate(s = "onemoretestcase",k = 6,fill = "t") == ['onemor', 'etestc', 'asettt']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onemoretestcase",k = 6,fill = "t") == ['onemor', 'etestc', 'asettt']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 3,fill = "v") == ['abc', 'def', 'gvv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 3,fill = "v") == ['abc', 'def', 'gvv']: {e}')
    
    total += 1
    try:
        result = candidate(s = "equalgroups",k = 5,fill = "w") == ['equal', 'group', 'swwww']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "equalgroups",k = 5,fill = "w") == ['equal', 'group', 'swwww']: {e}')
    
    total += 1
    try:
        result = candidate(s = "equalgroups",k = 3,fill = "c") == ['equ', 'alg', 'rou', 'psc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "equalgroups",k = 3,fill = "c") == ['equ', 'alg', 'rou', 'psc']: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfox",k = 3,fill = "y") == ['qui', 'ckb', 'row', 'nfo', 'xyy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfox",k = 3,fill = "y") == ['qui', 'ckb', 'row', 'nfo', 'xyy']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 7,fill = "n") == ['abcdefn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 7,fill = "n") == ['abcdefn']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 4,fill = "x") == ['abcd', 'efgh', 'ijxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 4,fill = "x") == ['abcd', 'efgh', 'ijxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 7,fill = "z") == ['abcdefz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 7,fill = "z") == ['abcdefz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "zebra",k = 1,fill = "x") == ['z', 'e', 'b', 'r', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zebra",k = 1,fill = "x") == ['z', 'e', 'b', 'r', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(s = "this is a test",k = 5,fill = "_") == ['this ', 'is a ', 'test_']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "this is a test",k = 5,fill = "_") == ['this ', 'is a ', 'test_']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 2,fill = "o") == ['ab', 'cd', 'ef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 2,fill = "o") == ['ab', 'cd', 'ef']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisalongstring",k = 4,fill = "x") == ['this', 'isal', 'ongs', 'trin', 'gxxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisalongstring",k = 4,fill = "x") == ['this', 'isal', 'ongs', 'trin', 'gxxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "partitioning",k = 7,fill = "f") == ['partiti', 'oningff']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partitioning",k = 7,fill = "f") == ['partiti', 'oningff']: {e}')
    
    total += 1
    try:
        result = candidate(s = "example",k = 10,fill = "z") == ['examplezzz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "example",k = 10,fill = "z") == ['examplezzz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 4,fill = "e") == ['abcd', 'efgh', 'ijee']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 4,fill = "e") == ['abcd', 'efgh', 'ijee']: {e}')
    
    total += 1
    try:
        result = candidate(s = "programmingisfun",k = 5,fill = "a") == ['progr', 'ammin', 'gisfu', 'naaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programmingisfun",k = 5,fill = "a") == ['progr', 'ammin', 'gisfu', 'naaaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatwillneedfilling",k = 7,fill = "a") == ['thisisa', 'verylon', 'gstring', 'thatwil', 'lneedfi', 'llingaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatwillneedfilling",k = 7,fill = "a") == ['thisisa', 'verylon', 'gstring', 'thatwil', 'lneedfi', 'llingaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "onetwothreefourfive",k = 6,fill = "j") == ['onetwo', 'threef', 'ourfiv', 'ejjjjj']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onetwothreefourfive",k = 6,fill = "j") == ['onetwo', 'threef', 'ourfiv', 'ejjjjj']: {e}')
    
    total += 1
    try:
        result = candidate(s = "world",k = 10,fill = "c") == ['worldccccc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "world",k = 10,fill = "c") == ['worldccccc']: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",k = 10,fill = "a") == ['xyzaaaaaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",k = 10,fill = "a") == ['xyzaaaaaaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello world",k = 4,fill = "x") == ['hell', 'o wo', 'rldx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello world",k = 4,fill = "x") == ['hell', 'o wo', 'rldx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyz",k = 4,fill = "a") == ['abcd', 'efgx', 'yzaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyz",k = 4,fill = "a") == ['abcd', 'efgx', 'yzaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 4,fill = "x") == ['abcd', 'efgh', 'ijkx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 4,fill = "x") == ['abcd', 'efgh', 'ijkx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "partition",k = 1,fill = "m") == ['p', 'a', 'r', 't', 'i', 't', 'i', 'o', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partition",k = 1,fill = "m") == ['p', 'a', 'r', 't', 'i', 't', 'i', 'o', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithms",k = 7,fill = "b") == ['algorit', 'hmsbbbb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithms",k = 7,fill = "b") == ['algorit', 'hmsbbbb']: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharacterstest",k = 7,fill = "z") == ['repeate', 'dcharac', 'terstes', 'tzzzzzz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharacterstest",k = 7,fill = "z") == ['repeate', 'dcharac', 'terstes', 'tzzzzzz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "almostfull",k = 4,fill = "i") == ['almo', 'stfu', 'llii']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "almostfull",k = 4,fill = "i") == ['almo', 'stfu', 'llii']: {e}')
    
    total += 1
    try:
        result = candidate(s = "filler",k = 11,fill = "l") == ['fillerlllll']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "filler",k = 11,fill = "l") == ['fillerlllll']: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 3,fill = "n") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 3,fill = "n") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 3,fill = "n") == ['abc', 'def', 'ghi', 'jkn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 3,fill = "n") == ['abc', 'def', 'ghi', 'jkn']: {e}')
    
    total += 1
    try:
        result = candidate(s = "elephants",k = 3,fill = "p") == ['ele', 'pha', 'nts']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elephants",k = 3,fill = "p") == ['ele', 'pha', 'nts']: {e}')
    
    total += 1
    try:
        result = candidate(s = "short",k = 10,fill = "p") == ['shortppppp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "short",k = 10,fill = "p") == ['shortppppp']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 6,fill = "w") == ['abcdww']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 6,fill = "w") == ['abcdww']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 2,fill = "x") == ['ab', 'cd', 'ef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 2,fill = "x") == ['ab', 'cd', 'ef']: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfox",k = 4,fill = "x") == ['quic', 'kbro', 'wnfo', 'xxxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfox",k = 4,fill = "x") == ['quic', 'kbro', 'wnfo', 'xxxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwert",k = 10,fill = "n") == ['qwertnnnnn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwert",k = 10,fill = "n") == ['qwertnnnnn']: {e}')
    
    total += 1
    try:
        result = candidate(s = "machinelearning",k = 8,fill = "d") == ['machinel', 'earningd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "machinelearning",k = 8,fill = "d") == ['machinel', 'earningd']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 1,fill = "z") == ['a', 'b', 'c', 'd', 'e', 'f']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 1,fill = "z") == ['a', 'b', 'c', 'd', 'e', 'f']: {e}')
    
    total += 1
    try:
        result = candidate(s = "short",k = 10,fill = "b") == ['shortbbbbb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "short",k = 10,fill = "b") == ['shortbbbbb']: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",k = 7,fill = "a") == ['program', 'mingaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",k = 7,fill = "a") == ['program', 'mingaaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "datastructure",k = 5,fill = "a") == ['datas', 'truct', 'ureaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "datastructure",k = 5,fill = "a") == ['datas', 'truct', 'ureaa']: {e}')
    
    total += 1
    try:
        result = candidate(s = "helloWorld",k = 3,fill = "x") == ['hel', 'loW', 'orl', 'dxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "helloWorld",k = 3,fill = "x") == ['hel', 'loW', 'orl', 'dxx']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkmnopqrstuvwxyz",k = 5,fill = "x") == ['abcde', 'fghij', 'kmnop', 'qrstu', 'vwxyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkmnopqrstuvwxyz",k = 5,fill = "x") == ['abcde', 'fghij', 'kmnop', 'qrstu', 'vwxyz']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 3,fill = "p") == ['abc', 'def', 'ghi', 'jkp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 3,fill = "p") == ['abc', 'def', 'ghi', 'jkp']: {e}')
    
    total += 1
    try:
        result = candidate(s = "divisiblebyk",k = 2,fill = "h") == ['di', 'vi', 'si', 'bl', 'eb', 'yk']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "divisiblebyk",k = 2,fill = "h") == ['di', 'vi', 'si', 'bl', 'eb', 'yk']: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwenassistant",k = 7,fill = "a") == ['qwenass', 'istanta']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwenassistant",k = 7,fill = "a") == ['qwenass', 'istanta']: {e}')
    
    total += 1
    try:
        result = candidate(s = "cloudcomputing",k = 6,fill = "c") == ['cloudc', 'omputi', 'ngcccc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cloudcomputing",k = 6,fill = "c") == ['cloudc', 'omputi', 'ngcccc']: {e}')
    
    total += 1
    try:
        result = candidate(s = "longerstringexample",k = 6,fill = "n") == ['longer', 'string', 'exampl', 'ennnnn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longerstringexample",k = 6,fill = "n") == ['longer', 'string', 'exampl', 'ennnnn']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklnm",k = 4,fill = "r") == ['abcd', 'efgh', 'ijkl', 'nmrr']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklnm",k = 4,fill = "r") == ['abcd', 'efgh', 'ijkl', 'nmrr']: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",k = 5,fill = "b") == ['algor', 'ithmb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",k = 5,fill = "b") == ['algor', 'ithmb']: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfox",k = 3,fill = "m") == ['qui', 'ckb', 'row', 'nfo', 'xmm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfox",k = 3,fill = "m") == ['qui', 'ckb', 'row', 'nfo', 'xmm']: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 4,fill = "x") == ['abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 4,fill = "x") == ['abcd']: {e}')
    
    total += 1
    try:
        result = candidate(s = "almostfull",k = 8,fill = "o") == ['almostfu', 'lloooooo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "almostfull",k = 8,fill = "o") == ['almostfu', 'lloooooo']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefghij",k = 3,fill = "x") == ['abc', 'def', 'ghi', 'jxx']
    assert candidate(s = "abcdefg",k = 2,fill = "z") == ['ab', 'cd', 'ef', 'gz']
    assert candidate(s = "abcdefghi",k = 3,fill = "x") == ['abc', 'def', 'ghi']
    assert candidate(s = "a",k = 1,fill = "y") == ['a']
    assert candidate(s = "python",k = 6,fill = "q") == ['python']
    assert candidate(s = "hello world",k = 4,fill = "_") == ['hell', 'o wo', 'rld_']
    assert candidate(s = "programming",k = 1,fill = "a") == ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
    assert candidate(s = "hello world",k = 2,fill = "_") == ['he', 'll', 'o ', 'wo', 'rl', 'd_']
    assert candidate(s = "",k = 3,fill = "b") == []
    assert candidate(s = "hello",k = 2,fill = "q") == ['he', 'll', 'oq']
    assert candidate(s = "abc",k = 5,fill = "z") == ['abczz']
    assert candidate(s = "a",k = 5,fill = "y") == ['ayyyy']
    assert candidate(s = "boundarycase",k = 8,fill = "b") == ['boundary', 'casebbbb']
    assert candidate(s = "thisisaverylongstring",k = 5,fill = "p") == ['thisi', 'saver', 'ylong', 'strin', 'gpppp']
    assert candidate(s = "abcdexyz",k = 2,fill = "g") == ['ab', 'cd', 'ex', 'yz']
    assert candidate(s = "repeatedcharacters",k = 7,fill = "e") == ['repeate', 'dcharac', 'terseee']
    assert candidate(s = "interview",k = 2,fill = "z") == ['in', 'te', 'rv', 'ie', 'wz']
    assert candidate(s = "abcdefg",k = 7,fill = "z") == ['abcdefg']
    assert candidate(s = "abcdefghijk",k = 5,fill = "m") == ['abcde', 'fghij', 'kmmmm']
    assert candidate(s = "abcdef",k = 8,fill = "n") == ['abcdefnn']
    assert candidate(s = "programming",k = 3,fill = "a") == ['pro', 'gra', 'mmi', 'nga']
    assert candidate(s = "complexstringwithfill",k = 9,fill = "r") == ['complexst', 'ringwithf', 'illrrrrrr']
    assert candidate(s = "abcd",k = 5,fill = "t") == ['abcdt']
    assert candidate(s = "almostfill",k = 9,fill = "l") == ['almostfil', 'lllllllll']
    assert candidate(s = "partitioning",k = 3,fill = "z") == ['par', 'tit', 'ion', 'ing']
    assert candidate(s = "abcdefgxyz",k = 1,fill = "m") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'y', 'z']
    assert candidate(s = "abcdefg",k = 1,fill = "d") == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert candidate(s = "hello",k = 4,fill = "o") == ['hell', 'oooo']
    assert candidate(s = "abcdefghijabcdefghij",k = 11,fill = "c") == ['abcdefghija', 'bcdefghijcc']
    assert candidate(s = "repeatthispattern",k = 8,fill = "m") == ['repeatth', 'ispatter', 'nmmmmmmm']
    assert candidate(s = "ab",k = 2,fill = "l") == ['ab']
    assert candidate(s = "example",k = 2,fill = "z") == ['ex', 'am', 'pl', 'ez']
    assert candidate(s = "fill",k = 1,fill = "f") == ['f', 'i', 'l', 'l']
    assert candidate(s = "thisisaverylongstringthatneedstobedivided",k = 5,fill = "a") == ['thisi', 'saver', 'ylong', 'strin', 'gthat', 'needs', 'tobed', 'ivide', 'daaaa']
    assert candidate(s = "abcdefghijk",k = 1,fill = "m") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    assert candidate(s = "short",k = 5,fill = "q") == ['short']
    assert candidate(s = "thisisaverylongstring",k = 5,fill = "m") == ['thisi', 'saver', 'ylong', 'strin', 'gmmmm']
    assert candidate(s = "abcdefghij",k = 2,fill = "w") == ['ab', 'cd', 'ef', 'gh', 'ij']
    assert candidate(s = "hello",k = 4,fill = "p") == ['hell', 'oppp']
    assert candidate(s = "almostfullgroup",k = 10,fill = "a") == ['almostfull', 'groupaaaaa']
    assert candidate(s = "qwen",k = 2,fill = "q") == ['qw', 'en']
    assert candidate(s = "hello",k = 1,fill = "b") == ['h', 'e', 'l', 'l', 'o']
    assert candidate(s = "abcd",k = 2,fill = "p") == ['ab', 'cd']
    assert candidate(s = "partitioning",k = 5,fill = "p") == ['parti', 'tioni', 'ngppp']
    assert candidate(s = "thisisanexample",k = 3,fill = "y") == ['thi', 'sis', 'ane', 'xam', 'ple']
    assert candidate(s = "abcdefg",k = 10,fill = "q") == ['abcdefgqqq']
    assert candidate(s = "samecharacter",k = 2,fill = "s") == ['sa', 'me', 'ch', 'ar', 'ac', 'te', 'rs']
    assert candidate(s = "fillingwithx",k = 7,fill = "x") == ['filling', 'withxxx']
    assert candidate(s = "longerstring",k = 6,fill = "p") == ['longer', 'string']
    assert candidate(s = "algorithm",k = 4,fill = "m") == ['algo', 'rith', 'mmmm']
    assert candidate(s = "xylophone",k = 6,fill = "o") == ['xyloph', 'oneooo']
    assert candidate(s = "thisisaverylongstringthatneedstobedivided",k = 5,fill = "x") == ['thisi', 'saver', 'ylong', 'strin', 'gthat', 'needs', 'tobed', 'ivide', 'dxxxx']
    assert candidate(s = "abcdeabcdeabcdea",k = 4,fill = "w") == ['abcd', 'eabc', 'deab', 'cdea']
    assert candidate(s = "xyz",k = 1,fill = "v") == ['x', 'y', 'z']
    assert candidate(s = "evenlydivisible",k = 2,fill = "q") == ['ev', 'en', 'ly', 'di', 'vi', 'si', 'bl', 'eq']
    assert candidate(s = "programming",k = 3,fill = "w") == ['pro', 'gra', 'mmi', 'ngw']
    assert candidate(s = "boundarycase",k = 9,fill = "b") == ['boundaryc', 'asebbbbbb']
    assert candidate(s = "onemoretestcase",k = 6,fill = "t") == ['onemor', 'etestc', 'asettt']
    assert candidate(s = "abcdefg",k = 3,fill = "v") == ['abc', 'def', 'gvv']
    assert candidate(s = "equalgroups",k = 5,fill = "w") == ['equal', 'group', 'swwww']
    assert candidate(s = "equalgroups",k = 3,fill = "c") == ['equ', 'alg', 'rou', 'psc']
    assert candidate(s = "quickbrownfox",k = 3,fill = "y") == ['qui', 'ckb', 'row', 'nfo', 'xyy']
    assert candidate(s = "abcdef",k = 7,fill = "n") == ['abcdefn']
    assert candidate(s = "abcdefghij",k = 4,fill = "x") == ['abcd', 'efgh', 'ijxx']
    assert candidate(s = "abcdef",k = 7,fill = "z") == ['abcdefz']
    assert candidate(s = "zebra",k = 1,fill = "x") == ['z', 'e', 'b', 'r', 'a']
    assert candidate(s = "this is a test",k = 5,fill = "_") == ['this ', 'is a ', 'test_']
    assert candidate(s = "abcdef",k = 2,fill = "o") == ['ab', 'cd', 'ef']
    assert candidate(s = "thisisalongstring",k = 4,fill = "x") == ['this', 'isal', 'ongs', 'trin', 'gxxx']
    assert candidate(s = "partitioning",k = 7,fill = "f") == ['partiti', 'oningff']
    assert candidate(s = "example",k = 10,fill = "z") == ['examplezzz']
    assert candidate(s = "abcdefghij",k = 4,fill = "e") == ['abcd', 'efgh', 'ijee']
    assert candidate(s = "programmingisfun",k = 5,fill = "a") == ['progr', 'ammin', 'gisfu', 'naaaa']
    assert candidate(s = "thisisaverylongstringthatwillneedfilling",k = 7,fill = "a") == ['thisisa', 'verylon', 'gstring', 'thatwil', 'lneedfi', 'llingaa']
    assert candidate(s = "onetwothreefourfive",k = 6,fill = "j") == ['onetwo', 'threef', 'ourfiv', 'ejjjjj']
    assert candidate(s = "world",k = 10,fill = "c") == ['worldccccc']
    assert candidate(s = "xyz",k = 10,fill = "a") == ['xyzaaaaaaa']
    assert candidate(s = "hello world",k = 4,fill = "x") == ['hell', 'o wo', 'rldx']
    assert candidate(s = "abcdefgxyz",k = 4,fill = "a") == ['abcd', 'efgx', 'yzaa']
    assert candidate(s = "abcdefghijk",k = 4,fill = "x") == ['abcd', 'efgh', 'ijkx']
    assert candidate(s = "partition",k = 1,fill = "m") == ['p', 'a', 'r', 't', 'i', 't', 'i', 'o', 'n']
    assert candidate(s = "algorithms",k = 7,fill = "b") == ['algorit', 'hmsbbbb']
    assert candidate(s = "repeatedcharacterstest",k = 7,fill = "z") == ['repeate', 'dcharac', 'terstes', 'tzzzzzz']
    assert candidate(s = "almostfull",k = 4,fill = "i") == ['almo', 'stfu', 'llii']
    assert candidate(s = "filler",k = 11,fill = "l") == ['fillerlllll']
    assert candidate(s = "",k = 3,fill = "n") == []
    assert candidate(s = "abcdefghijk",k = 3,fill = "n") == ['abc', 'def', 'ghi', 'jkn']
    assert candidate(s = "elephants",k = 3,fill = "p") == ['ele', 'pha', 'nts']
    assert candidate(s = "short",k = 10,fill = "p") == ['shortppppp']
    assert candidate(s = "abcd",k = 6,fill = "w") == ['abcdww']
    assert candidate(s = "abcdef",k = 2,fill = "x") == ['ab', 'cd', 'ef']
    assert candidate(s = "quickbrownfox",k = 4,fill = "x") == ['quic', 'kbro', 'wnfo', 'xxxx']
    assert candidate(s = "qwert",k = 10,fill = "n") == ['qwertnnnnn']
    assert candidate(s = "machinelearning",k = 8,fill = "d") == ['machinel', 'earningd']
    assert candidate(s = "abcdef",k = 1,fill = "z") == ['a', 'b', 'c', 'd', 'e', 'f']
    assert candidate(s = "short",k = 10,fill = "b") == ['shortbbbbb']
    assert candidate(s = "programming",k = 7,fill = "a") == ['program', 'mingaaa']
    assert candidate(s = "datastructure",k = 5,fill = "a") == ['datas', 'truct', 'ureaa']
    assert candidate(s = "helloWorld",k = 3,fill = "x") == ['hel', 'loW', 'orl', 'dxx']
    assert candidate(s = "abcdefghijkmnopqrstuvwxyz",k = 5,fill = "x") == ['abcde', 'fghij', 'kmnop', 'qrstu', 'vwxyz']
    assert candidate(s = "abcdefghijk",k = 3,fill = "p") == ['abc', 'def', 'ghi', 'jkp']
    assert candidate(s = "divisiblebyk",k = 2,fill = "h") == ['di', 'vi', 'si', 'bl', 'eb', 'yk']
    assert candidate(s = "qwenassistant",k = 7,fill = "a") == ['qwenass', 'istanta']
    assert candidate(s = "cloudcomputing",k = 6,fill = "c") == ['cloudc', 'omputi', 'ngcccc']
    assert candidate(s = "longerstringexample",k = 6,fill = "n") == ['longer', 'string', 'exampl', 'ennnnn']
    assert candidate(s = "abcdefghijklnm",k = 4,fill = "r") == ['abcd', 'efgh', 'ijkl', 'nmrr']
    assert candidate(s = "algorithm",k = 5,fill = "b") == ['algor', 'ithmb']
    assert candidate(s = "quickbrownfox",k = 3,fill = "m") == ['qui', 'ckb', 'row', 'nfo', 'xmm']
    assert candidate(s = "abcd",k = 4,fill = "x") == ['abcd']
    assert candidate(s = "almostfull",k = 8,fill = "o") == ['almostfu', 'lloooooo']


