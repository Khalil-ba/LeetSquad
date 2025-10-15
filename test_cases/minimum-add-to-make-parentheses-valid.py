def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "(()))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "()))((") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()))((") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "))(()()((()(()))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))(()()((()(()))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()(()(()))(()(()(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()(()(()))(()(()(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((()))))))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((()))))))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(())))(()") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())))(()") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = ")(()))()()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")(()))()()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())()()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())()()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((())") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((())") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))()()(()(()()()(()())())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))()()(()(()()()(()())())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()()()(()))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()()()(()))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()())())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()())())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))))((()") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))))((()") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())((()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())((()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "()))(((((()))))())") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()))(((((()))))())") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()(()(()(()))))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()(()(()(()))))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))(())()(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))(())()(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()))))())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()))))())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())(()())(()())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())(()())(()())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()(()(()))((()))(()(()(()(())))()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()(()(()))((()))(()(()(()(())))()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))())((())()())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))())((())()())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(((()))()()(()(()(()))))(())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(((()))()()(()(()(()))))(())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((())))))))()()") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((())))))))()()") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "))(()(()))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))(()(()))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())()(()))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())()(()))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = ")((((((((((())") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")((((((((((())") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()()))))(()(()(()))))()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()()))))(()(()(()))))()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()))(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()))(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((())))))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((())))))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()((()())(()())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()((()())(()())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "())()()()(((())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())()()()(((())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()())(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()())(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()))(()(())))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()))(()(())))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()(()))(()((()())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()(()))(()((()())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())(()(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())(()(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()()(()))(()(()(()))(()(()))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()()(()))(()(()(()))(()(()))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = ")((((((()())") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")((((((()())") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()))(()(()))(()(()))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()))(()(()))(()(()))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()(()))(()") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()(()))(()") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((())(())))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((())(())))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()))))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()))))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())())(()(()(()))())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())())(()(()(()))())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()())))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()())))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()))(()(()))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()))(()(()))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()())())))())())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()())())))())())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())((()()(())))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())((()()(())))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()()(()(())))()(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()()(()(())))()(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))()()()(((()(()))))()()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))()()()(((()(()))))()()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()))))))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()))))))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()())))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()())))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(((())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(((())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()())(()(()))(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()())(()(()))(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = ")(()(()(()(()(())))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")(()(()(()(()(())))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((()))))))))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((()))))))))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(())))))(((()()()(()(()))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())))))(((()()()(()(()))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = ")(()(()(()(()))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")(()(()(()(()))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()))(()(()(()(()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()))(()(()(()(()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((())))))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((())))))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()))(()(()(()())))((()())())") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()))(()(()(()())))((()())())") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((())))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((())))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()())()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()())()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()))))())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()))))())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(())))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(())))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()(()()())()()()()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()(()()())()()()()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())(()())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())(()())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()(()(()(())))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()(()(()(())))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()()()()()()") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()()()()()()") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()))((())((())())") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()))((())((())())") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()(()))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()(()))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "())())())())())())") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())())())())())())") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))())(()") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))())(()") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(())))))()") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())))))()") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()((())))()()(()(()))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()((())))()()(()(()))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))()(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))()(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()))(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()))(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()(()()((()())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()(()()((()())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))((())(()(())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))((())(()(())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()()(()(()())))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()()(()(()())))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "())((())") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())((())") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((()))())())())(())))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((()))())())())(())))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))()") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))()") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "))))))))))))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))))))))))))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()(((()))))((()))(()(()))(()())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()(((()))))((()))(()(()))(()())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())()(()(()))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())()(()(()))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(((((((((()))))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(((((((((()))))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))()(()(()))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))()(()(()))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(((())))())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(((())))())") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(()))") == 1
    assert candidate(s = "())") == 1
    assert candidate(s = "()") == 0
    assert candidate(s = "((((((()))") == 4
    assert candidate(s = "())(()") == 2
    assert candidate(s = "((()))") == 0
    assert candidate(s = "((") == 2
    assert candidate(s = "") == 0
    assert candidate(s = "(()))(") == 2
    assert candidate(s = "(())") == 0
    assert candidate(s = "(()))(()") == 2
    assert candidate(s = "()))((") == 4
    assert candidate(s = "))(()()((()(()))))") == 2
    assert candidate(s = "()()(()(()))(()(()(()(()))))") == 0
    assert candidate(s = "((((((((((()))))))))") == 2
    assert candidate(s = "(())))(()") == 3
    assert candidate(s = ")(()))()()") == 2
    assert candidate(s = "(()((())()()))") == 0
    assert candidate(s = "((((((())") == 5
    assert candidate(s = "()(()(()))") == 0
    assert candidate(s = "(()(()))()()(()(()()()(()())())") == 1
    assert candidate(s = "((((()()()(()))))") == 1
    assert candidate(s = "(()(()(()(()(()())())))") == 1
    assert candidate(s = "(()(()))))((()") == 4
    assert candidate(s = "(()(()))(()(()(()(()))))") == 0
    assert candidate(s = "(()())((()))") == 0
    assert candidate(s = "()))(((((()))))())") == 2
    assert candidate(s = "(((()(()(()(()))))))") == 0
    assert candidate(s = "((()))(())()(()(()))") == 0
    assert candidate(s = "(()(()(()(()(()))))())") == 0
    assert candidate(s = "(()())(()())(()())") == 0
    assert candidate(s = "()()()(()(()))((()))(()(()(()(())))()(()))") == 0
    assert candidate(s = "((()))())((())()())") == 1
    assert candidate(s = "()()()()()()()()()()()()()()") == 0
    assert candidate(s = "(()))(((()))()()(()(()(()))))(())") == 1
    assert candidate(s = "((((((((())))))))()()") == 1
    assert candidate(s = "((((((()))))") == 2
    assert candidate(s = "))(()(()))") == 2
    assert candidate(s = "((((((()))))))") == 0
    assert candidate(s = "(()((())()(()))") == 1
    assert candidate(s = ")((((((((((())") == 10
    assert candidate(s = "(()(()(()(()))))") == 0
    assert candidate(s = "(()(()(()(()(()()))))(()(()(()))))()") == 0
    assert candidate(s = "(()(()(()(()))(()(()))))") == 0
    assert candidate(s = "((((((())))))))") == 1
    assert candidate(s = "(()))(()((()())(()())))") == 1
    assert candidate(s = "(()())())") == 1
    assert candidate(s = "())()()()(((())))") == 1
    assert candidate(s = "(()(()))(()())(()(()))") == 0
    assert candidate(s = "(((()))(()(())))") == 0
    assert candidate(s = "()()(()))(()((()())))") == 1
    assert candidate(s = "((())(()(()(()))))") == 0
    assert candidate(s = "(()()(()))(()(()(()))(()(()))))") == 1
    assert candidate(s = "(()(()))") == 0
    assert candidate(s = ")((((((()())") == 6
    assert candidate(s = "(((()))(()(()))(()(()))") == 1
    assert candidate(s = ")()(()))(()") == 3
    assert candidate(s = "()()()()") == 0
    assert candidate(s = "(((())(())))") == 0
    assert candidate(s = "(()(()(()(()(()(()))))))") == 0
    assert candidate(s = "((())())(()(()(()))())") == 0
    assert candidate(s = "(()(()(()())))") == 0
    assert candidate(s = "())(()))(()(()))") == 2
    assert candidate(s = "(()(()(()(()(()(()())())))())())") == 0
    assert candidate(s = "(()())((()()(())))") == 0
    assert candidate(s = "(()(())))") == 1
    assert candidate(s = "(()()(()(())))()(()(()))") == 0
    assert candidate(s = "(((((())))))()()()(((()(()))))()()") == 0
    assert candidate(s = "(()(()(()(()(()(()(()))))))))") == 1
    assert candidate(s = "()(()(()(()(()))))") == 0
    assert candidate(s = "(()(()))(()(()))") == 0
    assert candidate(s = "()(()(()(()())))") == 0
    assert candidate(s = "())(((())))") == 1
    assert candidate(s = "()())(()(()))(()") == 2
    assert candidate(s = ")(()(()(()(()(())))))") == 1
    assert candidate(s = "((((((((((()))))))))))") == 0
    assert candidate(s = "(())))))(((()()()(()(()))))))") == 5
    assert candidate(s = ")(()(()(()(()))))") == 1
    assert candidate(s = "()(()(()))(()(()(()(()))))") == 0
    assert candidate(s = "(((((((())))))))") == 0
    assert candidate(s = "())(()))(()(()(()())))((()())())") == 2
    assert candidate(s = "(((((((())))))") == 2
    assert candidate(s = "(((()())()))") == 0
    assert candidate(s = "(()(()(()(()))))())") == 1
    assert candidate(s = "(()))(()))(())))") == 4
    assert candidate(s = "()()()(()()())()()()()") == 0
    assert candidate(s = "(()())(()())") == 0
    assert candidate(s = "(()(()))(()(()(()(()(())))))") == 0
    assert candidate(s = ")()()()()()()") == 1
    assert candidate(s = "()(()))((())((())())") == 2
    assert candidate(s = "())(()(()))") == 1
    assert candidate(s = "())())())())())())") == 6
    assert candidate(s = "(()))())(()") == 3
    assert candidate(s = "()()()()()()()()") == 0
    assert candidate(s = "((())(()))") == 0
    assert candidate(s = "(())))))()") == 4
    assert candidate(s = "()(()((())))()()(()(()))))") == 2
    assert candidate(s = "(()(()))()(()(()))") == 0
    assert candidate(s = "(()))(()))") == 2
    assert candidate(s = "(((()))(()))") == 0
    assert candidate(s = "()()()()()()") == 0
    assert candidate(s = ")()(()()((()())))") == 1
    assert candidate(s = "(()))((())(()(())))") == 1
    assert candidate(s = "()(()()(()(()())))") == 0
    assert candidate(s = "())((())") == 2
    assert candidate(s = "(((((((()))())())())(())))))") == 2
    assert candidate(s = "(((((())))))()") == 0
    assert candidate(s = "))))))))))))") == 12
    assert candidate(s = "()()()(((()))))((()))(()(()))(()())") == 1
    assert candidate(s = "((())()(()(()))") == 1
    assert candidate(s = "())(()()") == 2
    assert candidate(s = "(()(((((((((()))))))") == 4
    assert candidate(s = "((((()))))") == 0
    assert candidate(s = "(((((())))))()(()(()))") == 0
    assert candidate(s = "(()(((())))())") == 0


