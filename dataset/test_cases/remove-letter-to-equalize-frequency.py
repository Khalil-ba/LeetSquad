def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aabbccd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zazaza") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zazaza") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabbbbbcccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabbbbbcccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeff") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeff") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbbcccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbbcccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aazz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aazz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcccddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcccddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeee") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabad") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabad") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccdde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccdde") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abbbccddde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abbbccddde") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwerty") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwerty") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxzy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxzy") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghi") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcccd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcccd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijj") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccdddde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccdddde") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeefffg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeefffg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeeffffgggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeeffffgggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccccddddeeeeeffffffggggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccccddddeeeeeffffffggggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffg") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccccdddde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccccdddde") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgggh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgggh") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeff") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeff") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzyyyyy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzyyyyy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccdddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccdddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccccdddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccccdddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccccddddeeeeeffffff") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccccddddeeeeeffffff") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijjk") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijjk") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccde") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abbbbcccccdddddeeeeee") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abbbbcccccdddddeeeeee") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeeffff") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeeffff") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccccddddeeeee") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccccddddeeeee") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffggghhhh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffggghhhh") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccdddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccdddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcddd") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aabbccd") == True
    assert candidate(word = "aaabbbccc") == False
    assert candidate(word = "zazaza") == False
    assert candidate(word = "aaaaabbbbbcccc") == False
    assert candidate(word = "zzzzzzzz") == True
    assert candidate(word = "aabbccddeff") == True
    assert candidate(word = "aabbbbcccc") == False
    assert candidate(word = "aazz") == False
    assert candidate(word = "aabbbccccc") == False
    assert candidate(word = "aaa") == True
    assert candidate(word = "aabbbccddd") == False
    assert candidate(word = "abcdef") == True
    assert candidate(word = "aabbcccddd") == False
    assert candidate(word = "aabbc") == True
    assert candidate(word = "aabbccddeee") == True
    assert candidate(word = "abacabad") == False
    assert candidate(word = "abcdabcd") == False
    assert candidate(word = "aabbbccc") == False
    assert candidate(word = "aabbccdde") == True
    assert candidate(word = "aabbbcccc") == False
    assert candidate(word = "aabbbcccccc") == False
    assert candidate(word = "zzzz") == True
    assert candidate(word = "abcc") == True
    assert candidate(word = "xyyz") == True
    assert candidate(word = "aab") == True
    assert candidate(word = "aabbcc") == False
    assert candidate(word = "abcde") == True
    assert candidate(word = "aaabbbb") == True
    assert candidate(word = "aabbbb") == False
    assert candidate(word = "abcd") == True
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False
    assert candidate(word = "abbbccddde") == False
    assert candidate(word = "abcabcabc") == False
    assert candidate(word = "qwerty") == True
    assert candidate(word = "aabbbcccd") == False
    assert candidate(word = "aabbccddd") == True
    assert candidate(word = "abc") == True
    assert candidate(word = "abcddd") == False
    assert candidate(word = "abcdefghijklmnopqrstuvwxzy") == True
    assert candidate(word = "aaaabbbb") == False
    assert candidate(word = "aabbccc") == True
    assert candidate(word = "abcdabcdabcd") == False
    assert candidate(word = "abcdefghi") == True
    assert candidate(word = "aabbcccd") == False
    assert candidate(word = "abcdefghijj") == True
    assert candidate(word = "aabbbcccdddde") == False
    assert candidate(word = "aabbcccc") == False
    assert candidate(word = "aabbccddeeefffg") == False
    assert candidate(word = "aabbccddeeeffffgggg") == False
    assert candidate(word = "aabbbccccddddeeeeeffffffggggg") == False
    assert candidate(word = "aabbccddeeffg") == True
    assert candidate(word = "zzzzzzzzzz") == True
    assert candidate(word = "aabbbccccdddde") == False
    assert candidate(word = "aabbccddeeffgg") == False
    assert candidate(word = "abcdefghij") == True
    assert candidate(word = "aabbccddeeffgggh") == False
    assert candidate(word = "aabbccddeeff") == False
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word = "abcabcabcabcabcabcabcabc") == False
    assert candidate(word = "zzzzzyyyyy") == False
    assert candidate(word = "aaaabbbbccccdddd") == False
    assert candidate(word = "aabbbccccdddd") == False
    assert candidate(word = "aabbbcccddd") == False
    assert candidate(word = "abcdefg") == True
    assert candidate(word = "aabbbccccddddeeeeeffffff") == False
    assert candidate(word = "abcdefghijjk") == True
    assert candidate(word = "aabbbcccde") == False
    assert candidate(word = "abbbbcccccdddddeeeeee") == False
    assert candidate(word = "aabbccddeeeffff") == False
    assert candidate(word = "aabbbccccddddeeeee") == False
    assert candidate(word = "aabbccddeeffggghhhh") == False
    assert candidate(word = "abcabcabcabc") == False
    assert candidate(word = "aabbbcccdddd") == False
    assert candidate(word = "aabbcddd") == False


