def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 11891) == 99009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11891) == 99009: {e}')
    
    total += 1
    try:
        result = candidate(num = 234567890) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 234567890) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 123321) == 900009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123321) == 900009: {e}')
    
    total += 1
    try:
        result = candidate(num = 55555555) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 55555555) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210) == 9100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210) == 9100000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 88888888) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88888888) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 910000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 910000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101) == 909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101) == 909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 12321) == 90009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12321) == 90009: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999) == 9999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999) == 9999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 475328) == 900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 475328) == 900000: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999999) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999999) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 8888888) == 9999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8888888) == 9999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 9000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 9000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 90) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 90) == 99: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111) == 9999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111) == 9999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 66666666) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 66666666) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 44444444) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 44444444) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111111) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 888111222) == 999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888111222) == 999000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 8765432109) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8765432109) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999999999999999) == 9999999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999999999999999) == 9999999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101010101) == 909090909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101010101) == 909090909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 88888888888888888888) == 99999999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88888888888888888888) == 99999999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111000011) == 9999000099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111000011) == 9999000099: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 80808080) == 90909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 80808080) == 90909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 3330333) == 9990999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3330333) == 9990999: {e}')
    
    total += 1
    try:
        result = candidate(num = 11119999) == 99990000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11119999) == 99990000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1233211233) == 9000099000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1233211233) == 9000099000: {e}')
    
    total += 1
    try:
        result = candidate(num = 777000777) == 999000999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777000777) == 999000999: {e}')
    
    total += 1
    try:
        result = candidate(num = 59595959) == 90909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 59595959) == 90909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 5678909876) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5678909876) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555555555555) == 999999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555555555555) == 999999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 123123123) == 900900900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123123123) == 900900900: {e}')
    
    total += 1
    try:
        result = candidate(num = 4321098765) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4321098765) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 5555555555) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5555555555) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 111000111000111) == 999000999000999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111000111000111) == 999000999000999: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333444555666777888999) == 999000000000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333444555666777888999) == 999000000000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 7777777777) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7777777777) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1232123212321232123) == 9000900090009000900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1232123212321232123) == 9000900090009000900: {e}')
    
    total += 1
    try:
        result = candidate(num = 7676767676) == 9090909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7676767676) == 9090909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 50505050) == 90909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50505050) == 90909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 199999991) == 900000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199999991) == 900000009: {e}')
    
    total += 1
    try:
        result = candidate(num = 123321123) == 900009900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123321123) == 900009900: {e}')
    
    total += 1
    try:
        result = candidate(num = 12233445) == 90000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12233445) == 90000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 990099009) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 990099009) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 505050505) == 909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 505050505) == 909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 111999) == 999000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111999) == 999000: {e}')
    
    total += 1
    try:
        result = candidate(num = 10001) == 90009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10001) == 90009: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333) == 999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333) == 999000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 3210987654) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3210987654) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 959595959) == 949494949
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 959595959) == 949494949: {e}')
    
    total += 1
    try:
        result = candidate(num = 10101010) == 90909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10101010) == 90909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000001) == 9000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000001) == 9000000009: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678901234567890) == 90000000009000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678901234567890) == 90000000009000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1098765432) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1098765432) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1199119911) == 9900990099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1199119911) == 9900990099: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 555505555) == 999909999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555505555) == 999909999: {e}')
    
    total += 1
    try:
        result = candidate(num = 999111999111999) == 999888999888999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999111999111999) == 999888999888999: {e}')
    
    total += 1
    try:
        result = candidate(num = 8888888888) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8888888888) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432109876543210) == 91000000009100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432109876543210) == 91000000009100000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 111000111) == 999000999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111000111) == 999000999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1010101010) == 9090909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1010101010) == 9090909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 9900990099) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9900990099) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888888888888) == 999999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888888888888) == 999999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777777) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777777) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 989898989) == 919191919
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 989898989) == 919191919: {e}')
    
    total += 1
    try:
        result = candidate(num = 12312312312312312312) == 90090090090090090090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12312312312312312312) == 90090090090090090090: {e}')
    
    total += 1
    try:
        result = candidate(num = 1001001001) == 9009009009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001001001) == 9009009009: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000001) == 900000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000001) == 900000009: {e}')
    
    total += 1
    try:
        result = candidate(num = 2109876543) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2109876543) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1223344556677889900) == 9000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1223344556677889900) == 9000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 19999999999999999999) == 90000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 19999999999999999999) == 90000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 595959595) == 909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 595959595) == 909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 876543210) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 876543210) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999999) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999999) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 90909090) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 90909090) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 99990000) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99990000) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 191919191) == 909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 191919191) == 909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 555000) == 999000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555000) == 999000: {e}')
    
    total += 1
    try:
        result = candidate(num = 989898989898989) == 919191919191919
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 989898989898989) == 919191919191919: {e}')
    
    total += 1
    try:
        result = candidate(num = 5432109876) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5432109876) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 11100011) == 99900099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11100011) == 99900099: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 321321321) == 900900900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 321321321) == 900900900: {e}')
    
    total += 1
    try:
        result = candidate(num = 95959595) == 94949494
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 95959595) == 94949494: {e}')
    
    total += 1
    try:
        result = candidate(num = 121212121) == 909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 121212121) == 909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234321098) == 9000009000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234321098) == 9000009000: {e}')
    
    total += 1
    try:
        result = candidate(num = 4321234321) == 9000009000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4321234321) == 9000009000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1230123012) == 9000900090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1230123012) == 9000900090: {e}')
    
    total += 1
    try:
        result = candidate(num = 2233223322) == 9900990099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2233223322) == 9900990099: {e}')
    
    total += 1
    try:
        result = candidate(num = 99009900) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99009900) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 9123456789) == 9800000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9123456789) == 9800000009: {e}')
    
    total += 1
    try:
        result = candidate(num = 5555555) == 9999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5555555) == 9999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 122334455) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 122334455) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9090909090) == 9999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9090909090) == 9999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 999000) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999000) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 10101010101010101010) == 90909090909090909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10101010101010101010) == 90909090909090909090: {e}')
    
    total += 1
    try:
        result = candidate(num = 88811122) == 99900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88811122) == 99900000: {e}')
    
    total += 1
    try:
        result = candidate(num = 202020202) == 909090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 202020202) == 909090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 246813579135791357) == 900000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 246813579135791357) == 900000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 12121212) == 90909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12121212) == 90909090: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 11891) == 99009
    assert candidate(num = 234567890) == 900000000
    assert candidate(num = 123321) == 900009
    assert candidate(num = 55555555) == 99999999
    assert candidate(num = 111111) == 999999
    assert candidate(num = 123456789) == 900000000
    assert candidate(num = 9876543210) == 9100000000
    assert candidate(num = 88888888) == 99999999
    assert candidate(num = 987654321) == 910000000
    assert candidate(num = 101010101) == 909090909
    assert candidate(num = 12321) == 90009
    assert candidate(num = 9999999) == 9999999
    assert candidate(num = 1) == 9
    assert candidate(num = 475328) == 900000
    assert candidate(num = 99999999) == 99999999
    assert candidate(num = 8888888) == 9999999
    assert candidate(num = 99999) == 99999
    assert candidate(num = 1000000) == 9000000
    assert candidate(num = 90) == 99
    assert candidate(num = 1111111) == 9999999
    assert candidate(num = 66666666) == 99999999
    assert candidate(num = 44444444) == 99999999
    assert candidate(num = 111111111) == 999999999
    assert candidate(num = 888111222) == 999000000
    assert candidate(num = 8765432109) == 9000000000
    assert candidate(num = 9999999999999999999) == 9999999999999999999
    assert candidate(num = 101010101010101) == 909090909090909
    assert candidate(num = 88888888888888888888) == 99999999999999999999
    assert candidate(num = 1111000011) == 9999000099
    assert candidate(num = 1000000000) == 9000000000
    assert candidate(num = 80808080) == 90909090
    assert candidate(num = 3330333) == 9990999
    assert candidate(num = 11119999) == 99990000
    assert candidate(num = 1233211233) == 9000099000
    assert candidate(num = 777000777) == 999000999
    assert candidate(num = 59595959) == 90909090
    assert candidate(num = 5678909876) == 9000000000
    assert candidate(num = 555555555555555555) == 999999999999999999
    assert candidate(num = 123123123) == 900900900
    assert candidate(num = 4321098765) == 9000000000
    assert candidate(num = 5555555555) == 9999999999
    assert candidate(num = 111000111000111) == 999000999000999
    assert candidate(num = 111222333444555666777888999) == 999000000000000000000000000
    assert candidate(num = 7777777777) == 9999999999
    assert candidate(num = 1232123212321232123) == 9000900090009000900
    assert candidate(num = 7676767676) == 9090909090
    assert candidate(num = 50505050) == 90909090
    assert candidate(num = 199999991) == 900000009
    assert candidate(num = 123321123) == 900009900
    assert candidate(num = 12233445) == 90000000
    assert candidate(num = 990099009) == 999999999
    assert candidate(num = 505050505) == 909090909
    assert candidate(num = 111999) == 999000
    assert candidate(num = 10001) == 90009
    assert candidate(num = 111222333) == 999000000
    assert candidate(num = 3210987654) == 9000000000
    assert candidate(num = 959595959) == 949494949
    assert candidate(num = 10101010) == 90909090
    assert candidate(num = 1000000001) == 9000000009
    assert candidate(num = 12345678901234567890) == 90000000009000000000
    assert candidate(num = 1098765432) == 9000000000
    assert candidate(num = 1199119911) == 9900990099
    assert candidate(num = 999999999) == 999999999
    assert candidate(num = 555555555) == 999999999
    assert candidate(num = 555505555) == 999909999
    assert candidate(num = 999111999111999) == 999888999888999
    assert candidate(num = 8888888888) == 9999999999
    assert candidate(num = 98765432109876543210) == 91000000009100000000
    assert candidate(num = 111000111) == 999000999
    assert candidate(num = 1010101010) == 9090909090
    assert candidate(num = 9900990099) == 9999999999
    assert candidate(num = 888888888888888888) == 999999999999999999
    assert candidate(num = 777777777) == 999999999
    assert candidate(num = 989898989) == 919191919
    assert candidate(num = 12312312312312312312) == 90090090090090090090
    assert candidate(num = 1001001001) == 9009009009
    assert candidate(num = 100000001) == 900000009
    assert candidate(num = 2109876543) == 9000000000
    assert candidate(num = 1223344556677889900) == 9000000000000000000
    assert candidate(num = 19999999999999999999) == 90000000000000000000
    assert candidate(num = 595959595) == 909090909
    assert candidate(num = 876543210) == 900000000
    assert candidate(num = 9999999999) == 9999999999
    assert candidate(num = 90909090) == 99999999
    assert candidate(num = 99990000) == 99999999
    assert candidate(num = 191919191) == 909090909
    assert candidate(num = 555000) == 999000
    assert candidate(num = 989898989898989) == 919191919191919
    assert candidate(num = 5432109876) == 9000000000
    assert candidate(num = 11100011) == 99900099
    assert candidate(num = 888888888) == 999999999
    assert candidate(num = 1111111111) == 9999999999
    assert candidate(num = 321321321) == 900900900
    assert candidate(num = 95959595) == 94949494
    assert candidate(num = 121212121) == 909090909
    assert candidate(num = 1234321098) == 9000009000
    assert candidate(num = 4321234321) == 9000009000
    assert candidate(num = 1230123012) == 9000900090
    assert candidate(num = 2233223322) == 9900990099
    assert candidate(num = 99009900) == 99999999
    assert candidate(num = 9123456789) == 9800000009
    assert candidate(num = 5555555) == 9999999
    assert candidate(num = 122334455) == 900000000
    assert candidate(num = 1234567890) == 9000000000
    assert candidate(num = 9090909090) == 9999999999
    assert candidate(num = 999000) == 999999
    assert candidate(num = 10101010101010101010) == 90909090909090909090
    assert candidate(num = 88811122) == 99900000
    assert candidate(num = 202020202) == 909090909
    assert candidate(num = 246813579135791357) == 900000000000000000
    assert candidate(num = 12121212) == 90909090


