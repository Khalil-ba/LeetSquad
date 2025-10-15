def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(source = "abcdefgh",target = "acdeeghh",original = ['bcd', 'fgh', 'thh'],changed = ['cde', 'thh', 'ghh'],cost = [1, 3, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgh",target = "acdeeghh",original = ['bcd', 'fgh', 'thh'],changed = ['cde', 'thh', 'ghh'],cost = [1, 3, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcd",target = "acbe",original = ['a', 'b', 'c', 'c', 'e', 'd'],changed = ['b', 'c', 'b', 'e', 'b', 'e'],cost = [2, 5, 5, 1, 2, 20]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcd",target = "acbe",original = ['a', 'b', 'c', 'c', 'e', 'd'],changed = ['b', 'c', 'b', 'e', 'b', 'e'],cost = [2, 5, 5, 1, 2, 20]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgh",target = "addddddd",original = ['bcd', 'defgh'],changed = ['ddd', 'ddddd'],cost = [100, 1578]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgh",target = "addddddd",original = ['bcd', 'defgh'],changed = ['ddd', 'ddddd'],cost = [100, 1578]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mississippi",target = "massissippi",original = ['issi', 'miss'],changed = ['assi', 'mass'],cost = [20, 30]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mississippi",target = "massissippi",original = ['issi', 'miss'],changed = ['assi', 'mass'],cost = [20, 30]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzxyzxyz",target = "zyxzyxzyx",original = ['xyz', 'zyx'],changed = ['zyx', 'xyz'],cost = [500, 500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzxyzxyz",target = "zyxzyxzyx",original = ['xyz', 'zyx'],changed = ['zyx', 'xyz'],cost = [500, 500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdeffedcba",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'fed', 'cba'],changed = ['zyx', 'wvu', 'tsr', 'pon'],cost = [50, 60, 70, 80]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdeffedcba",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'fed', 'cba'],changed = ['zyx', 'wvu', 'tsr', 'pon'],cost = [50, 60, 70, 80]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeeeddccbbaa",original = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz'],changed = ['yx', 'xw', 'wg', 'vf', 'fu', 'et', 'ts', 'sr', 'rq', 'qp', 'po', 'on', 'nm', 'ml', 'lk', 'kj', 'ji', 'ih', 'hg', 'gf', 'fe', 'ed', 'dc', 'cb', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeeeddccbbaa",original = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz'],changed = ['yx', 'xw', 'wg', 'vf', 'fu', 'et', 'ts', 'sr', 'rq', 'qp', 'po', 'on', 'nm', 'ml', 'lk', 'kj', 'ji', 'ih', 'hg', 'gf', 'fe', 'ed', 'dc', 'cb', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'edc', 'ba'],cost = [200, 150, 100, 50, 150, 200, 50, 100, 150]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'edc', 'ba'],cost = [200, 150, 100, 50, 150, 200, 50, 100, 150]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqr",target = "rqpomn",original = ['mnop', 'opqr', 'pqro', 'qrop', 'rpoq', 'poqm'],changed = ['rpoq', 'poqm', 'mnop', 'opqr', 'pqro', 'qrop'],cost = [100, 200, 300, 400, 500, 600]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqr",target = "rqpomn",original = ['mnop', 'opqr', 'pqro', 'qrop', 'rpoq', 'poqm'],changed = ['rpoq', 'poqm', 'mnop', 'opqr', 'pqro', 'qrop'],cost = [100, 200, 300, 400, 500, 600]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgabcdefgabcdefg",target = "zyxwvutzyxwvutzyxwvut",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'ba'],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgabcdefgabcdefg",target = "zyxwvutzyxwvutzyxwvut",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'ba'],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mnopqrst",target = "nopqrstu",original = ['mnop', 'qrst', 'rstu'],changed = ['nopq', 'mnop', 'rstv'],cost = [100, 200, 300]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mnopqrst",target = "nopqrstu",original = ['mnop', 'qrst', 'rstu'],changed = ['nopq', 'mnop', 'rstv'],cost = [100, 200, 300]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abracadabra",target = "abracabadaa",original = ['ra'],changed = ['aa'],cost = [3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abracadabra",target = "abracabadaa",original = ['ra'],changed = ['aa'],cost = [3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabc",target = "defdefdefdef",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [1000, 1000]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabc",target = "defdefdefdef",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [1000, 1000]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaaa', 'bbbbb'],changed = ['bbbbb', 'aaaaa'],cost = [2000, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaaa', 'bbbbb'],changed = ['bbbbb', 'aaaaa'],cost = [2000, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mississippi",target = "mssssssssss",original = ['issi', 'ssis', 'ippi', 'ppi', 'missi', 'ssipp'],changed = ['ssss', 'ssss', 'ppp', 'pp', 'sssss', 'sssss'],cost = [50, 55, 30, 35, 40, 45]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mississippi",target = "mssssssssss",original = ['issi', 'ssis', 'ippi', 'ppi', 'missi', 'ssipp'],changed = ['ssss', 'ssss', 'ppp', 'pp', 'sssss', 'sssss'],cost = [50, 55, 30, 35, 40, 45]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaaa', 'bbbbb'],changed = ['bbbbb', 'aaaaa'],cost = [1000, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaaa', 'bbbbb'],changed = ['bbbbb', 'aaaaa'],cost = [1000, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefabcdefabcdef",target = "ghijklghijklghijkl",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['ghi', 'jkl', 'abc', 'def'],cost = [10, 20, 30, 40]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefabcdefabcdef",target = "ghijklghijklghijkl",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['ghi', 'jkl', 'abc', 'def'],cost = [10, 20, 30, 40]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(source = "qwertyuiopqwertyuiopqwertyuiop",target = "asdfghjklasdfghjklasdfghjkl",original = ['qwerty', 'uiop', 'asdf', 'ghjkl', 'qwertyuiop', 'asdfghjkl'],changed = ['asdfgh', 'jklasdf', 'qwerty', 'uiopqw', 'asdfghjkl', 'qwertyui'],cost = [150, 250, 350, 450, 550, 650]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "qwertyuiopqwertyuiopqwertyuiop",target = "asdfghjklasdfghjklasdfghjkl",original = ['qwerty', 'uiop', 'asdf', 'ghjkl', 'qwertyuiop', 'asdfghjkl'],changed = ['asdfgh', 'jklasdf', 'qwerty', 'uiopqw', 'asdfghjkl', 'qwertyui'],cost = [150, 250, 350, 450, 550, 650]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "ababababab",target = "bababababa",original = ['aba', 'bab'],changed = ['bab', 'aba'],cost = [5, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ababababab",target = "bababababa",original = ['aba', 'bab'],changed = ['bab', 'aba'],cost = [5, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "ababababab",target = "cdcdcdcdcd",original = ['ab', 'ba'],changed = ['cd', 'dc'],cost = [1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ababababab",target = "cdcdcdcdcd",original = ['ab', 'ba'],changed = ['cd', 'dc'],cost = [1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(source = "abababababababababababab",target = "babababababababababababa",original = ['ab', 'ba'],changed = ['ba', 'ab'],cost = [1, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abababababababababababab",target = "babababababababababababa",original = ['ab', 'ba'],changed = ['ba', 'ab'],cost = [1, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgabcdefg",target = "gfedcbagfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['cba', 'fed', 'ihg', 'lkj', 'onm', 'rqp', 'uts', 'xwv', 'zy'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgabcdefg",target = "gfedcbagfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['cba', 'fed', 'ihg', 'lkj', 'onm', 'rqp', 'uts', 'xwv', 'zy'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabcabcabc",target = "defdefdefdefdefdef",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabcabcabc",target = "defdefdefdefdefdef",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fedcba",original = ['abc', 'def', 'fed'],changed = ['def', 'fed', 'abc'],cost = [100, 200, 300]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fedcba",original = ['abc', 'def', 'fed'],changed = ['def', 'fed', 'abc'],cost = [100, 200, 300]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabc",target = "cbacbacbacba",original = ['abc', 'cba'],changed = ['cba', 'abc'],cost = [25, 35]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabc",target = "cbacbacbacba",original = ['abc', 'cba'],changed = ['cba', 'abc'],cost = [25, 35]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaabbbbccccddddeeeeffff",target = "zzzzzzzzzzzzzzzzzzzzzzzzzz",original = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff'],changed = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz'],cost = [100, 200, 300, 400, 500, 600]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaabbbbccccddddeeeeffff",target = "zzzzzzzzzzzzzzzzzzzzzzzzzz",original = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff'],changed = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz'],cost = [100, 200, 300, 400, 500, 600]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(source = "abababab",target = "cdcdcdcd",original = ['ab', 'ba', 'abcd', 'cd', 'dc'],changed = ['cd', 'cd', 'cdcd', 'ab', 'ab'],cost = [10, 20, 30, 40, 50]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abababab",target = "cdcdcdcd",original = ['ab', 'ba', 'abcd', 'cd', 'dc'],changed = ['cd', 'cd', 'cdcd', 'ab', 'ab'],cost = [10, 20, 30, 40, 50]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abcdefghi', 'hgfedcba'],changed = ['jihgfedcba', 'abcdefghij'],cost = [500, 600]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abcdefghi', 'hgfedcba'],changed = ['jihgfedcba', 'abcdefghij'],cost = [500, 600]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijkl",target = "abcklmnopq",original = ['def', 'ghi', 'jkl', 'mnop'],changed = ['ghi', 'jkl', 'mnop', 'nopq'],cost = [10, 15, 20, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijkl",target = "abcklmnopq",original = ['def', 'ghi', 'jkl', 'mnop'],changed = ['ghi', 'jkl', 'mnop', 'nopq'],cost = [10, 15, 20, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abcdefghi', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h'],changed = ['ihgfedcb', 'ihgfedc', 'ihgfed', 'ihgfe', 'ihgf', 'ihg', 'ih', 'i'],cost = [1000, 900, 800, 700, 600, 500, 400, 300]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abcdefghi', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h'],changed = ['ihgfedcb', 'ihgfedc', 'ihgfed', 'ihgfe', 'ihgf', 'ihg', 'ih', 'i'],cost = [1000, 900, 800, 700, 600, 500, 400, 300]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['xyz', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['xyz', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgabcdefg",target = "ghijklmghijklm",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['ghi', 'jkl', 'mno', 'pqr'],cost = [50, 75, 100, 125]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgabcdefg",target = "ghijklmghijklm",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['ghi', 'jkl', 'mno', 'pqr'],cost = [50, 75, 100, 125]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaaaaaaaaaaaaaaaaa",target = "bbbbbbbbbbbbbbbbbbbb",original = ['aaa', 'bbb', 'aab', 'abb'],changed = ['bbb', 'aaa', 'abb', 'aab'],cost = [10, 5, 20, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaaaaaaaaaaaaaaaaa",target = "bbbbbbbbbbbbbbbbbbbb",original = ['aaa', 'bbb', 'aab', 'abb'],changed = ['bbb', 'aaa', 'abb', 'aab'],cost = [10, 5, 20, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mississippi",target = "maddessippi",original = ['issi', 'ippi', 'ippi', 'issi'],changed = ['addi', 'essi', 'ppii', 'ppii'],cost = [100, 200, 50, 300]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mississippi",target = "maddessippi",original = ['issi', 'ippi', 'ippi', 'issi'],changed = ['addi', 'essi', 'ppii', 'ppii'],cost = [100, 200, 50, 300]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "abcdefg",original = ['abc', 'def', 'ghi'],changed = ['bcd', 'efg', 'hij'],cost = [10, 20, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "abcdefg",original = ['abc', 'def', 'ghi'],changed = ['bcd', 'efg', 'hij'],cost = [10, 20, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = "thisisatargetstring",target = "thisisanoriginalstr",original = ['target', 'string', 'atarget', 'original'],changed = ['original', 'str', 'isan', 'target'],cost = [12, 15, 7, 18]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "thisisatargetstring",target = "thisisanoriginalstr",original = ['target', 'string', 'atarget', 'original'],changed = ['original', 'str', 'isan', 'target'],cost = [12, 15, 7, 18]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaaabbbbbbccccccdddddd",target = "ddddddddccccccccbbbbbaaaaa",original = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd'],changed = ['dddddd', 'cccccc', 'bbbbbb', 'aaaaaa'],cost = [1000, 2000, 3000, 4000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaaabbbbbbccccccdddddd",target = "ddddddddccccccccbbbbbaaaaa",original = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd'],changed = ['dddddd', 'cccccc', 'bbbbbb', 'aaaaaa'],cost = [1000, 2000, 3000, 4000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "ababababab",target = "bababababa",original = ['aba', 'bab'],changed = ['bab', 'aba'],cost = [5, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "ababababab",target = "bababababa",original = ['aba', 'bab'],changed = ['bab', 'aba'],cost = [5, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mississippi",target = "missezzzzzzzzzz",original = ['issi', 'ssis', 'ssiss', 'ippi', 'ppi', 'ippii'],changed = ['zzzz', 'pppi', 'issip', 'zzzz', 'ippp', 'zzzzz'],cost = [100, 200, 300, 400, 500, 600]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mississippi",target = "missezzzzzzzzzz",original = ['issi', 'ssis', 'ssiss', 'ippi', 'ppi', 'ippii'],changed = ['zzzz', 'pppi', 'issip', 'zzzz', 'ippp', 'zzzzz'],cost = [100, 200, 300, 400, 500, 600]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdabcdabcd",target = "zzzzzzzzzzzz",original = ['abcd', 'abc', 'bcd', 'cd', 'd', 'ab'],changed = ['zzzz', 'zzz', 'zzz', 'zz', 'z', 'zz'],cost = [100, 110, 120, 130, 140, 150]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdabcdabcd",target = "zzzzzzzzzzzz",original = ['abcd', 'abc', 'bcd', 'cd', 'd', 'ab'],changed = ['zzzz', 'zzz', 'zzz', 'zz', 'z', 'zz'],cost = [100, 110, 120, 130, 140, 150]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(source = "transform",target = "reformant",original = ['trans', 'form', 'ant'],changed = ['reform', 'orm', 'tant'],cost = [150, 250, 350]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "transform",target = "reformant",original = ['trans', 'form', 'ant'],changed = ['reform', 'orm', 'tant'],cost = [150, 250, 350]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbcc",target = "bbaaccaa",original = ['aa', 'bb', 'cc', 'bb', 'aa'],changed = ['bb', 'cc', 'bb', 'aa', 'cc'],cost = [5, 10, 15, 20, 25]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbcc",target = "bbaaccaa",original = ['aa', 'bb', 'cc', 'bb', 'aa'],changed = ['bb', 'cc', 'bb', 'aa', 'cc'],cost = [5, 10, 15, 20, 25]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcde",target = "edcba",original = ['abc', 'cde', 'edc', 'cba'],changed = ['cde', 'edc', 'cba', 'abc'],cost = [10, 20, 30, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcde",target = "edcba",original = ['abc', 'cde', 'edc', 'cba'],changed = ['cde', 'edc', 'cba', 'abc'],cost = [10, 20, 30, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefgabcdefgabcdefg",target = "bcdefgbcdefgbcdefga",original = ['abcdefg'],changed = ['bcdefga'],cost = [500]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefgabcdefgabcdefg",target = "bcdefgbcdefgbcdefga",original = ['abcdefg'],changed = ['bcdefga'],cost = [500]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "complexproblemcomplexproblem",target = "simpleproblemcomplexproblem",original = ['complex', 'problem', 'simple'],changed = ['simple', 'solution', 'complex'],cost = [100, 200, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "complexproblemcomplexproblem",target = "simpleproblemcomplexproblem",original = ['complex', 'problem', 'simple'],changed = ['simple', 'solution', 'complex'],cost = [100, 200, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abababab",target = "babababa",original = ['aba', 'bab', 'aab'],changed = ['bab', 'aba', 'bab'],cost = [2, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abababab",target = "babababa",original = ['aba', 'bab', 'aab'],changed = ['bab', 'aba', 'bab'],cost = [2, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefabcdef",target = "fedcbafedcba",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [50, 60]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefabcdef",target = "fedcbafedcba",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [50, 60]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza'],changed = ['uvw', 'rst', 'opq', 'lmn', 'fed', 'cba', 'zyx', 'wvu', 'tsr'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza'],changed = ['uvw', 'rst', 'opq', 'lmn', 'fed', 'cba', 'zyx', 'wvu', 'tsr'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaabbbbcccc",target = "bbbbaaaaaccc",original = ['aaa', 'bbb', 'ccc'],changed = ['bbb', 'aaa', 'ccc'],cost = [10, 20, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaabbbbcccc",target = "bbbbaaaaaccc",original = ['aaa', 'bbb', 'ccc'],changed = ['bbb', 'aaa', 'ccc'],cost = [10, 20, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "hellohellohello",target = "worldworldworld",original = ['hello', 'world'],changed = ['world', 'hello'],cost = [500, 300]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "hellohellohello",target = "worldworldworld",original = ['hello', 'world'],changed = ['world', 'hello'],cost = [500, 300]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabc",target = "xyzxyzxyzxyz",original = ['abc', 'ab', 'bc'],changed = ['xyz', 'yx', 'zx'],cost = [100, 50, 30]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabc",target = "xyzxyzxyzxyz",original = ['abc', 'ab', 'bc'],changed = ['xyz', 'yx', 'zx'],cost = [100, 50, 30]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['cba', 'fed', 'ihg', 'lkj'],cost = [10, 20, 30, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['cba', 'fed', 'ihg', 'lkj'],cost = [10, 20, 30, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefg",target = "zzzzzzz",original = ['abc', 'def', 'gh', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],changed = ['zzz', 'zzz', 'zzz', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],cost = [100, 100, 100, 1, 2, 3, 4, 5, 6, 7]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefg",target = "zzzzzzz",original = ['abc', 'def', 'gh', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],changed = ['zzz', 'zzz', 'zzz', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],cost = [100, 100, 100, 1, 2, 3, 4, 5, 6, 7]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",original = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],changed = ['ba', 'dc', 'fe', 'hg', 'ji', 'lk', 'no', 'po', 'rq', 'ts', 'vu', 'xw', 'zy'],cost = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333, 4444]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",original = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],changed = ['ba', 'dc', 'fe', 'hg', 'ji', 'lk', 'no', 'po', 'rq', 'ts', 'vu', 'xw', 'zy'],cost = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333, 4444]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaabbbbbcccc",target = "bbbbbcccccddddd",original = ['aaa', 'bbb', 'ccc'],changed = ['bbb', 'ccc', 'ddd'],cost = [1, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaabbbbbcccc",target = "bbbbbcccccddddd",original = ['aaa', 'bbb', 'ccc'],changed = ['bbb', 'ccc', 'ddd'],cost = [1, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "ijabcdefgh",original = ['abcdefgh', 'ijkl'],changed = ['ijkl', 'abcdefgh'],cost = [2000000, 2000000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "ijabcdefgh",original = ['abcdefgh', 'ijkl'],changed = ['ijkl', 'abcdefgh'],cost = [2000000, 2000000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdef",target = "fedcba",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [10, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdef",target = "fedcba",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [10, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abacabadabacaba",target = "xyzxyzxyzxyzxyz",original = ['aba', 'bac', 'cab', 'abc'],changed = ['xyz', 'zyx', 'yxz', 'yzx'],cost = [1000, 2000, 3000, 4000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abacabadabacaba",target = "xyzxyzxyzxyzxyz",original = ['aba', 'bac', 'cab', 'abc'],changed = ['xyz', 'zyx', 'yxz', 'yzx'],cost = [1000, 2000, 3000, 4000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "zzzzzzzzzz",target = "zzzzzzzzzz",original = ['zzz', 'zzzz'],changed = ['zzzz', 'zzz'],cost = [1000, 2000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zzzzzzzzzz",target = "zzzzzzzzzz",original = ['zzz', 'zzzz'],changed = ['zzzz', 'zzz'],cost = [1000, 2000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "zabcdefghi",original = ['a', 'z'],changed = ['z', 'a'],cost = [1000000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "zabcdefghi",original = ['a', 'z'],changed = ['z', 'a'],cost = [1000000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyxyxyxyxy",target = "yxyxyxyxyx",original = ['xy', 'yx'],changed = ['yx', 'xy'],cost = [10, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyxyxyxyxy",target = "yxyxyxyxyx",original = ['xy', 'yx'],changed = ['yx', 'xy'],cost = [10, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "abcdefghij",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['abc', 'def', 'ghi', 'jkl'],cost = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "abcdefghij",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['abc', 'def', 'ghi', 'jkl'],cost = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzxyzxyz",target = "zyxzyxzyx",original = ['xyz', 'zyx'],changed = ['zyx', 'xyz'],cost = [1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzxyzxyz",target = "zyxzyxzyx",original = ['xyz', 'zyx'],changed = ['zyx', 'xyz'],cost = [1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(source = "mississippi",target = "hellohello",original = ['issi', 'issipp', 'ippi', 'issipp', 'issipp'],changed = ['ello', 'ello', 'ello', 'ello', 'ello'],cost = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mississippi",target = "hellohello",original = ['issi', 'issipp', 'ippi', 'issipp', 'issipp'],changed = ['ello', 'ello', 'ello', 'ello', 'ello'],cost = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],changed = ['ff', 'ee', 'dd', 'cc', 'bb', 'aa'],cost = [1, 2, 3, 4, 5, 6]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],changed = ['ff', 'ee', 'dd', 'cc', 'bb', 'aa'],cost = [1, 2, 3, 4, 5, 6]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(source = "zzzzzzzz",target = "yyyyyyyy",original = ['zzz', 'zyz', 'yzy'],changed = ['yyy', 'yyy', 'yyy'],cost = [10, 20, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zzzzzzzz",target = "yyyyyyyy",original = ['zzz', 'zyz', 'yzy'],changed = ['yyy', 'yyy', 'yyy'],cost = [10, 20, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['ab', 'bc', 'cd', 'de', 'ef'],changed = ['fe', 'ed', 'dc', 'cb', 'ba'],cost = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['ab', 'bc', 'cd', 'de', 'ef'],changed = ['fe', 'ed', 'dc', 'cb', 'ba'],cost = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeff",target = "zzzzzzzzzzzz",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'abcdef'],changed = ['zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zzzzzz'],cost = [10, 10, 10, 10, 10, 10, 50]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeff",target = "zzzzzzzzzzzz",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'abcdef'],changed = ['zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zzzzzz'],cost = [10, 10, 10, 10, 10, 10, 50]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(source = "zzzzzzzzzz",target = "abcdefghij",original = ['zzzz', 'zzz', 'zz', 'z'],changed = ['abcd', 'bcde', 'cdef', 'defg'],cost = [1000, 500, 250, 125]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "zzzzzzzzzz",target = "abcdefghij",original = ['zzzz', 'zzz', 'zz', 'z'],changed = ['abcd', 'bcde', 'cdef', 'defg'],cost = [1000, 500, 250, 125]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "thisisaverylongstringthatweneedtoconvert",target = "toreallyconvertthislongstring",original = ['this', 'very', 'long', 'string', 'that', 'need', 'to'],changed = ['to', 'need', 'that', 'convert', 'very', 'long', 'this'],cost = [1, 2, 3, 4, 5, 6, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "thisisaverylongstringthatweneedtoconvert",target = "toreallyconvertthislongstring",original = ['this', 'very', 'long', 'string', 'that', 'need', 'to'],changed = ['to', 'need', 'that', 'convert', 'very', 'long', 'this'],cost = [1, 2, 3, 4, 5, 6, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abc', 'def', 'ghi', 'jih', 'fed', 'cba'],changed = ['jih', 'fed', 'cba', 'abc', 'def', 'ghi'],cost = [100, 200, 300, 400, 500, 600]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abc', 'def', 'ghi', 'jih', 'fed', 'cba'],changed = ['jih', 'fed', 'cba', 'abc', 'def', 'ghi'],cost = [100, 200, 300, 400, 500, 600]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['aab', 'bcc', 'dde', 'eff'],changed = ['ff', 'ee', 'dd', 'cc'],cost = [1, 2, 3, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['aab', 'bcc', 'dde', 'eff'],changed = ['ff', 'ee', 'dd', 'cc'],cost = [1, 2, 3, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaabbbbbcccccdddddeeeee",target = "eeeeeaaaaabbbbcccccd",original = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee'],changed = ['eeeee', 'aaaaa', 'bbbbb', 'ccccc', 'ddddd'],cost = [100, 200, 300, 400, 500]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaabbbbbcccccdddddeeeee",target = "eeeeeaaaaabbbbcccccd",original = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee'],changed = ['eeeee', 'aaaaa', 'bbbbb', 'ccccc', 'ddddd'],cost = [100, 200, 300, 400, 500]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcabcabcabcabcabcabcabcabcabc",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",original = ['abc', 'bc', 'c', 'a', 'b', 'ab', 'bc', 'ca'],changed = ['xyz', 'yz', 'z', 'x', 'y', 'xy', 'yz', 'zx'],cost = [10, 20, 30, 40, 50, 60, 70, 80]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcabcabcabcabcabcabcabcabcabc",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",original = ['abc', 'bc', 'c', 'a', 'b', 'ab', 'bc', 'ca'],changed = ['xyz', 'yz', 'z', 'x', 'y', 'xy', 'yz', 'zx'],cost = [10, 20, 30, 40, 50, 60, 70, 80]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(source = "conversionexampleexample",target = "transformationexampleexample",original = ['conversion', 'transformation'],changed = ['transformation', 'conversion'],cost = [40, 60]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "conversionexampleexample",target = "transformationexampleexample",original = ['conversion', 'transformation'],changed = ['transformation', 'conversion'],cost = [40, 60]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abacabadabacaba",target = "zzzzzzzzzzzzzzz",original = ['aba', 'abc', 'aca', 'bca', 'cab'],changed = ['zzz', 'zzz', 'zzz', 'zzz', 'zzz'],cost = [10, 20, 30, 40, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abacabadabacaba",target = "zzzzzzzzzzzzzzz",original = ['aba', 'abc', 'aca', 'bca', 'cab'],changed = ['zzz', 'zzz', 'zzz', 'zzz', 'zzz'],cost = [10, 20, 30, 40, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abacabadabacabad",target = "xyzxyzxyzxyz",original = ['aba', 'bac', 'cad', 'bad', 'abc', 'acb', 'bcd', 'bca', 'cab', 'cba'],changed = ['xyz', 'zyx', 'yzx', 'xyz', 'zyx', 'yzx', 'xyz', 'zyx', 'yzx', 'xyz'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abacabadabacabad",target = "xyzxyzxyzxyz",original = ['aba', 'bac', 'cad', 'bad', 'abc', 'acb', 'bcd', 'bca', 'cab', 'cba'],changed = ['xyz', 'zyx', 'yzx', 'xyz', 'zyx', 'yzx', 'xyz', 'zyx', 'yzx', 'xyz'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyzxyzxyz",target = "uvwuvwuvw",original = ['xyz', 'yzx', 'zxy', 'xy', 'yz', 'zx', 'x', 'y', 'z'],changed = ['uvw', 'uvw', 'uvw', 'uv', 'uw', 'vw', 'u', 'v', 'w'],cost = [100, 150, 200, 10, 20, 30, 1, 2, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyzxyzxyz",target = "uvwuvwuvw",original = ['xyz', 'yzx', 'zxy', 'xy', 'yz', 'zx', 'x', 'y', 'z'],changed = ['uvw', 'uvw', 'uvw', 'uv', 'uw', 'vw', 'u', 'v', 'w'],cost = [100, 150, 200, 10, 20, 30, 1, 2, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaa', 'bbbb'],changed = ['bbbb', 'aaaa'],cost = [1000, 2000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaa', 'bbbb'],changed = ['bbbb', 'aaaa'],cost = [1000, 2000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aabbccddeeff",target = "aabbccddeeff",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],changed = ['bb', 'cc', 'dd', 'ee', 'ff', 'aa'],cost = [10, 20, 30, 40, 50, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aabbccddeeff",target = "aabbccddeeff",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],changed = ['bb', 'cc', 'dd', 'ee', 'ff', 'aa'],cost = [10, 20, 30, 40, 50, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(source = "abababababababababab",target = "babababababababababa",original = ['ab', 'ba'],changed = ['ba', 'ab'],cost = [3, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abababababababababab",target = "babababababababababa",original = ['ab', 'ba'],changed = ['ba', 'ab'],cost = [3, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(source = "repeatedsubstringsubstring",target = "differentsubstringsubstring",original = ['repeated', 'different'],changed = ['different', 'repeated'],cost = [100, 120]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "repeatedsubstringsubstring",target = "differentsubstringsubstring",original = ['repeated', 'different'],changed = ['different', 'repeated'],cost = [100, 120]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "qwertyuiop",target = "zxcvbnmzxc",original = ['qw', 'er', 'ty', 'ui', 'op', 'zxc', 'cv', 'bn', 'm', 'zx', 'xc'],changed = ['zx', 'xc', 'cv', 'bn', 'm', 'qw', 'er', 'ty', 'ui', 'op', 'zxc'],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "qwertyuiop",target = "zxcvbnmzxc",original = ['qw', 'er', 'ty', 'ui', 'op', 'zxc', 'cv', 'bn', 'm', 'zx', 'xc'],changed = ['zx', 'xc', 'cv', 'bn', 'm', 'qw', 'er', 'ty', 'ui', 'op', 'zxc'],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "mississippi",target = "mississippa",original = ['ippi'],changed = ['appa'],cost = [5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "mississippi",target = "mississippa",original = ['ippi'],changed = ['appa'],cost = [5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'ed', 'cb'],cost = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'ed', 'cb'],cost = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "aaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaa",target = "zzzzzxxxxxzzzzzxxxxxzzzzzxxxxxzzzzz",original = ['aaaaa', 'bbbbb', 'xxxxx', 'zzzzz'],changed = ['zzzzz', 'aaaaa', 'zzzzz', 'xxxxx'],cost = [100, 200, 300, 400]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "aaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaa",target = "zzzzzxxxxxzzzzzxxxxxzzzzzxxxxxzzzzz",original = ['aaaaa', 'bbbbb', 'xxxxx', 'zzzzz'],changed = ['zzzzz', 'aaaaa', 'zzzzz', 'xxxxx'],cost = [100, 200, 300, 400]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(source = "xyxyxyxyxyxyxyxyxy",target = "yxyxyxyxyxyxyxyxyx",original = ['xy', 'yx'],changed = ['yx', 'xy'],cost = [1, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "xyxyxyxyxyxyxyxyxy",target = "yxyxyxyxyxyxyxyxyx",original = ['xy', 'yx'],changed = ['yx', 'xy'],cost = [1, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'abc'],cost = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'abc'],cost = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "nestednestednested",target = "deepdeepdeep",original = ['nested', 'deep'],changed = ['deep', 'nested'],cost = [50, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "nestednestednested",target = "deepdeepdeep",original = ['nested', 'deep'],changed = ['deep', 'nested'],cost = [50, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(source = "thisisatest",target = "tistiatest",original = ['this', 'test'],changed = ['tist', 'taste'],cost = [50, 70]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(source = "thisisatest",target = "tistiatest",original = ['this', 'test'],changed = ['tist', 'taste'],cost = [50, 70]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(source = "abcdefgh",target = "acdeeghh",original = ['bcd', 'fgh', 'thh'],changed = ['cde', 'thh', 'ghh'],cost = [1, 3, 5]) == 9
    assert candidate(source = "abcd",target = "acbe",original = ['a', 'b', 'c', 'c', 'e', 'd'],changed = ['b', 'c', 'b', 'e', 'b', 'e'],cost = [2, 5, 5, 1, 2, 20]) == 28
    assert candidate(source = "abcdefgh",target = "addddddd",original = ['bcd', 'defgh'],changed = ['ddd', 'ddddd'],cost = [100, 1578]) == -1
    assert candidate(source = "mississippi",target = "massissippi",original = ['issi', 'miss'],changed = ['assi', 'mass'],cost = [20, 30]) == 20
    assert candidate(source = "xyzxyzxyz",target = "zyxzyxzyx",original = ['xyz', 'zyx'],changed = ['zyx', 'xyz'],cost = [500, 500]) == 1500
    assert candidate(source = "abcdeffedcba",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'fed', 'cba'],changed = ['zyx', 'wvu', 'tsr', 'pon'],cost = [50, 60, 70, 80]) == -1
    assert candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeeeddccbbaa",original = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz'],changed = ['yx', 'xw', 'wg', 'vf', 'fu', 'et', 'ts', 'sr', 'rq', 'qp', 'po', 'on', 'nm', 'ml', 'lk', 'kj', 'ji', 'ih', 'hg', 'gf', 'fe', 'ed', 'dc', 'cb', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == -1
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'edc', 'ba'],cost = [200, 150, 100, 50, 150, 200, 50, 100, 150]) == -1
    assert candidate(source = "mnopqr",target = "rqpomn",original = ['mnop', 'opqr', 'pqro', 'qrop', 'rpoq', 'poqm'],changed = ['rpoq', 'poqm', 'mnop', 'opqr', 'pqro', 'qrop'],cost = [100, 200, 300, 400, 500, 600]) == -1
    assert candidate(source = "abcdefgabcdefgabcdefg",target = "zyxwvutzyxwvutzyxwvut",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'ba'],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(source = "mnopqrst",target = "nopqrstu",original = ['mnop', 'qrst', 'rstu'],changed = ['nopq', 'mnop', 'rstv'],cost = [100, 200, 300]) == -1
    assert candidate(source = "abracadabra",target = "abracabadaa",original = ['ra'],changed = ['aa'],cost = [3]) == -1
    assert candidate(source = "abcabcabcabc",target = "defdefdefdef",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [1000, 1000]) == 4000
    assert candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaaa', 'bbbbb'],changed = ['bbbbb', 'aaaaa'],cost = [2000, 1000]) == -1
    assert candidate(source = "mississippi",target = "mssssssssss",original = ['issi', 'ssis', 'ippi', 'ppi', 'missi', 'ssipp'],changed = ['ssss', 'ssss', 'ppp', 'pp', 'sssss', 'sssss'],cost = [50, 55, 30, 35, 40, 45]) == -1
    assert candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaaa', 'bbbbb'],changed = ['bbbbb', 'aaaaa'],cost = [1000, 1000]) == -1
    assert candidate(source = "abcdefabcdefabcdef",target = "ghijklghijklghijkl",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['ghi', 'jkl', 'abc', 'def'],cost = [10, 20, 30, 40]) == 90
    assert candidate(source = "qwertyuiopqwertyuiopqwertyuiop",target = "asdfghjklasdfghjklasdfghjkl",original = ['qwerty', 'uiop', 'asdf', 'ghjkl', 'qwertyuiop', 'asdfghjkl'],changed = ['asdfgh', 'jklasdf', 'qwerty', 'uiopqw', 'asdfghjkl', 'qwertyui'],cost = [150, 250, 350, 450, 550, 650]) == -1
    assert candidate(source = "ababababab",target = "bababababa",original = ['aba', 'bab'],changed = ['bab', 'aba'],cost = [5, 10]) == -1
    assert candidate(source = "ababababab",target = "cdcdcdcdcd",original = ['ab', 'ba'],changed = ['cd', 'dc'],cost = [1, 2]) == 5
    assert candidate(source = "abababababababababababab",target = "babababababababababababa",original = ['ab', 'ba'],changed = ['ba', 'ab'],cost = [1, 2]) == 12
    assert candidate(source = "abcdefgabcdefg",target = "gfedcbagfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['cba', 'fed', 'ihg', 'lkj', 'onm', 'rqp', 'uts', 'xwv', 'zy'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
    assert candidate(source = "abcabcabcabcabcabc",target = "defdefdefdefdefdef",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [1, 2]) == 6
    assert candidate(source = "abcdef",target = "fedcba",original = ['abc', 'def', 'fed'],changed = ['def', 'fed', 'abc'],cost = [100, 200, 300]) == -1
    assert candidate(source = "abcabcabcabc",target = "cbacbacbacba",original = ['abc', 'cba'],changed = ['cba', 'abc'],cost = [25, 35]) == 100
    assert candidate(source = "aaaabbbbccccddddeeeeffff",target = "zzzzzzzzzzzzzzzzzzzzzzzzzz",original = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff'],changed = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz'],cost = [100, 200, 300, 400, 500, 600]) == 2100
    assert candidate(source = "abababab",target = "cdcdcdcd",original = ['ab', 'ba', 'abcd', 'cd', 'dc'],changed = ['cd', 'cd', 'cdcd', 'ab', 'ab'],cost = [10, 20, 30, 40, 50]) == 40
    assert candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abcdefghi', 'hgfedcba'],changed = ['jihgfedcba', 'abcdefghij'],cost = [500, 600]) == -1
    assert candidate(source = "abcdefghijkl",target = "abcklmnopq",original = ['def', 'ghi', 'jkl', 'mnop'],changed = ['ghi', 'jkl', 'mnop', 'nopq'],cost = [10, 15, 20, 25]) == -1
    assert candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abcdefghi', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h'],changed = ['ihgfedcb', 'ihgfedc', 'ihgfed', 'ihgfe', 'ihgf', 'ihg', 'ih', 'i'],cost = [1000, 900, 800, 700, 600, 500, 400, 300]) == -1
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['xyz', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
    assert candidate(source = "abcdefgabcdefg",target = "ghijklmghijklm",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['ghi', 'jkl', 'mno', 'pqr'],cost = [50, 75, 100, 125]) == -1
    assert candidate(source = "aaaaaaaaaaaaaaaaaaaa",target = "bbbbbbbbbbbbbbbbbbbb",original = ['aaa', 'bbb', 'aab', 'abb'],changed = ['bbb', 'aaa', 'abb', 'aab'],cost = [10, 5, 20, 15]) == -1
    assert candidate(source = "mississippi",target = "maddessippi",original = ['issi', 'ippi', 'ippi', 'issi'],changed = ['addi', 'essi', 'ppii', 'ppii'],cost = [100, 200, 50, 300]) == -1
    assert candidate(source = "abcdefg",target = "abcdefg",original = ['abc', 'def', 'ghi'],changed = ['bcd', 'efg', 'hij'],cost = [10, 20, 30]) == 0
    assert candidate(source = "thisisatargetstring",target = "thisisanoriginalstr",original = ['target', 'string', 'atarget', 'original'],changed = ['original', 'str', 'isan', 'target'],cost = [12, 15, 7, 18]) == -1
    assert candidate(source = "aaaaaabbbbbbccccccdddddd",target = "ddddddddccccccccbbbbbaaaaa",original = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd'],changed = ['dddddd', 'cccccc', 'bbbbbb', 'aaaaaa'],cost = [1000, 2000, 3000, 4000]) == -1
    assert candidate(source = "ababababab",target = "bababababa",original = ['aba', 'bab'],changed = ['bab', 'aba'],cost = [5, 7]) == -1
    assert candidate(source = "mississippi",target = "missezzzzzzzzzz",original = ['issi', 'ssis', 'ssiss', 'ippi', 'ppi', 'ippii'],changed = ['zzzz', 'pppi', 'issip', 'zzzz', 'ippp', 'zzzzz'],cost = [100, 200, 300, 400, 500, 600]) == -1
    assert candidate(source = "abcdabcdabcd",target = "zzzzzzzzzzzz",original = ['abcd', 'abc', 'bcd', 'cd', 'd', 'ab'],changed = ['zzzz', 'zzz', 'zzz', 'zz', 'z', 'zz'],cost = [100, 110, 120, 130, 140, 150]) == 300
    assert candidate(source = "transform",target = "reformant",original = ['trans', 'form', 'ant'],changed = ['reform', 'orm', 'tant'],cost = [150, 250, 350]) == -1
    assert candidate(source = "aabbcc",target = "bbaaccaa",original = ['aa', 'bb', 'cc', 'bb', 'aa'],changed = ['bb', 'cc', 'bb', 'aa', 'cc'],cost = [5, 10, 15, 20, 25]) == 25
    assert candidate(source = "abcde",target = "edcba",original = ['abc', 'cde', 'edc', 'cba'],changed = ['cde', 'edc', 'cba', 'abc'],cost = [10, 20, 30, 40]) == -1
    assert candidate(source = "abcdefgabcdefgabcdefg",target = "bcdefgbcdefgbcdefga",original = ['abcdefg'],changed = ['bcdefga'],cost = [500]) == -1
    assert candidate(source = "complexproblemcomplexproblem",target = "simpleproblemcomplexproblem",original = ['complex', 'problem', 'simple'],changed = ['simple', 'solution', 'complex'],cost = [100, 200, 50]) == -1
    assert candidate(source = "abababab",target = "babababa",original = ['aba', 'bab', 'aab'],changed = ['bab', 'aba', 'bab'],cost = [2, 3, 1]) == -1
    assert candidate(source = "abcdefabcdef",target = "fedcbafedcba",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [50, 60]) == -1
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza'],changed = ['uvw', 'rst', 'opq', 'lmn', 'fed', 'cba', 'zyx', 'wvu', 'tsr'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
    assert candidate(source = "aaaabbbbcccc",target = "bbbbaaaaaccc",original = ['aaa', 'bbb', 'ccc'],changed = ['bbb', 'aaa', 'ccc'],cost = [10, 20, 30]) == -1
    assert candidate(source = "hellohellohello",target = "worldworldworld",original = ['hello', 'world'],changed = ['world', 'hello'],cost = [500, 300]) == 1500
    assert candidate(source = "abcabcabcabc",target = "xyzxyzxyzxyz",original = ['abc', 'ab', 'bc'],changed = ['xyz', 'yx', 'zx'],cost = [100, 50, 30]) == 400
    assert candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['cba', 'fed', 'ihg', 'lkj'],cost = [10, 20, 30, 40]) == -1
    assert candidate(source = "abcdefg",target = "zzzzzzz",original = ['abc', 'def', 'gh', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],changed = ['zzz', 'zzz', 'zzz', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],cost = [100, 100, 100, 1, 2, 3, 4, 5, 6, 7]) == 28
    assert candidate(source = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",target = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",original = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],changed = ['ba', 'dc', 'fe', 'hg', 'ji', 'lk', 'no', 'po', 'rq', 'ts', 'vu', 'xw', 'zy'],cost = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333, 4444]) == -1
    assert candidate(source = "aaaaabbbbbcccc",target = "bbbbbcccccddddd",original = ['aaa', 'bbb', 'ccc'],changed = ['bbb', 'ccc', 'ddd'],cost = [1, 2, 3]) == -1
    assert candidate(source = "abcdefghij",target = "ijabcdefgh",original = ['abcdefgh', 'ijkl'],changed = ['ijkl', 'abcdefgh'],cost = [2000000, 2000000]) == -1
    assert candidate(source = "abcdef",target = "fedcba",original = ['abc', 'def'],changed = ['def', 'abc'],cost = [10, 20]) == -1
    assert candidate(source = "abacabadabacaba",target = "xyzxyzxyzxyzxyz",original = ['aba', 'bac', 'cab', 'abc'],changed = ['xyz', 'zyx', 'yxz', 'yzx'],cost = [1000, 2000, 3000, 4000]) == -1
    assert candidate(source = "zzzzzzzzzz",target = "zzzzzzzzzz",original = ['zzz', 'zzzz'],changed = ['zzzz', 'zzz'],cost = [1000, 2000]) == 0
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'ba'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
    assert candidate(source = "abcdefghij",target = "zabcdefghi",original = ['a', 'z'],changed = ['z', 'a'],cost = [1000000]) == -1
    assert candidate(source = "xyxyxyxyxy",target = "yxyxyxyxyx",original = ['xy', 'yx'],changed = ['yx', 'xy'],cost = [10, 5]) == 50
    assert candidate(source = "abcdefghij",target = "abcdefghij",original = ['abc', 'def', 'ghi', 'jkl'],changed = ['abc', 'def', 'ghi', 'jkl'],cost = [1, 1, 1, 1]) == 0
    assert candidate(source = "xyzxyzxyz",target = "zyxzyxzyx",original = ['xyz', 'zyx'],changed = ['zyx', 'xyz'],cost = [1, 2]) == 3
    assert candidate(source = "mississippi",target = "hellohello",original = ['issi', 'issipp', 'ippi', 'issipp', 'issipp'],changed = ['ello', 'ello', 'ello', 'ello', 'ello'],cost = [1, 2, 3, 4, 5]) == -1
    assert candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],changed = ['ff', 'ee', 'dd', 'cc', 'bb', 'aa'],cost = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(source = "zzzzzzzz",target = "yyyyyyyy",original = ['zzz', 'zyz', 'yzy'],changed = ['yyy', 'yyy', 'yyy'],cost = [10, 20, 5]) == -1
    assert candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['ab', 'bc', 'cd', 'de', 'ef'],changed = ['fe', 'ed', 'dc', 'cb', 'ba'],cost = [1, 2, 3, 4, 5]) == -1
    assert candidate(source = "aabbccddeeff",target = "zzzzzzzzzzzz",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'abcdef'],changed = ['zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zzzzzz'],cost = [10, 10, 10, 10, 10, 10, 50]) == 60
    assert candidate(source = "zzzzzzzzzz",target = "abcdefghij",original = ['zzzz', 'zzz', 'zz', 'z'],changed = ['abcd', 'bcde', 'cdef', 'defg'],cost = [1000, 500, 250, 125]) == -1
    assert candidate(source = "thisisaverylongstringthatweneedtoconvert",target = "toreallyconvertthislongstring",original = ['this', 'very', 'long', 'string', 'that', 'need', 'to'],changed = ['to', 'need', 'that', 'convert', 'very', 'long', 'this'],cost = [1, 2, 3, 4, 5, 6, 7]) == -1
    assert candidate(source = "abcdefghij",target = "jihgfedcba",original = ['abc', 'def', 'ghi', 'jih', 'fed', 'cba'],changed = ['jih', 'fed', 'cba', 'abc', 'def', 'ghi'],cost = [100, 200, 300, 400, 500, 600]) == -1
    assert candidate(source = "aabbccddeeff",target = "ffeeddccbbaa",original = ['aab', 'bcc', 'dde', 'eff'],changed = ['ff', 'ee', 'dd', 'cc'],cost = [1, 2, 3, 4]) == -1
    assert candidate(source = "aaaaabbbbbcccccdddddeeeee",target = "eeeeeaaaaabbbbcccccd",original = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee'],changed = ['eeeee', 'aaaaa', 'bbbbb', 'ccccc', 'ddddd'],cost = [100, 200, 300, 400, 500]) == -1
    assert candidate(source = "abcabcabcabcabcabcabcabcabcabc",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",original = ['abc', 'bc', 'c', 'a', 'b', 'ab', 'bc', 'ca'],changed = ['xyz', 'yz', 'z', 'x', 'y', 'xy', 'yz', 'zx'],cost = [10, 20, 30, 40, 50, 60, 70, 80]) == 100
    assert candidate(source = "conversionexampleexample",target = "transformationexampleexample",original = ['conversion', 'transformation'],changed = ['transformation', 'conversion'],cost = [40, 60]) == -1
    assert candidate(source = "abacabadabacaba",target = "zzzzzzzzzzzzzzz",original = ['aba', 'abc', 'aca', 'bca', 'cab'],changed = ['zzz', 'zzz', 'zzz', 'zzz', 'zzz'],cost = [10, 20, 30, 40, 50]) == -1
    assert candidate(source = "abacabadabacabad",target = "xyzxyzxyzxyz",original = ['aba', 'bac', 'cad', 'bad', 'abc', 'acb', 'bcd', 'bca', 'cab', 'cba'],changed = ['xyz', 'zyx', 'yzx', 'xyz', 'zyx', 'yzx', 'xyz', 'zyx', 'yzx', 'xyz'],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(source = "xyzxyzxyz",target = "uvwuvwuvw",original = ['xyz', 'yzx', 'zxy', 'xy', 'yz', 'zx', 'x', 'y', 'z'],changed = ['uvw', 'uvw', 'uvw', 'uv', 'uw', 'vw', 'u', 'v', 'w'],cost = [100, 150, 200, 10, 20, 30, 1, 2, 3]) == 18
    assert candidate(source = "aaaaabbbbb",target = "bbbbbbaaaa",original = ['aaaa', 'bbbb'],changed = ['bbbb', 'aaaa'],cost = [1000, 2000]) == -1
    assert candidate(source = "aabbccddeeff",target = "aabbccddeeff",original = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],changed = ['bb', 'cc', 'dd', 'ee', 'ff', 'aa'],cost = [10, 20, 30, 40, 50, 60]) == 0
    assert candidate(source = "abababababababababab",target = "babababababababababa",original = ['ab', 'ba'],changed = ['ba', 'ab'],cost = [3, 2]) == 30
    assert candidate(source = "repeatedsubstringsubstring",target = "differentsubstringsubstring",original = ['repeated', 'different'],changed = ['different', 'repeated'],cost = [100, 120]) == -1
    assert candidate(source = "qwertyuiop",target = "zxcvbnmzxc",original = ['qw', 'er', 'ty', 'ui', 'op', 'zxc', 'cv', 'bn', 'm', 'zx', 'xc'],changed = ['zx', 'xc', 'cv', 'bn', 'm', 'qw', 'er', 'ty', 'ui', 'op', 'zxc'],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == -1
    assert candidate(source = "mississippi",target = "mississippa",original = ['ippi'],changed = ['appa'],cost = [5]) == -1
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'ed', 'cb'],cost = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1
    assert candidate(source = "aaaaabbbbbaaaaabbbbbaaaaabbbbbaaaaa",target = "zzzzzxxxxxzzzzzxxxxxzzzzzxxxxxzzzzz",original = ['aaaaa', 'bbbbb', 'xxxxx', 'zzzzz'],changed = ['zzzzz', 'aaaaa', 'zzzzz', 'xxxxx'],cost = [100, 200, 300, 400]) == 2500
    assert candidate(source = "xyxyxyxyxyxyxyxyxy",target = "yxyxyxyxyxyxyxyxyx",original = ['xy', 'yx'],changed = ['yx', 'xy'],cost = [1, 2]) == 9
    assert candidate(source = "abcdefghijklmnopqrstuvwxyz",target = "zyxwvutsrqponmlkjihgfedcba",original = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],changed = ['zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'fed', 'cba', 'abc'],cost = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1
    assert candidate(source = "nestednestednested",target = "deepdeepdeep",original = ['nested', 'deep'],changed = ['deep', 'nested'],cost = [50, 30]) == -1
    assert candidate(source = "thisisatest",target = "tistiatest",original = ['this', 'test'],changed = ['tist', 'taste'],cost = [50, 70]) == -1


