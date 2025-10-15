def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'O O', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'O O', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', 'X  ', 'X  ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', 'X  ', 'X  ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'O O', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'O O', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', '   ', 'O O']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', '   ', 'O O']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', '    ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', '    ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'XOX', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'XOX', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OXX', 'XOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OXX', 'XOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXO', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXO', '   ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'XOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'XOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' X ', '  X']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' X ', '  X']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', 'XO ', ' X ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', 'XO ', ' X ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', '   ', 'OOO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', '   ', 'OOO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'O O', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'O O', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OOO', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OOO', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XO ', 'OX ', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XO ', 'OX ', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XX ', 'OO ', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XX ', 'OO ', '   ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOO', 'XOX', 'OOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOO', 'XOX', 'OOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XX ', 'OOX', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XX ', 'OOX', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'XOX', 'OOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'XOX', 'OOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', 'XOX', 'XXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', 'XOX', 'XXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'O O', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'O O', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', ' X ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', ' X ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OOX', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OOX', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', 'OOO', 'OOO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', 'OOO', 'OOO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OXO', 'XOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OXO', 'XOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOO', 'XOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOO', 'XOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', 'XOX', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', 'XOX', '   ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', '  O']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', '  O']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOO', 'OXO', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOO', 'OXO', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'XOX', 'OOO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'XOX', 'OOO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OXO', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OXO', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOO', 'XOX', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOO', 'XOX', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', 'OOO', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', 'OOO', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', 'OOO', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', 'OOO', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXO', 'XO ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXO', 'XO ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', 'X X', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', 'X X', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', 'XXX', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', 'XXX', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['O  ', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['O  ', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' X ', '  X']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' X ', '  X']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOO', 'XOO', 'XOO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOO', 'XOO', 'XOO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', '  X']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', '  X']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['O  ', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['O  ', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OXX', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OXX', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OXO', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OXO', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', 'OOO', 'XXX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', 'OOO', 'XXX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', '   ', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', '   ', '   ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', ' X ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', ' X ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OOX', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OOX', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', '  O']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', '  O']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', ' X ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', ' X ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', 'OOO', 'X  ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', 'OOO', 'X  ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXX', 'OXO']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXX', 'OXO']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', 'X  ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', 'X  ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOO', 'XOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOO', 'XOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X O', 'X O', 'X O']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X O', 'X O', 'X O']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'XOX', 'OOO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'XOX', 'OOO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'XOX', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'XOX', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXO', 'OOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXO', 'OOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['O  ', 'O  ', 'O  ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['O  ', 'O  ', 'O  ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXO', 'OXO', 'OOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXO', 'OXO', 'OOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', '   ', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', '   ', '   ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XX ', 'OOX', 'X  ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XX ', 'OOX', 'X  ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', '   ', 'XXX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', '   ', 'XXX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', ' O ', '  X']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', ' O ', '  X']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', '   ', 'XXX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', '   ', 'XXX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['O  ', ' O ', '  O']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['O  ', ' O ', '  O']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XO ', 'OX ', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XO ', 'OX ', '   ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'OXO', 'XOX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'OXO', 'XOX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XO ', 'OXO', 'OXO']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XO ', 'OXO', 'OXO']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', '   ', '  O']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', '   ', '  O']) == True: {e}')
    
    total += 1
    try:
        result = candidate(board = ['O  ', '   ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['O  ', '   ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', ' X ', '   ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', ' X ', '   ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XXX', 'XXX', 'XXX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XXX', 'XXX', 'XXX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['X  ', 'X  ', 'X  ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['X  ', 'X  ', 'X  ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['OOO', '   ', 'XXX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['OOO', '   ', 'XXX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['O  ', ' O ', '  O']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['O  ', ' O ', '  O']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['XOX', 'XOX', 'XOX']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['XOX', 'XOX', 'XOX']) == False: {e}')
    
    total += 1
    try:
        result = candidate(board = ['   ', '   ', '   ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['   ', '   ', '   ']) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(board = ['XOX', 'O O', 'XOX']) == True
    assert candidate(board = ['X  ', 'X  ', 'X  ']) == False
    assert candidate(board = ['XOX', 'O O', 'XOX']) == True
    assert candidate(board = ['XXX', '   ', 'O O']) == True
    assert candidate(board = ['X  ', ' O ', '    ']) == True
    assert candidate(board = ['XOX', 'XOX', 'XOX']) == False
    assert candidate(board = ['OXX', 'XOX', 'OXO']) == False
    assert candidate(board = ['OOO', '   ', '   ']) == False
    assert candidate(board = ['XOX', 'OXO', '   ']) == True
    assert candidate(board = ['XOX', 'OXO', 'XOX']) == True
    assert candidate(board = ['XXO', 'OXO', 'XOX']) == True
    assert candidate(board = ['XXO', 'XOX', 'OXO']) == False
    assert candidate(board = ['XXX', '   ', '   ']) == False
    assert candidate(board = ['X  ', ' X ', '  X']) == False
    assert candidate(board = ['XXO', 'OOX', 'OXO']) == False
    assert candidate(board = ['X  ', 'XO ', ' X ']) == False
    assert candidate(board = ['XXX', '   ', 'OOO']) == False
    assert candidate(board = ['XOX', 'O O', 'XOX']) == True
    assert candidate(board = ['XOX', 'OOO', 'XOX']) == False
    assert candidate(board = ['XO ', 'OX ', 'OXO']) == False
    assert candidate(board = ['X  ', ' O ', 'XOX']) == True
    assert candidate(board = ['XX ', 'OO ', '   ']) == True
    assert candidate(board = ['XOO', 'XOX', 'OOX']) == False
    assert candidate(board = ['XX ', 'OOX', 'XOX']) == False
    assert candidate(board = ['XXO', 'XOX', 'OOX']) == False
    assert candidate(board = ['OOO', 'XOX', 'XXO']) == False
    assert candidate(board = ['XOX', 'O O', '   ']) == False
    assert candidate(board = ['XOX', ' X ', '   ']) == False
    assert candidate(board = ['XOX', 'OOX', 'XOX']) == False
    assert candidate(board = ['OOO', 'OOO', 'OOO']) == False
    assert candidate(board = ['OXO', 'XOX', 'OXO']) == False
    assert candidate(board = ['XOO', 'XOX', 'OXO']) == False
    assert candidate(board = ['   ', 'XOX', '   ']) == True
    assert candidate(board = ['X  ', ' O ', '  O']) == False
    assert candidate(board = ['XOO', 'OXO', 'XOX']) == False
    assert candidate(board = ['XOX', 'XOX', 'OOO']) == False
    assert candidate(board = ['XXO', 'OXO', 'OXO']) == False
    assert candidate(board = ['XOO', 'XOX', 'XOX']) == False
    assert candidate(board = ['XXX', 'OOO', '   ']) == False
    assert candidate(board = ['XXX', 'OOO', '   ']) == False
    assert candidate(board = ['XOX', 'OXO', 'XO ']) == False
    assert candidate(board = ['OOO', 'X X', 'XOX']) == True
    assert candidate(board = ['XOX', 'OXO', 'XOX']) == True
    assert candidate(board = ['   ', 'XXX', '   ']) == False
    assert candidate(board = ['O  ', '   ', '   ']) == False
    assert candidate(board = ['XXO', 'OXO', 'XOX']) == True
    assert candidate(board = ['OOO', '   ', '   ']) == False
    assert candidate(board = ['X  ', ' X ', '  X']) == False
    assert candidate(board = ['XOO', 'XOO', 'XOO']) == False
    assert candidate(board = ['X  ', ' O ', '  X']) == True
    assert candidate(board = ['O  ', '   ', '   ']) == False
    assert candidate(board = ['XXX', '   ', '   ']) == False
    assert candidate(board = ['OXX', 'OXO', 'XOX']) == True
    assert candidate(board = ['XXO', 'OXO', 'OXO']) == False
    assert candidate(board = ['XXX', 'OOO', 'XXX']) == False
    assert candidate(board = ['   ', '   ', '   ']) == True
    assert candidate(board = ['XOX', ' X ', '   ']) == False
    assert candidate(board = ['XXO', 'OOX', 'XOX']) == True
    assert candidate(board = ['XXO', 'OXO', 'XOX']) == True
    assert candidate(board = ['X  ', ' O ', '  O']) == False
    assert candidate(board = ['X  ', ' O ', ' X ']) == True
    assert candidate(board = ['X  ', 'OOO', 'X  ']) == False
    assert candidate(board = ['XOX', 'OXX', 'OXO']) == True
    assert candidate(board = ['X  ', ' O ', 'X  ']) == True
    assert candidate(board = ['XOO', 'XOX', 'OXO']) == False
    assert candidate(board = ['X O', 'X O', 'X O']) == False
    assert candidate(board = ['XXX', '   ', '   ']) == False
    assert candidate(board = ['XXO', 'XOX', 'OOO']) == False
    assert candidate(board = ['XXO', 'XOX', 'OXO']) == False
    assert candidate(board = ['XOX', 'OXO', 'OOX']) == False
    assert candidate(board = ['O  ', 'O  ', 'O  ']) == False
    assert candidate(board = ['XXO', 'OXO', 'OOX']) == False
    assert candidate(board = ['   ', '   ', '   ']) == True
    assert candidate(board = ['XX ', 'OOX', 'X  ']) == False
    assert candidate(board = ['   ', '   ', 'XXX']) == False
    assert candidate(board = ['OOO', '   ', '   ']) == False
    assert candidate(board = ['X  ', ' O ', '  X']) == True
    assert candidate(board = ['   ', '   ', 'XXX']) == False
    assert candidate(board = ['O  ', ' O ', '  O']) == False
    assert candidate(board = ['XO ', 'OX ', '   ']) == True
    assert candidate(board = ['XOX', 'OXO', 'XOX']) == True
    assert candidate(board = ['XO ', 'OXO', 'OXO']) == False
    assert candidate(board = ['X  ', '   ', '  O']) == True
    assert candidate(board = ['O  ', '   ', '   ']) == False
    assert candidate(board = ['XOX', ' X ', '   ']) == False
    assert candidate(board = ['XXX', 'XXX', 'XXX']) == False
    assert candidate(board = ['X  ', 'X  ', 'X  ']) == False
    assert candidate(board = ['OOO', '   ', 'XXX']) == False
    assert candidate(board = ['O  ', ' O ', '  O']) == False
    assert candidate(board = ['XOX', 'XOX', 'XOX']) == False
    assert candidate(board = ['   ', '   ', '   ']) == True


