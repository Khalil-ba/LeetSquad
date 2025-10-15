def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4])) == "dba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4])) == "dba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 1, None, 1, 0, None, 0])) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 1, None, 1, 0, None, 0])) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2])) == "adz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2])) == "adz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == "onmlkjihgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == "onmlkjihgfedcb": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "anuxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "anuxz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])) == "aaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])) == "aaaaab": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])) == "abaca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])) == "abaca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 11, 14, 10, 13, 13, 15, 9, 12, 12, 14, 14, 16, 8, 11, 11, 13, 13, 15, 15, 17, 7, 10, 10, 12, 12, 14, 14, 16, 16, 18])) == "honlm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 11, 14, 10, 13, 13, 15, 9, 12, 12, 14, 14, 16, 8, 11, 11, 13, 13, 15, 15, 17, 7, 10, 10, 12, 12, 14, 14, 16, 16, 18])) == "honlm": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 5, 1, 3, None, 6, 0, None, None, 7, None, None, 8, None, None, 9])) == "gfe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 5, 1, 3, None, 6, 0, None, None, 7, None, None, 8, None, None, 9])) == "gfe": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == "fdba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == "fdba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == "fffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == "fffff": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, None])) == "bce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, None])) == "bce": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 11, 13, 10, None, 14, None, 9, None, 15, None, 8, None, 16, None, 7, None, 17, None, 6, None, 18, None, 5, None, 19, None, 4, None, 20, None, 3, None, 21, None, 2, None, 22, None, 1, None, 23, None, 0, None, 24, None, 25])) == "yxwvutsrqponm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 11, 13, 10, None, 14, None, 9, None, 15, None, 8, None, 16, None, 7, None, 17, None, 6, None, 18, None, 5, None, 19, None, 4, None, 20, None, 3, None, 21, None, 2, None, 22, None, 1, None, 23, None, 0, None, 24, None, 25])) == "yxwvutsrqponm": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 11, 13, 10, 14, 9, 15, 8, 16, 7, 17, 6, 18, 5, 19, 4, 20, 3, 21, 2, 22, 1, 23, 0, 24, 25])) == "agjnm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 11, 13, 10, 14, 9, 15, 8, 16, 7, 17, 6, 18, 5, 19, 4, 20, 3, 21, 2, 22, 1, 23, 0, 24, 25])) == "agjnm": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == "beif"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == "beif": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])) == "ahbbz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])) == "ahbbz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None])) == "aaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None])) == "aaaaab": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "ngdb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "ngdb": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == "aaaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == "aaaba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "ca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "ca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "awsheba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "awsheba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "lcdz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "lcdz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, 0, None, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "mykdca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, 0, None, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "mykdca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "hdba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "hdba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 5, 6, None, None, 8, 9, None, None, 10, 11, None, None, None, None, None, None, 12, 13, None, None, None, None, None, 14, 15])) == "fhud"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 5, 6, None, None, 8, 9, None, None, 10, 11, None, None, None, None, None, None, 12, 13, None, None, None, None, None, 14, 15])) == "fhud": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == "ltxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == "ltxz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ftbgjk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ftbgjk": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, None, 0, 0, 0, 0, None])) == "aaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, None, 0, 0, 0, 0, None])) == "aaab": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 2, 5, 12, 18, None, 4, 6, None, 10, 14, 16, 19, None, None, None, None, None, 8, None, None, None, None, None, 9, 11, 13, None, None, 17])) == "ecdh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 2, 5, 12, 18, None, 4, 6, None, 10, 14, 16, 19, None, None, None, None, None, 8, None, None, None, None, None, 9, 11, 13, None, None, 17])) == "ecdh": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "iecb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "iecb": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([13, 7, 18, 3, 9, None, 20, 1, None, 5, 10, None, None, None, None, 2, 6, 8, 11, None, None, 12, None, 14, None, 15])) == "bdhn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([13, 7, 18, 3, 9, None, 20, 1, None, 5, 10, None, None, None, None, 2, 6, 8, 11, None, None, 12, None, 14, None, 15])) == "bdhn": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0])) == "atkon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0])) == "atkon": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == "angca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == "angca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 15, 10, 2, 20, 7, 13, None, 8, None, None, 2, 12, None, None, None, None, 4, 6, 5, 11, None, None, None, None, None, None, None, None, 3, None, None, None, None, None])) == "echkh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 15, 10, 2, 20, 7, 13, None, 8, None, None, 2, 12, None, None, None, None, 4, 6, 5, 11, None, None, None, None, None, None, None, None, 3, None, None, None, None, None])) == "echkh": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == "dfk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == "dfk": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "azmfca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "azmfca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "alrhcpud"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "alrhcpud": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, 8, 12, 7, 13, 6, 14, 5, 15, 4, 16, 3, 17, 2, 18, 1, 19, 0, 20, 25, 21, 24, 22, 23])) == "afmjk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, 8, 12, 7, 13, 6, 14, 5, 15, 4, 16, 3, 17, 2, 18, 1, 19, 0, 20, 25, 21, 24, 22, 23])) == "afmjk": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])) == "mmmm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])) == "mmmm": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, None, None, None, None, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, None, None, None, None, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 2, 1, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == "igeba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 2, 1, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == "igeba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4])) == "dddba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4])) == "dddba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "meca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "meca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aangdb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aangdb": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])) == "anuxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])) == "anuxz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaacd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaacd": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == "ba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "anuxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "anuxz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2])) == "adcdz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2])) == "adcdz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 10, 8, 9, 9, 10, 7, 8, 8, 9, 9, 10, 6, 7, 7, 8, 8, 9, 9, 10, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10])) == "aegjjjk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 10, 8, 9, 9, 10, 7, 8, 8, 9, 9, 10, 6, 7, 7, 8, 8, 9, 9, 10, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10])) == "aegjjjk": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, 8, 10, 10, 12, 7, 9, 9, 11, 11, 13, 6, 8, 8, 10, 10, 12, 12, 14, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18])) == "cngmlk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, 8, 10, 10, 12, 7, 9, 9, 11, 11, 13, 6, 8, 8, 10, 10, 12, 12, 14, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18])) == "cngmlk": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == "dddddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == "dddddd": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 14, 16, 13, 15, 15, 17, 12, 14, 14, 16, 16, 18, 11, 13, 13, 15, 15, 17, 17, 19, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23])) == "hslrqp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 14, 16, 13, 15, 15, 17, 12, 14, 14, 16, 16, 18, 11, 13, 13, 15, 15, 17, 17, 19, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23])) == "hslrqp": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 6, 8, 5, 7, 7, 9, 4, 6, 6, 8, 8, 10, 3, 5, 5, 7, 7, 9, 9, 11, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14])) == "acihgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 6, 8, 5, 7, 7, 9, 4, 6, 6, 8, 8, 10, 3, 5, 5, 7, 7, 9, 9, 11, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14])) == "acihgh": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "azmtxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "azmtxz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([13, 12, 14, 11, 13, 13, 15, 10, 12, 12, 14, 14, 16, 9, 11, 11, 13, 13, 15, 15, 17, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 23, 25, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 24, 26])) == "akppmlmn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([13, 12, 14, 11, 13, 13, 15, 10, 12, 12, 14, 14, 16, 9, 11, 11, 13, 13, 15, 15, 17, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 23, 25, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 24, 26])) == "akppmlmn": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ngca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ngca": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2])) == "addbz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2])) == "addbz": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "zyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "zyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, 2, 1, 1, 2, 0, 0, 2, 0, 1, 2, 1, 2, 0, 0, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1])) == "aacab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, 2, 1, 1, 2, 0, 0, 2, 0, 1, 2, 1, 2, 0, 0, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1])) == "aacab": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])) == "aaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])) == "aaaab": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 19, 21, 18, 22, 17, 23, 16, 24, 15, 25, 14, 26, 13, 27, 12, 28, 11, 29, 10, 30, 9, 31, 8, 32, 7, 33, 6, 34, 5, 35, 4, 36, 3, 37, 2, 38, 1, 39, 0])) == "akpwtu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 19, 21, 18, 22, 17, 23, 16, 24, 15, 25, 14, 26, 13, 27, 12, 28, 11, 29, 10, 30, 9, 31, 8, 32, 7, 33, 6, 34, 5, 35, 4, 36, 3, 37, 2, 38, 1, 39, 0])) == "akpwtu": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13])) == "hdba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13])) == "hdba": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, 1, 5, 3, 6, 0, None, None, None, None, None, None, 7])) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, 1, 5, 3, 6, 0, None, None, None, None, None, None, 7])) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10, 24, 11, 23, 12, 22, 13, 21, 14, 20, 15, 19, 16, 18, 17])) == "lcgf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10, 24, 11, 23, 12, 22, 13, 21, 14, 20, 15, 19, 16, 18, 17])) == "lcgf": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaabc": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, None, None, 4, 8, None, None, None, None, 5, 6])) == "cpud"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, None, None, 4, 8, None, None, None, None, 5, 6])) == "cpud": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 3, 6, 7, 9, None, None, 2, None, None, None, None, None, None, None, 0])) == "cgef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 3, 6, 7, 9, None, None, 2, None, None, None, None, None, None, None, 0])) == "cgef": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == "beif"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == "beif": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4])) == "dba"
    assert candidate(root = tree_node([2, 2, 1, None, 1, 0, None, 0])) == "abc"
    assert candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2])) == "adz"
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == "onmlkjihgfedcb"
    assert candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "anuxz"
    assert candidate(root = tree_node([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])) == "aaaaab"
    assert candidate(root = tree_node([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])) == "abaca"
    assert candidate(root = tree_node([12, 11, 14, 10, 13, 13, 15, 9, 12, 12, 14, 14, 16, 8, 11, 11, 13, 13, 15, 15, 17, 7, 10, 10, 12, 12, 14, 14, 16, 16, 18])) == "honlm"
    assert candidate(root = tree_node([4, 2, 5, 1, 3, None, 6, 0, None, None, 7, None, None, 8, None, None, 9])) == "gfe"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == "fdba"
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == "fffff"
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, None])) == "bce"
    assert candidate(root = tree_node([12, 11, 13, 10, None, 14, None, 9, None, 15, None, 8, None, 16, None, 7, None, 17, None, 6, None, 18, None, 5, None, 19, None, 4, None, 20, None, 3, None, 21, None, 2, None, 22, None, 1, None, 23, None, 0, None, 24, None, 25])) == "yxwvutsrqponm"
    assert candidate(root = tree_node([12, 11, 13, 10, 14, 9, 15, 8, 16, 7, 17, 6, 18, 5, 19, 4, 20, 3, 21, 2, 22, 1, 23, 0, 24, 25])) == "agjnm"
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == "beif"
    assert candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])) == "ahbbz"
    assert candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None])) == "aaaaab"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "ngdb"
    assert candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == "aaaba"
    assert candidate(root = tree_node([0, 1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "ca"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "awsheba"
    assert candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "lcdz"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, 0, None, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "mykdca"
    assert candidate(root = tree_node([0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "hdba"
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 5, 6, None, None, 8, 9, None, None, 10, 11, None, None, None, None, None, None, 12, 13, None, None, None, None, None, 14, 15])) == "fhud"
    assert candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == "ltxz"
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, None, None, None, None, None, None, None, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ftbgjk"
    assert candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, None, 0, 0, 0, 0, None])) == "aaab"
    assert candidate(root = tree_node([7, 3, 15, 2, 5, 12, 18, None, 4, 6, None, 10, 14, 16, 19, None, None, None, None, None, 8, None, None, None, None, None, 9, 11, 13, None, None, 17])) == "ecdh"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "iecb"
    assert candidate(root = tree_node([13, 7, 18, 3, 9, None, 20, 1, None, 5, 10, None, None, None, None, 2, 6, 8, 11, None, None, 12, None, 14, None, 15])) == "bdhn"
    assert candidate(root = tree_node([13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0])) == "atkon"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == "angca"
    assert candidate(root = tree_node([7, 15, 10, 2, 20, 7, 13, None, 8, None, None, 2, 12, None, None, None, None, 4, 6, 5, 11, None, None, None, None, None, None, None, None, 3, None, None, None, None, None])) == "echkh"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == "dfk"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "azmfca"
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "alrhcpud"
    assert candidate(root = tree_node([10, 9, 11, 8, 12, 7, 13, 6, 14, 5, 15, 4, 16, 3, 17, 2, 18, 1, 19, 0, 20, 25, 21, 24, 22, 23])) == "afmjk"
    assert candidate(root = tree_node([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])) == "mmmm"
    assert candidate(root = tree_node([0, 1, 2, None, None, None, None, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ba"
    assert candidate(root = tree_node([0, 2, 1, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == "igeba"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4])) == "dddba"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "meca"
    assert candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == "aaaaa"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aangdb"
    assert candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])) == "anuxz"
    assert candidate(root = tree_node([3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaacd"
    assert candidate(root = tree_node([0, 1, 2, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == "ba"
    assert candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == "anuxz"
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaaaaa"
    assert candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2])) == "adcdz"
    assert candidate(root = tree_node([10, 9, 10, 8, 9, 9, 10, 7, 8, 8, 9, 9, 10, 6, 7, 7, 8, 8, 9, 9, 10, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10])) == "aegjjjk"
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 10, 12, 7, 9, 9, 11, 11, 13, 6, 8, 8, 10, 10, 12, 12, 14, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18])) == "cngmlk"
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == "dddddd"
    assert candidate(root = tree_node([15, 14, 16, 13, 15, 15, 17, 12, 14, 14, 16, 16, 18, 11, 13, 13, 15, 15, 17, 17, 19, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23])) == "hslrqp"
    assert candidate(root = tree_node([7, 6, 8, 5, 7, 7, 9, 4, 6, 6, 8, 8, 10, 3, 5, 5, 7, 7, 9, 9, 11, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14])) == "acihgh"
    assert candidate(root = tree_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == "azmtxz"
    assert candidate(root = tree_node([13, 12, 14, 11, 13, 13, 15, 10, 12, 12, 14, 14, 16, 9, 11, 11, 13, 13, 15, 15, 17, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 23, 25, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 24, 26])) == "akppmlmn"
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == "ngca"
    assert candidate(root = tree_node([25, 1, 3, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2, 25, 1, 3, 0, 2])) == "addbz"
    assert candidate(root = tree_node([0, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == "zyxwvutsrqponmlkjihgfedcba"
    assert candidate(root = tree_node([1, 0, 2, 2, 1, 1, 2, 0, 0, 2, 0, 1, 2, 1, 2, 0, 0, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1])) == "aacab"
    assert candidate(root = tree_node([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])) == "aaaab"
    assert candidate(root = tree_node([20, 19, 21, 18, 22, 17, 23, 16, 24, 15, 25, 14, 26, 13, 27, 12, 28, 11, 29, 10, 30, 9, 31, 8, 32, 7, 33, 6, 34, 5, 35, 4, 36, 3, 37, 2, 38, 1, 39, 0])) == "akpwtu"
    assert candidate(root = tree_node([0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13])) == "hdba"
    assert candidate(root = tree_node([3, 2, 4, 1, 5, 3, 6, 0, None, None, None, None, None, None, 7])) == "abcd"
    assert candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10, 24, 11, 23, 12, 22, 13, 21, 14, 20, 15, 19, 16, 18, 17])) == "lcgf"
    assert candidate(root = tree_node([2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "aaabc"
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, None, None, 4, 8, None, None, None, None, 5, 6])) == "cpud"
    assert candidate(root = tree_node([5, 4, 8, 3, 6, 7, 9, None, None, 2, None, None, None, None, None, None, None, 0])) == "cgef"
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == "beif"


