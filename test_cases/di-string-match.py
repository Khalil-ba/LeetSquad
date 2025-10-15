def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "DDI") == [3, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDI") == [3, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDDI") == [6, 5, 0, 4, 3, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDDI") == [6, 5, 0, 4, 3, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDD") == [0, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDD") == [0, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDD") == [8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDD") == [8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "I") == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "I") == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIII") == [0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIII") == [0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "D") == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "D") == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIII") == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIII") == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIII") == [0, 7, 6, 5, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIII") == [0, 7, 6, 5, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDII") == [4, 3, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDII") == [4, 3, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDID") == [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDID") == [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDD") == [6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDD") == [6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "III") == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "III") == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDID") == [0, 4, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDID") == [0, 4, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDD") == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDD") == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDDID") == [7, 6, 0, 5, 4, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDDID") == [7, 6, 0, 5, 4, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDID") == [0, 8, 1, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDID") == [0, 8, 1, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDD") == [0, 1, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDD") == [0, 1, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDII") == [5, 4, 3, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDII") == [5, 4, 3, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDD") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDD") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIDDDIIID") == [12, 11, 0, 1, 2, 10, 9, 8, 3, 4, 5, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIDDDIIID") == [12, 11, 0, 1, 2, 10, 9, 8, 3, 4, 5, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDII") == [0, 10, 9, 8, 7, 6, 5, 4, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDII") == [0, 10, 9, 8, 7, 6, 5, 4, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIII") == [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIII") == [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDIIIII") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDIIIII") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIIDIIDI") == [0, 1, 10, 2, 3, 9, 4, 5, 8, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIIDIIDI") == [0, 1, 10, 2, 3, 9, 4, 5, 8, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDDIDDID") == [10, 9, 0, 8, 7, 1, 6, 5, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDDIDDID") == [10, 9, 0, 8, 7, 1, 6, 5, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDID") == [10, 9, 8, 7, 6, 5, 0, 4, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDID") == [10, 9, 8, 7, 6, 5, 0, 4, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDIDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 0, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDIDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 0, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIIIIII") == [0, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIIIIII") == [0, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDD") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDD") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIII") == [9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIII") == [9, 8, 7, 6, 5, 4, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIIIDDD") == [0, 1, 12, 11, 10, 9, 2, 3, 4, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIIIDDD") == [0, 1, 12, 11, 10, 9, 2, 3, 4, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDIIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDIIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIID") == [9, 8, 7, 6, 0, 1, 2, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIID") == [9, 8, 7, 6, 0, 1, 2, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDID") == [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDID") == [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDI") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDI") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIDIDIDI") == [10, 9, 8, 0, 7, 1, 6, 2, 5, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIDIDIDI") == [10, 9, 8, 0, 7, 1, 6, 2, 5, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDID") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDID") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDIDID") == [12, 11, 10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDIDID") == [12, 11, 10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIIIIIIIIDIDDDDD") == [0, 1, 18, 2, 3, 4, 5, 6, 7, 8, 9, 17, 10, 16, 15, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIIIIIIIIDIDDDDD") == [0, 1, 18, 2, 3, 4, 5, 6, 7, 8, 9, 17, 10, 16, 15, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIIIIIII") == [0, 12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIIIIIII") == [0, 12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIDIDIDIDIDID") == [22, 21, 20, 19, 0, 1, 2, 3, 4, 5, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIDIDIDIDIDID") == [22, 21, 20, 19, 0, 1, 2, 3, 4, 5, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDID") == [0, 12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDID") == [0, 12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDD") == [0, 1, 2, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDD") == [0, 1, 2, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDID") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDID") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIIIDDD") == [0, 1, 9, 2, 3, 4, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIIIDDD") == [0, 1, 9, 2, 3, 4, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDD") == [0, 1, 2, 3, 4, 5, 6, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDD") == [0, 1, 2, 3, 4, 5, 6, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIIIIIIIIIID") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIIIIIIIIIID") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDI") == [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDI") == [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDII") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDII") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIDDDIIDDDIIII") == [0, 18, 17, 16, 1, 2, 15, 14, 13, 3, 4, 12, 11, 10, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIDDDIIDDDIIII") == [0, 18, 17, 16, 1, 2, 15, 14, 13, 3, 4, 12, 11, 10, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIDDDD") == [12, 11, 10, 9, 0, 1, 2, 3, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIDDDD") == [12, 11, 10, 9, 0, 1, 2, 3, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDDDDD") == [0, 10, 1, 9, 2, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDDDDD") == [0, 10, 1, 9, 2, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDDDDDDDDIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 27, 26, 25, 24, 23, 22, 21, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDDDDDDDDIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 27, 26, 25, 24, 23, 22, 21, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDDDD") == [0, 11, 1, 10, 2, 9, 3, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDDDD") == [0, 11, 1, 10, 2, 9, 3, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDID") == [0, 1, 2, 3, 4, 12, 11, 10, 9, 8, 5, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDID") == [0, 1, 2, 3, 4, 12, 11, 10, 9, 8, 5, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDIIIIIIIII") == [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDIIIIIIIII") == [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDIDIDI") == [0, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDIDIDI") == [0, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDD") == [0, 1, 2, 3, 4, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDD") == [0, 1, 2, 3, 4, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDIDIDID") == [0, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDIDIDID") == [0, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIDIDIDID") == [11, 10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIDIDIDID") == [11, 10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDIIID") == [0, 1, 2, 10, 9, 8, 3, 4, 5, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDIIID") == [0, 1, 2, 10, 9, 8, 3, 4, 5, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDIDID") == [10, 9, 0, 1, 8, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDIDID") == [10, 9, 0, 1, 8, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDDDDDDD") == [12, 11, 10, 9, 0, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDDDDDDD") == [12, 11, 10, 9, 0, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDD") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDD") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIDIDIDID") == [10, 0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIDIDIDID") == [10, 0, 1, 9, 2, 8, 3, 7, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDIII") == [0, 12, 11, 10, 9, 8, 7, 6, 5, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDIII") == [0, 12, 11, 10, 9, 8, 7, 6, 5, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIDDDDDDDD") == [12, 11, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIDDDDDDDD") == [12, 11, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIDDDDIII") == [0, 1, 2, 3, 11, 10, 9, 8, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIDDDDIII") == [0, 1, 2, 3, 11, 10, 9, 8, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDID") == [0, 1, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDID") == [0, 1, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDIDID") == [0, 10, 1, 9, 8, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDIDID") == [0, 10, 1, 9, 8, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDD") == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDD") == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDD") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDD") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDI") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDI") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDID") == [0, 16, 1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDID") == [0, 16, 1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDII") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDII") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIIIIII") == [0, 1, 2, 3, 4, 12, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIIIIII") == [0, 1, 2, 3, 4, 12, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDDDD") == [0, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDDDD") == [0, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDD") == [0, 1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDD") == [0, 1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIDDDDDDID") == [0, 1, 2, 3, 12, 11, 10, 9, 8, 7, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIDDDDDDID") == [0, 1, 2, 3, 12, 11, 10, 9, 8, 7, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIDDDDD") == [11, 10, 9, 8, 7, 0, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIDDDDD") == [11, 10, 9, 8, 7, 0, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIII") == [8, 7, 6, 5, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIII") == [8, 7, 6, 5, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDDDDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDDDDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIIIII") == [12, 11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIIIII") == [12, 11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDDDDD") == [0, 12, 1, 11, 2, 10, 3, 9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDDDDD") == [0, 12, 1, 11, 2, 10, 3, 9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDID") == [10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDID") == [10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDDIIID") == [11, 10, 0, 1, 9, 8, 7, 2, 3, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDDIIID") == [11, 10, 0, 1, 9, 8, 7, 2, 3, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDII") == [0, 1, 10, 9, 8, 7, 6, 5, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDII") == [0, 1, 10, 9, 8, 7, 6, 5, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDIDID") == [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDIDID") == [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIIIIIII") == [14, 13, 12, 11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIIIIIII") == [14, 13, 12, 11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIDDDDDDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIDDDDDDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDIII") == [0, 1, 2, 3, 4, 12, 11, 10, 9, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDIII") == [0, 1, 2, 3, 4, 12, 11, 10, 9, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDID") == [25, 0, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDID") == [25, 0, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIDDDIIIIIDDDIIII") == [26, 25, 24, 23, 0, 1, 2, 3, 4, 5, 6, 22, 21, 20, 7, 8, 9, 10, 11, 19, 18, 17, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIDDDIIIIIDDDIIII") == [26, 25, 24, 23, 0, 1, 2, 3, 4, 5, 6, 22, 21, 20, 7, 8, 9, 10, 11, 19, 18, 17, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDDD") == [0, 1, 2, 10, 9, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDDD") == [0, 1, 2, 10, 9, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDD") == [0, 1, 2, 3, 4, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDD") == [0, 1, 2, 3, 4, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDD") == [0, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDD") == [0, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIIIIIIDDDDD") == [21, 20, 19, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIIIIIIDDDDD") == [21, 20, 19, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDD") == [0, 1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDD") == [0, 1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIIIIIDDDD") == [0, 1, 12, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIIIIIDDDD") == [0, 1, 12, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDIII") == [11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDIII") == [11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDID") == [12, 11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDID") == [12, 11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDIDIDID") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 0, 6, 1, 5, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDIDIDID") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 0, 6, 1, 5, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIIIDDD") == [0, 1, 11, 10, 9, 2, 3, 4, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIIIDDD") == [0, 1, 11, 10, 9, 2, 3, 4, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDI") == [10, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDI") == [10, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDDDII") == [12, 11, 10, 9, 8, 7, 0, 6, 5, 4, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDDDII") == [12, 11, 10, 9, 8, 7, 0, 6, 5, 4, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDD") == [0, 10, 1, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDD") == [0, 10, 1, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDID") == [0, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDID") == [0, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIII") == [11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIII") == [11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIID") == [10, 9, 8, 7, 6, 5, 0, 1, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIID") == [10, 9, 8, 7, 6, 5, 0, 1, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDID") == [0, 20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDID") == [0, 20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDID") == [0, 1, 10, 9, 8, 7, 6, 5, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDID") == [0, 1, 10, 9, 8, 7, 6, 5, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIII") == [10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIII") == [10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIDDII") == [10, 9, 8, 7, 0, 1, 6, 5, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIDDII") == [10, 9, 8, 7, 0, 1, 6, 5, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDID") == [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDID") == [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDID") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDID") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIDDDII") == [10, 9, 0, 1, 2, 8, 7, 6, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIDDDII") == [10, 9, 0, 1, 2, 8, 7, 6, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDIIIIIIIIIIDDDDDDDD") == [27, 26, 25, 24, 23, 22, 21, 20, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDIIIIIIIIIIDDDDDDDD") == [27, 26, 25, 24, 23, 22, 21, 20, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 17, 16, 15, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIIIII") == [11, 10, 9, 8, 7, 0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIIIII") == [11, 10, 9, 8, 7, 0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDIII") == [0, 1, 10, 9, 8, 7, 6, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDIII") == [0, 1, 10, 9, 8, 7, 6, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDDDDDD") == [0, 14, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDDDDDD") == [0, 14, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIII") == [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIII") == [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIIID") == [0, 1, 10, 9, 8, 7, 2, 3, 4, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIIID") == [0, 1, 10, 9, 8, 7, 2, 3, 4, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDDIID") == [10, 9, 0, 1, 8, 7, 6, 2, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDDIID") == [10, 9, 0, 1, 8, 7, 6, 2, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDID") == [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDID") == [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDD") == [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDD") == [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDDDDDD") == [0, 11, 1, 10, 2, 9, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDDDDDD") == [0, 11, 1, 10, 2, 9, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDD") == [0, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDD") == [0, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDDID") == [0, 1, 12, 11, 10, 9, 8, 7, 6, 5, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDDID") == [0, 1, 12, 11, 10, 9, 8, 7, 6, 5, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDD") == [0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDD") == [0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIDIDIDIDIDIDDD") == [0, 1, 2, 3, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIDIDIDIDIDIDDD") == [0, 1, 2, 3, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDIDDD") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 0, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDIDDD") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 0, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIDDDIIIID") == [12, 0, 1, 2, 11, 10, 9, 3, 4, 5, 6, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIDDDIIIID") == [12, 0, 1, 2, 11, 10, 9, 3, 4, 5, 6, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIDDDID") == [0, 10, 9, 8, 1, 7, 6, 5, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIDDDID") == [0, 10, 9, 8, 1, 7, 6, 5, 2, 4, 3]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "DDI") == [3, 2, 0, 1]
    assert candidate(s = "DDIDDI") == [6, 5, 0, 4, 3, 1, 2]
    assert candidate(s = "IDDD") == [0, 4, 3, 2, 1]
    assert candidate(s = "DDDDDDDD") == [8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "I") == [0, 1]
    assert candidate(s = "IIIIII") == [0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "D") == [1, 0]
    assert candidate(s = "IIII") == [0, 1, 2, 3, 4]
    assert candidate(s = "IDDDIII") == [0, 7, 6, 5, 1, 2, 3, 4]
    assert candidate(s = "DDII") == [4, 3, 0, 1, 2]
    assert candidate(s = "IDIDIDIDID") == [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert candidate(s = "IIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(s = "DDDDDD") == [6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "III") == [0, 1, 2, 3]
    assert candidate(s = "IDID") == [0, 4, 1, 3, 2]
    assert candidate(s = "DDDD") == [4, 3, 2, 1, 0]
    assert candidate(s = "DDIDDID") == [7, 6, 0, 5, 4, 1, 3, 2]
    assert candidate(s = "IDIDIDID") == [0, 8, 1, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "IIDDD") == [0, 1, 5, 4, 3, 2]
    assert candidate(s = "DDDII") == [5, 4, 3, 0, 1, 2]
    assert candidate(s = "IIIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert candidate(s = "IDDDDDDDDDDDDD") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDIIIDDDIIID") == [12, 11, 0, 1, 2, 10, 9, 8, 3, 4, 5, 7, 6]
    assert candidate(s = "IDDDDDDDII") == [0, 10, 9, 8, 7, 6, 5, 4, 1, 2, 3]
    assert candidate(s = "DDDDDDIIIII") == [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
    assert candidate(s = "IDDDDDDDDIIIII") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "IIDIIDIIDI") == [0, 1, 10, 2, 3, 9, 4, 5, 8, 6, 7]
    assert candidate(s = "DDIDDIDDID") == [10, 9, 0, 8, 7, 1, 6, 5, 2, 4, 3]
    assert candidate(s = "DDDDDDIDID") == [10, 9, 8, 7, 6, 5, 0, 4, 1, 3, 2]
    assert candidate(s = "DDDDDDDDDIDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 0, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(s = "IDDDDDIIIIII") == [0, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "DDDDDDDDDDDDDDDD") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DDDDDDIII") == [9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
    assert candidate(s = "IIDDDDIIIDDD") == [0, 1, 12, 11, 10, 9, 2, 3, 4, 8, 7, 6, 5]
    assert candidate(s = "DDDDDDDDDIIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
    assert candidate(s = "DDDDIIIID") == [9, 8, 7, 6, 0, 1, 2, 3, 5, 4]
    assert candidate(s = "IDIDIDIDIDIDID") == [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
    assert candidate(s = "DDDDDDDDDI") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 1]
    assert candidate(s = "DDDIDIDIDI") == [10, 9, 8, 0, 7, 1, 6, 2, 5, 3, 4]
    assert candidate(s = "DDDDDDDDDID") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 2, 1]
    assert candidate(s = "DDDDIDIDIDID") == [12, 11, 10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "IIDIIIIIIIIDIDDDDD") == [0, 1, 18, 2, 3, 4, 5, 6, 7, 8, 9, 17, 10, 16, 15, 14, 13, 12, 11]
    assert candidate(s = "IDDDIIIIIIII") == [0, 12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(s = "DDDDIIIIIIIDIDIDIDIDID") == [22, 21, 20, 19, 0, 1, 2, 3, 4, 5, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]
    assert candidate(s = "IIIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    assert candidate(s = "IDIDIDIDIDID") == [0, 12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
    assert candidate(s = "IIIIIIIDDDDD") == [0, 1, 2, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7]
    assert candidate(s = "IDDDDDDDDDDDID") == [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 1, 3, 2]
    assert candidate(s = "IIDIIIDDD") == [0, 1, 9, 2, 3, 4, 8, 7, 6, 5]
    assert candidate(s = "IIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
    assert candidate(s = "IIIIIIIDDD") == [0, 1, 2, 3, 4, 5, 6, 10, 9, 8, 7]
    assert candidate(s = "DDDDDDDDDDIIIIIIIIIID") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
    assert candidate(s = "IDIDIDIDIDI") == [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert candidate(s = "DDDDDDDDDDII") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 1, 2]
    assert candidate(s = "IDDDIIDDDIIDDDIIII") == [0, 18, 17, 16, 1, 2, 15, 14, 13, 3, 4, 12, 11, 10, 5, 6, 7, 8, 9]
    assert candidate(s = "DDDDIIIIDDDD") == [12, 11, 10, 9, 0, 1, 2, 3, 8, 7, 6, 5, 4]
    assert candidate(s = "IIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert candidate(s = "IDIDIDDDDD") == [0, 10, 1, 9, 2, 8, 7, 6, 5, 4, 3]
    assert candidate(s = "IIIIIIIIIIIDDDDDDDDIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 27, 26, 25, 24, 23, 22, 21, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(s = "IDIDIDIDDDD") == [0, 11, 1, 10, 2, 9, 3, 8, 7, 6, 5, 4]
    assert candidate(s = "DDDDDDDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "IIIIIDDDDDID") == [0, 1, 2, 3, 4, 12, 11, 10, 9, 8, 5, 7, 6]
    assert candidate(s = "IDDDDDDDDDDDDIIIIIIIII") == [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(s = "IIDIDIDIDI") == [0, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert candidate(s = "IIIIIDDDDDDDDD") == [0, 1, 2, 3, 4, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    assert candidate(s = "IIDIDIDIDID") == [0, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
    assert candidate(s = "DDDIDIDIDID") == [11, 10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "IIIDDDIIID") == [0, 1, 2, 10, 9, 8, 3, 4, 5, 7, 6]
    assert candidate(s = "IIIIIIIIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18]
    assert candidate(s = "DDIIDDIDID") == [10, 9, 0, 1, 8, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "DDDDIDDDDDDD") == [12, 11, 10, 9, 0, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDDDDDDDDDDDD") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DIIDIDIDID") == [10, 0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert candidate(s = "IDDDDDDDDIII") == [0, 12, 11, 10, 9, 8, 7, 6, 5, 1, 2, 3, 4]
    assert candidate(s = "DDDDDDDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DDDIDDDDDDDD") == [12, 11, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIDDDDIII") == [0, 1, 2, 3, 11, 10, 9, 8, 4, 5, 6, 7]
    assert candidate(s = "IIDIDID") == [0, 1, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "IIIIIIIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(s = "IDIDDDIDID") == [0, 10, 1, 9, 8, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDD") == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DDDDDDDDDD") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DDDDDDDDDDI") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0, 1]
    assert candidate(s = "IDIDIDIDIDIDIDID") == [0, 16, 1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8]
    assert candidate(s = "DDDDDDDDDDDII") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 1, 2]
    assert candidate(s = "IIIIIDIIIIII") == [0, 1, 2, 3, 4, 12, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(s = "IIDDDDDDDDDD") == [0, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "IIIIIIIDDDD") == [0, 1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]
    assert candidate(s = "IIIIDDDDDDID") == [0, 1, 2, 3, 12, 11, 10, 9, 8, 7, 4, 6, 5]
    assert candidate(s = "DDDDDIDDDDD") == [11, 10, 9, 8, 7, 0, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDIIII") == [8, 7, 6, 5, 0, 1, 2, 3, 4]
    assert candidate(s = "IIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(s = "IIIIIIIIIIIDDDDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    assert candidate(s = "DDDDDDDIIIII") == [12, 11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
    assert candidate(s = "IDIDIDIDDDDD") == [0, 12, 1, 11, 2, 10, 3, 9, 8, 7, 6, 5, 4]
    assert candidate(s = "DDIDIDIDID") == [10, 9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "DDIIDDDIIID") == [11, 10, 0, 1, 9, 8, 7, 2, 3, 4, 6, 5]
    assert candidate(s = "IIDDDDDDII") == [0, 1, 10, 9, 8, 7, 6, 5, 2, 3, 4]
    assert candidate(s = "IIDIDIDID") == [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert candidate(s = "DDDDDDDIIIIIII") == [14, 13, 12, 11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "IIIIIIIIIIIIIIDDDDDDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
    assert candidate(s = "IIIIIDDDDIII") == [0, 1, 2, 3, 4, 12, 11, 10, 9, 5, 6, 7, 8]
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDID") == [25, 0, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]
    assert candidate(s = "DDDDIIIIIIIDDDIIIIIDDDIIII") == [26, 25, 24, 23, 0, 1, 2, 3, 4, 5, 6, 22, 21, 20, 7, 8, 9, 10, 11, 19, 18, 17, 12, 13, 14, 15, 16]
    assert candidate(s = "IIIDDDDDDD") == [0, 1, 2, 10, 9, 8, 7, 6, 5, 4, 3]
    assert candidate(s = "IIIIIDDDDD") == [0, 1, 2, 3, 4, 10, 9, 8, 7, 6, 5]
    assert candidate(s = "DDDDDDDDDDIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    assert candidate(s = "IDDDDDDDDDDD") == [0, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDIIIIIIIIIIIIDDDDD") == [21, 20, 19, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]
    assert candidate(s = "IIIIIDDDDDD") == [0, 1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5]
    assert candidate(s = "IIDIIIIIDDDD") == [0, 1, 12, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]
    assert candidate(s = "DDDDDDDDIII") == [11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
    assert candidate(s = "DDIDIDIDIDID") == [12, 11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert candidate(s = "DDDDDDDDDIDIDID") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 0, 6, 1, 5, 2, 4, 3]
    assert candidate(s = "IIIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(s = "IIDDDIIIDDD") == [0, 1, 11, 10, 9, 2, 3, 4, 8, 7, 6, 5]
    assert candidate(s = "DIDIDIDIDI") == [10, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
    assert candidate(s = "DDDDDDDDDDDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DDDDDDIDDDII") == [12, 11, 10, 9, 8, 7, 0, 6, 5, 4, 1, 2, 3]
    assert candidate(s = "IDIDDDDDDD") == [0, 10, 1, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDID") == [0, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12]
    assert candidate(s = "DDDDIIIIIII") == [11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "DDDDDDIIID") == [10, 9, 8, 7, 6, 5, 0, 1, 2, 4, 3]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDID") == [0, 20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]
    assert candidate(s = "DDDDDDDDDDDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "IIDDDDDDID") == [0, 1, 10, 9, 8, 7, 6, 5, 2, 4, 3]
    assert candidate(s = "IIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(s = "DDDDDDIIII") == [10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    assert candidate(s = "DDDDIIDDII") == [10, 9, 8, 7, 0, 1, 6, 5, 2, 3, 4]
    assert candidate(s = "DIDIDIDIDID") == [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert candidate(s = "DDDDDDDDDDDID") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 0, 2, 1]
    assert candidate(s = "DDDDDDDDDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "DDIIIDDDII") == [10, 9, 0, 1, 2, 8, 7, 6, 3, 4, 5]
    assert candidate(s = "DDDDDDDDDIIIIIIIIIIDDDDDDDD") == [27, 26, 25, 24, 23, 22, 21, 20, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    assert candidate(s = "DDDDDIIIIII") == [11, 10, 9, 8, 7, 0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "IIDDDDDIII") == [0, 1, 10, 9, 8, 7, 6, 2, 3, 4, 5]
    assert candidate(s = "IDIDDDDDDDDDDD") == [0, 14, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIII") == [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert candidate(s = "IIDDDDIIID") == [0, 1, 10, 9, 8, 7, 2, 3, 4, 6, 5]
    assert candidate(s = "IIIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12]
    assert candidate(s = "DDIIDDDIID") == [10, 9, 0, 1, 8, 7, 6, 2, 3, 5, 4]
    assert candidate(s = "DIDIDIDID") == [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    assert candidate(s = "IIIIIIIDDDDDDD") == [0, 1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7]
    assert candidate(s = "IDDDDDDDDD") == [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIIIIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(s = "IIIIIIIIIIID") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]
    assert candidate(s = "IDIDIDDDDDD") == [0, 11, 1, 10, 2, 9, 8, 7, 6, 5, 4, 3]
    assert candidate(s = "IIDDDDDDDD") == [0, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "IIDDDDDDDDID") == [0, 1, 12, 11, 10, 9, 8, 7, 6, 5, 2, 4, 3]
    assert candidate(s = "IIIIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(s = "IDDDDDDDDDD") == [0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIIDIDIDIDIDIDIDDD") == [0, 1, 2, 3, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 13, 12, 11]
    assert candidate(s = "DDDDDDDDDDDDDDDIDDD") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 0, 4, 3, 2, 1]
    assert candidate(s = "DDDDDDDDDDDIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
    assert candidate(s = "DIIIDDDIIIID") == [12, 0, 1, 2, 11, 10, 9, 3, 4, 5, 6, 8, 7]
    assert candidate(s = "IDDDIDDDID") == [0, 10, 9, 8, 1, 7, 6, 5, 2, 4, 3]


