def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(deadends = [],target = "1111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = [],target = "1111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333'],target = "4444") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333'],target = "4444") == 16: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0003', '0004'],target = "0005") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0003', '0004'],target = "0005") == 5: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0011', '0101', '1001', '1101', '0111', '0110', '1010', '1110', '1100'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0011', '0101', '1001', '1101', '0111', '0110', '1010', '1110', '1100'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '1101', '1011', '0111'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '1101', '1011', '0111'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9998', '9997', '9996', '9995'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9998', '9997', '9996', '9995'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000'],target = "1111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000'],target = "1111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444'],target = "5555") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444'],target = "5555") == 20: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['8888'],target = "0009") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['8888'],target = "0009") == 1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0002', '0020', '0200', '2000'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0002', '0020', '0200', '2000'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0201', '0101', '0102', '1212', '2002'],target = "0202") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0201', '0101', '0102', '1212', '2002'],target = "0202") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '1101', '1011', '0111'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '1101', '1011', '0111'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111'],target = "1112") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111'],target = "1112") == 5: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'],target = "8888") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'],target = "8888") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = [],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = [],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000'],target = "8888") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000'],target = "8888") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9999'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9999'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5555") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5555") == 20: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678'],target = "8765") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678'],target = "8765") == 14: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '4321', '2143', '3412', '0987', '7890', '8709', '9087'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '4321', '2143', '3412', '0987', '7890', '8709', '9087'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', '0000'],target = "1234") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', '0000'],target = "1234") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0011', '0110', '1100', '1001', '1112', '1211', '2111'],target = "2222") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0011', '0110', '1100', '1001', '1112', '1211', '2111'],target = "2222") == 8: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1000', '0100', '0010', '0001', '0011', '0110', '1010', '1100', '1110'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1000', '0100', '0010', '0001', '0011', '0110', '1010', '1100', '1110'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0009', '0018', '0108', '0117', '0126', '0135', '0144', '0153', '0162', '0171'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0009', '0018', '0108', '0117', '0126', '0135', '0144', '0153', '0162', '0171'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0101', '1010', '1100', '1111'],target = "0011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0101', '1010', '1100', '1111'],target = "0011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '1111', '2222', '3333', '4444'],target = "5555") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '1111', '2222', '3333', '4444'],target = "5555") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '1000', '0100', '0011', '1100', '0110', '1010'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '1000', '0100', '0011', '1100', '0110', '1010'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '1112', '2223', '3334', '4445', '5556', '6667', '7778', '8889'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '1112', '2223', '3334', '4445', '5556', '6667', '7778', '8889'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0123', '9876', '5432', '1357', '2468', '0909', '1111', '2222', '3333'],target = "4444") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0123', '9876', '5432', '1357', '2468', '0909', '1111', '2222', '3333'],target = "4444") == 16: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9998', '9989', '9899', '8999', '0000', '1111', '2222', '3333', '4444', '5555'],target = "6789") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9998', '9989', '9899', '8999', '0000', '1111', '2222', '3333', '4444', '5555'],target = "6789") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "1111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "1111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "9999") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "9999") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0100'],target = "0011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0100'],target = "0011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9999', '8888', '7777', '6666', '5555', '4444', '3333', '2222', '1111'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9999', '8888', '7777', '6666', '5555', '4444', '3333', '2222', '1111'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "1000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "1000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', '1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765', '6789', '9876', '7890', '0987', '8790', '9087', '0879'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', '1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765', '6789', '9876', '7890', '0987', '8790', '9087', '0879'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '9999', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "1234") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '9999', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "1234") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0011', '0101', '1001', '1100', '1110', '1101'],target = "1111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0011', '0101', '1001', '1100', '1110', '1101'],target = "1111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0100'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0100'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1000', '0100', '0010', '0001', '2000', '0200', '0020', '0002'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1000', '0100', '0010', '0001', '2000', '0200', '0020', '0002'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '0009', '0090', '0900', '9000', '1111', '2222', '3333', '4444'],target = "5555") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '0009', '0090', '0900', '9000', '1111', '2222', '3333', '4444'],target = "5555") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0010', '0100', '0001', '0110', '1001', '1100', '1111', '0000'],target = "0101") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0010', '0100', '0001', '0110', '1001', '1100', '1111', '0000'],target = "0101") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0010', '0020', '0100', '0200', '1000', '2000', '0003', '0030', '0300', '3000'],target = "0004") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0010', '0020', '0100', '0200', '1000', '2000', '0003', '0030', '0300', '3000'],target = "0004") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000', '0111', '1110', '1101', '1011', '2220', '2202', '2022', '0222'],target = "0202") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000', '0111', '1110', '1101', '1011', '2220', '2202', '2022', '0222'],target = "0202") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '4321', '2143', '3412'],target = "5678") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '4321', '2143', '3412'],target = "5678") == 14: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123', '0234', '1345', '2456', '3567', '4678', '5789', '6890', '7901', '8012', '9123'],target = "4567") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123', '0234', '1345', '2456', '3567', '4678', '5789', '6890', '7901', '8012', '9123'],target = "4567") == 16: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000', '1234', '4321', '5678', '8765', '9999'],target = "8888") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000', '1234', '4321', '5678', '8765', '9999'],target = "8888") == 8: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9999', '8888', '7777', '6666', '5555'],target = "4444") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9999', '8888', '7777', '6666', '5555'],target = "4444") == 16: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0002', '0020', '0200', '2000', '0013', '0130', '1300', '3000', '0112', '1120', '1201', '2011', '1011', '0110', '0101', '1010', '0011'],target = "1111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0002', '0020', '0200', '2000', '0013', '0130', '1300', '3000', '0112', '1120', '1201', '2011', '1011', '0110', '0101', '1010', '0011'],target = "1111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '1110', '1101', '1011', '0111', '2222', '2221', '2212', '2122', '1222', '3333', '3332', '3323', '3233', '2333', '4444', '4443', '4434', '4344', '3444'],target = "5555") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '1110', '1101', '1011', '0111', '2222', '2221', '2212', '2122', '1222', '3333', '3332', '3323', '3233', '2333', '4444', '4443', '4434', '4344', '3444'],target = "5555") == 20: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9998', '9989', '9899', '8999', '0001', '0010', '0100', '1000'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9998', '9989', '9899', '8999', '0001', '0010', '0100', '1000'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '1101', '1011', '0111', '2220', '2202', '2022', '0222', '3330', '3303', '3033', '0333'],target = "4444") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '1101', '1011', '0111', '2220', '2202', '2022', '0222', '3330', '3303', '3033', '0333'],target = "4444") == 16: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0009', '0018', '0108', '0117', '0126', '0135', '0144', '0153', '0162', '0171', '0800', '0900', '1800', '1900', '2800', '2900', '3800', '3900', '4800', '4900', '5800', '5900', '6800', '6900', '7800', '7900', '8800', '8900', '9800', '9900'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0009', '0018', '0108', '0117', '0126', '0135', '0144', '0153', '0162', '0171', '0800', '0900', '1800', '1900', '2800', '2900', '3800', '3900', '4800', '4900', '5800', '5900', '6800', '6900', '7800', '7900', '8800', '8900', '9800', '9900'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000', '1110', '1101', '1011', '0111'],target = "1111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000', '1110', '1101', '1011', '0111'],target = "1111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '1234', '5678', '9999'],target = "4321") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '1234', '5678', '9999'],target = "4321") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0010', '0020', '0030', '0040', '0050'],target = "0060") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0010', '0020', '0030', '0040', '0050'],target = "0060") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '1101', '1011', '0111', '0011', '0101', '0110'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '1101', '1011', '0111', '0011', '0101', '0110'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000', '1110', '1101', '1011', '0111', '0002', '0020'],target = "3333") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000', '1110', '1101', '1011', '0111', '0002', '0020'],target = "3333") == 14: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0011', '1100', '2211', '3322', '4433', '5544', '6655', '7766', '8877'],target = "9988") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0011', '1100', '2211', '3322', '4433', '5544', '6655', '7766', '8877'],target = "9988") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '0010', '0100', '0110', '1000', '1010', '1100', '1110', '0001', '0011', '0101', '0111', '1001', '1011', '1101'],target = "1111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '0010', '0100', '0110', '1000', '1010', '1100', '1110', '0001', '0011', '0101', '0111', '1001', '1011', '1101'],target = "1111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0010', '0100', '0111', '1000', '1001', '1010', '1100', '1111', '0001', '0011', '0110', '1101', '0101', '1011'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0010', '0100', '0111', '1000', '1001', '1010', '1100', '1111', '0001', '0011', '0110', '1101', '0101', '1011'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0011', '0111', '1111', '0002', '0020', '0200', '2000', '0003', '0030', '0300', '3000'],target = "0101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0011', '0111', '1111', '0002', '0020', '0200', '2000', '0003', '0030', '0300', '3000'],target = "0101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1112', '1121', '1211', '2111', '2221', '2212', '2122', '1222'],target = "2222") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1112', '1121', '1211', '2111', '2221', '2212', '2122', '1222'],target = "2222") == 10: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['8888', '8887', '8878', '8788', '7888', '9999', '9998', '9989', '9899', '8999'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['8888', '8887', '8878', '8788', '7888', '9999', '9998', '9989', '9899', '8999'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0010', '0100', '1000', '0001', '0002', '0020', '0200', '2000'],target = "0003") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0010', '0100', '1000', '0001', '0002', '0020', '0200', '2000'],target = "0003") == 5: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '0011', '0101', '0110', '1001', '1010', '1100', '1111', '2222'],target = "3333") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '0011', '0101', '0110', '1001', '1010', '1100', '1111', '2222'],target = "3333") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0009', '0010', '0090', '0100', '0900', '1000', '9000', '0002', '0020', '0200', '2000', '0008', '0080', '0800', '8000'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0009', '0010', '0090', '0100', '0900', '1000', '9000', '0002', '0020', '0200', '2000', '0008', '0080', '0800', '8000'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0009', '0018', '0027', '0036', '0045', '0054', '0063', '0072', '0081'],target = "0090") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0009', '0018', '0027', '0036', '0045', '0054', '0063', '0072', '0081'],target = "0090") == 1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['8888', '9999', '0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777'],target = "0001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['8888', '9999', '0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777'],target = "0001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0101', '1010', '1111', '0011', '1100', '1001', '0110', '0001', '0010', '0100'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0101', '1010', '1111', '0011', '1100', '1001', '0110', '0001', '0010', '0100'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "1234") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "1234") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "9999") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "9999") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '1112', '2223', '3334', '4445', '5556', '6667', '7778', '8889'],target = "4321") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '1112', '2223', '3334', '4445', '5556', '6667', '7778', '8889'],target = "4321") == 10: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "1000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "1000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '0010', '0020', '0030', '0040', '0050', '0060', '0070', '0080', '0090'],target = "0009") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '0010', '0020', '0030', '0040', '0050', '0060', '0070', '0080', '0090'],target = "0009") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0123', '4567', '8901', '2345', '6789', '0987', '5432', '1098', '3210'],target = "1111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0123', '4567', '8901', '2345', '6789', '0987', '5432', '1098', '3210'],target = "1111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '1101', '1011', '0111', '2222', '3333', '4444', '5555', '6666', '7777'],target = "1234") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '1101', '1011', '0111', '2222', '3333', '4444', '5555', '6666', '7777'],target = "1234") == 10: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890'],target = "9876") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890'],target = "9876") == 10: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9998', '9989', '9899', '8999', '0000', '0001', '0010', '0100', '1000'],target = "1111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9998', '9989', '9899', '8999', '0000', '0001', '0010', '0100', '1000'],target = "1111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['9998', '9989', '9899', '8999', '0001', '0010', '0100', '1000'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['9998', '9989', '9899', '8999', '0001', '0010', '0100', '1000'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5678") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5678") == 14: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765'],target = "9876") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765'],target = "9876") == 10: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5432") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5432") == 14: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0101', '1010', '1100', '1110', '1101', '0111', '1001', '0011'],target = "1111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0101', '1010', '1100', '1110', '1101', '0111', '1001', '0011'],target = "1111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0123', '1230', '2301', '3012', '1023', '0231', '2310', '3102', '2013', '0132', '1320', '3201', '0213', '2130', '3021', '1203'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0123', '1230', '2301', '3012', '1023', '0231', '2310', '3102', '2013', '0132', '1320', '3201', '0213', '2130', '3021', '1203'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '1101', '1011', '0111', '1112', '1121', '1211', '2111', '1113', '1131', '1311', '3111'],target = "1114") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '1101', '1011', '0111', '1112', '1121', '1211', '2111', '1113', '1131', '1311', '3111'],target = "1114") == 7: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0013', '0103', '0130', '1030', '1300', '3000'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0013', '0103', '0130', '1030', '1300', '3000'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0012', '0102', '0201', '0210', '1002', '1020', '1200', '2001', '2010', '2100'],target = "2222") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0012', '0102', '0201', '0210', '1002', '1020', '1200', '2001', '2010', '2100'],target = "2222") == 8: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "8888") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "8888") == 8: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0101', '1212', '2323', '3434', '4545', '5656', '6767', '7878', '8989', '9090'],target = "9090") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0101', '1212', '2323', '3434', '4545', '5656', '6767', '7878', '8989', '9090'],target = "9090") == 2: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0009', '0090', '0900', '9000', '1111'],target = "2222") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0009', '0090', '0900', '9000', '1111'],target = "2222") == 8: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0010', '0100', '1000', '0011', '0110', '1100', '1010', '0101', '1001', '0111', '1110', '1101', '1011', '1111'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0010', '0100', '1000', '0011', '0110', '1100', '1010', '0101', '1001', '0111', '1110', '1101', '1011', '1111'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['0001', '0011', '0111', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['0001', '0011', '0111', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1110', '2220', '3330', '4440', '5550', '6660', '7770', '8880', '9990'],target = "0001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1110', '2220', '3330', '4440', '5550', '6660', '7770', '8880', '9990'],target = "0001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1111', '2222', '3333', '4444', '5555'],target = "6666") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1111', '2222', '3333', '4444', '5555'],target = "6666") == 16: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1001', '2002', '3003', '4004', '5005', '6006', '7007', '8008', '9009'],target = "9999") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1001', '2002', '3003', '4004', '5005', '6006', '7007', '8008', '9009'],target = "9999") == 4: {e}')
    
    total += 1
    try:
        result = candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0000") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(deadends = [],target = "1111") == 4
    assert candidate(deadends = ['1111', '2222', '3333'],target = "4444") == 16
    assert candidate(deadends = ['0001', '0002', '0003', '0004'],target = "0005") == 5
    assert candidate(deadends = ['0001', '0011', '0101', '1001', '1101', '0111', '0110', '1010', '1110', '1100'],target = "1111") == 6
    assert candidate(deadends = ['1110', '1101', '1011', '0111'],target = "1111") == 6
    assert candidate(deadends = ['9998', '9997', '9996', '9995'],target = "9999") == 4
    assert candidate(deadends = ['0000'],target = "1111") == -1
    assert candidate(deadends = ['1111', '2222', '3333', '4444'],target = "5555") == 20
    assert candidate(deadends = ['1234'],target = "0000") == 0
    assert candidate(deadends = ['8888'],target = "0009") == 1
    assert candidate(deadends = ['0002', '0020', '0200', '2000'],target = "0000") == 0
    assert candidate(deadends = ['0001', '0010', '0100', '1000'],target = "1111") == 6
    assert candidate(deadends = ['0201', '0101', '0102', '1212', '2002'],target = "0202") == 6
    assert candidate(deadends = ['1110', '1101', '1011', '0111'],target = "0000") == 0
    assert candidate(deadends = ['1111'],target = "0000") == 0
    assert candidate(deadends = ['1111'],target = "1112") == 5
    assert candidate(deadends = ['0001', '0010', '0100', '1000'],target = "0000") == 0
    assert candidate(deadends = ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'],target = "8888") == -1
    assert candidate(deadends = [],target = "0000") == 0
    assert candidate(deadends = ['0000'],target = "8888") == -1
    assert candidate(deadends = ['9999'],target = "0000") == 0
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5555") == 20
    assert candidate(deadends = ['1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678'],target = "8765") == 14
    assert candidate(deadends = ['1234', '4321', '2143', '3412', '0987', '7890', '8709', '9087'],target = "0000") == 0
    assert candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', '0000'],target = "1234") == -1
    assert candidate(deadends = ['0011', '0110', '1100', '1001', '1112', '1211', '2111'],target = "2222") == 8
    assert candidate(deadends = ['1000', '0100', '0010', '0001', '0011', '0110', '1010', '1100', '1110'],target = "1111") == 6
    assert candidate(deadends = ['0009', '0018', '0108', '0117', '0126', '0135', '0144', '0153', '0162', '0171'],target = "0000") == 0
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "9999") == 4
    assert candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0
    assert candidate(deadends = ['0101', '1010', '1100', '1111'],target = "0011") == 2
    assert candidate(deadends = ['0000', '1111', '2222', '3333', '4444'],target = "5555") == -1
    assert candidate(deadends = ['0001', '0010', '1000', '0100', '0011', '1100', '0110', '1010'],target = "1111") == 6
    assert candidate(deadends = ['0001', '1112', '2223', '3334', '4445', '5556', '6667', '7778', '8889'],target = "9999") == 4
    assert candidate(deadends = ['0123', '9876', '5432', '1357', '2468', '0909', '1111', '2222', '3333'],target = "4444") == 16
    assert candidate(deadends = ['9998', '9989', '9899', '8999', '0000', '1111', '2222', '3333', '4444', '5555'],target = "6789") == -1
    assert candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "1111") == 4
    assert candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6
    assert candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "9999") == -1
    assert candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0100'],target = "0011") == 2
    assert candidate(deadends = ['9999', '8888', '7777', '6666', '5555', '4444', '3333', '2222', '1111'],target = "0000") == 0
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "1000") == 1
    assert candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', '1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765', '6789', '9876', '7890', '0987', '8790', '9087', '0879'],target = "0000") == 0
    assert candidate(deadends = ['0000', '9999', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "1234") == -1
    assert candidate(deadends = ['0011', '0101', '1001', '1100', '1110', '1101'],target = "1111") == 4
    assert candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0100'],target = "9999") == 4
    assert candidate(deadends = ['1000', '0100', '0010', '0001', '2000', '0200', '0020', '0002'],target = "0000") == 0
    assert candidate(deadends = ['0000', '0009', '0090', '0900', '9000', '1111', '2222', '3333', '4444'],target = "5555") == -1
    assert candidate(deadends = ['0010', '0100', '0001', '0110', '1001', '1100', '1111', '0000'],target = "0101") == -1
    assert candidate(deadends = ['0001', '0002', '0010', '0020', '0100', '0200', '1000', '2000', '0003', '0030', '0300', '3000'],target = "0004") == 6
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6
    assert candidate(deadends = ['0001', '0010', '0100', '1000', '0111', '1110', '1101', '1011', '2220', '2202', '2022', '0222'],target = "0202") == 6
    assert candidate(deadends = ['1234', '4321', '2143', '3412'],target = "5678") == 14
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123', '0234', '1345', '2456', '3567', '4678', '5789', '6890', '7901', '8012', '9123'],target = "4567") == 16
    assert candidate(deadends = ['0001', '0010', '0100', '1000', '1234', '4321', '5678', '8765', '9999'],target = "8888") == 8
    assert candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "9999") == 4
    assert candidate(deadends = ['9999', '8888', '7777', '6666', '5555'],target = "4444") == 16
    assert candidate(deadends = ['0002', '0020', '0200', '2000', '0013', '0130', '1300', '3000', '0112', '1120', '1201', '2011', '1011', '0110', '0101', '1010', '0011'],target = "1111") == 4
    assert candidate(deadends = ['1111', '1110', '1101', '1011', '0111', '2222', '2221', '2212', '2122', '1222', '3333', '3332', '3323', '3233', '2333', '4444', '4443', '4434', '4344', '3444'],target = "5555") == 20
    assert candidate(deadends = ['9998', '9989', '9899', '8999', '0001', '0010', '0100', '1000'],target = "9999") == 4
    assert candidate(deadends = ['1110', '1101', '1011', '0111', '2220', '2202', '2022', '0222', '3330', '3303', '3033', '0333'],target = "4444") == 16
    assert candidate(deadends = ['0009', '0018', '0108', '0117', '0126', '0135', '0144', '0153', '0162', '0171', '0800', '0900', '1800', '1900', '2800', '2900', '3800', '3900', '4800', '4900', '5800', '5900', '6800', '6900', '7800', '7900', '8800', '8900', '9800', '9900'],target = "0000") == 0
    assert candidate(deadends = ['0001', '0010', '0100', '1000', '1110', '1101', '1011', '0111'],target = "1111") == 8
    assert candidate(deadends = ['0000', '1234', '5678', '9999'],target = "4321") == -1
    assert candidate(deadends = ['0010', '0020', '0030', '0040', '0050'],target = "0060") == 4
    assert candidate(deadends = ['1110', '1101', '1011', '0111', '0011', '0101', '0110'],target = "1111") == 6
    assert candidate(deadends = ['0001', '0010', '0100', '1000', '1110', '1101', '1011', '0111', '0002', '0020'],target = "3333") == 14
    assert candidate(deadends = ['0011', '1100', '2211', '3322', '4433', '5544', '6655', '7766', '8877'],target = "9988") == 6
    assert candidate(deadends = ['0000', '0010', '0100', '0110', '1000', '1010', '1100', '1110', '0001', '0011', '0101', '0111', '1001', '1011', '1101'],target = "1111") == -1
    assert candidate(deadends = ['0010', '0100', '0111', '1000', '1001', '1010', '1100', '1111', '0001', '0011', '0110', '1101', '0101', '1011'],target = "0000") == 0
    assert candidate(deadends = ['0001', '0011', '0111', '1111', '0002', '0020', '0200', '2000', '0003', '0030', '0300', '3000'],target = "0101") == 2
    assert candidate(deadends = ['1112', '1121', '1211', '2111', '2221', '2212', '2122', '1222'],target = "2222") == 10
    assert candidate(deadends = ['8888', '8887', '8878', '8788', '7888', '9999', '9998', '9989', '9899', '8999'],target = "0000") == 0
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0123") == 6
    assert candidate(deadends = ['0010', '0100', '1000', '0001', '0002', '0020', '0200', '2000'],target = "0003") == 5
    assert candidate(deadends = ['0000', '0011', '0101', '0110', '1001', '1010', '1100', '1111', '2222'],target = "3333") == -1
    assert candidate(deadends = ['0001', '0009', '0010', '0090', '0100', '0900', '1000', '9000', '0002', '0020', '0200', '2000', '0008', '0080', '0800', '8000'],target = "0000") == 0
    assert candidate(deadends = ['0009', '0018', '0027', '0036', '0045', '0054', '0063', '0072', '0081'],target = "0090") == 1
    assert candidate(deadends = ['8888', '9999', '0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777'],target = "0001") == -1
    assert candidate(deadends = ['0101', '1010', '1111', '0011', '1100', '1001', '0110', '0001', '0010', '0100'],target = "9999") == 4
    assert candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "1234") == -1
    assert candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "9999") == -1
    assert candidate(deadends = ['0001', '1112', '2223', '3334', '4445', '5556', '6667', '7778', '8889'],target = "4321") == 10
    assert candidate(deadends = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009'],target = "1000") == 1
    assert candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'],target = "0000") == 0
    assert candidate(deadends = ['0000', '0010', '0020', '0030', '0040', '0050', '0060', '0070', '0080', '0090'],target = "0009") == -1
    assert candidate(deadends = ['0123', '4567', '8901', '2345', '6789', '0987', '5432', '1098', '3210'],target = "1111") == 4
    assert candidate(deadends = ['1110', '1101', '1011', '0111', '2222', '3333', '4444', '5555', '6666', '7777'],target = "1234") == 10
    assert candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890'],target = "9876") == 10
    assert candidate(deadends = ['9998', '9989', '9899', '8999', '0000', '0001', '0010', '0100', '1000'],target = "1111") == -1
    assert candidate(deadends = ['9998', '9989', '9899', '8999', '0001', '0010', '0100', '1000'],target = "0000") == 0
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5678") == 14
    assert candidate(deadends = ['1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765'],target = "9876") == 10
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0123'],target = "5432") == 14
    assert candidate(deadends = ['0101', '1010', '1100', '1110', '1101', '0111', '1001', '0011'],target = "1111") == 6
    assert candidate(deadends = ['0123', '1230', '2301', '3012', '1023', '0231', '2310', '3102', '2013', '0132', '1320', '3201', '0213', '2130', '3021', '1203'],target = "9999") == 4
    assert candidate(deadends = ['1110', '1101', '1011', '0111', '1112', '1121', '1211', '2111', '1113', '1131', '1311', '3111'],target = "1114") == 7
    assert candidate(deadends = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012', '0013', '0103', '0130', '1030', '1300', '3000'],target = "0000") == 0
    assert candidate(deadends = ['0001', '0012', '0102', '0201', '0210', '1002', '1020', '1200', '2001', '2010', '2100'],target = "2222") == 8
    assert candidate(deadends = ['1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000'],target = "0000") == 0
    assert candidate(deadends = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "8888") == 8
    assert candidate(deadends = ['0101', '1212', '2323', '3434', '4545', '5656', '6767', '7878', '8989', '9090'],target = "9090") == 2
    assert candidate(deadends = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0
    assert candidate(deadends = ['0009', '0090', '0900', '9000', '1111'],target = "2222") == 8
    assert candidate(deadends = ['0001', '0010', '0100', '1000', '0011', '0110', '1100', '1010', '0101', '1001', '0111', '1110', '1101', '1011', '1111'],target = "0000") == 0
    assert candidate(deadends = ['0001', '0011', '0111', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999'],target = "0000") == 0
    assert candidate(deadends = ['1110', '2220', '3330', '4440', '5550', '6660', '7770', '8880', '9990'],target = "0001") == 1
    assert candidate(deadends = ['1111', '2222', '3333', '4444', '5555'],target = "6666") == 16
    assert candidate(deadends = ['1001', '2002', '3003', '4004', '5005', '6006', '7007', '8008', '9009'],target = "9999") == 4
    assert candidate(deadends = ['1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012'],target = "0000") == 0


