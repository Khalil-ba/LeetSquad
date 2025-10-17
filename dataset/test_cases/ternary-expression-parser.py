def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(expression = "T?T?F:5:3") == "F"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?F:5:3") == "F": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?F?T?F?T?F?T?F?1:2:3:4:5:6:7:8:9") == "8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?F?T?F?T?F?T?F?1:2:3:4:5:6:7:8:9") == "8": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F:2:3?4:5") == "5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F:2:3?4:5") == "5": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?T?2:3:F?1:0") == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?T?2:3:F?1:0") == "0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?T?T?T?T?9:8:7:6:5:4") == "9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?T?T?T?9:8:7:6:5:4") == "9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F:5:T") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F:5:T") == "T": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?4:5?6:7") == "4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?4:5?6:7") == "4": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F?F?F?0:1:2:3:4:5") == "5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F?F?F?0:1:2:3:4:5") == "5": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?9:T?8:T?7:6") == "8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?9:T?8:T?7:6") == "8": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?T?T?T?T?T?T?T?T?T:T:T:T:T:T:T:T:T:T:T") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?T?T?T?T?T?T?T?T:T:T:T:T:T:T:T:T:T:T") == "T": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?T?T?T?T?1:2:3:4:5:6") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?T?T?T?1:2:3:4:5:6") == "1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F?F?F?F?F?F?F?9:8:7:6:5:4:3:2:1:0") == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F?F?F?F?F?F?F?9:8:7:6:5:4:3:2:1:0") == "0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?5:9:T?F:9") == "F"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?5:9:T?F:9") == "F": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?1:2?3:4") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?1:2?3:4") == "1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?T?T?T?T?T?T?T?1:2:3:4:5:6:7:8:9") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?T?T?T?T?T?T?1:2:3:4:5:6:7:8:9") == "1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?T?F?T?F?T?F?T?9:8:7:6:5:4:3:2:1") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?T?F?T?F?T?F?T?9:8:7:6:5:4:3:2:1") == "1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F?F?F?F?F?F?9:8:7:6:5:4:3:2:1") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F?F?F?F?F?F?9:8:7:6:5:4:3:2:1") == "1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?T?T?T?T?T?T?T?T?1:0:0:0:0:0:0:0:0:0") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?T?T?T?T?T?T?T?1:0:0:0:0:0:0:0:0:0") == "1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?F?T?9:8:7:6?5:4") == "7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?F?T?9:8:7:6?5:4") == "7": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F?F?F?9:8:7:6:5:4") == "4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F?F?F?9:8:7:6:5:4") == "4": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?2:3") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?2:3") == "2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?F?F?F:1:2:3?4:5?6:7") == "7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?F?F?F:1:2:3?4:5?6:7") == "7": {e}')
    
    total += 1
    try:
        result = candidate(expression = "F?1:T?4:5") == "4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "F?1:T?4:5") == "4": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?T?T?T?T?T?T?T?T?0:1:2:3:4:5:6:7:8:9") == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?T?T?T?T?T?T?T?T?0:1:2:3:4:5:6:7:8:9") == "0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "T?F?F?1:2:T?3:4:F?5:6") == "3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "T?F?F?1:2:T?3:4:F?5:6") == "3": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(expression = "T?T?F:5:3") == "F"
    assert candidate(expression = "T?F?T?F?T?F?T?F?1:2:3:4:5:6:7:8:9") == "8"
    assert candidate(expression = "F?F?F:2:3?4:5") == "5"
    assert candidate(expression = "F?T?2:3:F?1:0") == "0"
    assert candidate(expression = "T?T?T?T?T?9:8:7:6:5:4") == "9"
    assert candidate(expression = "F?F?F:5:T") == "T"
    assert candidate(expression = "T?4:5?6:7") == "4"
    assert candidate(expression = "F?F?F?F?F?0:1:2:3:4:5") == "5"
    assert candidate(expression = "F?9:T?8:T?7:6") == "8"
    assert candidate(expression = "T?T?T?T?T?T?T?T?T?T:T:T:T:T:T:T:T:T:T:T") == "T"
    assert candidate(expression = "T?T?T?T?T?1:2:3:4:5:6") == "1"
    assert candidate(expression = "F?F?F?F?F?F?F?F?F?9:8:7:6:5:4:3:2:1:0") == "0"
    assert candidate(expression = "F?F?5:9:T?F:9") == "F"
    assert candidate(expression = "T?1:2?3:4") == "1"
    assert candidate(expression = "T?T?T?T?T?T?T?T?1:2:3:4:5:6:7:8:9") == "1"
    assert candidate(expression = "F?T?F?T?F?T?F?T?9:8:7:6:5:4:3:2:1") == "1"
    assert candidate(expression = "F?F?F?F?F?F?F?F?9:8:7:6:5:4:3:2:1") == "1"
    assert candidate(expression = "T?T?T?T?T?T?T?T?T?1:0:0:0:0:0:0:0:0:0") == "1"
    assert candidate(expression = "T?F?T?9:8:7:6?5:4") == "7"
    assert candidate(expression = "F?F?F?F?F?9:8:7:6:5:4") == "4"
    assert candidate(expression = "T?2:3") == "2"
    assert candidate(expression = "F?F?F?F:1:2:3?4:5?6:7") == "7"
    assert candidate(expression = "F?1:T?4:5") == "4"
    assert candidate(expression = "T?T?T?T?T?T?T?T?T?0:1:2:3:4:5:6:7:8:9") == "0"
    assert candidate(expression = "T?F?F?1:2:T?3:4:F?5:6") == "3"


