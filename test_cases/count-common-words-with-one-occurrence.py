def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words1 = ['one'],words2 = ['two']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one'],words2 = ['two']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique'],words2 = ['unique']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique'],words2 = ['unique']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['b', 'bb', 'bbb'],words2 = ['a', 'aa', 'aaa']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['b', 'bb', 'bbb'],words2 = ['a', 'aa', 'aaa']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['distinct'],words2 = ['distinct', 'distinct']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['distinct'],words2 = ['distinct', 'distinct']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c'],words2 = ['c', 'b', 'a']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c'],words2 = ['c', 'b', 'a']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['same', 'same'],words2 = ['same', 'same', 'same']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['same', 'same'],words2 = ['same', 'same', 'same']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'ab'],words2 = ['a', 'a', 'a', 'ab']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'ab'],words2 = ['a', 'a', 'a', 'ab']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world'],words2 = ['hello', 'world', 'hello']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world'],words2 = ['hello', 'world', 'hello']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world'],words2 = ['hello', 'world']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world'],words2 = ['hello', 'world']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'date']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'date']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['leetcode', 'is', 'amazing', 'as', 'is'],words2 = ['amazing', 'leetcode', 'is']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['leetcode', 'is', 'amazing', 'as', 'is'],words2 = ['amazing', 'leetcode', 'is']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['repeat', 'repeat'],words2 = ['repeat', 'repeat']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['repeat', 'repeat'],words2 = ['repeat', 'repeat']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['python', 'java', 'c++', 'javascript'],words2 = ['c++', 'java', 'python', 'python', 'javascript', 'java', 'c++', 'javascript', 'c++', 'javascript']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['python', 'java', 'c++', 'javascript'],words2 = ['c++', 'java', 'python', 'python', 'javascript', 'java', 'c++', 'javascript', 'c++', 'javascript']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['abc', 'def', 'ghi', 'jkl'],words2 = ['def', 'ghi', 'jkl', 'mno', 'pqr', 'abc', 'def', 'ghi', 'jkl']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['abc', 'def', 'ghi', 'jkl'],words2 = ['def', 'ghi', 'jkl', 'mno', 'pqr', 'abc', 'def', 'ghi', 'jkl']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['python', 'java', 'c++', 'ruby'],words2 = ['java', 'c++', 'ruby', 'python', 'python', 'java']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['python', 'java', 'c++', 'ruby'],words2 = ['java', 'c++', 'ruby', 'python', 'python', 'java']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['alpha', 'beta', 'gamma', 'delta'],words2 = ['delta', 'gamma', 'beta', 'alpha', 'alpha', 'beta', 'gamma', 'delta']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['alpha', 'beta', 'gamma', 'delta'],words2 = ['delta', 'gamma', 'beta', 'alpha', 'alpha', 'beta', 'gamma', 'delta']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world', 'hello'],words2 = ['world', 'hello', 'hello', 'world']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world', 'hello'],words2 = ['world', 'hello', 'hello', 'world']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'bird', 'fish'],words2 = ['cat', 'dog', 'bird', 'fish', 'dog', 'bird']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'bird', 'fish'],words2 = ['cat', 'dog', 'bird', 'fish', 'dog', 'bird']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'hello', 'world'],words2 = ['hello', 'world', 'world', 'world']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'hello', 'world'],words2 = ['hello', 'world', 'world', 'world']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'fish'],words2 = ['dog', 'cat', 'bird', 'fish', 'dog', 'fish']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'fish'],words2 = ['dog', 'cat', 'bird', 'fish', 'dog', 'fish']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['f', 'g', 'h', 'i', 'j']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['f', 'g', 'h', 'i', 'j']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['alpha', 'beta', 'gamma', 'delta'],words2 = ['alpha', 'beta', 'gamma', 'delta', 'delta']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['alpha', 'beta', 'gamma', 'delta'],words2 = ['alpha', 'beta', 'gamma', 'delta', 'delta']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four', 'five', 'six'],words2 = ['three', 'four', 'seven', 'eight', 'nine', 'one', 'two']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four', 'five', 'six'],words2 = ['three', 'four', 'seven', 'eight', 'nine', 'one', 'two']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four'],words2 = ['four', 'three', 'two', 'one', 'one', 'two', 'three', 'four', 'four', 'three', 'two', 'one']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four'],words2 = ['four', 'three', 'two', 'one', 'one', 'two', 'three', 'four', 'four', 'three', 'two', 'one']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['same', 'word', 'multiple'],words2 = ['same', 'word', 'multiple', 'same', 'word', 'multiple']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['same', 'word', 'multiple'],words2 = ['same', 'word', 'multiple', 'same', 'word', 'multiple']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['test', 'case', 'one'],words2 = ['case', 'test', 'one', 'one', 'test', 'case']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['test', 'case', 'one'],words2 = ['case', 'test', 'one', 'one', 'test', 'case']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['same', 'word', 'repeated'],words2 = ['same', 'word', 'repeated', 'same', 'word', 'repeated']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['same', 'word', 'repeated'],words2 = ['same', 'word', 'repeated', 'same', 'word', 'repeated']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world', 'hello', 'world'],words2 = ['hello', 'world', 'hello', 'world', 'hello', 'world']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world', 'hello', 'world'],words2 = ['hello', 'world', 'hello', 'world', 'hello', 'world']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words2 = ['a', 'b', 'b', 'c', 'd', 'd', 'e', 'f', 'f', 'g']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words2 = ['a', 'b', 'b', 'c', 'd', 'd', 'e', 'f', 'f', 'g']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['car', 'truck', 'bus', 'van', 'car', 'truck'],words2 = ['bus', 'van', 'motorcycle', 'bicycle', 'bus', 'van', 'truck']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['car', 'truck', 'bus', 'van', 'car', 'truck'],words2 = ['bus', 'van', 'motorcycle', 'bicycle', 'bus', 'van', 'truck']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'fish', 'bird'],words2 = ['dog', 'cat', 'cat', 'fish', 'dog', 'bird']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'fish', 'bird'],words2 = ['dog', 'cat', 'cat', 'fish', 'dog', 'bird']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],words2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],words2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['same', 'word', 'repeated', 'multiple', 'times'],words2 = ['times', 'repeated', 'multiple', 'same', 'word', 'word']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['same', 'word', 'repeated', 'multiple', 'times'],words2 = ['times', 'repeated', 'multiple', 'same', 'word', 'word']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four'],words2 = ['four', 'three', 'two', 'one', 'one', 'two', 'three', 'four']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four'],words2 = ['four', 'three', 'two', 'one', 'one', 'two', 'three', 'four']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'apple']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'apple']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z', 'w', 'v'],words2 = ['x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z', 'w', 'v'],words2 = ['x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['e', 'd', 'c', 'b', 'a', 'a', 'b', 'c', 'd', 'e']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['e', 'd', 'c', 'b', 'a', 'a', 'b', 'c', 'd', 'e']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique', 'words', 'only', 'once', 'here'],words2 = ['words', 'only', 'once', 'here', 'unique', 'twice', 'unique']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique', 'words', 'only', 'once', 'here'],words2 = ['words', 'only', 'once', 'here', 'unique', 'twice', 'unique']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'elephant', 'frog', 'cat'],words2 = ['dog', 'frog', 'giraffe', 'elephant', 'hippo']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'elephant', 'frog', 'cat'],words2 = ['dog', 'frog', 'giraffe', 'elephant', 'hippo']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'fish'],words2 = ['fish', 'dog', 'cat', 'dog', 'cat']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'fish'],words2 = ['fish', 'dog', 'cat', 'dog', 'cat']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['python', 'java', 'c', 'cpp'],words2 = ['python', 'java', 'java', 'csharp']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['python', 'java', 'c', 'cpp'],words2 = ['python', 'java', 'java', 'csharp']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique', 'words', 'only', 'here'],words2 = ['here', 'only', 'words', 'unique', 'unique']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique', 'words', 'only', 'here'],words2 = ['here', 'only', 'words', 'unique', 'unique']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world', 'hello'],words2 = ['world', 'hello', 'world', 'hello', 'world', 'hello']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world', 'hello'],words2 = ['world', 'hello', 'world', 'hello', 'world', 'hello']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world', 'python', 'java', 'csharp'],words2 = ['python', 'java', 'csharp', 'hello', 'ruby', 'scala', 'world', 'python', 'java']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world', 'python', 'java', 'csharp'],words2 = ['python', 'java', 'csharp', 'hello', 'ruby', 'scala', 'world', 'python', 'java']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique', 'word', 'only', 'in', 'this', 'array'],words2 = ['unique', 'only', 'word', 'in', 'that', 'array']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique', 'word', 'only', 'in', 'this', 'array'],words2 = ['unique', 'only', 'word', 'in', 'that', 'array']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'apple', 'apple']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'apple', 'apple']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry', 'date'],words2 = ['banana', 'cherry', 'fig', 'grape']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry', 'date'],words2 = ['banana', 'cherry', 'fig', 'grape']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'apple', 'cherry', 'date']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'apple', 'cherry', 'date']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abc'],words2 = ['mno', 'pqr', 'stu', 'vwx', 'yz', 'abc', 'def', 'ghi', 'jkl', 'mno']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abc'],words2 = ['mno', 'pqr', 'stu', 'vwx', 'yz', 'abc', 'def', 'ghi', 'jkl', 'mno']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry', 'date'],words2 = ['banana', 'date', 'fig', 'grape', 'apple']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry', 'date'],words2 = ['banana', 'date', 'fig', 'grape', 'apple']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry', 'date', 'elderberry'],words2 = ['banana', 'cherry', 'elderberry', 'fig', 'grape', 'apple', 'date']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry', 'date', 'elderberry'],words2 = ['banana', 'cherry', 'elderberry', 'fig', 'grape', 'apple', 'date']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'a', 'b', 'c'],words2 = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'a', 'b', 'c'],words2 = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['sun', 'moon', 'star', 'planet', 'sun', 'moon'],words2 = ['star', 'planet', 'comet', 'asteroid', 'planet', 'star']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['sun', 'moon', 'star', 'planet', 'sun', 'moon'],words2 = ['star', 'planet', 'comet', 'asteroid', 'planet', 'star']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'],words2 = ['gamma', 'delta', 'zeta', 'eta', 'theta', 'epsilon', 'delta']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'],words2 = ['gamma', 'delta', 'zeta', 'eta', 'theta', 'epsilon', 'delta']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['python', 'java', 'csharp'],words2 = ['java', 'csharp', 'python', 'python']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['python', 'java', 'csharp'],words2 = ['java', 'csharp', 'python', 'python']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['python', 'java', 'c++'],words2 = ['c++', 'java', 'python', 'java', 'python', 'c++', 'python']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['python', 'java', 'c++'],words2 = ['c++', 'java', 'python', 'java', 'python', 'c++', 'python']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'mouse'],words2 = ['dog', 'cat', 'cat', 'mouse', 'dog']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'mouse'],words2 = ['dog', 'cat', 'cat', 'mouse', 'dog']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'apple', 'banana']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'apple', 'banana']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['same', 'words', 'in', 'both', 'arrays'],words2 = ['same', 'words', 'in', 'both', 'arrays']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['same', 'words', 'in', 'both', 'arrays'],words2 = ['same', 'words', 'in', 'both', 'arrays']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['single'],words2 = ['single', 'single', 'single', 'single']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['single'],words2 = ['single', 'single', 'single', 'single']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['cherry', 'banana', 'apple', 'apple']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['cherry', 'banana', 'apple', 'apple']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['abc', 'def', 'ghi'],words2 = ['def', 'ghi', 'jkl', 'def', 'ghi']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['abc', 'def', 'ghi'],words2 = ['def', 'ghi', 'jkl', 'def', 'ghi']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault'],words2 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'grault']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault'],words2 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'grault']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['foo', 'bar', 'baz', 'qux'],words2 = ['foo', 'bar', 'qux', 'quux']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['foo', 'bar', 'baz', 'qux'],words2 = ['foo', 'bar', 'qux', 'quux']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'banana']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'banana']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'hello', 'world'],words2 = ['world', 'world', 'hello', 'hello', 'hello']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'hello', 'world'],words2 = ['world', 'world', 'hello', 'hello', 'hello']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['five', 'four', 'three', 'two', 'one']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['five', 'four', 'three', 'two', 'one']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'cherry']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'cherry']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique', 'words', 'only'],words2 = ['only', 'words', 'unique', 'words']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique', 'words', 'only'],words2 = ['only', 'words', 'unique', 'words']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['red', 'blue', 'green'],words2 = ['red', 'red', 'blue', 'green', 'blue', 'green']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['red', 'blue', 'green'],words2 = ['red', 'red', 'blue', 'green', 'blue', 'green']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['cat', 'dog', 'mouse', 'elephant'],words2 = ['dog', 'mouse', 'cat', 'tiger', 'elephant', 'dog']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['cat', 'dog', 'mouse', 'elephant'],words2 = ['dog', 'mouse', 'cat', 'tiger', 'elephant', 'dog']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['test', 'case', 'input'],words2 = ['input', 'test', 'case', 'input', 'test', 'case', 'input', 'test', 'case']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['test', 'case', 'input'],words2 = ['input', 'test', 'case', 'input', 'test', 'case', 'input', 'test', 'case']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world', 'hello', 'world'],words2 = ['hello', 'world', 'world', 'hello']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world', 'hello', 'world'],words2 = ['hello', 'world', 'world', 'hello']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['first', 'second', 'third', 'fourth'],words2 = ['fourth', 'third', 'second', 'first', 'first', 'second', 'third', 'fourth', 'first', 'second', 'third', 'fourth']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['first', 'second', 'third', 'fourth'],words2 = ['fourth', 'third', 'second', 'first', 'first', 'second', 'third', 'fourth', 'first', 'second', 'third', 'fourth']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['two', 'three', 'five', 'six', 'seven', 'eight', 'nine', 'one', 'four']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['two', 'three', 'five', 'six', 'seven', 'eight', 'nine', 'one', 'four']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['repeated', 'repeated', 'words', 'in', 'both', 'arrays'],words2 = ['repeated', 'words', 'in', 'both', 'arrays', 'arrays']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['repeated', 'repeated', 'words', 'in', 'both', 'arrays'],words2 = ['repeated', 'words', 'in', 'both', 'arrays', 'arrays']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z'],words2 = ['z', 'y', 'x']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z'],words2 = ['z', 'y', 'x']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['single'],words2 = ['single']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['single'],words2 = ['single']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['hello', 'world', 'python', 'java'],words2 = ['python', 'java', 'hello', 'world', 'world', 'hello']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['hello', 'world', 'python', 'java'],words2 = ['python', 'java', 'hello', 'world', 'world', 'hello']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'e']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'e']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['python', 'java', 'c', 'cpp'],words2 = ['java', 'c', 'cpp', 'ruby']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['python', 'java', 'c', 'cpp'],words2 = ['java', 'c', 'cpp', 'ruby']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique', 'string', 'in', 'each', 'array'],words2 = ['different', 'string', 'in', 'each', 'array']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique', 'string', 'in', 'each', 'array'],words2 = ['different', 'string', 'in', 'each', 'array']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['single'],words2 = ['single', 'single', 'single']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['single'],words2 = ['single', 'single', 'single']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'date']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'date']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['repeat', 'repeat', 'repeat'],words2 = ['repeat', 'repeat', 'repeat', 'repeat']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['repeat', 'repeat', 'repeat'],words2 = ['repeat', 'repeat', 'repeat', 'repeat']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['red', 'blue', 'green', 'yellow', 'red'],words2 = ['blue', 'green', 'purple', 'yellow', 'blue', 'green']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['red', 'blue', 'green', 'yellow', 'red'],words2 = ['blue', 'green', 'purple', 'yellow', 'blue', 'green']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['foo', 'bar', 'baz', 'qux', 'quux'],words2 = ['qux', 'quux', 'foo', 'bar', 'baz', 'corge', 'grault', 'foo']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['foo', 'bar', 'baz', 'qux', 'quux'],words2 = ['qux', 'quux', 'foo', 'bar', 'baz', 'corge', 'grault', 'foo']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['example', 'test', 'case'],words2 = ['test', 'case', 'example', 'example', 'test', 'case']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['example', 'test', 'case'],words2 = ['test', 'case', 'example', 'example', 'test', 'case']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique'],words2 = ['unique', 'unique', 'unique']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique'],words2 = ['unique', 'unique', 'unique']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],words2 = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'x', 'y', 'z']) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],words2 = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'x', 'y', 'z']) == 23: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words1 = ['unique'],words2 = ['unique', 'unique', 'unique', 'unique']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words1 = ['unique'],words2 = ['unique', 'unique', 'unique', 'unique']) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words1 = ['one'],words2 = ['two']) == 0
    assert candidate(words1 = ['unique'],words2 = ['unique']) == 1
    assert candidate(words1 = ['b', 'bb', 'bbb'],words2 = ['a', 'aa', 'aaa']) == 0
    assert candidate(words1 = ['distinct'],words2 = ['distinct', 'distinct']) == 0
    assert candidate(words1 = ['a', 'b', 'c'],words2 = ['c', 'b', 'a']) == 3
    assert candidate(words1 = ['same', 'same'],words2 = ['same', 'same', 'same']) == 0
    assert candidate(words1 = ['a', 'ab'],words2 = ['a', 'a', 'a', 'ab']) == 1
    assert candidate(words1 = ['hello', 'world'],words2 = ['hello', 'world', 'hello']) == 1
    assert candidate(words1 = ['hello', 'world'],words2 = ['hello', 'world']) == 2
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'date']) == 2
    assert candidate(words1 = ['leetcode', 'is', 'amazing', 'as', 'is'],words2 = ['amazing', 'leetcode', 'is']) == 2
    assert candidate(words1 = ['repeat', 'repeat'],words2 = ['repeat', 'repeat']) == 0
    assert candidate(words1 = ['python', 'java', 'c++', 'javascript'],words2 = ['c++', 'java', 'python', 'python', 'javascript', 'java', 'c++', 'javascript', 'c++', 'javascript']) == 0
    assert candidate(words1 = ['abc', 'def', 'ghi', 'jkl'],words2 = ['def', 'ghi', 'jkl', 'mno', 'pqr', 'abc', 'def', 'ghi', 'jkl']) == 1
    assert candidate(words1 = ['python', 'java', 'c++', 'ruby'],words2 = ['java', 'c++', 'ruby', 'python', 'python', 'java']) == 2
    assert candidate(words1 = ['alpha', 'beta', 'gamma', 'delta'],words2 = ['delta', 'gamma', 'beta', 'alpha', 'alpha', 'beta', 'gamma', 'delta']) == 0
    assert candidate(words1 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
    assert candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight']) == 4
    assert candidate(words1 = ['hello', 'world', 'hello'],words2 = ['world', 'hello', 'hello', 'world']) == 0
    assert candidate(words1 = ['cat', 'dog', 'bird', 'fish'],words2 = ['cat', 'dog', 'bird', 'fish', 'dog', 'bird']) == 2
    assert candidate(words1 = ['hello', 'hello', 'world'],words2 = ['hello', 'world', 'world', 'world']) == 0
    assert candidate(words1 = ['cat', 'dog', 'fish'],words2 = ['dog', 'cat', 'bird', 'fish', 'dog', 'fish']) == 1
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['f', 'g', 'h', 'i', 'j']) == 0
    assert candidate(words1 = ['alpha', 'beta', 'gamma', 'delta'],words2 = ['alpha', 'beta', 'gamma', 'delta', 'delta']) == 3
    assert candidate(words1 = ['one', 'two', 'three', 'four', 'five', 'six'],words2 = ['three', 'four', 'seven', 'eight', 'nine', 'one', 'two']) == 4
    assert candidate(words1 = ['one', 'two', 'three', 'four'],words2 = ['four', 'three', 'two', 'one', 'one', 'two', 'three', 'four', 'four', 'three', 'two', 'one']) == 0
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 0
    assert candidate(words1 = ['same', 'word', 'multiple'],words2 = ['same', 'word', 'multiple', 'same', 'word', 'multiple']) == 0
    assert candidate(words1 = ['test', 'case', 'one'],words2 = ['case', 'test', 'one', 'one', 'test', 'case']) == 0
    assert candidate(words1 = ['same', 'word', 'repeated'],words2 = ['same', 'word', 'repeated', 'same', 'word', 'repeated']) == 0
    assert candidate(words1 = ['hello', 'world', 'hello', 'world'],words2 = ['hello', 'world', 'hello', 'world', 'hello', 'world']) == 0
    assert candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z']) == 0
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words2 = ['a', 'b', 'b', 'c', 'd', 'd', 'e', 'f', 'f', 'g']) == 4
    assert candidate(words1 = ['car', 'truck', 'bus', 'van', 'car', 'truck'],words2 = ['bus', 'van', 'motorcycle', 'bicycle', 'bus', 'van', 'truck']) == 0
    assert candidate(words1 = ['cat', 'dog', 'fish', 'bird'],words2 = ['dog', 'cat', 'cat', 'fish', 'dog', 'bird']) == 2
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']) == 5
    assert candidate(words1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],words2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']) == 0
    assert candidate(words1 = ['same', 'word', 'repeated', 'multiple', 'times'],words2 = ['times', 'repeated', 'multiple', 'same', 'word', 'word']) == 4
    assert candidate(words1 = ['one', 'two', 'three', 'four'],words2 = ['four', 'three', 'two', 'one', 'one', 'two', 'three', 'four']) == 0
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'apple']) == 2
    assert candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 4
    assert candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']) == 0
    assert candidate(words1 = ['x', 'y', 'z', 'w', 'v'],words2 = ['x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v', 'x', 'y', 'z', 'w', 'v']) == 0
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['e', 'd', 'c', 'b', 'a', 'a', 'b', 'c', 'd', 'e']) == 0
    assert candidate(words1 = ['unique', 'words', 'only', 'once', 'here'],words2 = ['words', 'only', 'once', 'here', 'unique', 'twice', 'unique']) == 4
    assert candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
    assert candidate(words1 = ['cat', 'dog', 'elephant', 'frog', 'cat'],words2 = ['dog', 'frog', 'giraffe', 'elephant', 'hippo']) == 3
    assert candidate(words1 = ['cat', 'dog', 'fish'],words2 = ['fish', 'dog', 'cat', 'dog', 'cat']) == 1
    assert candidate(words1 = ['python', 'java', 'c', 'cpp'],words2 = ['python', 'java', 'java', 'csharp']) == 1
    assert candidate(words1 = ['unique', 'words', 'only', 'here'],words2 = ['here', 'only', 'words', 'unique', 'unique']) == 3
    assert candidate(words1 = ['hello', 'world', 'hello'],words2 = ['world', 'hello', 'world', 'hello', 'world', 'hello']) == 0
    assert candidate(words1 = ['hello', 'world', 'python', 'java', 'csharp'],words2 = ['python', 'java', 'csharp', 'hello', 'ruby', 'scala', 'world', 'python', 'java']) == 3
    assert candidate(words1 = ['x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
    assert candidate(words1 = ['unique', 'word', 'only', 'in', 'this', 'array'],words2 = ['unique', 'only', 'word', 'in', 'that', 'array']) == 5
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'apple', 'apple']) == 2
    assert candidate(words1 = ['apple', 'banana', 'cherry', 'date'],words2 = ['banana', 'cherry', 'fig', 'grape']) == 2
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'apple', 'cherry', 'date']) == 2
    assert candidate(words1 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abc'],words2 = ['mno', 'pqr', 'stu', 'vwx', 'yz', 'abc', 'def', 'ghi', 'jkl', 'mno']) == 7
    assert candidate(words1 = ['apple', 'banana', 'cherry', 'date'],words2 = ['banana', 'date', 'fig', 'grape', 'apple']) == 3
    assert candidate(words1 = ['apple', 'banana', 'cherry', 'date', 'elderberry'],words2 = ['banana', 'cherry', 'elderberry', 'fig', 'grape', 'apple', 'date']) == 5
    assert candidate(words1 = ['a', 'b', 'c', 'a', 'b', 'c'],words2 = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == 0
    assert candidate(words1 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],words2 = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == 0
    assert candidate(words1 = ['sun', 'moon', 'star', 'planet', 'sun', 'moon'],words2 = ['star', 'planet', 'comet', 'asteroid', 'planet', 'star']) == 0
    assert candidate(words1 = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'],words2 = ['gamma', 'delta', 'zeta', 'eta', 'theta', 'epsilon', 'delta']) == 2
    assert candidate(words1 = ['python', 'java', 'csharp'],words2 = ['java', 'csharp', 'python', 'python']) == 2
    assert candidate(words1 = ['python', 'java', 'c++'],words2 = ['c++', 'java', 'python', 'java', 'python', 'c++', 'python']) == 0
    assert candidate(words1 = ['cat', 'dog', 'mouse'],words2 = ['dog', 'cat', 'cat', 'mouse', 'dog']) == 1
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'apple', 'banana']) == 2
    assert candidate(words1 = ['same', 'words', 'in', 'both', 'arrays'],words2 = ['same', 'words', 'in', 'both', 'arrays']) == 5
    assert candidate(words1 = ['single'],words2 = ['single', 'single', 'single', 'single']) == 0
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['cherry', 'banana', 'apple', 'apple']) == 2
    assert candidate(words1 = ['abc', 'def', 'ghi'],words2 = ['def', 'ghi', 'jkl', 'def', 'ghi']) == 0
    assert candidate(words1 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault'],words2 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'grault']) == 6
    assert candidate(words1 = ['foo', 'bar', 'baz', 'qux'],words2 = ['foo', 'bar', 'qux', 'quux']) == 3
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'banana']) == 2
    assert candidate(words1 = ['hello', 'hello', 'world'],words2 = ['world', 'world', 'hello', 'hello', 'hello']) == 0
    assert candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['five', 'four', 'three', 'two', 'one']) == 5
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'apple', 'cherry', 'cherry']) == 2
    assert candidate(words1 = ['unique', 'words', 'only'],words2 = ['only', 'words', 'unique', 'words']) == 2
    assert candidate(words1 = ['red', 'blue', 'green'],words2 = ['red', 'red', 'blue', 'green', 'blue', 'green']) == 0
    assert candidate(words1 = ['cat', 'dog', 'mouse', 'elephant'],words2 = ['dog', 'mouse', 'cat', 'tiger', 'elephant', 'dog']) == 3
    assert candidate(words1 = ['test', 'case', 'input'],words2 = ['input', 'test', 'case', 'input', 'test', 'case', 'input', 'test', 'case']) == 0
    assert candidate(words1 = ['hello', 'world', 'hello', 'world'],words2 = ['hello', 'world', 'world', 'hello']) == 0
    assert candidate(words1 = ['first', 'second', 'third', 'fourth'],words2 = ['fourth', 'third', 'second', 'first', 'first', 'second', 'third', 'fourth', 'first', 'second', 'third', 'fourth']) == 0
    assert candidate(words1 = ['one', 'two', 'three', 'four', 'five'],words2 = ['two', 'three', 'five', 'six', 'seven', 'eight', 'nine', 'one', 'four']) == 5
    assert candidate(words1 = ['repeated', 'repeated', 'words', 'in', 'both', 'arrays'],words2 = ['repeated', 'words', 'in', 'both', 'arrays', 'arrays']) == 3
    assert candidate(words1 = ['x', 'y', 'z'],words2 = ['z', 'y', 'x']) == 3
    assert candidate(words1 = ['a', 'b', 'c', 'd'],words2 = ['a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']) == 1
    assert candidate(words1 = ['single'],words2 = ['single']) == 1
    assert candidate(words1 = ['hello', 'world', 'python', 'java'],words2 = ['python', 'java', 'hello', 'world', 'world', 'hello']) == 2
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e'],words2 = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'e']) == 2
    assert candidate(words1 = ['python', 'java', 'c', 'cpp'],words2 = ['java', 'c', 'cpp', 'ruby']) == 3
    assert candidate(words1 = ['unique', 'string', 'in', 'each', 'array'],words2 = ['different', 'string', 'in', 'each', 'array']) == 4
    assert candidate(words1 = ['single'],words2 = ['single', 'single', 'single']) == 0
    assert candidate(words1 = ['apple', 'banana', 'cherry'],words2 = ['banana', 'cherry', 'date']) == 2
    assert candidate(words1 = ['repeat', 'repeat', 'repeat'],words2 = ['repeat', 'repeat', 'repeat', 'repeat']) == 0
    assert candidate(words1 = ['red', 'blue', 'green', 'yellow', 'red'],words2 = ['blue', 'green', 'purple', 'yellow', 'blue', 'green']) == 1
    assert candidate(words1 = ['foo', 'bar', 'baz', 'qux', 'quux'],words2 = ['qux', 'quux', 'foo', 'bar', 'baz', 'corge', 'grault', 'foo']) == 4
    assert candidate(words1 = ['example', 'test', 'case'],words2 = ['test', 'case', 'example', 'example', 'test', 'case']) == 0
    assert candidate(words1 = ['unique'],words2 = ['unique', 'unique', 'unique']) == 0
    assert candidate(words1 = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],words2 = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'x', 'y', 'z']) == 23
    assert candidate(words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == 0
    assert candidate(words1 = ['unique'],words2 = ['unique', 'unique', 'unique', 'unique']) == 0


