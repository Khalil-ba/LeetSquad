def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(password = "IloveLe3tcode!") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "IloveLe3tcode!") == True: {e}')
    
    total += 1
    try:
        result = candidate(password = "Me+You--IsMyDream") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Me+You--IsMyDream") == False: {e}')
    
    total += 1
    try:
        result = candidate(password = "1aB!") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "1aB!") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(password = "IloveLe3tcode!") == True
    assert candidate(password = "Me+You--IsMyDream") == False
    assert candidate(password = "1aB!") == False


