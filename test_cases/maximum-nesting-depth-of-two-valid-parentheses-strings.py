def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(seq = "()") == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()") == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())") == [0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())") == [0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())())()") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())())()") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "") == []: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))") == [0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))") == [0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(())(())") == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(())(())") == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())(())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())(())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(())()()") == [0, 1, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(())()()") == [0, 1, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(()())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(()())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()") == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()") == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(())()") == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(())()") == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())())") == [0, 1, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())())") == [0, 1, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))") == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))") == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()") == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()") == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))()((()))(())") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))()((()))(())") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()())(()(()())))") == [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()())(()(()())))") == [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()((()))()))") == [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()((()))()))") == [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(()(()))))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(()(()))))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()(())))") == [0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()(())))") == [0, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()()(()())))") == [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()()(()())))") == [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()()()())(()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()()()())(()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()())))((())))") == [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()())))((())))") == [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(()(()(())))()") == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(()(()(())))()") == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()())(()())))((()))") == [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()())(()())))((()))") == [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()()(()(())))") == [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()()(()(())))") == [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()()())))") == [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()()())))") == [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()))(()())") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()))(()())") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()()()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()()()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()))(())") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()))(())") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(((()(())))))") == [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(((()(())))))") == [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()()())))((()))") == [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()()())))((()))") == [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()())(()))") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()())(()))") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))()(()())") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))()(()())") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(((())))(())()") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(((())))(())()") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()(()(()))))()") == [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()(()(()))))()") == [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(())()(())()(())") == [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(())()(())()(())") == [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))((((()))))((((()))))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))((((()))))((((()))))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()(((())))()()()(((())))") == [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()(((())))()()()(((())))") == [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()()))((()()))") == [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()()))((()()))") == [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))(((())))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))(((())))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))()((()))()") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))()((()))()") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))(((())))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))(((())))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(()))(()))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(()))(()))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())(())(())(())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())(())(())(())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(())()((()))()(())") == [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(())()((()))()(())") == [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()()()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()()()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())(()(())))") == [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())(()(())))") == [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((())))(()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((())))(()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()(()))))") == [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()(()))))") == [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(())((())))") == [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(())((())))") == [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(()())(())))()()") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(()())(())))()()") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((((())))))") == [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((((())))))") == [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))(())(()(()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))(())(()(()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()()())((()))") == [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()()())((()))") == [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()))(())((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()))(())((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()(())(())()") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()(())(())()") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()())(()))") == [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()())(()))") == [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()()()()))((()()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()()()()))((()()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))((()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))((()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()(())") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()(())") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(())(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(())(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()())((())))") == [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()())((())))") == [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()))()(())(((())))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()))()(())(((())))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())(()))((()()))") == [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())(()))((()()))") == [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))(()(()))(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))(()(()))(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((((()))))))") == [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((((()))))))") == [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(((())))()") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(((())))()") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())(())((()))") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())(())((()))") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()))(()(())))") == [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()))(()(())))") == [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))(())(()(()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))(())(()(()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(()))(()(())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(()))(()(())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()())(())))") == [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()())(())))") == [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()(())))((()(())))") == [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()(())))((()(())))") == [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(()(()))(()(()))") == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(()(()))(()(()))") == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((((()))))()") == [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((((()))))()") == [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())())((()))") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())())((()))") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()(())))))") == [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()(())))))") == [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((())))())(()())") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((())))())(()())") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))()()") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))()()") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())(()(()(()))))") == [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())(()(()(()))))") == [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))(()(()))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))(()(()))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())()((()))") == [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())()((()))") == [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())(())((()))))") == [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())(())((()))))") == [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))(())((()))((()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))(())((()))((()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))((()))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))((()))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()))()((()))()((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()))()((()))()((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()())())") == [0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()())())") == [0, 1, 0, 0, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()((()))(())())") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()((()))(())())") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()(())()()(())()()") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()(())()()(())()()") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())())(())") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())())(())") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()())(()()))(())") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()())(()()))(())") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(()(()))()(()(()))") == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(()(()))()(()(()))") == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()(()(()(()(())))))())") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()(()(()(()(())))))())") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()(()())()()") == [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()(()())()()") == [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(())((()))(())((()))") == [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(())((()))(())((()))") == [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(()())(()())") == [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(()())(()())") == [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))((())))") == [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))((())))") == [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))()(())()(())") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))()(())()(())") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()())())") == [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()())())") == [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))((()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))((()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()((()))()(())") == [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()((()))()(())") == [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())((()))(()(()))") == [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())((()))(()(()))") == [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()(()(()))))") == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()(()(()))))") == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()((()))())(())") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()((()))())(())") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(((())))()(((())))") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(((())))()(((())))") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()((()))") == [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()((()))") == [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())())((())())") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())())((())())") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()))))(())") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()))))(())") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((((((()))))))))))") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((((((()))))))))))") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))((()))((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))((()))((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(((()))))(()(((()))))") == [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(((()))))(()(((()))))") == [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()(())))(()(())))") == [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()(())))(()(())))") == [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()(()(()))))((()(()(()))))") == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()(()(()))))((()(()(()))))") == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()(())(())(())") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()(())(())(())") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()(()())))") == [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()(()())))") == [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))(()(()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))(()(()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))(())()(()(()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))(())()(()(()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))((())())") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))((())())") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()(()(()(()(()))))()") == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()(()(()(()(()))))()") == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((((()()()))))((()))") == [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((((()()()))))((()))") == [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()(()))(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()(()))(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()((())))") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()((())))") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((()))())()((()))") == [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((()))())()((()))") == [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))()(())") == [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))()(())") == [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((())))((((()))))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((())))((((()))))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((())()(()))") == [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((())()(()))") == [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())(()())(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())(()())(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(((((())))))(((((())))))") == [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(((((())))))(((((())))))") == [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()((()))()()((()))") == [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()((()))()()((()))") == [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(()())(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(()())(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "(())(())(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "(())(())(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(seq = "()((()))()((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seq = "()((()))()((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(seq = "()") == [0, 0]
    assert candidate(seq = "(()())") == [0, 1, 1, 1, 1, 0]
    assert candidate(seq = "(()(()(())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((())())()") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 0]
    assert candidate(seq = "") == []
    assert candidate(seq = "((()))") == [0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(())(())") == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()())(())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "(())()()") == [0, 1, 1, 0, 0, 0, 0, 0]
    assert candidate(seq = "(()(()(()())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    assert candidate(seq = "()()()()") == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "()(())()") == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(seq = "((())())") == [0, 1, 0, 0, 1, 1, 1, 0]
    assert candidate(seq = "(((())))") == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "()()()") == [0, 0, 0, 0, 0, 0]
    assert candidate(seq = "((((()))))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "((()))((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()(()))()((()))(())") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "(()(()())(()(()())))") == [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    assert candidate(seq = "(()(()((()))()))") == [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    assert candidate(seq = "(()(()(()(()))))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "((()(())))") == [0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((()()(()())))") == [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    assert candidate(seq = "((()()()())(()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "((((()())))((())))") == [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "()(()(()(())))()") == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    assert candidate(seq = "(((()())(()())))((()))") == [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()()(()(())))") == [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "(((()()())))") == [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]
    assert candidate(seq = "()((()))(()())") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "((()()()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    assert candidate(seq = "()((()))(())") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "(()(((()(())))))") == [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
    assert candidate(seq = "(((()()())))((()))") == [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()())(()))") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(((())))()(()())") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "()(((())))(())()") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(seq = "()((()(()(()))))()") == [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    assert candidate(seq = "()(())()(())()(())") == [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    assert candidate(seq = "((((()))))((((()))))((((()))))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "()()()(((())))()()()(((())))") == [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((()()))((()()))") == [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    assert candidate(seq = "((((()))))(((())))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "(()(()))()((()))()") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    assert candidate(seq = "(((())))(((())))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "(()(()(()))(()))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()())(())(())(())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "()(())()((()))()(())") == [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    assert candidate(seq = "()()()()()()()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "((())(()(())))") == [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((((())))(()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    assert candidate(seq = "(((()(()))))") == [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "(()(())((())))") == [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "(()(()(()())(())))()()") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
    assert candidate(seq = "(((((())))))") == [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    assert candidate(seq = "((()))(())(()(()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()()())((()))") == [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()((()))(())((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()()(())(())()") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(seq = "()((()())(()))") == [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()()()()))((()()()()))") == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    assert candidate(seq = "(()(()))((()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "()()()()()(())") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
    assert candidate(seq = "(())(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "(()(()())((())))") == [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "()((()))()(())(((())))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((())(()))((()()))") == [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    assert candidate(seq = "(()(()))(()(()))(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "((((((()))))))") == [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(seq = "()()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "()(((())))()") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
    assert candidate(seq = "(()())(())((()))") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(((()))(()(())))") == [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((((()))))(())(()(()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()(()(()))(()(())))") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "(((()())(())))") == [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((()(())))((()(())))") == [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "()(()(()))(()(()))") == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "()((((()))))()") == [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    assert candidate(seq = "((())())((()))") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "((((()(())))))") == [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
    assert candidate(seq = "((((())))())(()())") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "(()(()))()()") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert candidate(seq = "((())(()(()(()))))") == [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "(((())))(()(()))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "(()())()((()))") == [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(((())(())((()))))") == [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "((((()))))(())((()))((()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(((())))((()))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()((()))()((()))()((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()())())") == [0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
    assert candidate(seq = "(()((()))(())())") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    assert candidate(seq = "()()()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "()()(())()()(())()()") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    assert candidate(seq = "((())())(())") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "((()())(()()))(())") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "()(()(()))()(()(()))") == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()(()(()(()(()(())))))())") == [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
    assert candidate(seq = "()()(()())()()") == [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    assert candidate(seq = "(())((()))(())((()))") == [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()(()())(()())") == [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "((((()))((())))") == [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
    assert candidate(seq = "(((())))()(())()(())") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    assert candidate(seq = "()((()())())") == [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
    assert candidate(seq = "((((()))))((()))") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()()()((()))()(())") == [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    assert candidate(seq = "(()())((()))(()(()))") == [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()(()(()))))") == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "(()((()))())(())") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "()(((())))()(((())))") == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "()()()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "()()((()))") == [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "((())())((())())") == [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    assert candidate(seq = "((((()))))(())") == [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "((((((((()))))))))))") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(seq = "((()))((()))((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()(((()))))(()(((()))))") == [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "(((()(())))(()(())))") == [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "((()(()(()))))((()(()(()))))") == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "()()(())(())(())") == [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "((()(()())))") == [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    assert candidate(seq = "((()))(()(()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()))(())()(()(()))") == [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()))((())())") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    assert candidate(seq = "()(()(()(()(()))))()") == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    assert candidate(seq = "((((()()()))))((()))") == [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()(()))(()(()))") == [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()((())))") == [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(seq = "(((()))())()((()))") == [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "((()))()(())") == [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    assert candidate(seq = "(((())))((((()))))") == [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(seq = "((())()(()))") == [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()())(()())(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "(((((())))))(((((())))))") == [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    assert candidate(seq = "((()))((()))") == [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "()()((()))()()((()))") == [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(seq = "(()())(()())(()())") == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    assert candidate(seq = "()()()()()") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(seq = "(())(())(())(())(())") == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(seq = "()((()))()((()))") == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]


