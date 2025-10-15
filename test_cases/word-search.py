def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(board = [['A', 'B'], ['C', 'D']],word = "BD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B'], ['C', 'D']],word = "BD") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B'], ['C', 'D']],word = "AC") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B'], ['C', 'D']],word = "AC") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASADB") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASADB") == False: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']],word = "ABCESEEEFS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']],word = "ABCESEEEFS") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "Z") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "Z") == False: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "AB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "AB") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "E") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "E") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B'], ['C', 'D']],word = "AB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B'], ['C', 'D']],word = "AB") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B'], ['C', 'D']],word = "CD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B'], ['C', 'D']],word = "CD") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASAD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASAD") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A']],word = "A") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A']],word = "A") == True: {e}')
    
    total += 1
    try:
        result = candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "BD") == True
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "AC") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASADB") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']],word = "ABCESEEEFS") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "Z") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "AB") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "E") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "AB") == True
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "CD") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASAD") == True
    assert candidate(board = [['A']],word = "A") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True


