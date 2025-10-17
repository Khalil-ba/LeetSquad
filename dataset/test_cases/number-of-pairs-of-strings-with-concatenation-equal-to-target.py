def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = ['777', '7', '77', '77'],target = "7777") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['777', '7', '77', '77'],target = "7777") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '11', '1'],target = "101") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '11', '1'],target = "101") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '56', '78', '9'],target = "123456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '56', '78', '9'],target = "123456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['99', '9', '999'],target = "9999") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['99', '9', '999'],target = "9999") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['50', '2', '5', '0'],target = "5025") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['50', '2', '5', '0'],target = "5025") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '100', '1'],target = "10100") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '100', '1'],target = "10100") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '4', '12', '34'],target = "1234") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '4', '12', '34'],target = "1234") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['50', '5', '500'],target = "505") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['50', '5', '500'],target = "505") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '1', '1'],target = "11") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '1', '1'],target = "11") == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '234', '345', '456', '567', '678', '789', '890'],target = "123234") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '234', '345', '456', '567', '678', '789', '890'],target = "123234") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['66', '666', '6666', '66666'],target = "66666666") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['66', '666', '6666', '66666'],target = "66666666") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['33', '3', '333', '3333', '33'],target = "333333") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['33', '3', '333', '3333', '33'],target = "333333") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['555', '55', '5', '5555'],target = "555555") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['555', '55', '5', '5555'],target = "555555") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '1', '2', '2', '3', '3'],target = "11") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '1', '2', '2', '3', '3'],target = "11") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['78', '87', '7', '8'],target = "7887") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['78', '87', '7', '8'],target = "7887") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['7777', '777', '77', '7'],target = "7777777") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['7777', '777', '77', '7'],target = "7777777") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['0', '00', '000', '0000'],target = "0000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['0', '00', '000', '0000'],target = "0000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['001', '010', '100', '1'],target = "1001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['001', '010', '100', '1'],target = "1001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['15', '51', '1515', '151', '515'],target = "151515") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['15', '51', '1515', '151', '515'],target = "151515") == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '01', '100', '001', '1000', '0001'],target = "1001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '01', '100', '001', '1000', '0001'],target = "1001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['789', '897', '978', '78', '89', '97'],target = "789897") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['789', '897', '978', '78', '89', '97'],target = "789897") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '20', '30', '40', '50'],target = "1020") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '20', '30', '40', '50'],target = "1020") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '5678', '4321', '8765'],target = "12345678") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '5678', '4321', '8765'],target = "12345678") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111', '222', '333', '444', '555', '666', '777', '888', '999'],target = "111222") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111', '222', '333', '444', '555', '666', '777', '888', '999'],target = "111222") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['5', '55', '555', '5555', '55555'],target = "555555") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['5', '55', '555', '5555', '55555'],target = "555555") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['9', '99', '999', '9999'],target = "999999") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['9', '99', '999', '9999'],target = "999999") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['18', '81', '181', '818', '1818'],target = "181818") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['18', '81', '181', '818', '1818'],target = "181818") == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['20', '02', '2', '2002'],target = "200202") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['20', '02', '2', '2002'],target = "200202") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['5', '55', '555', '5555'],target = "55555") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['5', '55', '555', '5555'],target = "55555") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['9', '99', '999', '9999', '99999'],target = "999999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['9', '99', '999', '9999', '99999'],target = "999999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['90', '09', '9', '0'],target = "9009") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['90', '09', '9', '0'],target = "9009") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],target = "12") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],target = "12") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111', '222', '333', '111', '222'],target = "111222") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111', '222', '333', '111', '222'],target = "111222") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['222', '2222', '2', '22', '22222'],target = "22222222") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['222', '2222', '2', '22', '22222'],target = "22222222") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '5678', '12', '34', '56', '78'],target = "12345678") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '5678', '12', '34', '56', '78'],target = "12345678") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111', '222', '333', '444'],target = "111222") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111', '222', '333', '444'],target = "111222") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['98765', '4321', '9876', '54321'],target = "987654321") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['98765', '4321', '9876', '54321'],target = "987654321") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['90', '909', '09', '9'],target = "90909") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['90', '909', '09', '9'],target = "90909") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '09'],target = "09") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '09'],target = "09") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['100000', '10000', '1000', '100', '10', '1'],target = "10000010000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['100000', '10000', '1000', '100', '10', '1'],target = "10000010000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['0', '0', '0', '0'],target = "00") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['0', '0', '0', '0'],target = "00") == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['8', '88', '888', '8888'],target = "88888") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['8', '88', '888', '8888'],target = "88888") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '456', '789', '0', '1', '2'],target = "123456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '456', '789', '0', '1', '2'],target = "123456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111111', '11111', '1111', '111', '11'],target = "111111111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111111', '11111', '1111', '111', '11'],target = "111111111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['100', '200', '300', '400', '500'],target = "100200") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['100', '200', '300', '400', '500'],target = "100200") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '234', '345', '456', '567'],target = "123234") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '234', '345', '456', '567'],target = "123234") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '4321', '2341', '3412', '5678', '8765', '6785', '7856'],target = "12344321") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '4321', '2341', '3412', '5678', '8765', '6785', '7856'],target = "12344321") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '345', '567', '789'],target = "123345") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '345', '567', '789'],target = "123345") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '20', '30', '40', '50'],target = "2030") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '20', '30', '40', '50'],target = "2030") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['0000', '000', '00', '0'],target = "00000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['0000', '000', '00', '0'],target = "00000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['0001', '10', '01', '1'],target = "00011") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['0001', '10', '01', '1'],target = "00011") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '456', '789', '0'],target = "123456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '456', '789', '0'],target = "123456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['16', '61', '161', '6', '1661'],target = "166161") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['16', '61', '161', '6', '1661'],target = "166161") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['21', '12', '22', '11', '2112'],target = "211221") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['21', '12', '22', '11', '2112'],target = "211221") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['42', '424', '2', '4'],target = "4242") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['42', '424', '2', '4'],target = "4242") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['777', '77', '7', '7777'],target = "777777") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['777', '77', '7', '7777'],target = "777777") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['11', '11', '11', '11', '11'],target = "1111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['11', '11', '11', '11', '11'],target = "1111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['19', '91', '191', '9', '1991'],target = "199191") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['19', '91', '191', '9', '1991'],target = "199191") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['987654321', '123456789', '1234', '4321'],target = "987654321123456789") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['987654321', '123456789', '1234', '4321'],target = "987654321123456789") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111111', '1111', '111', '11', '1'],target = "111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111111', '1111', '111', '11', '1'],target = "111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],target = "12") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],target = "12") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],target = "11") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],target = "11") == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['101', '101', '101', '101'],target = "101101") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['101', '101', '101', '101'],target = "101101") == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['8888', '888', '88', '8', '88', '888', '8888'],target = "88888888") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['8888', '888', '88', '8', '88', '888', '8888'],target = "88888888") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['22', '2', '222', '2222'],target = "222222") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['22', '2', '222', '2222'],target = "222222") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123456', '654321', '1234', '4321', '5678', '8765'],target = "123456654321") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123456', '654321', '1234', '4321', '5678', '8765'],target = "123456654321") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '21', '11', '22'],target = "1221") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '21', '11', '22'],target = "1221") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['55', '555', '5555', '55555'],target = "5555555") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['55', '555', '5555', '55555'],target = "5555555") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['14', '41', '144', '4'],target = "1441") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['14', '41', '144', '4'],target = "1441") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['8', '88', '888', '8888', '88888', '888888'],target = "8888888") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['8', '88', '888', '8888', '88888', '888888'],target = "8888888") == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '23', '34', '45', '56'],target = "2345") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '23', '34', '45', '56'],target = "2345") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12345', '54321', '123', '321', '12', '21'],target = "1234554321") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12345', '54321', '123', '321', '12', '21'],target = "1234554321") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['55', '5', '555', '5555'],target = "55555") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['55', '5', '555', '5555'],target = "55555") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['987', '654', '321', '654'],target = "987654") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['987', '654', '321', '654'],target = "987654") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111', '11', '1', '1111', '11111'],target = "1111111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111', '11', '1', '1111', '11111'],target = "1111111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '4321', '2341', '3412'],target = "12344321") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '4321', '2341', '3412'],target = "12344321") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['101', '01', '10', '1'],target = "1010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['101', '01', '10', '1'],target = "1010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['8', '88', '888', '8888', '88888'],target = "888888888") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['8', '88', '888', '8888', '88888'],target = "888888888") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['6', '66', '666', '6666'],target = "666666") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['6', '66', '666', '6666'],target = "666666") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '01', '0', '1'],target = "1001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '01', '0', '1'],target = "1001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '20', '30', '40', '50', '60', '70', '80', '90'],target = "1020") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '20', '30', '40', '50', '60', '70', '80', '90'],target = "1020") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111', '11', '1', '1111'],target = "111111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111', '11', '1', '1111'],target = "111111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1', '2', '3', '4', '5'],target = "12") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1', '2', '3', '4', '5'],target = "12") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['111', '222', '112', '121', '211'],target = "111222") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['111', '222', '112', '121', '211'],target = "111222") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12345', '23456', '34567', '45678', '56789'],target = "1234523456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12345', '23456', '34567', '45678', '56789'],target = "1234523456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '12', '12', '12'],target = "1212") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '12', '12', '12'],target = "1212") == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['555', '55', '5', '5555', '55555'],target = "5555555") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['555', '55', '5', '5555', '55555'],target = "5555555") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['23', '32', '232', '2', '3223'],target = "233223") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['23', '32', '232', '2', '3223'],target = "233223") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['11', '22', '33', '44', '55', '66', '77', '88', '99'],target = "1122") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['11', '22', '33', '44', '55', '66', '77', '88', '99'],target = "1122") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '321', '213', '132', '231', '312'],target = "123213") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '321', '213', '132', '231', '312'],target = "123213") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '21', '121', '212'],target = "1212") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '21', '121', '212'],target = "1212") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['555', '555', '555', '555', '555'],target = "555555") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['555', '555', '555', '555', '555'],target = "555555") == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['89', '98', '8998', '9889'],target = "899889") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['89', '98', '8998', '9889'],target = "899889") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['22', '222', '2', '2222'],target = "222222") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['22', '222', '2', '2222'],target = "222222") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['23', '32', '123', '456', '654', '321'],target = "23456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['23', '32', '123', '456', '654', '321'],target = "23456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['9876', '8765', '7654', '6543', '5432', '4321', '3210', '2109'],target = "98768765") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['9876', '8765', '7654', '6543', '5432', '4321', '3210', '2109'],target = "98768765") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1010', '0101', '10', '01', '101', '010'],target = "10100101") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1010', '0101', '10', '01', '101', '010'],target = "10100101") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['90', '80', '70', '60'],target = "7080") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['90', '80', '70', '60'],target = "7080") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['101', '010', '10', '01'],target = "101010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['101', '010', '10', '01'],target = "101010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['9', '99', '999', '9999'],target = "99999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['9', '99', '999', '9999'],target = "99999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['5050', '50', '5', '500', '5000'],target = "505050") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['5050', '50', '5', '500', '5000'],target = "505050") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '21', '121', '112'],target = "12112") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '21', '121', '112'],target = "12112") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['13', '31', '1', '3'],target = "1331") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['13', '31', '1', '3'],target = "1331") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['2', '22', '222', '2222', '22222'],target = "222222") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['2', '22', '222', '2222', '22222'],target = "222222") == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['2020', '20', '2', '0202'],target = "202020") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['2020', '20', '2', '0202'],target = "202020") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '23', '34', '45', '56', '67', '78', '89'],target = "1223") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '23', '34', '45', '56', '67', '78', '89'],target = "1223") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['999', '99', '9', '9999'],target = "9999999") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['999', '99', '9', '9999'],target = "9999999") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['00', '0', '000', '0000'],target = "000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['00', '0', '000', '0000'],target = "000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['17', '71', '1717', '717', '177'],target = "171717") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['17', '71', '1717', '717', '177'],target = "171717") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['987', '876', '765', '654', '543'],target = "987876") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['987', '876', '765', '654', '543'],target = "987876") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '23', '34', '45', '56', '67', '78', '89', '90'],target = "1223") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '23', '34', '45', '56', '67', '78', '89', '90'],target = "1223") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '12', '12', '12', '12', '12', '12', '12', '12', '12'],target = "1212") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '12', '12', '12', '12', '12', '12', '12', '12', '12'],target = "1212") == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['00', '000', '0000', '00000'],target = "00000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['00', '000', '0000', '00000'],target = "00000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1010', '10', '1', '101', '10101'],target = "10101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1010', '10', '1', '101', '10101'],target = "10101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12', '23', '34', '45', '56'],target = "1223") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12', '23', '34', '45', '56'],target = "1223") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['55', '5', '555', '5555'],target = "5555") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['55', '5', '555', '5555'],target = "5555") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '456', '12', '3456'],target = "123456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '456', '12', '3456'],target = "123456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['45', '54', '4', '5'],target = "4554") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['45', '54', '4', '5'],target = "4554") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['10', '01', '100', '1'],target = "101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['10', '01', '100', '1'],target = "101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['100', '10', '1', '1000'],target = "1001000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['100', '10', '1', '1000'],target = "1001000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1111', '111', '11', '1'],target = "11111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1111', '111', '11', '1'],target = "11111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['11', '111', '1111', '11111'],target = "111111111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['11', '111', '1111', '11111'],target = "111111111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['9876', '8769', '7698', '6987', '987', '876', '769', '698'],target = "98768769") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['9876', '8769', '7698', '6987', '987', '876', '769', '698'],target = "98768769") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['12345', '67890', '123', '4567890'],target = "1234567890") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['12345', '67890', '123', '4567890'],target = "1234567890") == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9'],target = "99") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9'],target = "99") == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['123', '456', '789', '1234'],target = "123456") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['123', '456', '789', '1234'],target = "123456") == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = ['1234', '5678', '91011', '121314'],target = "12345678") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = ['1234', '5678', '91011', '121314'],target = "12345678") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = ['777', '7', '77', '77'],target = "7777") == 4
    assert candidate(nums = ['10', '11', '1'],target = "101") == 1
    assert candidate(nums = ['1234', '56', '78', '9'],target = "123456") == 1
    assert candidate(nums = ['99', '9', '999'],target = "9999") == 2
    assert candidate(nums = ['50', '2', '5', '0'],target = "5025") == 0
    assert candidate(nums = ['10', '100', '1'],target = "10100") == 1
    assert candidate(nums = ['123', '4', '12', '34'],target = "1234") == 2
    assert candidate(nums = ['50', '5', '500'],target = "505") == 1
    assert candidate(nums = ['1', '1', '1'],target = "11") == 6
    assert candidate(nums = ['123', '234', '345', '456', '567', '678', '789', '890'],target = "123234") == 1
    assert candidate(nums = ['66', '666', '6666', '66666'],target = "66666666") == 2
    assert candidate(nums = ['33', '3', '333', '3333', '33'],target = "333333") == 4
    assert candidate(nums = ['555', '55', '5', '5555'],target = "555555") == 2
    assert candidate(nums = ['1', '1', '2', '2', '3', '3'],target = "11") == 2
    assert candidate(nums = ['78', '87', '7', '8'],target = "7887") == 1
    assert candidate(nums = ['7777', '777', '77', '7'],target = "7777777") == 2
    assert candidate(nums = ['0', '00', '000', '0000'],target = "0000") == 2
    assert candidate(nums = ['001', '010', '100', '1'],target = "1001") == 2
    assert candidate(nums = ['15', '51', '1515', '151', '515'],target = "151515") == 3
    assert candidate(nums = ['10', '01', '100', '001', '1000', '0001'],target = "1001") == 1
    assert candidate(nums = ['789', '897', '978', '78', '89', '97'],target = "789897") == 1
    assert candidate(nums = ['10', '20', '30', '40', '50'],target = "1020") == 1
    assert candidate(nums = ['1234', '5678', '4321', '8765'],target = "12345678") == 1
    assert candidate(nums = ['111', '222', '333', '444', '555', '666', '777', '888', '999'],target = "111222") == 1
    assert candidate(nums = ['5', '55', '555', '5555', '55555'],target = "555555") == 4
    assert candidate(nums = ['9', '99', '999', '9999'],target = "999999") == 2
    assert candidate(nums = ['18', '81', '181', '818', '1818'],target = "181818") == 3
    assert candidate(nums = ['20', '02', '2', '2002'],target = "200202") == 1
    assert candidate(nums = ['5', '55', '555', '5555'],target = "55555") == 4
    assert candidate(nums = ['9', '99', '999', '9999', '99999'],target = "999999") == 4
    assert candidate(nums = ['90', '09', '9', '0'],target = "9009") == 1
    assert candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],target = "12") == 1
    assert candidate(nums = ['111', '222', '333', '111', '222'],target = "111222") == 4
    assert candidate(nums = ['222', '2222', '2', '22', '22222'],target = "22222222") == 2
    assert candidate(nums = ['1234', '5678', '12', '34', '56', '78'],target = "12345678") == 1
    assert candidate(nums = ['111', '222', '333', '444'],target = "111222") == 1
    assert candidate(nums = ['98765', '4321', '9876', '54321'],target = "987654321") == 2
    assert candidate(nums = ['90', '909', '09', '9'],target = "90909") == 2
    assert candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '09'],target = "09") == 1
    assert candidate(nums = ['100000', '10000', '1000', '100', '10', '1'],target = "10000010000") == 1
    assert candidate(nums = ['0', '0', '0', '0'],target = "00") == 12
    assert candidate(nums = ['8', '88', '888', '8888'],target = "88888") == 4
    assert candidate(nums = ['123', '456', '789', '0', '1', '2'],target = "123456") == 1
    assert candidate(nums = ['111111', '11111', '1111', '111', '11'],target = "111111111") == 4
    assert candidate(nums = ['100', '200', '300', '400', '500'],target = "100200") == 1
    assert candidate(nums = ['123', '234', '345', '456', '567'],target = "123234") == 1
    assert candidate(nums = ['1234', '4321', '2341', '3412', '5678', '8765', '6785', '7856'],target = "12344321") == 1
    assert candidate(nums = ['123', '345', '567', '789'],target = "123345") == 1
    assert candidate(nums = ['10', '20', '30', '40', '50'],target = "2030") == 1
    assert candidate(nums = ['0000', '000', '00', '0'],target = "00000000") == 0
    assert candidate(nums = ['0001', '10', '01', '1'],target = "00011") == 1
    assert candidate(nums = ['123', '456', '789', '0'],target = "123456") == 1
    assert candidate(nums = ['16', '61', '161', '6', '1661'],target = "166161") == 1
    assert candidate(nums = ['21', '12', '22', '11', '2112'],target = "211221") == 1
    assert candidate(nums = ['42', '424', '2', '4'],target = "4242") == 1
    assert candidate(nums = ['777', '77', '7', '7777'],target = "777777") == 2
    assert candidate(nums = ['11', '11', '11', '11', '11'],target = "1111") == 20
    assert candidate(nums = ['19', '91', '191', '9', '1991'],target = "199191") == 1
    assert candidate(nums = ['987654321', '123456789', '1234', '4321'],target = "987654321123456789") == 1
    assert candidate(nums = ['111111', '1111', '111', '11', '1'],target = "111111111111") == 0
    assert candidate(nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],target = "12") == 1
    assert candidate(nums = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],target = "11") == 90
    assert candidate(nums = ['101', '101', '101', '101'],target = "101101") == 12
    assert candidate(nums = ['8888', '888', '88', '8', '88', '888', '8888'],target = "88888888") == 2
    assert candidate(nums = ['22', '2', '222', '2222'],target = "222222") == 2
    assert candidate(nums = ['123456', '654321', '1234', '4321', '5678', '8765'],target = "123456654321") == 1
    assert candidate(nums = ['12', '21', '11', '22'],target = "1221") == 1
    assert candidate(nums = ['55', '555', '5555', '55555'],target = "5555555") == 4
    assert candidate(nums = ['14', '41', '144', '4'],target = "1441") == 1
    assert candidate(nums = ['8', '88', '888', '8888', '88888', '888888'],target = "8888888") == 6
    assert candidate(nums = ['12', '23', '34', '45', '56'],target = "2345") == 1
    assert candidate(nums = ['12345', '54321', '123', '321', '12', '21'],target = "1234554321") == 1
    assert candidate(nums = ['55', '5', '555', '5555'],target = "55555") == 4
    assert candidate(nums = ['987', '654', '321', '654'],target = "987654") == 2
    assert candidate(nums = ['111', '11', '1', '1111', '11111'],target = "1111111") == 4
    assert candidate(nums = ['1234', '4321', '2341', '3412'],target = "12344321") == 1
    assert candidate(nums = ['101', '01', '10', '1'],target = "1010") == 0
    assert candidate(nums = ['8', '88', '888', '8888', '88888'],target = "888888888") == 2
    assert candidate(nums = ['6', '66', '666', '6666'],target = "666666") == 2
    assert candidate(nums = ['10', '01', '0', '1'],target = "1001") == 1
    assert candidate(nums = ['10', '20', '30', '40', '50', '60', '70', '80', '90'],target = "1020") == 1
    assert candidate(nums = ['111', '11', '1', '1111'],target = "111111") == 2
    assert candidate(nums = ['1', '2', '3', '4', '5'],target = "12") == 1
    assert candidate(nums = ['111', '222', '112', '121', '211'],target = "111222") == 1
    assert candidate(nums = ['12345', '23456', '34567', '45678', '56789'],target = "1234523456") == 1
    assert candidate(nums = ['12', '12', '12', '12'],target = "1212") == 12
    assert candidate(nums = ['555', '55', '5', '5555', '55555'],target = "5555555") == 4
    assert candidate(nums = ['23', '32', '232', '2', '3223'],target = "233223") == 1
    assert candidate(nums = ['11', '22', '33', '44', '55', '66', '77', '88', '99'],target = "1122") == 1
    assert candidate(nums = ['123', '321', '213', '132', '231', '312'],target = "123213") == 1
    assert candidate(nums = ['12', '21', '121', '212'],target = "1212") == 0
    assert candidate(nums = ['555', '555', '555', '555', '555'],target = "555555") == 20
    assert candidate(nums = ['89', '98', '8998', '9889'],target = "899889") == 2
    assert candidate(nums = ['22', '222', '2', '2222'],target = "222222") == 2
    assert candidate(nums = ['23', '32', '123', '456', '654', '321'],target = "23456") == 1
    assert candidate(nums = ['9876', '8765', '7654', '6543', '5432', '4321', '3210', '2109'],target = "98768765") == 1
    assert candidate(nums = ['1010', '0101', '10', '01', '101', '010'],target = "10100101") == 1
    assert candidate(nums = ['90', '80', '70', '60'],target = "7080") == 1
    assert candidate(nums = ['101', '010', '10', '01'],target = "101010") == 1
    assert candidate(nums = ['9', '99', '999', '9999'],target = "99999999") == 0
    assert candidate(nums = ['5050', '50', '5', '500', '5000'],target = "505050") == 2
    assert candidate(nums = ['12', '21', '121', '112'],target = "12112") == 2
    assert candidate(nums = ['13', '31', '1', '3'],target = "1331") == 1
    assert candidate(nums = ['2', '22', '222', '2222', '22222'],target = "222222") == 4
    assert candidate(nums = ['2020', '20', '2', '0202'],target = "202020") == 2
    assert candidate(nums = ['12', '23', '34', '45', '56', '67', '78', '89'],target = "1223") == 1
    assert candidate(nums = ['999', '99', '9', '9999'],target = "9999999") == 2
    assert candidate(nums = ['00', '0', '000', '0000'],target = "000000") == 2
    assert candidate(nums = ['17', '71', '1717', '717', '177'],target = "171717") == 2
    assert candidate(nums = ['987', '876', '765', '654', '543'],target = "987876") == 1
    assert candidate(nums = ['12', '23', '34', '45', '56', '67', '78', '89', '90'],target = "1223") == 1
    assert candidate(nums = ['12', '12', '12', '12', '12', '12', '12', '12', '12', '12'],target = "1212") == 90
    assert candidate(nums = ['00', '000', '0000', '00000'],target = "00000000") == 2
    assert candidate(nums = ['1010', '10', '1', '101', '10101'],target = "10101010") == 0
    assert candidate(nums = ['12', '23', '34', '45', '56'],target = "1223") == 1
    assert candidate(nums = ['55', '5', '555', '5555'],target = "5555") == 2
    assert candidate(nums = ['1234', '456', '12', '3456'],target = "123456") == 1
    assert candidate(nums = ['45', '54', '4', '5'],target = "4554") == 1
    assert candidate(nums = ['10', '01', '100', '1'],target = "101") == 2
    assert candidate(nums = ['100', '10', '1', '1000'],target = "1001000") == 1
    assert candidate(nums = ['1111', '111', '11', '1'],target = "11111111") == 0
    assert candidate(nums = ['11', '111', '1111', '11111'],target = "111111111") == 2
    assert candidate(nums = ['9876', '8769', '7698', '6987', '987', '876', '769', '698'],target = "98768769") == 1
    assert candidate(nums = ['12345', '67890', '123', '4567890'],target = "1234567890") == 2
    assert candidate(nums = ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9'],target = "99") == 90
    assert candidate(nums = ['123', '456', '789', '1234'],target = "123456") == 1
    assert candidate(nums = ['1234', '5678', '91011', '121314'],target = "12345678") == 1


