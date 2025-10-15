def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(board = ['E123', '45X7', '89XS']) == [21, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123', '45X7', '89XS']) == [21, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11', 'XXX', '11S']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11', 'XXX', '11S']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['EX', 'XS']) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['EX', 'XS']) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E111', '1X11', '1111', '111S']) == [5, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E111', '1X11', '1111', '111S']) == [5, 8]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E22', '222', '22S']) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E22', '222', '22S']) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X', 'X1X', 'X1S']) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X', 'X1X', 'X1S']) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123', '12X3', '21XS']) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123', '12X3', '21XS']) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123', '1X21', '21XS']) == [5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123', '1X21', '21XS']) == [5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['EX', '1S']) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['EX', '1S']) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E23', '2X2', '12S']) == [7, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E23', '2X2', '12S']) == [7, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E111', '1111', '11X1', '111S']) == [5, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E111', '1111', '11X1', '111S']) == [5, 8]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12', '1X1', '21S']) == [4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12', '1X1', '21S']) == [4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123', '456X', '789S']) == [28, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123', '456X', '789S']) == [28, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123', '4X56', '789S']) == [28, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123', '4X56', '789S']) == [28, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X', '1X1', 'S11']) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X', '1X1', 'S11']) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1', '1S']) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1', '1S']) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456', '2345678', '345678X', '456789X', '56789XS', '6789XSX']) == [44, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456', '2345678', '345678X', '456789X', '56789XS', '6789XSX']) == [44, 35]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E121', '2121', '1212', '1S11']) == [9, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E121', '2121', '1212', '1S11']) == [9, 6]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12X4', '56789', 'X1234', '5678X', '9XS12']) == [40, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12X4', '56789', 'X1234', '5678X', '9XS12']) == [40, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '6789X1', '234567', '89XS12', '345678']) == [49, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '6789X1', '234567', '89XS12', '345678']) == [49, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1X1X1', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1S']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1X1X1', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1S']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '56X89', '4X321', '12X56', '789XS']) == [30, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '56X89', '4X321', '12X56', '789XS']) == [30, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234567', '23456789', '3456789X', '456789XS', '56789XSX', '6789XSXX', '789XSXXX', '89XSXXXX']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234567', '23456789', '3456789X', '456789XS', '56789XSX', '6789XSXX', '789XSXXX', '89XSXXXX']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '56789', 'X123X', '45678', '9XS12']) == [46, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '56789', 'X123X', '45678', '9XS12']) == [46, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1', '1X1X', '1X1X', '1X1S']) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1', '1X1X', '1X1X', '1X1S']) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E2222', '22222', '22X22', '22222', '2222S']) == [14, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E2222', '22222', '22X22', '22222', '2222S']) == [14, 34]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111111', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '11111111S']) == [15, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111111', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '11111111S']) == [15, 11]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E9876', '9X8X7', '6X5X4', '3X2X1', '4321S']) == [42, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E9876', '9X8X7', '6X5X4', '3X2X1', '4321S']) == [42, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234567', '89X12345', '6789X123', '456789X1', '23456789', '1234567S', '89XS1234']) == [90, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234567', '89X12345', '6789X123', '456789X1', '23456789', '1234567S', '89XS1234']) == [90, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E999', '9X99', '99X9', '999S']) == [45, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E999', '9X99', '99X9', '999S']) == [45, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12X4', '56789', 'X1234', '56789', 'S1234']) == [52, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12X4', '56789', 'X1234', '56789', 'S1234']) == [52, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456', '789X123', '456789X', '1234567', '89X1234', '56789XS']) == [63, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456', '789X123', '456789X', '1234567', '89X1234', '56789XS']) == [63, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E111', '1X11', '11X1', '111S']) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E111', '1X11', '11X1', '111S']) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E222', '2X22', '2X22', '2X2S']) == [10, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E222', '2X22', '2X22', '2X2S']) == [10, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '6X7X89', '1X2X3X', '4X5X6X', '7X8X9X', '12345S']) == [41, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '6X7X89', '1X2X3X', '4X5X6X', '7X8X9X', '12345S']) == [41, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '1X1X1', '21212', '31313', '4141S']) == [16, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '1X1X1', '21212', '31313', '4141S']) == [16, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '56X78', '9X0X1', '23456', '7XS9E']) == [37, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '56X78', '9X0X1', '23456', '7XS9E']) == [37, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234567', '1X2X3X4X', '5X6X7X8X', '9X0X1X2X', '3X4X5X6X', '7X8X9X0X', '1234567S']) == [53, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234567', '1X2X3X4X', '5X6X7X8X', '9X0X1X2X', '3X4X5X6X', '7X8X9X0X', '1234567S']) == [53, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E2222', '2X2X2', '2X2X2', '2X2X2', '2222S']) == [14, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E2222', '2X2X2', '2X2X2', '2X2X2', '2222S']) == [14, 3]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456', '789X123', '456789X', '1234567', '89XS123', '3456789']) == [70, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456', '789X123', '456789X', '1234567', '89XS123', '3456789']) == [70, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1X1X1X1X1', '111111111111', '1X1X1X1X1X11', '111X1X1X1X11', '1X1X1X1X1X11', '111X1X1X1X11', '1X1X1X1X1X11', '111X1X1X1X1S']) == [13, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1X1X1X1X1', '111111111111', '1X1X1X1X1X11', '111X1X1X1X11', '1X1X1X1X1X11', '111X1X1X1X11', '1X1X1X1X1X11', '111X1X1X1X1S']) == [13, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1X1X1X1X1X1X1', '1111111111111111', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111111111111111S']) == [26, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1X1X1X1X1X1X1', '1111111111111111', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111111111111111S']) == [26, 18]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12X45', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '45678S']) == [43, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12X45', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '45678S']) == [43, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '1X1X1', '111X1', '1X1X1', '1111S']) == [7, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '1X1X1', '111X1', '1X1X1', '1111S']) == [7, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '56X78', '9XABC', 'DEFXS']) == [14, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '56X78', '9XABC', 'DEFXS']) == [14, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12121', '1X1X11', '212121', '1X1X11', '212121', '11111S']) == [13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12121', '1X1X11', '212121', '1X1X11', '212121', '11111S']) == [13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '6789XS', '54321X', '98765X', '43210X', '32109S']) == [55, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '6789XS', '54321X', '98765X', '43210X', '32109S']) == [55, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '1X1X1X', '212121', '1X1X1X', '32323S']) == [17, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '1X1X1X', '212121', '1X1X1X', '32323S']) == [17, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E22222', '2X2X22', '222X22', '2X2X22', '222X22', '22222S']) == [18, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E22222', '2X2X22', '222X22', '2X2X22', '222X22', '22222S']) == [18, 11]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111', '1X1X11', '1X1X11', '1X1X11', '1X1X11', '11111S']) == [9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111', '1X1X11', '1X1X11', '1X1X11', '1X1X11', '11111S']) == [9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '67X9X1', '234567', '89XS12', '345678', '456789']) == [64, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '67X9X1', '234567', '89XS12', '345678', '456789']) == [64, 10]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1X1X1X1X1X1', '11111111111111', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '1111111111111S']) == [22, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1X1X1X1X1X1', '11111111111111', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '1111111111111S']) == [22, 15]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '56X78', '9X123', '45678', '89XS1']) == [45, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '56X78', '9X123', '45678', '89XS1']) == [45, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E234', '1X12', '21XS', '3456']) == [21, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E234', '1X12', '21XS', '3456']) == [21, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '1X1X1', '1X1X1', '1X1X1', '1111S']) == [7, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '1X1X1', '1X1X1', '1X1X1', '1111S']) == [7, 3]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111', '111111', '111X11', '111111', '111111', '11111S']) == [9, 152]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111', '111111', '111X11', '111111', '111111', '11111S']) == [9, 152]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111111', '1X1X1X11', '111X1111', '1X1X1X11', '111X1111', '1X1X1X11', '111X1111', '1111111S']) == [13, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111111', '1X1X1X11', '111X1111', '1X1X1X11', '111X1111', '1X1X1X11', '111X1111', '1111111S']) == [13, 28]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345678910', '1X1X1X1X1X1X11', '212121212121', '1X1X1X1X1X1X11', '323232323232', '1X1X1X1X1X1X11', '414141414141', '1X1X1X1X1X1X11', '515151515151', '1X1X1X1X1X1X11', '616161616161', '1111111111111S']) == [73, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345678910', '1X1X1X1X1X1X11', '212121212121', '1X1X1X1X1X1X11', '323232323232', '1X1X1X1X1X1X11', '414141414141', '1X1X1X1X1X1X11', '515151515151', '1X1X1X1X1X1X11', '616161616161', '1111111111111S']) == [73, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456789', '987654321X', '123456789X', 'X987654321', '123456789X', 'X987654321', '123456789X', 'X987654321', '123456789X', 'XS12345678']) == [121, 72]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456789', '987654321X', '123456789X', 'X987654321', '123456789X', 'X987654321', '123456789X', 'X987654321', '123456789X', 'XS12345678']) == [121, 72]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '67X890', '123X45', '678X90', '123X45', '6789XS']) == [45, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '67X890', '123X45', '678X90', '123X45', '6789XS']) == [45, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '45678S']) == [43, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '45678S']) == [43, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '11111', '11X11', '11111', '1111S']) == [7, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '11111', '11X11', '11111', '1111S']) == [7, 34]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11X1', '1X1X1', '1X1X1', '1X1X1', '111XS']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11X1', '1X1X1', '1X1X1', '1X1X1', '111XS']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E111111', '1X1X1X1', '111X111', '1X1X1X1', '111X111', '1X1X1X1', '111111S']) == [11, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E111111', '1X1X1X1', '111X111', '1X1X1X1', '111X111', '1X1X1X1', '111111S']) == [11, 8]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1X1', '1X1X1X', '1X1X1X', '1X1X1X', '1X1X1S']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1X1', '1X1X1X', '1X1X1X', '1X1X1X', '1X1X1S']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111', '1X1X1X', '111X11', '1X1X1X', '11111S']) == [8, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111', '1X1X1X', '111X11', '1X1X1X', '11111S']) == [8, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X1X1X1X1X1X1X1X1', '111111111111111111', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '11111111111111111S']) == [30, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X1X1X1X1X1X1X1X1', '111111111111111111', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '11111111111111111S']) == [30, 21]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E111111', '1X1X1X1', '111X1X1', '1X1X1X1', '111X1X1', '1X1X1X1', '111111S']) == [11, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E111111', '1X1X1X1', '111X1X1', '1X1X1X1', '111X1X1', '1X1X1X1', '111111S']) == [11, 6]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11X1', '1X1X1', '1X1X1', '1X1X1', '11X1S']) == [6, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11X1', '1X1X1', '1X1X1', '1X1X1', '11X1S']) == [6, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123', '21X1', '1X1X', '321S']) == [9, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123', '21X1', '1X1X', '321S']) == [9, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111', '1X1X11', '111X11', '1X1X11', '111X11', '11111S']) == [9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111', '1X1X11', '111X11', '1X1X11', '111X11', '11111S']) == [9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '1X1X1', '11111', '1X1X1', '1111S']) == [7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '1X1X1', '11111', '1X1X1', '1111S']) == [7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1X11', '11X11', '111X1', '1111X', '1111S']) == [7, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1X11', '11X11', '111X1', '1111X', '1111S']) == [7, 19]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456', '1X2X3X4', '5X6X7X8', '9X0X1X2', '3X4X5X6', '7X8X9XS']) == [35, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456', '1X2X3X4', '5X6X7X8', '9X0X1X2', '3X4X5X6', '7X8X9XS']) == [35, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345678', '9X1234567', '89X12345X', '789XS1234', '6789XS123', '56789XS12', '456789XS1', '3456789XS']) == [111, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345678', '9X1234567', '89X12345X', '789XS1234', '6789XS123', '56789XS12', '456789XS1', '3456789XS']) == [111, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111', '1X1X11', '111111', '1X1X1X', '111111', '11XS11']) == [10, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111', '1X1X11', '111111', '1X1X1X', '111111', '11XS11']) == [10, 12]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111111', '1X1X1X11', '11111111', '1X1X1X11', '11111111', '1X1X1X11', '11111111', '11XS1111']) == [14, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111111', '1X1X1X11', '11111111', '1X1X1X11', '11111111', '1X1X1X11', '11111111', '11XS1111']) == [14, 90]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456', '789X123', '456789X', '1234567', '89XS123', '456789S']) == [71, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456', '789X123', '456789X', '1234567', '89XS123', '456789S']) == [71, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '4567XS']) == [31, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '4567XS']) == [31, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1212121', '1X1X1X11', '21212121', '1X1X1X11', '21212121', '1X1X1X11', '21212121', '1111111S']) == [19, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1212121', '1X1X1X11', '21212121', '1X1X1X11', '21212121', '1X1X1X11', '21212121', '1111111S']) == [19, 40]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '4321X', '1234X', '4321X', '1234S']) == [21, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '4321X', '1234X', '4321X', '1234S']) == [21, 8]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E2222', '2X2X2', '222X2', '2X2X2', '2222S']) == [14, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E2222', '2X2X2', '222X2', '2X2X2', '2222S']) == [14, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E11111', '1X1X1X', '1X1X1X', '1X1X1X', '1X1X1X', '11111S']) == [9, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E11111', '1X1X1X', '1X1X1X', '1X1X1X', '1X1X1X', '11111S']) == [9, 3]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '11111', '11111', '11111', '1111S']) == [7, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '11111', '11111', '11111', '1111S']) == [7, 70]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456789', '1X11111111', '2121212121', '3131313131', '4141414141', '5151515151', '6161616161', '7171717171', '8181818181', '9191919191S']) == [86, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456789', '1X11111111', '2121212121', '3131313131', '4141414141', '5151515151', '6161616161', '7171717171', '8181818181', '9191919191S']) == [86, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12X12', '234567', '89XS12', '345678', '456789', '56789S']) == [58, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12X12', '234567', '89XS12', '345678', '456789', '56789S']) == [58, 15]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '678X91', '234567', '89X123', '456789', '9XS123']) == [63, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '678X91', '234567', '89X123', '456789', '9XS123']) == [63, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456789', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9XS']) == [56, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456789', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9XS']) == [56, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '1X1X1', '1X1X1', '1111S']) == [6, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '1X1X1', '1X1X1', '1111S']) == [6, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234567', '89X12345', '6789XS12', '3456789S', '456789XS', '56789XS1', '6789XS12']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234567', '89X12345', '6789XS12', '3456789S', '456789XS', '56789XS1', '6789XS12']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12X45', '6789X1', '234567', '89X123', '45678X', '9XS123']) == [56, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12X45', '6789X1', '234567', '89X123', '45678X', '9XS123']) == [56, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E123456789', '987654X789', '87654321X9', '7654321X89', '654321X789', '54321X6789', '4321X56789', '321X456789', '21X3456789', '1XS2345678']) == [125, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E123456789', '987654X789', '87654321X9', '7654321X89', '654321X789', '54321X6789', '4321X56789', '321X456789', '21X3456789', '1XS2345678']) == [125, 1]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1111', '11X11', '1X1X1', '11X11', '1111S']) == [7, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1111', '11X11', '1X1X1', '11X11', '1111S']) == [7, 4]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E12345', '67X89X', '123XS1', '456789', 'X98765', '4321XS']) == [55, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E12345', '67X89X', '123XS1', '456789', 'X98765', '4321XS']) == [55, 2]: {e}')
    
    total += 1
    try:
        result = candidate(board = ['E1234', '1X1X1', '23X32', '1X1X1', '4321S']) == [14, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = ['E1234', '1X1X1', '23X32', '1X1X1', '4321S']) == [14, 2]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(board = ['E123', '45X7', '89XS']) == [21, 1]
    assert candidate(board = ['E11', 'XXX', '11S']) == [0, 0]
    assert candidate(board = ['EX', 'XS']) == [0, 1]
    assert candidate(board = ['E111', '1X11', '1111', '111S']) == [5, 8]
    assert candidate(board = ['E22', '222', '22S']) == [6, 6]
    assert candidate(board = ['E1X', 'X1X', 'X1S']) == [3, 1]
    assert candidate(board = ['E123', '12X3', '21XS']) == [4, 3]
    assert candidate(board = ['E123', '1X21', '21XS']) == [5, 1]
    assert candidate(board = ['EX', '1S']) == [1, 1]
    assert candidate(board = ['E23', '2X2', '12S']) == [7, 1]
    assert candidate(board = ['E111', '1111', '11X1', '111S']) == [5, 8]
    assert candidate(board = ['E12', '1X1', '21S']) == [4, 2]
    assert candidate(board = ['E123', '456X', '789S']) == [28, 1]
    assert candidate(board = ['E123', '4X56', '789S']) == [28, 1]
    assert candidate(board = ['E1X', '1X1', 'S11']) == [3, 2]
    assert candidate(board = ['E1', '1S']) == [1, 2]
    assert candidate(board = ['E123456', '2345678', '345678X', '456789X', '56789XS', '6789XSX']) == [44, 35]
    assert candidate(board = ['E121', '2121', '1212', '1S11']) == [9, 6]
    assert candidate(board = ['E12X4', '56789', 'X1234', '5678X', '9XS12']) == [40, 1]
    assert candidate(board = ['E12345', '6789X1', '234567', '89XS12', '345678']) == [49, 1]
    assert candidate(board = ['E1X1X1X1', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1X', '1X1X1X1S']) == [0, 0]
    assert candidate(board = ['E1234', '56X89', '4X321', '12X56', '789XS']) == [30, 1]
    assert candidate(board = ['E1234567', '23456789', '3456789X', '456789XS', '56789XSX', '6789XSXX', '789XSXXX', '89XSXXXX']) == [0, 0]
    assert candidate(board = ['E1234', '56789', 'X123X', '45678', '9XS12']) == [46, 1]
    assert candidate(board = ['E1X1', '1X1X', '1X1X', '1X1S']) == [4, 1]
    assert candidate(board = ['E2222', '22222', '22X22', '22222', '2222S']) == [14, 34]
    assert candidate(board = ['E11111111', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '111X111X1', '1X1X1X1X1', '11111111S']) == [15, 11]
    assert candidate(board = ['E9876', '9X8X7', '6X5X4', '3X2X1', '4321S']) == [42, 1]
    assert candidate(board = ['E1234567', '89X12345', '6789X123', '456789X1', '23456789', '1234567S', '89XS1234']) == [90, 1]
    assert candidate(board = ['E999', '9X99', '99X9', '999S']) == [45, 4]
    assert candidate(board = ['E12X4', '56789', 'X1234', '56789', 'S1234']) == [52, 1]
    assert candidate(board = ['E123456', '789X123', '456789X', '1234567', '89X1234', '56789XS']) == [63, 1]
    assert candidate(board = ['E111', '1X11', '11X1', '111S']) == [5, 4]
    assert candidate(board = ['E222', '2X22', '2X22', '2X2S']) == [10, 4]
    assert candidate(board = ['E12345', '6X7X89', '1X2X3X', '4X5X6X', '7X8X9X', '12345S']) == [41, 1]
    assert candidate(board = ['E1234', '1X1X1', '21212', '31313', '4141S']) == [16, 2]
    assert candidate(board = ['E1234', '56X78', '9X0X1', '23456', '7XS9E']) == [37, 1]
    assert candidate(board = ['E1234567', '1X2X3X4X', '5X6X7X8X', '9X0X1X2X', '3X4X5X6X', '7X8X9X0X', '1234567S']) == [53, 2]
    assert candidate(board = ['E2222', '2X2X2', '2X2X2', '2X2X2', '2222S']) == [14, 3]
    assert candidate(board = ['E123456', '789X123', '456789X', '1234567', '89XS123', '3456789']) == [70, 1]
    assert candidate(board = ['E1X1X1X1X1X1', '111111111111', '1X1X1X1X1X11', '111X1X1X1X11', '1X1X1X1X1X11', '111X1X1X1X11', '1X1X1X1X1X11', '111X1X1X1X1S']) == [13, 2]
    assert candidate(board = ['E1X1X1X1X1X1X1X1', '1111111111111111', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111X1X1X1X1X1X11', '1X1X1X1X1X1X1X11', '111111111111111S']) == [26, 18]
    assert candidate(board = ['E12X45', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '45678S']) == [43, 1]
    assert candidate(board = ['E1111', '1X1X1', '111X1', '1X1X1', '1111S']) == [7, 4]
    assert candidate(board = ['E1234', '56X78', '9XABC', 'DEFXS']) == [14, 2]
    assert candidate(board = ['E12121', '1X1X11', '212121', '1X1X11', '212121', '11111S']) == [13, 12]
    assert candidate(board = ['E12345', '6789XS', '54321X', '98765X', '43210X', '32109S']) == [55, 1]
    assert candidate(board = ['E12345', '1X1X1X', '212121', '1X1X1X', '32323S']) == [17, 2]
    assert candidate(board = ['E22222', '2X2X22', '222X22', '2X2X22', '222X22', '22222S']) == [18, 11]
    assert candidate(board = ['E11111', '1X1X11', '1X1X11', '1X1X11', '1X1X11', '11111S']) == [9, 8]
    assert candidate(board = ['E12345', '67X9X1', '234567', '89XS12', '345678', '456789']) == [64, 10]
    assert candidate(board = ['E1X1X1X1X1X1X1', '11111111111111', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '111X1X1X1X1X11', '1X1X1X1X1X1X11', '1111111111111S']) == [22, 15]
    assert candidate(board = ['E1234', '56X78', '9X123', '45678', '89XS1']) == [45, 1]
    assert candidate(board = ['E234', '1X12', '21XS', '3456']) == [21, 1]
    assert candidate(board = ['E1111', '1X1X1', '1X1X1', '1X1X1', '1111S']) == [7, 3]
    assert candidate(board = ['E11111', '111111', '111X11', '111111', '111111', '11111S']) == [9, 152]
    assert candidate(board = ['E1111111', '1X1X1X11', '111X1111', '1X1X1X11', '111X1111', '1X1X1X11', '111X1111', '1111111S']) == [13, 28]
    assert candidate(board = ['E12345678910', '1X1X1X1X1X1X11', '212121212121', '1X1X1X1X1X1X11', '323232323232', '1X1X1X1X1X1X11', '414141414141', '1X1X1X1X1X1X11', '515151515151', '1X1X1X1X1X1X11', '616161616161', '1111111111111S']) == [73, 2]
    assert candidate(board = ['E123456789', '987654321X', '123456789X', 'X987654321', '123456789X', 'X987654321', '123456789X', 'X987654321', '123456789X', 'XS12345678']) == [121, 72]
    assert candidate(board = ['E12345', '67X890', '123X45', '678X90', '123X45', '6789XS']) == [45, 1]
    assert candidate(board = ['E12345', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '45678S']) == [43, 1]
    assert candidate(board = ['E1111', '11111', '11X11', '11111', '1111S']) == [7, 34]
    assert candidate(board = ['E11X1', '1X1X1', '1X1X1', '1X1X1', '111XS']) == [0, 0]
    assert candidate(board = ['E111111', '1X1X1X1', '111X111', '1X1X1X1', '111X111', '1X1X1X1', '111111S']) == [11, 8]
    assert candidate(board = ['E1X1X1', '1X1X1X', '1X1X1X', '1X1X1X', '1X1X1S']) == [0, 0]
    assert candidate(board = ['E11111', '1X1X1X', '111X11', '1X1X1X', '11111S']) == [8, 4]
    assert candidate(board = ['E1X1X1X1X1X1X1X1X1', '111111111111111111', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '111X1X1X1X1X1X1X11', '1X1X1X1X1X1X1X1X11', '11111111111111111S']) == [30, 21]
    assert candidate(board = ['E111111', '1X1X1X1', '111X1X1', '1X1X1X1', '111X1X1', '1X1X1X1', '111111S']) == [11, 6]
    assert candidate(board = ['E11X1', '1X1X1', '1X1X1', '1X1X1', '11X1S']) == [6, 1]
    assert candidate(board = ['E123', '21X1', '1X1X', '321S']) == [9, 1]
    assert candidate(board = ['E11111', '1X1X11', '111X11', '1X1X11', '111X11', '11111S']) == [9, 11]
    assert candidate(board = ['E1111', '1X1X1', '11111', '1X1X1', '1111S']) == [7, 6]
    assert candidate(board = ['E1X11', '11X11', '111X1', '1111X', '1111S']) == [7, 19]
    assert candidate(board = ['E123456', '1X2X3X4', '5X6X7X8', '9X0X1X2', '3X4X5X6', '7X8X9XS']) == [35, 1]
    assert candidate(board = ['E12345678', '9X1234567', '89X12345X', '789XS1234', '6789XS123', '56789XS12', '456789XS1', '3456789XS']) == [111, 1]
    assert candidate(board = ['E11111', '1X1X11', '111111', '1X1X1X', '111111', '11XS11']) == [10, 12]
    assert candidate(board = ['E1111111', '1X1X1X11', '11111111', '1X1X1X11', '11111111', '1X1X1X11', '11111111', '11XS1111']) == [14, 90]
    assert candidate(board = ['E123456', '789X123', '456789X', '1234567', '89XS123', '456789S']) == [71, 1]
    assert candidate(board = ['E12345', '1X2X3X', '4X5X6X', '7X8X9X', '1X2X3X', '4567XS']) == [31, 1]
    assert candidate(board = ['E1212121', '1X1X1X11', '21212121', '1X1X1X11', '21212121', '1X1X1X11', '21212121', '1111111S']) == [19, 40]
    assert candidate(board = ['E1234', '4321X', '1234X', '4321X', '1234S']) == [21, 8]
    assert candidate(board = ['E2222', '2X2X2', '222X2', '2X2X2', '2222S']) == [14, 4]
    assert candidate(board = ['E11111', '1X1X1X', '1X1X1X', '1X1X1X', '1X1X1X', '11111S']) == [9, 3]
    assert candidate(board = ['E1111', '11111', '11111', '11111', '1111S']) == [7, 70]
    assert candidate(board = ['E123456789', '1X11111111', '2121212121', '3131313131', '4141414141', '5151515151', '6161616161', '7171717171', '8181818181', '9191919191S']) == [86, 1]
    assert candidate(board = ['E12X12', '234567', '89XS12', '345678', '456789', '56789S']) == [58, 15]
    assert candidate(board = ['E12345', '678X91', '234567', '89X123', '456789', '9XS123']) == [63, 2]
    assert candidate(board = ['E123456789', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9X0', '1X2X3X4X5', '6X7X8X9XS']) == [56, 1]
    assert candidate(board = ['E1111', '1X1X1', '1X1X1', '1111S']) == [6, 2]
    assert candidate(board = ['E1234567', '89X12345', '6789XS12', '3456789S', '456789XS', '56789XS1', '6789XS12']) == [0, 0]
    assert candidate(board = ['E12X45', '6789X1', '234567', '89X123', '45678X', '9XS123']) == [56, 4]
    assert candidate(board = ['E123456789', '987654X789', '87654321X9', '7654321X89', '654321X789', '54321X6789', '4321X56789', '321X456789', '21X3456789', '1XS2345678']) == [125, 1]
    assert candidate(board = ['E1111', '11X11', '1X1X1', '11X11', '1111S']) == [7, 4]
    assert candidate(board = ['E12345', '67X89X', '123XS1', '456789', 'X98765', '4321XS']) == [55, 2]
    assert candidate(board = ['E1234', '1X1X1', '23X32', '1X1X1', '4321S']) == [14, 2]


