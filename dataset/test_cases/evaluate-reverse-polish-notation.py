def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tokens = ['4', '13', '5', '/', '+']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['4', '13', '5', '/', '+']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['2', '1', '+', '3', '*']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['2', '1', '+', '3', '*']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['20', '5', '/', '2', '+', '10', '3', '/', '-', '3', '4', '*', '+', '2', '-', '1', '*']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['20', '5', '/', '2', '+', '10', '3', '/', '-', '3', '4', '*', '+', '2', '-', '1', '*']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '/', '3', '-', '2', '*', '4', '1', '+', '/', '5', '-', '2', '*']) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '/', '3', '-', '2', '*', '4', '1', '+', '/', '5', '-', '2', '*']) == -10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-10', '-3', '/', '2', '*']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-10', '-3', '/', '2', '*']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['20', '5', '*']) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['20', '5', '*']) == 100: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['3', '-4', '+', '2', '*', '5', '/', '10', '+']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['3', '-4', '+', '2', '*', '5', '/', '10', '+']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '4', '+', '3', '*', '2', '/', '7', '-', '1', '+', '5', '*']) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '4', '+', '3', '*', '2', '/', '7', '-', '1', '+', '5', '*']) == 60: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['17', '5', '+', '3', '8', '*', '-', '10', '2', '/', '+']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['17', '5', '+', '3', '8', '*', '-', '10', '2', '/', '+']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '-5', '*', '2', '-', '3', '*']) == -156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '-5', '*', '2', '-', '3', '*']) == -156: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '-', '20', '*', '2', '/', '3', '+', '5', '-', '6', '*', '7', '/', '8', '+', '9', '-']) == 425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '-', '20', '*', '2', '/', '3', '+', '5', '-', '6', '*', '7', '/', '8', '+', '9', '-']) == 425: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '/', '20', '10', '/', '*', '30', '2', '*', '+']) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '/', '20', '10', '/', '*', '30', '2', '*', '+']) == 64: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '-50', '/', '20', '-10', '/', '*']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '-50', '/', '20', '-10', '/', '*']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '+', '3', '4', '+', '*', '5', '6', '+', '7', '8', '+', '*', '9', '10', '+', '*']) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '+', '3', '4', '+', '*', '5', '6', '+', '7', '8', '+', '*', '9', '10', '+', '*']) == 21: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '4', '*', '6', '2', '/', '-', '5', '+', '3', '2', '*']) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '4', '*', '6', '2', '/', '-', '5', '+', '3', '2', '*']) == 34: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-10', '-5', '/', '2', '*', '-1', '+']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-10', '-5', '/', '2', '*', '-1', '+']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '12', '+', '3', '/', '4', '*', '5', '2', '/', '-', '7', '+', '2', '*']) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '12', '+', '3', '/', '4', '*', '5', '2', '/', '-', '7', '+', '2', '*']) == 58: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '+', '3', '4', '+', '*']) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '+', '3', '4', '+', '*']) == 21: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['3', '8', '2', '/', '+', '4', '*', '10', '5', '/', '-', '2', '*']) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['3', '8', '2', '/', '+', '4', '*', '10', '5', '/', '-', '2', '*']) == 52: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['20', '5', '+', '3', '*', '2', '-', '8', '/', '4', '*']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['20', '5', '+', '3', '*', '2', '-', '8', '/', '4', '*']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '2', '/', '1', '+', '4', '*']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '2', '/', '1', '+', '4', '*']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '3', '+', '2', '*', '5', '-']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '3', '+', '2', '*', '5', '-']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '2', '/', '3', '4', '+', '*', '1', '5', '-', '*']) == -112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '2', '/', '3', '4', '+', '*', '1', '5', '-', '*']) == -112: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['20', '10', '/', '5', '*']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['20', '10', '/', '5', '*']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '3', '2', '*', '+', '5', '-', '1', '2', '+', '/']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '3', '2', '*', '+', '5', '-', '1', '2', '+', '/']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '5', '2', '/', '+', '3', '-14', '*', '8', '/']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '5', '2', '/', '+', '3', '-14', '*', '8', '/']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-1', '3', '*', -1, '2', '+', '*', '4', '1', '-']) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-1', '3', '*', -1, '2', '+', '*', '4', '1', '-']) == -3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '5', '+', '20', '-', '2', '/', '15', '*', '3', '-', '10', '/', '2', '+', '1', '-', '7', '*', '3', '/', '2', '*']) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '5', '+', '20', '-', '2', '/', '15', '*', '3', '-', '10', '/', '2', '+', '1', '-', '7', '*', '3', '/', '2', '*']) == -8: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['12', '-3', '*', '4', '/', '8', '+', '2', '-', '5', '*', '-2', '/']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['12', '-3', '*', '4', '/', '8', '+', '2', '-', '5', '*', '-2', '/']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '8', '4', '/', '+']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '8', '4', '/', '+']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '4', '2', '+', '*']) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '4', '2', '+', '*']) == 60: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '3', '5', '/', '2', '*', '+', '8', '3', '2', '*', '-', '4', '*', '2', '/', '+']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '3', '5', '/', '2', '*', '+', '8', '3', '2', '*', '-', '4', '*', '2', '/', '+']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['12', '3', '*']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['12', '3', '*']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['17', '5', '+', '3', '*', '2', '-', '1', '+', '4', '/', '2', '*', '3', '+', '1', '-', '9', '/', '3', '*', '-11', '+', '-2', '*', '-3', '+', '17', '/', '5', '-', '7', '+', '-4', '*']) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['17', '5', '+', '3', '*', '2', '-', '1', '+', '4', '/', '2', '*', '3', '+', '1', '-', '9', '/', '3', '*', '-11', '+', '-2', '*', '-3', '+', '17', '/', '5', '-', '7', '+', '-4', '*']) == -8: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['18', '4', '-']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['18', '4', '-']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '20', '+', '30', '*', '40', '+', '50', '*', '60', '-']) == 46940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '20', '+', '30', '*', '40', '+', '50', '*', '60', '-']) == 46940: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '-5', '*', '2', '+', '20', '-10', '/', '*', '3', '+', '2', '*']) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '-5', '*', '2', '+', '20', '-10', '/', '*', '3', '+', '2', '*']) == 198: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '20', '30', '40', '+', '*']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '20', '30', '40', '+', '*']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '3', '-', '2', '1', '/', '*']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '3', '-', '2', '1', '/', '*']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['9', '3', '+', '6', '2', '/', '-', '11', '*', '7', '/', '2', '+']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['9', '3', '+', '6', '2', '/', '-', '11', '*', '7', '/', '2', '+']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '3', '4', '+', '*', '5', '/']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '3', '4', '+', '*', '5', '/']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '3', '+', '4', '/', '+', '5', '-', '6', '*']) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '3', '+', '4', '/', '+', '5', '-', '6', '*']) == -18: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '1', '+', '1', '1', '+', '1', '1', '+', '1', '1', '+', '1', '1', '+']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '1', '+', '1', '1', '+', '1', '1', '+', '1', '1', '+', '1', '1', '+']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-7', '3', '/', '2', '-3', '*']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-7', '3', '/', '2', '-3', '*']) == -2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['9', '3', '+', '6', '2', '/', '*']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['9', '3', '+', '6', '2', '/', '*']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['9', '3', '-', '4', '/', '8', '2', '*', '+', '6', '1', '-', '*', '3', '+', '5', '-', '11', '/']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['9', '3', '-', '4', '/', '8', '2', '*', '+', '6', '1', '-', '*', '3', '+', '5', '-', '11', '/']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-8', '*', '2', '/', '3', '+', '1', '-', '5', '11', '+', '2', '/', '*', '4', '-']) == -212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-8', '*', '2', '/', '3', '+', '1', '-', '5', '11', '+', '2', '/', '*', '4', '-']) == -212: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '+', '25', '-', '10', '*', '5', '/']) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '+', '25', '-', '10', '*', '5', '/']) == 250: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-3', '*', '2', '1', '+', '*', '5', '-', '3', '+', '2', '*']) == -130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-3', '*', '2', '1', '+', '*', '5', '-', '3', '+', '2', '*']) == -130: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '3', '/', '5', '+', '-3', '*', '7', '2', '/', '+', '8', '-', '2', '*', '3', '+', '6', '-', '4', '/', '9', '+', '11', '-', '13', '*', '15', '/', '17', '+', '19', '-']) == -16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '3', '/', '5', '+', '-3', '*', '7', '2', '/', '+', '8', '-', '2', '*', '3', '+', '6', '-', '4', '/', '9', '+', '11', '-', '13', '*', '15', '/', '17', '+', '19', '-']) == -16: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '8', '4', '2', '+', '*']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '8', '4', '2', '+', '*']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '3', '+', '2', '*', '8', '4', '/', '-']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '3', '+', '2', '*', '8', '4', '/', '-']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-1', '-2', '*']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-1', '-2', '*']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['15', '7', '1', '1', '+', '-', '3', '/', '2', '1', '1', '+', '+', '-']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['15', '7', '1', '1', '+', '-', '3', '/', '2', '1', '1', '+', '+', '-']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['20', '4', '/', '5', '2', '*', '+']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['20', '4', '/', '5', '2', '*', '+']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '4', '+', '2', '/', '3', '*', '1', '+', '6', '-']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '4', '+', '2', '/', '3', '*', '1', '+', '6', '-']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['9', '3', '/', '2', '1', '+', '*']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['9', '3', '/', '2', '1', '+', '*']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['18', '7', '+', '3', '-', '1', '*', '2', '+', '5', '/', '9', '+', '1', '+', '-11', '*', '13', '-', '5', '+', '9', '+', '15', '+', '1', '-', '7', '*', '8', '+', '-3', '-', '2', '-']) == -964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['18', '7', '+', '3', '-', '1', '*', '2', '+', '5', '/', '9', '+', '1', '+', '-11', '*', '13', '-', '5', '+', '9', '+', '15', '+', '1', '-', '7', '*', '8', '+', '-3', '-', '2', '-']) == -964: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '-5', '+', '20', '-10', '/', '2', '*']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '-5', '+', '20', '-10', '/', '2', '*']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '-2', '*']) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '-2', '*']) == -10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '20', '5', '/', '2', '*']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '20', '5', '/', '2', '*']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['13', '7', '2', '+', '/']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['13', '7', '2', '+', '/']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-1', '-1', '*', '-2', '-', '2', '*', '-3', '/', '4', '-']) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-1', '-1', '*', '-2', '-', '2', '*', '-3', '/', '4', '-']) == -6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '3', '-']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '3', '-']) == -2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['15', '11', '+']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['15', '11', '+']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '20', '+', '30', '40', '+', '50', '60', '+', '70', '80', '+', '90', '*']) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '20', '+', '30', '40', '+', '50', '60', '+', '70', '80', '+', '90', '*']) == 30: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['6', '3', '1', '+', '*', '4', '/']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['6', '3', '1', '+', '*', '4', '/']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['15', '7', '1', '1', '+', '-', '/', '3', '*', '2', '1', '1', '+', '+', '-']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['15', '7', '1', '1', '+', '-', '/', '3', '*', '2', '1', '1', '+', '+', '-']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '+', '20', '*', '4', '/', '2', '+', '8', '-', '3', '*']) == 2232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '+', '20', '*', '4', '/', '2', '+', '8', '-', '3', '*']) == 2232: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '+', '3', '4', '+', '*', '5', '6', '+', '*', '7', '8', '+', '*', '9', '10', '+', '*']) == 65835
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '+', '3', '4', '+', '*', '5', '6', '+', '*', '7', '8', '+', '*', '9', '10', '+', '*']) == 65835: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '-']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '-']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '200', '+', '50', '-', '2', '/', '3', '*', '10', '+']) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '200', '+', '50', '-', '2', '/', '3', '*', '10', '+']) == 385: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '3', '+', '7', '4', '-', '*']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '3', '+', '7', '4', '-', '*']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '+', '3', '*', '4', '+', '5', '*', '6', '+', '7', '*', '8', '+', '9', '+', '10', '+', '11', '+', '12', '+', '13', '+', '14', '+', '15', '+', '16', '+', '17', '+', '18', '+', '19', '+']) == 659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '+', '3', '*', '4', '+', '5', '*', '6', '+', '7', '*', '8', '+', '9', '+', '10', '+', '11', '+', '12', '+', '13', '+', '14', '+', '15', '+', '16', '+', '17', '+', '18', '+', '19', '+']) == 659: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '/', '20', '*', '10', '-', '5', '+', '2', '*', '3', '/', '1', '+', '4', '-']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '/', '20', '*', '10', '-', '5', '+', '2', '*', '3', '/', '1', '+', '4', '-']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['18', '5', '+', '12', '-', '3', '/', '2', '*', '4', '-']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['18', '5', '+', '12', '-', '3', '/', '2', '*', '4', '-']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['8', '3', '2', '*', '1', '-', '2', '/']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['8', '3', '2', '*', '1', '-', '2', '/']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['-11', '-12', '-', '13', '-14', '-', '*']) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['-11', '-12', '-', '13', '-14', '-', '*']) == 27: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['20', '5', '2', '/', '*']) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['20', '5', '2', '/', '*']) == 40: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['0', '3', '/', '5', '+']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['0', '3', '/', '5', '+']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['3', '-4', '*', '2', '/', '5', '-']) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['3', '-4', '*', '2', '/', '5', '-']) == -11: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['1', '2', '3', '+', '*']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['1', '2', '3', '+', '*']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '2', '*', '-', '30', '20', '+', '/', '10', '+']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '2', '*', '-', '30', '20', '+', '/', '10', '+']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-3', '*', '11', '5', '-', '/', '2', '2', '+', '*']) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-3', '*', '11', '5', '-', '/', '2', '2', '+', '*']) == -12: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-3', '*', '2', '1', '+', '-', '15', '5', '/', '+']) == -21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-3', '*', '2', '1', '+', '-', '15', '5', '/', '+']) == -21: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['2', '3', '4', '5', '+', '*', '6', '/']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['2', '3', '4', '5', '+', '*', '6', '/']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '6', '9', '3', '+', '-11', '*']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '6', '9', '3', '+', '-11', '*']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-3', '*']) == -21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-3', '*']) == -21: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['10', '5', '-', '3', '*', '4', '+', '2', '/']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['10', '5', '-', '3', '*', '4', '+', '2', '/']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-3', '*', '2', '+', '15', '5', '/', '*']) == -57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-3', '*', '2', '+', '15', '5', '/', '*']) == -57: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['15', '-3', '/', '7', '+', '2', '*', '10', '-', '5', '*']) == -30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['15', '-3', '/', '7', '+', '2', '*', '10', '-', '5', '*']) == -30: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['100', '50', '/', '25', '*', '5', '+', '3', '-', '2', '*']) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['100', '50', '/', '25', '*', '5', '+', '3', '-', '2', '*']) == 104: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '-8', '*', '5', '+', '3', '-12', '/', '4', '*']) == -51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '-8', '*', '5', '+', '3', '-12', '/', '4', '*']) == -51: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['7', '8', '3', '*', '+', '2', '/', '4', '-', '10', '5', '*', '+']) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['7', '8', '3', '*', '+', '2', '/', '4', '-', '10', '5', '*', '+']) == 61: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '2', '/', '10', '2', '/', '-', '3', '*', '7', '+', '-1', '*']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '2', '/', '10', '2', '/', '-', '3', '*', '7', '+', '-1', '*']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = ['5', '2', '/', '-1', '*', '3', '-']) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = ['5', '2', '/', '-1', '*', '3', '-']) == -5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tokens = ['4', '13', '5', '/', '+']) == 6
    assert candidate(tokens = ['2', '1', '+', '3', '*']) == 9
    assert candidate(tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22
    assert candidate(tokens = ['20', '5', '/', '2', '+', '10', '3', '/', '-', '3', '4', '*', '+', '2', '-', '1', '*']) == 13
    assert candidate(tokens = ['100', '50', '/', '3', '-', '2', '*', '4', '1', '+', '/', '5', '-', '2', '*']) == -10
    assert candidate(tokens = ['-10', '-3', '/', '2', '*']) == 6
    assert candidate(tokens = ['20', '5', '*']) == 100
    assert candidate(tokens = ['3', '-4', '+', '2', '*', '5', '/', '10', '+']) == 10
    assert candidate(tokens = ['8', '4', '+', '3', '*', '2', '/', '7', '-', '1', '+', '5', '*']) == 60
    assert candidate(tokens = ['17', '5', '+', '3', '8', '*', '-', '10', '2', '/', '+']) == 3
    assert candidate(tokens = ['10', '-5', '*', '2', '-', '3', '*']) == -156
    assert candidate(tokens = ['100', '50', '-', '20', '*', '2', '/', '3', '+', '5', '-', '6', '*', '7', '/', '8', '+', '9', '-']) == 425
    assert candidate(tokens = ['100', '50', '/', '20', '10', '/', '*', '30', '2', '*', '+']) == 64
    assert candidate(tokens = ['100', '-50', '/', '20', '-10', '/', '*']) == 4
    assert candidate(tokens = ['1', '2', '+', '3', '4', '+', '*', '5', '6', '+', '7', '8', '+', '*', '9', '10', '+', '*']) == 21
    assert candidate(tokens = ['8', '4', '*', '6', '2', '/', '-', '5', '+', '3', '2', '*']) == 34
    assert candidate(tokens = ['-10', '-5', '/', '2', '*', '-1', '+']) == 3
    assert candidate(tokens = ['8', '12', '+', '3', '/', '4', '*', '5', '2', '/', '-', '7', '+', '2', '*']) == 58
    assert candidate(tokens = ['1', '2', '+', '3', '4', '+', '*']) == 21
    assert candidate(tokens = ['3', '8', '2', '/', '+', '4', '*', '10', '5', '/', '-', '2', '*']) == 52
    assert candidate(tokens = ['20', '5', '+', '3', '*', '2', '-', '8', '/', '4', '*']) == 36
    assert candidate(tokens = ['5', '2', '/', '1', '+', '4', '*']) == 12
    assert candidate(tokens = ['7', '3', '+', '2', '*', '5', '-']) == 15
    assert candidate(tokens = ['8', '2', '/', '3', '4', '+', '*', '1', '5', '-', '*']) == -112
    assert candidate(tokens = ['20', '10', '/', '5', '*']) == 10
    assert candidate(tokens = ['1', '3', '2', '*', '+', '5', '-', '1', '2', '+', '/']) == 0
    assert candidate(tokens = ['10', '5', '2', '/', '+', '3', '-14', '*', '8', '/']) == 12
    assert candidate(tokens = ['-1', '3', '*', -1, '2', '+', '*', '4', '1', '-']) == -3
    assert candidate(tokens = ['10', '5', '+', '20', '-', '2', '/', '15', '*', '3', '-', '10', '/', '2', '+', '1', '-', '7', '*', '3', '/', '2', '*']) == -8
    assert candidate(tokens = ['12', '-3', '*', '4', '/', '8', '+', '2', '-', '5', '*', '-2', '/']) == 7
    assert candidate(tokens = ['5', '8', '4', '/', '+']) == 7
    assert candidate(tokens = ['10', '4', '2', '+', '*']) == 60
    assert candidate(tokens = ['10', '3', '5', '/', '2', '*', '+', '8', '3', '2', '*', '-', '4', '*', '2', '/', '+']) == 14
    assert candidate(tokens = ['12', '3', '*']) == 36
    assert candidate(tokens = ['17', '5', '+', '3', '*', '2', '-', '1', '+', '4', '/', '2', '*', '3', '+', '1', '-', '9', '/', '3', '*', '-11', '+', '-2', '*', '-3', '+', '17', '/', '5', '-', '7', '+', '-4', '*']) == -8
    assert candidate(tokens = ['18', '4', '-']) == 14
    assert candidate(tokens = ['10', '20', '+', '30', '*', '40', '+', '50', '*', '60', '-']) == 46940
    assert candidate(tokens = ['10', '-5', '*', '2', '+', '20', '-10', '/', '*', '3', '+', '2', '*']) == 198
    assert candidate(tokens = ['10', '20', '30', '40', '+', '*']) == 10
    assert candidate(tokens = ['8', '3', '-', '2', '1', '/', '*']) == 10
    assert candidate(tokens = ['9', '3', '+', '6', '2', '/', '-', '11', '*', '7', '/', '2', '+']) == 16
    assert candidate(tokens = ['1', '2', '3', '4', '+', '*', '5', '/']) == 1
    assert candidate(tokens = ['1', '2', '3', '+', '4', '/', '+', '5', '-', '6', '*']) == -18
    assert candidate(tokens = ['1', '1', '+', '1', '1', '+', '1', '1', '+', '1', '1', '+', '1', '1', '+']) == 2
    assert candidate(tokens = ['-7', '3', '/', '2', '-3', '*']) == -2
    assert candidate(tokens = ['9', '3', '+', '6', '2', '/', '*']) == 36
    assert candidate(tokens = ['9', '3', '-', '4', '/', '8', '2', '*', '+', '6', '1', '-', '*', '3', '+', '5', '-', '11', '/']) == 7
    assert candidate(tokens = ['7', '-8', '*', '2', '/', '3', '+', '1', '-', '5', '11', '+', '2', '/', '*', '4', '-']) == -212
    assert candidate(tokens = ['100', '50', '+', '25', '-', '10', '*', '5', '/']) == 250
    assert candidate(tokens = ['7', '-3', '*', '2', '1', '+', '*', '5', '-', '3', '+', '2', '*']) == -130
    assert candidate(tokens = ['10', '3', '/', '5', '+', '-3', '*', '7', '2', '/', '+', '8', '-', '2', '*', '3', '+', '6', '-', '4', '/', '9', '+', '11', '-', '13', '*', '15', '/', '17', '+', '19', '-']) == -16
    assert candidate(tokens = ['5', '8', '4', '2', '+', '*']) == 5
    assert candidate(tokens = ['5', '3', '+', '2', '*', '8', '4', '/', '-']) == 14
    assert candidate(tokens = ['-1', '-2', '*']) == 2
    assert candidate(tokens = ['15', '7', '1', '1', '+', '-', '3', '/', '2', '1', '1', '+', '+', '-']) == 15
    assert candidate(tokens = ['20', '4', '/', '5', '2', '*', '+']) == 15
    assert candidate(tokens = ['8', '4', '+', '2', '/', '3', '*', '1', '+', '6', '-']) == 13
    assert candidate(tokens = ['9', '3', '/', '2', '1', '+', '*']) == 9
    assert candidate(tokens = ['18', '7', '+', '3', '-', '1', '*', '2', '+', '5', '/', '9', '+', '1', '+', '-11', '*', '13', '-', '5', '+', '9', '+', '15', '+', '1', '-', '7', '*', '8', '+', '-3', '-', '2', '-']) == -964
    assert candidate(tokens = ['10', '-5', '+', '20', '-10', '/', '2', '*']) == 5
    assert candidate(tokens = ['5', '-2', '*']) == -10
    assert candidate(tokens = ['10', '20', '5', '/', '2', '*']) == 10
    assert candidate(tokens = ['13', '7', '2', '+', '/']) == 1
    assert candidate(tokens = ['-1', '-1', '*', '-2', '-', '2', '*', '-3', '/', '4', '-']) == -6
    assert candidate(tokens = ['1', '3', '-']) == -2
    assert candidate(tokens = ['15', '11', '+']) == 26
    assert candidate(tokens = ['10', '20', '+', '30', '40', '+', '50', '60', '+', '70', '80', '+', '90', '*']) == 30
    assert candidate(tokens = ['6', '3', '1', '+', '*', '4', '/']) == 6
    assert candidate(tokens = ['15', '7', '1', '1', '+', '-', '/', '3', '*', '2', '1', '1', '+', '+', '-']) == 5
    assert candidate(tokens = ['100', '50', '+', '20', '*', '4', '/', '2', '+', '8', '-', '3', '*']) == 2232
    assert candidate(tokens = ['1', '2', '+', '3', '4', '+', '*', '5', '6', '+', '*', '7', '8', '+', '*', '9', '10', '+', '*']) == 65835
    assert candidate(tokens = ['100', '50', '-']) == 50
    assert candidate(tokens = ['100', '200', '+', '50', '-', '2', '/', '3', '*', '10', '+']) == 385
    assert candidate(tokens = ['5', '3', '+', '7', '4', '-', '*']) == 24
    assert candidate(tokens = ['1', '2', '+', '3', '*', '4', '+', '5', '*', '6', '+', '7', '*', '8', '+', '9', '+', '10', '+', '11', '+', '12', '+', '13', '+', '14', '+', '15', '+', '16', '+', '17', '+', '18', '+', '19', '+']) == 659
    assert candidate(tokens = ['100', '50', '/', '20', '*', '10', '-', '5', '+', '2', '*', '3', '/', '1', '+', '4', '-']) == 20
    assert candidate(tokens = ['18', '5', '+', '12', '-', '3', '/', '2', '*', '4', '-']) == 2
    assert candidate(tokens = ['8', '3', '2', '*', '1', '-', '2', '/']) == 8
    assert candidate(tokens = ['-11', '-12', '-', '13', '-14', '-', '*']) == 27
    assert candidate(tokens = ['20', '5', '2', '/', '*']) == 40
    assert candidate(tokens = ['0', '3', '/', '5', '+']) == 5
    assert candidate(tokens = ['3', '-4', '*', '2', '/', '5', '-']) == -11
    assert candidate(tokens = ['1', '2', '3', '+', '*']) == 5
    assert candidate(tokens = ['100', '50', '2', '*', '-', '30', '20', '+', '/', '10', '+']) == 10
    assert candidate(tokens = ['7', '-3', '*', '11', '5', '-', '/', '2', '2', '+', '*']) == -12
    assert candidate(tokens = ['7', '-3', '*', '2', '1', '+', '-', '15', '5', '/', '+']) == -21
    assert candidate(tokens = ['2', '3', '4', '5', '+', '*', '6', '/']) == 2
    assert candidate(tokens = ['10', '6', '9', '3', '+', '-11', '*']) == 10
    assert candidate(tokens = ['7', '-3', '*']) == -21
    assert candidate(tokens = ['10', '5', '-', '3', '*', '4', '+', '2', '/']) == 9
    assert candidate(tokens = ['7', '-3', '*', '2', '+', '15', '5', '/', '*']) == -57
    assert candidate(tokens = ['15', '-3', '/', '7', '+', '2', '*', '10', '-', '5', '*']) == -30
    assert candidate(tokens = ['100', '50', '/', '25', '*', '5', '+', '3', '-', '2', '*']) == 104
    assert candidate(tokens = ['7', '-8', '*', '5', '+', '3', '-12', '/', '4', '*']) == -51
    assert candidate(tokens = ['7', '8', '3', '*', '+', '2', '/', '4', '-', '10', '5', '*', '+']) == 61
    assert candidate(tokens = ['5', '2', '/', '10', '2', '/', '-', '3', '*', '7', '+', '-1', '*']) == 2
    assert candidate(tokens = ['5', '2', '/', '-1', '*', '3', '-']) == -5


