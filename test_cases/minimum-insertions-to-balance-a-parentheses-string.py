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
        result = candidate(s = "))())(") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))())(") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "())") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(())))))))))))()()") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(())))))))))))()()") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(())))()") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(())))()") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()))())(()(()))()") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()))())(()(()))()") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()(()(()(())))()()") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()(()(()(())))()()") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()(()(()(()(())))))()))))))))))))))))))))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()(()(()(()(())))))()))))))))))))))))))))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()(()(()(())))") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()(()(()(())))") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((())") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((())") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))()(()))(())))()") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))()(()))(())))()") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = ")((((()))))))))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")((((()))))))))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))())") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))())") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((())))))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((())))))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()())()(()(()(())))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()())()(()(()(())))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((())))))))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((())))))))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()()(()(()(()))))(()))(()))(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()()(()(()(()))))(()))(()))(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()()()()()()()") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()()()()()()()") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())()())") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())()())") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()(()))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()(()))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))))())()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))))())()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "())()(()))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())()(()))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))(()(()))()(()(()))()()") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))(()(()))()(()(()))()()") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()(()))(()(()))(()(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()(()))(()(()))(()(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "))))))))))))))))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))))))))))))))))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(((()(()))())()()(())))") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(((()(()))())()()(())))") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))(((((())))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))(((((())))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((()))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((()))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()))))()(()(()))(()(()))()") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()))))()(()(()))(()(()))()") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()())") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()())") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())))))((()))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())))))((()))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()()(()(()(())))()()(()(()(())))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()()(()(()(())))()()(()(()(())))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))()(()))(()))(()))(()))(()))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))()(()))(()))(()))(()))(()))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))))())()") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))))())()") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()))))(())))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()))))(())))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = ")(((((((((((((())))))))))))") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")(((((((((((((())))))))))))") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))(()(()))()(()(()))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))(()(()))()(()(()))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(())))))()()()()()()()()()") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(())))))()()()()()()()()()") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))(((((())))))))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))(((((())))))))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = ")(()))(()(()))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")(()))(()(()))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()()(()(()(()))))(()))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()()(()(()(()))))(()))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))))())()()()") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))))())()()()") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((()))(()))()))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((()))(()))()))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((()))))()(()(()))(()(()))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((()))))()(()(()))(()(()))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((((())))))))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((((())))))))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()((())(()))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()((())(()))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((((((())))))))))))))()()()()()()()()()()()()()()()()()()()()()()()") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((((((())))))))))))))()()()()()()()()()()()()()()()()()()()()()()()") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()(()))())") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()(()))())") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))())") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))())") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()(()()(())))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()(()()(())))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((((((((())))))))))))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((((((((())))))))))))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))()(()))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))()(()))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))(()))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))(()))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(())))()())") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(())))()())") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()))(()(()))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()))(()(()))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))()(()))(())))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))()(()))(())))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))(()))(()))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))(()))(()))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))()()()()()()()") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))()()()()()()()") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))())(())))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))())(())))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()()()()()()()()()()()()()()()()()()()()()") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()()()()()()()()()()()()()()()()()()()()()") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((()))())(()(((()))())))") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((()))())(()(((()))())))") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(())))))()()()()()()()()()()()()()()") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(())))))()()()()()()()()()()()()()()") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))()(()))(()))(()))(()))(()))()(()))(()))(()))()(()))(()))()(()))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))()(()))(()))(()))(()))(()))()(()))(()))(()))()(()))(()))()(()))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))())))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))())))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "()((((()))))))((((()))))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()((((()))))))((((()))))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))(()") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))(()") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((())))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((())))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((())))))()(()))(()))(()))(()))(()))()(()))(()))(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((())))))()(()))(()))(()))(()))(()))()(()))(()))(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))()()") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))()()") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))())))()()") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))())))()()") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))()())") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))()())") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "())()(()(()(()(()))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())()(()(()(()(()))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "))))(((") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))))(((") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()))))())") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()))))())") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(())))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(())))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(())))()") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(())))()") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()()(()(()(()))))(()))(()))(()))(()))") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()()(()(()(()))))(()))(()))(()))(()))") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()()(()(()(()(()(())))))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()()(()(()(()(()(())))))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()))))(())))") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()))))(())))") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = ")()()()()()()") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ")()()()()()()") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()))))())") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()))))())") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))(()))(()))(()))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))(()))(()))(()))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(())))()()(()(()(())))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(())))()()(()(()(())))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()(()(())))()()(()(()(()))))(()))(()))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()(()(())))()()(()(()(()))))(()))(()))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((()))))(()(()))(()(()))()()()()") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((()))))(()(()))(()(()))()()()()") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((((()))))))))))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((((()))))))))))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()))())(()))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()))())(()))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(((())))((()))(()))()()(()(())))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(((())))((()))(()))()()(()(())))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "()))))(((()))(()))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()))))(((()))(()))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()))(()(()(()))())") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()))(()(()(()))())") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(()))))))))))))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(()))))))))))))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "())(()(()(()))())") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "())(()(()(()))())") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((()))))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((()))))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()()()()()()()") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()()()()()()()") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(()(()(()(()(()(())))))()()()()()()") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(()(()(()(()(()(())))))()()()()()()") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((()))))(()(()))()(()(()))()()()") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((()))))(()(()))()(()(()))()()()") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "(()(()(()(()(())))))))()(()))(()))") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(()(()(()(()(())))))))()(()))(()))") == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(()))") == 1
    assert candidate(s = "))())(") == 3
    assert candidate(s = "())") == 0
    assert candidate(s = "(()(())))))))))))()()") == 6
    assert candidate(s = "(()))(()))(()))(()))(())))()") == 5
    assert candidate(s = "(()(()(()(()(())))))") == 10
    assert candidate(s = "()(()(()))())(()(()))()") == 10
    assert candidate(s = "(()(()(())))()(()(()(())))()()") == 15
    assert candidate(s = "(((()(()(()(()(())))))()))))))))))))))))))))") == 10
    assert candidate(s = "(()(()(())))()(()(()(())))") == 13
    assert candidate(s = "((((((())") == 12
    assert candidate(s = "(()(()(()(()(())))))))()(()))(())))()") == 11
    assert candidate(s = ")((((()))))))))))))") == 5
    assert candidate(s = "(()(()))())") == 4
    assert candidate(s = "((((((())))))") == 8
    assert candidate(s = "(((((())))))))") == 4
    assert candidate(s = "(()())()(()(()(())))") == 10
    assert candidate(s = "((((((())))))))))") == 4
    assert candidate(s = "(()(()(())))()()(()(()(()))))(()))(()))(()))") == 16
    assert candidate(s = "()()()()()()()()()()()()()()()()") == 16
    assert candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 9
    assert candidate(s = "((())()())") == 5
    assert candidate(s = "(()))(()(()))") == 5
    assert candidate(s = "()(()(()(()(()(()))))())()()") == 14
    assert candidate(s = "())()(()))") == 2
    assert candidate(s = "((((()))))(()(()))()(()(()))()()") == 16
    assert candidate(s = "(()(()))(()(()))(()(()))(()(()))") == 16
    assert candidate(s = "))))))))))))))))") == 8
    assert candidate(s = "(()(((()(()))())()()(())))") == 13
    assert candidate(s = "(((((())))(((((())))") == 16
    assert candidate(s = "((((((((()))))))))") == 9
    assert candidate(s = "(()(()(()(()(())))))))") == 8
    assert candidate(s = "(((()))))()(()(()))(()(()))()") == 13
    assert candidate(s = "((((((()))))))") == 7
    assert candidate(s = "(()))(()))(()())") == 5
    assert candidate(s = "((())))))((()))))") == 1
    assert candidate(s = "(()(()(())))()()(()(()(())))()()(()(()(())))") == 22
    assert candidate(s = "(((((())))))()(()))(()))(()))(()))(()))") == 12
    assert candidate(s = "()(()(()(()(()(()))))())()") == 13
    assert candidate(s = "()(()(()(()(()))))(())))") == 9
    assert candidate(s = ")(((((((((((((())))))))))))") == 18
    assert candidate(s = "((((()))))(()(()))()(()(()))") == 14
    assert candidate(s = "()(()(()(()(()(()(())))))()()()()()()()()()") == 23
    assert candidate(s = "(((((())))(((((())))))))") == 12
    assert candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))") == 8
    assert candidate(s = ")(()))(()(()))") == 7
    assert candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 12
    assert candidate(s = "(()(()(())))()()(()(()(()))))(()))") == 14
    assert candidate(s = "()(()(()(()(()(()))))())()()()") == 15
    assert candidate(s = "()()()()()()()()()()") == 10
    assert candidate(s = "(((((()))(()))()))") == 9
    assert candidate(s = "(((()))))()(()(()))(()(()))") == 12
    assert candidate(s = "(((((((((())))))))") == 12
    assert candidate(s = "(()((())(()))") == 8
    assert candidate(s = "((((((((((((((())))))))))))))()()()()()()()()()()()()()()()()()()()()()()()") == 39
    assert candidate(s = "(()))(()(()))())") == 5
    assert candidate(s = "(()))())") == 1
    assert candidate(s = "()()()()") == 4
    assert candidate(s = "(()))(()))(()(()()(())))") == 9
    assert candidate(s = "(()))(()))(()))(()))") == 4
    assert candidate(s = "(((((((((((((())))))))))))") == 16
    assert candidate(s = "(()(()(()(()(())))))))()(()))") == 10
    assert candidate(s = "((((()))))))") == 3
    assert candidate(s = "(()))(()))(()))(()))(()))(()))") == 6
    assert candidate(s = "(()(()(()(())))()())") == 10
    assert candidate(s = "())(()))(()(()))") == 5
    assert candidate(s = "(()(()(()(()(())))))))()(()))(())))") == 10
    assert candidate(s = "(()(()(())))") == 6
    assert candidate(s = "(()))(()))(()))") == 3
    assert candidate(s = "(()))(()))(()))(()))(()))(()))(()))") == 7
    assert candidate(s = "((()))()()()()()()()") == 10
    assert candidate(s = "(()))())(())))") == 1
    assert candidate(s = ")()()()()()()()()()()()()()()()()()()()()()") == 23
    assert candidate(s = "(((((()))())(()(((()))())))") == 15
    assert candidate(s = "()(()(()(()(()(()(())))))()()()()()()()()()()()()()()") == 28
    assert candidate(s = "(((((())))))()(()))(()))(()))(()))(()))()(()))(()))(()))()(()))(()))()(()))") == 21
    assert candidate(s = "()(()(()(()(()))))") == 9
    assert candidate(s = "(()))(()))(()))(()))(()))(()))(()))(()))(()))(()))") == 10
    assert candidate(s = "()(()(()(()(()(()))())))") == 12
    assert candidate(s = "()((((()))))))((((()))))))") == 7
    assert candidate(s = "(()(()))(()") == 7
    assert candidate(s = "(((())))") == 4
    assert candidate(s = "(((((())))))()(()))(()))(()))(()))(()))()(()))(()))(()))") == 16
    assert candidate(s = "(()(()(()(()(())))))))()()") == 10
    assert candidate(s = "()(()(()(()(()(()))())))()()") == 14
    assert candidate(s = "(()(()(()(()(())))))))()())") == 9
    assert candidate(s = "())()(()(()(()(()))))") == 9
    assert candidate(s = "))))(((") == 8
    assert candidate(s = "(()(()(()(()))))())") == 8
    assert candidate(s = "(()))(()))(())))") == 2
    assert candidate(s = "()(()(()(())))()") == 8
    assert candidate(s = "(()(()(())))()()(()(()(()))))(()))(()))(()))(()))") == 17
    assert candidate(s = "()()()()()()()()()()(()(()(()(()(())))))") == 20
    assert candidate(s = "(()(()(()(()(()))))(())))") == 11
    assert candidate(s = ")()()()()()()") == 8
    assert candidate(s = "()(()(()(()(()(()))))())") == 12
    assert candidate(s = "(()))(()))(()))(()))(()))") == 5
    assert candidate(s = "(()(()(())))()()(()(()(())))") == 14
    assert candidate(s = "(()))(()(()(())))()()(()(()(()))))(()))(()))") == 16
    assert candidate(s = "(((((()))))(()(()))(()(()))()()()()") == 19
    assert candidate(s = "((((((((((((()))))))))))))))))") == 9
    assert candidate(s = "(()(()))())(()))") == 5
    assert candidate(s = "(()))(()))") == 2
    assert candidate(s = "()()()()()()") == 6
    assert candidate(s = "(()))(((())))((()))(()))()()(()(())))") == 14
    assert candidate(s = "()))))(((()))(()))") == 9
    assert candidate(s = "(()))(()(()(()))())") == 8
    assert candidate(s = "(()(()(()(()(()))))))))))))))") == 7
    assert candidate(s = "((()))))") == 1
    assert candidate(s = "())(()(()(()))())") == 7
    assert candidate(s = "((((((()))))))))") == 5
    assert candidate(s = "()()()()()()()()()") == 9
    assert candidate(s = "()(()(()(()(()(()(())))))()()()()()()") == 20
    assert candidate(s = "((((()))))(()(()))()(()(()))()()()") == 17
    assert candidate(s = "(()(()(()(()(())))))))()(()))(()))") == 11


