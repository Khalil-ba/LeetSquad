def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbaa', 'abc', 'cba']) == [[0, 1], [1, 0], [2, 3], [3, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbaa', 'abc', 'cba']) == [[0, 1], [1, 0], [2, 3], [3, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['bat', 'tab', 'cat']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['bat', 'tab', 'cat']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'cba', 'bca', 'xyz', 'zyx']) == [[0, 1], [1, 0], [3, 4], [4, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'cba', 'bca', 'xyz', 'zyx']) == [[0, 1], [1, 0], [3, 4], [4, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abba', 'a', 'abc', 'cba']) == [[2, 3], [3, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abba', 'a', 'abc', 'cba']) == [[2, 3], [3, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'dcba', '', 'cba', 'abc']) == [[0, 3], [0, 1], [4, 1], [1, 0], [3, 4], [4, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'dcba', '', 'cba', 'abc']) == [[0, 3], [0, 1], [4, 1], [1, 0], [3, 4], [4, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abba', 'a', 'abc', 'cba', 'bbaa', 'aba']) == [[2, 3], [3, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abba', 'a', 'abc', 'cba', 'bbaa', 'aba']) == [[2, 3], [3, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'aaa', 'bbb', 'aaaa', 'bbbb']) == [[0, 2], [2, 0], [1, 3], [3, 1], [2, 4], [4, 0], [0, 4], [4, 2], [3, 5], [5, 1], [1, 5], [5, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'aaa', 'bbb', 'aaaa', 'bbbb']) == [[0, 2], [2, 0], [1, 3], [3, 1], [2, 4], [4, 0], [0, 4], [4, 2], [3, 5], [5, 1], [1, 5], [5, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'b', 'aaa', 'bb']) == [[0, 2], [2, 0], [3, 1], [1, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'b', 'aaa', 'bb']) == [[0, 2], [2, 0], [3, 1], [1, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', '']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', '']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'dcba', 'lls', 's', 'sssll']) == [[0, 1], [1, 0], [3, 2], [2, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'dcba', 'lls', 's', 'sssll']) == [[0, 1], [1, 0], [3, 2], [2, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'cba', 'bba', 'aab', 'aaa']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'cba', 'bba', 'aab', 'aaa']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', '']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', '']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tacocat', 'racecar', 'banana', 'ananab', 'civic']) == [[2, 3], [3, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tacocat', 'racecar', 'banana', 'ananab', 'civic']) == [[2, 3], [3, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbaa', 'abab', 'baba', 'aaaa', 'bbbb']) == [[0, 1], [1, 0], [2, 3], [3, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbaa', 'abab', 'baba', 'aaaa', 'bbbb']) == [[0, 1], [1, 0], [2, 3], [3, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'dcba']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'dcba']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dcb', 'abcd', 'cba', 'abc', 'bca', 'bac', 'cab', 'a']) == [[0, 1], [1, 2], [2, 3], [3, 2], [5, 6], [6, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dcb', 'abcd', 'cba', 'abc', 'bca', 'bac', 'cab', 'a']) == [[0, 1], [1, 2], [2, 3], [3, 2], [5, 6], [6, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abab', 'baba', 'abba', 'baab', 'aaaa', 'bbbb']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abab', 'baba', 'abba', 'baab', 'aaaa', 'bbbb']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abba', 'a', 'baa', 'b']) == [[2, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abba', 'a', 'baa', 'b']) == [[2, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'dcba', 'lls', 's', 'sssll', 'ddsssll']) == [[0, 1], [1, 0], [3, 2], [2, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'dcba', 'lls', 's', 'sssll', 'ddsssll']) == [[0, 1], [1, 0], [3, 2], [2, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'abc', 'aba', 'xyz', 'zyx']) == [[3, 4], [4, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'abc', 'aba', 'xyz', 'zyx']) == [[3, 4], [4, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['', 'a', 'b', 'c', 'd']) == [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['', 'a', 'b', 'c', 'd']) == [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbaa', 'aaaa', 'abba', 'baab']) == [[0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbaa', 'aaaa', 'abba', 'baab']) == [[0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dcb', 'abcd', 'cba', 'cbcd']) == [[0, 1], [1, 2], [0, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dcb', 'abcd', 'cba', 'cbcd']) == [[0, 1], [1, 2], [0, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zxcvbnm', 'mnbvcxz', 'asdfghjkl', 'lkjhgfdsa', 'qwertyuiop', 'poiuytrewq', '1234567890', '0987654321', 'abcdefghij', 'jihgfedcba', 'klmnopqrst', 'tsrqponmlk', 'uvwxyz', 'zyxwvut', 'nopqrstu', 'utsrqpon', 'abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq', 'yz', 'zy', 'abcd', 'dcba', 'ab', 'ba', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [13, 12], [14, 15], [15, 14], [16, 17], [17, 16], [18, 19], [19, 18], [20, 21], [21, 20], [22, 52], [53, 22], [22, 23], [23, 53], [52, 23], [23, 22], [24, 25], [25, 24], [26, 28], [29, 26], [26, 27], [27, 29], [28, 27], [27, 26]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zxcvbnm', 'mnbvcxz', 'asdfghjkl', 'lkjhgfdsa', 'qwertyuiop', 'poiuytrewq', '1234567890', '0987654321', 'abcdefghij', 'jihgfedcba', 'klmnopqrst', 'tsrqponmlk', 'uvwxyz', 'zyxwvut', 'nopqrstu', 'utsrqpon', 'abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq', 'yz', 'zy', 'abcd', 'dcba', 'ab', 'ba', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [13, 12], [14, 15], [15, 14], [16, 17], [17, 16], [18, 19], [19, 18], [20, 21], [21, 20], [22, 52], [53, 22], [22, 23], [23, 53], [52, 23], [23, 22], [24, 25], [25, 24], [26, 28], [29, 26], [26, 27], [27, 29], [28, 27], [27, 26]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6], [7, 0], [6, 7], [7, 1], [5, 7], [7, 2], [4, 7], [7, 3], [3, 7], [7, 4], [2, 7], [7, 5], [1, 7], [7, 6], [0, 7], [8, 0], [7, 8], [8, 1], [6, 8], [8, 2], [5, 8], [8, 3], [4, 8], [8, 4], [3, 8], [8, 5], [2, 8], [8, 6], [1, 8], [8, 7], [0, 8], [9, 0], [8, 9], [9, 1], [7, 9], [9, 2], [6, 9], [9, 3], [5, 9], [9, 4], [4, 9], [9, 5], [3, 9], [9, 6], [2, 9], [9, 7], [1, 9], [9, 8], [0, 9], [10, 0], [9, 10], [10, 1], [8, 10], [10, 2], [7, 10], [10, 3], [6, 10], [10, 4], [5, 10], [10, 5], [4, 10], [10, 6], [3, 10], [10, 7], [2, 10], [10, 8], [1, 10], [10, 9], [0, 10], [11, 0], [10, 11], [11, 1], [9, 11], [11, 2], [8, 11], [11, 3], [7, 11], [11, 4], [6, 11], [11, 5], [5, 11], [11, 6], [4, 11], [11, 7], [3, 11], [11, 8], [2, 11], [11, 9], [1, 11], [11, 10], [0, 11], [12, 0], [11, 12], [12, 1], [10, 12], [12, 2], [9, 12], [12, 3], [8, 12], [12, 4], [7, 12], [12, 5], [6, 12], [12, 6], [5, 12], [12, 7], [4, 12], [12, 8], [3, 12], [12, 9], [2, 12], [12, 10], [1, 12], [12, 11], [0, 12], [13, 0], [12, 13], [13, 1], [11, 13], [13, 2], [10, 13], [13, 3], [9, 13], [13, 4], [8, 13], [13, 5], [7, 13], [13, 6], [6, 13], [13, 7], [5, 13], [13, 8], [4, 13], [13, 9], [3, 13], [13, 10], [2, 13], [13, 11], [1, 13], [13, 12], [0, 13], [14, 0], [13, 14], [14, 1], [12, 14], [14, 2], [11, 14], [14, 3], [10, 14], [14, 4], [9, 14], [14, 5], [8, 14], [14, 6], [7, 14], [14, 7], [6, 14], [14, 8], [5, 14], [14, 9], [4, 14], [14, 10], [3, 14], [14, 11], [2, 14], [14, 12], [1, 14], [14, 13], [0, 14], [15, 0], [14, 15], [15, 1], [13, 15], [15, 2], [12, 15], [15, 3], [11, 15], [15, 4], [10, 15], [15, 5], [9, 15], [15, 6], [8, 15], [15, 7], [7, 15], [15, 8], [6, 15], [15, 9], [5, 15], [15, 10], [4, 15], [15, 11], [3, 15], [15, 12], [2, 15], [15, 13], [1, 15], [15, 14], [0, 15], [16, 0], [15, 16], [16, 1], [14, 16], [16, 2], [13, 16], [16, 3], [12, 16], [16, 4], [11, 16], [16, 5], [10, 16], [16, 6], [9, 16], [16, 7], [8, 16], [16, 8], [7, 16], [16, 9], [6, 16], [16, 10], [5, 16], [16, 11], [4, 16], [16, 12], [3, 16], [16, 13], [2, 16], [16, 14], [1, 16], [16, 15], [0, 16], [17, 0], [16, 17], [17, 1], [15, 17], [17, 2], [14, 17], [17, 3], [13, 17], [17, 4], [12, 17], [17, 5], [11, 17], [17, 6], [10, 17], [17, 7], [9, 17], [17, 8], [8, 17], [17, 9], [7, 17], [17, 10], [6, 17], [17, 11], [5, 17], [17, 12], [4, 17], [17, 13], [3, 17], [17, 14], [2, 17], [17, 15], [1, 17], [17, 16], [0, 17], [18, 0], [17, 18], [18, 1], [16, 18], [18, 2], [15, 18], [18, 3], [14, 18], [18, 4], [13, 18], [18, 5], [12, 18], [18, 6], [11, 18], [18, 7], [10, 18], [18, 8], [9, 18], [18, 9], [8, 18], [18, 10], [7, 18], [18, 11], [6, 18], [18, 12], [5, 18], [18, 13], [4, 18], [18, 14], [3, 18], [18, 15], [2, 18], [18, 16], [1, 18], [18, 17], [0, 18], [19, 0], [18, 19], [19, 1], [17, 19], [19, 2], [16, 19], [19, 3], [15, 19], [19, 4], [14, 19], [19, 5], [13, 19], [19, 6], [12, 19], [19, 7], [11, 19], [19, 8], [10, 19], [19, 9], [9, 19], [19, 10], [8, 19], [19, 11], [7, 19], [19, 12], [6, 19], [19, 13], [5, 19], [19, 14], [4, 19], [19, 15], [3, 19], [19, 16], [2, 19], [19, 17], [1, 19], [19, 18], [0, 19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6], [7, 0], [6, 7], [7, 1], [5, 7], [7, 2], [4, 7], [7, 3], [3, 7], [7, 4], [2, 7], [7, 5], [1, 7], [7, 6], [0, 7], [8, 0], [7, 8], [8, 1], [6, 8], [8, 2], [5, 8], [8, 3], [4, 8], [8, 4], [3, 8], [8, 5], [2, 8], [8, 6], [1, 8], [8, 7], [0, 8], [9, 0], [8, 9], [9, 1], [7, 9], [9, 2], [6, 9], [9, 3], [5, 9], [9, 4], [4, 9], [9, 5], [3, 9], [9, 6], [2, 9], [9, 7], [1, 9], [9, 8], [0, 9], [10, 0], [9, 10], [10, 1], [8, 10], [10, 2], [7, 10], [10, 3], [6, 10], [10, 4], [5, 10], [10, 5], [4, 10], [10, 6], [3, 10], [10, 7], [2, 10], [10, 8], [1, 10], [10, 9], [0, 10], [11, 0], [10, 11], [11, 1], [9, 11], [11, 2], [8, 11], [11, 3], [7, 11], [11, 4], [6, 11], [11, 5], [5, 11], [11, 6], [4, 11], [11, 7], [3, 11], [11, 8], [2, 11], [11, 9], [1, 11], [11, 10], [0, 11], [12, 0], [11, 12], [12, 1], [10, 12], [12, 2], [9, 12], [12, 3], [8, 12], [12, 4], [7, 12], [12, 5], [6, 12], [12, 6], [5, 12], [12, 7], [4, 12], [12, 8], [3, 12], [12, 9], [2, 12], [12, 10], [1, 12], [12, 11], [0, 12], [13, 0], [12, 13], [13, 1], [11, 13], [13, 2], [10, 13], [13, 3], [9, 13], [13, 4], [8, 13], [13, 5], [7, 13], [13, 6], [6, 13], [13, 7], [5, 13], [13, 8], [4, 13], [13, 9], [3, 13], [13, 10], [2, 13], [13, 11], [1, 13], [13, 12], [0, 13], [14, 0], [13, 14], [14, 1], [12, 14], [14, 2], [11, 14], [14, 3], [10, 14], [14, 4], [9, 14], [14, 5], [8, 14], [14, 6], [7, 14], [14, 7], [6, 14], [14, 8], [5, 14], [14, 9], [4, 14], [14, 10], [3, 14], [14, 11], [2, 14], [14, 12], [1, 14], [14, 13], [0, 14], [15, 0], [14, 15], [15, 1], [13, 15], [15, 2], [12, 15], [15, 3], [11, 15], [15, 4], [10, 15], [15, 5], [9, 15], [15, 6], [8, 15], [15, 7], [7, 15], [15, 8], [6, 15], [15, 9], [5, 15], [15, 10], [4, 15], [15, 11], [3, 15], [15, 12], [2, 15], [15, 13], [1, 15], [15, 14], [0, 15], [16, 0], [15, 16], [16, 1], [14, 16], [16, 2], [13, 16], [16, 3], [12, 16], [16, 4], [11, 16], [16, 5], [10, 16], [16, 6], [9, 16], [16, 7], [8, 16], [16, 8], [7, 16], [16, 9], [6, 16], [16, 10], [5, 16], [16, 11], [4, 16], [16, 12], [3, 16], [16, 13], [2, 16], [16, 14], [1, 16], [16, 15], [0, 16], [17, 0], [16, 17], [17, 1], [15, 17], [17, 2], [14, 17], [17, 3], [13, 17], [17, 4], [12, 17], [17, 5], [11, 17], [17, 6], [10, 17], [17, 7], [9, 17], [17, 8], [8, 17], [17, 9], [7, 17], [17, 10], [6, 17], [17, 11], [5, 17], [17, 12], [4, 17], [17, 13], [3, 17], [17, 14], [2, 17], [17, 15], [1, 17], [17, 16], [0, 17], [18, 0], [17, 18], [18, 1], [16, 18], [18, 2], [15, 18], [18, 3], [14, 18], [18, 4], [13, 18], [18, 5], [12, 18], [18, 6], [11, 18], [18, 7], [10, 18], [18, 8], [9, 18], [18, 9], [8, 18], [18, 10], [7, 18], [18, 11], [6, 18], [18, 12], [5, 18], [18, 13], [4, 18], [18, 14], [3, 18], [18, 15], [2, 18], [18, 16], [1, 18], [18, 17], [0, 18], [19, 0], [18, 19], [19, 1], [17, 19], [19, 2], [16, 19], [19, 3], [15, 19], [19, 4], [14, 19], [19, 5], [13, 19], [19, 6], [12, 19], [19, 7], [11, 19], [19, 8], [10, 19], [19, 9], [9, 19], [19, 10], [8, 19], [19, 11], [7, 19], [19, 12], [6, 19], [19, 13], [5, 19], [19, 14], [4, 19], [19, 15], [3, 19], [19, 16], [2, 19], [19, 17], [1, 19], [19, 18], [0, 19]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', '', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [[0, 3], [3, 0], [1, 3], [3, 1], [2, 3], [3, 2], [4, 3], [3, 4], [5, 3], [3, 5], [6, 3], [3, 6], [7, 3], [3, 7], [8, 3], [3, 8], [9, 3], [3, 9], [10, 3], [3, 10], [11, 3], [3, 11], [12, 3], [3, 12], [13, 3], [3, 13], [14, 3], [3, 14], [15, 3], [3, 15], [16, 3], [3, 16], [17, 3], [3, 17], [18, 3], [3, 18], [19, 3], [3, 19], [20, 3], [3, 20], [21, 3], [3, 21], [22, 3], [3, 22], [23, 3], [3, 23], [24, 3], [3, 24], [25, 3], [3, 25], [26, 3], [3, 26]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', '', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [[0, 3], [3, 0], [1, 3], [3, 1], [2, 3], [3, 2], [4, 3], [3, 4], [5, 3], [3, 5], [6, 3], [3, 6], [7, 3], [3, 7], [8, 3], [3, 8], [9, 3], [3, 9], [10, 3], [3, 10], [11, 3], [3, 11], [12, 3], [3, 12], [13, 3], [3, 13], [14, 3], [3, 14], [15, 3], [3, 15], [16, 3], [3, 16], [17, 3], [3, 17], [18, 3], [3, 18], [19, 3], [3, 19], [20, 3], [3, 20], [21, 3], [3, 21], [22, 3], [3, 22], [23, 3], [3, 23], [24, 3], [3, 24], [25, 3], [3, 25], [26, 3], [3, 26]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'civic', 'level', 'rotor', 'deified', 'redder', 'repaper', 'refer', 'reviver', 'reviled']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'civic', 'level', 'rotor', 'deified', 'redder', 'repaper', 'refer', 'reviver', 'reviled']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abba', 'baab', 'aabb', 'bbaa', 'aaaa', 'aaab', 'abaa', 'baaa', 'bbba', 'baba']) == [[2, 3], [3, 2], [5, 7], [7, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abba', 'baab', 'aabb', 'bbaa', 'aaaa', 'aaab', 'abaa', 'baaa', 'bbba', 'baba']) == [[2, 3], [3, 2], [5, 7], [7, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == [[1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == [[1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['race', 'car', '', '', 'racecar', 'ecar', 'cec', 'ceccec']) == [[0, 1], [0, 5], [2, 3], [4, 3], [3, 4], [5, 0], [6, 3], [3, 6], [7, 3], [7, 6], [6, 7], [3, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['race', 'car', '', '', 'racecar', 'ecar', 'cec', 'ceccec']) == [[0, 1], [0, 5], [2, 3], [4, 3], [3, 4], [5, 0], [6, 3], [3, 6], [7, 3], [7, 6], [6, 7], [3, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcd', 'dcbaabcd', 'cdabcd', 'dcbabcd', 'abcbabc', 'cbababc', 'abcabcba', 'bcbabcba', 'cdcdcdcd', 'dcddcddc', 'abcd', 'dcba', 'cd', 'dc', 'abcdabc', 'dcbaabc', 'abc', 'cba']) == [[15, 1], [6, 17], [4, 7], [12, 9], [10, 17], [10, 11], [16, 11], [11, 10], [12, 13], [13, 12], [16, 17], [17, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcd', 'dcbaabcd', 'cdabcd', 'dcbabcd', 'abcbabc', 'cbababc', 'abcabcba', 'bcbabcba', 'cdcdcdcd', 'dcddcddc', 'abcd', 'dcba', 'cd', 'dc', 'abcdabc', 'dcbaabc', 'abc', 'cba']) == [[15, 1], [6, 17], [4, 7], [12, 9], [10, 17], [10, 11], [16, 11], [11, 10], [12, 13], [13, 12], [16, 17], [17, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['race', 'car', 'cec', 'dec', 'ded', 'level', 'deified', 'civic']) == [[0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['race', 'car', 'cec', 'dec', 'ded', 'level', 'deified', 'civic']) == [[0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'fgh', 'hgf', 'xyz', 'zyx', 'ijk', 'kji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvw', 'wvu']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [12, 13], [13, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'fgh', 'hgf', 'xyz', 'zyx', 'ijk', 'kji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvw', 'wvu']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [12, 13], [13, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['race', 'ecar', 'car', 'racecar', 'carrace', 'arcec', 'cecarr', 'racecarcar']) == [[0, 2], [0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['race', 'ecar', 'car', 'racecar', 'carrace', 'arcec', 'cecarr', 'racecarcar']) == [[0, 2], [0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ccbbaa', 'abcde', 'edcba', 'abcd', 'dcba']) == [[0, 1], [1, 0], [2, 5], [2, 3], [4, 3], [3, 2], [4, 5], [5, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ccbbaa', 'abcde', 'edcba', 'abcd', 'dcba']) == [[0, 1], [1, 0], [2, 5], [2, 3], [4, 3], [3, 2], [4, 5], [5, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ccbbaa', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ccbbaa', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwuv']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwuv']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abab', 'baba', 'ab', 'ba', 'a', 'b', '', 'aba', 'bab', 'bba', 'aab', 'baa']) == [[0, 4], [8, 0], [0, 7], [5, 0], [0, 1], [1, 5], [7, 1], [1, 8], [4, 1], [1, 0], [2, 4], [5, 2], [2, 3], [3, 5], [4, 3], [3, 2], [4, 6], [6, 4], [5, 6], [6, 5], [7, 6], [2, 7], [7, 3], [6, 7], [8, 6], [3, 8], [8, 2], [6, 8], [2, 9], [4, 9], [3, 10], [5, 10], [10, 11], [11, 5], [11, 2], [11, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abab', 'baba', 'ab', 'ba', 'a', 'b', '', 'aba', 'bab', 'bba', 'aab', 'baa']) == [[0, 4], [8, 0], [0, 7], [5, 0], [0, 1], [1, 5], [7, 1], [1, 8], [4, 1], [1, 0], [2, 4], [5, 2], [2, 3], [3, 5], [4, 3], [3, 2], [4, 6], [6, 4], [5, 6], [6, 5], [7, 6], [2, 7], [7, 3], [6, 7], [8, 6], [3, 8], [8, 2], [6, 8], [2, 9], [4, 9], [3, 10], [5, 10], [10, 11], [11, 5], [11, 2], [11, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ccbbaa', 'abcabc', 'cbabca', 'bacbac', 'abacab', 'bacbac', 'cababc', 'bcaacb', 'aabb', 'bbaa', 'aabbaa', 'abbbaa', 'aaabbb', 'baaabb', 'aababb', 'abbaab', 'bababa']) == [[0, 10], [0, 1], [9, 1], [1, 0], [9, 10], [10, 9], [9, 11], [11, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ccbbaa', 'abcabc', 'cbabca', 'bacbac', 'abacab', 'bacbac', 'cababc', 'bcaacb', 'aabb', 'bbaa', 'aabbaa', 'abbbaa', 'aaabbb', 'baaabb', 'aababb', 'abbaab', 'bababa']) == [[0, 10], [0, 1], [9, 1], [1, 0], [9, 10], [10, 9], [9, 11], [11, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyxy', 'yxyx', 'yxx', 'xx', 'xyyx', 'yyxy', 'xyx', 'yyy', 'xyyxxyy', 'yyxxyyx', 'xyyyxyx', 'yyxyxxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy', 'xyyyxyy', 'yyxxyxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy', 'xyyyxyy', 'yyxxyxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy']) == [[0, 6], [0, 1], [6, 1], [1, 0], [3, 2], [8, 9], [9, 8], [12, 28], [16, 4], [20, 28], [24, 4], [32, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyxy', 'yxyx', 'yxx', 'xx', 'xyyx', 'yyxy', 'xyx', 'yyy', 'xyyxxyy', 'yyxxyyx', 'xyyyxyx', 'yyxyxxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy', 'xyyyxyy', 'yyxxyxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy', 'xyyyxyy', 'yyxxyxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy']) == [[0, 6], [0, 1], [6, 1], [1, 0], [3, 2], [8, 9], [9, 8], [12, 28], [16, 4], [20, 28], [24, 4], [32, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghijk', 'kjihgfedcba', 'abcdefghijkl', 'lkjihgfedcba', 'abcdefghijklm', 'mlkjihgfedcba', 'abcdefghijklmn', 'nmlkjihgfedcba', 'abcdefghijklmno', 'onmlkjihgfedcba', 'abcdefghijklmnop', 'ponmlkjihgfedcba', 'abcdefghijklmnopq', 'qponmlkjihgfedcba', 'abcdefghijklmnopqr', 'rponmlkjihgfedcba', 'abcdefghijklmnopqrs', 'spnmlkjihgfedcba', 'abcdefghijklmnopqrst', 'tspnmlkjihgfedcba', 'abcdefghijklmnopqrstu', 'ustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuv', 'vustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvw', 'wvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwx', 'xwvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxy', 'yxwvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14], [16, 15], [16, 17], [14, 17], [17, 16], [18, 17], [18, 19], [16, 19], [19, 18], [20, 19], [20, 21], [18, 21], [21, 20], [22, 21], [22, 23], [20, 23], [23, 22], [24, 23], [24, 25], [22, 25], [25, 24], [26, 25], [26, 27], [24, 27], [27, 26], [28, 27], [28, 29], [26, 29], [29, 28], [30, 29], [30, 31], [28, 31], [31, 30], [32, 31], [28, 33], [48, 49], [46, 49], [49, 48]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghijk', 'kjihgfedcba', 'abcdefghijkl', 'lkjihgfedcba', 'abcdefghijklm', 'mlkjihgfedcba', 'abcdefghijklmn', 'nmlkjihgfedcba', 'abcdefghijklmno', 'onmlkjihgfedcba', 'abcdefghijklmnop', 'ponmlkjihgfedcba', 'abcdefghijklmnopq', 'qponmlkjihgfedcba', 'abcdefghijklmnopqr', 'rponmlkjihgfedcba', 'abcdefghijklmnopqrs', 'spnmlkjihgfedcba', 'abcdefghijklmnopqrst', 'tspnmlkjihgfedcba', 'abcdefghijklmnopqrstu', 'ustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuv', 'vustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvw', 'wvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwx', 'xwvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxy', 'yxwvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14], [16, 15], [16, 17], [14, 17], [17, 16], [18, 17], [18, 19], [16, 19], [19, 18], [20, 19], [20, 21], [18, 21], [21, 20], [22, 21], [22, 23], [20, 23], [23, 22], [24, 23], [24, 25], [22, 25], [25, 24], [26, 25], [26, 27], [24, 27], [27, 26], [28, 27], [28, 29], [26, 29], [29, 28], [30, 29], [30, 31], [28, 31], [31, 30], [32, 31], [28, 33], [48, 49], [46, 49], [49, 48]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcba', 'bcbaa', 'cbaab', 'baabc', 'aabcd', 'bcdcb', 'cdcbc', 'dcbcd', 'cbcdc', 'bcdbc', 'abcdc']) == [[2, 3], [3, 2], [6, 8], [8, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcba', 'bcbaa', 'cbaab', 'baabc', 'aabcd', 'bcdcb', 'cdcbc', 'dcbcd', 'cbcdc', 'bcdbc', 'abcdc']) == [[2, 3], [3, 2], [6, 8], [8, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', '', '', 'abcdeedcba', 'aabcdeedcbaa', 'aaabcdeedcbaaa', 'aaaabcdeedcbaaaa', 'aaaaabcdeedcbaaaaa', 'abcdeedcbaaaaa', 'aabcdeedcbaaaaaa', 'aaabcdeedcbaaaaaaa', 'aaaabcdeedcbaaaaaaaa', 'aaaaabcdeedcbaaaaaaaaa', 'abcdeedcbaaaaaaaaaa']) == [[0, 1], [1, 0], [2, 3], [4, 3], [3, 4], [5, 3], [3, 5], [6, 3], [3, 6], [7, 3], [3, 7], [8, 3], [8, 9], [3, 8], [9, 4], [10, 5], [11, 6], [12, 7], [13, 9], [13, 8], [14, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', '', '', 'abcdeedcba', 'aabcdeedcbaa', 'aaabcdeedcbaaa', 'aaaabcdeedcbaaaa', 'aaaaabcdeedcbaaaaa', 'abcdeedcbaaaaa', 'aabcdeedcbaaaaaa', 'aaabcdeedcbaaaaaaa', 'aaaabcdeedcbaaaaaaaa', 'aaaaabcdeedcbaaaaaaaaa', 'abcdeedcbaaaaaaaaaa']) == [[0, 1], [1, 0], [2, 3], [4, 3], [3, 4], [5, 3], [3, 5], [6, 3], [3, 6], [7, 3], [3, 7], [8, 3], [8, 9], [3, 8], [9, 4], [10, 5], [11, 6], [12, 7], [13, 9], [13, 8], [14, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaba', 'abcbaca', 'abcdcba', 'abeceda', 'aabcdcbba', 'abcddcba', 'deified', 'civic', 'level', 'rotor', 'madam', 'refer', 'repaper', 'reviver', 'reviled', 'redder']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaba', 'abcbaca', 'abcdcba', 'abeceda', 'aabcdcbba', 'abcddcba', 'deified', 'civic', 'level', 'rotor', 'madam', 'refer', 'repaper', 'reviver', 'reviled', 'redder']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaba', 'acababa', 'bacabab', 'cabaaba', '', 'abacaba', 'acababa', 'bacabab', 'cabaaba']) == [[0, 4], [0, 5], [4, 0], [5, 4], [4, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaba', 'acababa', 'bacabab', 'cabaaba', '', 'abacaba', 'acababa', 'bacabab', 'cabaaba']) == [[0, 4], [0, 5], [4, 0], [5, 4], [4, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcba', 'abccba', 'abcdcba', 'abccbaa']) == [[1, 0], [7, 5], [0, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcba', 'abccba', 'abcdcba', 'abccbaa']) == [[1, 0], [7, 5], [0, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['palindrome', 'emordnilap', 'word', 'drow', 'madam', 'ada', 'radar', 'kayak', 'reviled', 'devil']) == [[0, 1], [1, 0], [2, 3], [3, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['palindrome', 'emordnilap', 'word', 'drow', 'madam', 'ada', 'radar', 'kayak', 'reviled', 'devil']) == [[0, 1], [1, 0], [2, 3], [3, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'moon', 'noontime', 'timenoon', 'time', 'emit']) == [[5, 2], [3, 5], [4, 5], [5, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'moon', 'noontime', 'timenoon', 'time', 'emit']) == [[5, 2], [3, 5], [4, 5], [5, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyx', 'yxy', 'xxyy', 'yyxx', 'xyyx', 'yxxy', 'xyxx', 'yxx', 'xxy', 'yy', 'xy', 'yx', 'x', 'y', '', 'aaa', 'bbb', 'ccc', 'aaab', 'bbba', 'aaa', 'bbbb', 'cccc', 'dddd', 'dddb', 'bbbd', 'aaa', 'bbbb', 'cccc', 'dddd', 'dddb', 'bbbd']) == [[0, 14], [10, 0], [0, 11], [14, 0], [1, 14], [11, 1], [1, 10], [14, 1], [9, 2], [2, 7], [2, 3], [8, 3], [3, 9], [3, 2], [4, 14], [14, 4], [5, 14], [7, 5], [5, 8], [14, 5], [8, 6], [6, 11], [6, 0], [12, 6], [7, 13], [7, 10], [7, 8], [11, 8], [13, 8], [8, 7], [9, 14], [9, 13], [13, 9], [14, 9], [10, 12], [13, 10], [10, 11], [11, 13], [12, 11], [11, 10], [12, 14], [14, 12], [13, 14], [14, 13], [15, 14], [15, 26], [14, 15], [16, 14], [14, 16], [17, 14], [14, 17], [18, 26], [19, 16], [20, 14], [20, 26], [14, 20], [21, 14], [16, 21], [21, 16], [21, 27], [14, 21], [22, 14], [17, 22], [22, 17], [22, 28], [14, 22], [23, 14], [23, 29], [14, 23], [25, 16], [26, 14], [14, 26], [27, 14], [16, 27], [27, 16], [14, 27], [28, 14], [17, 28], [28, 17], [14, 28], [29, 14], [14, 29], [31, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyx', 'yxy', 'xxyy', 'yyxx', 'xyyx', 'yxxy', 'xyxx', 'yxx', 'xxy', 'yy', 'xy', 'yx', 'x', 'y', '', 'aaa', 'bbb', 'ccc', 'aaab', 'bbba', 'aaa', 'bbbb', 'cccc', 'dddd', 'dddb', 'bbbd', 'aaa', 'bbbb', 'cccc', 'dddd', 'dddb', 'bbbd']) == [[0, 14], [10, 0], [0, 11], [14, 0], [1, 14], [11, 1], [1, 10], [14, 1], [9, 2], [2, 7], [2, 3], [8, 3], [3, 9], [3, 2], [4, 14], [14, 4], [5, 14], [7, 5], [5, 8], [14, 5], [8, 6], [6, 11], [6, 0], [12, 6], [7, 13], [7, 10], [7, 8], [11, 8], [13, 8], [8, 7], [9, 14], [9, 13], [13, 9], [14, 9], [10, 12], [13, 10], [10, 11], [11, 13], [12, 11], [11, 10], [12, 14], [14, 12], [13, 14], [14, 13], [15, 14], [15, 26], [14, 15], [16, 14], [14, 16], [17, 14], [14, 17], [18, 26], [19, 16], [20, 14], [20, 26], [14, 20], [21, 14], [16, 21], [21, 16], [21, 27], [14, 21], [22, 14], [17, 22], [22, 17], [22, 28], [14, 22], [23, 14], [23, 29], [14, 23], [25, 16], [26, 14], [14, 26], [27, 14], [16, 27], [27, 16], [14, 27], [28, 14], [17, 28], [28, 17], [14, 28], [29, 14], [14, 29], [31, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba', 'abcdefghij', 'jihgfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14], [16, 15], [16, 17], [14, 17], [17, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba', 'abcdefghij', 'jihgfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14], [16, 15], [16, 17], [14, 17], [17, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['amanaplanacanalpanama', 'noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['amanaplanacanalpanama', 'noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'baaa', 'baba', 'abab', 'abba']) == [[1, 2], [2, 1], [3, 4], [4, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'baaa', 'baba', 'abab', 'abba']) == [[1, 2], [2, 1], [3, 4], [4, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdexyz', 'zyxcdeba', 'mnop', 'ponm', '', 'pponm', 'mnopq', 'zyxwvutsrqp', 'rqsponmlkjihgfedcba']) == [[2, 3], [3, 2], [2, 5], [6, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdexyz', 'zyxcdeba', 'mnop', 'ponm', '', 'pponm', 'mnopq', 'zyxwvutsrqp', 'rqsponmlkjihgfedcba']) == [[2, 3], [3, 2], [2, 5], [6, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6], [7, 0], [6, 7], [7, 1], [5, 7], [7, 2], [4, 7], [7, 3], [3, 7], [7, 4], [2, 7], [7, 5], [1, 7], [7, 6], [0, 7], [8, 0], [7, 8], [8, 1], [6, 8], [8, 2], [5, 8], [8, 3], [4, 8], [8, 4], [3, 8], [8, 5], [2, 8], [8, 6], [1, 8], [8, 7], [0, 8], [9, 0], [8, 9], [9, 1], [7, 9], [9, 2], [6, 9], [9, 3], [5, 9], [9, 4], [4, 9], [9, 5], [3, 9], [9, 6], [2, 9], [9, 7], [1, 9], [9, 8], [0, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6], [7, 0], [6, 7], [7, 1], [5, 7], [7, 2], [4, 7], [7, 3], [3, 7], [7, 4], [2, 7], [7, 5], [1, 7], [7, 6], [0, 7], [8, 0], [7, 8], [8, 1], [6, 8], [8, 2], [5, 8], [8, 3], [4, 8], [8, 4], [3, 8], [8, 5], [2, 8], [8, 6], [1, 8], [8, 7], [0, 8], [9, 0], [8, 9], [9, 1], [7, 9], [9, 2], [6, 9], [9, 3], [5, 9], [9, 4], [4, 9], [9, 5], [3, 9], [9, 6], [2, 9], [9, 7], [1, 9], [9, 8], [0, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyx', 'yxy', 'xyyx', 'yyxy', 'xyxyy', 'yxyxy', 'xyxyxy', 'yxyxyx', 'xyxyxyx', 'yxyxyxy', 'xyxyxyxy']) == [[1, 3], [3, 4], [4, 0], [5, 6], [6, 0], [1, 6], [6, 7], [7, 1], [0, 7], [7, 5], [7, 6], [6, 8], [8, 7], [7, 9], [9, 6], [9, 10], [10, 0], [5, 10], [1, 10], [10, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyx', 'yxy', 'xyyx', 'yyxy', 'xyxyy', 'yxyxy', 'xyxyxy', 'yxyxyx', 'xyxyxyx', 'yxyxyxy', 'xyxyxyxy']) == [[1, 3], [3, 4], [4, 0], [5, 6], [6, 0], [1, 6], [6, 7], [7, 1], [0, 7], [7, 5], [7, 6], [6, 8], [8, 7], [7, 9], [9, 6], [9, 10], [10, 0], [5, 10], [1, 10], [10, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['race', 'ecar', 'car', 'arc', 'racer', 'carrace', '', 'a', 'aa', 'aaa']) == [[0, 2], [0, 1], [1, 0], [4, 1], [7, 6], [6, 7], [8, 6], [8, 7], [7, 8], [6, 8], [9, 6], [9, 7], [8, 9], [9, 8], [7, 9], [6, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['race', 'ecar', 'car', 'arc', 'racer', 'carrace', '', 'a', 'aa', 'aaa']) == [[0, 2], [0, 1], [1, 0], [4, 1], [7, 6], [6, 7], [8, 6], [8, 7], [7, 8], [6, 8], [9, 6], [9, 7], [8, 9], [9, 8], [7, 9], [6, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['racecar', 'carerac', 'level', 'deified', 'civic']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['racecar', 'carerac', 'level', 'deified', 'civic']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'moon', 'noonmoon', 'moonoon', 'moonnoon', 'noonnoo']) == [[5, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'moon', 'noonmoon', 'moonoon', 'moonnoon', 'noonnoo']) == [[5, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['madam', 'racecar', 'level', 'noon', 'civic', 'rotor', 'refer', 'deified', 'reviled', 'deed', 'peep', 'radar', 'repaper', 'kayak', 'reviver', 'redder', 'repel']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['madam', 'racecar', 'level', 'noon', 'civic', 'rotor', 'refer', 'deified', 'reviled', 'deed', 'peep', 'radar', 'repaper', 'kayak', 'reviver', 'redder', 'repel']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ccbbaa', 'abcabc', 'cbacba', 'xyzzyx', 'yxzzxy', 'mnopqr', 'rqponm', '', 'pqr', 'qpon']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 8], [8, 4], [5, 8], [8, 5], [6, 7], [7, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ccbbaa', 'abcabc', 'cbacba', 'xyzzyx', 'yxzzxy', 'mnopqr', 'rqponm', '', 'pqr', 'qpon']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 8], [8, 4], [5, 8], [8, 5], [6, 7], [7, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ccbbaa', 'bbccaa', 'aabb', 'bbaa', 'ccaa', 'aabbccaa', 'aabbccbb', 'aabbaa', 'bbcc', 'ccbb', 'aabbccc', 'ccbaab', 'bbccaabb', 'ccaabbbc', 'aabbbcc', 'ccbbbaa', 'bbcaabbcc', 'aabcc', 'bbaac', 'ccaab', 'bbaabbcc', 'aabbbccaa', 'aabbbccbb', 'aaabbccaa', 'aaabbccbb', 'aabbbbcc', 'bbccbbbb', 'aabbbbaa', 'bbaaaa', 'ccaabbbaa', 'aabbbcccc', 'cccaabbb', 'bbcccaabb', 'aabbbcccbb', 'bbbaaabbbc', 'ccbbbaabbb', 'bbbaabbbcc', 'aabbbbaabbcc', 'aabbbbaabbbc', 'bbbaabbccbb', 'bbbaabbbccc', 'bbbaaabbbcc', 'aabbbbaaabbb', 'bbbaaabbbb', 'aabbbaaaaabb', 'aabbbbaaaaab', 'aabbbaaaaaaa', 'bbaaaaaaabbb', 'bbaaaaaaaabb', 'bbaaaaaaabba', 'bbaaaaaaaaab', 'bbaaaaaaaaaa']) == [[10, 0], [0, 4], [0, 1], [3, 1], [1, 9], [1, 0], [2, 10], [3, 4], [4, 3], [6, 1], [7, 1], [3, 8], [8, 4], [9, 10], [10, 9], [11, 4], [11, 1], [12, 18], [15, 16], [16, 15], [19, 3], [1, 21], [22, 16], [23, 16], [27, 10], [29, 3], [31, 16], [36, 15], [36, 37], [16, 37], [37, 36], [10, 38], [41, 36], [44, 43], [52, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ccbbaa', 'bbccaa', 'aabb', 'bbaa', 'ccaa', 'aabbccaa', 'aabbccbb', 'aabbaa', 'bbcc', 'ccbb', 'aabbccc', 'ccbaab', 'bbccaabb', 'ccaabbbc', 'aabbbcc', 'ccbbbaa', 'bbcaabbcc', 'aabcc', 'bbaac', 'ccaab', 'bbaabbcc', 'aabbbccaa', 'aabbbccbb', 'aaabbccaa', 'aaabbccbb', 'aabbbbcc', 'bbccbbbb', 'aabbbbaa', 'bbaaaa', 'ccaabbbaa', 'aabbbcccc', 'cccaabbb', 'bbcccaabb', 'aabbbcccbb', 'bbbaaabbbc', 'ccbbbaabbb', 'bbbaabbbcc', 'aabbbbaabbcc', 'aabbbbaabbbc', 'bbbaabbccbb', 'bbbaabbbccc', 'bbbaaabbbcc', 'aabbbbaaabbb', 'bbbaaabbbb', 'aabbbaaaaabb', 'aabbbbaaaaab', 'aabbbaaaaaaa', 'bbaaaaaaabbb', 'bbaaaaaaaabb', 'bbaaaaaaabba', 'bbaaaaaaaaab', 'bbaaaaaaaaaa']) == [[10, 0], [0, 4], [0, 1], [3, 1], [1, 9], [1, 0], [2, 10], [3, 4], [4, 3], [6, 1], [7, 1], [3, 8], [8, 4], [9, 10], [10, 9], [11, 4], [11, 1], [12, 18], [15, 16], [16, 15], [19, 3], [1, 21], [22, 16], [23, 16], [27, 10], [29, 3], [31, 16], [36, 15], [36, 37], [16, 37], [37, 36], [10, 38], [41, 36], [44, 43], [52, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyx', 'yxy', 'yxx', 'xxz', 'zxx', 'zzz', 'zzxz', 'xzzx', 'zxzx', 'xzzxz', 'zxzzx', 'zxxxxz', 'xzxxxxz', 'zxzxzxz', 'xzzzzzzx', 'zzzzzzzz', 'zxxzzzxxz', 'zxzzzzzxz', 'xzxxxxzzx', 'zzxxxxzzz', 'zxzzzzzzx']) == [[3, 4], [4, 3], [9, 7], [9, 10], [7, 10], [10, 6], [10, 9], [11, 12], [8, 13], [15, 5], [5, 15], [14, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyx', 'yxy', 'yxx', 'xxz', 'zxx', 'zzz', 'zzxz', 'xzzx', 'zxzx', 'xzzxz', 'zxzzx', 'zxxxxz', 'xzxxxxz', 'zxzxzxz', 'xzzzzzzx', 'zzzzzzzz', 'zxxzzzxxz', 'zxzzzzzxz', 'xzxxxxzzx', 'zzxxxxzzz', 'zxzzzzzzx']) == [[3, 4], [4, 3], [9, 7], [9, 10], [7, 10], [10, 6], [10, 9], [11, 12], [8, 13], [15, 5], [5, 15], [14, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaba', 'bacabab', 'cababac', 'abacabc', 'bacabc', 'cababc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', '', 'a', 'b', 'ba', 'ab', 'ac', 'ca', 'bca', 'cab', 'abcba', 'bcbca', 'cabcb', 'abcabcba', 'bcabcbca', 'cabcbcab']) == [[0, 12], [12, 0], [15, 1], [2, 12], [12, 2], [11, 4], [9, 15], [10, 14], [11, 10], [11, 12], [12, 11], [13, 12], [12, 13], [14, 12], [12, 14], [15, 14], [13, 15], [15, 16], [16, 13], [14, 16], [16, 15], [17, 13], [11, 17], [17, 18], [18, 11], [13, 18], [18, 17], [17, 19], [15, 20], [20, 17], [21, 12], [12, 21], [17, 22], [23, 17]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaba', 'bacabab', 'cababac', 'abacabc', 'bacabc', 'cababc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', '', 'a', 'b', 'ba', 'ab', 'ac', 'ca', 'bca', 'cab', 'abcba', 'bcbca', 'cabcb', 'abcabcba', 'bcabcbca', 'cabcbcab']) == [[0, 12], [12, 0], [15, 1], [2, 12], [12, 2], [11, 4], [9, 15], [10, 14], [11, 10], [11, 12], [12, 11], [13, 12], [12, 13], [14, 12], [12, 14], [15, 14], [13, 15], [15, 16], [16, 13], [14, 16], [16, 15], [17, 13], [11, 17], [17, 18], [18, 11], [13, 18], [18, 17], [17, 19], [15, 20], [20, 17], [21, 12], [12, 21], [17, 22], [23, 17]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'moon', 'noom', 'noon', 'moom', 'omo', 'moo', 'omo', 'm', 'oo', 'om', 'mo', '', 'n', 'nn', 'nno', 'onn', 'no', 'on', 'o', 'oo', 'ooo', 'oooo', 'ooooo', 'oooooo', 'ooooooo', 'oooooooo', 'ooooooooo']) == [[0, 12], [0, 3], [12, 0], [1, 2], [6, 2], [2, 1], [3, 12], [12, 3], [4, 12], [6, 4], [12, 4], [5, 12], [10, 5], [5, 11], [5, 7], [12, 5], [6, 8], [20, 6], [6, 10], [7, 12], [10, 7], [7, 11], [12, 7], [8, 12], [12, 8], [9, 12], [9, 19], [19, 9], [9, 20], [12, 9], [10, 19], [8, 10], [10, 11], [11, 8], [19, 11], [11, 10], [13, 12], [12, 13], [14, 12], [14, 13], [13, 14], [12, 14], [18, 15], [15, 14], [19, 15], [15, 16], [16, 19], [14, 16], [16, 17], [16, 15], [17, 13], [19, 17], [17, 18], [18, 19], [13, 18], [18, 17], [19, 12], [12, 19], [20, 12], [20, 19], [19, 20], [12, 20], [21, 12], [21, 19], [20, 21], [21, 20], [19, 21], [12, 21], [22, 12], [22, 19], [21, 22], [22, 20], [20, 22], [22, 21], [19, 22], [12, 22], [23, 12], [23, 19], [22, 23], [23, 20], [21, 23], [23, 21], [20, 23], [23, 22], [19, 23], [12, 23], [24, 12], [24, 19], [23, 24], [24, 20], [22, 24], [24, 21], [21, 24], [24, 22], [20, 24], [24, 23], [19, 24], [12, 24], [25, 12], [25, 19], [24, 25], [25, 20], [23, 25], [25, 21], [22, 25], [25, 22], [21, 25], [25, 23], [20, 25], [25, 24], [19, 25], [12, 25], [26, 12], [26, 19], [25, 26], [26, 20], [24, 26], [26, 21], [23, 26], [26, 22], [22, 26], [26, 23], [21, 26], [26, 24], [20, 26], [26, 25], [19, 26], [12, 26], [27, 12], [27, 19], [26, 27], [27, 20], [25, 27], [27, 21], [24, 27], [27, 22], [23, 27], [27, 23], [22, 27], [27, 24], [21, 27], [27, 25], [20, 27], [27, 26], [19, 27], [12, 27]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'moon', 'noom', 'noon', 'moom', 'omo', 'moo', 'omo', 'm', 'oo', 'om', 'mo', '', 'n', 'nn', 'nno', 'onn', 'no', 'on', 'o', 'oo', 'ooo', 'oooo', 'ooooo', 'oooooo', 'ooooooo', 'oooooooo', 'ooooooooo']) == [[0, 12], [0, 3], [12, 0], [1, 2], [6, 2], [2, 1], [3, 12], [12, 3], [4, 12], [6, 4], [12, 4], [5, 12], [10, 5], [5, 11], [5, 7], [12, 5], [6, 8], [20, 6], [6, 10], [7, 12], [10, 7], [7, 11], [12, 7], [8, 12], [12, 8], [9, 12], [9, 19], [19, 9], [9, 20], [12, 9], [10, 19], [8, 10], [10, 11], [11, 8], [19, 11], [11, 10], [13, 12], [12, 13], [14, 12], [14, 13], [13, 14], [12, 14], [18, 15], [15, 14], [19, 15], [15, 16], [16, 19], [14, 16], [16, 17], [16, 15], [17, 13], [19, 17], [17, 18], [18, 19], [13, 18], [18, 17], [19, 12], [12, 19], [20, 12], [20, 19], [19, 20], [12, 20], [21, 12], [21, 19], [20, 21], [21, 20], [19, 21], [12, 21], [22, 12], [22, 19], [21, 22], [22, 20], [20, 22], [22, 21], [19, 22], [12, 22], [23, 12], [23, 19], [22, 23], [23, 20], [21, 23], [23, 21], [20, 23], [23, 22], [19, 23], [12, 23], [24, 12], [24, 19], [23, 24], [24, 20], [22, 24], [24, 21], [21, 24], [24, 22], [20, 24], [24, 23], [19, 24], [12, 24], [25, 12], [25, 19], [24, 25], [25, 20], [23, 25], [25, 21], [22, 25], [25, 22], [21, 25], [25, 23], [20, 25], [25, 24], [19, 25], [12, 25], [26, 12], [26, 19], [25, 26], [26, 20], [24, 26], [26, 21], [23, 26], [26, 22], [22, 26], [26, 23], [21, 26], [26, 24], [20, 26], [26, 25], [19, 26], [12, 26], [27, 12], [27, 19], [26, 27], [27, 20], [25, 27], [27, 21], [24, 27], [27, 22], [23, 27], [27, 23], [22, 27], [27, 24], [21, 27], [27, 25], [20, 27], [27, 26], [19, 27], [12, 27]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['racecar', 'carerac', 'madam', 'level', 'noon', 'civic', 'rotor', 'refer', 'deified', 'redder', 'repaper', 'rotator', 'detartrated', 'reviled', 'repel', 'redivider', 'repaper', 'reviver', 'rotor', 'rotator', 'redder', 'refer', 'civic', 'level', 'rotor', 'repaper', 'rotator', 'deified', 'detartrated', 'refer', 'rotor', 'reviver', 'redder', 'repaper', 'repaper', 'rotor', 'repaper']) == [[3, 23], [5, 22], [6, 35], [7, 29], [8, 27], [9, 32], [10, 36], [11, 26], [12, 28], [16, 36], [17, 31], [18, 35], [19, 26], [20, 32], [21, 29], [24, 35], [25, 36], [30, 35], [33, 36], [34, 36]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['racecar', 'carerac', 'madam', 'level', 'noon', 'civic', 'rotor', 'refer', 'deified', 'redder', 'repaper', 'rotator', 'detartrated', 'reviled', 'repel', 'redivider', 'repaper', 'reviver', 'rotor', 'rotator', 'redder', 'refer', 'civic', 'level', 'rotor', 'repaper', 'rotator', 'deified', 'detartrated', 'refer', 'rotor', 'reviver', 'redder', 'repaper', 'repaper', 'rotor', 'repaper']) == [[3, 23], [5, 22], [6, 35], [7, 29], [8, 27], [9, 32], [10, 36], [11, 26], [12, 28], [16, 36], [17, 31], [18, 35], [19, 26], [20, 32], [21, 29], [24, 35], [25, 36], [30, 35], [33, 36], [34, 36]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'baaa', 'bbbb', 'aaaaa']) == [[1, 2], [2, 1], [0, 4], [4, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'baaa', 'bbbb', 'aaaaa']) == [[1, 2], [2, 1], [0, 4], [4, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a1b', 'b1a', 'abc2', '2cba', 'abcd3', '3dcba', 'abcde4', '4edcba', 'abcdef5', '5fedcba', 'abcdefg6', '6gfedcba', 'abcdefgh7', '7hgfedcba', 'abcdefghi8', '8ihgfedcba']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [12, 13], [13, 12], [14, 15], [15, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a1b', 'b1a', 'abc2', '2cba', 'abcd3', '3dcba', 'abcde4', '4edcba', 'abcdef5', '5fedcba', 'abcdefg6', '6gfedcba', 'abcdefgh7', '7hgfedcba', 'abcdefghi8', '8ihgfedcba']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [12, 13], [13, 12], [14, 15], [15, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['racecar', 'madam', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid', 'noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == [[2, 11], [3, 12], [4, 13], [5, 14], [6, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['racecar', 'madam', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid', 'noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == [[2, 11], [3, 12], [4, 13], [5, 14], [6, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aa', 'bb', 'cc', 'dd', 'ee', 'a', 'b', 'c', 'd', 'e', '', 'ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'bc', 'cb', 'bd', 'db', 'be', 'eb', 'cd', 'dc', 'ce', 'ec', 'de', 'ed', 'abc', 'cba', 'abd', 'dba', 'abe', 'eba', 'acd', 'dca', 'ace', 'eca', 'ade', 'eda', 'bcd', 'dcb', 'bce', 'ecb', 'bde', 'edb', 'cde', 'edc', 'cef', 'fec', 'def', 'fed', 'cef', 'fec', 'gfe', 'efg', 'geh', 'ehg', 'heg', 'geh', 'hic', 'cih', 'ich', 'hic', 'jid', 'dij', 'idj', 'jid', 'kil', 'lik', 'ilk', 'kil', 'lmn', 'nml', 'mln', 'lmn', 'nop', 'pon', 'opn', 'nop', 'qrs', 'srq', 'rsq', 'qrs', 'tuv', 'vtu', 'utv', 'tuv', 'wxy', 'yxw', 'xyw', 'wxy', 'zzz', 'zz', 'z']) == [[0, 25], [0, 20], [5, 0], [0, 15], [10, 0], [0, 10], [15, 0], [0, 5], [20, 0], [25, 0], [1, 25], [1, 21], [6, 1], [1, 16], [11, 1], [1, 11], [16, 1], [1, 6], [21, 1], [25, 1], [2, 25], [2, 22], [7, 2], [2, 17], [12, 2], [2, 12], [17, 2], [2, 7], [22, 2], [25, 2], [3, 25], [3, 23], [8, 3], [3, 18], [13, 3], [3, 13], [18, 3], [3, 8], [23, 3], [25, 3], [4, 25], [4, 24], [9, 4], [4, 19], [14, 4], [4, 14], [19, 4], [4, 9], [24, 4], [25, 4], [5, 25], [5, 20], [10, 5], [5, 15], [15, 5], [5, 10], [20, 5], [25, 5], [6, 25], [6, 21], [11, 6], [6, 16], [16, 6], [6, 11], [21, 6], [25, 6], [7, 25], [7, 22], [12, 7], [7, 17], [17, 7], [7, 12], [22, 7], [25, 7], [8, 25], [8, 23], [13, 8], [8, 18], [18, 8], [8, 13], [23, 8], [25, 8], [9, 25], [9, 24], [14, 9], [9, 19], [19, 9], [9, 14], [24, 9], [25, 9], [10, 25], [10, 20], [15, 10], [10, 15], [20, 10], [25, 10], [11, 25], [11, 21], [16, 11], [11, 16], [21, 11], [25, 11], [12, 25], [12, 22], [17, 12], [12, 17], [22, 12], [25, 12], [13, 25], [13, 23], [18, 13], [13, 18], [23, 13], [25, 13], [14, 25], [14, 24], [19, 14], [14, 19], [24, 14], [25, 14], [15, 25], [15, 20], [20, 15], [25, 15], [16, 25], [16, 21], [21, 16], [25, 16], [17, 25], [17, 22], [22, 17], [25, 17], [18, 25], [18, 23], [23, 18], [25, 18], [19, 25], [19, 24], [24, 19], [25, 19], [20, 25], [25, 20], [21, 25], [25, 21], [22, 25], [25, 22], [23, 25], [25, 23], [24, 25], [25, 24], [26, 20], [21, 26], [26, 27], [27, 21], [20, 27], [27, 26], [28, 20], [22, 28], [28, 29], [29, 22], [20, 29], [29, 28], [30, 20], [23, 30], [30, 31], [31, 23], [20, 31], [31, 30], [32, 20], [24, 32], [32, 33], [33, 24], [20, 33], [33, 32], [34, 21], [22, 34], [34, 35], [35, 22], [21, 35], [35, 34], [36, 21], [23, 36], [36, 37], [37, 23], [21, 37], [37, 36], [38, 21], [24, 38], [38, 39], [39, 24], [21, 39], [39, 38], [40, 22], [23, 40], [40, 41], [41, 23], [22, 41], [41, 40], [42, 22], [24, 42], [42, 43], [43, 24], [22, 43], [43, 42], [44, 23], [24, 44], [44, 45], [45, 24], [23, 45], [45, 44], [35, 46], [46, 27], [46, 47], [26, 47], [47, 34], [47, 46], [37, 48], [48, 27], [48, 49], [26, 49], [49, 36], [49, 48], [39, 50], [50, 27], [50, 51], [26, 51], [51, 38], [51, 50], [41, 52], [52, 29], [52, 53], [28, 53], [53, 40], [53, 52], [43, 54], [54, 29], [54, 55], [28, 55], [55, 42], [55, 54], [45, 56], [56, 31], [56, 57], [30, 57], [57, 44], [57, 56], [41, 58], [58, 35], [58, 59], [34, 59], [59, 40], [59, 58], [43, 60], [60, 35], [60, 61], [34, 61], [61, 42], [61, 60], [45, 62], [62, 37], [62, 63], [36, 63], [63, 44], [63, 62], [45, 64], [64, 41], [64, 65], [40, 65], [65, 44], [65, 64], [66, 43], [66, 71], [42, 67], [67, 70], [68, 45], [68, 69], [44, 69], [69, 68], [70, 43], [70, 71], [42, 71], [71, 70], [72, 73], [73, 72], [74, 76], [76, 77], [77, 76], [78, 79], [79, 81], [81, 79], [82, 83], [83, 85], [85, 83], [86, 87], [87, 89], [89, 87], [90, 91], [91, 93], [93, 91], [94, 95], [95, 97], [97, 95], [98, 99], [99, 101], [101, 99], [103, 104], [104, 103], [106, 107], [107, 109], [109, 107], [110, 25], [110, 112], [111, 110], [110, 111], [112, 110], [25, 110], [111, 25], [111, 112], [112, 111], [25, 111], [112, 25], [25, 112]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aa', 'bb', 'cc', 'dd', 'ee', 'a', 'b', 'c', 'd', 'e', '', 'ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'bc', 'cb', 'bd', 'db', 'be', 'eb', 'cd', 'dc', 'ce', 'ec', 'de', 'ed', 'abc', 'cba', 'abd', 'dba', 'abe', 'eba', 'acd', 'dca', 'ace', 'eca', 'ade', 'eda', 'bcd', 'dcb', 'bce', 'ecb', 'bde', 'edb', 'cde', 'edc', 'cef', 'fec', 'def', 'fed', 'cef', 'fec', 'gfe', 'efg', 'geh', 'ehg', 'heg', 'geh', 'hic', 'cih', 'ich', 'hic', 'jid', 'dij', 'idj', 'jid', 'kil', 'lik', 'ilk', 'kil', 'lmn', 'nml', 'mln', 'lmn', 'nop', 'pon', 'opn', 'nop', 'qrs', 'srq', 'rsq', 'qrs', 'tuv', 'vtu', 'utv', 'tuv', 'wxy', 'yxw', 'xyw', 'wxy', 'zzz', 'zz', 'z']) == [[0, 25], [0, 20], [5, 0], [0, 15], [10, 0], [0, 10], [15, 0], [0, 5], [20, 0], [25, 0], [1, 25], [1, 21], [6, 1], [1, 16], [11, 1], [1, 11], [16, 1], [1, 6], [21, 1], [25, 1], [2, 25], [2, 22], [7, 2], [2, 17], [12, 2], [2, 12], [17, 2], [2, 7], [22, 2], [25, 2], [3, 25], [3, 23], [8, 3], [3, 18], [13, 3], [3, 13], [18, 3], [3, 8], [23, 3], [25, 3], [4, 25], [4, 24], [9, 4], [4, 19], [14, 4], [4, 14], [19, 4], [4, 9], [24, 4], [25, 4], [5, 25], [5, 20], [10, 5], [5, 15], [15, 5], [5, 10], [20, 5], [25, 5], [6, 25], [6, 21], [11, 6], [6, 16], [16, 6], [6, 11], [21, 6], [25, 6], [7, 25], [7, 22], [12, 7], [7, 17], [17, 7], [7, 12], [22, 7], [25, 7], [8, 25], [8, 23], [13, 8], [8, 18], [18, 8], [8, 13], [23, 8], [25, 8], [9, 25], [9, 24], [14, 9], [9, 19], [19, 9], [9, 14], [24, 9], [25, 9], [10, 25], [10, 20], [15, 10], [10, 15], [20, 10], [25, 10], [11, 25], [11, 21], [16, 11], [11, 16], [21, 11], [25, 11], [12, 25], [12, 22], [17, 12], [12, 17], [22, 12], [25, 12], [13, 25], [13, 23], [18, 13], [13, 18], [23, 13], [25, 13], [14, 25], [14, 24], [19, 14], [14, 19], [24, 14], [25, 14], [15, 25], [15, 20], [20, 15], [25, 15], [16, 25], [16, 21], [21, 16], [25, 16], [17, 25], [17, 22], [22, 17], [25, 17], [18, 25], [18, 23], [23, 18], [25, 18], [19, 25], [19, 24], [24, 19], [25, 19], [20, 25], [25, 20], [21, 25], [25, 21], [22, 25], [25, 22], [23, 25], [25, 23], [24, 25], [25, 24], [26, 20], [21, 26], [26, 27], [27, 21], [20, 27], [27, 26], [28, 20], [22, 28], [28, 29], [29, 22], [20, 29], [29, 28], [30, 20], [23, 30], [30, 31], [31, 23], [20, 31], [31, 30], [32, 20], [24, 32], [32, 33], [33, 24], [20, 33], [33, 32], [34, 21], [22, 34], [34, 35], [35, 22], [21, 35], [35, 34], [36, 21], [23, 36], [36, 37], [37, 23], [21, 37], [37, 36], [38, 21], [24, 38], [38, 39], [39, 24], [21, 39], [39, 38], [40, 22], [23, 40], [40, 41], [41, 23], [22, 41], [41, 40], [42, 22], [24, 42], [42, 43], [43, 24], [22, 43], [43, 42], [44, 23], [24, 44], [44, 45], [45, 24], [23, 45], [45, 44], [35, 46], [46, 27], [46, 47], [26, 47], [47, 34], [47, 46], [37, 48], [48, 27], [48, 49], [26, 49], [49, 36], [49, 48], [39, 50], [50, 27], [50, 51], [26, 51], [51, 38], [51, 50], [41, 52], [52, 29], [52, 53], [28, 53], [53, 40], [53, 52], [43, 54], [54, 29], [54, 55], [28, 55], [55, 42], [55, 54], [45, 56], [56, 31], [56, 57], [30, 57], [57, 44], [57, 56], [41, 58], [58, 35], [58, 59], [34, 59], [59, 40], [59, 58], [43, 60], [60, 35], [60, 61], [34, 61], [61, 42], [61, 60], [45, 62], [62, 37], [62, 63], [36, 63], [63, 44], [63, 62], [45, 64], [64, 41], [64, 65], [40, 65], [65, 44], [65, 64], [66, 43], [66, 71], [42, 67], [67, 70], [68, 45], [68, 69], [44, 69], [69, 68], [70, 43], [70, 71], [42, 71], [71, 70], [72, 73], [73, 72], [74, 76], [76, 77], [77, 76], [78, 79], [79, 81], [81, 79], [82, 83], [83, 85], [85, 83], [86, 87], [87, 89], [89, 87], [90, 91], [91, 93], [93, 91], [94, 95], [95, 97], [97, 95], [98, 99], [99, 101], [101, 99], [103, 104], [104, 103], [106, 107], [107, 109], [109, 107], [110, 25], [110, 112], [111, 110], [110, 111], [112, 110], [25, 110], [111, 25], [111, 112], [112, 111], [25, 111], [112, 25], [25, 112]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [2, 1], [1, 2], [0, 2], [3, 0], [3, 1], [2, 3], [3, 2], [1, 3], [0, 3], [4, 0], [4, 1], [3, 4], [4, 2], [2, 4], [4, 3], [1, 4], [0, 4], [5, 0], [5, 1], [4, 5], [5, 2], [3, 5], [5, 3], [2, 5], [5, 4], [1, 5], [0, 5], [6, 0], [6, 1], [5, 6], [6, 2], [4, 6], [6, 3], [3, 6], [6, 4], [2, 6], [6, 5], [1, 6], [0, 6], [7, 0], [7, 1], [7, 2], [7, 3], [6, 7], [7, 4], [5, 7], [7, 5], [4, 7], [7, 6], [3, 7], [2, 7], [1, 7], [0, 7], [8, 0], [8, 1], [7, 8], [8, 2], [8, 3], [8, 4], [6, 8], [8, 5], [5, 8], [8, 6], [4, 8], [3, 8], [2, 8], [8, 7], [1, 8], [0, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [2, 1], [1, 2], [0, 2], [3, 0], [3, 1], [2, 3], [3, 2], [1, 3], [0, 3], [4, 0], [4, 1], [3, 4], [4, 2], [2, 4], [4, 3], [1, 4], [0, 4], [5, 0], [5, 1], [4, 5], [5, 2], [3, 5], [5, 3], [2, 5], [5, 4], [1, 5], [0, 5], [6, 0], [6, 1], [5, 6], [6, 2], [4, 6], [6, 3], [3, 6], [6, 4], [2, 6], [6, 5], [1, 6], [0, 6], [7, 0], [7, 1], [7, 2], [7, 3], [6, 7], [7, 4], [5, 7], [7, 5], [4, 7], [7, 6], [3, 7], [2, 7], [1, 7], [0, 7], [8, 0], [8, 1], [7, 8], [8, 2], [8, 3], [8, 4], [6, 8], [8, 5], [5, 8], [8, 6], [4, 8], [3, 8], [2, 8], [8, 7], [1, 8], [0, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['race', 'car', 'level', '', 'deified', 'civic', 'rotor', '', 'madam', 'refer', 'redder', 'repaper', 'reviled', 'deed', 'noon', 'detartrated', 'redivider', 'rotor']) == [[0, 1], [2, 7], [7, 2], [3, 7], [4, 7], [7, 4], [5, 7], [7, 5], [6, 7], [6, 17], [7, 6], [8, 7], [7, 8], [9, 7], [7, 9], [10, 7], [7, 10], [11, 7], [7, 11], [13, 7], [7, 13], [14, 7], [7, 14], [15, 7], [7, 15], [16, 7], [7, 16], [17, 7], [7, 17]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['race', 'car', 'level', '', 'deified', 'civic', 'rotor', '', 'madam', 'refer', 'redder', 'repaper', 'reviled', 'deed', 'noon', 'detartrated', 'redivider', 'rotor']) == [[0, 1], [2, 7], [7, 2], [3, 7], [4, 7], [7, 4], [5, 7], [7, 5], [6, 7], [6, 17], [7, 6], [8, 7], [7, 8], [9, 7], [7, 9], [10, 7], [7, 10], [11, 7], [7, 11], [13, 7], [7, 13], [14, 7], [7, 14], [15, 7], [7, 15], [16, 7], [7, 16], [17, 7], [7, 17]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xabc', 'cba', 'abcx', 'abxcba', 'cabxa', 'bxcba', 'abcabc', 'bcabc', 'cbabc', 'xcba', 'bac', 'cabx', 'bacxab', 'xcbax', 'baxcb', 'cbaabc']) == [[1, 0], [2, 1], [2, 9], [2, 5], [9, 2], [11, 10], [0, 13], [13, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xabc', 'cba', 'abcx', 'abxcba', 'cabxa', 'bxcba', 'abcabc', 'bcabc', 'cbabc', 'xcba', 'bac', 'cabx', 'bacxab', 'xcbax', 'baxcb', 'cbaabc']) == [[1, 0], [2, 1], [2, 9], [2, 5], [9, 2], [11, 10], [0, 13], [13, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'level', 'deified', 'civic', 'rotor', 'madam', 'refer', 'deed', 'peep', 'radar', 'reviled', 'repaid', 'detartrated', 'reviver', 'redder', 'repaper', 'pepper', 'repel', 'deterred', 'reworded', 'repeal', 'perpet', 'repressed', 'repellet', 'perpetual', 'repellect']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'level', 'deified', 'civic', 'rotor', 'madam', 'refer', 'deed', 'peep', 'radar', 'reviled', 'repaid', 'detartrated', 'reviver', 'redder', 'repaper', 'pepper', 'repel', 'deterred', 'reworded', 'repeal', 'perpet', 'repressed', 'repellet', 'perpetual', 'repellect']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['palindrome', 'emordnilap', 'detartrated', 'deified', 'repaid', 'stressed', 'desserts', 'deed', 'civic', 'rotor', 'refer', 'level', 'kayak', 'reviled']) == [[0, 1], [1, 0], [5, 6], [6, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['palindrome', 'emordnilap', 'detartrated', 'deified', 'repaid', 'stressed', 'desserts', 'deed', 'civic', 'rotor', 'refer', 'level', 'kayak', 'reviled']) == [[0, 1], [1, 0], [5, 6], [6, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrstu', 'utsrqp', 'vwxyz', 'zyxwv']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrstu', 'utsrqp', 'vwxyz', 'zyxwv']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xabcx', 'xbax', 'xcabx', 'xcax', 'xbxc', 'xcabxx', 'xxcabx', 'abcxx', 'xxcba', 'abcdxx', 'xxdcba', 'xxabcd', 'dxxcba', 'xabxx', 'xxbax']) == [[7, 8], [8, 7], [9, 10], [10, 9], [7, 12], [13, 1], [13, 14], [14, 13]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xabcx', 'xbax', 'xcabx', 'xcax', 'xbxc', 'xcabxx', 'xxcabx', 'abcxx', 'xxcba', 'abcdxx', 'xxdcba', 'xxabcd', 'dxxcba', 'xabxx', 'xxbax']) == [[7, 8], [8, 7], [9, 10], [10, 9], [7, 12], [13, 1], [13, 14], [14, 13]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['', 'a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc', 'aaaaa', 'bbbbb', 'ccccc']) == [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [4, 1], [1, 4], [0, 4], [5, 0], [5, 2], [2, 5], [0, 5], [6, 0], [6, 3], [3, 6], [0, 6], [7, 0], [7, 1], [4, 7], [7, 4], [1, 7], [0, 7], [8, 0], [8, 2], [5, 8], [8, 5], [2, 8], [0, 8], [9, 0], [9, 3], [6, 9], [9, 6], [3, 9], [0, 9], [10, 0], [10, 1], [7, 10], [10, 4], [4, 10], [10, 7], [1, 10], [0, 10], [11, 0], [11, 2], [8, 11], [11, 5], [5, 11], [11, 8], [2, 11], [0, 11], [12, 0], [12, 3], [9, 12], [12, 6], [6, 12], [12, 9], [3, 12], [0, 12], [13, 0], [13, 1], [10, 13], [13, 4], [7, 13], [13, 7], [4, 13], [13, 10], [1, 13], [0, 13], [14, 0], [14, 2], [11, 14], [14, 5], [8, 14], [14, 8], [5, 14], [14, 11], [2, 14], [0, 14], [15, 0], [15, 3], [12, 15], [15, 6], [9, 15], [15, 9], [6, 15], [15, 12], [3, 15], [0, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['', 'a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc', 'aaaaa', 'bbbbb', 'ccccc']) == [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [4, 1], [1, 4], [0, 4], [5, 0], [5, 2], [2, 5], [0, 5], [6, 0], [6, 3], [3, 6], [0, 6], [7, 0], [7, 1], [4, 7], [7, 4], [1, 7], [0, 7], [8, 0], [8, 2], [5, 8], [8, 5], [2, 8], [0, 8], [9, 0], [9, 3], [6, 9], [9, 6], [3, 9], [0, 9], [10, 0], [10, 1], [7, 10], [10, 4], [4, 10], [10, 7], [1, 10], [0, 10], [11, 0], [11, 2], [8, 11], [11, 5], [5, 11], [11, 8], [2, 11], [0, 11], [12, 0], [12, 3], [9, 12], [12, 6], [6, 12], [12, 9], [3, 12], [0, 12], [13, 0], [13, 1], [10, 13], [13, 4], [7, 13], [13, 7], [4, 13], [13, 10], [1, 13], [0, 13], [14, 0], [14, 2], [11, 14], [14, 5], [8, 14], [14, 8], [5, 14], [14, 11], [2, 14], [0, 14], [15, 0], [15, 3], [12, 15], [15, 6], [9, 15], [15, 9], [6, 15], [15, 12], [3, 15], [0, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'a', 'b', 'aba', 'bab', 'aa', 'bb', 'aaa', 'bbb']) == [[0, 2], [3, 0], [0, 1], [1, 3], [2, 1], [1, 0], [0, 4], [4, 1], [1, 5], [5, 0], [6, 2], [2, 6], [7, 3], [3, 7], [8, 2], [6, 8], [8, 6], [2, 8], [9, 3], [7, 9], [9, 7], [3, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'a', 'b', 'aba', 'bab', 'aa', 'bb', 'aaa', 'bbb']) == [[0, 2], [3, 0], [0, 1], [1, 3], [2, 1], [1, 0], [0, 4], [4, 1], [1, 5], [5, 0], [6, 2], [2, 6], [7, 3], [3, 7], [8, 2], [6, 8], [8, 6], [2, 8], [9, 3], [7, 9], [9, 7], [3, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['race', 'ecar', 'car', 'arc', 'civic', 'level', 'deified', 'rotor', 'redder', 'repaper']) == [[0, 2], [0, 1], [1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['race', 'ecar', 'car', 'arc', 'civic', 'level', 'deified', 'rotor', 'redder', 'repaper']) == [[0, 2], [0, 1], [1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['noon', 'moon', 'noonmoon', 'moonnoon', 'noonno', 'onnoon', 'noonmo', 'onnoom']) == [[4, 5], [5, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['noon', 'moon', 'noonmoon', 'moonnoon', 'noonno', 'onnoon', 'noonmo', 'onnoom']) == [[4, 5], [5, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa']) == [[0, 1], [1, 0], [1, 2], [0, 2], [2, 0], [2, 1], [2, 3], [1, 3], [0, 3], [3, 0], [3, 1], [3, 2], [3, 4], [2, 4], [1, 4], [0, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa']) == [[0, 1], [1, 0], [1, 2], [0, 2], [2, 0], [2, 1], [2, 3], [1, 3], [0, 3], [3, 0], [3, 1], [3, 2], [3, 4], [2, 4], [1, 4], [0, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['12321', '21312', '32123', '43234', '54345', '65456', '76567', '87678', '98789', '10901', '11011']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['12321', '21312', '32123', '43234', '54345', '65456', '76567', '87678', '98789', '10901', '11011']) == []: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['aabb', 'bbaa', 'abc', 'cba']) == [[0, 1], [1, 0], [2, 3], [3, 2]]
    assert candidate(words = ['bat', 'tab', 'cat']) == [[0, 1], [1, 0]]
    assert candidate(words = ['abc', 'cba', 'bca', 'xyz', 'zyx']) == [[0, 1], [1, 0], [3, 4], [4, 3]]
    assert candidate(words = ['abba', 'a', 'abc', 'cba']) == [[2, 3], [3, 2]]
    assert candidate(words = ['abcd', 'dcba', '', 'cba', 'abc']) == [[0, 3], [0, 1], [4, 1], [1, 0], [3, 4], [4, 3]]
    assert candidate(words = ['abba', 'a', 'abc', 'cba', 'bbaa', 'aba']) == [[2, 3], [3, 2]]
    assert candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4]]
    assert candidate(words = ['aa', 'bb', 'aaa', 'bbb', 'aaaa', 'bbbb']) == [[0, 2], [2, 0], [1, 3], [3, 1], [2, 4], [4, 0], [0, 4], [4, 2], [3, 5], [5, 1], [1, 5], [5, 3]]
    assert candidate(words = ['aa', 'b', 'aaa', 'bb']) == [[0, 2], [2, 0], [3, 1], [1, 3]]
    assert candidate(words = ['a', '']) == [[0, 1], [1, 0]]
    assert candidate(words = ['abcd', 'dcba', 'lls', 's', 'sssll']) == [[0, 1], [1, 0], [3, 2], [2, 4]]
    assert candidate(words = ['abc', 'cba', 'bba', 'aab', 'aaa']) == [[0, 1], [1, 0]]
    assert candidate(words = ['a', 'b', 'c', 'd']) == []
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == []
    assert candidate(words = ['a', '']) == [[0, 1], [1, 0]]
    assert candidate(words = ['tacocat', 'racecar', 'banana', 'ananab', 'civic']) == [[2, 3], [3, 2]]
    assert candidate(words = ['aabb', 'bbaa', 'abab', 'baba', 'aaaa', 'bbbb']) == [[0, 1], [1, 0], [2, 3], [3, 2]]
    assert candidate(words = ['abcd', 'dcba']) == [[0, 1], [1, 0]]
    assert candidate(words = ['dcb', 'abcd', 'cba', 'abc', 'bca', 'bac', 'cab', 'a']) == [[0, 1], [1, 2], [2, 3], [3, 2], [5, 6], [6, 5]]
    assert candidate(words = ['abab', 'baba', 'abba', 'baab', 'aaaa', 'bbbb']) == [[0, 1], [1, 0]]
    assert candidate(words = ['abba', 'a', 'baa', 'b']) == [[2, 3]]
    assert candidate(words = ['abcd', 'dcba', 'lls', 's', 'sssll', 'ddsssll']) == [[0, 1], [1, 0], [3, 2], [2, 4]]
    assert candidate(words = ['a', 'abc', 'aba', 'xyz', 'zyx']) == [[3, 4], [4, 3]]
    assert candidate(words = ['', 'a', 'b', 'c', 'd']) == [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4]]
    assert candidate(words = ['aabb', 'bbaa', 'aaaa', 'abba', 'baab']) == [[0, 1], [1, 0]]
    assert candidate(words = ['dcb', 'abcd', 'cba', 'cbcd']) == [[0, 1], [1, 2], [0, 3]]
    assert candidate(words = ['zxcvbnm', 'mnbvcxz', 'asdfghjkl', 'lkjhgfdsa', 'qwertyuiop', 'poiuytrewq', '1234567890', '0987654321', 'abcdefghij', 'jihgfedcba', 'klmnopqrst', 'tsrqponmlk', 'uvwxyz', 'zyxwvut', 'nopqrstu', 'utsrqpon', 'abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq', 'yz', 'zy', 'abcd', 'dcba', 'ab', 'ba', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [13, 12], [14, 15], [15, 14], [16, 17], [17, 16], [18, 19], [19, 18], [20, 21], [21, 20], [22, 52], [53, 22], [22, 23], [23, 53], [52, 23], [23, 22], [24, 25], [25, 24], [26, 28], [29, 26], [26, 27], [27, 29], [28, 27], [27, 26]]
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6], [7, 0], [6, 7], [7, 1], [5, 7], [7, 2], [4, 7], [7, 3], [3, 7], [7, 4], [2, 7], [7, 5], [1, 7], [7, 6], [0, 7], [8, 0], [7, 8], [8, 1], [6, 8], [8, 2], [5, 8], [8, 3], [4, 8], [8, 4], [3, 8], [8, 5], [2, 8], [8, 6], [1, 8], [8, 7], [0, 8], [9, 0], [8, 9], [9, 1], [7, 9], [9, 2], [6, 9], [9, 3], [5, 9], [9, 4], [4, 9], [9, 5], [3, 9], [9, 6], [2, 9], [9, 7], [1, 9], [9, 8], [0, 9], [10, 0], [9, 10], [10, 1], [8, 10], [10, 2], [7, 10], [10, 3], [6, 10], [10, 4], [5, 10], [10, 5], [4, 10], [10, 6], [3, 10], [10, 7], [2, 10], [10, 8], [1, 10], [10, 9], [0, 10], [11, 0], [10, 11], [11, 1], [9, 11], [11, 2], [8, 11], [11, 3], [7, 11], [11, 4], [6, 11], [11, 5], [5, 11], [11, 6], [4, 11], [11, 7], [3, 11], [11, 8], [2, 11], [11, 9], [1, 11], [11, 10], [0, 11], [12, 0], [11, 12], [12, 1], [10, 12], [12, 2], [9, 12], [12, 3], [8, 12], [12, 4], [7, 12], [12, 5], [6, 12], [12, 6], [5, 12], [12, 7], [4, 12], [12, 8], [3, 12], [12, 9], [2, 12], [12, 10], [1, 12], [12, 11], [0, 12], [13, 0], [12, 13], [13, 1], [11, 13], [13, 2], [10, 13], [13, 3], [9, 13], [13, 4], [8, 13], [13, 5], [7, 13], [13, 6], [6, 13], [13, 7], [5, 13], [13, 8], [4, 13], [13, 9], [3, 13], [13, 10], [2, 13], [13, 11], [1, 13], [13, 12], [0, 13], [14, 0], [13, 14], [14, 1], [12, 14], [14, 2], [11, 14], [14, 3], [10, 14], [14, 4], [9, 14], [14, 5], [8, 14], [14, 6], [7, 14], [14, 7], [6, 14], [14, 8], [5, 14], [14, 9], [4, 14], [14, 10], [3, 14], [14, 11], [2, 14], [14, 12], [1, 14], [14, 13], [0, 14], [15, 0], [14, 15], [15, 1], [13, 15], [15, 2], [12, 15], [15, 3], [11, 15], [15, 4], [10, 15], [15, 5], [9, 15], [15, 6], [8, 15], [15, 7], [7, 15], [15, 8], [6, 15], [15, 9], [5, 15], [15, 10], [4, 15], [15, 11], [3, 15], [15, 12], [2, 15], [15, 13], [1, 15], [15, 14], [0, 15], [16, 0], [15, 16], [16, 1], [14, 16], [16, 2], [13, 16], [16, 3], [12, 16], [16, 4], [11, 16], [16, 5], [10, 16], [16, 6], [9, 16], [16, 7], [8, 16], [16, 8], [7, 16], [16, 9], [6, 16], [16, 10], [5, 16], [16, 11], [4, 16], [16, 12], [3, 16], [16, 13], [2, 16], [16, 14], [1, 16], [16, 15], [0, 16], [17, 0], [16, 17], [17, 1], [15, 17], [17, 2], [14, 17], [17, 3], [13, 17], [17, 4], [12, 17], [17, 5], [11, 17], [17, 6], [10, 17], [17, 7], [9, 17], [17, 8], [8, 17], [17, 9], [7, 17], [17, 10], [6, 17], [17, 11], [5, 17], [17, 12], [4, 17], [17, 13], [3, 17], [17, 14], [2, 17], [17, 15], [1, 17], [17, 16], [0, 17], [18, 0], [17, 18], [18, 1], [16, 18], [18, 2], [15, 18], [18, 3], [14, 18], [18, 4], [13, 18], [18, 5], [12, 18], [18, 6], [11, 18], [18, 7], [10, 18], [18, 8], [9, 18], [18, 9], [8, 18], [18, 10], [7, 18], [18, 11], [6, 18], [18, 12], [5, 18], [18, 13], [4, 18], [18, 14], [3, 18], [18, 15], [2, 18], [18, 16], [1, 18], [18, 17], [0, 18], [19, 0], [18, 19], [19, 1], [17, 19], [19, 2], [16, 19], [19, 3], [15, 19], [19, 4], [14, 19], [19, 5], [13, 19], [19, 6], [12, 19], [19, 7], [11, 19], [19, 8], [10, 19], [19, 9], [9, 19], [19, 10], [8, 19], [19, 11], [7, 19], [19, 12], [6, 19], [19, 13], [5, 19], [19, 14], [4, 19], [19, 15], [3, 19], [19, 16], [2, 19], [19, 17], [1, 19], [19, 18], [0, 19]]
    assert candidate(words = ['a', 'b', 'c', '', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [[0, 3], [3, 0], [1, 3], [3, 1], [2, 3], [3, 2], [4, 3], [3, 4], [5, 3], [3, 5], [6, 3], [3, 6], [7, 3], [3, 7], [8, 3], [3, 8], [9, 3], [3, 9], [10, 3], [3, 10], [11, 3], [3, 11], [12, 3], [3, 12], [13, 3], [3, 13], [14, 3], [3, 14], [15, 3], [3, 15], [16, 3], [3, 16], [17, 3], [3, 17], [18, 3], [3, 18], [19, 3], [3, 19], [20, 3], [3, 20], [21, 3], [3, 21], [22, 3], [3, 22], [23, 3], [3, 23], [24, 3], [3, 24], [25, 3], [3, 25], [26, 3], [3, 26]]
    assert candidate(words = ['noon', 'civic', 'level', 'rotor', 'deified', 'redder', 'repaper', 'refer', 'reviver', 'reviled']) == []
    assert candidate(words = ['abba', 'baab', 'aabb', 'bbaa', 'aaaa', 'aaab', 'abaa', 'baaa', 'bbba', 'baba']) == [[2, 3], [3, 2], [5, 7], [7, 5]]
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == [[1, 0]]
    assert candidate(words = ['noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == []
    assert candidate(words = ['race', 'car', '', '', 'racecar', 'ecar', 'cec', 'ceccec']) == [[0, 1], [0, 5], [2, 3], [4, 3], [3, 4], [5, 0], [6, 3], [3, 6], [7, 3], [7, 6], [6, 7], [3, 7]]
    assert candidate(words = ['abcdabcd', 'dcbaabcd', 'cdabcd', 'dcbabcd', 'abcbabc', 'cbababc', 'abcabcba', 'bcbabcba', 'cdcdcdcd', 'dcddcddc', 'abcd', 'dcba', 'cd', 'dc', 'abcdabc', 'dcbaabc', 'abc', 'cba']) == [[15, 1], [6, 17], [4, 7], [12, 9], [10, 17], [10, 11], [16, 11], [11, 10], [12, 13], [13, 12], [16, 17], [17, 16]]
    assert candidate(words = ['race', 'car', 'cec', 'dec', 'ded', 'level', 'deified', 'civic']) == [[0, 1]]
    assert candidate(words = ['abcde', 'edcba', 'fgh', 'hgf', 'xyz', 'zyx', 'ijk', 'kji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvw', 'wvu']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [12, 13], [13, 12]]
    assert candidate(words = ['race', 'ecar', 'car', 'racecar', 'carrace', 'arcec', 'cecarr', 'racecarcar']) == [[0, 2], [0, 1], [1, 0]]
    assert candidate(words = ['aabbcc', 'ccbbaa', 'abcde', 'edcba', 'abcd', 'dcba']) == [[0, 1], [1, 0], [2, 5], [2, 3], [4, 3], [3, 2], [4, 5], [5, 4]]
    assert candidate(words = ['aabbcc', 'ccbbaa', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14]]
    assert candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwuv']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6]]
    assert candidate(words = ['abab', 'baba', 'ab', 'ba', 'a', 'b', '', 'aba', 'bab', 'bba', 'aab', 'baa']) == [[0, 4], [8, 0], [0, 7], [5, 0], [0, 1], [1, 5], [7, 1], [1, 8], [4, 1], [1, 0], [2, 4], [5, 2], [2, 3], [3, 5], [4, 3], [3, 2], [4, 6], [6, 4], [5, 6], [6, 5], [7, 6], [2, 7], [7, 3], [6, 7], [8, 6], [3, 8], [8, 2], [6, 8], [2, 9], [4, 9], [3, 10], [5, 10], [10, 11], [11, 5], [11, 2], [11, 10]]
    assert candidate(words = ['aabbcc', 'ccbbaa', 'abcabc', 'cbabca', 'bacbac', 'abacab', 'bacbac', 'cababc', 'bcaacb', 'aabb', 'bbaa', 'aabbaa', 'abbbaa', 'aaabbb', 'baaabb', 'aababb', 'abbaab', 'bababa']) == [[0, 10], [0, 1], [9, 1], [1, 0], [9, 10], [10, 9], [9, 11], [11, 10]]
    assert candidate(words = ['xyxy', 'yxyx', 'yxx', 'xx', 'xyyx', 'yyxy', 'xyx', 'yyy', 'xyyxxyy', 'yyxxyyx', 'xyyyxyx', 'yyxyxxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy', 'xyyyxyy', 'yyxxyxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy', 'xyyyxyy', 'yyxxyxy', 'xyyxyyx', 'yyxxyxy', 'xyyyxxy', 'yyxyxyx', 'xyyxyxy', 'yyxxyyy']) == [[0, 6], [0, 1], [6, 1], [1, 0], [3, 2], [8, 9], [9, 8], [12, 28], [16, 4], [20, 28], [24, 4], [32, 4]]
    assert candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4]]
    assert candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10]]
    assert candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghijk', 'kjihgfedcba', 'abcdefghijkl', 'lkjihgfedcba', 'abcdefghijklm', 'mlkjihgfedcba', 'abcdefghijklmn', 'nmlkjihgfedcba', 'abcdefghijklmno', 'onmlkjihgfedcba', 'abcdefghijklmnop', 'ponmlkjihgfedcba', 'abcdefghijklmnopq', 'qponmlkjihgfedcba', 'abcdefghijklmnopqr', 'rponmlkjihgfedcba', 'abcdefghijklmnopqrs', 'spnmlkjihgfedcba', 'abcdefghijklmnopqrst', 'tspnmlkjihgfedcba', 'abcdefghijklmnopqrstu', 'ustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuv', 'vustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvw', 'wvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwx', 'xwvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxy', 'yxwvustpnmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14], [16, 15], [16, 17], [14, 17], [17, 16], [18, 17], [18, 19], [16, 19], [19, 18], [20, 19], [20, 21], [18, 21], [21, 20], [22, 21], [22, 23], [20, 23], [23, 22], [24, 23], [24, 25], [22, 25], [25, 24], [26, 25], [26, 27], [24, 27], [27, 26], [28, 27], [28, 29], [26, 29], [29, 28], [30, 29], [30, 31], [28, 31], [31, 30], [32, 31], [28, 33], [48, 49], [46, 49], [49, 48]]
    assert candidate(words = ['abcba', 'bcbaa', 'cbaab', 'baabc', 'aabcd', 'bcdcb', 'cdcbc', 'dcbcd', 'cbcdc', 'bcdbc', 'abcdc']) == [[2, 3], [3, 2], [6, 8], [8, 6]]
    assert candidate(words = ['abcde', 'edcba', '', '', 'abcdeedcba', 'aabcdeedcbaa', 'aaabcdeedcbaaa', 'aaaabcdeedcbaaaa', 'aaaaabcdeedcbaaaaa', 'abcdeedcbaaaaa', 'aabcdeedcbaaaaaa', 'aaabcdeedcbaaaaaaa', 'aaaabcdeedcbaaaaaaaa', 'aaaaabcdeedcbaaaaaaaaa', 'abcdeedcbaaaaaaaaaa']) == [[0, 1], [1, 0], [2, 3], [4, 3], [3, 4], [5, 3], [3, 5], [6, 3], [3, 6], [7, 3], [3, 7], [8, 3], [8, 9], [3, 8], [9, 4], [10, 5], [11, 6], [12, 7], [13, 9], [13, 8], [14, 4]]
    assert candidate(words = ['abacaba', 'abcbaca', 'abcdcba', 'abeceda', 'aabcdcbba', 'abcddcba', 'deified', 'civic', 'level', 'rotor', 'madam', 'refer', 'repaper', 'reviver', 'reviled', 'redder']) == []
    assert candidate(words = ['abacaba', 'acababa', 'bacabab', 'cabaaba', '', 'abacaba', 'acababa', 'bacabab', 'cabaaba']) == [[0, 4], [0, 5], [4, 0], [5, 4], [4, 5]]
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcba', 'abccba', 'abcdcba', 'abccbaa']) == [[1, 0], [7, 5], [0, 7]]
    assert candidate(words = ['palindrome', 'emordnilap', 'word', 'drow', 'madam', 'ada', 'radar', 'kayak', 'reviled', 'devil']) == [[0, 1], [1, 0], [2, 3], [3, 2]]
    assert candidate(words = ['noon', 'moon', 'noontime', 'timenoon', 'time', 'emit']) == [[5, 2], [3, 5], [4, 5], [5, 4]]
    assert candidate(words = ['xyx', 'yxy', 'xxyy', 'yyxx', 'xyyx', 'yxxy', 'xyxx', 'yxx', 'xxy', 'yy', 'xy', 'yx', 'x', 'y', '', 'aaa', 'bbb', 'ccc', 'aaab', 'bbba', 'aaa', 'bbbb', 'cccc', 'dddd', 'dddb', 'bbbd', 'aaa', 'bbbb', 'cccc', 'dddd', 'dddb', 'bbbd']) == [[0, 14], [10, 0], [0, 11], [14, 0], [1, 14], [11, 1], [1, 10], [14, 1], [9, 2], [2, 7], [2, 3], [8, 3], [3, 9], [3, 2], [4, 14], [14, 4], [5, 14], [7, 5], [5, 8], [14, 5], [8, 6], [6, 11], [6, 0], [12, 6], [7, 13], [7, 10], [7, 8], [11, 8], [13, 8], [8, 7], [9, 14], [9, 13], [13, 9], [14, 9], [10, 12], [13, 10], [10, 11], [11, 13], [12, 11], [11, 10], [12, 14], [14, 12], [13, 14], [14, 13], [15, 14], [15, 26], [14, 15], [16, 14], [14, 16], [17, 14], [14, 17], [18, 26], [19, 16], [20, 14], [20, 26], [14, 20], [21, 14], [16, 21], [21, 16], [21, 27], [14, 21], [22, 14], [17, 22], [22, 17], [22, 28], [14, 22], [23, 14], [23, 29], [14, 23], [25, 16], [26, 14], [14, 26], [27, 14], [16, 27], [27, 16], [14, 27], [28, 14], [17, 28], [28, 17], [14, 28], [29, 14], [14, 29], [31, 16]]
    assert candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba', 'abcdefg', 'gfedcba', 'abcdefgh', 'hgfedcba', 'abcdefghi', 'ihgfedcba', 'abcdefghij', 'jihgfedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8], [10, 9], [10, 11], [8, 11], [11, 10], [12, 11], [12, 13], [10, 13], [13, 12], [14, 13], [14, 15], [12, 15], [15, 14], [16, 15], [16, 17], [14, 17], [17, 16]]
    assert candidate(words = ['amanaplanacanalpanama', 'noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == []
    assert candidate(words = ['aaaa', 'aaab', 'baaa', 'baba', 'abab', 'abba']) == [[1, 2], [2, 1], [3, 4], [4, 3]]
    assert candidate(words = ['abcdexyz', 'zyxcdeba', 'mnop', 'ponm', '', 'pponm', 'mnopq', 'zyxwvutsrqp', 'rqsponmlkjihgfedcba']) == [[2, 3], [3, 2], [2, 5], [6, 3]]
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6], [7, 0], [6, 7], [7, 1], [5, 7], [7, 2], [4, 7], [7, 3], [3, 7], [7, 4], [2, 7], [7, 5], [1, 7], [7, 6], [0, 7], [8, 0], [7, 8], [8, 1], [6, 8], [8, 2], [5, 8], [8, 3], [4, 8], [8, 4], [3, 8], [8, 5], [2, 8], [8, 6], [1, 8], [8, 7], [0, 8], [9, 0], [8, 9], [9, 1], [7, 9], [9, 2], [6, 9], [9, 3], [5, 9], [9, 4], [4, 9], [9, 5], [3, 9], [9, 6], [2, 9], [9, 7], [1, 9], [9, 8], [0, 9]]
    assert candidate(words = ['xyx', 'yxy', 'xyyx', 'yyxy', 'xyxyy', 'yxyxy', 'xyxyxy', 'yxyxyx', 'xyxyxyx', 'yxyxyxy', 'xyxyxyxy']) == [[1, 3], [3, 4], [4, 0], [5, 6], [6, 0], [1, 6], [6, 7], [7, 1], [0, 7], [7, 5], [7, 6], [6, 8], [8, 7], [7, 9], [9, 6], [9, 10], [10, 0], [5, 10], [1, 10], [10, 8]]
    assert candidate(words = ['race', 'ecar', 'car', 'arc', 'racer', 'carrace', '', 'a', 'aa', 'aaa']) == [[0, 2], [0, 1], [1, 0], [4, 1], [7, 6], [6, 7], [8, 6], [8, 7], [7, 8], [6, 8], [9, 6], [9, 7], [8, 9], [9, 8], [7, 9], [6, 9]]
    assert candidate(words = ['racecar', 'carerac', 'level', 'deified', 'civic']) == []
    assert candidate(words = ['noon', 'moon', 'noonmoon', 'moonoon', 'moonnoon', 'noonnoo']) == [[5, 4]]
    assert candidate(words = ['madam', 'racecar', 'level', 'noon', 'civic', 'rotor', 'refer', 'deified', 'reviled', 'deed', 'peep', 'radar', 'repaper', 'kayak', 'reviver', 'redder', 'repel']) == []
    assert candidate(words = ['aabbcc', 'ccbbaa', 'abcabc', 'cbacba', 'xyzzyx', 'yxzzxy', 'mnopqr', 'rqponm', '', 'pqr', 'qpon']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 8], [8, 4], [5, 8], [8, 5], [6, 7], [7, 6]]
    assert candidate(words = ['aabbcc', 'ccbbaa', 'bbccaa', 'aabb', 'bbaa', 'ccaa', 'aabbccaa', 'aabbccbb', 'aabbaa', 'bbcc', 'ccbb', 'aabbccc', 'ccbaab', 'bbccaabb', 'ccaabbbc', 'aabbbcc', 'ccbbbaa', 'bbcaabbcc', 'aabcc', 'bbaac', 'ccaab', 'bbaabbcc', 'aabbbccaa', 'aabbbccbb', 'aaabbccaa', 'aaabbccbb', 'aabbbbcc', 'bbccbbbb', 'aabbbbaa', 'bbaaaa', 'ccaabbbaa', 'aabbbcccc', 'cccaabbb', 'bbcccaabb', 'aabbbcccbb', 'bbbaaabbbc', 'ccbbbaabbb', 'bbbaabbbcc', 'aabbbbaabbcc', 'aabbbbaabbbc', 'bbbaabbccbb', 'bbbaabbbccc', 'bbbaaabbbcc', 'aabbbbaaabbb', 'bbbaaabbbb', 'aabbbaaaaabb', 'aabbbbaaaaab', 'aabbbaaaaaaa', 'bbaaaaaaabbb', 'bbaaaaaaaabb', 'bbaaaaaaabba', 'bbaaaaaaaaab', 'bbaaaaaaaaaa']) == [[10, 0], [0, 4], [0, 1], [3, 1], [1, 9], [1, 0], [2, 10], [3, 4], [4, 3], [6, 1], [7, 1], [3, 8], [8, 4], [9, 10], [10, 9], [11, 4], [11, 1], [12, 18], [15, 16], [16, 15], [19, 3], [1, 21], [22, 16], [23, 16], [27, 10], [29, 3], [31, 16], [36, 15], [36, 37], [16, 37], [37, 36], [10, 38], [41, 36], [44, 43], [52, 3]]
    assert candidate(words = ['xyx', 'yxy', 'yxx', 'xxz', 'zxx', 'zzz', 'zzxz', 'xzzx', 'zxzx', 'xzzxz', 'zxzzx', 'zxxxxz', 'xzxxxxz', 'zxzxzxz', 'xzzzzzzx', 'zzzzzzzz', 'zxxzzzxxz', 'zxzzzzzxz', 'xzxxxxzzx', 'zzxxxxzzz', 'zxzzzzzzx']) == [[3, 4], [4, 3], [9, 7], [9, 10], [7, 10], [10, 6], [10, 9], [11, 12], [8, 13], [15, 5], [5, 15], [14, 20]]
    assert candidate(words = ['abacaba', 'bacabab', 'cababac', 'abacabc', 'bacabc', 'cababc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', '', 'a', 'b', 'ba', 'ab', 'ac', 'ca', 'bca', 'cab', 'abcba', 'bcbca', 'cabcb', 'abcabcba', 'bcabcbca', 'cabcbcab']) == [[0, 12], [12, 0], [15, 1], [2, 12], [12, 2], [11, 4], [9, 15], [10, 14], [11, 10], [11, 12], [12, 11], [13, 12], [12, 13], [14, 12], [12, 14], [15, 14], [13, 15], [15, 16], [16, 13], [14, 16], [16, 15], [17, 13], [11, 17], [17, 18], [18, 11], [13, 18], [18, 17], [17, 19], [15, 20], [20, 17], [21, 12], [12, 21], [17, 22], [23, 17]]
    assert candidate(words = ['noon', 'moon', 'noom', 'noon', 'moom', 'omo', 'moo', 'omo', 'm', 'oo', 'om', 'mo', '', 'n', 'nn', 'nno', 'onn', 'no', 'on', 'o', 'oo', 'ooo', 'oooo', 'ooooo', 'oooooo', 'ooooooo', 'oooooooo', 'ooooooooo']) == [[0, 12], [0, 3], [12, 0], [1, 2], [6, 2], [2, 1], [3, 12], [12, 3], [4, 12], [6, 4], [12, 4], [5, 12], [10, 5], [5, 11], [5, 7], [12, 5], [6, 8], [20, 6], [6, 10], [7, 12], [10, 7], [7, 11], [12, 7], [8, 12], [12, 8], [9, 12], [9, 19], [19, 9], [9, 20], [12, 9], [10, 19], [8, 10], [10, 11], [11, 8], [19, 11], [11, 10], [13, 12], [12, 13], [14, 12], [14, 13], [13, 14], [12, 14], [18, 15], [15, 14], [19, 15], [15, 16], [16, 19], [14, 16], [16, 17], [16, 15], [17, 13], [19, 17], [17, 18], [18, 19], [13, 18], [18, 17], [19, 12], [12, 19], [20, 12], [20, 19], [19, 20], [12, 20], [21, 12], [21, 19], [20, 21], [21, 20], [19, 21], [12, 21], [22, 12], [22, 19], [21, 22], [22, 20], [20, 22], [22, 21], [19, 22], [12, 22], [23, 12], [23, 19], [22, 23], [23, 20], [21, 23], [23, 21], [20, 23], [23, 22], [19, 23], [12, 23], [24, 12], [24, 19], [23, 24], [24, 20], [22, 24], [24, 21], [21, 24], [24, 22], [20, 24], [24, 23], [19, 24], [12, 24], [25, 12], [25, 19], [24, 25], [25, 20], [23, 25], [25, 21], [22, 25], [25, 22], [21, 25], [25, 23], [20, 25], [25, 24], [19, 25], [12, 25], [26, 12], [26, 19], [25, 26], [26, 20], [24, 26], [26, 21], [23, 26], [26, 22], [22, 26], [26, 23], [21, 26], [26, 24], [20, 26], [26, 25], [19, 26], [12, 26], [27, 12], [27, 19], [26, 27], [27, 20], [25, 27], [27, 21], [24, 27], [27, 22], [23, 27], [27, 23], [22, 27], [27, 24], [21, 27], [27, 25], [20, 27], [27, 26], [19, 27], [12, 27]]
    assert candidate(words = ['racecar', 'carerac', 'madam', 'level', 'noon', 'civic', 'rotor', 'refer', 'deified', 'redder', 'repaper', 'rotator', 'detartrated', 'reviled', 'repel', 'redivider', 'repaper', 'reviver', 'rotor', 'rotator', 'redder', 'refer', 'civic', 'level', 'rotor', 'repaper', 'rotator', 'deified', 'detartrated', 'refer', 'rotor', 'reviver', 'redder', 'repaper', 'repaper', 'rotor', 'repaper']) == [[3, 23], [5, 22], [6, 35], [7, 29], [8, 27], [9, 32], [10, 36], [11, 26], [12, 28], [16, 36], [17, 31], [18, 35], [19, 26], [20, 32], [21, 29], [24, 35], [25, 36], [30, 35], [33, 36], [34, 36]]
    assert candidate(words = ['aaaa', 'aaab', 'baaa', 'bbbb', 'aaaaa']) == [[1, 2], [2, 1], [0, 4], [4, 0]]
    assert candidate(words = ['a1b', 'b1a', 'abc2', '2cba', 'abcd3', '3dcba', 'abcde4', '4edcba', 'abcdef5', '5fedcba', 'abcdefg6', '6gfedcba', 'abcdefgh7', '7hgfedcba', 'abcdefghi8', '8ihgfedcba']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8], [10, 11], [11, 10], [12, 13], [13, 12], [14, 15], [15, 14]]
    assert candidate(words = ['racecar', 'madam', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid', 'noon', 'civic', 'rotor', 'refer', 'deed', 'level', 'kayak', 'reviled', 'repaid']) == [[2, 11], [3, 12], [4, 13], [5, 14], [6, 15]]
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aa', 'bb', 'cc', 'dd', 'ee', 'a', 'b', 'c', 'd', 'e', '', 'ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'bc', 'cb', 'bd', 'db', 'be', 'eb', 'cd', 'dc', 'ce', 'ec', 'de', 'ed', 'abc', 'cba', 'abd', 'dba', 'abe', 'eba', 'acd', 'dca', 'ace', 'eca', 'ade', 'eda', 'bcd', 'dcb', 'bce', 'ecb', 'bde', 'edb', 'cde', 'edc', 'cef', 'fec', 'def', 'fed', 'cef', 'fec', 'gfe', 'efg', 'geh', 'ehg', 'heg', 'geh', 'hic', 'cih', 'ich', 'hic', 'jid', 'dij', 'idj', 'jid', 'kil', 'lik', 'ilk', 'kil', 'lmn', 'nml', 'mln', 'lmn', 'nop', 'pon', 'opn', 'nop', 'qrs', 'srq', 'rsq', 'qrs', 'tuv', 'vtu', 'utv', 'tuv', 'wxy', 'yxw', 'xyw', 'wxy', 'zzz', 'zz', 'z']) == [[0, 25], [0, 20], [5, 0], [0, 15], [10, 0], [0, 10], [15, 0], [0, 5], [20, 0], [25, 0], [1, 25], [1, 21], [6, 1], [1, 16], [11, 1], [1, 11], [16, 1], [1, 6], [21, 1], [25, 1], [2, 25], [2, 22], [7, 2], [2, 17], [12, 2], [2, 12], [17, 2], [2, 7], [22, 2], [25, 2], [3, 25], [3, 23], [8, 3], [3, 18], [13, 3], [3, 13], [18, 3], [3, 8], [23, 3], [25, 3], [4, 25], [4, 24], [9, 4], [4, 19], [14, 4], [4, 14], [19, 4], [4, 9], [24, 4], [25, 4], [5, 25], [5, 20], [10, 5], [5, 15], [15, 5], [5, 10], [20, 5], [25, 5], [6, 25], [6, 21], [11, 6], [6, 16], [16, 6], [6, 11], [21, 6], [25, 6], [7, 25], [7, 22], [12, 7], [7, 17], [17, 7], [7, 12], [22, 7], [25, 7], [8, 25], [8, 23], [13, 8], [8, 18], [18, 8], [8, 13], [23, 8], [25, 8], [9, 25], [9, 24], [14, 9], [9, 19], [19, 9], [9, 14], [24, 9], [25, 9], [10, 25], [10, 20], [15, 10], [10, 15], [20, 10], [25, 10], [11, 25], [11, 21], [16, 11], [11, 16], [21, 11], [25, 11], [12, 25], [12, 22], [17, 12], [12, 17], [22, 12], [25, 12], [13, 25], [13, 23], [18, 13], [13, 18], [23, 13], [25, 13], [14, 25], [14, 24], [19, 14], [14, 19], [24, 14], [25, 14], [15, 25], [15, 20], [20, 15], [25, 15], [16, 25], [16, 21], [21, 16], [25, 16], [17, 25], [17, 22], [22, 17], [25, 17], [18, 25], [18, 23], [23, 18], [25, 18], [19, 25], [19, 24], [24, 19], [25, 19], [20, 25], [25, 20], [21, 25], [25, 21], [22, 25], [25, 22], [23, 25], [25, 23], [24, 25], [25, 24], [26, 20], [21, 26], [26, 27], [27, 21], [20, 27], [27, 26], [28, 20], [22, 28], [28, 29], [29, 22], [20, 29], [29, 28], [30, 20], [23, 30], [30, 31], [31, 23], [20, 31], [31, 30], [32, 20], [24, 32], [32, 33], [33, 24], [20, 33], [33, 32], [34, 21], [22, 34], [34, 35], [35, 22], [21, 35], [35, 34], [36, 21], [23, 36], [36, 37], [37, 23], [21, 37], [37, 36], [38, 21], [24, 38], [38, 39], [39, 24], [21, 39], [39, 38], [40, 22], [23, 40], [40, 41], [41, 23], [22, 41], [41, 40], [42, 22], [24, 42], [42, 43], [43, 24], [22, 43], [43, 42], [44, 23], [24, 44], [44, 45], [45, 24], [23, 45], [45, 44], [35, 46], [46, 27], [46, 47], [26, 47], [47, 34], [47, 46], [37, 48], [48, 27], [48, 49], [26, 49], [49, 36], [49, 48], [39, 50], [50, 27], [50, 51], [26, 51], [51, 38], [51, 50], [41, 52], [52, 29], [52, 53], [28, 53], [53, 40], [53, 52], [43, 54], [54, 29], [54, 55], [28, 55], [55, 42], [55, 54], [45, 56], [56, 31], [56, 57], [30, 57], [57, 44], [57, 56], [41, 58], [58, 35], [58, 59], [34, 59], [59, 40], [59, 58], [43, 60], [60, 35], [60, 61], [34, 61], [61, 42], [61, 60], [45, 62], [62, 37], [62, 63], [36, 63], [63, 44], [63, 62], [45, 64], [64, 41], [64, 65], [40, 65], [65, 44], [65, 64], [66, 43], [66, 71], [42, 67], [67, 70], [68, 45], [68, 69], [44, 69], [69, 68], [70, 43], [70, 71], [42, 71], [71, 70], [72, 73], [73, 72], [74, 76], [76, 77], [77, 76], [78, 79], [79, 81], [81, 79], [82, 83], [83, 85], [85, 83], [86, 87], [87, 89], [89, 87], [90, 91], [91, 93], [93, 91], [94, 95], [95, 97], [97, 95], [98, 99], [99, 101], [101, 99], [103, 104], [104, 103], [106, 107], [107, 109], [109, 107], [110, 25], [110, 112], [111, 110], [110, 111], [112, 110], [25, 110], [111, 25], [111, 112], [112, 111], [25, 111], [112, 25], [25, 112]]
    assert candidate(words = ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == [[1, 0], [0, 1], [2, 0], [2, 1], [1, 2], [0, 2], [3, 0], [3, 1], [2, 3], [3, 2], [1, 3], [0, 3], [4, 0], [4, 1], [3, 4], [4, 2], [2, 4], [4, 3], [1, 4], [0, 4], [5, 0], [5, 1], [4, 5], [5, 2], [3, 5], [5, 3], [2, 5], [5, 4], [1, 5], [0, 5], [6, 0], [6, 1], [5, 6], [6, 2], [4, 6], [6, 3], [3, 6], [6, 4], [2, 6], [6, 5], [1, 6], [0, 6], [7, 0], [7, 1], [7, 2], [7, 3], [6, 7], [7, 4], [5, 7], [7, 5], [4, 7], [7, 6], [3, 7], [2, 7], [1, 7], [0, 7], [8, 0], [8, 1], [7, 8], [8, 2], [8, 3], [8, 4], [6, 8], [8, 5], [5, 8], [8, 6], [4, 8], [3, 8], [2, 8], [8, 7], [1, 8], [0, 8]]
    assert candidate(words = ['race', 'car', 'level', '', 'deified', 'civic', 'rotor', '', 'madam', 'refer', 'redder', 'repaper', 'reviled', 'deed', 'noon', 'detartrated', 'redivider', 'rotor']) == [[0, 1], [2, 7], [7, 2], [3, 7], [4, 7], [7, 4], [5, 7], [7, 5], [6, 7], [6, 17], [7, 6], [8, 7], [7, 8], [9, 7], [7, 9], [10, 7], [7, 10], [11, 7], [7, 11], [13, 7], [7, 13], [14, 7], [7, 14], [15, 7], [7, 15], [16, 7], [7, 16], [17, 7], [7, 17]]
    assert candidate(words = ['xabc', 'cba', 'abcx', 'abxcba', 'cabxa', 'bxcba', 'abcabc', 'bcabc', 'cbabc', 'xcba', 'bac', 'cabx', 'bacxab', 'xcbax', 'baxcb', 'cbaabc']) == [[1, 0], [2, 1], [2, 9], [2, 5], [9, 2], [11, 10], [0, 13], [13, 2]]
    assert candidate(words = ['ab', 'ba', 'abc', 'cba', 'abcd', 'dcba', 'abcde', 'edcba', 'abcdef', 'fedcba']) == [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2], [4, 3], [4, 5], [2, 5], [5, 4], [6, 5], [6, 7], [4, 7], [7, 6], [8, 7], [8, 9], [6, 9], [9, 8]]
    assert candidate(words = ['noon', 'level', 'deified', 'civic', 'rotor', 'madam', 'refer', 'deed', 'peep', 'radar', 'reviled', 'repaid', 'detartrated', 'reviver', 'redder', 'repaper', 'pepper', 'repel', 'deterred', 'reworded', 'repeal', 'perpet', 'repressed', 'repellet', 'perpetual', 'repellect']) == []
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == []
    assert candidate(words = ['palindrome', 'emordnilap', 'detartrated', 'deified', 'repaid', 'stressed', 'desserts', 'deed', 'civic', 'rotor', 'refer', 'level', 'kayak', 'reviled']) == [[0, 1], [1, 0], [5, 6], [6, 5]]
    assert candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrstu', 'utsrqp', 'vwxyz', 'zyxwv']) == [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]
    assert candidate(words = ['xabcx', 'xbax', 'xcabx', 'xcax', 'xbxc', 'xcabxx', 'xxcabx', 'abcxx', 'xxcba', 'abcdxx', 'xxdcba', 'xxabcd', 'dxxcba', 'xabxx', 'xxbax']) == [[7, 8], [8, 7], [9, 10], [10, 9], [7, 12], [13, 1], [13, 14], [14, 13]]
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2], [3, 0], [2, 3], [3, 1], [1, 3], [3, 2], [0, 3], [4, 0], [3, 4], [4, 1], [2, 4], [4, 2], [1, 4], [4, 3], [0, 4], [5, 0], [4, 5], [5, 1], [3, 5], [5, 2], [2, 5], [5, 3], [1, 5], [5, 4], [0, 5], [6, 0], [5, 6], [6, 1], [4, 6], [6, 2], [3, 6], [6, 3], [2, 6], [6, 4], [1, 6], [6, 5], [0, 6]]
    assert candidate(words = ['', 'a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc', 'aaaaa', 'bbbbb', 'ccccc']) == [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [4, 1], [1, 4], [0, 4], [5, 0], [5, 2], [2, 5], [0, 5], [6, 0], [6, 3], [3, 6], [0, 6], [7, 0], [7, 1], [4, 7], [7, 4], [1, 7], [0, 7], [8, 0], [8, 2], [5, 8], [8, 5], [2, 8], [0, 8], [9, 0], [9, 3], [6, 9], [9, 6], [3, 9], [0, 9], [10, 0], [10, 1], [7, 10], [10, 4], [4, 10], [10, 7], [1, 10], [0, 10], [11, 0], [11, 2], [8, 11], [11, 5], [5, 11], [11, 8], [2, 11], [0, 11], [12, 0], [12, 3], [9, 12], [12, 6], [6, 12], [12, 9], [3, 12], [0, 12], [13, 0], [13, 1], [10, 13], [13, 4], [7, 13], [13, 7], [4, 13], [13, 10], [1, 13], [0, 13], [14, 0], [14, 2], [11, 14], [14, 5], [8, 14], [14, 8], [5, 14], [14, 11], [2, 14], [0, 14], [15, 0], [15, 3], [12, 15], [15, 6], [9, 15], [15, 9], [6, 15], [15, 12], [3, 15], [0, 15]]
    assert candidate(words = ['ab', 'ba', 'a', 'b', 'aba', 'bab', 'aa', 'bb', 'aaa', 'bbb']) == [[0, 2], [3, 0], [0, 1], [1, 3], [2, 1], [1, 0], [0, 4], [4, 1], [1, 5], [5, 0], [6, 2], [2, 6], [7, 3], [3, 7], [8, 2], [6, 8], [8, 6], [2, 8], [9, 3], [7, 9], [9, 7], [3, 9]]
    assert candidate(words = ['race', 'ecar', 'car', 'arc', 'civic', 'level', 'deified', 'rotor', 'redder', 'repaper']) == [[0, 2], [0, 1], [1, 0]]
    assert candidate(words = ['noon', 'moon', 'noonmoon', 'moonnoon', 'noonno', 'onnoon', 'noonmo', 'onnoom']) == [[4, 5], [5, 4]]
    assert candidate(words = ['aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa']) == [[0, 1], [1, 0], [1, 2], [0, 2], [2, 0], [2, 1], [2, 3], [1, 3], [0, 3], [3, 0], [3, 1], [3, 2], [3, 4], [2, 4], [1, 4], [0, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5]]
    assert candidate(words = ['12321', '21312', '32123', '43234', '54345', '65456', '76567', '87678', '98789', '10901', '11011']) == []


