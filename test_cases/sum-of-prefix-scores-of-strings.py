def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h']) == [12, 11, 7, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h']) == [12, 11, 7, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'ab', 'bc', 'b']) == [5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'ab', 'bc', 'b']) == [5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd']) == [1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd']) == [1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aaa', 'aaaa', 'aaaaa']) == [8, 11, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aaa', 'aaaa', 'aaaaa']) == [8, 11, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd']) == [4, 7, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd']) == [4, 7, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'abcd', 'abc', 'ab', 'a']) == [15, 14, 12, 9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'abcd', 'abc', 'ab', 'a']) == [15, 14, 12, 9, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['b', 'bb', 'bbb', 'bbbb']) == [4, 7, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['b', 'bb', 'bbb', 'bbbb']) == [4, 7, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'x']) == [6, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'x']) == [6, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd']) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd']) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'x', 'xyzabc']) == [9, 7, 4, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'x', 'xyzabc']) == [9, 7, 4, 12]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']) == [4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']) == [4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aa', 'a']) == [7, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aa', 'a']) == [7, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dynamic', 'dyn', 'dynam', 'dynamicp', 'dynamicpr', 'dynamicpro', 'dynamicprogra', 'dynamicprogram', 'dynamicprogramming']) == [57, 27, 43, 63, 68, 72, 81, 83, 87]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dynamic', 'dyn', 'dynam', 'dynamicp', 'dynamicpr', 'dynamicpro', 'dynamicprogra', 'dynamicprogram', 'dynamicprogramming']) == [57, 27, 43, 63, 68, 72, 81, 83, 87]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'optimize', 'opt', 'opti', 'optim', 'optimi']) == [37, 33, 18, 23, 27, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'optimize', 'opt', 'opti', 'optim', 'optimi']) == [37, 33, 18, 23, 27, 30]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylo', 'xylophon', 'xy', 'xyl', 'xylophonist', 'xylophoneplayer', 'xylophoneplayerperformance']) == [52, 29, 49, 16, 23, 52, 64, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylo', 'xylophon', 'xy', 'xyl', 'xylophonist', 'xylophoneplayer', 'xylophoneplayerperformance']) == [52, 29, 49, 16, 23, 52, 64, 75]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylography', 'xylo', 'xylophoneography', 'xyl', 'xylonate']) == [33, 29, 23, 40, 18, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylography', 'xylo', 'xylophoneography', 'xyl', 'xylonate']) == [33, 29, 23, 40, 18, 27]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aa', 'a', 'aabbbccc', 'aabbbbcccc', 'aabbbbccccd']) == [30, 29, 27, 15, 8, 33, 40, 41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aa', 'a', 'aabbbccc', 'aabbbbcccc', 'aabbbbccccd']) == [30, 29, 27, 15, 8, 33, 40, 41]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aaac', 'aabb', 'aabc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accc']) == [31, 31, 31, 30, 30, 35, 35, 35, 35, 35, 35, 35, 35, 35, 34, 34, 34, 34, 34, 34, 33, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aaac', 'aabb', 'aabc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accc']) == [31, 31, 31, 30, 30, 35, 35, 35, 35, 35, 35, 35, 35, 35, 34, 34, 34, 34, 34, 34, 33, 33]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacax', 'abaca', 'bacax', 'abac', 'ab']) == [17, 16, 5, 14, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacax', 'abaca', 'bacax', 'abac', 'ab']) == [17, 16, 5, 14, 8]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'application', 'applesauce', 'appetizer']) == [20, 15, 25, 25, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'application', 'applesauce', 'appetizer']) == [20, 15, 25, 25, 21]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumo', 'pneumonoultra', 'pneumonoultramicro', 'pneumonoultramicroscopicsilico', 'pneumonoultramicroscopicsilicovolcano', 'pneumo']) == [155, 42, 77, 97, 133, 147, 42]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumo', 'pneumonoultra', 'pneumonoultramicro', 'pneumonoultramicroscopicsilico', 'pneumonoultramicroscopicsilicovolcano', 'pneumo']) == [155, 42, 77, 97, 133, 147, 42]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro', 'prog', 'progr']) == [30, 26, 15, 19, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro', 'prog', 'progr']) == [30, 26, 15, 19, 22]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'al', 'alex', 'ale', 'all']) == [21, 16, 12, 15, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'al', 'alex', 'ale', 'all']) == [21, 16, 12, 15, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcd', 'abcabc', 'ababab', 'aaaaaa', 'bbbbbb', 'cccccc', 'dddddd']) == [14, 12, 11, 9, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcd', 'abcabc', 'ababab', 'aaaaaa', 'bbbbbb', 'cccccc', 'dddddd']) == [14, 12, 11, 9, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'alg', 'algor', 'algorith', 'algori']) == [35, 23, 18, 27, 34, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'alg', 'algor', 'algorith', 'algori']) == [35, 23, 18, 27, 34, 30]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa', 'a', 'aabbbcc', 'aabbb', 'aabbbb']) == [33, 32, 30, 24, 17, 9, 35, 33, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa', 'a', 'aabbbcc', 'aabbb', 'aabbbb']) == [33, 32, 30, 24, 17, 9, 35, 33, 34]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa']) == [9, 17, 24, 30, 35, 39, 42, 44, 45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa']) == [9, 17, 24, 30, 35, 39, 42, 44, 45]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'prefer', 'preference', 'presentation', 'president', 'presidency']) == [26, 21, 28, 32, 32, 33, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'prefer', 'preference', 'presentation', 'president', 'presidency']) == [26, 21, 28, 32, 32, 33, 34]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h', 'hero', 'helium', 'helper']) == [20, 19, 13, 7, 15, 20, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h', 'hero', 'helium', 'helper']) == [20, 19, 13, 7, 15, 20, 20]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'un', 'uni', 'unic', 'uniqu', 'uniquee', 'uniqueee', 'uniqueeee']) == [37, 16, 23, 24, 33, 40, 42, 43]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'un', 'uni', 'unic', 'uniqu', 'uniquee', 'uniqueee', 'uniqueeee']) == [37, 16, 23, 24, 33, 40, 42, 43]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefin', 'prefixation', 'prefixes', 'prefixing', 'prefixes', 'preference', 'prefer']) == [55, 33, 43, 50, 51, 60, 59, 58, 59, 51, 47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefin', 'prefixation', 'prefixes', 'prefixing', 'prefixes', 'preference', 'prefer']) == [55, 33, 43, 50, 51, 60, 59, 58, 59, 51, 47]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'ap', 'application', 'appetite']) == [17, 14, 10, 23, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'ap', 'application', 'appetite']) == [17, 14, 10, 23, 19]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'aab', 'abc', 'aac', 'acc', 'aaa', 'bbb', 'ccc', 'aabbc', 'aabbbc', 'aabbbcc', 'aabbbccc']) == [32, 24, 12, 19, 12, 19, 3, 3, 31, 35, 37, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'aab', 'abc', 'aac', 'acc', 'aaa', 'bbb', 'ccc', 'aabbc', 'aabbbc', 'aabbbcc', 'aabbbccc']) == [32, 24, 12, 19, 12, 19, 3, 3, 31, 35, 37, 38]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'com', 'compl', 'complexity', 'composite']) == [26, 15, 22, 29, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'com', 'compl', 'complexity', 'composite']) == [26, 15, 22, 29, 24]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'cater', 'caterpillar', 'catering', 'caterer', 'caterers', 'catered', 'catering']) == [24, 38, 44, 44, 43, 44, 42, 44]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'cater', 'caterpillar', 'catering', 'caterer', 'caterers', 'catered', 'catering']) == [24, 38, 44, 44, 43, 44, 42, 44]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'opt', 'opti', 'optim', 'optimiz', 'optimise', 'optimized']) == [44, 21, 27, 32, 39, 38, 41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'opt', 'opti', 'optim', 'optimiz', 'optimise', 'optimized']) == [44, 21, 27, 32, 39, 38, 41]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['data', 'dat', 'database', 'datascience', 'datastructure']) == [19, 15, 23, 27, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['data', 'dat', 'database', 'datascience', 'datastructure']) == [19, 15, 23, 27, 29]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['car', 'cat', 'catch', 'cart', 'card', 'carpet']) == [16, 14, 16, 17, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['car', 'cat', 'catch', 'cart', 'card', 'carpet']) == [16, 14, 16, 17, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'band', 'ball', 'bat', 'basketball']) == [15, 13, 12, 11, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'band', 'ball', 'bat', 'basketball']) == [15, 13, 12, 11, 18]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro', 'pr', 'p', 'prefix', 'pre', 'preprocessing']) == [30, 26, 18, 15, 8, 21, 18, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro', 'pr', 'p', 'prefix', 'pre', 'preprocessing']) == [30, 26, 18, 15, 8, 21, 18, 28]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longword', 'longworder', 'longworderer', 'longwordererest', 'longwordereresterest']) == [40, 48, 54, 60, 65]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longword', 'longworder', 'longworderer', 'longwordererest', 'longwordereresterest']) == [40, 48, 54, 60, 65]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'al', 'alex', 'algorithmic', 'algorithms']) == [35, 20, 12, 14, 37, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'al', 'alex', 'algorithmic', 'algorithms']) == [35, 20, 12, 14, 37, 36]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']) == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']) == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['backtracking', 'back', 'backt', 'backtr', 'backtra', 'backtrac', 'backtrack', 'backtracki', 'backtrackin', 'backtrackin', 'backtrackinga', 'backtrackingal', 'backtrackingalg', 'backtrackingalgo']) == [131, 56, 69, 81, 92, 102, 111, 119, 126, 126, 135, 138, 140, 141]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['backtracking', 'back', 'backt', 'backtr', 'backtra', 'backtrac', 'backtrack', 'backtracki', 'backtrackin', 'backtrackin', 'backtrackinga', 'backtrackingal', 'backtrackingalg', 'backtrackingalgo']) == [131, 56, 69, 81, 92, 102, 111, 119, 126, 126, 135, 138, 140, 141]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pres', 'presum', 'pressure']) == [18, 15, 18, 20, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pres', 'presum', 'pressure']) == [18, 15, 18, 20, 22]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interview', 'inter', 'inte', 'interw', 'interv', 'intervi', 'interviewe']) == [45, 34, 28, 35, 38, 41, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interview', 'inter', 'inte', 'interw', 'interv', 'intervi', 'interviewe']) == [45, 34, 28, 35, 38, 41, 46]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zoo', 'zookeeper', 'zoozoo', 'ze', 'zee', 'z']) == [13, 13, 19, 16, 10, 11, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zoo', 'zookeeper', 'zoozoo', 'ze', 'zee', 'z']) == [13, 13, 19, 16, 10, 11, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeated', 'repeat', 'rep', 're', 'r', 'peated', 'eat', 'e', 't', 'ted', 'tedious', 'tediousness']) == [20, 18, 12, 9, 5, 6, 4, 2, 4, 10, 18, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeated', 'repeat', 'rep', 're', 'r', 'peated', 'eat', 'e', 't', 'ted', 'tedious', 'tediousness']) == [20, 18, 12, 9, 5, 6, 4, 2, 4, 10, 18, 22]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ban', 'bananas', 'band', 'bandana', 'bandwidth']) == [24, 18, 25, 21, 24, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ban', 'bananas', 'band', 'bandana', 'bandwidth']) == [24, 18, 25, 21, 24, 26]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeated', 'repeats', 'repeat', 'repeating', 'repeatedly', 'repeatability']) == [40, 37, 36, 39, 42, 43]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeated', 'repeats', 'repeat', 'repeating', 'repeatedly', 'repeatability']) == [40, 37, 36, 39, 42, 43]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'al', 'algo', 'all', 'algorithms', 'application', 'app']) == [28, 12, 18, 13, 29, 19, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'al', 'algo', 'all', 'algorithms', 'application', 'app']) == [28, 12, 18, 13, 29, 19, 11]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['flower', 'flow', 'flight', 'flour', 'flourish', 'flourishingly']) == [21, 19, 16, 23, 29, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['flower', 'flow', 'flight', 'flour', 'flourish', 'flourishingly']) == [21, 19, 16, 23, 29, 34]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandanna', 'banda']) == [21, 18, 22, 28, 29, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandanna', 'banda']) == [21, 18, 22, 28, 29, 25]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h', 'helicopter', 'helium', 'help', 'hero', 'her', 'hemoglobin']) == [27, 26, 19, 10, 32, 28, 25, 22, 21, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h', 'helicopter', 'helium', 'help', 'hero', 'her', 'hemoglobin']) == [27, 26, 19, 10, 32, 28, 25, 22, 21, 27]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniques', 'unicorn', 'unicycle', 'universality']) == [21, 22, 20, 21, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniques', 'unicorn', 'unicycle', 'universality']) == [21, 22, 20, 21, 24]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'optimizer', 'optimize', 'optimal', 'optimism', 'optimist', 'optimistic', 'optimum', 'opt', 'optional']) == [61, 59, 58, 49, 57, 58, 60, 49, 30, 43]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'optimizer', 'optimize', 'optimal', 'optimism', 'optimist', 'optimistic', 'optimum', 'opt', 'optional']) == [61, 59, 58, 49, 57, 58, 60, 49, 30, 43]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'complicated', 'complicate', 'complexity', 'complexion', 'complexing', 'complexified', 'complexify', 'complexifies', 'complexing']) == [66, 61, 60, 75, 75, 77, 81, 77, 81, 77]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'complicated', 'complicate', 'complexity', 'complexion', 'complexing', 'complexified', 'complexify', 'complexifies', 'complexing']) == [66, 61, 60, 75, 75, 77, 81, 77, 81, 77]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'abra', 'bracadabra', 'bracada', 'braca', 'bracad', 'bracadab', 'bracadabr', 'bracadabra', 'bracadabram', 'bracadabramm']) == [15, 8, 75, 60, 45, 53, 66, 71, 75, 77, 78]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'abra', 'bracadabra', 'bracada', 'braca', 'bracad', 'bracadab', 'bracadabr', 'bracadabra', 'bracadabram', 'bracadabramm']) == [15, 8, 75, 60, 45, 53, 66, 71, 75, 77, 78]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'help', 'hero', 'her', 'hers', 'he', 'hem', 'hemoglobin']) == [24, 23, 22, 22, 21, 22, 18, 20, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'help', 'hero', 'her', 'hers', 'he', 'hem', 'hemoglobin']) == [24, 23, 22, 22, 21, 22, 18, 20, 27]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['trie', 'tr', 'tree', 'tries', 'trigger', 'trig']) == [18, 12, 14, 19, 21, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['trie', 'tr', 'tree', 'tries', 'trigger', 'trig']) == [18, 12, 14, 19, 21, 18]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa', 'a']) == [21, 20, 18, 15, 11, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa', 'a']) == [21, 20, 18, 15, 11, 6]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcde', 'abcdef', 'abcdefghij', 'a']) == [48, 21, 24, 32, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcde', 'abcdef', 'abcdefghij', 'a']) == [48, 21, 24, 32, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'algor', 'algorit', 'algorith', 'algorithme', 'algori', 'algorithmically']) == [57, 32, 39, 50, 54, 58, 45, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'algor', 'algorit', 'algorith', 'algorithme', 'algori', 'algorithmically']) == [57, 32, 39, 50, 54, 58, 45, 63]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandwidth']) == [18, 15, 18, 21, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandwidth']) == [18, 15, 18, 21, 23]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'alien', 'alliance', 'alibi', 'allocate', 'allot', 'allow', 'allude', 'allure', 'alloy', 'ally']) == [32, 30, 28, 37, 28, 40, 37, 37, 36, 36, 37, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'alien', 'alliance', 'alibi', 'allocate', 'allot', 'allow', 'allude', 'allure', 'alloy', 'ally']) == [32, 30, 28, 37, 28, 40, 37, 37, 36, 36, 37, 33]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pref', 'prefer', 'preference', 'preferred', 'preferring']) == [29, 21, 27, 35, 39, 39, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pref', 'prefer', 'preference', 'preferred', 'preferring']) == [29, 21, 27, 35, 39, 39, 40]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['data', 'database', 'datastructure', 'datamining', 'dataviz', 'datascience', 'datamodel']) == [28, 32, 38, 35, 31, 36, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['data', 'database', 'datastructure', 'datamining', 'dataviz', 'datascience', 'datamodel']) == [28, 32, 38, 35, 31, 36, 34]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro', 'progress', 'profound', 'process', 'progressive']) == [37, 33, 21, 35, 26, 25, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro', 'progress', 'profound', 'process', 'progressive']) == [37, 33, 21, 35, 26, 25, 38]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro', 'programminglanguage', 'prolog', 'protocol']) == [38, 30, 18, 46, 21, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro', 'programminglanguage', 'prolog', 'protocol']) == [38, 30, 18, 46, 21, 23]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'abacax', 'abac', 'aba', 'ab', 'a', 'abc', 'abcd', 'abcde']) == [29, 28, 24, 21, 17, 9, 20, 22, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'abacax', 'abac', 'aba', 'ab', 'a', 'abc', 'abcd', 'abcde']) == [29, 28, 24, 21, 17, 9, 20, 22, 23]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'ze', 'zoo', 'zookeeper', 'zest', 'zippy', 'zeta', 'zone']) == [15, 12, 13, 19, 14, 12, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'ze', 'zoo', 'zookeeper', 'zest', 'zippy', 'zeta', 'zone']) == [15, 12, 13, 19, 14, 12, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complexity', 'comp', 'compl', 'comple', 'complex', 'complexe', 'complexit']) == [48, 28, 34, 39, 43, 44, 47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complexity', 'comp', 'compl', 'comple', 'complex', 'complexe', 'complexit']) == [48, 28, 34, 39, 43, 44, 47]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'al', 'algorithmically', 'algo']) == [27, 18, 10, 33, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'al', 'algorithmically', 'algo']) == [27, 18, 10, 33, 17]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'un', 'uni', 'unic', 'uniqu', 'uniqueness', 'uniquely', 'uniques']) == [37, 16, 23, 24, 33, 41, 39, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'un', 'uni', 'unic', 'uniqu', 'uniqueness', 'uniquely', 'uniques']) == [37, 16, 23, 24, 33, 41, 39, 38]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['datastructure', 'data', 'datas', 'datast', 'datastr', 'datastru', 'datastruc']) == [52, 28, 34, 39, 43, 46, 48]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['datastructure', 'data', 'datas', 'datast', 'datastr', 'datastru', 'datastruc']) == [52, 28, 34, 39, 43, 46, 48]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefixes', 'pref', 'prefer', 'prefixing']) == [26, 28, 20, 22, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefixes', 'pref', 'prefer', 'prefixing']) == [26, 28, 20, 22, 29]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'ap', 'a', 'application']) == [15, 12, 9, 5, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'ap', 'a', 'application']) == [15, 12, 9, 5, 21]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'bandana', 'band', 'bandwidth', 'bandage']) == [18, 23, 19, 24, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'bandana', 'band', 'bandwidth', 'bandage']) == [18, 23, 19, 24, 23]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'abac', 'aba', 'ab', 'a', 'abacax', 'abacaxs', 'abacaxus']) == [35, 26, 21, 15, 8, 34, 35, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'abac', 'aba', 'ab', 'a', 'abacax', 'abacaxs', 'abacaxus']) == [35, 26, 21, 15, 8, 34, 35, 36]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interview', 'inter', 'interac', 'interactive', 'interact', 'interactivity']) == [34, 30, 38, 46, 41, 48]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interview', 'inter', 'interac', 'interactive', 'interact', 'interactivity']) == [34, 30, 38, 46, 41, 48]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefixing', 'prefixation', 'prefixer', 'pref', 'pre', 'p']) == [32, 35, 37, 34, 24, 19, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefixing', 'prefixation', 'prefixer', 'pref', 'pre', 'p']) == [32, 35, 37, 34, 24, 19, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zebr', 'zeb', 'ze', 'z', 'zebraa', 'zebrab', 'zebrac', 'zebrad']) == [35, 30, 24, 17, 9, 36, 36, 36, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zebr', 'zeb', 'ze', 'z', 'zebraa', 'zebrab', 'zebrac', 'zebrad']) == [35, 30, 24, 17, 9, 36, 36, 36, 36]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'cater', 'category', 'categories', 'caterpillar', 'catering', 'catered', 'caterer', 'caterers', 'catering']) == [30, 46, 46, 48, 52, 52, 50, 51, 52, 52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'cater', 'category', 'categories', 'caterpillar', 'catering', 'catered', 'caterer', 'caterers', 'catering']) == [30, 46, 46, 48, 52, 52, 50, 51, 52, 52]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'abacax', 'abac', 'aba', 'ab', 'a', 'bacaxi', 'bacax', 'bac', 'ba', 'b']) == [23, 22, 18, 15, 11, 6, 17, 16, 12, 9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'abacax', 'abac', 'aba', 'ab', 'a', 'bacaxi', 'bacax', 'bac', 'ba', 'b']) == [23, 22, 18, 15, 11, 6, 17, 16, 12, 9, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacax', 'abaca', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == [21, 20, 14, 18, 21, 23, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacax', 'abaca', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == [21, 20, 14, 18, 21, 23, 24]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylo', 'xylophon', 'xylophone', 'xylophones', 'xylophonist', 'xylophonists', 'xylophonistic', 'xylophonistically', 'xylophonists', 'xylophonist']) == [87, 44, 84, 87, 88, 102, 104, 106, 110, 104, 102]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylo', 'xylophon', 'xylophone', 'xylophones', 'xylophonist', 'xylophonists', 'xylophonistic', 'xylophonistically', 'xylophonists', 'xylophonist']) == [87, 44, 84, 87, 88, 102, 104, 106, 110, 104, 102]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'al', 'alex', 'alert']) == [19, 14, 10, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'al', 'alex', 'alert']) == [19, 14, 10, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandwidth', 'bandage']) == [21, 18, 22, 26, 27, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandwidth', 'bandage']) == [21, 18, 22, 26, 27, 26]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested', 'testify', 'testimony', 'testimonial', 'testament', 'testamentary', 'testator', 'testatrix']) == [40, 46, 42, 46, 51, 53, 52, 55, 48, 49]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested', 'testify', 'testimony', 'testimonial', 'testament', 'testamentary', 'testator', 'testatrix']) == [40, 46, 42, 46, 51, 53, 52, 55, 48, 49]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'band', 'bandana', 'bandanna', 'bandage', 'bandaid']) == [21, 23, 30, 31, 29, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'band', 'bandana', 'bandanna', 'bandage', 'bandaid']) == [21, 23, 30, 31, 29, 29]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abc', 'ab', 'a', 'zyx', 'zy', 'z', 'mnop', 'mno', 'mn', 'm']) == [10, 9, 7, 4, 6, 5, 3, 10, 9, 7, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abc', 'ab', 'a', 'zyx', 'zy', 'z', 'mnop', 'mno', 'mn', 'm']) == [10, 9, 7, 4, 6, 5, 3, 10, 9, 7, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'optimizer', 'optimize', 'optimal', 'optimism', 'optimist', 'optimum', 'option', 'optional', 'opt', 'optic', 'optics']) == [67, 65, 64, 56, 62, 62, 56, 51, 53, 36, 49, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'optimizer', 'optimize', 'optimal', 'optimism', 'optimist', 'optimum', 'option', 'optional', 'opt', 'optic', 'optics']) == [67, 65, 64, 56, 62, 62, 56, 51, 53, 36, 49, 50]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandanna', 'banda', 'bandanaaa']) == [24, 21, 26, 35, 35, 30, 37]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandanna', 'banda', 'bandanaaa']) == [24, 21, 26, 35, 35, 30, 37]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'super', 'supercal', 'supercalifrag', 'supercalifragilistic', 'supercalifragilisticex', 'supercalifragilisticexp', 'supercalifragilisticexpia', 'supercalifragilisticexpiali', 'supercalifragilisticexpialidoc', 'supercalifragilisticexpialidociou', 'supercalifragilisticexpialidociousness']) == [274, 60, 93, 143, 206, 222, 229, 241, 251, 263, 272, 278]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'super', 'supercal', 'supercalifrag', 'supercalifragilistic', 'supercalifragilisticex', 'supercalifragilisticexp', 'supercalifragilisticexpia', 'supercalifragilisticexpiali', 'supercalifragilisticexpialidoc', 'supercalifragilisticexpialidociou', 'supercalifragilisticexpialidociousness']) == [274, 60, 93, 143, 206, 222, 229, 241, 251, 263, 272, 278]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interspecies', 'inter', 'interstellar', 'interact', 'interaction', 'interference', 'internet', 'interim']) == [48, 40, 48, 46, 49, 47, 43, 42]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interspecies', 'inter', 'interstellar', 'interact', 'interaction', 'interference', 'internet', 'interim']) == [48, 40, 48, 46, 49, 47, 43, 42]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['hello', 'hell', 'he', 'h']) == [12, 11, 7, 4]
    assert candidate(words = ['abc', 'ab', 'bc', 'b']) == [5, 4, 3, 2]
    assert candidate(words = ['a', 'b', 'c', 'd']) == [1, 1, 1, 1]
    assert candidate(words = ['aa', 'aaa', 'aaaa', 'aaaaa']) == [8, 11, 13, 14]
    assert candidate(words = ['a', 'ab', 'abc', 'abcd']) == [4, 7, 9, 10]
    assert candidate(words = ['abcde', 'abcd', 'abc', 'ab', 'a']) == [15, 14, 12, 9, 5]
    assert candidate(words = ['b', 'bb', 'bbb', 'bbbb']) == [4, 7, 9, 10]
    assert candidate(words = ['xyz', 'xy', 'x']) == [6, 5, 3]
    assert candidate(words = ['abcd']) == [4]
    assert candidate(words = ['xyz', 'xy', 'x', 'xyzabc']) == [9, 7, 4, 12]
    assert candidate(words = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']) == [4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(words = ['aaaa', 'aa', 'a']) == [7, 5, 3]
    assert candidate(words = ['dynamic', 'dyn', 'dynam', 'dynamicp', 'dynamicpr', 'dynamicpro', 'dynamicprogra', 'dynamicprogram', 'dynamicprogramming']) == [57, 27, 43, 63, 68, 72, 81, 83, 87]
    assert candidate(words = ['optimization', 'optimize', 'opt', 'opti', 'optim', 'optimi']) == [37, 33, 18, 23, 27, 30]
    assert candidate(words = ['xylophone', 'xylo', 'xylophon', 'xy', 'xyl', 'xylophonist', 'xylophoneplayer', 'xylophoneplayerperformance']) == [52, 29, 49, 16, 23, 52, 64, 75]
    assert candidate(words = ['xylophone', 'xylography', 'xylo', 'xylophoneography', 'xyl', 'xylonate']) == [33, 29, 23, 40, 18, 27]
    assert candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aa', 'a', 'aabbbccc', 'aabbbbcccc', 'aabbbbccccd']) == [30, 29, 27, 15, 8, 33, 40, 41]
    assert candidate(words = ['aaaa', 'aaab', 'aaac', 'aabb', 'aabc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accc']) == [31, 31, 31, 30, 30, 35, 35, 35, 35, 35, 35, 35, 35, 35, 34, 34, 34, 34, 34, 34, 33, 33]
    assert candidate(words = ['abacax', 'abaca', 'bacax', 'abac', 'ab']) == [17, 16, 5, 14, 8]
    assert candidate(words = ['apple', 'app', 'application', 'applesauce', 'appetizer']) == [20, 15, 25, 25, 21]
    assert candidate(words = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumo', 'pneumonoultra', 'pneumonoultramicro', 'pneumonoultramicroscopicsilico', 'pneumonoultramicroscopicsilicovolcano', 'pneumo']) == [155, 42, 77, 97, 133, 147, 42]
    assert candidate(words = ['programming', 'program', 'pro', 'prog', 'progr']) == [30, 26, 15, 19, 22]
    assert candidate(words = ['algorithm', 'algo', 'al', 'alex', 'ale', 'all']) == [21, 16, 12, 15, 14, 13]
    assert candidate(words = ['abcdabcd', 'abcabc', 'ababab', 'aaaaaa', 'bbbbbb', 'cccccc', 'dddddd']) == [14, 12, 11, 9, 6, 6, 6]
    assert candidate(words = ['algorithm', 'algo', 'alg', 'algor', 'algorith', 'algori']) == [35, 23, 18, 27, 34, 30]
    assert candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa', 'a', 'aabbbcc', 'aabbb', 'aabbbb']) == [33, 32, 30, 24, 17, 9, 35, 33, 34]
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa']) == [9, 17, 24, 30, 35, 39, 42, 44, 45]
    assert candidate(words = ['prefix', 'pre', 'prefer', 'preference', 'presentation', 'president', 'presidency']) == [26, 21, 28, 32, 32, 33, 34]
    assert candidate(words = ['hello', 'hell', 'he', 'h', 'hero', 'helium', 'helper']) == [20, 19, 13, 7, 15, 20, 20]
    assert candidate(words = ['unique', 'un', 'uni', 'unic', 'uniqu', 'uniquee', 'uniqueee', 'uniqueeee']) == [37, 16, 23, 24, 33, 40, 42, 43]
    assert candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefin', 'prefixation', 'prefixes', 'prefixing', 'prefixes', 'preference', 'prefer']) == [55, 33, 43, 50, 51, 60, 59, 58, 59, 51, 47]
    assert candidate(words = ['apple', 'app', 'ap', 'application', 'appetite']) == [17, 14, 10, 23, 19]
    assert candidate(words = ['aabbcc', 'aab', 'abc', 'aac', 'acc', 'aaa', 'bbb', 'ccc', 'aabbc', 'aabbbc', 'aabbbcc', 'aabbbccc']) == [32, 24, 12, 19, 12, 19, 3, 3, 31, 35, 37, 38]
    assert candidate(words = ['complex', 'com', 'compl', 'complexity', 'composite']) == [26, 15, 22, 29, 24]
    assert candidate(words = ['cat', 'cater', 'caterpillar', 'catering', 'caterer', 'caterers', 'catered', 'catering']) == [24, 38, 44, 44, 43, 44, 42, 44]
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
    assert candidate(words = ['optimization', 'opt', 'opti', 'optim', 'optimiz', 'optimise', 'optimized']) == [44, 21, 27, 32, 39, 38, 41]
    assert candidate(words = ['data', 'dat', 'database', 'datascience', 'datastructure']) == [19, 15, 23, 27, 29]
    assert candidate(words = ['car', 'cat', 'catch', 'cart', 'card', 'carpet']) == [16, 14, 16, 17, 17, 19]
    assert candidate(words = ['banana', 'band', 'ball', 'bat', 'basketball']) == [15, 13, 12, 11, 18]
    assert candidate(words = ['programming', 'program', 'pro', 'pr', 'p', 'prefix', 'pre', 'preprocessing']) == [30, 26, 18, 15, 8, 21, 18, 28]
    assert candidate(words = ['longword', 'longworder', 'longworderer', 'longwordererest', 'longwordereresterest']) == [40, 48, 54, 60, 65]
    assert candidate(words = ['algorithm', 'algo', 'al', 'alex', 'algorithmic', 'algorithms']) == [35, 20, 12, 14, 37, 36]
    assert candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']) == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    assert candidate(words = ['backtracking', 'back', 'backt', 'backtr', 'backtra', 'backtrac', 'backtrack', 'backtracki', 'backtrackin', 'backtrackin', 'backtrackinga', 'backtrackingal', 'backtrackingalg', 'backtrackingalgo']) == [131, 56, 69, 81, 92, 102, 111, 119, 126, 126, 135, 138, 140, 141]
    assert candidate(words = ['prefix', 'pre', 'pres', 'presum', 'pressure']) == [18, 15, 18, 20, 22]
    assert candidate(words = ['interview', 'inter', 'inte', 'interw', 'interv', 'intervi', 'interviewe']) == [45, 34, 28, 35, 38, 41, 46]
    assert candidate(words = ['zebra', 'zoo', 'zookeeper', 'zoozoo', 'ze', 'zee', 'z']) == [13, 13, 19, 16, 10, 11, 7]
    assert candidate(words = ['repeated', 'repeat', 'rep', 're', 'r', 'peated', 'eat', 'e', 't', 'ted', 'tedious', 'tediousness']) == [20, 18, 12, 9, 5, 6, 4, 2, 4, 10, 18, 22]
    assert candidate(words = ['banana', 'ban', 'bananas', 'band', 'bandana', 'bandwidth']) == [24, 18, 25, 21, 24, 26]
    assert candidate(words = ['repeated', 'repeats', 'repeat', 'repeating', 'repeatedly', 'repeatability']) == [40, 37, 36, 39, 42, 43]
    assert candidate(words = ['algorithm', 'al', 'algo', 'all', 'algorithms', 'application', 'app']) == [28, 12, 18, 13, 29, 19, 11]
    assert candidate(words = ['flower', 'flow', 'flight', 'flour', 'flourish', 'flourishingly']) == [21, 19, 16, 23, 29, 34]
    assert candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandanna', 'banda']) == [21, 18, 22, 28, 29, 25]
    assert candidate(words = ['hello', 'hell', 'he', 'h', 'helicopter', 'helium', 'help', 'hero', 'her', 'hemoglobin']) == [27, 26, 19, 10, 32, 28, 25, 22, 21, 27]
    assert candidate(words = ['unique', 'uniques', 'unicorn', 'unicycle', 'universality']) == [21, 22, 20, 21, 24]
    assert candidate(words = ['optimization', 'optimizer', 'optimize', 'optimal', 'optimism', 'optimist', 'optimistic', 'optimum', 'opt', 'optional']) == [61, 59, 58, 49, 57, 58, 60, 49, 30, 43]
    assert candidate(words = ['complex', 'complicated', 'complicate', 'complexity', 'complexion', 'complexing', 'complexified', 'complexify', 'complexifies', 'complexing']) == [66, 61, 60, 75, 75, 77, 81, 77, 81, 77]
    assert candidate(words = ['abracadabra', 'abra', 'bracadabra', 'bracada', 'braca', 'bracad', 'bracadab', 'bracadabr', 'bracadabra', 'bracadabram', 'bracadabramm']) == [15, 8, 75, 60, 45, 53, 66, 71, 75, 77, 78]
    assert candidate(words = ['hello', 'hell', 'help', 'hero', 'her', 'hers', 'he', 'hem', 'hemoglobin']) == [24, 23, 22, 22, 21, 22, 18, 20, 27]
    assert candidate(words = ['trie', 'tr', 'tree', 'tries', 'trigger', 'trig']) == [18, 12, 14, 19, 21, 18]
    assert candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa', 'a']) == [21, 20, 18, 15, 11, 6]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcde', 'abcdef', 'abcdefghij', 'a']) == [48, 21, 24, 32, 5]
    assert candidate(words = ['algorithm', 'algo', 'algor', 'algorit', 'algorith', 'algorithme', 'algori', 'algorithmically']) == [57, 32, 39, 50, 54, 58, 45, 63]
    assert candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandwidth']) == [18, 15, 18, 21, 23]
    assert candidate(words = ['algorithm', 'algebra', 'alien', 'alliance', 'alibi', 'allocate', 'allot', 'allow', 'allude', 'allure', 'alloy', 'ally']) == [32, 30, 28, 37, 28, 40, 37, 37, 36, 36, 37, 33]
    assert candidate(words = ['prefix', 'pre', 'pref', 'prefer', 'preference', 'preferred', 'preferring']) == [29, 21, 27, 35, 39, 39, 40]
    assert candidate(words = ['data', 'database', 'datastructure', 'datamining', 'dataviz', 'datascience', 'datamodel']) == [28, 32, 38, 35, 31, 36, 34]
    assert candidate(words = ['programming', 'program', 'pro', 'progress', 'profound', 'process', 'progressive']) == [37, 33, 21, 35, 26, 25, 38]
    assert candidate(words = ['programming', 'program', 'pro', 'programminglanguage', 'prolog', 'protocol']) == [38, 30, 18, 46, 21, 23]
    assert candidate(words = ['abacaxi', 'abacax', 'abac', 'aba', 'ab', 'a', 'abc', 'abcd', 'abcde']) == [29, 28, 24, 21, 17, 9, 20, 22, 23]
    assert candidate(words = ['zebra', 'ze', 'zoo', 'zookeeper', 'zest', 'zippy', 'zeta', 'zone']) == [15, 12, 13, 19, 14, 12, 14, 13]
    assert candidate(words = ['complexity', 'comp', 'compl', 'comple', 'complex', 'complexe', 'complexit']) == [48, 28, 34, 39, 43, 44, 47]
    assert candidate(words = ['algorithm', 'algebra', 'al', 'algorithmically', 'algo']) == [27, 18, 10, 33, 17]
    assert candidate(words = ['unique', 'un', 'uni', 'unic', 'uniqu', 'uniqueness', 'uniquely', 'uniques']) == [37, 16, 23, 24, 33, 41, 39, 38]
    assert candidate(words = ['datastructure', 'data', 'datas', 'datast', 'datastr', 'datastru', 'datastruc']) == [52, 28, 34, 39, 43, 46, 48]
    assert candidate(words = ['prefix', 'prefixes', 'pref', 'prefer', 'prefixing']) == [26, 28, 20, 22, 29]
    assert candidate(words = ['apple', 'app', 'ap', 'a', 'application']) == [15, 12, 9, 5, 21]
    assert candidate(words = ['banana', 'bandana', 'band', 'bandwidth', 'bandage']) == [18, 23, 19, 24, 23]
    assert candidate(words = ['abacaxi', 'abac', 'aba', 'ab', 'a', 'abacax', 'abacaxs', 'abacaxus']) == [35, 26, 21, 15, 8, 34, 35, 36]
    assert candidate(words = ['interview', 'inter', 'interac', 'interactive', 'interact', 'interactivity']) == [34, 30, 38, 46, 41, 48]
    assert candidate(words = ['prefix', 'prefixing', 'prefixation', 'prefixer', 'pref', 'pre', 'p']) == [32, 35, 37, 34, 24, 19, 7]
    assert candidate(words = ['zebra', 'zebr', 'zeb', 'ze', 'z', 'zebraa', 'zebrab', 'zebrac', 'zebrad']) == [35, 30, 24, 17, 9, 36, 36, 36, 36]
    assert candidate(words = ['cat', 'cater', 'category', 'categories', 'caterpillar', 'catering', 'catered', 'caterer', 'caterers', 'catering']) == [30, 46, 46, 48, 52, 52, 50, 51, 52, 52]
    assert candidate(words = ['abacaxi', 'abacax', 'abac', 'aba', 'ab', 'a', 'bacaxi', 'bacax', 'bac', 'ba', 'b']) == [23, 22, 18, 15, 11, 6, 17, 16, 12, 9, 5]
    assert candidate(words = ['abacax', 'abaca', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == [21, 20, 14, 18, 21, 23, 24]
    assert candidate(words = ['xylophone', 'xylo', 'xylophon', 'xylophone', 'xylophones', 'xylophonist', 'xylophonists', 'xylophonistic', 'xylophonistically', 'xylophonists', 'xylophonist']) == [87, 44, 84, 87, 88, 102, 104, 106, 110, 104, 102]
    assert candidate(words = ['algorithm', 'algo', 'al', 'alex', 'alert']) == [19, 14, 10, 13, 14]
    assert candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandwidth', 'bandage']) == [21, 18, 22, 26, 27, 26]
    assert candidate(words = ['test', 'testing', 'tested', 'testify', 'testimony', 'testimonial', 'testament', 'testamentary', 'testator', 'testatrix']) == [40, 46, 42, 46, 51, 53, 52, 55, 48, 49]
    assert candidate(words = ['banana', 'band', 'bandana', 'bandanna', 'bandage', 'bandaid']) == [21, 23, 30, 31, 29, 29]
    assert candidate(words = ['abcd', 'abc', 'ab', 'a', 'zyx', 'zy', 'z', 'mnop', 'mno', 'mn', 'm']) == [10, 9, 7, 4, 6, 5, 3, 10, 9, 7, 4]
    assert candidate(words = ['optimization', 'optimizer', 'optimize', 'optimal', 'optimism', 'optimist', 'optimum', 'option', 'optional', 'opt', 'optic', 'optics']) == [67, 65, 64, 56, 62, 62, 56, 51, 53, 36, 49, 50]
    assert candidate(words = ['banana', 'ban', 'band', 'bandana', 'bandanna', 'banda', 'bandanaaa']) == [24, 21, 26, 35, 35, 30, 37]
    assert candidate(words = ['supercalifragilisticexpialidocious', 'super', 'supercal', 'supercalifrag', 'supercalifragilistic', 'supercalifragilisticex', 'supercalifragilisticexp', 'supercalifragilisticexpia', 'supercalifragilisticexpiali', 'supercalifragilisticexpialidoc', 'supercalifragilisticexpialidociou', 'supercalifragilisticexpialidociousness']) == [274, 60, 93, 143, 206, 222, 229, 241, 251, 263, 272, 278]
    assert candidate(words = ['interspecies', 'inter', 'interstellar', 'interact', 'interaction', 'interference', 'internet', 'interim']) == [48, 40, 48, 46, 49, 47, 43, 42]


