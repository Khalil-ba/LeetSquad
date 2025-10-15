def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [12345, 54321, 13245]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 54321, 13245]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 234, 345]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 234, 345]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 876, 765, 654]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 876, 765, 654]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99999, 99999]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99999, 99999]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 23, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 23, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 321, 213]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 321, 213]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 876, 765, 654, 543]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 876, 765, 654, 543]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5678, 6789, 7890]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5678, 6789, 7890]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234561, 345612, 456123, 561234, 612345]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234561, 345612, 456123, 561234, 612345]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [191919191, 282828282, 373737373, 464646464, 555555555]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [191919191, 282828282, 373737373, 464646464, 555555555]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 987, 654, 321, 111, 222, 333, 444, 555, 666, 777, 888, 999]) == 294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 987, 654, 321, 111, 222, 333, 444, 555, 666, 777, 888, 999]) == 294: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56789, 98765, 58679, 67985]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56789, 98765, 58679, 67985]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 2345, 3456, 4567, 5678]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 2345, 3456, 4567, 5678]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000001, 2000002, 3000003, 4000004, 5000005, 6000006, 7000007]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000001, 2000002, 3000003, 4000004, 5000005, 6000006, 7000007]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [55555, 55554, 55545, 55455, 54555, 45555, 55555, 55555, 55555, 55555, 55555, 55555]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55555, 55554, 55545, 55455, 54555, 45555, 55555, 55555, 55555, 55555, 55555, 55555]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060, 707070, 808080, 909090]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060, 707070, 808080, 909090]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121212, 212121, 121211, 212112, 112121, 221212, 122121, 211221]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121212, 212121, 121211, 212112, 112121, 221212, 122121, 211221]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums = [56789, 56788, 56787, 56786, 56785]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56789, 56788, 56787, 56786, 56785]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1999999, 2999998, 3999997, 4999996, 5999995, 6999994, 7999993, 8999992, 9999991]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1999999, 2999998, 3999997, 4999996, 5999995, 6999994, 7999993, 8999992, 9999991]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 7654321, 1357924, 8642035, 9876543, 3210987]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 7654321, 1357924, 8642035, 9876543, 3210987]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 111222333, 222333444, 333444555, 444555666]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 111222333, 222333444, 333444555, 444555666]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112233, 223344, 334455, 445566, 556677, 667788, 778899, 889900, 990011]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112233, 223344, 334455, 445566, 556677, 667788, 778899, 889900, 990011]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [55555, 54445, 53335, 52225, 51115, 50005, 49995, 48885, 47775, 46665]) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55555, 54445, 53335, 52225, 51115, 50005, 49995, 48885, 47775, 46665]) == 159: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111222333, 333222111]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111222333, 333222111]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123123123, 234234234, 345345345, 456456456, 567567567, 678678678, 789789789, 890890890, 901901901]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123123123, 234234234, 345345345, 456456456, 567567567, 678678678, 789789789, 890890890, 901901901]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010, 202020, 303030, 404040, 505050]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010, 202020, 303030, 404040, 505050]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 1100, 1110, 1111, 1011, 1101]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 1100, 1110, 1111, 1011, 1101]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 99999999, 88888888, 77777777, 66666666, 55555555]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 99999999, 88888888, 77777777, 66666666, 55555555]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 876543219, 765432198, 654321987, 543219876, 432198765, 321987654, 219876543, 198765432]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 876543219, 765432198, 654321987, 543219876, 432198765, 321987654, 219876543, 198765432]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 111111111, 222222222, 333333333, 444444444]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 111111111, 222222222, 333333333, 444444444]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [900000, 899999, 889998, 879997, 869996, 859995, 849994, 839993, 829992]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [900000, 899999, 889998, 879997, 869996, 859995, 849994, 839993, 829992]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11122, 22233, 33344, 44455, 55566]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11122, 22233, 33344, 44455, 55566]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999, 123456789]) == 396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999, 123456789]) == 396: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555555555, 444444444, 333333333, 222222222, 111111111]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555555555, 444444444, 333333333, 222222222, 111111111]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123123, 321321, 213213, 132132, 312312, 231231, 123123]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123123, 321321, 213213, 132132, 312312, 231231, 123123]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 321, 213, 132, 231, 312, 456, 654, 564, 546, 465, 645, 789, 987, 897, 879, 798, 978]) == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 321, 213, 132, 231, 312, 456, 654, 564, 546, 465, 645, 789, 987, 897, 879, 798, 978]) == 432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11112222, 22223333, 33334444, 44445555]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11112222, 22223333, 33334444, 44445555]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [199991, 299992, 399993, 499994, 599995, 699996, 799997, 899998, 999999]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [199991, 299992, 399993, 499994, 599995, 699996, 799997, 899998, 999999]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123123, 234234, 345345, 456456, 567567, 678678, 789789, 890890, 901901]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123123, 234234, 345345, 456456, 567567, 678678, 789789, 890890, 901901]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876543, 8765432, 7654321, 6543210, 5432109, 4321098, 3210987, 2109876, 1098765]) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876543, 8765432, 7654321, 6543210, 5432109, 4321098, 3210987, 2109876, 1098765]) == 252: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [989898989, 878787878, 767676767, 656565656, 545454545, 434343434, 323232323, 212121212, 101010101]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [989898989, 878787878, 767676767, 656565656, 545454545, 434343434, 323232323, 212121212, 101010101]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123123123, 234234234, 345345345, 456456456, 567567567]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123123123, 234234234, 345345345, 456456456, 567567567]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 2345671, 3456712, 4567123, 5671234, 6712345, 7123456, 1234567]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 2345671, 3456712, 4567123, 5671234, 6712345, 7123456, 1234567]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 876543219, 918273645]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 876543219, 918273645]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111222333, 222333444, 333444555, 444555666, 555666777]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111222333, 222333444, 333444555, 444555666, 555666777]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1212121, 2323232, 3434343, 4545454, 5656565, 6767676, 7878787, 8989898, 9090909]) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1212121, 2323232, 3434343, 4545454, 5656565, 6767676, 7878787, 8989898, 9090909]) == 252: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5555555, 5555554, 5555553, 5555552, 5555551, 5555550]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5555555, 5555554, 5555553, 5555552, 5555551, 5555550]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010101, 202020202, 303030303, 404040404, 505050505]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010101, 202020202, 303030303, 404040404, 505050505]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 2345, 3456, 4567, 5678, 6789]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 2345, 3456, 4567, 5678, 6789]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000001, 200000002, 300000003, 400000004, 500000005, 600000006, 700000007, 800000008, 900000009]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000001, 200000002, 300000003, 400000004, 500000005, 600000006, 700000007, 800000008, 900000009]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901, 123, 234, 345, 456, 567, 678, 789, 890, 901]) == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901, 123, 234, 345, 456, 567, 678, 789, 890, 901]) == 432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 1010, 1100, 1110, 10011]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 1010, 1100, 1110, 10011]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 876543219, 912345678]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 876543219, 912345678]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [918273645, 827364591, 736459182, 645918273, 591827364]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [918273645, 827364591, 736459182, 645918273, 591827364]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234]) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234]) == 147: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121212121, 212121212, 323232323, 434343434, 545454545, 656565656, 767676767, 878787878, 989898989]) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121212121, 212121212, 323232323, 434343434, 545454545, 656565656, 767676767, 878787878, 989898989]) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111, 222222, 333333, 444444, 555555, 666666, 777777]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111, 222222, 333333, 444444, 555555, 666666, 777777]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1122334455, 2233445566, 3344556677, 4455667788, 5566778899, 6677889911]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1122334455, 2233445566, 3344556677, 4455667788, 5566778899, 6677889911]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 987654320, 987654319, 987654318, 987654317, 987654316, 987654315, 987654314, 987654313]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 987654320, 987654319, 987654318, 987654317, 987654316, 987654315, 987654314, 987654313]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 135792468, 864208642, 246802468]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 135792468, 864208642, 246802468]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999]) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999]) == 288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [121212121, 212121212, 323232323, 434343434, 545454545]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121212121, 212121212, 323232323, 434343434, 545454545]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 876543210, 765432109, 654321098, 543210987, 432109876, 321098765, 210987654, 109876543]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 876543210, 765432109, 654321098, 543210987, 432109876, 321098765, 210987654, 109876543]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 1234568, 1234569, 1234570, 1234571, 1234572, 1234573, 1234574, 1234575]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 1234568, 1234569, 1234570, 1234571, 1234572, 1234573, 1234574, 1234575]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010, 110110, 101101, 111000]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010, 110110, 101101, 111000]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [80808, 80807, 80806, 80805, 80804, 80803, 80802]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [80808, 80807, 80806, 80805, 80804, 80803, 80802]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 111111, 999999]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 111111, 999999]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [223344, 443322, 332244, 224433]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [223344, 443322, 332244, 224433]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010101, 202020202, 303030303, 404040404, 505050505, 606060606]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010101, 202020202, 303030303, 404040404, 505050505, 606060606]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == 405: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112233, 445566, 778899, 332211, 665544]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112233, 445566, 778899, 332211, 665544]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876543, 8765432, 7654321, 6543210, 5432109, 4321098, 3210987, 2109876, 1098765]) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876543, 8765432, 7654321, 6543210, 5432109, 4321098, 3210987, 2109876, 1098765]) == 252: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 123456788, 123456787, 123456786, 123456785, 123456784, 123456783]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 123456788, 123456787, 123456786, 123456785, 123456784, 123456783]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555555, 555555, 555555, 555555, 555555, 555555]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555555, 555555, 555555, 555555, 555555, 555555]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112233, 113322, 121233, 122133, 123123, 123312, 131223, 132123, 132213, 132312]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112233, 113322, 121233, 122133, 123123, 123312, 131223, 132123, 132213, 132312]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 2341, 3412, 4123, 1324, 2413, 3241, 4312, 1423, 2134]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 2341, 3412, 4123, 1324, 2413, 3241, 4312, 1423, 2134]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 234567891, 891234567, 345678912, 789123456, 456789123, 654321987, 567891234]) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 234567891, 891234567, 345678912, 789123456, 456789123, 654321987, 567891234]) == 310: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 987654321, 123456789]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 987654321, 123456789]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555555555, 444444444, 333333333, 222222222, 111111111, 123456789]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555555555, 444444444, 333333333, 222222222, 111111111, 123456789]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111222, 222333, 333444, 444555]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111222, 222333, 333444, 444555]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100100100, 110110110, 120120120, 130130130, 140140140]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100100100, 110110110, 120120120, 130130130, 140140140]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 564738291]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 564738291]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 234561, 165432, 345612, 432165]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 234561, 165432, 345612, 432165]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555555555, 666666666, 777777777, 888888888, 999999999, 111111111, 222222222, 333333333, 444444444, 123456789, 987654321]) == 476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555555555, 666666666, 777777777, 888888888, 999999999, 111111111, 222222222, 333333333, 444444444, 123456789, 987654321]) == 476: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 112233445, 554433221]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 112233445, 554433221]) == 47: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [12345, 54321, 13245]) == 11
    assert candidate(nums = [10, 10, 10, 10]) == 0
    assert candidate(nums = [123, 234, 345]) == 9
    assert candidate(nums = [123, 456, 789]) == 9
    assert candidate(nums = [987, 876, 765, 654]) == 18
    assert candidate(nums = [99999, 99999, 99999]) == 0
    assert candidate(nums = [13, 23, 12]) == 4
    assert candidate(nums = [123, 321, 213]) == 7
    assert candidate(nums = [987, 876, 765, 654, 543]) == 30
    assert candidate(nums = [111, 222, 333, 444]) == 18
    assert candidate(nums = [5678, 6789, 7890]) == 12
    assert candidate(nums = [123456, 234561, 345612, 456123, 561234, 612345]) == 90
    assert candidate(nums = [191919191, 282828282, 373737373, 464646464, 555555555]) == 90
    assert candidate(nums = [123, 456, 789, 987, 654, 321, 111, 222, 333, 444, 555, 666, 777, 888, 999]) == 294
    assert candidate(nums = [56789, 98765, 58679, 67985]) == 24
    assert candidate(nums = [1234, 2345, 3456, 4567, 5678]) == 40
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 216
    assert candidate(nums = [1000001, 2000002, 3000003, 4000004, 5000005, 6000006, 7000007]) == 42
    assert candidate(nums = [55555, 55554, 55545, 55455, 54555, 45555, 55555, 55555, 55555, 55555, 55555, 55555]) == 55
    assert candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060, 707070, 808080, 909090]) == 108
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 324
    assert candidate(nums = [121212, 212121, 121211, 212112, 112121, 221212, 122121, 211221]) == 95
    assert candidate(nums = [56789, 56788, 56787, 56786, 56785]) == 10
    assert candidate(nums = [1999999, 2999998, 3999997, 4999996, 5999995, 6999994, 7999993, 8999992, 9999991]) == 72
    assert candidate(nums = [1234567, 7654321, 1357924, 8642035, 9876543, 3210987]) == 96
    assert candidate(nums = [123456789, 111222333, 222333444, 333444555, 444555666]) == 85
    assert candidate(nums = [112233, 223344, 334455, 445566, 556677, 667788, 778899, 889900, 990011]) == 216
    assert candidate(nums = [55555, 54445, 53335, 52225, 51115, 50005, 49995, 48885, 47775, 46665]) == 159
    assert candidate(nums = [123456789, 987654321, 111222333, 333222111]) == 46
    assert candidate(nums = [123123123, 234234234, 345345345, 456456456, 567567567, 678678678, 789789789, 890890890, 901901901]) == 324
    assert candidate(nums = [101010, 202020, 303030, 404040, 505050]) == 30
    assert candidate(nums = [1001, 1100, 1110, 1111, 1011, 1101]) == 25
    assert candidate(nums = [100000000, 99999999, 88888888, 77777777, 66666666, 55555555]) == 125
    assert candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000]) == 10
    assert candidate(nums = [987654321, 876543219, 765432198, 654321987, 543219876, 432198765, 321987654, 219876543, 198765432]) == 324
    assert candidate(nums = [999999999, 111111111, 222222222, 333333333, 444444444]) == 90
    assert candidate(nums = [900000, 899999, 889998, 879997, 869996, 859995, 849994, 839993, 829992]) == 104
    assert candidate(nums = [11122, 22233, 33344, 44455, 55566]) == 50
    assert candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999, 123456789]) == 396
    assert candidate(nums = [555555555, 444444444, 333333333, 222222222, 111111111]) == 90
    assert candidate(nums = [123123, 321321, 213213, 132132, 312312, 231231, 123123]) == 96
    assert candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987]) == 180
    assert candidate(nums = [123, 321, 213, 132, 231, 312, 456, 654, 564, 546, 465, 645, 789, 987, 897, 879, 798, 978]) == 432
    assert candidate(nums = [11112222, 22223333, 33334444, 44445555]) == 48
    assert candidate(nums = [199991, 299992, 399993, 499994, 599995, 699996, 799997, 899998, 999999]) == 72
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 60
    assert candidate(nums = [123123, 234234, 345345, 456456, 567567, 678678, 789789, 890890, 901901]) == 216
    assert candidate(nums = [9876543, 8765432, 7654321, 6543210, 5432109, 4321098, 3210987, 2109876, 1098765]) == 252
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 216
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987]) == 168
    assert candidate(nums = [989898989, 878787878, 767676767, 656565656, 545454545, 434343434, 323232323, 212121212, 101010101]) == 324
    assert candidate(nums = [123123123, 234234234, 345345345, 456456456, 567567567]) == 90
    assert candidate(nums = [1234567, 2345671, 3456712, 4567123, 5671234, 6712345, 7123456, 1234567]) == 189
    assert candidate(nums = [987654321, 123456789, 876543219, 918273645]) == 50
    assert candidate(nums = [111222333, 222333444, 333444555, 444555666, 555666777]) == 90
    assert candidate(nums = [1212121, 2323232, 3434343, 4545454, 5656565, 6767676, 7878787, 8989898, 9090909]) == 252
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444]) == 90
    assert candidate(nums = [5555555, 5555554, 5555553, 5555552, 5555551, 5555550]) == 15
    assert candidate(nums = [101010101, 202020202, 303030303, 404040404, 505050505]) == 50
    assert candidate(nums = [1234, 2345, 3456, 4567, 5678, 6789]) == 60
    assert candidate(nums = [1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]) == 90
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]) == 36
    assert candidate(nums = [100000001, 200000002, 300000003, 400000004, 500000005, 600000006, 700000007, 800000008, 900000009]) == 72
    assert candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901, 123, 234, 345, 456, 567, 678, 789, 890, 901]) == 432
    assert candidate(nums = [1001, 1010, 1100, 1110, 10011]) == 22
    assert candidate(nums = [987654321, 123456789, 876543219, 912345678]) == 50
    assert candidate(nums = [918273645, 827364591, 736459182, 645918273, 591827364]) == 90
    assert candidate(nums = [2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234]) == 147
    assert candidate(nums = [121212121, 212121212, 323232323, 434343434, 545454545, 656565656, 767676767, 878787878, 989898989]) == 320
    assert candidate(nums = [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909]) == 144
    assert candidate(nums = [111111, 222222, 333333, 444444, 555555, 666666, 777777]) == 126
    assert candidate(nums = [1122334455, 2233445566, 3344556677, 4455667788, 5566778899, 6677889911]) == 150
    assert candidate(nums = [987654321, 987654320, 987654319, 987654318, 987654317, 987654316, 987654315, 987654314, 987654313]) == 50
    assert candidate(nums = [123456789, 987654321, 135792468, 864208642, 246802468]) == 83
    assert candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999]) == 288
    assert candidate(nums = [121212121, 212121212, 323232323, 434343434, 545454545]) == 86
    assert candidate(nums = [987654321, 876543210, 765432109, 654321098, 543210987, 432109876, 321098765, 210987654, 109876543]) == 324
    assert candidate(nums = [1234567, 1234568, 1234569, 1234570, 1234571, 1234572, 1234573, 1234574, 1234575]) == 54
    assert candidate(nums = [101010, 110110, 101101, 111000]) == 18
    assert candidate(nums = [80808, 80807, 80806, 80805, 80804, 80803, 80802]) == 21
    assert candidate(nums = [123456, 654321, 111111, 999999]) == 34
    assert candidate(nums = [223344, 443322, 332244, 224433]) == 30
    assert candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 144
    assert candidate(nums = [101010101, 202020202, 303030303, 404040404, 505050505, 606060606]) == 75
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == 405
    assert candidate(nums = [112233, 445566, 778899, 332211, 665544]) == 56
    assert candidate(nums = [9876543, 8765432, 7654321, 6543210, 5432109, 4321098, 3210987, 2109876, 1098765]) == 252
    assert candidate(nums = [123456789, 123456788, 123456787, 123456786, 123456785, 123456784, 123456783]) == 21
    assert candidate(nums = [555555, 555555, 555555, 555555, 555555, 555555]) == 0
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210]) == 60
    assert candidate(nums = [112233, 113322, 121233, 122133, 123123, 123312, 131223, 132123, 132213, 132312]) == 150
    assert candidate(nums = [1234, 2341, 3412, 4123, 1324, 2413, 3241, 4312, 1423, 2134]) == 148
    assert candidate(nums = [123456789, 987654321, 234567891, 891234567, 345678912, 789123456, 456789123, 654321987, 567891234]) == 310
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 30
    assert candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555]) == 90
    assert candidate(nums = [987654321, 123456789, 987654321, 123456789]) == 32
    assert candidate(nums = [555555555, 444444444, 333333333, 222222222, 111111111, 123456789]) == 130
    assert candidate(nums = [111222, 222333, 333444, 444555]) == 36
    assert candidate(nums = [100100100, 110110110, 120120120, 130130130, 140140140]) == 30
    assert candidate(nums = [123456789, 987654321, 564738291]) == 25
    assert candidate(nums = [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909]) == 144
    assert candidate(nums = [123456, 654321, 234561, 165432, 345612, 432165]) == 82
    assert candidate(nums = [555555555, 666666666, 777777777, 888888888, 999999999, 111111111, 222222222, 333333333, 444444444, 123456789, 987654321]) == 476
    assert candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000]) == 15
    assert candidate(nums = [123456789, 987654321, 112233445, 554433221]) == 47


