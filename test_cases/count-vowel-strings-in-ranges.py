def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'cde', 'ua'],queries = [[0, 0], [1, 2], [0, 3]]) == [1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'cde', 'ua'],queries = [[0, 0], [1, 2], [0, 3]]) == [1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 3], [1, 2], [2, 2]]) == [1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 3], [1, 2], [2, 2]]) == [1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'cde', 'aeiou'],queries = [[0, 3], [1, 2], [3, 3]]) == [2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'cde', 'aeiou'],queries = [[0, 3], [1, 2], [3, 3]]) == [2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'ee', 'iii', 'oo', 'uu'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'ee', 'iii', 'oo', 'uu'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [1, 3], [2, 3]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [1, 3], [2, 3]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [1, 3], [0, 3]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [1, 3], [0, 3]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aba', 'bcb', 'ece', 'aa', 'e'],queries = [[0, 2], [1, 4], [1, 1]]) == [2, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aba', 'bcb', 'ece', 'aa', 'e'],queries = [[0, 2], [1, 4], [1, 1]]) == [2, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [2, 3], [0, 3]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [2, 3], [0, 3]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'eae'],queries = [[0, 4], [1, 3], [2, 2]]) == [2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'eae'],queries = [[0, 4], [1, 3], [2, 2]]) == [2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dea', 'eae'],queries = [[0, 1], [1, 3], [2, 4]]) == [0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dea', 'eae'],queries = [[0, 1], [1, 3], [2, 4]]) == [0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i'],queries = [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i'],queries = [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 3], [1, 2], [2, 2]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 3], [1, 2], [2, 2]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],queries = [[0, 4], [1, 3], [2, 2]]) == [2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],queries = [[0, 4], [1, 3], [2, 2]]) == [2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'eoe'],queries = [[0, 0], [1, 2], [0, 2]]) == [1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'eoe'],queries = [[0, 0], [1, 2], [0, 2]]) == [1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeioua', 'beoibe', 'ieoiie', 'oioioi', 'uaouau', 'aeiou', 'eioue', 'iouoi', 'ououo', 'uouou'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == [9, 7, 6, 4, 2, 4, 5, 2, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeioua', 'beoibe', 'ieoiie', 'oioioi', 'uaouau', 'aeiou', 'eioue', 'iouoi', 'ououo', 'uouou'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == [9, 7, 6, 4, 2, 4, 5, 2, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'aeiouaeiou'],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 0], [7, 7]]) == [8, 6, 4, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'aeiouaeiou'],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 0], [7, 7]]) == [8, 6, 4, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ae', 'ea', 'aa', 'ee', 'ii', 'oo', 'uu', 'aee', 'eaa', 'iee'],queries = [[0, 9], [0, 5], [5, 9], [3, 6], [7, 8]]) == [10, 6, 5, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ae', 'ea', 'aa', 'ee', 'ii', 'oo', 'uu', 'aee', 'eaa', 'iee'],queries = [[0, 9], [0, 5], [5, 9], [3, 6], [7, 8]]) == [10, 6, 5, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou'],queries = [[0, 0]]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou'],queries = [[0, 0]]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'umbrella', 'elephant', 'ice'],queries = [[0, 2], [1, 4], [2, 2], [3, 4], [0, 4]]) == [3, 3, 1, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'umbrella', 'elephant', 'ice'],queries = [[0, 2], [1, 4], [2, 2], [3, 4], [0, 4]]) == [3, 3, 1, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['automobile', 'bicycle', 'car', 'plane', 'ship', 'train', 'truck', 'motorcycle', 'bus', 'ferry'],queries = [[0, 4], [1, 5], [2, 8], [0, 9], [1, 6], [2, 4], [3, 7], [0, 7], [8, 9]]) == [1, 0, 0, 1, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['automobile', 'bicycle', 'car', 'plane', 'ship', 'train', 'truck', 'motorcycle', 'bus', 'ferry'],queries = [[0, 4], [1, 5], [2, 8], [0, 9], [1, 6], [2, 4], [3, 7], [0, 7], [8, 9]]) == [1, 0, 0, 1, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['education', 'environment', 'algorithm', 'finance', 'economics', 'optimization', 'development'],queries = [[0, 2], [3, 5], [0, 6], [2, 4], [1, 3], [0, 5], [4, 6]]) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['education', 'environment', 'algorithm', 'finance', 'economics', 'optimization', 'development'],queries = [[0, 2], [3, 5], [0, 6], [2, 4], [1, 3], [0, 5], [4, 6]]) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['umbrella', 'elephant', 'ice', 'onion', 'apple', 'orange'],queries = [[0, 2], [1, 5], [3, 4], [0, 1], [2, 3]]) == [2, 3, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['umbrella', 'elephant', 'ice', 'onion', 'apple', 'orange'],queries = [[0, 2], [1, 5], [3, 4], [0, 1], [2, 3]]) == [2, 3, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'grape', 'kiwi', 'lemon', 'melon', 'mango', 'peach', 'pear', 'plum'],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 5], [6, 6], [7, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'grape', 'kiwi', 'lemon', 'melon', 'mango', 'peach', 'pear', 'plum'],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 5], [6, 6], [7, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'eoo', 'i', 'oee', 'u', 'aa', 'e', 'i', 'o', 'u'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9]]) == [9, 8, 6, 4, 2, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'eoo', 'i', 'oee', 'u', 'aa', 'e', 'i', 'o', 'u'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9]]) == [9, 8, 6, 4, 2, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],queries = [[0, 12], [1, 11], [2, 10], [3, 9], [4, 8]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],queries = [[0, 12], [1, 11], [2, 10], [3, 9], [4, 8]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff', 'gggggg'],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]]) == [1, 0, 0, 1, 1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff', 'gggggg'],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]]) == [1, 0, 0, 1, 1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [0, 3], [1, 4]]) == [1, 1, 1, 1, 1, 5, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [0, 3], [1, 4]]) == [1, 1, 1, 1, 1, 5, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'efg', 'hij', 'klm', 'nop', 'qrstu', 'vwxyz', 'yzzzy', 'uaeuu'],queries = [[0, 9], [1, 3], [2, 8], [4, 7], [5, 5]]) == [2, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'efg', 'hij', 'klm', 'nop', 'qrstu', 'vwxyz', 'yzzzy', 'uaeuu'],queries = [[0, 9], [1, 3], [2, 8], [4, 7], [5, 5]]) == [2, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'aa', 'ee', 'ii', 'oo', 'uu', 'aaa', 'eee', 'iii', 'ooo', 'uuu'],queries = [[0, 4], [5, 9], [10, 14], [0, 9], [5, 14], [0, 14], [1, 13]]) == [5, 5, 5, 10, 10, 15, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'aa', 'ee', 'ii', 'oo', 'uu', 'aaa', 'eee', 'iii', 'ooo', 'uuu'],queries = [[0, 4], [5, 9], [10, 14], [0, 9], [5, 14], [0, 14], [1, 13]]) == [5, 5, 5, 10, 10, 15, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'apple', 'grape', 'kiwi', 'melon', 'peach', 'pear'],queries = [[0, 3], [2, 5], [1, 6], [0, 6], [4, 4]]) == [1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'apple', 'grape', 'kiwi', 'melon', 'peach', 'pear'],queries = [[0, 3], [2, 5], [1, 6], [0, 6], [4, 4]]) == [1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiouaeiou', 'bcdefghijklmno', 'pqrstuvwxyzz', 'zyxwvutsrqponmlkjihgfedcba', 'aeiouaeiouaeiou'],queries = [[0, 4], [1, 3], [0, 0], [2, 2], [1, 4]]) == [2, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiouaeiou', 'bcdefghijklmno', 'pqrstuvwxyzz', 'zyxwvutsrqponmlkjihgfedcba', 'aeiouaeiouaeiou'],queries = [[0, 4], [1, 3], [0, 0], [2, 2], [1, 4]]) == [2, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['education', 'university', 'college', 'school', 'academy', 'institute', 'faculty', 'student', 'teacher', 'research'],queries = [[0, 9], [1, 4], [2, 6], [3, 8], [4, 7]]) == [1, 0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['education', 'university', 'college', 'school', 'academy', 'institute', 'faculty', 'student', 'teacher', 'research'],queries = [[0, 9], [1, 4], [2, 6], [3, 8], [4, 7]]) == [1, 0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['umbrella', 'elephant', 'ice', 'onion', 'apple', 'orange', 'grape'],queries = [[0, 6], [1, 5], [2, 4], [0, 1], [5, 6], [2, 3], [4, 4]]) == [4, 3, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['umbrella', 'elephant', 'ice', 'onion', 'apple', 'orange', 'grape'],queries = [[0, 6], [1, 5], [2, 4], [0, 1], [5, 6], [2, 3], [4, 4]]) == [4, 3, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [3, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [3, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'eeeee', 'iiii', 'oooo', 'uuuu', 'aeiou', 'uoiea'],queries = [[0, 4], [3, 6], [0, 3], [4, 4], [5, 6], [1, 1], [2, 2]]) == [5, 4, 4, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'eeeee', 'iiii', 'oooo', 'uuuu', 'aeiou', 'uoiea'],queries = [[0, 4], [3, 6], [0, 3], [4, 4], [5, 6], [1, 1], [2, 2]]) == [5, 4, 4, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dea', 'aeiou', 'uoiea'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5]]) == [2, 1, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dea', 'aeiou', 'uoiea'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5]]) == [2, 1, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea'],queries = [[0, 6], [1, 5], [2, 4], [0, 3], [3, 6]]) == [7, 5, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea'],queries = [[0, 6], [1, 5], [2, 4], [0, 3], [3, 6]]) == [7, 5, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'io', 'ua'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 0], [9, 9]]) == [10, 8, 6, 4, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'io', 'ua'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 0], [9, 9]]) == [10, 8, 6, 4, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'banana', 'grape', 'peach'],queries = [[0, 2], [1, 3], [0, 3], [2, 2], [3, 3], [1, 4], [0, 4]]) == [2, 1, 2, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'banana', 'grape', 'peach'],queries = [[0, 2], [1, 3], [0, 3], [2, 2], [3, 3], [1, 4], [0, 4]]) == [2, 1, 2, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['bcd'],queries = [[0, 0]]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['bcd'],queries = [[0, 0]]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'apricot', 'grape', 'kiwi', 'peach', 'melon'],queries = [[0, 5], [1, 3], [2, 4], [0, 2], [3, 5]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'apricot', 'grape', 'kiwi', 'peach', 'melon'],queries = [[0, 5], [1, 3], [2, 4], [0, 2], [3, 5]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [0, 9]]) == [3, 4, 4, 5, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [0, 9]]) == [3, 4, 4, 5, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],queries = [[0, 14], [0, 9], [5, 10], [10, 14]]) == [4, 3, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],queries = [[0, 14], [0, 9], [5, 10], [10, 14]]) == [4, 3, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu'],queries = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 8], [1, 9], [0, 7], [2, 5]]) == [2, 0, 0, 0, 2, 1, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu'],queries = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 8], [1, 9], [0, 7], [2, 5]]) == [2, 0, 0, 0, 2, 1, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'grape', 'avocado', 'kiwi', 'melon', 'orange', 'elderberry'],queries = [[0, 6], [1, 5], [2, 4], [3, 3], [0, 3]]) == [2, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'grape', 'avocado', 'kiwi', 'melon', 'orange', 'elderberry'],queries = [[0, 6], [1, 5], [2, 4], [3, 3], [0, 3]]) == [2, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['x', 'y', 'z', 'aeiou', 'aeiou', 'aeiou'],queries = [[0, 2], [2, 4], [4, 5], [0, 5]]) == [0, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['x', 'y', 'z', 'aeiou', 'aeiou', 'aeiou'],queries = [[0, 2], [2, 4], [4, 5], [0, 5]]) == [0, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [3, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [3, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]) == [4, 3, 3, 3, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]) == [4, 3, 3, 3, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'ia', 'uo'],queries = [[0, 5], [2, 8], [1, 4], [0, 9], [3, 7], [5, 9], [0, 0], [9, 9]]) == [6, 7, 4, 10, 5, 5, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'ia', 'uo'],queries = [[0, 5], [2, 8], [1, 4], [0, 9], [3, 7], [5, 9], [0, 0], [9, 9]]) == [6, 7, 4, 10, 5, 5, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [0, 1, 1, 1, 1, 0, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'uo', 'ea'],queries = [[0, 9], [0, 5], [5, 9], [3, 6], [7, 8]]) == [10, 6, 5, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'uo', 'ea'],queries = [[0, 9], [0, 5], [5, 9], [3, 6], [7, 8]]) == [10, 6, 5, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'aee', 'oau', 'bcd', 'eaa'],queries = [[0, 2], [1, 5], [3, 5], [0, 5]]) == [2, 3, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'aee', 'oau', 'bcd', 'eaa'],queries = [[0, 2], [1, 5], [3, 5], [0, 5]]) == [2, 3, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'umbrella', 'elephant', 'ice', 'onion'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5]]) == [4, 3, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'umbrella', 'elephant', 'ice', 'onion'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5]]) == [4, 3, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvw', 'xyz'],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 0], [7, 7]]) == [1, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvw', 'xyz'],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 0], [7, 7]]) == [1, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'eee', 'iii', 'ooo', 'uuu', 'aa', 'ee', 'ii', 'oo', 'uu'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9]]) == [10, 8, 6, 4, 2, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'eee', 'iii', 'ooo', 'uuu', 'aa', 'ee', 'ii', 'oo', 'uu'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9]]) == [10, 8, 6, 4, 2, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'avocado', 'elderberry', 'kiwi', 'grape', 'lemon'],queries = [[0, 2], [1, 5], [2, 3], [0, 5]]) == [1, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'avocado', 'elderberry', 'kiwi', 'grape', 'lemon'],queries = [[0, 2], [1, 5], [2, 3], [0, 5]]) == [1, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'ocean', 'elephant', 'umbrella'],queries = [[0, 0], [0, 4], [1, 2], [2, 3], [3, 4], [0, 3], [1, 4]]) == [1, 2, 0, 0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'ocean', 'elephant', 'umbrella'],queries = [[0, 0], [0, 4], [1, 2], [2, 3], [3, 4], [0, 3], [1, 4]]) == [1, 2, 0, 0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['under', 'over', 'around', 'before', 'after', 'above', 'below'],queries = [[0, 1], [2, 4], [1, 3], [0, 6], [5, 5]]) == [0, 0, 0, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['under', 'over', 'around', 'before', 'after', 'above', 'below'],queries = [[0, 1], [2, 4], [1, 3], [0, 6], [5, 5]]) == [0, 0, 0, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 5], [5, 10], [10, 15], [15, 20]]) == [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 6, 6, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 5], [5, 10], [10, 15], [15, 20]]) == [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 6, 6, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'eae', 'oio', 'uaa'],queries = [[0, 2], [1, 4], [0, 4]]) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'eae', 'oio', 'uaa'],queries = [[0, 2], [1, 4], [0, 4]]) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'ccbbdd', 'ddeerr', 'eeffgg', 'ffggee', 'gghhee', 'hhiig', 'iihhj'],queries = [[0, 2], [1, 5], [2, 7], [0, 8], [1, 6], [2, 4], [3, 7], [0, 7], [8, 9]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'ccbbdd', 'ddeerr', 'eeffgg', 'ffggee', 'gghhee', 'hhiig', 'iihhj'],queries = [[0, 2], [1, 5], [2, 7], [0, 8], [1, 6], [2, 4], [3, 7], [0, 7], [8, 9]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'science', 'python', 'java', 'c++', 'javascript'],queries = [[0, 2], [3, 5], [1, 4], [0, 6], [5, 5], [2, 3], [4, 6]]) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'science', 'python', 'java', 'c++', 'javascript'],queries = [[0, 2], [3, 5], [1, 4], [0, 6], [5, 5], [2, 3], [4, 6]]) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 4], [1, 7], [2, 8], [3, 9], [0, 9]]) == [4, 6, 6, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 4], [1, 7], [2, 8], [3, 9], [0, 9]]) == [4, 6, 6, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcdfg', 'ae', 'iou', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 8], [1, 5], [2, 7], [3, 6], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [8, 4, 6, 4, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcdfg', 'ae', 'iou', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 8], [1, 5], [2, 7], [3, 6], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [8, 4, 6, 4, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4]]) == [6, 4, 2, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4]]) == [6, 4, 2, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],queries = [[0, 5], [1, 4], [0, 0], [5, 5]]) == [6, 4, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],queries = [[0, 5], [1, 4], [0, 0], [5, 5]]) == [6, 4, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'umbrella', 'echo', 'alpha'],queries = [[0, 4], [1, 3], [0, 0], [2, 2], [1, 4]]) == [5, 3, 1, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'umbrella', 'echo', 'alpha'],queries = [[0, 4], [1, 3], [0, 0], [2, 2], [1, 4]]) == [5, 3, 1, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7], [0, 9], [1, 8]]) == [15, 13, 11, 9, 7, 5, 3, 1, 10, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7], [0, 9], [1, 8]]) == [15, 13, 11, 9, 7, 5, 3, 1, 10, 8]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'bcd'],queries = [[0, 6], [1, 5], [2, 7], [3, 3]]) == [7, 5, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'bcd'],queries = [[0, 6], [1, 5], [2, 7], [3, 3]]) == [7, 5, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 6], [1, 5], [2, 4]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 6], [1, 5], [2, 4]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['amplifier', 'equalizer', 'microphone', 'audio', 'sound', 'voice', 'volume', 'level', 'peak', 'gain'],queries = [[0, 2], [1, 5], [2, 7], [3, 8], [4, 9], [0, 9]]) == [0, 1, 1, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['amplifier', 'equalizer', 'microphone', 'audio', 'sound', 'voice', 'volume', 'level', 'peak', 'gain'],queries = [[0, 2], [1, 5], [2, 7], [3, 8], [4, 9], [0, 9]]) == [0, 1, 1, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'datastructure', 'programming', 'python', 'java', 'csharp', 'javascript', 'html', 'css', 'vue'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'datastructure', 'programming', 'python', 'java', 'csharp', 'javascript', 'html', 'css', 'vue'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 15], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == [4, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 15], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == [4, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['strawberry', 'blueberry', 'raspberry', 'blackberry', 'kiwi', 'mango', 'papaya'],queries = [[0, 6], [1, 5], [2, 4], [0, 1], [5, 6]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['strawberry', 'blueberry', 'raspberry', 'blackberry', 'kiwi', 'mango', 'papaya'],queries = [[0, 6], [1, 5], [2, 4], [0, 1], [5, 6]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbaa', 'abcd', 'dcba', 'efgh', 'hgfe', 'ijkl', 'lkji', 'mnop', 'ponm'],queries = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9]]) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbaa', 'abcd', 'dcba', 'efgh', 'hgfe', 'ijkl', 'lkji', 'mnop', 'ponm'],queries = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9]]) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'engine', 'idea', 'open', 'ocean', 'under', 'education'],queries = [[0, 2], [1, 5], [2, 6], [0, 6]]) == [2, 2, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'engine', 'idea', 'open', 'ocean', 'under', 'education'],queries = [[0, 2], [1, 5], [2, 6], [0, 6]]) == [2, 2, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'ananas', 'acerola', 'banana', 'manga', 'abacaxi', 'manga', 'banana'],queries = [[0, 3], [4, 7], [0, 4], [3, 6], [1, 5], [2, 2], [6, 7]]) == [2, 1, 2, 1, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'ananas', 'acerola', 'banana', 'manga', 'abacaxi', 'manga', 'banana'],queries = [[0, 3], [4, 7], [0, 4], [3, 6], [1, 5], [2, 2], [6, 7]]) == [2, 1, 2, 1, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['umbrella', 'orange', 'apple', 'elephant', 'ocean', 'idea', 'education'],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]]) == [2, 2, 1, 0, 1, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['umbrella', 'orange', 'apple', 'elephant', 'ocean', 'idea', 'education'],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]]) == [2, 2, 1, 0, 1, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ae', 'ei', 'ou', 'ia', 'oe', 'uo', 'oi', 'ie', 'oa', 'eu'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [0, 3], [1, 7], [2, 6]]) == [10, 8, 6, 4, 2, 5, 5, 4, 7, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ae', 'ei', 'ou', 'ia', 'oe', 'uo', 'oi', 'ie', 'oa', 'eu'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [0, 3], [1, 7], [2, 6]]) == [10, 8, 6, 4, 2, 5, 5, 4, 7, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'umbrella', 'electric', 'ice', 'onion', 'octopus'],queries = [[0, 6], [1, 3], [2, 5], [0, 0], [6, 6], [3, 4], [1, 5]]) == [4, 2, 2, 1, 0, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'umbrella', 'electric', 'ice', 'onion', 'octopus'],queries = [[0, 6], [1, 3], [2, 5], [0, 0], [6, 6], [3, 4], [1, 5]]) == [4, 2, 2, 1, 0, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'e', 'i', 'o', 'u', 'vowel', 'nonvowel'],queries = [[0, 6], [1, 5], [2, 4], [3, 3], [4, 4]]) == [5, 4, 3, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'e', 'i', 'o', 'u', 'vowel', 'nonvowel'],queries = [[0, 6], [1, 5], [2, 4], [3, 3], [4, 4]]) == [5, 4, 3, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeioua', 'aeioue', 'aeiouo', 'aeioui', 'aeiouu', 'euoeu', 'iuoie', 'oueia', 'uaeio', 'eaoui'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [0, 3], [1, 7], [2, 6]]) == [10, 8, 6, 4, 2, 5, 5, 4, 7, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeioua', 'aeioue', 'aeiouo', 'aeioui', 'aeiouu', 'euoeu', 'iuoie', 'oueia', 'uaeio', 'eaoui'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [0, 3], [1, 7], [2, 6]]) == [10, 8, 6, 4, 2, 5, 5, 4, 7, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'structure', 'design', 'computer', 'science', 'software', 'engineering'],queries = [[0, 3], [1, 5], [2, 7], [0, 8], [1, 6], [2, 4], [3, 7], [0, 7]]) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'structure', 'design', 'computer', 'science', 'software', 'engineering'],queries = [[0, 3], [1, 5], [2, 7], [0, 8], [1, 6], [2, 4], [3, 7], [0, 7]]) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ddeeff', 'gg', 'hhii', 'jjkk', 'llmm', 'nnoopp', 'qqrr', 'ssttuu', 'vvww'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ddeeff', 'gg', 'hhii', 'jjkk', 'llmm', 'nnoopp', 'qqrr', 'ssttuu', 'vvww'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'eae', 'oio', 'uaa', 'aeiou', 'bcd', 'eae', 'oio', 'uaa'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [0, 4], [1, 9]]) == [8, 6, 5, 3, 2, 5, 4, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'eae', 'oio', 'uaa', 'aeiou', 'bcd', 'eae', 'oio', 'uaa'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [0, 4], [1, 9]]) == [8, 6, 5, 3, 2, 5, 4, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'ice', 'elephant', 'umbrella'],queries = [[0, 1], [1, 3], [2, 4], [0, 4]]) == [2, 2, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'ice', 'elephant', 'umbrella'],queries = [[0, 1], [1, 3], [2, 4], [0, 4]]) == [2, 2, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'bcd', 'eee', 'oee', 'uau'],queries = [[0, 4], [1, 3], [2, 4], [0, 0], [4, 4]]) == [4, 2, 3, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'bcd', 'eee', 'oee', 'uau'],queries = [[0, 4], [1, 3], [2, 4], [0, 0], [4, 4]]) == [4, 2, 3, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['umbrella', 'raincoat', 'umbrella', 'hat', 'scarf', 'umbrella', 'umbrella', 'raincoat'],queries = [[0, 3], [4, 7], [0, 4], [3, 6], [1, 5], [0, 6], [2, 2], [5, 7]]) == [2, 2, 2, 2, 2, 4, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['umbrella', 'raincoat', 'umbrella', 'hat', 'scarf', 'umbrella', 'umbrella', 'raincoat'],queries = [[0, 3], [4, 7], [0, 4], [3, 6], [1, 5], [0, 6], [2, 2], [5, 7]]) == [2, 2, 2, 2, 2, 4, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 4], [1, 3], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == [4, 3, 3, 3, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 4], [1, 3], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == [4, 3, 3, 3, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvw', 'xyz'],queries = [[0, 6], [1, 5], [2, 4], [0, 2], [3, 5], [0, 6], [6, 6]]) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvw', 'xyz'],queries = [[0, 6], [1, 5], [2, 4], [0, 2], [3, 5], [0, 6], [6, 6]]) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiouaeiou', 'bcd', 'eee', 'oau', 'bcd', 'eaa', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 4], [1, 7], [3, 8], [0, 9], [5, 5]]) == [3, 4, 3, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiouaeiou', 'bcd', 'eee', 'oau', 'bcd', 'eaa', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 4], [1, 7], [3, 8], [0, 9], [5, 5]]) == [3, 4, 3, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'eeffgg', 'hhhiii', 'jjjkll', 'mmmoonnn', 'pppqqq', 'rrrsss', 'tttuuu', 'vvvwww', 'xxxyyy'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'eeffgg', 'hhhiii', 'jjjkll', 'mmmoonnn', 'pppqqq', 'rrrsss', 'tttuuu', 'vvvwww', 'xxxyyy'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'orange', 'banana', 'umbrella', 'ice', 'elephant', 'octopus'],queries = [[0, 2], [3, 6], [0, 6], [2, 4]]) == [2, 2, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'orange', 'banana', 'umbrella', 'ice', 'elephant', 'octopus'],queries = [[0, 2], [3, 6], [0, 6], [2, 4]]) == [2, 2, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'apple', 'orange', 'grape', 'kiwi'],queries = [[0, 4], [1, 2], [2, 3], [3, 4], [0, 3]]) == [2, 2, 1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'apple', 'orange', 'grape', 'kiwi'],queries = [[0, 4], [1, 2], [2, 3], [3, 4], [0, 3]]) == [2, 2, 1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aeiou', 'banana', 'grape', 'kiwi', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == [6, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aeiou', 'banana', 'grape', 'kiwi', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == [6, 4, 3, 2, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['aeiou', 'bcd', 'cde', 'ua'],queries = [[0, 0], [1, 2], [0, 3]]) == [1, 0, 2]
    assert candidate(words = ['aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 3], [1, 2], [2, 2]]) == [1, 0, 0]
    assert candidate(words = ['aeiou', 'bcd', 'cde', 'aeiou'],queries = [[0, 3], [1, 2], [3, 3]]) == [2, 0, 1]
    assert candidate(words = ['aaaa', 'ee', 'iii', 'oo', 'uu'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 1, 1, 1, 1]
    assert candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [1, 3], [2, 3]]) == [0, 0, 0]
    assert candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [1, 3], [0, 3]]) == [0, 0, 0]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 1, 1, 1, 1]
    assert candidate(words = ['aba', 'bcb', 'ece', 'aa', 'e'],queries = [[0, 2], [1, 4], [1, 1]]) == [2, 3, 0]
    assert candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 1], [2, 3], [0, 3]]) == [0, 0, 0]
    assert candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'eae'],queries = [[0, 4], [1, 3], [2, 2]]) == [2, 0, 0]
    assert candidate(words = ['abc', 'bcd', 'cde', 'dea', 'eae'],queries = [[0, 1], [1, 3], [2, 4]]) == [0, 0, 1]
    assert candidate(words = ['a', 'e', 'i'],queries = [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1]
    assert candidate(words = ['abc', 'bcd', 'cde', 'dea'],queries = [[0, 3], [1, 2], [2, 2]]) == [0, 0, 0]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [1, 0, 0, 0, 1]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],queries = [[0, 4], [1, 3], [2, 2]]) == [2, 0, 0]
    assert candidate(words = ['aeiou', 'bcd', 'eoe'],queries = [[0, 0], [1, 2], [0, 2]]) == [1, 1, 2]
    assert candidate(words = ['aeioua', 'beoibe', 'ieoiie', 'oioioi', 'uaouau', 'aeiou', 'eioue', 'iouoi', 'ououo', 'uouou'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == [9, 7, 6, 4, 2, 4, 5, 2, 3, 3, 3, 3, 3, 3]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'aeiouaeiou'],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 0], [7, 7]]) == [8, 6, 4, 2, 1, 1]
    assert candidate(words = ['ae', 'ea', 'aa', 'ee', 'ii', 'oo', 'uu', 'aee', 'eaa', 'iee'],queries = [[0, 9], [0, 5], [5, 9], [3, 6], [7, 8]]) == [10, 6, 5, 4, 2]
    assert candidate(words = ['aeiou'],queries = [[0, 0]]) == [1]
    assert candidate(words = ['apple', 'orange', 'umbrella', 'elephant', 'ice'],queries = [[0, 2], [1, 4], [2, 2], [3, 4], [0, 4]]) == [3, 3, 1, 1, 4]
    assert candidate(words = ['automobile', 'bicycle', 'car', 'plane', 'ship', 'train', 'truck', 'motorcycle', 'bus', 'ferry'],queries = [[0, 4], [1, 5], [2, 8], [0, 9], [1, 6], [2, 4], [3, 7], [0, 7], [8, 9]]) == [1, 0, 0, 1, 0, 0, 0, 1, 0]
    assert candidate(words = ['education', 'environment', 'algorithm', 'finance', 'economics', 'optimization', 'development'],queries = [[0, 2], [3, 5], [0, 6], [2, 4], [1, 3], [0, 5], [4, 6]]) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['umbrella', 'elephant', 'ice', 'onion', 'apple', 'orange'],queries = [[0, 2], [1, 5], [3, 4], [0, 1], [2, 3]]) == [2, 3, 1, 1, 1]
    assert candidate(words = ['banana', 'grape', 'kiwi', 'lemon', 'melon', 'mango', 'peach', 'pear', 'plum'],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 5], [6, 6], [7, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['aabbcc', 'eoo', 'i', 'oee', 'u', 'aa', 'e', 'i', 'o', 'u'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9]]) == [9, 8, 6, 4, 2, 4, 5]
    assert candidate(words = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],queries = [[0, 12], [1, 11], [2, 10], [3, 9], [4, 8]]) == [0, 0, 0, 0, 0]
    assert candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff', 'gggggg'],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]]) == [1, 0, 0, 1, 1, 0, 2]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [0, 3], [1, 4]]) == [1, 1, 1, 1, 1, 5, 4, 4]
    assert candidate(words = ['aeiou', 'bcd', 'efg', 'hij', 'klm', 'nop', 'qrstu', 'vwxyz', 'yzzzy', 'uaeuu'],queries = [[0, 9], [1, 3], [2, 8], [4, 7], [5, 5]]) == [2, 0, 0, 0, 0]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aa', 'ee', 'ii', 'oo', 'uu', 'aaa', 'eee', 'iii', 'ooo', 'uuu'],queries = [[0, 4], [5, 9], [10, 14], [0, 9], [5, 14], [0, 14], [1, 13]]) == [5, 5, 5, 10, 10, 15, 13]
    assert candidate(words = ['banana', 'apple', 'grape', 'kiwi', 'melon', 'peach', 'pear'],queries = [[0, 3], [2, 5], [1, 6], [0, 6], [4, 4]]) == [1, 0, 1, 1, 0]
    assert candidate(words = ['aeiouaeiou', 'bcdefghijklmno', 'pqrstuvwxyzz', 'zyxwvutsrqponmlkjihgfedcba', 'aeiouaeiouaeiou'],queries = [[0, 4], [1, 3], [0, 0], [2, 2], [1, 4]]) == [2, 0, 1, 0, 1]
    assert candidate(words = ['education', 'university', 'college', 'school', 'academy', 'institute', 'faculty', 'student', 'teacher', 'research'],queries = [[0, 9], [1, 4], [2, 6], [3, 8], [4, 7]]) == [1, 0, 1, 1, 1]
    assert candidate(words = ['umbrella', 'elephant', 'ice', 'onion', 'apple', 'orange', 'grape'],queries = [[0, 6], [1, 5], [2, 4], [0, 1], [5, 6], [2, 3], [4, 4]]) == [4, 3, 2, 1, 1, 1, 1]
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [3, 2, 1, 1, 1]
    assert candidate(words = ['aaaa', 'eeeee', 'iiii', 'oooo', 'uuuu', 'aeiou', 'uoiea'],queries = [[0, 4], [3, 6], [0, 3], [4, 4], [5, 6], [1, 1], [2, 2]]) == [5, 4, 4, 1, 2, 1, 1]
    assert candidate(words = ['abc', 'bcd', 'cde', 'dea', 'aeiou', 'uoiea'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5]]) == [2, 1, 0, 0, 1]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea'],queries = [[0, 6], [1, 5], [2, 4], [0, 3], [3, 6]]) == [7, 5, 3, 4, 4]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'io', 'ua'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 0], [9, 9]]) == [10, 8, 6, 4, 2, 1, 1]
    assert candidate(words = ['apple', 'orange', 'banana', 'grape', 'peach'],queries = [[0, 2], [1, 3], [0, 3], [2, 2], [3, 3], [1, 4], [0, 4]]) == [2, 1, 2, 0, 0, 1, 2]
    assert candidate(words = ['bcd'],queries = [[0, 0]]) == [0]
    assert candidate(words = ['banana', 'apricot', 'grape', 'kiwi', 'peach', 'melon'],queries = [[0, 5], [1, 3], [2, 4], [0, 2], [3, 5]]) == [0, 0, 0, 0, 0]
    assert candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [0, 9]]) == [3, 4, 4, 5, 5, 7]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],queries = [[0, 14], [0, 9], [5, 10], [10, 14]]) == [4, 3, 1, 1]
    assert candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu'],queries = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 8], [1, 9], [0, 7], [2, 5]]) == [2, 0, 0, 0, 2, 1, 2, 0]
    assert candidate(words = ['banana', 'grape', 'avocado', 'kiwi', 'melon', 'orange', 'elderberry'],queries = [[0, 6], [1, 5], [2, 4], [3, 3], [0, 3]]) == [2, 2, 1, 0, 1]
    assert candidate(words = ['x', 'y', 'z', 'aeiou', 'aeiou', 'aeiou'],queries = [[0, 2], [2, 4], [4, 5], [0, 5]]) == [0, 2, 2, 3]
    assert candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [3, 2, 1, 1, 1]
    assert candidate(words = ['aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 15], [1, 14], [2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]) == [4, 3, 3, 3, 2, 1, 1, 1]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'ia', 'uo'],queries = [[0, 5], [2, 8], [1, 4], [0, 9], [3, 7], [5, 9], [0, 0], [9, 9]]) == [6, 7, 4, 10, 5, 5, 1, 1]
    assert candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'ae', 'ei', 'ou', 'uo', 'ea'],queries = [[0, 9], [0, 5], [5, 9], [3, 6], [7, 8]]) == [10, 6, 5, 4, 2]
    assert candidate(words = ['aeiou', 'bcd', 'aee', 'oau', 'bcd', 'eaa'],queries = [[0, 2], [1, 5], [3, 5], [0, 5]]) == [2, 3, 2, 4]
    assert candidate(words = ['apple', 'orange', 'umbrella', 'elephant', 'ice', 'onion'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5]]) == [4, 3, 1, 1, 0]
    assert candidate(words = ['aeiou', 'bcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvw', 'xyz'],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 0], [7, 7]]) == [1, 0, 0, 0, 1, 0]
    assert candidate(words = ['aaa', 'eee', 'iii', 'ooo', 'uuu', 'aa', 'ee', 'ii', 'oo', 'uu'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9]]) == [10, 8, 6, 4, 2, 5, 5]
    assert candidate(words = ['banana', 'avocado', 'elderberry', 'kiwi', 'grape', 'lemon'],queries = [[0, 2], [1, 5], [2, 3], [0, 5]]) == [1, 1, 0, 1]
    assert candidate(words = ['aeiou', 'bcd', 'ocean', 'elephant', 'umbrella'],queries = [[0, 0], [0, 4], [1, 2], [2, 3], [3, 4], [0, 3], [1, 4]]) == [1, 2, 0, 0, 1, 1, 1]
    assert candidate(words = ['under', 'over', 'around', 'before', 'after', 'above', 'below'],queries = [[0, 1], [2, 4], [1, 3], [0, 6], [5, 5]]) == [0, 0, 0, 1, 1]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10], [0, 5], [5, 10], [10, 15], [15, 20]]) == [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 6, 6, 6, 5]
    assert candidate(words = ['aeiou', 'bcd', 'eae', 'oio', 'uaa'],queries = [[0, 2], [1, 4], [0, 4]]) == [2, 3, 4]
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'ccbbdd', 'ddeerr', 'eeffgg', 'ffggee', 'gghhee', 'hhiig', 'iihhj'],queries = [[0, 2], [1, 5], [2, 7], [0, 8], [1, 6], [2, 4], [3, 7], [0, 7], [8, 9]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['algorithm', 'data', 'science', 'python', 'java', 'c++', 'javascript'],queries = [[0, 2], [3, 5], [1, 4], [0, 6], [5, 5], [2, 3], [4, 6]]) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 4], [1, 7], [2, 8], [3, 9], [0, 9]]) == [4, 6, 6, 6, 8]
    assert candidate(words = ['aeiou', 'bcdfg', 'ae', 'iou', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 8], [1, 5], [2, 7], [3, 6], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [8, 4, 6, 4, 1, 1, 1, 1, 1]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],queries = [[0, 5], [1, 4], [2, 3], [0, 0], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4]]) == [6, 4, 2, 1, 1, 1, 1, 1, 1]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],queries = [[0, 5], [1, 4], [0, 0], [5, 5]]) == [6, 4, 1, 1]
    assert candidate(words = ['apple', 'orange', 'umbrella', 'echo', 'alpha'],queries = [[0, 4], [1, 3], [0, 0], [2, 2], [1, 4]]) == [5, 3, 1, 1, 4]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7], [0, 9], [1, 8]]) == [15, 13, 11, 9, 7, 5, 3, 1, 10, 8]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'bcd'],queries = [[0, 6], [1, 5], [2, 7], [3, 3]]) == [7, 5, 5, 1]
    assert candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],queries = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 6], [1, 5], [2, 4]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['amplifier', 'equalizer', 'microphone', 'audio', 'sound', 'voice', 'volume', 'level', 'peak', 'gain'],queries = [[0, 2], [1, 5], [2, 7], [3, 8], [4, 9], [0, 9]]) == [0, 1, 1, 1, 0, 1]
    assert candidate(words = ['algorithm', 'datastructure', 'programming', 'python', 'java', 'csharp', 'javascript', 'html', 'css', 'vue'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]
    assert candidate(words = ['a', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 15], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == [4, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    assert candidate(words = ['strawberry', 'blueberry', 'raspberry', 'blackberry', 'kiwi', 'mango', 'papaya'],queries = [[0, 6], [1, 5], [2, 4], [0, 1], [5, 6]]) == [0, 0, 0, 0, 0]
    assert candidate(words = ['aabb', 'bbaa', 'abcd', 'dcba', 'efgh', 'hgfe', 'ijkl', 'lkji', 'mnop', 'ponm'],queries = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9]]) == [0, 0, 0, 0, 0, 0]
    assert candidate(words = ['algorithm', 'engine', 'idea', 'open', 'ocean', 'under', 'education'],queries = [[0, 2], [1, 5], [2, 6], [0, 6]]) == [2, 2, 1, 2]
    assert candidate(words = ['abacaxi', 'ananas', 'acerola', 'banana', 'manga', 'abacaxi', 'manga', 'banana'],queries = [[0, 3], [4, 7], [0, 4], [3, 6], [1, 5], [2, 2], [6, 7]]) == [2, 1, 2, 1, 2, 1, 0]
    assert candidate(words = ['umbrella', 'orange', 'apple', 'elephant', 'ocean', 'idea', 'education'],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]]) == [2, 2, 1, 0, 1, 1, 4]
    assert candidate(words = ['ae', 'ei', 'ou', 'ia', 'oe', 'uo', 'oi', 'ie', 'oa', 'eu'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [0, 3], [1, 7], [2, 6]]) == [10, 8, 6, 4, 2, 5, 5, 4, 7, 5]
    assert candidate(words = ['apple', 'orange', 'umbrella', 'electric', 'ice', 'onion', 'octopus'],queries = [[0, 6], [1, 3], [2, 5], [0, 0], [6, 6], [3, 4], [1, 5]]) == [4, 2, 2, 1, 0, 1, 3]
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'vowel', 'nonvowel'],queries = [[0, 6], [1, 5], [2, 4], [3, 3], [4, 4]]) == [5, 4, 3, 1, 1]
    assert candidate(words = ['aeioua', 'aeioue', 'aeiouo', 'aeioui', 'aeiouu', 'euoeu', 'iuoie', 'oueia', 'uaeio', 'eaoui'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 4], [5, 9], [0, 3], [1, 7], [2, 6]]) == [10, 8, 6, 4, 2, 5, 5, 4, 7, 5]
    assert candidate(words = ['algorithm', 'data', 'structure', 'design', 'computer', 'science', 'software', 'engineering'],queries = [[0, 3], [1, 5], [2, 7], [0, 8], [1, 6], [2, 4], [3, 7], [0, 7]]) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['aabbcc', 'ddeeff', 'gg', 'hhii', 'jjkk', 'llmm', 'nnoopp', 'qqrr', 'ssttuu', 'vvww'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]
    assert candidate(words = ['aeiou', 'bcd', 'eae', 'oio', 'uaa', 'aeiou', 'bcd', 'eae', 'oio', 'uaa'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 5], [0, 4], [1, 9]]) == [8, 6, 5, 3, 2, 5, 4, 7]
    assert candidate(words = ['apple', 'orange', 'ice', 'elephant', 'umbrella'],queries = [[0, 1], [1, 3], [2, 4], [0, 4]]) == [2, 2, 2, 4]
    assert candidate(words = ['aeiou', 'bcd', 'eee', 'oee', 'uau'],queries = [[0, 4], [1, 3], [2, 4], [0, 0], [4, 4]]) == [4, 2, 3, 1, 1]
    assert candidate(words = ['umbrella', 'raincoat', 'umbrella', 'hat', 'scarf', 'umbrella', 'umbrella', 'raincoat'],queries = [[0, 3], [4, 7], [0, 4], [3, 6], [1, 5], [0, 6], [2, 2], [5, 7]]) == [2, 2, 2, 2, 2, 4, 1, 2]
    assert candidate(words = ['abacax', 'azedo', 'oiue', 'ueia', 'uiaeu', 'uiaed', 'uieaeu', 'ueae', 'euae', 'aeu'],queries = [[0, 4], [1, 3], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == [4, 3, 3, 3, 3, 3, 4]
    assert candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvw', 'xyz'],queries = [[0, 6], [1, 5], [2, 4], [0, 2], [3, 5], [0, 6], [6, 6]]) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(words = ['aeiouaeiou', 'bcd', 'eee', 'oau', 'bcd', 'eaa', 'aeiou', 'bcd', 'cde', 'dea'],queries = [[0, 4], [1, 7], [3, 8], [0, 9], [5, 5]]) == [3, 4, 3, 5, 1]
    assert candidate(words = ['aabbcc', 'eeffgg', 'hhhiii', 'jjjkll', 'mmmoonnn', 'pppqqq', 'rrrsss', 'tttuuu', 'vvvwww', 'xxxyyy'],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 0, 0, 0, 0]
    assert candidate(words = ['apple', 'orange', 'banana', 'umbrella', 'ice', 'elephant', 'octopus'],queries = [[0, 2], [3, 6], [0, 6], [2, 4]]) == [2, 2, 4, 2]
    assert candidate(words = ['banana', 'apple', 'orange', 'grape', 'kiwi'],queries = [[0, 4], [1, 2], [2, 3], [3, 4], [0, 3]]) == [2, 2, 1, 0, 2]
    assert candidate(words = ['aeiou', 'banana', 'grape', 'kiwi', 'a', 'e', 'i', 'o', 'u'],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == [6, 4, 3, 2, 1]


