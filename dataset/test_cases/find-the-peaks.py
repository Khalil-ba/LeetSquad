def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 6, 7, 8, 9, 10, 8, 6, 4]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 6, 7, 8, 9, 10, 8, 6, 4]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 4, 4]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 4, 4]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 10, 20, 10]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 10, 20, 10]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [7, 6, 5, 4, 3, 2, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [7, 6, 5, 4, 3, 2, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 4, 3, 8, 5]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 4, 3, 8, 5]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 1, 2, 3, 1]) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 1, 2, 3, 1]) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 6, 5]) == [1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 6, 5]) == [1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 2, 1, 4, 3, 2, 1]) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 2, 1, 4, 3, 2, 1]) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 1]) == [1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 1]) == [1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [2, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [2, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 1, 3, 1]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 1, 3, 1]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 1]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 1]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4]) == [1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4]) == [1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 4, 3, 2, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 4, 3, 2, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [50, 40, 30, 20, 10, 20, 30, 20, 10, 20, 30, 20, 10, 20, 30]) == [6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [50, 40, 30, 20, 10, 20, 30, 20, 10, 20, 30, 20, 10, 20, 30]) == [6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 25, 20, 30, 25, 35, 30]) == [1, 3, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 25, 20, 30, 25, 35, 30]) == [1, 3, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [8, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11, 14, 12, 15, 13, 16, 14, 17, 15, 18, 16, 19, 17]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [8, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11, 14, 12, 15, 13, 16, 14, 17, 15, 18, 16, 19, 17]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12, 11, 13, 14, 13, 15, 16, 15]) == [1, 4, 7, 10, 13, 16, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12, 11, 13, 14, 13, 15, 16, 15]) == [1, 4, 7, 10, 13, 16, 19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 1, 3, 5, 7, 9, 2, 6, 5, 3, 5, 9]) == [2, 5, 7, 11, 13, 17, 19, 21, 29, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 1, 3, 5, 7, 9, 2, 6, 5, 3, 5, 9]) == [2, 5, 7, 11, 13, 17, 19, 21, 29, 31]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12, 11, 13, 14, 13, 15, 16, 15, 17, 18, 17]) == [5, 8, 11, 14, 17, 20, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12, 11, 13, 14, 13, 15, 16, 15, 17, 18, 17]) == [5, 8, 11, 14, 17, 20, 23]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 27]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 25, 30, 5, 35, 40, 38, 45, 50]) == [1, 4, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 25, 30, 5, 35, 40, 38, 45, 50]) == [1, 4, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30]) == [4, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30]) == [4, 12]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == [3, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == [3, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == [1, 3, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == [1, 3, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5, 3]) == [5, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5, 3]) == [5, 15]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [2, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [2, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3]) == [1, 3, 5, 7, 9, 11, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3]) == [1, 3, 5, 7, 9, 11, 13]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40]) == [1, 3, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40]) == [1, 3, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 3, 1, 2, 4, 6, 5, 4, 3, 5, 7, 9, 7, 5, 6, 8, 6, 4, 3, 2]) == [5, 11, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 3, 1, 2, 4, 6, 5, 4, 3, 5, 7, 9, 7, 5, 6, 8, 6, 4, 3, 2]) == [5, 11, 15]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == [1, 3, 5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == [1, 3, 5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [1, 3, 5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [1, 3, 5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [6, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11, 14, 12, 15, 13, 16, 14, 17, 15]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [6, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11, 14, 12, 15, 13, 16, 14, 17, 15]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 6]) == [2, 5, 7, 11, 13, 17, 19, 21, 25, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 6]) == [2, 5, 7, 11, 13, 17, 19, 21, 25, 29]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 4, 3, 5, 6, 4, 7, 8, 6, 9, 10, 7, 11, 12, 9, 13, 14, 11, 15, 16, 12, 17, 18, 13]) == [1, 4, 7, 10, 13, 16, 19, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 4, 3, 5, 6, 4, 7, 8, 6, 9, 10, 7, 11, 12, 9, 13, 14, 11, 15, 16, 12, 17, 18, 13]) == [1, 4, 7, 10, 13, 16, 19, 22]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 2, 1]) == [4, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 2, 1]) == [4, 10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [8, 9, 7, 10, 6, 11, 5, 12, 4, 13, 3]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [8, 9, 7, 10, 6, 11, 5, 12, 4, 13, 3]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5]) == [4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5]) == [4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 8, 7, 9, 8, 7, 6]) == [1, 3, 5, 7, 9, 11, 13, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 8, 7, 9, 8, 7, 6]) == [1, 3, 5, 7, 9, 11, 13, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 1, 4, 1, 6, 1, 8, 1, 10, 1, 12, 1, 14, 1, 16, 1, 18, 1]) == [2, 4, 6, 8, 10, 12, 14, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 1, 4, 1, 6, 1, 8, 1, 10, 1, 12, 1, 14, 1, 16, 1, 18, 1]) == [2, 4, 6, 8, 10, 12, 14, 16]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [2, 7, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [2, 7, 14]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == [3, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == [3, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [2, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [2, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 4, 6, 8, 10, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 4, 6, 8, 10, 12]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == [17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == [17]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [1, 3, 5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [1, 3, 5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 25, 30, 28, 35, 40, 38, 45, 43]) == [1, 4, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 25, 30, 28, 35, 40, 38, 45, 43]) == [1, 4, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [2, 5, 8, 11, 14, 17, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [2, 5, 8, 11, 14, 17, 20]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == [2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == [2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 30, 25, 40, 35]) == [1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 30, 25, 40, 35]) == [1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7]) == [1, 3, 5, 7, 9, 11, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7]) == [1, 3, 5, 7, 9, 11, 13]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == [2, 4, 6, 8, 10, 12, 14, 16, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == [2, 4, 6, 8, 10, 12, 14, 16, 18]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [1, 3, 5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [1, 3, 5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 30, 25, 35, 40, 20, 50, 45]) == [1, 3, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 30, 25, 35, 40, 20, 50, 45]) == [1, 3, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 8, 9, 8, 7, 6, 5]) == [8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 8, 9, 8, 7, 6, 5]) == [8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == [4, 6, 8, 10, 12, 14, 16, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == [4, 6, 8, 10, 12, 14, 16, 18]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]) == [1, 7, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]) == [1, 7, 13]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 3, 8, 6, 7, 2, 9, 4, 10, 1, 11]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 3, 8, 6, 7, 2, 9, 4, 10, 1, 11]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9, 15, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9, 15, 21]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [4, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [4, 11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 8, 7]) == [1, 3, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 8, 7]) == [1, 3, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 5, 4, 7, 6]) == [1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 5, 4, 7, 6]) == [1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 10, 12, 11, 13, 14, 12, 15, 16, 14, 17, 18, 16]) == [2, 5, 7, 12, 15, 18, 21, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 10, 12, 11, 13, 14, 12, 15, 16, 14, 17, 18, 16]) == [2, 5, 7, 12, 15, 18, 21, 24]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6]) == [4, 8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6]) == [4, 8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [16]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1]) == [1, 3, 5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1]) == [1, 3, 5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [2, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [2, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]) == [2, 6, 10, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]) == [2, 6, 10, 14]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 3, 4, 3, 5, 3, 5, 7, 5, 8, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11]) == [2, 4, 7, 9, 11, 13, 15, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 3, 4, 3, 5, 3, 5, 7, 5, 8, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11]) == [2, 4, 7, 9, 11, 13, 15, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == [1, 3, 5, 7, 9, 11, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == [1, 3, 5, 7, 9, 11, 13]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [1, 4, 7, 10, 13, 16, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [1, 4, 7, 10, 13, 16, 19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 25, 30, 20, 50, 45, 60, 55]) == [1, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 25, 30, 20, 50, 45, 60, 55]) == [1, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [10, 20, 15, 25, 30, 20, 35, 40, 50, 45]) == [1, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [10, 20, 15, 25, 30, 20, 35, 40, 50, 45]) == [1, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4, 12, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4, 12, 20]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [1, 3, 5, 7, 9, 11, 13, 15, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [1, 3, 5, 7, 9, 11, 13, 15, 17]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == [1, 3, 5, 7, 9, 11, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == [1, 3, 5, 7, 9, 11, 13]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [4, 8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [4, 8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [1, 3, 2, 4, 1, 5, 4, 6, 1]) == [1, 3, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [1, 3, 2, 4, 1, 5, 4, 6, 1]) == [1, 3, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 1, 3, 5, 7, 9, 2, 6, 5, 3, 5, 9, 1, 3, 4, 6, 5, 4, 3, 2, 1, 2, 3]) == [2, 5, 7, 11, 13, 17, 19, 21, 29, 31, 35, 39]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 1, 3, 5, 7, 9, 2, 6, 5, 3, 5, 9, 1, 3, 4, 6, 5, 4, 3, 2, 1, 2, 3]) == [2, 5, 7, 11, 13, 17, 19, 21, 29, 31, 35, 39]: {e}')
    
    total += 1
    try:
        result = candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mountain = [1, 2, 3, 4, 5]) == []
    assert candidate(mountain = [5, 6, 7, 8, 9, 10, 8, 6, 4]) == [5]
    assert candidate(mountain = [2, 4, 4]) == []
    assert candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4]
    assert candidate(mountain = [10, 20, 10, 20, 10]) == [1, 3]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7]) == []
    assert candidate(mountain = [7, 6, 5, 4, 3, 2, 1]) == []
    assert candidate(mountain = [1, 4, 3, 8, 5]) == [1, 3]
    assert candidate(mountain = [1, 2, 3, 1, 2, 3, 1]) == [2, 5]
    assert candidate(mountain = [1, 3, 2, 4, 3, 6, 5]) == [1, 3, 5]
    assert candidate(mountain = [3, 2, 1, 4, 3, 2, 1]) == [3]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 1]) == [1, 3, 5]
    assert candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [2, 5, 7]
    assert candidate(mountain = [1, 3, 1, 3, 1]) == [1, 3]
    assert candidate(mountain = [1, 3, 2, 1]) == [1]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4]) == [1, 3, 5]
    assert candidate(mountain = [5, 4, 3, 2, 1]) == []
    assert candidate(mountain = [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10]) == []
    assert candidate(mountain = [50, 40, 30, 20, 10, 20, 30, 20, 10, 20, 30, 20, 10, 20, 30]) == [6, 10]
    assert candidate(mountain = [10, 20, 15, 25, 20, 30, 25, 35, 30]) == [1, 3, 5, 7]
    assert candidate(mountain = [8, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11, 14, 12, 15, 13, 16, 14, 17, 15, 18, 16, 19, 17]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    assert candidate(mountain = [3, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12, 11, 13, 14, 13, 15, 16, 15]) == [1, 4, 7, 10, 13, 16, 19]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == [1, 3, 5, 7, 9]
    assert candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 1, 3, 5, 7, 9, 2, 6, 5, 3, 5, 9]) == [2, 5, 7, 11, 13, 17, 19, 21, 29, 31]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12, 11, 13, 14, 13, 15, 16, 15, 17, 18, 17]) == [5, 8, 11, 14, 17, 20, 23]
    assert candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 27]
    assert candidate(mountain = [10, 20, 15, 25, 30, 5, 35, 40, 38, 45, 50]) == [1, 4, 7]
    assert candidate(mountain = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30]) == [4, 12]
    assert candidate(mountain = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == [3, 8]
    assert candidate(mountain = [5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == [1, 3, 5, 7, 9]
    assert candidate(mountain = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [9]
    assert candidate(mountain = [3, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == [1, 3, 5, 7]
    assert candidate(mountain = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5, 3]) == [5, 15]
    assert candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [2, 5, 7]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3]) == [1, 3, 5, 7, 9, 11, 13]
    assert candidate(mountain = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40]) == [1, 3, 5, 7]
    assert candidate(mountain = [5, 3, 1, 2, 4, 6, 5, 4, 3, 5, 7, 9, 7, 5, 6, 8, 6, 4, 3, 2]) == [5, 11, 15]
    assert candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 4, 6, 8]
    assert candidate(mountain = [3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == [1, 3, 5, 7, 9, 11]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [1, 3, 5, 7, 9, 11]
    assert candidate(mountain = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5]) == [2, 4, 6, 8]
    assert candidate(mountain = [6, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11, 14, 12, 15, 13, 16, 14, 17, 15]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    assert candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9]
    assert candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 6]) == [2, 5, 7, 11, 13, 17, 19, 21, 25, 29]
    assert candidate(mountain = [2, 4, 3, 5, 6, 4, 7, 8, 6, 9, 10, 7, 11, 12, 9, 13, 14, 11, 15, 16, 12, 17, 18, 13]) == [1, 4, 7, 10, 13, 16, 19, 22]
    assert candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 6, 10]
    assert candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 2, 1]) == [4, 10]
    assert candidate(mountain = [8, 9, 7, 10, 6, 11, 5, 12, 4, 13, 3]) == [1, 3, 5, 7, 9]
    assert candidate(mountain = [5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5]) == [4, 8]
    assert candidate(mountain = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 8, 7, 9, 8, 7, 6]) == [1, 3, 5, 7, 9, 11, 13, 17, 19]
    assert candidate(mountain = [2, 1, 4, 1, 6, 1, 8, 1, 10, 1, 12, 1, 14, 1, 16, 1, 18, 1]) == [2, 4, 6, 8, 10, 12, 14, 16]
    assert candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [2, 7, 14]
    assert candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == [3, 9]
    assert candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [2, 6, 10]
    assert candidate(mountain = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25]) == [9]
    assert candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 4, 6, 8, 10, 12]
    assert candidate(mountain = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == [17]
    assert candidate(mountain = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [1, 3, 5, 7, 9, 11]
    assert candidate(mountain = [10, 20, 15, 25, 30, 28, 35, 40, 38, 45, 43]) == [1, 4, 7, 9]
    assert candidate(mountain = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [2, 5, 8, 11, 14, 17, 20]
    assert candidate(mountain = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == [2, 4, 6, 8, 10]
    assert candidate(mountain = [10, 20, 15, 30, 25, 40, 35]) == [1, 3, 5]
    assert candidate(mountain = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5]) == [8]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7]) == [1, 3, 5, 7, 9, 11, 13]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
    assert candidate(mountain = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == [2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3]) == [6]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [1, 3, 5, 7, 9, 11]
    assert candidate(mountain = [10, 20, 15, 30, 25, 35, 40, 20, 50, 45]) == [1, 3, 6, 8]
    assert candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == [1, 3, 5, 7, 9]
    assert candidate(mountain = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 8, 9, 8, 7, 6, 5]) == [8, 12]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9]
    assert candidate(mountain = [7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
    assert candidate(mountain = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == [4, 6, 8, 10, 12, 14, 16, 18]
    assert candidate(mountain = [1, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]) == [1, 7, 13]
    assert candidate(mountain = [5, 3, 8, 6, 7, 2, 9, 4, 10, 1, 11]) == [2, 4, 6, 8]
    assert candidate(mountain = [2, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8]) == [2, 4, 6, 8]
    assert candidate(mountain = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [3, 9, 15, 21]
    assert candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert candidate(mountain = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [8]
    assert candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [4, 11]
    assert candidate(mountain = [1, 3, 2, 5, 4, 7, 6, 8, 7]) == [1, 3, 5, 7]
    assert candidate(mountain = [1, 3, 2, 5, 4, 7, 6]) == [1, 3, 5]
    assert candidate(mountain = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13]) == [2, 4, 6, 8]
    assert candidate(mountain = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 10, 12, 11, 13, 14, 12, 15, 16, 14, 17, 18, 16]) == [2, 5, 7, 12, 15, 18, 21, 24]
    assert candidate(mountain = [8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6]) == [4, 8, 12]
    assert candidate(mountain = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [16]
    assert candidate(mountain = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1]) == [1, 3, 5, 7, 9, 11]
    assert candidate(mountain = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [2, 6, 10]
    assert candidate(mountain = [2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]) == [2, 6, 10, 14]
    assert candidate(mountain = [5, 3, 4, 3, 5, 3, 5, 7, 5, 8, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11]) == [2, 4, 7, 9, 11, 13, 15, 17, 19]
    assert candidate(mountain = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10]
    assert candidate(mountain = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == [5]
    assert candidate(mountain = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    assert candidate(mountain = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []
    assert candidate(mountain = [1, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == [1, 3, 5, 7, 9, 11, 13]
    assert candidate(mountain = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [1, 4, 7, 10, 13, 16, 19]
    assert candidate(mountain = [10, 20, 15, 25, 30, 20, 50, 45, 60, 55]) == [1, 4, 6, 8]
    assert candidate(mountain = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1]) == [6]
    assert candidate(mountain = [10, 20, 15, 25, 30, 20, 35, 40, 50, 45]) == [1, 4, 8]
    assert candidate(mountain = [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == [6]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == [6]
    assert candidate(mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19]
    assert candidate(mountain = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11]
    assert candidate(mountain = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4, 12, 20]
    assert candidate(mountain = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [15]
    assert candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == [1, 3, 5, 7, 9]
    assert candidate(mountain = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [1, 3, 5, 7, 9, 11, 13, 15, 17]
    assert candidate(mountain = [5, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == [1, 3, 5, 7, 9, 11, 13]
    assert candidate(mountain = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [4, 8, 12]
    assert candidate(mountain = [1, 3, 2, 4, 1, 5, 4, 6, 1]) == [1, 3, 5, 7]
    assert candidate(mountain = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 1, 3, 5, 7, 9, 2, 6, 5, 3, 5, 9, 1, 3, 4, 6, 5, 4, 3, 2, 1, 2, 3]) == [2, 5, 7, 11, 13, 17, 19, 21, 29, 31, 35, 39]
    assert candidate(mountain = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


