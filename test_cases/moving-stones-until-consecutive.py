def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 7,b = 8,c = 10) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 8,c = 10) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 100,c = 50) == [2, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 100,c = 50) == [2, 97]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 3,c = 100) == [1, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 3,c = 100) == [1, 97]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 12,c = 14) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 12,c = 14) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 51,c = 53) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 51,c = 53) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 27,c = 30) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 27,c = 30) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 6,c = 8) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 6,c = 8) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 9,c = 8) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 9,c = 8) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 5,c = 7) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 5,c = 7) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 1,c = 3) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 1,c = 3) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 8,c = 15) == [2, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 8,c = 15) == [2, 11]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,c = 5) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,c = 5) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 25,c = 30) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 25,c = 30) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 17,c = 20) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 17,c = 20) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 5,c = 1) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 5,c = 1) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 7,c = 10) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 7,c = 10) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 6,c = 5) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 6,c = 5) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 13,c = 11) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 13,c = 11) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 10,c = 15) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 10,c = 15) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 20,c = 30) == [2, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 20,c = 30) == [2, 18]: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 1,c = 50) == [2, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 1,c = 50) == [2, 97]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 6,c = 9) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 6,c = 9) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 28,c = 30) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 28,c = 30) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 3,c = 4) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 3,c = 4) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 3,c = 6) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 3,c = 6) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 4,c = 5) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 4,c = 5) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 13,c = 17) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 13,c = 17) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 3,c = 2) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 3,c = 2) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 18,c = 20) == [1, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 18,c = 20) == [1, 16]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 10,c = 20) == [2, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 10,c = 20) == [2, 17]: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 35,c = 40) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 35,c = 40) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 5,c = 9) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 5,c = 9) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 50,c = 100) == [2, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 50,c = 100) == [2, 97]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 12,c = 25) == [1, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 12,c = 25) == [1, 13]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 8,c = 12) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 8,c = 12) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 11,c = 20) == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 11,c = 20) == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(a = 23,b = 24,c = 26) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 23,b = 24,c = 26) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 3,c = 7) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 3,c = 7) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 10,c = 13) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 10,c = 13) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 11,c = 20) == [2, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 11,c = 20) == [2, 15]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 12,c = 17) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 12,c = 17) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 13,b = 16,c = 20) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 13,b = 16,c = 20) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 22,c = 26) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 22,c = 26) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 3,c = 8) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 3,c = 8) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 10,c = 14) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 10,c = 14) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 98,b = 99,c = 100) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 98,b = 99,c = 100) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 15,c = 25) == [2, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 15,c = 25) == [2, 18]: {e}')
    
    total += 1
    try:
        result = candidate(a = 35,b = 40,c = 45) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 35,b = 40,c = 45) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 5,c = 8) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 5,c = 8) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 6,c = 9) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 6,c = 9) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 9,c = 14) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 9,c = 14) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 10,c = 12) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 10,c = 12) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 10,c = 15) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 10,c = 15) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 10,c = 15) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 10,c = 15) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 32,c = 34) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 32,c = 34) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 6,c = 10) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 6,c = 10) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 4,c = 7) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 4,c = 7) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 9,c = 12) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 9,c = 12) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 20,c = 25) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 20,c = 25) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 13,c = 18) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 13,c = 18) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 23,b = 26,c = 29) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 23,b = 26,c = 29) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 40,b = 41,c = 43) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 40,b = 41,c = 43) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 9,c = 12) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 9,c = 12) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 3,c = 6) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 3,c = 6) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 4,c = 100) == [2, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 4,c = 100) == [2, 97]: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 7,c = 12) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 7,c = 12) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 10,c = 14) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 10,c = 14) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 11,c = 14) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 11,c = 14) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 5,c = 10) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 5,c = 10) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 25,c = 35) == [2, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 25,c = 35) == [2, 18]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 15,c = 25) == [2, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 15,c = 25) == [2, 13]: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 21,c = 26) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 21,c = 26) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 8,c = 11) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 8,c = 11) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 8,c = 14) == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 8,c = 14) == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 7,c = 14) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 7,c = 14) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 30,c = 40) == [2, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 30,c = 40) == [2, 13]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 6,c = 11) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 6,c = 11) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 35,c = 40) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 35,c = 40) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 3,c = 10) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 3,c = 10) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 4,c = 8) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 4,c = 8) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 7,c = 11) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 7,c = 11) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 13,c = 16) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 13,c = 16) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 20,c = 40) == [2, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 20,c = 40) == [2, 23]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 6,c = 9) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 6,c = 9) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 21,b = 24,c = 28) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 21,b = 24,c = 28) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 90,b = 95,c = 100) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 90,b = 95,c = 100) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 20,c = 25) == [2, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 20,c = 25) == [2, 13]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 7,c = 11) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 7,c = 11) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 8,c = 10) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 8,c = 10) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 11,c = 14) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 11,c = 14) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 12,b = 14,c = 20) == [1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 12,b = 14,c = 20) == [1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 31,c = 34) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 31,c = 34) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 11,c = 17) == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 11,c = 17) == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 99,c = 97) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 99,c = 97) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 5,c = 10) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 5,c = 10) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 7,c = 11) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 7,c = 11) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,c = 4) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,c = 4) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 5,c = 9) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 5,c = 9) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 7,c = 10) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 7,c = 10) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 8,c = 13) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 8,c = 13) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 17,c = 25) == [1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 17,c = 25) == [1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 9,c = 18) == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 9,c = 18) == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 8,c = 14) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 8,c = 14) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 6,c = 8) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 6,c = 8) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 17,b = 20,c = 23) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 17,b = 20,c = 23) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 32,c = 40) == [1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 32,c = 40) == [1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 10,c = 13) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 10,c = 13) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 4,c = 10) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 4,c = 10) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 8,c = 15) == [1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 8,c = 15) == [1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 14,c = 21) == [2, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 14,c = 21) == [2, 12]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 15,c = 20) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 15,c = 20) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 6,c = 9) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 6,c = 9) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 22,c = 30) == [1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 22,c = 30) == [1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 14,c = 17) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 14,c = 17) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 12,c = 22) == [2, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 12,c = 22) == [2, 12]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 11,c = 15) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 11,c = 15) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 15,c = 3) == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 15,c = 3) == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 8,c = 9) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 8,c = 9) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(a = 45,b = 50,c = 55) == [2, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 45,b = 50,c = 55) == [2, 8]: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 6,c = 8) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 6,c = 8) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 9,c = 15) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 9,c = 15) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 5,c = 7) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 5,c = 7) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,c = 3) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,c = 3) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 52,c = 55) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 52,c = 55) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 11,c = 25) == [2, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 11,c = 25) == [2, 16]: {e}')
    
    total += 1
    try:
        result = candidate(a = 9,b = 11,c = 13) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 9,b = 11,c = 13) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 30,c = 50) == [2, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 30,c = 50) == [2, 23]: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 14,c = 18) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 14,c = 18) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 99,c = 100) == [1, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 99,c = 100) == [1, 96]: {e}')
    
    total += 1
    try:
        result = candidate(a = 23,b = 27,c = 31) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 23,b = 27,c = 31) == [2, 6]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 7,b = 8,c = 10) == [1, 1]
    assert candidate(a = 1,b = 100,c = 50) == [2, 97]
    assert candidate(a = 1,b = 3,c = 100) == [1, 97]
    assert candidate(a = 10,b = 12,c = 14) == [1, 2]
    assert candidate(a = 50,b = 51,c = 53) == [1, 1]
    assert candidate(a = 25,b = 27,c = 30) == [1, 3]
    assert candidate(a = 5,b = 6,c = 8) == [1, 1]
    assert candidate(a = 10,b = 9,c = 8) == [0, 0]
    assert candidate(a = 2,b = 5,c = 7) == [1, 3]
    assert candidate(a = 7,b = 1,c = 3) == [1, 4]
    assert candidate(a = 2,b = 8,c = 15) == [2, 11]
    assert candidate(a = 1,b = 2,c = 5) == [1, 2]
    assert candidate(a = 20,b = 25,c = 30) == [2, 8]
    assert candidate(a = 15,b = 17,c = 20) == [1, 3]
    assert candidate(a = 3,b = 5,c = 1) == [1, 2]
    assert candidate(a = 2,b = 7,c = 10) == [2, 6]
    assert candidate(a = 2,b = 6,c = 5) == [1, 2]
    assert candidate(a = 15,b = 13,c = 11) == [1, 2]
    assert candidate(a = 5,b = 10,c = 15) == [2, 8]
    assert candidate(a = 10,b = 20,c = 30) == [2, 18]
    assert candidate(a = 100,b = 1,c = 50) == [2, 97]
    assert candidate(a = 3,b = 6,c = 9) == [2, 4]
    assert candidate(a = 25,b = 28,c = 30) == [1, 3]
    assert candidate(a = 2,b = 3,c = 4) == [0, 0]
    assert candidate(a = 1,b = 3,c = 6) == [1, 3]
    assert candidate(a = 3,b = 4,c = 5) == [0, 0]
    assert candidate(a = 8,b = 13,c = 17) == [2, 7]
    assert candidate(a = 4,b = 3,c = 2) == [0, 0]
    assert candidate(a = 2,b = 18,c = 20) == [1, 16]
    assert candidate(a = 1,b = 10,c = 20) == [2, 17]
    assert candidate(a = 30,b = 35,c = 40) == [2, 8]
    assert candidate(a = 1,b = 5,c = 9) == [2, 6]
    assert candidate(a = 1,b = 50,c = 100) == [2, 97]
    assert candidate(a = 10,b = 12,c = 25) == [1, 13]
    assert candidate(a = 5,b = 8,c = 12) == [2, 5]
    assert candidate(a = 8,b = 11,c = 20) == [2, 10]
    assert candidate(a = 23,b = 24,c = 26) == [1, 1]
    assert candidate(a = 1,b = 3,c = 7) == [1, 4]
    assert candidate(a = 7,b = 10,c = 13) == [2, 4]
    assert candidate(a = 3,b = 11,c = 20) == [2, 15]
    assert candidate(a = 8,b = 12,c = 17) == [2, 7]
    assert candidate(a = 13,b = 16,c = 20) == [2, 5]
    assert candidate(a = 20,b = 22,c = 26) == [1, 4]
    assert candidate(a = 1,b = 3,c = 8) == [1, 5]
    assert candidate(a = 7,b = 10,c = 14) == [2, 5]
    assert candidate(a = 98,b = 99,c = 100) == [0, 0]
    assert candidate(a = 5,b = 15,c = 25) == [2, 18]
    assert candidate(a = 35,b = 40,c = 45) == [2, 8]
    assert candidate(a = 2,b = 5,c = 8) == [2, 4]
    assert candidate(a = 2,b = 6,c = 9) == [2, 5]
    assert candidate(a = 5,b = 9,c = 14) == [2, 7]
    assert candidate(a = 6,b = 10,c = 12) == [1, 4]
    assert candidate(a = 8,b = 10,c = 15) == [1, 5]
    assert candidate(a = 6,b = 10,c = 15) == [2, 7]
    assert candidate(a = 30,b = 32,c = 34) == [1, 2]
    assert candidate(a = 3,b = 6,c = 10) == [2, 5]
    assert candidate(a = 1,b = 4,c = 7) == [2, 4]
    assert candidate(a = 2,b = 9,c = 12) == [2, 8]
    assert candidate(a = 15,b = 20,c = 25) == [2, 8]
    assert candidate(a = 8,b = 13,c = 18) == [2, 8]
    assert candidate(a = 23,b = 26,c = 29) == [2, 4]
    assert candidate(a = 40,b = 41,c = 43) == [1, 1]
    assert candidate(a = 6,b = 9,c = 12) == [2, 4]
    assert candidate(a = 2,b = 3,c = 6) == [1, 2]
    assert candidate(a = 1,b = 4,c = 100) == [2, 97]
    assert candidate(a = 6,b = 7,c = 12) == [1, 4]
    assert candidate(a = 5,b = 10,c = 14) == [2, 7]
    assert candidate(a = 5,b = 11,c = 14) == [2, 7]
    assert candidate(a = 2,b = 5,c = 10) == [2, 6]
    assert candidate(a = 15,b = 25,c = 35) == [2, 18]
    assert candidate(a = 10,b = 15,c = 25) == [2, 13]
    assert candidate(a = 20,b = 21,c = 26) == [1, 4]
    assert candidate(a = 5,b = 8,c = 11) == [2, 4]
    assert candidate(a = 2,b = 8,c = 14) == [2, 10]
    assert candidate(a = 5,b = 7,c = 14) == [1, 7]
    assert candidate(a = 25,b = 30,c = 40) == [2, 13]
    assert candidate(a = 1,b = 6,c = 11) == [2, 8]
    assert candidate(a = 33,b = 35,c = 40) == [1, 5]
    assert candidate(a = 1,b = 3,c = 10) == [1, 7]
    assert candidate(a = 2,b = 4,c = 8) == [1, 4]
    assert candidate(a = 2,b = 7,c = 11) == [2, 7]
    assert candidate(a = 10,b = 13,c = 16) == [2, 4]
    assert candidate(a = 15,b = 20,c = 40) == [2, 23]
    assert candidate(a = 5,b = 6,c = 9) == [1, 2]
    assert candidate(a = 21,b = 24,c = 28) == [2, 5]
    assert candidate(a = 90,b = 95,c = 100) == [2, 8]
    assert candidate(a = 10,b = 20,c = 25) == [2, 13]
    assert candidate(a = 3,b = 7,c = 11) == [2, 6]
    assert candidate(a = 3,b = 8,c = 10) == [1, 5]
    assert candidate(a = 10,b = 11,c = 14) == [1, 2]
    assert candidate(a = 12,b = 14,c = 20) == [1, 6]
    assert candidate(a = 30,b = 31,c = 34) == [1, 2]
    assert candidate(a = 5,b = 11,c = 17) == [2, 10]
    assert candidate(a = 100,b = 99,c = 97) == [1, 1]
    assert candidate(a = 3,b = 5,c = 10) == [1, 5]
    assert candidate(a = 4,b = 7,c = 11) == [2, 5]
    assert candidate(a = 1,b = 2,c = 4) == [1, 1]
    assert candidate(a = 2,b = 5,c = 9) == [2, 5]
    assert candidate(a = 5,b = 7,c = 10) == [1, 3]
    assert candidate(a = 3,b = 8,c = 13) == [2, 8]
    assert candidate(a = 15,b = 17,c = 25) == [1, 8]
    assert candidate(a = 6,b = 9,c = 18) == [2, 10]
    assert candidate(a = 7,b = 8,c = 14) == [1, 5]
    assert candidate(a = 2,b = 6,c = 8) == [1, 4]
    assert candidate(a = 17,b = 20,c = 23) == [2, 4]
    assert candidate(a = 30,b = 32,c = 40) == [1, 8]
    assert candidate(a = 8,b = 10,c = 13) == [1, 3]
    assert candidate(a = 1,b = 4,c = 10) == [2, 7]
    assert candidate(a = 7,b = 8,c = 15) == [1, 6]
    assert candidate(a = 7,b = 14,c = 21) == [2, 12]
    assert candidate(a = 10,b = 15,c = 20) == [2, 8]
    assert candidate(a = 4,b = 6,c = 9) == [1, 3]
    assert candidate(a = 20,b = 22,c = 30) == [1, 8]
    assert candidate(a = 10,b = 14,c = 17) == [2, 5]
    assert candidate(a = 8,b = 12,c = 22) == [2, 12]
    assert candidate(a = 7,b = 11,c = 15) == [2, 6]
    assert candidate(a = 8,b = 15,c = 3) == [2, 10]
    assert candidate(a = 2,b = 8,c = 9) == [1, 5]
    assert candidate(a = 45,b = 50,c = 55) == [2, 8]
    assert candidate(a = 3,b = 6,c = 8) == [1, 3]
    assert candidate(a = 6,b = 9,c = 15) == [2, 7]
    assert candidate(a = 1,b = 5,c = 7) == [1, 4]
    assert candidate(a = 1,b = 2,c = 3) == [0, 0]
    assert candidate(a = 50,b = 52,c = 55) == [1, 3]
    assert candidate(a = 7,b = 11,c = 25) == [2, 16]
    assert candidate(a = 9,b = 11,c = 13) == [1, 2]
    assert candidate(a = 25,b = 30,c = 50) == [2, 23]
    assert candidate(a = 10,b = 14,c = 18) == [2, 6]
    assert candidate(a = 2,b = 99,c = 100) == [1, 96]
    assert candidate(a = 23,b = 27,c = 31) == [2, 6]


