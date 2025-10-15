def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 122333) == 123233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122333) == 123233: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 3133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 3133: {e}')
    
    total += 1
    try:
        result = candidate(n = 1222) == 1333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1222) == 1333: {e}')
    
    total += 1
    try:
        result = candidate(n = 55555) == 122333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55555) == 122333: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 1333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 1333: {e}')
    
    total += 1
    try:
        result = candidate(n = 112233) == 122333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112233) == 122333: {e}')
    
    total += 1
    try:
        result = candidate(n = 122133) == 122333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122133) == 122333: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 1242444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 1242444: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 132233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 132233: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 1333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 1333: {e}')
    
    total += 1
    try:
        result = candidate(n = 1224444) == 1242444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1224444) == 1242444: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 122) == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122) == 212: {e}')
    
    total += 1
    try:
        result = candidate(n = 122333444) == 122666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122333444) == 122666666: {e}')
    
    total += 1
    try:
        result = candidate(n = 2233445566) == 2233535555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2233445566) == 2233535555: {e}')
    
    total += 1
    try:
        result = candidate(n = 122444) == 123233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122444) == 123233: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333333) == 3334444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333333) == 3334444: {e}')
    
    total += 1
    try:
        result = candidate(n = 666666) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666666) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 11222233) == 12255555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11222233) == 12255555: {e}')
    
    total += 1
    try:
        result = candidate(n = 444444) == 515555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 444444) == 515555: {e}')
    
    total += 1
    try:
        result = candidate(n = 1223334444) == 1223343444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1223334444) == 1223343444: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222) == 2241444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222) == 2241444: {e}')
    
    total += 1
    try:
        result = candidate(n = 44445555) == 51225555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44445555) == 51225555: {e}')
    
    total += 1
    try:
        result = candidate(n = 6665554443332211) == 6665554444155666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6665554443332211) == 6665554444155666: {e}')
    
    total += 1
    try:
        result = candidate(n = 1233333) == 1242444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1233333) == 1242444: {e}')
    
    total += 1
    try:
        result = candidate(n = 122111333) == 122666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122111333) == 122666666: {e}')
    
    total += 1
    try:
        result = candidate(n = 22333444) == 22515555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22333444) == 22515555: {e}')
    
    total += 1
    try:
        result = candidate(n = 123321) == 123323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123321) == 123323: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 122333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 122333: {e}')
    
    total += 1
    try:
        result = candidate(n = 665544332211) == 665551556666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 665544332211) == 665551556666: {e}')
    
    total += 1
    try:
        result = candidate(n = 400000) == 422444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000) == 422444: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 126266666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 126266666: {e}')
    
    total += 1
    try:
        result = candidate(n = 1223334) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1223334) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 5555555) == 6166666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5555555) == 6166666: {e}')
    
    total += 1
    try:
        result = candidate(n = 223334444555) == 223336166666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 223334444555) == 223336166666: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 122: {e}')
    
    total += 1
    try:
        result = candidate(n = 7777777) == 12255555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7777777) == 12255555: {e}')
    
    total += 1
    try:
        result = candidate(n = 1112233) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1112233) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 122333444555555) == 122333445445555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122333444555555) == 122333445445555: {e}')
    
    total += 1
    try:
        result = candidate(n = 2233444) == 2241444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2233444) == 2241444: {e}')
    
    total += 1
    try:
        result = candidate(n = 1222333) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1222333) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 2121212121) == 2123334444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2121212121) == 2123334444: {e}')
    
    total += 1
    try:
        result = candidate(n = 122444455555) == 122444545555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122444455555) == 122444545555: {e}')
    
    total += 1
    try:
        result = candidate(n = 12233344) == 12255555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12233344) == 12255555: {e}')
    
    total += 1
    try:
        result = candidate(n = 666666555444333222111) == 666666555444333224155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666666555444333222111) == 666666555444333224155: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 22222222) == 22515555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22222222) == 22515555: {e}')
    
    total += 1
    try:
        result = candidate(n = 122333444555666) == 122333445445555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122333444555666) == 122333445445555: {e}')
    
    total += 1
    try:
        result = candidate(n = 1221221) == 1224444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1221221) == 1224444: {e}')
    
    total += 1
    try:
        result = candidate(n = 5555544332211) == 5555544333144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5555544332211) == 5555544333144: {e}')
    
    total += 1
    try:
        result = candidate(n = 1233322) == 1242444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1233322) == 1242444: {e}')
    
    total += 1
    try:
        result = candidate(n = 4444) == 14444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4444) == 14444: {e}')
    
    total += 1
    try:
        result = candidate(n = 122334444) == 122666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122334444) == 122666666: {e}')
    
    total += 1
    try:
        result = candidate(n = 1222233333) == 1223334444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1222233333) == 1223334444: {e}')
    
    total += 1
    try:
        result = candidate(n = 1333331) == 1422444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1333331) == 1422444: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 1
    assert candidate(n = 122333) == 123233
    assert candidate(n = 3000) == 3133
    assert candidate(n = 1222) == 1333
    assert candidate(n = 55555) == 122333
    assert candidate(n = 1234) == 1333
    assert candidate(n = 112233) == 122333
    assert candidate(n = 122133) == 122333
    assert candidate(n = 1234567) == 1242444
    assert candidate(n = 999999) == 1224444
    assert candidate(n = 123456) == 132233
    assert candidate(n = 1) == 22
    assert candidate(n = 1000) == 1333
    assert candidate(n = 1224444) == 1242444
    assert candidate(n = 987654) == 1224444
    assert candidate(n = 122) == 212
    assert candidate(n = 122333444) == 122666666
    assert candidate(n = 2233445566) == 2233535555
    assert candidate(n = 122444) == 123233
    assert candidate(n = 3333333) == 3334444
    assert candidate(n = 666666) == 1224444
    assert candidate(n = 11222233) == 12255555
    assert candidate(n = 444444) == 515555
    assert candidate(n = 1223334444) == 1223343444
    assert candidate(n = 2222222) == 2241444
    assert candidate(n = 44445555) == 51225555
    assert candidate(n = 6665554443332211) == 6665554444155666
    assert candidate(n = 1233333) == 1242444
    assert candidate(n = 122111333) == 122666666
    assert candidate(n = 22333444) == 22515555
    assert candidate(n = 123321) == 123323
    assert candidate(n = 98765) == 122333
    assert candidate(n = 665544332211) == 665551556666
    assert candidate(n = 400000) == 422444
    assert candidate(n = 123456789) == 126266666
    assert candidate(n = 1223334) == 1224444
    assert candidate(n = 5555555) == 6166666
    assert candidate(n = 223334444555) == 223336166666
    assert candidate(n = 111) == 122
    assert candidate(n = 7777777) == 12255555
    assert candidate(n = 1112233) == 1224444
    assert candidate(n = 122333444555555) == 122333445445555
    assert candidate(n = 2233444) == 2241444
    assert candidate(n = 1222333) == 1224444
    assert candidate(n = 2121212121) == 2123334444
    assert candidate(n = 122444455555) == 122444545555
    assert candidate(n = 12233344) == 12255555
    assert candidate(n = 666666555444333222111) == 666666555444333224155
    assert candidate(n = 1000000) == 1224444
    assert candidate(n = 22222222) == 22515555
    assert candidate(n = 122333444555666) == 122333445445555
    assert candidate(n = 1221221) == 1224444
    assert candidate(n = 5555544332211) == 5555544333144
    assert candidate(n = 1233322) == 1242444
    assert candidate(n = 4444) == 14444
    assert candidate(n = 122334444) == 122666666
    assert candidate(n = 1222233333) == 1223334444
    assert candidate(n = 1333331) == 1422444


