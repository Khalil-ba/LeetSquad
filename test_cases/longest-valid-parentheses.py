def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "(()())") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "())") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())()())()") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())()())()") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()(()(()))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()(()(()))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()))))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()))))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()())") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()())") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()(())") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()(())") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))()") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))()") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))(())()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))(())()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())()())") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())()())") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(())())()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(())())()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((()))))))))))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((()))))))))))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "())()(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())()(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((())))()()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((())))()()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())()())())") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())()())())") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())((()))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())((()))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()())") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()())") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()()()") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()()()") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()()") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()()") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 80: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()))()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()))()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())()()))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())()()))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))((((()))))((((()))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))((((()))))((((()))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((((())))))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((((())))))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((((((((())))))))))()))))))))))))))))))()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((((((((())))))))))()))))))))))))))))))()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())()(()))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())()(()))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())())())") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())())())") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "()((((((()))))))()") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()((((((()))))))()") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()(()(()(()(()(()()))))))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()(()(()(()(()(()()))))))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))(((())))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))(((())))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((())))(((())))(((())))(((())))") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((())))(((())))(((())))(((())))") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((())))))))))))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((())))))))))))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(((()))()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(((()))()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))(((((())))))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))(((((())))))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()(()(()))(()(()))()()") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()(()(()))(()(()))()()") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()))))())") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()))))())") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())(()())(()())") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())(()())(()())") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()(()(()(()(()(()()))))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()(()(()(()(()(()()))))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()))(()(()))(()(()))") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()))(()(()))(()(()))") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((()))))))))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((()))))))))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()()()()()()))((()()()()()()))") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()()()()()()))((()()()()()()))") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "()((()))()(()(()))()") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()((()))()(()(()))()") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((()(()(()(()(()(()()))))))))))()()()") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((()(()(()(()(()(()()))))))))))()()()") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(())))))))()()") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(())))))))()()") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()))()))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()))()))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()())(()(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()())(()(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(())))))))))") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(())))))))))") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(()(()(()))()))))))()()") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(()(()(()))()))))))()()") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()))()()()") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()))()()()") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(()(()(()(()))))))))))))))") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(()(()(()(()))))))))))))))") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))((()))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))((()))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()()(()())))()()") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()()(()())))()()") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(()(()))))))))))))()(()(()(()))()()()()()()()()") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(()(()))))))))))))()(()(()(()))()()()()()()()()") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())((()))(((())))))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())((()))(((())))))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((()))))))(()(()(()(()(()(()(()))))))))()()") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((()))))))(()(()(()(()(()(()(()))))))))()()") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(()(()(()(())))))()))))))))") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(()(()(()(())))))()))))))))") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()()))))))") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()()))))))") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()))))))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()))))))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(()(()(()(()()))))))))))()())") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(()(()(()(()()))))))))))()())") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(())))))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(())))))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()(()))(()(()))))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()(()))(()(()))))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "()((((()))))()(()(()))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()((((()))))()(()(()))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((((()))))))()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((((()))))))()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))(()(()))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))(()(()))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()))))())()()") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()))))())()()") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(()(()(()(()(()(()))()))))))))))))))))))") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(()(()(()(()(()(()))()))))))))))))))))))") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()))))))))))))()(()(()(()))") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()))))))))))))()(()(()(()))") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()))(()(())))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()))(()(())))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()()(()())()(()(())))))()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()()(()())()(()(())))))()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 126: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(()(())))))))))") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(()(())))))))))") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))()(()())") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))()(()())") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "()((((((((())))))))))()()") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()((((((((())))))))))()()") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(())))))()()()") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(())))))()()()") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()()))))))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()()))))))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())())(()(()(()())))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())())(()(()(()())))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))((()))((()))((()))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))((()))((()))((()))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))()((()))()((()))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))()((()))()((()))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()))))))))))))()") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()))))))))))))()") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(())((())))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(())((())))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((()))))))))))))))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((()))))))))))))))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(())))))))") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(())))))))") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()))))))())") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()))))))())") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()(()(()(()(()()))))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()(()(()(()(()()))))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()))(()(()))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()))(()(()))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(())))))())))") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(())))))())))") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(()(()(()))))))))))))()(()(()(()))()()()()()()()()(()(()(())))") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(()(()(()))))))))))))()(()(()(()))()()()()()()()()(()(()(())))") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(()(())))))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(()(())))))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()()(()))((())())") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()()(()))((())())") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))(((()(()))(()))(()(()))(()(()))(()(()))(()(())))") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))(((()(()))(()))(()(()))(()(()))(()(()))(()(())))") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()(()(())))))())()()()") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()(()(())))))())()()()") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(())))))()()") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(())))))()()") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))(()(()))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))(()(()))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()())(()(()()(())))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()())(()(()()(())))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())())(()(()(()(()))))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())())(()(()(()(()))))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()))(()))(()())") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()))(()))(()())") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())())(()(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())())(()(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()))(()(()))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()))(()(()))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()()()(()(()))") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()()()(()(()))") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((()(()))(()(())))))())") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((()(()))(()(())))))())") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(()(()))))))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(()(()))))))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())((()))(()(()))(()))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())((()))(()(()))(()))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()()(()(()())))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()()(()(()())))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()(()())))()((()(())))") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()(()())))()((()(())))") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))()()()(()))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))()()()(()))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))))(()(()(())))") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))))(()(()(())))") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()(()(()(()())))))()())") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()(()(()(()())))))()())") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(())))))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(())))))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()()()()()") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()()()()()") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))))(()(()(()(()))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))))(()(()(()(()))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())(())(()(()(()(())))())") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())(())(()(()(()(())))())") == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(()())") == 6
    assert candidate(s = "())") == 2
    assert candidate(s = "())(()") == 2
    assert candidate(s = "((((((()))))))") == 14
    assert candidate(s = "((())()())()") == 12
    assert candidate(s = ")()(()(()))") == 10
    assert candidate(s = "(()(()(()(()))))") == 16
    assert candidate(s = ")()())") == 4
    assert candidate(s = "()()()()()()()()") == 16
    assert candidate(s = "()(()(()))") == 10
    assert candidate(s = "()()(())") == 8
    assert candidate(s = "") == 0
    assert candidate(s = "(()))()") == 4
    assert candidate(s = "(()))(()))") == 4
    assert candidate(s = "(()))") == 4
    assert candidate(s = "(()(()))") == 8
    assert candidate(s = "((()))(())()()") == 14
    assert candidate(s = "((())()())") == 10
    assert candidate(s = "(()(())())()()") == 14
    assert candidate(s = "()(()(()(()(()(()))))") == 18
    assert candidate(s = "((((((((((()))))))))))") == 22
    assert candidate(s = "())()(()") == 2
    assert candidate(s = "()(()") == 2
    assert candidate(s = "(()") == 2
    assert candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 72
    assert candidate(s = "(((())))()()()") == 14
    assert candidate(s = "(()((())()())())") == 16
    assert candidate(s = "()()()()()()()()()") == 18
    assert candidate(s = "((())((()))") == 10
    assert candidate(s = "((()))") == 6
    assert candidate(s = "(()))(()())") == 6
    assert candidate(s = "()()") == 4
    assert candidate(s = "()()()()") == 8
    assert candidate(s = "()()()()()()()()()()()()()()()()()()") == 36
    assert candidate(s = "()()()()()()()()()()()()()()()()()") == 34
    assert candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 80
    assert candidate(s = "(()(()(()(()(())))))") == 20
    assert candidate(s = "()(()(()))()()") == 14
    assert candidate(s = "(()((())()()))") == 14
    assert candidate(s = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 60
    assert candidate(s = "((((()))))((((()))))((((()))))") == 30
    assert candidate(s = "(()((((())))))") == 14
    assert candidate(s = "(((((((((((((())))))))))()))))))))))))))))))()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 60
    assert candidate(s = "((())()(()))") == 12
    assert candidate(s = "(((((())))))") == 12
    assert candidate(s = "(()((())())())") == 14
    assert candidate(s = "()((((((()))))))()") == 18
    assert candidate(s = "(((()(()(()(()(()(()()))))))))") == 30
    assert candidate(s = "((((()))))(((())))") == 18
    assert candidate(s = "(((())))(((())))(((())))(((())))") == 32
    assert candidate(s = "((((((((((())))))))))))") == 22
    assert candidate(s = "()(()(((()))()))") == 16
    assert candidate(s = "(((((())))))(((((())))))") == 24
    assert candidate(s = "()()(()(()))(()(()))()()") == 24
    assert candidate(s = "(()(()(()(()(()))))())") == 22
    assert candidate(s = "(()())(()())(()())") == 18
    assert candidate(s = "()()()(()(()(()(()(()()))))") == 20
    assert candidate(s = "(()(()))(()(()))(()(()))(()(()))") == 32
    assert candidate(s = "((((((((()))))))))") == 18
    assert candidate(s = "((()()()()()()))((()()()()()()))") == 32
    assert candidate(s = "()((()))()(()(()))()") == 20
    assert candidate(s = "(((((()(()(()(()(()(()()))))))))))()()()") == 40
    assert candidate(s = "(()(()(()(()(()(()(()(())))))))()()") == 34
    assert candidate(s = "(()(()(()(()))()))") == 18
    assert candidate(s = "()(()())(()(()))") == 16
    assert candidate(s = "(()(()(()(()(()(()(()(())))))))))") == 32
    assert candidate(s = "()(()(()(()(()(()(()(()(()))()))))))()()") == 40
    assert candidate(s = "()(()(()))()()()") == 16
    assert candidate(s = "(()(()(()(()(()(()(()(()(()(()(()))))))))))))))") == 44
    assert candidate(s = "((()))((()))") == 12
    assert candidate(s = "((()()(()())))()()") == 18
    assert candidate(s = "()(()(()(()(()(()(()(()))))))))))))()(()(()(()))()()()()()()()()") == 30
    assert candidate(s = "(()((())((()))(((())))))") == 24
    assert candidate(s = "()()()()()()()()()()") == 20
    assert candidate(s = "((((((((()))))))(()(()(()(()(()(()(()))))))))()()") == 48
    assert candidate(s = "(()(()(()(()(()(()(()(()(()(()(())))))()))))))))") == 46
    assert candidate(s = "(()(()(()(()(()(()()))))))") == 26
    assert candidate(s = "(()(()(()(()(()(()))))))") == 24
    assert candidate(s = "(()(()(()(()(()(()(()(()(()(()(()()))))))))))()())") == 50
    assert candidate(s = "()(()(()(()(()(())))))") == 22
    assert candidate(s = "(((()(()))(()(()))))") == 20
    assert candidate(s = "()((((()))))()(()(()))") == 22
    assert candidate(s = "(()((((()))))))()()") == 14
    assert candidate(s = "((((()))))(()(()))") == 18
    assert candidate(s = "(()(()(()(()(()(()))))())()()") == 28
    assert candidate(s = "(()(()(()(()(()(()(()(()(()(()(()(()(()))()))))))))))))))))))") == 54
    assert candidate(s = "(()(()(()(()(()(()(()))))))))))))()(()(()(()))") == 28
    assert candidate(s = "(()(()(()))(()(())))") == 20
    assert candidate(s = "(()(()))(()(()))") == 16
    assert candidate(s = "(((()()(()())()(()(())))))()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 126
    assert candidate(s = "(()(()(()(()(()(()(()(()(())))))))))") == 36
    assert candidate(s = "(()(()))()(()())") == 16
    assert candidate(s = "()((((((((())))))))))()()") == 20
    assert candidate(s = "()(()(()(()(()(()(())))))()()()") == 28
    assert candidate(s = "(()(()(()(()(()(()(()()))))))))") == 30
    assert candidate(s = "((())())(()(()(()())))") == 22
    assert candidate(s = "((()))((()))((()))((()))") == 24
    assert candidate(s = "((()))()((()))()((()))") == 22
    assert candidate(s = "(()(()(()(()(()(()(()))))))))))))()") == 28
    assert candidate(s = "(()(())((())))") == 14
    assert candidate(s = "((((((((()))))))))))))))") == 18
    assert candidate(s = "(()(()(()(()(()(()(())))))))") == 28
    assert candidate(s = "(()(()(()(()(()(()(()))))))())") == 30
    assert candidate(s = "()()(()(()(()(()()))))") == 22
    assert candidate(s = "()(()))(()(()))") == 8
    assert candidate(s = "(()(()(()(()(()(()(()(())))))())))") == 34
    assert candidate(s = "(()(()(()(()(()(()(()(()(()))))))))))))()(()(()(()))()()()()()()()()(()(()(())))") == 38
    assert candidate(s = "()(()(()(()(()(()(()(())))))))") == 30
    assert candidate(s = "(()()(()))((())())") == 18
    assert candidate(s = "(((((())))))(((()(()))(()))(()(()))(()(()))(()(()))(()(())))") == 60
    assert candidate(s = "(()(()(()(()(()(()(())))))())()()()") == 34
    assert candidate(s = "()(()(()(()(()(())))))()()") == 26
    assert candidate(s = "((()))(()(()))") == 14
    assert candidate(s = "())(()())(()(()()(())))") == 20
    assert candidate(s = "((())())(()(()(()(()))))") == 24
    assert candidate(s = "(((()))(()))(()())") == 18
    assert candidate(s = "((())())(()(()))") == 16
    assert candidate(s = "(()(()))(()(()))(()(()))") == 24
    assert candidate(s = "(()(()(())))()()()(()(()))") == 26
    assert candidate(s = "()()()()()()()()()()()()") == 24
    assert candidate(s = "(((((()(()))(()(())))))())") == 26
    assert candidate(s = "()(()(()(()(()(()(()(()))))))))") == 30
    assert candidate(s = "((())((()))(()(()))(()))") == 24
    assert candidate(s = "()(()()(()(()())))") == 18
    assert candidate(s = "((()(()())))()((()(())))") == 24
    assert candidate(s = "((((()))()()()(()))") == 18
    assert candidate(s = "((((((()))))))(()(()(())))") == 26
    assert candidate(s = "(((()(()(()(()())))))()())") == 26
    assert candidate(s = "()(()(()(()(()(()(())))))") == 22
    assert candidate(s = "()()()()()()()()()()()()()()()()()()()()") == 40
    assert candidate(s = "()()()()()()()()()()()()()()()") == 30
    assert candidate(s = "((((((()))))))(()(()(()(()))))") == 30
    assert candidate(s = "(()())(())(()(()(()(())))())") == 28


