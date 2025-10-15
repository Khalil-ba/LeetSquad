def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(hamsters = "H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H") == 3: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H") == 5: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".....") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".....") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H..H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H..H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H....H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H....H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H") == 3: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HHHH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HHHH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H") == 4: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".HHH.") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".HHH.") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 8: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".H.H.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".H.H.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H") == 4: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H") == 7: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HHHHHH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HHHHHH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H") == 5: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 10: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "......") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "......") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H") == 6: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "...") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "...") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 9: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.HH.H.H") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.HH.H.H") == 4: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.....H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.....H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H") == 4: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.....H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.....H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".......") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".......") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HHHHH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HHHHH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".H.H.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".H.H.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "........") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "........") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H") == 5: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "..H.H..") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "..H.H..") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H") == 3: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.HH.H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.HH.H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HH.HH.HH.HH.HH.HH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HH.HH.HH.HH.HH.HH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "...") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "...") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H..H.H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H..H.H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.......H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.......H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "..H..H..") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "..H..H..") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HHHHH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HHHHH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.H.H.H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.H.H.H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H...H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H...H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HHH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HHH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "........") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "........") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.HH.H") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.HH.H") == 3: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HH.HH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HH.HH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HHHHHHHHHH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HHHHHHHHHH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".HHH.") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".HHH.") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".H") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".H") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".H.H.H.H.") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".H.H.H.H.") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".........") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".........") == 0: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".H.H.H.H.H.H.H.H.H.") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".H.H.H.H.H.H.H.H.H.") == 5: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = ".H.H.H.H.H.H.H.H.") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = ".H.H.H.H.H.H.H.H.") == 4: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HHHHHHH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HHHHHHH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH...HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH...HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H") == 6: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H......H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H......H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H.H") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H.H") == 1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH.HH.HH.HH.HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH.HH.HH.HH.HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "H..H") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "H..H") == 2: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HH..HH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HH..HH") == -1: {e}')
    
    total += 1
    try:
        result = candidate(hamsters = "HHHH") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hamsters = "HHHH") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(hamsters = "H") == -1
    assert candidate(hamsters = "H.H.H.H.H.H") == 3
    assert candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H") == 5
    assert candidate(hamsters = ".....") == 0
    assert candidate(hamsters = ".") == 0
    assert candidate(hamsters = "H..H") == 2
    assert candidate(hamsters = "H.H") == 1
    assert candidate(hamsters = "H....H") == 2
    assert candidate(hamsters = "H.H.H.H.H") == 3
    assert candidate(hamsters = "HHHH") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H") == 4
    assert candidate(hamsters = "HH") == -1
    assert candidate(hamsters = "H.H.HH") == -1
    assert candidate(hamsters = ".HHH.") == -1
    assert candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
    assert candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 8
    assert candidate(hamsters = "HH.HH.HH") == -1
    assert candidate(hamsters = "H.H.H") == 2
    assert candidate(hamsters = "HH.H.H.H.H") == -1
    assert candidate(hamsters = "H.H.H.H") == 2
    assert candidate(hamsters = "HH.HH") == -1
    assert candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H") == -1
    assert candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H") == -1
    assert candidate(hamsters = ".H.H.") == 1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H") == 4
    assert candidate(hamsters = "H.HH") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H") == 7
    assert candidate(hamsters = "HHHHHH") == -1
    assert candidate(hamsters = "HH.H.H") == -1
    assert candidate(hamsters = "HH.H") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H") == 5
    assert candidate(hamsters = "HH.H.H.H.H.H.H") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 10
    assert candidate(hamsters = "HH.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == -1
    assert candidate(hamsters = "HH.H.HH") == -1
    assert candidate(hamsters = "......") == 0
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H") == 6
    assert candidate(hamsters = "...") == 0
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H.H") == 9
    assert candidate(hamsters = "H.H.HH.H.H") == 4
    assert candidate(hamsters = "H.....H") == 2
    assert candidate(hamsters = "H.H.H.H.H.H.H") == 4
    assert candidate(hamsters = "H.....H") == 2
    assert candidate(hamsters = ".......") == 0
    assert candidate(hamsters = "HH.HHHHH.HH") == -1
    assert candidate(hamsters = ".H.H.") == 1
    assert candidate(hamsters = "H.H.H.H.HH") == -1
    assert candidate(hamsters = "........") == 0
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H") == 5
    assert candidate(hamsters = "..H.H..") == 1
    assert candidate(hamsters = "H.H.H.H.H") == 3
    assert candidate(hamsters = "HH.H.H.HH") == -1
    assert candidate(hamsters = "HH") == -1
    assert candidate(hamsters = "H.HH.H") == 2
    assert candidate(hamsters = "HH.HH.HH.HH.HH.HH.HH.HH") == -1
    assert candidate(hamsters = "...") == 0
    assert candidate(hamsters = "H.") == 1
    assert candidate(hamsters = "H.H..H.H") == 2
    assert candidate(hamsters = "H.......H") == 2
    assert candidate(hamsters = "..H..H..") == 2
    assert candidate(hamsters = "HHHHH") == -1
    assert candidate(hamsters = "HH.HH") == -1
    assert candidate(hamsters = "HH.H.H.H.HH") == -1
    assert candidate(hamsters = "H...H") == 2
    assert candidate(hamsters = "HH.HHH.HH") == -1
    assert candidate(hamsters = "........") == 0
    assert candidate(hamsters = "H.H.H.HH.H") == 3
    assert candidate(hamsters = "HH.HH.HH.HH") == -1
    assert candidate(hamsters = "H.H.H.H") == 2
    assert candidate(hamsters = ".") == 0
    assert candidate(hamsters = "HHHHHHHHHH") == -1
    assert candidate(hamsters = ".HHH.") == -1
    assert candidate(hamsters = "H.H.H.HH") == -1
    assert candidate(hamsters = ".H") == 1
    assert candidate(hamsters = ".H.H.H.H.") == 2
    assert candidate(hamsters = "H.H.H") == 2
    assert candidate(hamsters = "H") == -1
    assert candidate(hamsters = ".........") == 0
    assert candidate(hamsters = ".H.H.H.H.H.H.H.H.H.") == 5
    assert candidate(hamsters = ".H.H.H.H.H.H.H.H.") == 4
    assert candidate(hamsters = "HHHHHHH") == -1
    assert candidate(hamsters = "HH...HH") == -1
    assert candidate(hamsters = "H.H.H.H.H.H.H.H.H.H.H.H") == 6
    assert candidate(hamsters = "H......H") == 2
    assert candidate(hamsters = "H.H") == 1
    assert candidate(hamsters = "HH.HH.HH.HH.HH") == -1
    assert candidate(hamsters = "H..H") == 2
    assert candidate(hamsters = "HH..HH") == -1
    assert candidate(hamsters = "HHHH") == -1


