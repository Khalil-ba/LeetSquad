def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "IIDIIIDIDDDDDIII") == [1, 2, 4, 3, 5, 6, 8, 7, 14, 13, 12, 11, 10, 9, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIIIDIDDDDDIII") == [1, 2, 4, 3, 5, 6, 8, 7, 14, 13, 12, 11, 10, 9, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDID") == [2, 1, 4, 3, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDID") == [2, 1, 4, 3, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDID") == [1, 3, 2, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDID") == [1, 3, 2, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDD") == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDD") == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "I") == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "I") == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIDD") == [3, 2, 1, 4, 5, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIDD") == [3, 2, 1, 4, 5, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDI") == [3, 2, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDI") == [3, 2, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIII") == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIII") == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IID") == [1, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IID") == [1, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDI") == [1, 5, 4, 3, 2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDI") == [1, 5, 4, 3, 2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDII") == [1, 2, 6, 5, 4, 3, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDII") == [1, 2, 6, 5, 4, 3, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDD") == [2, 1, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDD") == [2, 1, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDI") == [1, 4, 3, 2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDI") == [1, 4, 3, 2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDII") == [1, 2, 3, 9, 8, 7, 6, 5, 4, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDII") == [1, 2, 3, 9, 8, 7, 6, 5, 4, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DI") == [2, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DI") == [2, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDD") == [1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDD") == [1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIDDDDIIDDD") == [6, 5, 4, 3, 2, 1, 7, 12, 11, 10, 9, 8, 13, 17, 16, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIDDDDIIDDD") == [6, 5, 4, 3, 2, 1, 7, 12, 11, 10, 9, 8, 13, 17, 16, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDID") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDID") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIDIDIDIDIDIDID") == [2, 1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIDIDIDIDIDIDID") == [2, 1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDIDIDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDIDIDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIII") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIII") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIIIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIIIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDII") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDII") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDIIII") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDIIII") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19, 20, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19, 20, 21]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIIIIIDDDDD") == [1, 2, 6, 5, 4, 3, 7, 8, 9, 10, 16, 15, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIIIIIDDDDD") == [1, 2, 6, 5, 4, 3, 7, 8, 9, 10, 16, 15, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDIIIIIDII") == [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 13, 12, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDIIIIIDII") == [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 13, 12, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIDDDD") == [1, 5, 4, 3, 2, 6, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIDDDD") == [1, 5, 4, 3, 2, 6, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDID") == [1, 2, 3, 4, 5, 9, 8, 7, 6, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDID") == [1, 2, 3, 4, 5, 9, 8, 7, 6, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIIDDDDDDI") == [4, 3, 2, 1, 5, 12, 11, 10, 9, 8, 7, 6, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIIDDDDDDI") == [4, 3, 2, 1, 5, 12, 11, 10, 9, 8, 7, 6, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDIDID") == [7, 6, 5, 4, 3, 2, 1, 9, 8, 11, 10, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDIDID") == [7, 6, 5, 4, 3, 2, 1, 9, 8, 11, 10, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIDDDIID") == [1, 2, 5, 4, 3, 9, 8, 7, 6, 10, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIDDDIID") == [1, 2, 5, 4, 3, 9, 8, 7, 6, 10, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDDDIDID") == [5, 4, 3, 2, 1, 7, 6, 11, 10, 9, 8, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDDDIDID") == [5, 4, 3, 2, 1, 7, 6, 11, 10, 9, 8, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDID") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDID") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIIDID") == [1, 2, 6, 5, 4, 3, 7, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIIDID") == [1, 2, 6, 5, 4, 3, 7, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDIDID") == [5, 4, 3, 2, 1, 7, 6, 9, 8, 11, 10, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDIDID") == [5, 4, 3, 2, 1, 7, 6, 9, 8, 11, 10, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIIIIIIIII") == [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIIIIIIIII") == [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIDII") == [7, 6, 5, 4, 3, 2, 1, 9, 8, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIDII") == [7, 6, 5, 4, 3, 2, 1, 9, 8, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDD") == [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDD") == [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDIII") == [1, 9, 8, 7, 6, 5, 4, 3, 2, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDIII") == [1, 9, 8, 7, 6, 5, 4, 3, 2, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIDID") == [1, 5, 4, 3, 2, 6, 8, 7, 10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIDID") == [1, 5, 4, 3, 2, 6, 8, 7, 10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDIIIIIIIIIIIIII") == [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDIIIIIIIIIIIIII") == [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIDIDDDD") == [8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 15, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIDIDDDD") == [8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 15, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDIIIIIIIIIIIIIIII") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDIIIIIIIIIIIIIIII") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDIIIIII") == [1, 2, 3, 4, 5, 6, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDIIIIII") == [1, 2, 3, 4, 5, 6, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIIID") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIIID") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDD") == [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDD") == [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIIIIID") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIIIIID") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDIIIIID") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 15, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDIIIIID") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 15, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDDDDIIII") == [1, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 14, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDDDDIIII") == [1, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 14, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDIDIDI") == [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDIDIDI") == [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIDIDDD") == [4, 3, 2, 1, 6, 5, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIDIDDD") == [4, 3, 2, 1, 6, 5, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDIDDDI") == [1, 2, 3, 7, 6, 5, 4, 11, 10, 9, 8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDIDDDI") == [1, 2, 3, 7, 6, 5, 4, 11, 10, 9, 8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDIDDDDDD") == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 17, 16, 15, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDIDDDDDD") == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 17, 16, 15, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDDDDD") == [1, 3, 2, 5, 4, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDDDDD") == [1, 3, 2, 5, 4, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDDIIIDDDD") == [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 11, 12, 17, 16, 15, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDDIIIDDDD") == [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 11, 12, 17, 16, 15, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDIIDDD") == [1, 2, 6, 5, 4, 3, 7, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDIIDDD") == [1, 2, 6, 5, 4, 3, 7, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDDDD") == [1, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDDDD") == [1, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDIIII") == [1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDIIII") == [1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDI") == [7, 6, 5, 4, 3, 2, 1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDI") == [7, 6, 5, 4, 3, 2, 1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDID") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDID") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDD") == [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDD") == [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDIID") == [1, 3, 2, 7, 6, 5, 4, 8, 10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDIID") == [1, 3, 2, 7, 6, 5, 4, 8, 10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIDDDIIDDID") == [2, 1, 3, 4, 8, 7, 6, 5, 9, 12, 11, 10, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIDDDIIDDID") == [2, 1, 3, 4, 8, 7, 6, 5, 9, 12, 11, 10, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDD") == [1, 2, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDD") == [1, 2, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDDDDDDDDDD") == [1, 2, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDDDDDDDDDD") == [1, 2, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDD") == [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDD") == [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDIDID") == [3, 2, 1, 4, 7, 6, 5, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDIDID") == [3, 2, 1, 4, 7, 6, 5, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDD") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDD") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDDD") == [5, 4, 3, 2, 1, 7, 6, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDDD") == [5, 4, 3, 2, 1, 7, 6, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 2, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 2, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDD") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDD") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDIIIIID") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 16, 18, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDIIIIID") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 16, 18, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIDDD") == [1, 7, 6, 5, 4, 3, 2, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIDDD") == [1, 7, 6, 5, 4, 3, 2, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIDDDDI") == [1, 2, 5, 4, 3, 10, 9, 8, 7, 6, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIDDDDI") == [1, 2, 5, 4, 3, 10, 9, 8, 7, 6, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79, 82, 81]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79, 82, 81]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDID") == [1, 2, 4, 3, 6, 5, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDID") == [1, 2, 4, 3, 6, 5, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDIDIDID") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 11, 10, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDIDIDID") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 11, 10, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDIDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDIDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIIIII") == [4, 3, 2, 1, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIIIII") == [4, 3, 2, 1, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDDDDID") == [1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDDDDID") == [1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDIIDDIID") == [3, 2, 1, 4, 7, 6, 5, 8, 11, 10, 9, 12, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDIIDDIID") == [3, 2, 1, 4, 7, 6, 5, 8, 11, 10, 9, 12, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDDDDDDDI") == [1, 3, 2, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDDDDDDDI") == [1, 3, 2, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDDDIID") == [1, 2, 4, 3, 8, 7, 6, 5, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDDDIID") == [1, 2, 4, 3, 8, 7, 6, 5, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIDIDID") == [1, 2, 5, 4, 3, 7, 6, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIDIDID") == [1, 2, 5, 4, 3, 7, 6, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIIDDDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 15, 14, 13, 12, 11, 10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIIDDDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 15, 14, 13, 12, 11, 10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIDDDIIDDD") == [1, 5, 4, 3, 2, 6, 10, 9, 8, 7, 11, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIDDDIIDDD") == [1, 5, 4, 3, 2, 6, 10, 9, 8, 7, 11, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDD") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDD") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDIDIDIDID") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 11, 10, 13, 12, 15, 14, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDIDIDIDID") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 11, 10, 13, 12, 15, 14, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIIDDDDDDDDI") == [4, 3, 2, 1, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIIDDDDDDDDI") == [4, 3, 2, 1, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDIDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDIDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDDDI") == [1, 3, 2, 12, 11, 10, 9, 8, 7, 6, 5, 4, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDDDI") == [1, 3, 2, 12, 11, 10, 9, 8, 7, 6, 5, 4, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDIIIDDDIIID") == [1, 2, 3, 7, 6, 5, 4, 8, 9, 13, 12, 11, 10, 14, 15, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDIIIDDDIIID") == [1, 2, 3, 7, 6, 5, 4, 8, 9, 13, 12, 11, 10, 14, 15, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDDIIII") == [1, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDDIIII") == [1, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDIIIIIIIIIIIIIDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 31, 30, 29, 28, 27, 26, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDIIIIIIIIIIIIIDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 31, 30, 29, 28, 27, 26, 25]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDI") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDI") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDIDID") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 13, 16, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDIDID") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 13, 16, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIIDDDDDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIIDDDDDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDIDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDIDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDDD") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 17, 16, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDDD") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 17, 16, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 15, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 15, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIIIIIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIIIIIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIDDDDDDDDDDDDIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 27, 28, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIDDDDDDDDDDDDIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 27, 28, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDIDIDIDIDIDIDIDIDID") == [1, 2, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDIDIDIDIDIDIDIDIDID") == [1, 2, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDIDDDDDDDDDIDDDDDDDDD") == [1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDIDDDDDDDDDIDDDDDDDDD") == [1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDDDD") == [1, 2, 3, 4, 5, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDDDD") == [1, 2, 3, 4, 5, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIDIDIDIDID") == [1, 2, 5, 4, 3, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIDIDIDIDID") == [1, 2, 5, 4, 3, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDIIII") == [1, 2, 3, 4, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 15, 16, 17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDIIII") == [1, 2, 3, 4, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 15, 16, 17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDIIIIIIIIII") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDIIIIIIIIII") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDIDID") == [1, 2, 3, 4, 5, 6, 7, 9, 8, 11, 10, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDIDID") == [1, 2, 3, 4, 5, 6, 7, 9, 8, 11, 10, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDIDID") == [1, 7, 6, 5, 4, 3, 2, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDIDID") == [1, 7, 6, 5, 4, 3, 2, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIDIDIDIDI") == [1, 5, 4, 3, 2, 7, 6, 9, 8, 11, 10, 13, 12, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIDIDIDIDI") == [1, 5, 4, 3, 2, 7, 6, 9, 8, 11, 10, 13, 12, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDIIIIIIIII") == [1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDIIIIIIIII") == [1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIDIIDIDI") == [2, 1, 3, 5, 4, 6, 8, 7, 10, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIDIIDIDI") == [2, 1, 3, 5, 4, 6, 8, 7, 10, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDDDDD") == [1, 2, 3, 4, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDDDDD") == [1, 2, 3, 4, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDIIIIIDDDDDDIIIIIDDDDD") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 16, 23, 22, 21, 20, 19, 18, 17, 24, 25, 26, 27, 33, 32, 31, 30, 29, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDIIIIIDDDDDDIIIIIDDDDD") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 16, 23, 22, 21, 20, 19, 18, 17, 24, 25, 26, 27, 33, 32, 31, 30, 29, 28]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIIIIIIIIID") == [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIIIIIIIIID") == [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDD") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDD") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIDDDIIDDDIID") == [1, 5, 4, 3, 2, 6, 10, 9, 8, 7, 11, 15, 14, 13, 12, 16, 18, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIDDDIIDDDIID") == [1, 5, 4, 3, 2, 6, 10, 9, 8, 7, 11, 15, 14, 13, 12, 16, 18, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIDDDD") == [5, 4, 3, 2, 1, 6, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIDDDD") == [5, 4, 3, 2, 1, 6, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDDD") == [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDDD") == [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIII") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIII") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIIDDDDI") == [4, 3, 2, 1, 5, 10, 9, 8, 7, 6, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIIDDDDI") == [4, 3, 2, 1, 5, 10, 9, 8, 7, 6, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIDDDDDIII") == [1, 2, 3, 9, 8, 7, 6, 5, 4, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIDDDDDIII") == [1, 2, 3, 9, 8, 7, 6, 5, 4, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDIDIDIDIDIDID") == [8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDIDIDIDIDIDID") == [8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIIIDDD") == [3, 2, 1, 4, 5, 6, 7, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIIIDDD") == [3, 2, 1, 4, 5, 6, 7, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIDIDIDIDID") == [6, 5, 4, 3, 2, 1, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIDIDIDIDID") == [6, 5, 4, 3, 2, 1, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIII") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIII") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDD") == [7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDD") == [7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDIIIDDIID") == [1, 5, 4, 3, 2, 6, 7, 10, 9, 8, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDIIIDDIID") == [1, 5, 4, 3, 2, 6, 7, 10, 9, 8, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDIIII") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDIIII") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDI") == [2, 1, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7, 13, 14, 15, 16, 22, 21, 20, 19, 18, 17, 23, 24, 25, 26, 32, 31, 30, 29, 28, 27, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDI") == [2, 1, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7, 13, 14, 15, 16, 22, 21, 20, 19, 18, 17, 23, 24, 25, 26, 32, 31, 30, 29, 28, 27, 33]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIDIDIDIDID") == [5, 4, 3, 2, 1, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIDIDIDIDID") == [5, 4, 3, 2, 1, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIIDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 13, 12, 11, 10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIIDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 13, 12, 11, 10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIDID") == [5, 4, 3, 2, 1, 6, 7, 9, 8, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIDID") == [5, 4, 3, 2, 1, 6, 7, 9, 8, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDD") == [1, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDD") == [1, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 16, 15, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 16, 15, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIDDDDDIIIID") == [3, 2, 1, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 16, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIDDDDDIIIID") == [3, 2, 1, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 16, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDI") == [3, 2, 1, 5, 4, 7, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDI") == [3, 2, 1, 5, 4, 7, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIDDIDDDD") == [3, 2, 1, 4, 7, 6, 5, 12, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIDDIDDDD") == [3, 2, 1, 4, 7, 6, 5, 12, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDD") == [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDD") == [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIDDDDDIDDDD") == [6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 17, 16, 15, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIDDDDDIDDDD") == [6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 17, 16, 15, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDIIID") == [1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDIIID") == [1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDDIIIIIII") == [1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 12, 13, 14, 15, 16, 17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDDIIIIIII") == [1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 12, 13, 14, 15, 16, 17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIIIIDDDIDDD") == [1, 2, 5, 4, 3, 6, 7, 8, 12, 11, 10, 9, 16, 15, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIIIIDDDIDDD") == [1, 2, 5, 4, 3, 6, 7, 8, 12, 11, 10, 9, 16, 15, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDII") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDII") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIII") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIII") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDID") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDID") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDIIIID") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDIIIID") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIDIDIDIDIDIDIDIDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIDIDIDIDIDIDIDIDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIIDDDDDDDDDDI") == [4, 3, 2, 1, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIIDDDDDDDDDDI") == [4, 3, 2, 1, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIDDDDDDD") == [1, 2, 3, 4, 12, 11, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIDDDDDDD") == [1, 2, 3, 4, 12, 11, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIII") == [1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIII") == [1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDIIIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDIIIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDIIDIDID") == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 13, 12, 15, 14, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDIIDIDID") == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 13, 12, 15, 14, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIIIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIIIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDIIIDDDII") == [3, 2, 1, 4, 5, 9, 8, 7, 6, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDIIIDDDII") == [3, 2, 1, 4, 5, 9, 8, 7, 6, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DIDIDIDIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DIDIDIDIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 21]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDIDIDIDIDID") == [1, 4, 3, 2, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDIDIDIDIDID") == [1, 4, 3, 2, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIIIIIIDDD") == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11, 12, 16, 15, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIIIIIIDDD") == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11, 12, 16, 15, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDIII") == [1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDIII") == [1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDIIDID") == [1, 2, 7, 6, 5, 4, 3, 8, 10, 9, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDIIDID") == [1, 2, 7, 6, 5, 4, 3, 8, 10, 9, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDDDDDDDDD") == [1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDDDDDDDDD") == [1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDIIIDDDD") == [4, 3, 2, 1, 5, 6, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDIIIDDDD") == [4, 3, 2, 1, 5, 6, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDIDDDIIDD") == [1, 2, 5, 4, 3, 9, 8, 7, 6, 10, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDIDDDIIDD") == [1, 2, 5, 4, 3, 9, 8, 7, 6, 10, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDD") == [1, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDD") == [1, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIDIDDDD") == [6, 5, 4, 3, 2, 1, 7, 9, 8, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIDIDDDD") == [6, 5, 4, 3, 2, 1, 7, 9, 8, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDIDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDIDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDDDDD") == [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDDDDD") == [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDIIIIIIIDDDD") == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11, 12, 17, 16, 15, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDIIIIIIIDDDD") == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11, 12, 17, 16, 15, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIDDDDDDD") == [1, 2, 3, 4, 5, 13, 12, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIDDDDDDD") == [1, 2, 3, 4, 5, 13, 12, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 28]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDDDDDDDDDDDDDDDI") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDDDDDDDDDDDDDDDI") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]: {e}')
    
    total += 1
    try:
        result = candidate(s = "DDDDIIIIIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 17, 16, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DDDDIIIIIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 17, 16, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IDIDDDDDDDDDDI") == [1, 3, 2, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IDIDDDDDDDDDDI") == [1, 3, 2, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 40]: {e}')
    
    total += 1
    try:
        result = candidate(s = "IIDDDDDDDDDDII") == [1, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IIDDDDDDDDDDII") == [1, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 14, 15]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "IIDIIIDIDDDDDIII") == [1, 2, 4, 3, 5, 6, 8, 7, 14, 13, 12, 11, 10, 9, 15, 16, 17]
    assert candidate(s = "DIDID") == [2, 1, 4, 3, 6, 5]
    assert candidate(s = "IDID") == [1, 3, 2, 5, 4]
    assert candidate(s = "DDDD") == [5, 4, 3, 2, 1]
    assert candidate(s = "I") == [1, 2]
    assert candidate(s = "DDIIIDD") == [3, 2, 1, 4, 5, 8, 7, 6]
    assert candidate(s = "DDI") == [3, 2, 1, 4]
    assert candidate(s = "IIII") == [1, 2, 3, 4, 5]
    assert candidate(s = "IID") == [1, 2, 4, 3]
    assert candidate(s = "IDDDI") == [1, 5, 4, 3, 2, 6]
    assert candidate(s = "IIDDDII") == [1, 2, 6, 5, 4, 3, 7, 8]
    assert candidate(s = "DIDD") == [2, 1, 5, 4, 3]
    assert candidate(s = "IDDI") == [1, 4, 3, 2, 5]
    assert candidate(s = "IIIDDDDDII") == [1, 2, 3, 9, 8, 7, 6, 5, 4, 10, 11]
    assert candidate(s = "DI") == [2, 1, 3]
    assert candidate(s = "DIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IDDDDDDDDDDDDD") == [1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "DDDDDIIDDDDIIDDD") == [6, 5, 4, 3, 2, 1, 7, 12, 11, 10, 9, 8, 13, 17, 16, 15, 14]
    assert candidate(s = "DDDDDDDDDDID") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12]
    assert candidate(s = "DIIDIDIDIDIDIDID") == [2, 1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]
    assert candidate(s = "IDIDDDIDIDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10, 13, 12, 15, 14]
    assert candidate(s = "DDDDIIIIII") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11]
    assert candidate(s = "DIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]
    assert candidate(s = "IDDDDDIIIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(s = "IDIDDDDDII") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 10, 11]
    assert candidate(s = "IDIDDDDDIIII") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 10, 11, 12, 13]
    assert candidate(s = "IIIIIIIIIIIDIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19, 20, 21]
    assert candidate(s = "IIDDDIIIIIDDDDD") == [1, 2, 6, 5, 4, 3, 7, 8, 9, 10, 16, 15, 14, 13, 12, 11]
    assert candidate(s = "IIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(s = "IDDDDDIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13]
    assert candidate(s = "IIIIIDIIIIIDII") == [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 13, 12, 14, 15]
    assert candidate(s = "IDDDIIDDDD") == [1, 5, 4, 3, 2, 6, 11, 10, 9, 8, 7]
    assert candidate(s = "IIIIIDDDID") == [1, 2, 3, 4, 5, 9, 8, 7, 6, 11, 10]
    assert candidate(s = "DDDIIDDDDDDI") == [4, 3, 2, 1, 5, 12, 11, 10, 9, 8, 7, 6, 13]
    assert candidate(s = "DDDDDDIDIDID") == [7, 6, 5, 4, 3, 2, 1, 9, 8, 11, 10, 13, 12]
    assert candidate(s = "IIDDIDDDIID") == [1, 2, 5, 4, 3, 9, 8, 7, 6, 10, 12, 11]
    assert candidate(s = "DDDDDDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDIDIDDDIDID") == [5, 4, 3, 2, 1, 7, 6, 11, 10, 9, 8, 13, 12, 15, 14]
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22]
    assert candidate(s = "DDDDDDDDID") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10]
    assert candidate(s = "IDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
    assert candidate(s = "IIDDDIIDID") == [1, 2, 6, 5, 4, 3, 7, 9, 8, 11, 10]
    assert candidate(s = "DDDDIDIDIDID") == [5, 4, 3, 2, 1, 7, 6, 9, 8, 11, 10, 13, 12]
    assert candidate(s = "DDDDDDDIIIIIIIII") == [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    assert candidate(s = "DDDDDDIDII") == [7, 6, 5, 4, 3, 2, 1, 9, 8, 10, 11]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDD") == [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IDDDDDDDIII") == [1, 9, 8, 7, 6, 5, 4, 3, 2, 10, 11, 12]
    assert candidate(s = "IDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]
    assert candidate(s = "IIIIIIIIIIIIIIIDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]
    assert candidate(s = "IDDDIIDID") == [1, 5, 4, 3, 2, 6, 8, 7, 10, 9]
    assert candidate(s = "IIIIIIIIIDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 14, 13, 12, 11, 10]
    assert candidate(s = "IIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(s = "IDDDDDDDDDDDDIIIIIIIIIIIIII") == [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    assert candidate(s = "DDDDDDDIDIDDDD") == [8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 15, 14, 13, 12, 11]
    assert candidate(s = "DIDIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 17]
    assert candidate(s = "DDDDDDDDDDDDDDDDIIIIIIIIIIIIIIII") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    assert candidate(s = "IIIIIIIDDDIIIIII") == [1, 2, 3, 4, 5, 6, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16, 17]
    assert candidate(s = "IIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]
    assert candidate(s = "IDDDDDIIID") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 11, 10]
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    assert candidate(s = "IDDDDDDDDDDDD") == [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "DDIIIIIIID") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 11, 10]
    assert candidate(s = "IIIIIDDDDDIIIIID") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 15, 17, 16]
    assert candidate(s = "IDIDDDDDDDDDIIII") == [1, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 14, 15, 16, 17]
    assert candidate(s = "DDIIDIDIDI") == [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 11]
    assert candidate(s = "IDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 14]
    assert candidate(s = "DDDIDIDDD") == [4, 3, 2, 1, 6, 5, 10, 9, 8, 7]
    assert candidate(s = "IDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
    assert candidate(s = "DDDDDDIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13]
    assert candidate(s = "IIIDDDIDDDI") == [1, 2, 3, 7, 6, 5, 4, 11, 10, 9, 8, 12]
    assert candidate(s = "IDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 12]
    assert candidate(s = "IDDDDDDDDIDDDDDD") == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 17, 16, 15, 14, 13, 12, 11]
    assert candidate(s = "IIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(s = "DIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15]
    assert candidate(s = "IDIDIDDDDD") == [1, 3, 2, 5, 4, 11, 10, 9, 8, 7, 6]
    assert candidate(s = "IIIDDDDDDIIIDDDD") == [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 11, 12, 17, 16, 15, 14, 13]
    assert candidate(s = "IIDDDIIDDD") == [1, 2, 6, 5, 4, 3, 7, 11, 10, 9, 8]
    assert candidate(s = "IDDDDDDDDDDDDDDD") == [1, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "DDDDDDDDDDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIDDDDDDIIII") == [1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]
    assert candidate(s = "DDDDDDI") == [7, 6, 5, 4, 3, 2, 1, 8]
    assert candidate(s = "DDDDDDDDDDDDDDID") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIIDDDDDDDDD") == [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IDIDDDIID") == [1, 3, 2, 7, 6, 5, 4, 8, 10, 9]
    assert candidate(s = "DIIIDDDIIDDID") == [2, 1, 3, 4, 8, 7, 6, 5, 9, 12, 11, 10, 14, 13]
    assert candidate(s = "IIDDDDD") == [1, 2, 8, 7, 6, 5, 4, 3]
    assert candidate(s = "IIDDDDDDDDDDDDDDDD") == [1, 2, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
    assert candidate(s = "DDDDDDDDDDDDDDDDD") == [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDIIDDIDID") == [3, 2, 1, 4, 7, 6, 5, 9, 8, 11, 10]
    assert candidate(s = "DDDDDDDDDDDDDDD") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDIDIDDD") == [5, 4, 3, 2, 1, 7, 6, 11, 10, 9, 8]
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23]
    assert candidate(s = "IIIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 2, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80]
    assert candidate(s = "DDDDDDDDD") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIIDDDDDDIIIIID") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 16, 18, 17]
    assert candidate(s = "IDDDDDIDDD") == [1, 7, 6, 5, 4, 3, 2, 11, 10, 9, 8]
    assert candidate(s = "IIDDIDDDDI") == [1, 2, 5, 4, 3, 10, 9, 8, 7, 6, 11]
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, 45, 48, 47, 50, 49, 52, 51, 54, 53, 56, 55, 58, 57, 60, 59, 62, 61, 64, 63, 66, 65, 68, 67, 70, 69, 72, 71, 74, 73, 76, 75, 78, 77, 80, 79, 82, 81]
    assert candidate(s = "IIDIDID") == [1, 2, 4, 3, 6, 5, 8, 7]
    assert candidate(s = "IDIDDDDDIDIDID") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 11, 10, 13, 12, 15, 14]
    assert candidate(s = "IDIDDDIDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10, 13, 12]
    assert candidate(s = "DDDIIIII") == [4, 3, 2, 1, 5, 6, 7, 8, 9]
    assert candidate(s = "IDDDDDDDDDDDDDID") == [1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 17, 16]
    assert candidate(s = "DDDDDDIIIIIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    assert candidate(s = "DDIIDDIIDDIID") == [3, 2, 1, 4, 7, 6, 5, 8, 11, 10, 9, 12, 14, 13]
    assert candidate(s = "IDIDDDDDDDDDDDDI") == [1, 3, 2, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 17]
    assert candidate(s = "IIDIDDDIID") == [1, 2, 4, 3, 8, 7, 6, 5, 9, 11, 10]
    assert candidate(s = "IIDDIDIDID") == [1, 2, 5, 4, 3, 7, 6, 9, 8, 11, 10]
    assert candidate(s = "IIDDDDIIDDDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 15, 14, 13, 12, 11, 10, 9]
    assert candidate(s = "IIIIIIIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    assert candidate(s = "IDDDIIDDDIIDDD") == [1, 5, 4, 3, 2, 6, 10, 9, 8, 7, 11, 15, 14, 13, 12]
    assert candidate(s = "IDIDDDIDID") == [1, 3, 2, 7, 6, 5, 4, 9, 8, 11, 10]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDD") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IDIDDDDDIDIDIDID") == [1, 3, 2, 9, 8, 7, 6, 5, 4, 11, 10, 13, 12, 15, 14, 17, 16]
    assert candidate(s = "DDDIIDDDDDDDDI") == [4, 3, 2, 1, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 15]
    assert candidate(s = "DDDDDDDDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDDDDDIDDD") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12, 11, 10]
    assert candidate(s = "IDIDDDDDDDDI") == [1, 3, 2, 12, 11, 10, 9, 8, 7, 6, 5, 4, 13]
    assert candidate(s = "IIIDDDIIIDDDIIID") == [1, 2, 3, 7, 6, 5, 4, 8, 9, 13, 12, 11, 10, 14, 15, 17, 16]
    assert candidate(s = "IDIDDDDDDDIIII") == [1, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 12, 13, 14, 15]
    assert candidate(s = "DDDDDDDDDDDIIIIIIIIIIIIIDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 31, 30, 29, 28, 27, 26, 25]
    assert candidate(s = "DDDDDDDDDDI") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]
    assert candidate(s = "DDDDDDDDDDDIDID") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 13, 16, 15]
    assert candidate(s = "IIDDDDIIDDDDDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26]
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]
    assert candidate(s = "DDDDDDDDDDIDDD") == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12]
    assert candidate(s = "IDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]
    assert candidate(s = "DDDDIIIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 15, 14, 13, 12]
    assert candidate(s = "IIIIIIIIIIIDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]
    assert candidate(s = "IDIDIDIDIDIDIDDD") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 17, 16, 15, 14]
    assert candidate(s = "IIIIIIIIIDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 12, 11, 10]
    assert candidate(s = "DDIIIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 15, 14, 13, 12, 11, 10]
    assert candidate(s = "IIIIIIIIIIIDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]
    assert candidate(s = "IIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
    assert candidate(s = "DDDDDDIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 13, 12]
    assert candidate(s = "IDDDDDIIIIIIIIII") == [1, 7, 6, 5, 4, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    assert candidate(s = "IIIIIIIIIIIIIDDDDDDDDDDDDIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 27, 28, 29, 30]
    assert candidate(s = "IIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]
    assert candidate(s = "IIIDIDIDIDIDIDIDIDIDID") == [1, 2, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]
    assert candidate(s = "IDDDDDDDDDDIDDDDDDDDDIDDDDDDDDD") == [1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]
    assert candidate(s = "DDDDDDIIIIIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(s = "IIIIIDDDDDDDDDDD") == [1, 2, 3, 4, 5, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    assert candidate(s = "IIDDIDIDIDIDID") == [1, 2, 5, 4, 3, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
    assert candidate(s = "IIIIIDDDDDDDDIIII") == [1, 2, 3, 4, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 15, 16, 17, 18]
    assert candidate(s = "DDDDDDDDDDDDIIIIIIIIII") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    assert candidate(s = "IIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29]
    assert candidate(s = "IIIIIIIDIDID") == [1, 2, 3, 4, 5, 6, 7, 9, 8, 11, 10, 13, 12]
    assert candidate(s = "IDDDDDIDID") == [1, 7, 6, 5, 4, 3, 2, 9, 8, 11, 10]
    assert candidate(s = "IDDDIDIDIDIDI") == [1, 5, 4, 3, 2, 7, 6, 9, 8, 11, 10, 13, 12, 14]
    assert candidate(s = "IIDDDDDDIIIIIIIII") == [1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert candidate(s = "DIIDIIDIDI") == [2, 1, 3, 5, 4, 6, 8, 7, 10, 9, 11]
    assert candidate(s = "DDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58]
    assert candidate(s = "IIIIIDDDDDDDDDD") == [1, 2, 3, 4, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    assert candidate(s = "IIIIIDDDDDDIIIIIDDDDDDIIIIIDDDDD") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 16, 23, 22, 21, 20, 19, 18, 17, 24, 25, 26, 27, 33, 32, 31, 30, 29, 28]
    assert candidate(s = "DIIIIIIIIIIID") == [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    assert candidate(s = "IIIIIDDDDD") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6]
    assert candidate(s = "IDDDIIDDDIIDDDIID") == [1, 5, 4, 3, 2, 6, 10, 9, 8, 7, 11, 15, 14, 13, 12, 16, 18, 17]
    assert candidate(s = "IDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]
    assert candidate(s = "DDDDIIDDDD") == [5, 4, 3, 2, 1, 6, 11, 10, 9, 8, 7]
    assert candidate(s = "IDDDDDDDDDDD") == [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "DDIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8]
    assert candidate(s = "DDDDDDIIIIIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIIIII") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    assert candidate(s = "DDDIIDDDDI") == [4, 3, 2, 1, 5, 10, 9, 8, 7, 6, 11]
    assert candidate(s = "IIIDDDDDIII") == [1, 2, 3, 9, 8, 7, 6, 5, 4, 10, 11, 12]
    assert candidate(s = "IDIDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 16]
    assert candidate(s = "DDDDDDDIDIDIDIDIDID") == [8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72]
    assert candidate(s = "DDIIIIIDDD") == [3, 2, 1, 4, 5, 6, 7, 11, 10, 9, 8]
    assert candidate(s = "DDDDDIDIDIDIDID") == [6, 5, 4, 3, 2, 1, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD") == [65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DIDIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDIIIIIIIIIIIIIIIIII") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
    assert candidate(s = "DDDDDD") == [7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IDDDIIIDDIID") == [1, 5, 4, 3, 2, 6, 7, 10, 9, 8, 11, 13, 12]
    assert candidate(s = "DDIDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]
    assert candidate(s = "IIIIIDDDDDIIII") == [1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 15]
    assert candidate(s = "IIIIIIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert candidate(s = "DIIIIIDDDDDIIIIIDDDDDIIIIIDDDDDI") == [2, 1, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7, 13, 14, 15, 16, 22, 21, 20, 19, 18, 17, 23, 24, 25, 26, 32, 31, 30, 29, 28, 27, 33]
    assert candidate(s = "DDDDIDIDIDIDID") == [5, 4, 3, 2, 1, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
    assert candidate(s = "DIDIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]
    assert candidate(s = "IIDDDDIIDDDD") == [1, 2, 7, 6, 5, 4, 3, 8, 13, 12, 11, 10, 9]
    assert candidate(s = "DIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 11]
    assert candidate(s = "DDDDIIIDID") == [5, 4, 3, 2, 1, 6, 7, 9, 8, 11, 10]
    assert candidate(s = "IDIDDDDDDD") == [1, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4]
    assert candidate(s = "IIIIIIIIIDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 16, 15, 14, 13, 12, 11, 10]
    assert candidate(s = "DDIIIDDDDDIIIID") == [3, 2, 1, 4, 5, 11, 10, 9, 8, 7, 6, 12, 13, 14, 16, 15]
    assert candidate(s = "DDIDIDI") == [3, 2, 1, 5, 4, 7, 6, 8]
    assert candidate(s = "DDIIDDIDDDD") == [3, 2, 1, 4, 7, 6, 5, 12, 11, 10, 9, 8]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDID") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDDDDDD") == [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDDIDDDDDIDDDD") == [6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 17, 16, 15, 14, 13]
    assert candidate(s = "DDDDDDDDDDDDD") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIDDDDDIIID") == [1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 12, 11]
    assert candidate(s = "IDDDDDDDDDIIIIIII") == [1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 12, 13, 14, 15, 16, 17, 18]
    assert candidate(s = "IIDDIIIIDDDIDDD") == [1, 2, 5, 4, 3, 6, 7, 8, 12, 11, 10, 9, 16, 15, 14, 13]
    assert candidate(s = "IIIIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(s = "DDDDDDIIII") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11]
    assert candidate(s = "DDDDDDDDDDDDDDII") == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17]
    assert candidate(s = "DIDIDIDIDIDIDIII") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15, 16, 17]
    assert candidate(s = "DDDDDDDDDDDDID") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14]
    assert candidate(s = "DIDIDIDIDID") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]
    assert candidate(s = "IIIIIDDDDDDIIIID") == [1, 2, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6, 13, 14, 15, 17, 16]
    assert candidate(s = "DDIDIDIDIDIDIDIDIDIDIDIDID") == [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26]
    assert candidate(s = "DDDIIDDDDDDDDDDI") == [4, 3, 2, 1, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 17]
    assert candidate(s = "IIIIDDDDDDD") == [1, 2, 3, 4, 12, 11, 10, 9, 8, 7, 6, 5]
    assert candidate(s = "DDDDDDDDDDD") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "IIIIII") == [1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "DDDDDDIIIIIIID") == [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 15, 14]
    assert candidate(s = "IDDDDDDDDIIDIDID") == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 13, 12, 15, 14, 17, 16]
    assert candidate(s = "DDIIIIIIIIIDDDDD") == [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 17, 16, 15, 14, 13, 12]
    assert candidate(s = "DDIIIDDDII") == [3, 2, 1, 4, 5, 9, 8, 7, 6, 10, 11]
    assert candidate(s = "DIDIDIDIDIDIDIDIDIDI") == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 21]
    assert candidate(s = "IDDIDIDIDIDID") == [1, 4, 3, 2, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]
    assert candidate(s = "DDDDDIIIIIIIDDD") == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11, 12, 16, 15, 14, 13]
    assert candidate(s = "IIDDDDDIII") == [1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11]
    assert candidate(s = "DDDDDDDDDDDDDIIIIIIIIIIIII") == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    assert candidate(s = "IIDDDDIIDID") == [1, 2, 7, 6, 5, 4, 3, 8, 10, 9, 12, 11]
    assert candidate(s = "IDDDDDDDDD") == [1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(s = "IIIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12]
    assert candidate(s = "DDDIIIDDDD") == [4, 3, 2, 1, 5, 6, 11, 10, 9, 8, 7]
    assert candidate(s = "IIDDIDDDIIDD") == [1, 2, 5, 4, 3, 9, 8, 7, 6, 10, 13, 12, 11]
    assert candidate(s = "IIDDDDDDDD") == [1, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3]
    assert candidate(s = "IIIIIIIII") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(s = "DDDDDIIDIDDDD") == [6, 5, 4, 3, 2, 1, 7, 9, 8, 14, 13, 12, 11, 10]
    assert candidate(s = "DDDDIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 13, 12, 11, 10]
    assert candidate(s = "DDDDDDDDDDDDIDDD") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 15, 14]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDDDDD") == [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(s = "DDDDDIIIIIIIDDDD") == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11, 12, 17, 16, 15, 14, 13]
    assert candidate(s = "IIIIIDDDDDDD") == [1, 2, 3, 4, 5, 13, 12, 11, 10, 9, 8, 7, 6]
    assert candidate(s = "IIIIIIIDDDDDDDDD") == [1, 2, 3, 4, 5, 6, 7, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8]
    assert candidate(s = "IDIDIDIDIDIDIDIDIDIDIDIDIDI") == [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 28]
    assert candidate(s = "DDDDDDDDDDDDDDDDDDI") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]
    assert candidate(s = "DDDDIIIIIIIIIDDD") == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 17, 16, 15, 14]
    assert candidate(s = "IDIDDDDDDDDDDI") == [1, 3, 2, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 15]
    assert candidate(s = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 40]
    assert candidate(s = "IIDDDDDDDDDDII") == [1, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 14, 15]


