def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 433494437) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 433494437) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 377) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 377) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 6765) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6765) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 24157817) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 24157817) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 102334155) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 102334155) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 89) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 121393) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 121393) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 500) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 514229) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 514229) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 39088169) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 39088169) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 21) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 21) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 2584) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2584) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 2178309) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2178309) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 46368) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 46368) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 233) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 233) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 63245986) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 63245986) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 13) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 13) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 144) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 144) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 701408733) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 701408733) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 55) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 55) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 5702887) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5702887) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 196418) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 196418) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 28657) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 28657) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 14930352) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 14930352) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 4181) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4181) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 3524578) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3524578) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 17711) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 17711) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 34) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 34) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 10946) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10946) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 165580141) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 165580141) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 610) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 610) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 317811) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 317811) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1346269) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1346269) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 9227465) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9227465) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 832040) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 832040) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1597) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1597) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 75025) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75025) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 267914296) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 267914296) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 987) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 35) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 35) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456789) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456789) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 1234567) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1234567) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 863999999) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 863999999) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 12586269025) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12586269025) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1134903170) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1134903170) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 555555555) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 555555555) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 2123366401) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2123366401) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 340513) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 340513) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 1836311903) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1836311903) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 104941883) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 104941883) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 470001109) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 470001109) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 55555555) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 55555555) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 2971215073) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2971215073) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 123456) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123456) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 433494437) == 1
    assert candidate(k = 377) == 1
    assert candidate(k = 6765) == 1
    assert candidate(k = 24157817) == 1
    assert candidate(k = 102334155) == 1
    assert candidate(k = 89) == 1
    assert candidate(k = 121393) == 1
    assert candidate(k = 500) == 3
    assert candidate(k = 514229) == 1
    assert candidate(k = 50) == 3
    assert candidate(k = 39088169) == 1
    assert candidate(k = 21) == 1
    assert candidate(k = 2584) == 1
    assert candidate(k = 2178309) == 1
    assert candidate(k = 100) == 3
    assert candidate(k = 46368) == 1
    assert candidate(k = 233) == 1
    assert candidate(k = 63245986) == 1
    assert candidate(k = 1000000000) == 14
    assert candidate(k = 7) == 2
    assert candidate(k = 13) == 1
    assert candidate(k = 144) == 1
    assert candidate(k = 701408733) == 1
    assert candidate(k = 55) == 1
    assert candidate(k = 5702887) == 1
    assert candidate(k = 196418) == 1
    assert candidate(k = 2) == 1
    assert candidate(k = 28657) == 1
    assert candidate(k = 14930352) == 1
    assert candidate(k = 4) == 2
    assert candidate(k = 4181) == 1
    assert candidate(k = 3524578) == 1
    assert candidate(k = 17711) == 1
    assert candidate(k = 34) == 1
    assert candidate(k = 10946) == 1
    assert candidate(k = 1) == 1
    assert candidate(k = 19) == 3
    assert candidate(k = 165580141) == 1
    assert candidate(k = 3) == 1
    assert candidate(k = 610) == 1
    assert candidate(k = 8) == 1
    assert candidate(k = 317811) == 1
    assert candidate(k = 1346269) == 1
    assert candidate(k = 10) == 2
    assert candidate(k = 9227465) == 1
    assert candidate(k = 832040) == 1
    assert candidate(k = 1597) == 1
    assert candidate(k = 1000000) == 5
    assert candidate(k = 75025) == 1
    assert candidate(k = 1000) == 2
    assert candidate(k = 267914296) == 1
    assert candidate(k = 5) == 1
    assert candidate(k = 987) == 1
    assert candidate(k = 35) == 2
    assert candidate(k = 123456789) == 12
    assert candidate(k = 1234567) == 10
    assert candidate(k = 863999999) == 13
    assert candidate(k = 12586269025) == 1
    assert candidate(k = 1134903170) == 1
    assert candidate(k = 555555555) == 11
    assert candidate(k = 2123366401) == 14
    assert candidate(k = 340513) == 7
    assert candidate(k = 1836311903) == 1
    assert candidate(k = 104941883) == 11
    assert candidate(k = 999999999) == 13
    assert candidate(k = 470001109) == 13
    assert candidate(k = 55555555) == 11
    assert candidate(k = 2971215073) == 1
    assert candidate(k = 123456) == 4
    assert candidate(k = 987654321) == 15


