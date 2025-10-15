def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(expression = "(1&(0|1&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(0|1&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&1&1)|(0|1)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&1&1)|(0|1)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&1)|(0&0)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&1)|(0&0)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0&0)|(1|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0&0)|(1|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "1&(1&(1&(1&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1&(1&(1&(1&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|1)&(0|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|1)&(0|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "1&(0|1)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1&(0|1)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&1)|(0&0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&1)|(0&0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&1&1)|(1|1|1)") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&1&1)|(1|1|1)") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "1|1|0&1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1|1|0&1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&0)|((1&1)|(0&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&0)|((1&1)|(0&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((1&1)&(1&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((1&1)&(1&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(1&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(1&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&0&0)|(0|0|0)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&0&0)|(0|0|0)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "0|1&(1|0)&1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "0|1&(1|0)&1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "1|1|(0&0)&1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1|1|(0&0)&1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&1)|(0&0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&1)|(0&0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0&1)|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0&1)|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|(1|0&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|(1|0&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((0|0)|(0|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((0|0)|(0|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&0)|(1&1)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&0)|(1&1)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&0)&(0&0&0)") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&0)&(0&0&0)") == 3: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|(0|(0|(0|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|(0|(0|(0|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|0)&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|0)&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|0|0)&(1&1)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|0|0)&(1&1)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(1&(1&(1&1))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(1&(1&(1&1))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&1&1)|(0|0|0)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&1&1)|(0|0|0)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&1)|((1|0)&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&1)|((1|0)&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "0|(0|(0|(0|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "0|(0|(0|(0|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(0|(1&0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(0|(1&0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(1|0))&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(1|0))&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&(((0|1)&(1|0))|((1&0)|(0|1))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&(((0|1)&(1|0))|((1&0)|(0|1))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(((1|0)|(0&1))&(1&1)))|((1|0)|(0|1)))&(1|0)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(((1|0)|(0&1))&(1&1)))|((1|0)|(0|1)))&(1|0)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(1|0))&(0&(1|0))&(0&(1|0)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(1|0))&(0&(1|0))&(0&(1|0)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((1&0)|(0|1)&((1|0)&(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((1&0)|(0|1)&((1|0)&(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&((1|0)|(0|1)))&((0&0)|(1&(1&(1&1)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&((1|0)|(0|1)))&((0&0)|(1&(1&(1&1)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|1)&(1|(0|1&0))&(1|(0&(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|1)&(1|(0|1&0))&(1|(0&(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&((0|1)&(0|1)))|((0&(1|0))&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&((0|1)&(0|1)))|((0&(1|0))&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|0)|(1|1))&((0|0)|(1|1))&((0|0)|(1|1))&((0|0)|(1|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|0)|(1|1))&((0|0)|(1|1))&((0|0)|(1|1))&((0|0)|(1|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)|(0&1))&((0|1)|(0&1))&((1|0)|(0&1))&((0|1)|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)|(0&1))&((0|1)|(0&1))&((1|0)|(0&1))&((0|1)|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&0)&(0&0)&(1|1)&((0|0)|(1|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&0)&(0&0)&(1|1)&((0|0)|(1|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(0|1)&((1|0)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(0|1)&((1|0)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|0)&(1&0)|(0|1)&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|0)&(1&0)|(0|1)&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|0)|(0&1)&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|0)|(0&1)&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(((1|0)&(0|1)))&(((0&1)|(1&1))&(1|0)))|(0|1)") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(((1|0)&(0|1)))&(((0&1)|(1&1))&(1|0)))|(0|1)") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(1|0)&(1|0))|(0&(0|1)&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(1|0)&(1|0))|(0&(0|1)&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(0|1))&((1&0)|(1&0))&((0|1)&(0|1))&((1&0)|(1&0)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(0|1))&((1&0)|(1&0))&((0|1)&(0|1))&((1&0)|(1&0)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|1)|(0|0))&(1&(1&(1&1))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|1)|(0|0))&(1&(1&(1&1))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|((0&1)|(1|((1&0)|(0|1)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|((0&1)|(1|((1&0)|(0|1)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0&(1|0))&(1&((0&1)|(1|0))))|((1&0)|(0&((1&0)|(0&1)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0&(1|0))&(1&((0&1)|(1|0))))|((1&0)|(0&((1&0)|(0&1)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)&(0|1))&((1|0)&(0|1)))|(1&(0|((1&1)|(0&0))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)&(0|1))&((1|0)&(0|1)))|(1&(0|((1&1)|(0&0))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(1|0))|((1&(0|1))|(0&1)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(1|0))|((1&(0|1))|(0&1)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((1&0)|(0|1)&((1|0)|(0|1)&(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((1&0)|(0|1)&((1|0)|(0|1)&(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)|(1&0))&((0&1)|(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)|(1&0))&((0&1)|(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(1&0)|(0|1)&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(1&0)|(0|1)&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(((1|0)&(1|0))|((0&1)|(0&1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(((1|0)&(1|0))|((0&1)|(0&1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(0|((1&1)|(0|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(0|((1&1)|(0|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(((0|1)&(0|1))&((1|0)|(0|1)&(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(((0|1)&(0|1))&((1|0)|(0|1)&(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&((0&1)|(1|0)))|((1&((0&1)|(1|0)))&(1&(0&(1|0)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&((0&1)|(1|0)))|((1&((0&1)|(1|0)))&(1&(0&(1|0)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(0|1)&((1|0)|(0|1)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(0|1)&((1|0)|(0|1)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(0&(1|0))|(0&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(0&(1|0))|(0&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((1&1)|(0&0)))&(1&(0|((1&1)|(0&0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((1&1)|(0&0)))&(1&(0|((1&1)|(0&0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(((0&(1|0))|(1&0))&((1|0)&(0|1))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(((0&(1|0))|(1&0))&((1|0)&(0|1))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)&(0|1))|((0&1)|(1|0))|((1|0)&(0|1))|((0&1)|(1|0)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)&(0|1))|((0&1)|(1|0))|((1|0)&(0|1))|((0&1)|(1|0)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&0)|(0&1))&((0&(1|0))|(1&((0&1)|(1|0)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&0)|(0&1))&((0&(1|0))|(1&((0&1)|(1|0)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&0)|(0|1))&((1|0)|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&0)|(0|1))&((1|0)|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(1&1))&(1|0)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(1&1))&(1|0)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|1)|(0&0))&((1&1)|(0|0))|(1|0))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|1)|(0&0))&((1&1)|(0|0))|(1|0))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|((0&0)|(1&1)))&(1|0))|((0|1)&(1&1))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|((0&0)|(1&1)))&(1|0))|((0|1)&(1&1))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)&1)|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)&1)|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&1)|(1&(0|1)))&((1&0)|(1|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&1)|(1&(0|1)))&((1&0)|(1|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0|1)&(0|1))&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0|1)&(0|1))&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|1)|(1|0)&(0|1)&(0|1))&((0|1)|(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|1)|(1|0)&(0|1)&(0|1))&((0|1)|(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0&1)|(0&(1|0))&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0&1)|(0&(1|0))&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((1|0)&(0|1)))|(((0&1)|(1&1))&(1|0))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((1|0)&(0|1)))|(((0&1)|(1&1))&(1|0))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&((1|0)&(0|1)))|((0&(1|0))&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&((1|0)&(0|1)))|((0&(1|0))&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(0|1))&((1|0)|(0|1)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(0|1))&((1|0)|(0|1)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(((0&0)|(1|1))&(1&((0&0)|(1|1)))))|((1&(0|((1&1)|(0&0))))&(1|0))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(((0&0)|(1|1))&(1&((0&0)|(1|1)))))|((1&(0|((1&1)|(0&0))))&(1|0))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&1)&(0|0))|(1|0)&((1&0)|(0|1))&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&1)&(0|0))|(1|0)&((1&0)|(0|1))&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|(0&(1&0)))&(0|(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|(0&(1&0)))&(0|(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)|(0&1))&(1|(0&0)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)|(0&1))&(1|(0&0)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0|1)&(0&1))|(1&0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0|1)&(0&1))|(1&0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(1&(0|1))|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(1&(0|1))|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|(1&0))&(((1|0)&(0|1))|((0&1)|(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|(1&0))&(((1|0)&(0|1))|((0&1)|(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(((0|1)|(1&0))&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(((0|1)|(1&0))&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&(0|1))&((1&0)|(0&1)))|((0&(1|0))&(1&((0&1)|(1|0)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&(0|1))&((1&0)|(0&1)))|((0&(1|0))&(1&((0&1)|(1|0)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|1)|((1&(0|1))&(0|1)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|1)|((1&(0|1))&(0|1)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&1)|(0&1)|(0&1)|(0&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&1)|(0&1)|(0&1)|(0&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|(1&0)|(0|1)&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|(1&0)|(0|1)&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|((1|0)&(1|0))))&((1&(0|((1|0)&(1|0))))&((1&(0|((1|0)&(1|0))))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|((1|0)&(1|0))))&((1&(0|((1|0)&(1|0))))&((1&(0|((1|0)&(1|0))))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0&0)|(1&(0|1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0&0)|(1&(0|1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((1&((0|1)|(1|0)))&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((1&((0|1)|(1|0)))&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|((1&0)|(0|1)))&(((1|0)&(0|1))|((0&1)|(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|((1&0)|(0|1)))&(((1|0)&(0|1))|((0&1)|(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0|0)|(1&0))&(0&(1|0))&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0|0)|(1&0))&(0&(1|0))&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|1)|(0|0))&(1&0))|(0|1)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|1)|(0|0))&(1&0))|(0|1)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(0|((0|0)&(0|0))))|((1|0)&(1&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(0|((0|0)&(0|0))))|((1|0)&(1&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((1|0)|(0|1))&(0&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((1|0)|(0|1))&(0&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&1)|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&1)|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((1&0)|(0|1)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((1&0)|(0|1)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0&(1|0))&(1&(0|1&0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0&(1|0))&(1&(0|1&0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(1|1))|((1&0)|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(1|1))|((1&0)|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(((1|0)|(0&1))&(1&1)))|((0|1)&(1&1))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(((1|0)|(0&1))&(1&1)))|((0|1)&(1&1))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(0|1))&((1|0)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(0|1))&((1|0)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(1|0))&((1&0)|(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(1|0))&((1&0)|(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&((0&1)|(1|0)))&((1|0)|(0&(1|0))))|((1&(0|((1&1)|(0&0))))&(1|0))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&((0&1)|(1|0)))&((1|0)|(0&(1|0))))|((1&(0|((1&1)|(0&0))))&(1|0))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0&0)|(1&(0|1)))&((1|0)|(0&((0&1)|(1|0)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0&0)|(1&(0|1)))&((1|0)|(0&((0&1)|(1|0)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(1|0))|((1&0)|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(1|0))|((1&0)|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((1|0)|(0|1))&(0&(1|0))&(0|1)&((0|0)&(1|1)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((1|0)|(0|1))&(0&(1|0))&(0|1)&((0|0)&(1|1)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(1&(1&0)))|((0|1)|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(1&(1&0)))|((0|1)|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|0)&(0|1)|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|0)&(0|1)|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((1|0)&(0|1))&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((1|0)&(0|1))&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|((1&0)|(0&1))))&((0&(1|0))|(1&(0|1))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|((1&0)|(0&1))))&((0&(1|0))|(1&(0|1))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))&(1&(0|1))&(1&(0|1))&(1&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))&(1&(0|1))&(1&(0|1))&(1&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0&(1|0))|(1&(0|1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0&(1|0))|(1&(0|1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|((0&(1&0))|(0|1)))&(0&((0&(1|0))|(1&(0|1)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|((0&(1&0))|(0|1)))&(0&((0&(1|0))|(1&(0|1)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&((1&0)|(1|(0&1&0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&((1&0)|(1|(0&1&0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0&0)&(0|0))|(0|(1&1)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0&0)&(0|0))|(0|(1&1)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|1)&(0&0))|(1&0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|1)&(0&0))|(1&0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(0|1))&(1|0)&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(0|1))&(1|0)&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|0)&(0|0)&(1|1)|(0|0)&(0|0))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|0)&(0|0)&(1|1)|(0|0)&(0|0))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&(((1|0)|(0&1))&(1&1)))|((1|0)|(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&(((1|0)|(0&1))&(1&1)))|((1|0)|(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(0|1))|(0&(0|1))|(0&(0|1))|(0&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(0|1))|(0&(0|1))|(0&(0|1))|(0&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&0)|(0|1)&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&0)|(0|1)&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&1)|(1&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&1)|(1&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(1&1))|((0|0)|(0&0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(1&1))|((0|0)|(0&0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1|(0&0)&(1|0))|(0&(0|1)&(0|1))&(0&(0|1)&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1|(0&0)&(1|0))|(0&(0|1)&(0|1))&(0&(0|1)&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&0)|(0&1))&((1&(0|1))|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&0)|(0&1))&((1&(0|1))|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|((1&(0|1))|(0&(1|0))))&(1&((0&1)|(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|((1&(0|1))|(0&(1|0))))&(1&((0&1)|(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|0)&(0|0))&((0|0)|(0|0)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|0)&(0|0))&((0|0)|(0|0)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((1&((0&0)|(1|1)))|((1|(0|1))&(0&0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((1&((0&0)|(1|1)))|((1|(0|1))&(0&0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&((1|0)|(0|1)))|((1&(0|1))&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&((1|0)|(0|1)))|((1&(0|1))&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0&(1|0))|(1&0))&((1|0)&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0&(1|0))|(1&0))&((1|0)&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&(0|1))|(0&(1|0)))|((1&(0|1))&(0|1)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&(0|1))|(0&(1|0)))|((1&(0|1))&(0|1)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(0&0))|((1|1)&(1|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(0&0))|((1|1)&(1|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))|(0&(0|1)&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))|(0&(0|1)&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0|1)|(0|1))&(0&((1|0)|(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0|1)|(0|1))&(0&((1|0)|(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&(0|1))|(0&1))&(1&((0|1)|(0&(1|0)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&(0|1))|(0&1))&(1&((0|1)|(0&(1|0)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)&(0|1))|(0&(1|0))&(1&(0|1&0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)&(0|1))|(0&(1|0))&(1&(0|1&0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))|(1&0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))|(1&0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(((0|1)&(0|1))&((1|0)&(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(((0|1)&(0|1))&((1|0)&(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(0|1&(0|1&(1|0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(0|1&(0|1&(1|0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)|(0&1))&((1|0)|(0&1))&((1|0)|(0&1))&((1|0)|(0&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)|(0&1))&((1|0)|(0&1))&((1|0)|(0&1))&((1|0)|(0&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((((0|0)|(1&1))&((0|1)&(1|0)))|((0&1)|(1|0)))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((((0|0)|(1&1))&((0|1)&(1|0)))|((0&1)|(1|0)))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0&0)|(1&0))&(0&(1|0))&(0|1)&((1|0)|(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0&0)|(1&0))&(0&(1|0))&(0|1)&((1|0)|(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(1|0))&(0|1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(1|0))&(0|1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)|(0&1))&((1&0)|(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)|(0&1))&((1&0)|(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(((0|1)&(1|0))|(0&(1|0))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(((0|1)&(1|0))|(0&(1|0))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(((1|0)&(0|1))|(1&(0&1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(((1|0)&(0|1))|(1&(0&1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&0)|(1|0))&((1&1)|(0|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&0)|(1|0))&((1&1)|(0|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|1)|((0&1)&(1|0))&(1&(0|((1&1)|(0&0)))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|1)|((0&1)&(1|0))&(1&(0|((1&1)|(0&0)))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|(((0&0)&(0|0))|((1|1)|(1&1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|(((0&0)&(0|0))|((1|1)|(1&1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0&(((1|0)|(0|1))&(0|1))&(1|0))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0&(((1|0)|(0|1))&(0|1))&(1|0))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0|0)|(1&1))&(((1|0)&(0|1))|(1&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0|0)|(1&1))&(((1|0)&(0|1))|(1&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))|((0&1)|((1|0)&(0|1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))|((0&1)|((1|0)&(0|1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&1)&(0|0))|((0|0)|(1&1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&1)&(0|0))|((0|0)|(1&1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1|0)|(1|0))&((0&1)|(0&1))&((0&1)|(0&1))&((1|0)|(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1|0)|(1|0))&((0&1)|(0&1))&((0&1)|(0&1))&((1|0)|(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))&((0|1)|(1&0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))&((0|1)|(1&0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))&((0|1)&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))&((0|1)&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&((0|1)&(0|1))|(1&0)&(0&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&((0|1)&(0|1))|(1&0)&(0&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1|((0&(1|0))|((0|1)&(1&0))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1|((0&(1|0))|((0|1)&(1&0))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((1&(0|1))|((0|1)|(1&(0|1&0))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((1&(0|1))|((0|1)|(1&(0|1&0))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((1&(0&(1|0)))|((0&(1|0))|(0&1)))&((0&1)|(1&(0&1))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((1&(0&(1|0)))|((0&(1|0))|(0&1)))&((0&1)|(1&(0&1))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(1&(1|(0&0)&(1|0))|(0&(0|1)&(0|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(1&(1|(0&0)&(1|0))|(0&(0|1)&(0|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(0|((((1|0)&(0|1))|((1&0)|(0|1)))|((1&(0&0))|(0|1))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(0|((((1|0)&(0|1))|((1&0)|(0|1)))|((1&(0&0))|(0|1))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0&0)|(1|1))&((0|1)|(1|0))&((1&0)|(0|1))&((0&0)|(1|1)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0&0)|(1|1))&((0|1)|(1|0))&((1&0)|(0|1))&((0&0)|(1|1)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(0|1))|((1|0)&1))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(0|1))|((1|0)&1))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0|1)&(1|0))|(0&(1|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0|1)&(1|0))|(0&(1|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "(((0&1)|(1&0))|((1&1)&(0|0)))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "(((0&1)|(1&0))|((1&1)&(0|0)))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(expression = "((0&(1|0))|((0&1)|(1&1)))&(1|0)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "((0&(1|0))|((0&1)|(1&1)))&(1|0)") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(expression = "(1&(0|1&(0|1)))") == 1
    assert candidate(expression = "(0&1&1)|(0|1)") == 1
    assert candidate(expression = "(1&1)|(0&0)") == 1
    assert candidate(expression = "(1&((0&0)|(1|1)))") == 1
    assert candidate(expression = "1&(1&(1&(1&1)))") == 1
    assert candidate(expression = "((1|1)&(0|0))") == 1
    assert candidate(expression = "1&(0|1)") == 1
    assert candidate(expression = "((1&1)|(0&0))") == 1
    assert candidate(expression = "(1&1&1)|(1|1|1)") == 2
    assert candidate(expression = "1|1|0&1") == 1
    assert candidate(expression = "(0&0)|((1&1)|(0&1))") == 1
    assert candidate(expression = "(1&((1&1)&(1&1)))") == 1
    assert candidate(expression = "((1&0)|(1&1))") == 1
    assert candidate(expression = "(0&0&0)|(0|0|0)") == 1
    assert candidate(expression = "0|1&(1|0)&1") == 1
    assert candidate(expression = "1|1|(0&0)&1") == 1
    assert candidate(expression = "(((0|1)&1)|(0&0))") == 1
    assert candidate(expression = "(1&((0&1)|0))") == 1
    assert candidate(expression = "(0|(1|0&1))") == 1
    assert candidate(expression = "(0|((0|0)|(0|0)))") == 1
    assert candidate(expression = "(1&0)|(1&1)") == 1
    assert candidate(expression = "(0&0)&(0&0&0)") == 3
    assert candidate(expression = "(0|(0|(0|(0|0))))") == 1
    assert candidate(expression = "((1|0)&(0|1))") == 1
    assert candidate(expression = "(1|0|0)&(1&1)") == 1
    assert candidate(expression = "((1&0)|(1|0))") == 1
    assert candidate(expression = "(1&(1&(1&(1&1))))") == 1
    assert candidate(expression = "(1&1&1)|(0|0|0)") == 1
    assert candidate(expression = "(1|(0&(1|0)))") == 1
    assert candidate(expression = "(0&1)|((1|0)&(0|1))") == 1
    assert candidate(expression = "0|(0|(0|(0|0)))") == 1
    assert candidate(expression = "(1&(0|(1&0)))") == 1
    assert candidate(expression = "((1&(1|0))&(0|1))") == 1
    assert candidate(expression = "(0&(((0|1)&(1|0))|((1&0)|(0|1))))") == 1
    assert candidate(expression = "((0&(((1|0)|(0&1))&(1&1)))|((1|0)|(0|1)))&(1|0)") == 1
    assert candidate(expression = "((0&(1|0))&(0&(1|0))&(0&(1|0)))") == 2
    assert candidate(expression = "(0|((1&0)|(0|1)&((1|0)&(1|0))))") == 1
    assert candidate(expression = "((1&((1|0)|(0|1)))&((0&0)|(1&(1&(1&1)))))") == 1
    assert candidate(expression = "((0|1)&(1|(0|1&0))&(1|(0&(1|0))))") == 1
    assert candidate(expression = "((1&((0|1)&(0|1)))|((0&(1|0))&(1|0)))") == 1
    assert candidate(expression = "(((0|0)|(1|1))&((0|0)|(1|1))&((0|0)|(1|1))&((0|0)|(1|1)))") == 1
    assert candidate(expression = "(((1|0)|(0&1))&((0|1)|(0&1))&((1|0)|(0&1))&((0|1)|(0&1)))") == 1
    assert candidate(expression = "((0&0)&(0&0)&(1|1)&((0|0)|(1|1)))") == 1
    assert candidate(expression = "((1&0)|(0|1)&((1|0)&(1|0)))") == 1
    assert candidate(expression = "((1|0)&(1&0)|(0|1)&(1|0))") == 1
    assert candidate(expression = "((1|0)|(0&1)&(0|1))") == 1
    assert candidate(expression = "(1|(((1|0)&(0|1)))&(((0&1)|(1&1))&(1|0)))|(0|1)") == 2
    assert candidate(expression = "((0&(1|0)&(1|0))|(0&(0|1)&(0|1)))") == 1
    assert candidate(expression = "(((0|1)&(0|1))&((1&0)|(1&0))&((0|1)&(0|1))&((1&0)|(1&0)))") == 2
    assert candidate(expression = "(((1|1)|(0|0))&(1&(1&(1&1))))") == 1
    assert candidate(expression = "((1&0)|((0&1)|(1|((1&0)|(0|1)))))") == 1
    assert candidate(expression = "(((0&(1|0))&(1&((0&1)|(1|0))))|((1&0)|(0&((1&0)|(0&1)))))") == 1
    assert candidate(expression = "(((1|0)&(0|1))&((1|0)&(0|1)))|(1&(0|((1&1)|(0&0))))") == 2
    assert candidate(expression = "(((0|1)&(1|0))|((1&(0|1))|(0&1)))") == 2
    assert candidate(expression = "(0|((1&0)|(0|1)&((1|0)|(0|1)&(1|0))))") == 1
    assert candidate(expression = "(((0|1)|(1&0))&((0&1)|(1|0)))") == 1
    assert candidate(expression = "((1&0)|(1&0)|(0|1)&(0|1))") == 1
    assert candidate(expression = "(1|(((1|0)&(1|0))|((0&1)|(0&1))))") == 2
    assert candidate(expression = "(1&(0|((1&1)|(0|0))))") == 1
    assert candidate(expression = "(1&(((0|1)&(0|1))&((1|0)|(0|1)&(1|0))))") == 1
    assert candidate(expression = "((0&((0&1)|(1|0)))|((1&((0&1)|(1|0)))&(1&(0&(1|0)))))") == 1
    assert candidate(expression = "((1&0)|(0|1)&((1|0)|(0|1)&(1|0)))") == 1
    assert candidate(expression = "(1|(0&(1|0))|(0&1))") == 1
    assert candidate(expression = "(0|((1&1)|(0&0)))&(1&(0|((1&1)|(0&0))))") == 1
    assert candidate(expression = "(1|(((0&(1|0))|(1&0))&((1|0)&(0|1))))") == 1
    assert candidate(expression = "(((1|0)&(0|1))|((0&1)|(1|0))|((1|0)&(0|1))|((0&1)|(1|0)))") == 2
    assert candidate(expression = "(((1&0)|(0&1))&((0&(1|0))|(1&((0&1)|(1|0)))))") == 1
    assert candidate(expression = "(((1&0)|(0|1))&((1|0)|(0&1)))") == 1
    assert candidate(expression = "((1&0)|(1&1))&(1|0)") == 1
    assert candidate(expression = "(((1|1)|(0&0))&((1&1)|(0|0))|(1|0))") == 2
    assert candidate(expression = "((1|((0&0)|(1&1)))&(1|0))|((0|1)&(1&1))") == 2
    assert candidate(expression = "(((1|0)&1)|(0&(1|0)))") == 1
    assert candidate(expression = "((0&1)|(1&(0|1)))&((1&0)|(1|1))") == 1
    assert candidate(expression = "(1&((0|1)&(0|1))&(0|1))") == 1
    assert candidate(expression = "((0|1)|(1|0)&(0|1)&(0|1))&((0|1)|(0|1))") == 1
    assert candidate(expression = "(1&((0&1)|(0&(1|0))&(1|0)))") == 1
    assert candidate(expression = "(1|((1|0)&(0|1)))|(((0&1)|(1&1))&(1|0))") == 2
    assert candidate(expression = "((0&((1|0)&(0|1)))|((0&(1|0))&(1|0)))") == 1
    assert candidate(expression = "(((0|1)&(0|1))&((1|0)|(0|1)&(1|0)))") == 1
    assert candidate(expression = "(1&(((0&0)|(1|1))&(1&((0&0)|(1|1)))))|((1&(0|((1&1)|(0&0))))&(1|0))") == 2
    assert candidate(expression = "(((1&1)&(0|0))|(1|0)&((1&0)|(0|1))&(1|0))") == 1
    assert candidate(expression = "((1|(0&(1&0)))&(0|(1|0)))") == 1
    assert candidate(expression = "((1&(0|1))|(0&(1|0)))") == 1
    assert candidate(expression = "(((0|1)|(0&1))&(1|(0&0)&(1|0)))") == 1
    assert candidate(expression = "(1|((0|1)&(0&1))|(1&0))") == 1
    assert candidate(expression = "((1&0)|(1&(0|1))|(0&(1|0)))") == 1
    assert candidate(expression = "((0|(1&0))&(((1|0)&(0|1))|((0&1)|(1|0))))") == 1
    assert candidate(expression = "(1&(((0|1)|(1&0))&(0|1)))") == 1
    assert candidate(expression = "(((1&(0|1))&((1&0)|(0&1)))|((0&(1|0))&(1&((0&1)|(1|0)))))") == 1
    assert candidate(expression = "((0|1)|((1&(0|1))&(0|1)))") == 2
    assert candidate(expression = "((0&1)|(0&1)|(0&1)|(0&1))") == 1
    assert candidate(expression = "(0|(1&0)|(0|1)&(1|0))") == 1
    assert candidate(expression = "((1&(0|((1|0)&(1|0))))&((1&(0|((1|0)&(1|0))))&((1&(0|((1|0)&(1|0))))))") == 1
    assert candidate(expression = "(1|((0&0)|(1&(0|1))))") == 2
    assert candidate(expression = "(0|((1&((0|1)|(1|0)))&(1|0)))") == 1
    assert candidate(expression = "((0|((1&0)|(0|1)))&(((1|0)&(0|1))|((0&1)|(1|0))))") == 1
    assert candidate(expression = "(1&((0|0)|(1&0))&(0&(1|0))&(0|1))") == 1
    assert candidate(expression = "(((1|1)|(0|0))&(1&0))|(0|1)") == 1
    assert candidate(expression = "(1&(0|((0|0)&(0|0))))|((1|0)&(1&1))") == 1
    assert candidate(expression = "((1&(0|1))&(1|0))") == 1
    assert candidate(expression = "(1|((1|0)|(0|1))&(0&1))") == 1
    assert candidate(expression = "((1&1)|(0&(1|0)))") == 1
    assert candidate(expression = "(0|((1&0)|(0|1)&(1|0)))") == 1
    assert candidate(expression = "(1|((0&(1|0))&(1&(0|1&0))))") == 1
    assert candidate(expression = "((0&(1|1))|((1&0)|(0&1)))") == 1
    assert candidate(expression = "(1&(((1|0)|(0&1))&(1&1)))|((0|1)&(1&1))") == 2
    assert candidate(expression = "(((0|1)&(0|1))&((1|0)&(1|0)))") == 1
    assert candidate(expression = "(((0|1)&(1|0))&((1&0)|(0|1)))") == 1
    assert candidate(expression = "((1&((0&1)|(1|0)))&((1|0)|(0&(1|0))))|((1&(0|((1&1)|(0&0))))&(1|0))") == 2
    assert candidate(expression = "(((0&0)|(1&(0|1)))&((1|0)|(0&((0&1)|(1|0)))))") == 1
    assert candidate(expression = "(((0|1)&(1|0))|((1&0)|(0&1)))") == 1
    assert candidate(expression = "(1&((1|0)|(0|1))&(0&(1|0))&(0|1)&((0|0)&(1|1)))") == 2
    assert candidate(expression = "((1&(1&(1&0)))|((0|1)|(0&1)))") == 1
    assert candidate(expression = "((1|0)&(0|1)|(0&(1|0)))") == 1
    assert candidate(expression = "(0|((1|0)&(0|1))&(1|0))") == 1
    assert candidate(expression = "((1&(0|((1&0)|(0&1))))&((0&(1|0))|(1&(0|1))))") == 1
    assert candidate(expression = "((1&(0|1))&(1&(0|1))&(1&(0|1))&(1&(0|1)))") == 1
    assert candidate(expression = "(1|((0&(1|0))|(1&(0|1))))") == 2
    assert candidate(expression = "((1|((0&(1&0))|(0|1)))&(0&((0&(1|0))|(1&(0|1)))))") == 1
    assert candidate(expression = "(0&((1&0)|(1|(0&1&0))))") == 1
    assert candidate(expression = "(1|((0&0)&(0|0))|(0|(1&1)))") == 2
    assert candidate(expression = "(((1|1)&(0&0))|(1&0))") == 1
    assert candidate(expression = "(((0|1)&(0|1))&(1|0)&(1|0))") == 1
    assert candidate(expression = "((0|0)&(0|0)&(1|1)|(0|0)&(0|0))") == 2
    assert candidate(expression = "(0&(((1|0)|(0&1))&(1&1)))|((1|0)|(0|1))") == 1
    assert candidate(expression = "((0&(0|1))|(0&(0|1))|(0&(0|1))|(0&(0|1)))") == 1
    assert candidate(expression = "((1&0)|(0|1)&(1|0))") == 1
    assert candidate(expression = "((0&1)|(1&(1|0)))") == 1
    assert candidate(expression = "((1&(1&1))|((0|0)|(0&0)))") == 1
    assert candidate(expression = "((1|(0&0)&(1|0))|(0&(0|1)&(0|1))&(0&(0|1)&(0|1)))") == 1
    assert candidate(expression = "(((1&0)|(0&1))&((1&(0|1))|(0&1)))") == 1
    assert candidate(expression = "((0|((1&(0|1))|(0&(1|0))))&(1&((0&1)|(1|0))))") == 1
    assert candidate(expression = "(((0|0)&(0|0))&((0|0)|(0|0)))") == 2
    assert candidate(expression = "(1&((1&((0&0)|(1|1)))|((1|(0|1))&(0&0))))") == 1
    assert candidate(expression = "((0&((1|0)|(0|1)))|((1&(0|1))&(0|1)))") == 1
    assert candidate(expression = "(((0&(1|0))|(1&0))&((1|0)&(0|1)))") == 1
    assert candidate(expression = "(((1&(0|1))|(0&(1|0)))|((1&(0|1))&(0|1)))") == 2
    assert candidate(expression = "((0&(0&0))|((1|1)&(1|1)))") == 1
    assert candidate(expression = "((1&(0|1))|(0&(0|1)&(0|1)))") == 1
    assert candidate(expression = "(1&((0|1)|(0|1))&(0&((1|0)|(1|0))))") == 1
    assert candidate(expression = "(((1&(0|1))|(0&1))&(1&((0|1)|(0&(1|0)))))") == 1
    assert candidate(expression = "(((1|0)&(0|1))|(0&(1|0))&(1&(0|1&0)))") == 1
    assert candidate(expression = "((1&(0|1))|(1&0))") == 1
    assert candidate(expression = "(1&(((0|1)&(0|1))&((1|0)&(1|0))))") == 1
    assert candidate(expression = "(1&(0|1&(0|1&(1|0))))") == 1
    assert candidate(expression = "(((1|0)|(0&1))&((1|0)|(0&1))&((1|0)|(0&1))&((1|0)|(0&1)))") == 1
    assert candidate(expression = "((((0|0)|(1&1))&((0|1)&(1|0)))|((0&1)|(1|0)))") == 2
    assert candidate(expression = "(1|((0&0)|(1&0))&(0&(1|0))&(0|1)&((1|0)|(0|1)))") == 1
    assert candidate(expression = "(((0|1)&(1|0))&(0|1))") == 1
    assert candidate(expression = "(((1|0)|(0&1))&((1&0)|(0|1)))") == 1
    assert candidate(expression = "(1|(((0|1)&(1|0))|(0&(1|0))))") == 2
    assert candidate(expression = "(1|(((1|0)&(0|1))|(1&(0&1))))") == 2
    assert candidate(expression = "(((1&0)|(1|0))&((1&1)|(0|0)))") == 1
    assert candidate(expression = "((0|1)|((0&1)&(1|0))&(1&(0|((1&1)|(0&0)))))") == 1
    assert candidate(expression = "(1|(((0&0)&(0|0))|((1|1)|(1&1))))") == 2
    assert candidate(expression = "(0&(((1|0)|(0|1))&(0|1))&(1|0))") == 1
    assert candidate(expression = "((0|0)|(1&1))&(((1|0)&(0|1))|(1&1))") == 1
    assert candidate(expression = "((1&(0|1))|((0&1)|((1|0)&(0|1))))") == 2
    assert candidate(expression = "(((1&1)&(0|0))|((0|0)|(1&1)))") == 1
    assert candidate(expression = "(((1|0)|(1|0))&((0&1)|(0&1))&((0&1)|(0&1))&((1|0)|(1|0)))") == 1
    assert candidate(expression = "((1&(0|1))&((0|1)|(1&0)))") == 1
    assert candidate(expression = "((1&(0|1))&((0|1)&(1|0)))") == 1
    assert candidate(expression = "(1&((0|1)&(0|1))|(1&0)&(0&1))") == 1
    assert candidate(expression = "(1|((0&(1|0))|((0|1)&(1&0))))") == 1
    assert candidate(expression = "((1&(0|1))|((0|1)|(1&(0|1&0))))") == 2
    assert candidate(expression = "(((1&(0&(1|0)))|((0&(1|0))|(0&1)))&((0&1)|(1&(0&1))))") == 2
    assert candidate(expression = "(1&(1|(0&0)&(1|0))|(0&(0|1)&(0|1)))") == 1
    assert candidate(expression = "(0|((((1|0)&(0|1))|((1&0)|(0|1)))|((1&(0&0))|(0|1))))") == 1
    assert candidate(expression = "(((0&0)|(1|1))&((0|1)|(1|0))&((1&0)|(0|1))&((0&0)|(1|1)))") == 1
    assert candidate(expression = "((0&(0|1))|((1|0)&1))") == 1
    assert candidate(expression = "(((0|1)&(1|0))|(0&(1|0)))") == 1
    assert candidate(expression = "(((0&1)|(1&0))|((1&1)&(0|0)))") == 1
    assert candidate(expression = "((0&(1|0))|((0&1)|(1&1)))&(1|0)") == 1


