def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aaabaaa",words = ['aa', 'aaa', 'aaaa', 'aabaaa']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa",words = ['aa', 'aaa', 'aaaa', 'aabaaa']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa",words = ['aaa', 'aab', 'aaaaa', 'aaabaa', 'aaaba']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa",words = ['aaa', 'aab', 'aaaaa', 'aaabaa', 'aaaba']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc', 'abcd', 'abdc', 'aabbccdd']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc', 'abcd', 'abdc', 'aabbccdd']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc', 'abcd', 'abcde']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc', 'abcd', 'abcde']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd",words = ['aabbccddd', 'aabbbcccddd', 'aabbbcccdd']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd",words = ['aabbccddd', 'aabbbcccddd', 'aabbbcccdd']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",words = ['a', 'aa', 'aaa', 'aaaa']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",words = ['a', 'aa', 'aaa', 'aaaa']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",words = ['aabbcc', 'aabbc', 'aaabc']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",words = ['aabbcc', 'aabbc', 'aaabc']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['aabbccdd', 'abccdd', 'abbbccdd', 'aabbcccddd']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['aabbccdd', 'abccdd', 'abbbccdd', 'aabbcccddd']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "heeellooo",words = ['hello', 'hi', 'helo']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "heeellooo",words = ['hello', 'hi', 'helo']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa",words = ['aab', 'aaab', 'aaaab', 'aaaba', 'aaaaaaab']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa",words = ['aab', 'aaab', 'aaaab', 'aaaba', 'aaaaaaab']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc', 'abcd', 'abcde', 'ab', 'a']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc', 'abcd', 'abcde', 'ab', 'a']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbb",words = ['aabb', 'aabbbb', 'aaabbbb']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbb",words = ['aabb', 'aabbbb', 'aaabbbb']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde', 'aabbccdd']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde', 'aabbccdd']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyy",words = ['zzyy', 'zy', 'zyy']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyy",words = ['zzyy', 'zy', 'zyy']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "heeellloooopppp",words = ['helloppp', 'heellooppp', 'helooppp', 'helllopppp', 'heeelllooooooo', 'hello']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "heeellloooopppp",words = ['helloppp', 'heellooppp', 'helooppp', 'helllopppp', 'heeelllooooooo', 'hello']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ttttuuuuuuuuuuuuvvv",words = ['tuv', 'tttuuuuuuuuuuvvv', 'ttttuuuuuuuuuuu', 'ttttuuuuuuuuuvv', 'ttttuuuuuuuuuuuuv']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ttttuuuuuuuuuuuuvvv",words = ['tuv', 'tttuuuuuuuuuuvvv', 'ttttuuuuuuuuuuu', 'ttttuuuuuuuuuvv', 'ttttuuuuuuuuuuuuv']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "heeeloooooo",words = ['hello', 'heeellooo', 'helllooo', 'heellooo', 'heeelloo']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "heeeloooooo",words = ['hello', 'heeellooo', 'helllooo', 'heellooo', 'heeelloo']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",words = ['aabbcc', 'aaabbbcccc', 'aaaabbbbccc', 'aaaabbbcccc', 'aaaaabbbbcccc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",words = ['aabbcc', 'aaabbbcccc', 'aaaabbbbccc', 'aaaabbbcccc', 'aaaaabbbbcccc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeee",words = ['aabcd', 'abbbcd', 'abccde', 'abcde', 'aaaaabbbbccccddddeee']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeee",words = ['aabcd', 'abbbcd', 'abccde', 'abcde', 'aaaaabbbbccccddddeee']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmmmnnnnnnoooopppppp",words = ['mnop', 'mmnnnnoooppp', 'mmmmmnnnnnnnoooooopppppp', 'mmnnoopp', 'mmnnoooopppp']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmmnnnnnnoooopppppp",words = ['mnop', 'mmnnnnoooppp', 'mmmmmnnnnnnnoooooopppppp', 'mmnnoopp', 'mmnnoooopppp']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxxxxyyyyyyzzzzzz",words = ['xyzz', 'xxxyyyyzzz', 'xxxxxyyyzzzzz', 'xxxxxyyyyyyzzzz', 'xxxxxyyyyyyzzzzzz']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxxxxyyyyyyzzzzzz",words = ['xyzz', 'xxxyyyyzzz', 'xxxxxyyyzzzzz', 'xxxxxyyyyyyzzzz', 'xxxxxyyyyyyzzzzzz']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "llllaaaabbbbccccddddeeeee",words = ['laabcd', 'labbbccddeee', 'labcde', 'laaaabbbbccccddddeee', 'lbbbcccddddeeee']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "llllaaaabbbbccccddddeeeee",words = ['laabcd', 'labbbccddeee', 'labcde', 'laaaabbbbccccddddeee', 'lbbbcccddddeeee']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbcccddd",words = ['abc', 'abbc', 'abbcc', 'abbbcccd', 'abbbcccddd', 'abbbcccdd', 'abbbccccd', 'abbbccccdd']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbcccddd",words = ['abc', 'abbc', 'abbcc', 'abbbcccd', 'abbbcccddd', 'abbbcccdd', 'abbbccccd', 'abbbccccdd']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmmmnnnnoooopppp",words = ['mno', 'mmnnnnooooppp', 'mmmmnnnnoooop', 'mmmmnnnnoooopppp', 'mmmmnnnnoooppp']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmmnnnnoooopppp",words = ['mno', 'mmnnnnooooppp', 'mmmmnnnnoooop', 'mmmmnnnnoooopppp', 'mmmmnnnnoooppp']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "heeellloooowooorlddd",words = ['helo', 'hello', 'helooworld', 'heeellooworld', 'heeelllooooowooorlddd']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "heeellloooowooorlddd",words = ['helo', 'hello', 'helooworld', 'heeellooworld', 'heeelllooooowooorlddd']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmmmmmmnnnnnnn",words = ['mmnn', 'mmmnnn', 'mmmmnnnn', 'mmmmmn', 'mmmmnn', 'mmmmmnnn', 'mmmmmmnnnnn', 'mmmmmmnnnn']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmmmmmnnnnnnn",words = ['mmnn', 'mmmnnn', 'mmmmnnnn', 'mmmmmn', 'mmmmnn', 'mmmmmnnn', 'mmmmmmnnnnn', 'mmmmmmnnnn']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zzzzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbbccddeeefffgghhhiiiijjjkkklllmmmnnnooooppppqqqqrrrrsssss', 'aabbccddeeefffgggiiiijjjkkklllmmmnnnoooopppqqqqrrrrrrsssss', 'aabbccddeeffgghhiijjkkklllmmmmmnnnnnoooooopppppqqqqqqrrrrrrssssss']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zzzzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbbccddeeefffgghhhiiiijjjkkklllmmmnnnooooppppqqqqrrrrsssss', 'aabbccddeeefffgggiiiijjjkkklllmmmnnnoooopppqqqqrrrrrrsssss', 'aabbccddeeffgghhiijjkkklllmmmmmnnnnnoooooopppppqqqqqqrrrrrrssssss']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzyyyyyyyy",words = ['xyz', 'xyyz', 'xyzz', 'xyzzz', 'xyzzzz', 'xyzzzzzyyyyy', 'xyzzzzzyyyyyy', 'xyzzzzzyyyyyyyy']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzyyyyyyyy",words = ['xyz', 'xyyz', 'xyzz', 'xyzzz', 'xyzzzz', 'xyzzzzzyyyyy', 'xyzzzzzyyyyyy', 'xyzzzzzyyyyyyyy']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzyyyyyyy",words = ['zzzyyyy', 'zzzzzyyy', 'zzzyyyyyyy', 'zzzzzzzzyy', 'zyyyyyyy']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzyyyyyyy",words = ['zzzyyyy', 'zzzzzyyy', 'zzzyyyyyyy', 'zzzzzzzzyy', 'zyyyyyyy']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiiii",words = ['mississippi', 'missisiiippi', 'mississippiiiii', 'missisipi', 'misisipi']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiiii",words = ['mississippi', 'missisiiippi', 'mississippiiiii', 'missisipi', 'misisipi']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyzzzz",words = ['xxyyz', 'xxyyzz', 'xxxyyyzzzz', 'xxyyzzz', 'xyzzz']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyzzzz",words = ['xxyyz', 'xxyyzz', 'xxxyyyzzzz', 'xxyyzzz', 'xyzzz']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccccddddeeeffggg",words = ['aabbccddeeffg', 'aabbcccddddeffgg', 'aabbbccccddddeeeffggg', 'aabbbcccddddeeeffgg', 'aabbccccdddddeeeffggg']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccccddddeeeffggg",words = ['aabbccddeeffg', 'aabbcccddddeffgg', 'aabbbccccddddeeeffggg', 'aabbbcccddddeeeffgg', 'aabbccccdddddeeeffggg']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxxxxxyyyyyyzzzzzz",words = ['xyzz', 'xyzzz', 'xyyz', 'xxxyyyyzzz', 'xxxxxyyyyyyzzzzzz']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxxxxxyyyyyyzzzzzz",words = ['xyzz', 'xyzzz', 'xyyz', 'xxxyyyyzzz', 'xxxxxyyyyyyzzzzzz']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",words = ['qq', 'qqq', 'qqqq', 'qqqqqq', 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",words = ['qq', 'qqq', 'qqqq', 'qqqqqq', 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ttttttttttttuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvvv",words = ['tuv', 'ttuuuvvv', 'ttttuuuuuuuvvvvvvv', 'tttuuuuuuvvvvvvvvvv', 'ttttuuuuuuuuuuuvvvvvvvvvvvvvvvvvv']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ttttttttttttuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvvv",words = ['tuv', 'ttuuuvvv', 'ttttuuuuuuuvvvvvvv', 'tttuuuuuuvvvvvvvvvv', 'ttttuuuuuuuuuuuvvvvvvvvvvvvvvvvvv']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqqrrrrssss",words = ['pqrst', 'pqrs', 'ppqrs', 'ppqqrrss', 'ppqqqrrrssss', 'ppqqqqrrrrsssss']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqqrrrrssss",words = ['pqrst', 'pqrs', 'ppqrs', 'ppqqrrss', 'ppqqqrrrssss', 'ppqqqqrrrrsssss']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "helloooooworlddddd",words = ['hellooworld', 'hellooworlddd', 'hellllooworld', 'helloooworldddddd', 'hellooooooworlddddd']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "helloooooworlddddd",words = ['hellooworld', 'hellooworlddd', 'hellllooworld', 'helloooworldddddd', 'hellooooooworlddddd']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiissi",words = ['mississippissi', 'misisipi', 'mississippi', 'mississsippi', 'mississippiii']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiissi",words = ['mississippissi', 'misisipi', 'mississippi', 'mississsippi', 'mississippiii']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeee",words = ['abcde', 'aabbcdeee', 'aaabbbcccdddeee', 'aabbccdde', 'aabccdeee']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeee",words = ['abcde', 'aabbcdeee', 'aaabbbcccdddeee', 'aabbccdde', 'aabccdeee']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqqrrrssss",words = ['pqr', 'ppqqrrsss', 'pppqqqrrrrssss', 'ppqqrrsssss', 'ppqqrrr']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqqrrrssss",words = ['pqr', 'ppqqrrsss', 'pppqqqrrrrssss', 'ppqqrrsssss', 'ppqqrrr']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklllllmnopqrstuvwxyz",words = ['abcdefghijklmopqrstuvwxyz', 'abcdefghijklllmmnopqrstuvwxyz', 'abcdefghijkllllmnopqrstuvwxyz', 'abcdefghijklllllmnopqrstuvwxy', 'abcdefghijklllllmnopqrstuvwxyz']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklllllmnopqrstuvwxyz",words = ['abcdefghijklmopqrstuvwxyz', 'abcdefghijklllmmnopqrstuvwxyz', 'abcdefghijkllllmnopqrstuvwxyz', 'abcdefghijklllllmnopqrstuvwxy', 'abcdefghijklllllmnopqrstuvwxyz']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "hhheeelllllooooworrlldd",words = ['helloworld', 'hhhellooooworld', 'hheeellllllooooworld', 'hellooworld', 'hheellooworl']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hhheeelllllooooworrlldd",words = ['helloworld', 'hhhellooooworld', 'hheeellllllooooworld', 'hellooworld', 'hheellooworl']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ssssaaafffff",words = ['saff', 'ssaff', 'ssaaaff', 'ssaaaafff', 'ssaaaaaffff', 'ssssaaaafffff']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ssssaaafffff",words = ['saff', 'ssaff', 'ssaaaff', 'ssaaaafff', 'ssaaaaaffff', 'ssssaaaafffff']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjjjjjjklmnopqrstuvwxyz",words = ['abcdefghijklnopqrstuvwxyz', 'abcdefghijjjklmnopqrstuvwxyz', 'abcdefghijjjjjjklmnopqrstuvwxyz', 'abcdefghijjjjjjjklmnopqrstuv', 'abcdefghijjjjjjjmnopqrstuvwxyz']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjjjjjjklmnopqrstuvwxyz",words = ['abcdefghijklnopqrstuvwxyz', 'abcdefghijjjklmnopqrstuvwxyz', 'abcdefghijjjjjjklmnopqrstuvwxyz', 'abcdefghijjjjjjjklmnopqrstuv', 'abcdefghijjjjjjjmnopqrstuvwxyz']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiiiiijjjjjjkkkkkkk",words = ['abcdefghijjk', 'abcdefghijk', 'abcdefghiiijjjjkk', 'abcdefghiiijjjjjjkkkkk', 'abcdefghiiijjjjjjkkkkkkk']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiiiiijjjjjjkkkkkkk",words = ['abcdefghijjk', 'abcdefghijk', 'abcdefghiiijjjjkk', 'abcdefghiiijjjjjjkkkkk', 'abcdefghiiijjjjjjkkkkkkk']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abcdefghijklmnopqrstuvwxyzz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzzz', 'abcdefghijklmnopqrstuvwxyzzzz', 'abcdefghijklmnopqrstuvwxyzzzzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abcdefghijklmnopqrstuvwxyzz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzzz', 'abcdefghijklmnopqrstuvwxyzzzz', 'abcdefghijklmnopqrstuvwxyzzzzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabbbbcccdd",words = ['aabbbccdd', 'aaabbbcccdd', 'aaaabbbcccdd', 'aaaaabbbcccdd', 'aaaaaaabbbcccdd', 'aaaaaaabbbcccd', 'aaaaaaabbbbccdd', 'aaaaaaabbbbcccdd']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabbbbcccdd",words = ['aabbbccdd', 'aaabbbcccdd', 'aaaabbbcccdd', 'aaaaabbbcccdd', 'aaaaaaabbbcccdd', 'aaaaaaabbbcccd', 'aaaaaaabbbbccdd', 'aaaaaaabbbbcccdd']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqwwweeeerrrrttttt",words = ['qqqqqqqwwwreeeeeerttt', 'qqqwwwreeert', 'qqqqqqqwwwreeerrttt', 'qqqqqqqqqqqwwweeeerrrtttt', 'qqqqqqqwwweeeerrrtttt']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqwwweeeerrrrttttt",words = ['qqqqqqqwwwreeeeeerttt', 'qqqwwwreeert', 'qqqqqqqwwwreeerrttt', 'qqqqqqqqqqqwwweeeerrrtttt', 'qqqqqqqwwweeeerrrtttt']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeeeeef",words = ['abcdeeef', 'abcdeeeef', 'abcdeeeeeef', 'abcdfeeeef', 'abcdef']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeeeeef",words = ['abcdeeef', 'abcdeeeef', 'abcdeeeeeef', 'abcdfeeeef', 'abcdef']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjkkklllllmmmmmmmnnnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz",words = ['abcdefghijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'abcdefghijjkkkllllmmmmnnnnooooopppqqqqrrrrsssssttttuvvvvwwwwxxyyyyzzzz', 'abcdefghijjkkklllllmmmmmmnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjkkklllllmmmmmmmnnnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz",words = ['abcdefghijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'abcdefghijjkkkllllmmmmnnnnooooopppqqqqrrrrsssssttttuvvvvwwwwxxyyyyzzzz', 'abcdefghijjkkklllllmmmmmmnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbccdddd",words = ['abcdd', 'abbbccdd', 'abbbccccdd', 'abbbccdddd', 'aabbccddd']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbccdddd",words = ['abcdd', 'abbbccdd', 'abbbccccdd', 'abbbccdddd', 'aabbccddd']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqqrrr",words = ['pqr', 'pppqqrr', 'ppqqqrrr', 'pppqqqqrrr', 'ppppqqqrrr']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqqrrr",words = ['pqr', 'pppqqrr', 'ppqqqrrr', 'pppqqqqrrr', 'ppppqqqrrr']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbcccddeeeee",words = ['aabccddee', 'aaabbbcccdddeeee', 'aaaabbbcccdddeee', 'aaaaabbcccddeeee', 'aaaaabbbbccccddeeeeee']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbcccddeeeee",words = ['aabccddee', 'aaabbbcccdddeeee', 'aaaabbbcccdddeee', 'aaaaabbcccddeeee', 'aaaaabbbbccccddeeeeee']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "llllllmmmnnnnoo",words = ['lmno', 'lllmmnno', 'lllllmmnnnoo', 'lllmmmnnnnoo', 'llllllmmmnnno']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "llllllmmmnnnnoo",words = ['lmno', 'lllmmnno', 'lllllmmnnnoo', 'lllmmmnnnnoo', 'llllllmmmnnno']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg",words = ['aabbccddeefffggg', 'aabbbcccdddeeefffggg', 'aabbccddeeeffffgggg', 'aabbccddeeeffg', 'aabbcddfeeeffggg']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg",words = ['aabbccddeefffggg', 'aabbbcccdddeeefffggg', 'aabbccddeeeffffgggg', 'aabbccddeeeffg', 'aabbcddfeeeffggg']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ttrrreeee",words = ['tree', 'ttrree', 'ttrreee', 'ttreee', 'ttrre', 'ttre', 'trreee', 'ttreere']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ttrrreeee",words = ['tree', 'ttrree', 'ttrreee', 'ttreee', 'ttrre', 'ttre', 'trreee', 'ttreere']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmmaaa",words = ['maa', 'maaaa', 'mmmaaa', 'mmma', 'mmmaaaam']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmaaa",words = ['maa', 'maaaa', 'mmmaaa', 'mmma', 'mmmaaaam']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "sssssssssssssssssssssssssssss",words = ['s', 'ss', 'sss', 'sssss', 'sssssss', 'sssssssssssssssssssssssssssss']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sssssssssssssssssssssssssssss",words = ['s', 'ss', 'sss', 'sssss', 'sssssss', 'sssssssssssssssssssssssssssss']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnooouuuuuuuuu",words = ['no', 'noon', 'nou', 'noou', 'noonnouuuu', 'nnoooouuuuuuuu', 'nnooouuuuuuuuu', 'nnnooouuuuuuuuu']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnooouuuuuuuuu",words = ['no', 'noon', 'nou', 'noou', 'noonnouuuu', 'nnoooouuuuuuuu', 'nnooouuuuuuuuu', 'nnnooouuuuuuuuu']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",words = ['aabbccc', 'aaabccc', 'aaabbbcc', 'aabbbccc', 'aaabbbccccc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",words = ['aabbccc', 'aaabccc', 'aaabbbcc', 'aabbbccc', 'aaabbbccccc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd",words = ['ab', 'aabbccddd', 'aabbbcccddd', 'aaabbbcccdd', 'aaabbbcccd']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd",words = ['ab', 'aabbccddd', 'aabbbcccddd', 'aaabbbcccdd', 'aaabbbcccd']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",words = ['aabbccdd', 'aaabbbcccddd', 'aaaabbbbccccdddd', 'aabbbbccccdddd', 'aaaabbbcccdddd']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",words = ['aabbccdd', 'aaabbbcccddd', 'aaaabbbbccccdddd', 'aabbbbccccdddd', 'aaaabbbcccdddd']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqqqqqqq",words = ['q', 'qq', 'qqq', 'qqqq', 'qqqqq', 'qqqqqq', 'qqqqqqqq', 'qqqqqqqqqqqqqqqqq']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqqqqqqq",words = ['q', 'qq', 'qqq', 'qqqq', 'qqqqq', 'qqqqqq', 'qqqqqqqq', 'qqqqqqqqqqqqqqqqq']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxxyyyzzz",words = ['xyzz', 'xxyyz', 'xxyyzz', 'xxxyyyzzz', 'xxxyyzzz', 'xxxxyyzzz', 'xxxyyyyzzz']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxxyyyzzz",words = ['xyzz', 'xxyyz', 'xxyyzz', 'xxxyyyzzz', 'xxxyyzzz', 'xxxxyyzzz', 'xxxyyyyzzz']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbbbccccdddd",words = ['abc', 'abcd', 'abbc', 'abcdd', 'abbbbbccccdddd']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbbbccccdddd",words = ['abc', 'abcd', 'abbc', 'abcdd', 'abbbbbccccdddd']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",words = ['aabbbccc', 'aaaaaaaaabbbbbbbbbbcccccccc', 'aaaaaaaaabbbbbbbbcccccccccc', 'aaaaaaaaaabbbbbbbbbbcccccc', 'aaaaaaaaaabbbbbbbbbbccccccccccc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",words = ['aabbbccc', 'aaaaaaaaabbbbbbbbbbcccccccc', 'aaaaaaaaabbbbbbbbcccccccccc', 'aaaaaaaaaabbbbbbbbbbcccccc', 'aaaaaaaaaabbbbbbbbbbccccccccccc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississiissippii",words = ['mississippi', 'mississiippii', 'mississsippii', 'mississssippiii', 'mississssiiiiippiii']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississiissippii",words = ['mississippi', 'mississiippii', 'mississsippii', 'mississssippiii', 'mississssiiiiippiii']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzxyzzzzzzzzzxyzzzzzzzzz",words = ['xyzyxzy', 'xyzzzxyzzzxyzzz', 'xyzzzzxyzzzzxyzzzz', 'xyzzzzzzzzxyzzzzzzzzxyzzzzzzzz', 'xyzzzzzzzzzxyzzzzzzzzxzzzzzzzzzz']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzxyzzzzzzzzzxyzzzzzzzzz",words = ['xyzyxzy', 'xyzzzxyzzzxyzzz', 'xyzzzzxyzzzzxyzzzz', 'xyzzzzzzzzxyzzzzzzzzxyzzzzzzzz', 'xyzzzzzzzzzxyzzzzzzzzxzzzzzzzzzz']) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aaabaaa",words = ['aa', 'aaa', 'aaaa', 'aabaaa']) == 1
    assert candidate(s = "aaabaaa",words = ['aaa', 'aab', 'aaaaa', 'aaabaa', 'aaaba']) == 2
    assert candidate(s = "abcd",words = ['abc', 'abcd', 'abdc', 'aabbccdd']) == 1
    assert candidate(s = "abcd",words = ['abc', 'abcd', 'abcde']) == 1
    assert candidate(s = "aaabbbcccddd",words = ['aabbccddd', 'aabbbcccddd', 'aabbbcccdd']) == 3
    assert candidate(s = "a",words = ['a', 'aa', 'aaa', 'aaaa']) == 1
    assert candidate(s = "aabbcc",words = ['aabbcc', 'aabbc', 'aaabc']) == 1
    assert candidate(s = "abcd",words = ['aabbccdd', 'abccdd', 'abbbccdd', 'aabbcccddd']) == 0
    assert candidate(s = "heeellooo",words = ['hello', 'hi', 'helo']) == 1
    assert candidate(s = "aaabaaa",words = ['aab', 'aaab', 'aaaab', 'aaaba', 'aaaaaaab']) == 1
    assert candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde']) == 1
    assert candidate(s = "aaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 3
    assert candidate(s = "abcd",words = ['abc', 'abcd', 'abcde', 'ab', 'a']) == 1
    assert candidate(s = "aaabbb",words = ['aabb', 'aabbbb', 'aaabbbb']) == 1
    assert candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde', 'aabbccdd']) == 1
    assert candidate(s = "zzzzzyyyyy",words = ['zzyy', 'zy', 'zyy']) == 3
    assert candidate(s = "heeellloooopppp",words = ['helloppp', 'heellooppp', 'helooppp', 'helllopppp', 'heeelllooooooo', 'hello']) == 4
    assert candidate(s = "ttttuuuuuuuuuuuuvvv",words = ['tuv', 'tttuuuuuuuuuuvvv', 'ttttuuuuuuuuuuu', 'ttttuuuuuuuuuvv', 'ttttuuuuuuuuuuuuv']) == 4
    assert candidate(s = "heeeloooooo",words = ['hello', 'heeellooo', 'helllooo', 'heellooo', 'heeelloo']) == 0
    assert candidate(s = "aaaabbbbcccc",words = ['aabbcc', 'aaabbbcccc', 'aaaabbbbccc', 'aaaabbbcccc', 'aaaaabbbbcccc']) == 4
    assert candidate(s = "aaaabbbbccccddddeeee",words = ['aabcd', 'abbbcd', 'abccde', 'abcde', 'aaaaabbbbccccddddeee']) == 2
    assert candidate(s = "mmmmnnnnnnoooopppppp",words = ['mnop', 'mmnnnnoooppp', 'mmmmmnnnnnnnoooooopppppp', 'mmnnoopp', 'mmnnoooopppp']) == 4
    assert candidate(s = "xxxxxyyyyyyzzzzzz",words = ['xyzz', 'xxxyyyyzzz', 'xxxxxyyyzzzzz', 'xxxxxyyyyyyzzzz', 'xxxxxyyyyyyzzzzzz']) == 5
    assert candidate(s = "llllaaaabbbbccccddddeeeee",words = ['laabcd', 'labbbccddeee', 'labcde', 'laaaabbbbccccddddeee', 'lbbbcccddddeeee']) == 3
    assert candidate(s = "abbbcccddd",words = ['abc', 'abbc', 'abbcc', 'abbbcccd', 'abbbcccddd', 'abbbcccdd', 'abbbccccd', 'abbbccccdd']) == 3
    assert candidate(s = "mmmmnnnnoooopppp",words = ['mno', 'mmnnnnooooppp', 'mmmmnnnnoooop', 'mmmmnnnnoooopppp', 'mmmmnnnnoooppp']) == 4
    assert candidate(s = "heeellloooowooorlddd",words = ['helo', 'hello', 'helooworld', 'heeellooworld', 'heeelllooooowooorlddd']) == 2
    assert candidate(s = "mmmmmmmnnnnnnn",words = ['mmnn', 'mmmnnn', 'mmmmnnnn', 'mmmmmn', 'mmmmnn', 'mmmmmnnn', 'mmmmmmnnnnn', 'mmmmmmnnnn']) == 8
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zzzzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbbccddeeefffgghhhiiiijjjkkklllmmmnnnooooppppqqqqrrrrsssss', 'aabbccddeeefffgggiiiijjjkkklllmmmnnnoooopppqqqqrrrrrrsssss', 'aabbccddeeffgghhiijjkkklllmmmmmnnnnnoooooopppppqqqqqqrrrrrrssssss']) == 1
    assert candidate(s = "xyzzzzzyyyyyyyy",words = ['xyz', 'xyyz', 'xyzz', 'xyzzz', 'xyzzzz', 'xyzzzzzyyyyy', 'xyzzzzzyyyyyy', 'xyzzzzzyyyyyyyy']) == 3
    assert candidate(s = "zzzzzzzyyyyyyy",words = ['zzzyyyy', 'zzzzzyyy', 'zzzyyyyyyy', 'zzzzzzzzyy', 'zyyyyyyy']) == 4
    assert candidate(s = "mississippiiii",words = ['mississippi', 'missisiiippi', 'mississippiiiii', 'missisipi', 'misisipi']) == 1
    assert candidate(s = "xxyyzzzz",words = ['xxyyz', 'xxyyzz', 'xxxyyyzzzz', 'xxyyzzz', 'xyzzz']) == 3
    assert candidate(s = "aabbccccddddeeeffggg",words = ['aabbccddeeffg', 'aabbcccddddeffgg', 'aabbbccccddddeeeffggg', 'aabbbcccddddeeeffgg', 'aabbccccdddddeeeffggg']) == 2
    assert candidate(s = "xxxxxxyyyyyyzzzzzz",words = ['xyzz', 'xyzzz', 'xyyz', 'xxxyyyyzzz', 'xxxxxyyyyyyzzzzzz']) == 5
    assert candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",words = ['qq', 'qqq', 'qqqq', 'qqqqqq', 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq']) == 4
    assert candidate(s = "ttttttttttttuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvvv",words = ['tuv', 'ttuuuvvv', 'ttttuuuuuuuvvvvvvv', 'tttuuuuuuvvvvvvvvvv', 'ttttuuuuuuuuuuuvvvvvvvvvvvvvvvvvv']) == 5
    assert candidate(s = "ppppqqqqrrrrssss",words = ['pqrst', 'pqrs', 'ppqrs', 'ppqqrrss', 'ppqqqrrrssss', 'ppqqqqrrrrsssss']) == 4
    assert candidate(s = "helloooooworlddddd",words = ['hellooworld', 'hellooworlddd', 'hellllooworld', 'helloooworldddddd', 'hellooooooworlddddd']) == 2
    assert candidate(s = "mississippiissi",words = ['mississippissi', 'misisipi', 'mississippi', 'mississsippi', 'mississippiii']) == 0
    assert candidate(s = "aabbccddeee",words = ['abcde', 'aabbcdeee', 'aaabbbcccdddeee', 'aabbccdde', 'aabccdeee']) == 1
    assert candidate(s = "ppppqqqqrrrssss",words = ['pqr', 'ppqqrrsss', 'pppqqqrrrrssss', 'ppqqrrsssss', 'ppqqrrr']) == 1
    assert candidate(s = "abcdefghijklllllmnopqrstuvwxyz",words = ['abcdefghijklmopqrstuvwxyz', 'abcdefghijklllmmnopqrstuvwxyz', 'abcdefghijkllllmnopqrstuvwxyz', 'abcdefghijklllllmnopqrstuvwxy', 'abcdefghijklllllmnopqrstuvwxyz']) == 2
    assert candidate(s = "hhheeelllllooooworrlldd",words = ['helloworld', 'hhhellooooworld', 'hheeellllllooooworld', 'hellooworld', 'hheellooworl']) == 0
    assert candidate(s = "ssssaaafffff",words = ['saff', 'ssaff', 'ssaaaff', 'ssaaaafff', 'ssaaaaaffff', 'ssssaaaafffff']) == 3
    assert candidate(s = "abcdefghijjjjjjjklmnopqrstuvwxyz",words = ['abcdefghijklnopqrstuvwxyz', 'abcdefghijjjklmnopqrstuvwxyz', 'abcdefghijjjjjjklmnopqrstuvwxyz', 'abcdefghijjjjjjjklmnopqrstuv', 'abcdefghijjjjjjjmnopqrstuvwxyz']) == 2
    assert candidate(s = "abcdefghiiiiijjjjjjkkkkkkk",words = ['abcdefghijjk', 'abcdefghijk', 'abcdefghiiijjjjkk', 'abcdefghiiijjjjjjkkkkk', 'abcdefghiiijjjjjjkkkkkkk']) == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abcdefghijklmnopqrstuvwxyzz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzzz', 'abcdefghijklmnopqrstuvwxyzzzz', 'abcdefghijklmnopqrstuvwxyzzzzz']) == 0
    assert candidate(s = "aaaaaaabbbbcccdd",words = ['aabbbccdd', 'aaabbbcccdd', 'aaaabbbcccdd', 'aaaaabbbcccdd', 'aaaaaaabbbcccdd', 'aaaaaaabbbcccd', 'aaaaaaabbbbccdd', 'aaaaaaabbbbcccdd']) == 7
    assert candidate(s = "qqqqqqqqqqqwwweeeerrrrttttt",words = ['qqqqqqqwwwreeeeeerttt', 'qqqwwwreeert', 'qqqqqqqwwwreeerrttt', 'qqqqqqqqqqqwwweeeerrrtttt', 'qqqqqqqwwweeeerrrtttt']) == 2
    assert candidate(s = "abcdeeeeef",words = ['abcdeeef', 'abcdeeeef', 'abcdeeeeeef', 'abcdfeeeef', 'abcdef']) == 3
    assert candidate(s = "abcdefghijjkkklllllmmmmmmmnnnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz",words = ['abcdefghijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'abcdefghijjkkkllllmmmmnnnnooooopppqqqqrrrrsssssttttuvvvvwwwwxxyyyyzzzz', 'abcdefghijjkkklllllmmmmmmnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz']) == 3
    assert candidate(s = "abbbccdddd",words = ['abcdd', 'abbbccdd', 'abbbccccdd', 'abbbccdddd', 'aabbccddd']) == 2
    assert candidate(s = "ppppqqqqrrr",words = ['pqr', 'pppqqrr', 'ppqqqrrr', 'pppqqqqrrr', 'ppppqqqrrr']) == 5
    assert candidate(s = "aaaaaabbcccddeeeee",words = ['aabccddee', 'aaabbbcccdddeeee', 'aaaabbbcccdddeee', 'aaaaabbcccddeeee', 'aaaaabbbbccccddeeeeee']) == 1
    assert candidate(s = "llllllmmmnnnnoo",words = ['lmno', 'lllmmnno', 'lllllmmnnnoo', 'lllmmmnnnnoo', 'llllllmmmnnno']) == 2
    assert candidate(s = "aabbccddeeefffggg",words = ['aabbccddeefffggg', 'aabbbcccdddeeefffggg', 'aabbccddeeeffffgggg', 'aabbccddeeeffg', 'aabbcddfeeeffggg']) == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz']) == 4
    assert candidate(s = "ttrrreeee",words = ['tree', 'ttrree', 'ttrreee', 'ttreee', 'ttrre', 'ttre', 'trreee', 'ttreere']) == 5
    assert candidate(s = "mmmaaa",words = ['maa', 'maaaa', 'mmmaaa', 'mmma', 'mmmaaaam']) == 3
    assert candidate(s = "sssssssssssssssssssssssssssss",words = ['s', 'ss', 'sss', 'sssss', 'sssssss', 'sssssssssssssssssssssssssssss']) == 6
    assert candidate(s = "nnnnooouuuuuuuuu",words = ['no', 'noon', 'nou', 'noou', 'noonnouuuu', 'nnoooouuuuuuuu', 'nnooouuuuuuuuu', 'nnnooouuuuuuuuu']) == 4
    assert candidate(s = "aaabbbccc",words = ['aabbccc', 'aaabccc', 'aaabbbcc', 'aabbbccc', 'aaabbbccccc']) == 4
    assert candidate(s = "aaabbbcccddd",words = ['ab', 'aabbccddd', 'aabbbcccddd', 'aaabbbcccdd', 'aaabbbcccd']) == 4
    assert candidate(s = "aaaabbbbccccdddd",words = ['aabbccdd', 'aaabbbcccddd', 'aaaabbbbccccdddd', 'aabbbbccccdddd', 'aaaabbbcccdddd']) == 5
    assert candidate(s = "qqqqqqqqqqqqqqqqq",words = ['q', 'qq', 'qqq', 'qqqq', 'qqqqq', 'qqqqqq', 'qqqqqqqq', 'qqqqqqqqqqqqqqqqq']) == 8
    assert candidate(s = "xxxyyyzzz",words = ['xyzz', 'xxyyz', 'xxyyzz', 'xxxyyyzzz', 'xxxyyzzz', 'xxxxyyzzz', 'xxxyyyyzzz']) == 5
    assert candidate(s = "abbbbbccccdddd",words = ['abc', 'abcd', 'abbc', 'abcdd', 'abbbbbccccdddd']) == 3
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",words = ['aabbbccc', 'aaaaaaaaabbbbbbbbbbcccccccc', 'aaaaaaaaabbbbbbbbcccccccccc', 'aaaaaaaaaabbbbbbbbbbcccccc', 'aaaaaaaaaabbbbbbbbbbccccccccccc']) == 4
    assert candidate(s = "mississiissippii",words = ['mississippi', 'mississiippii', 'mississsippii', 'mississssippiii', 'mississssiiiiippiii']) == 0
    assert candidate(s = "xyzzzzzzzzzxyzzzzzzzzzxyzzzzzzzzz",words = ['xyzyxzy', 'xyzzzxyzzzxyzzz', 'xyzzzzxyzzzzxyzzzz', 'xyzzzzzzzzxyzzzzzzzzxyzzzzzzzz', 'xyzzzzzzzzzxyzzzzzzzzxzzzzzzzzzz']) == 3


