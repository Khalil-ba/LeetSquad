def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 687) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 687) == 75: {e}')
    
    total += 1
    try:
        result = candidate(num = 4325) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4325) == 59: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111) == 22222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111) == 22222: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234) == 37: {e}')
    
    total += 1
    try:
        result = candidate(num = 222) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222) == 24: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111) == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111) == 222: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333) == 12456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333) == 12456: {e}')
    
    total += 1
    try:
        result = candidate(num = 1999999999) == 119998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1999999999) == 119998: {e}')
    
    total += 1
    try:
        result = candidate(num = 1020304050) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1020304050) == 159: {e}')
    
    total += 1
    try:
        result = candidate(num = 29392342) == 4588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 29392342) == 4588: {e}')
    
    total += 1
    try:
        result = candidate(num = 1001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 543321) == 369
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 543321) == 369: {e}')
    
    total += 1
    try:
        result = candidate(num = 5555555555) == 111110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5555555555) == 111110: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(num = 9191919191) == 23198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9191919191) == 23198: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1357924680) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1357924680) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 314159) == 284
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 314159) == 284: {e}')
    
    total += 1
    try:
        result = candidate(num = 444444444444444444) == 888888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444444444444444444) == 888888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 2233445566778899) == 46913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2233445566778899) == 46913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 567894321) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567894321) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 99991111) == 2398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99991111) == 2398: {e}')
    
    total += 1
    try:
        result = candidate(num = 5647382910) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5647382910) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000009) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000009) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 100100100100) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100100100100) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num = 4444444444) == 88888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4444444444) == 88888: {e}')
    
    total += 1
    try:
        result = candidate(num = 99887766554433221100) == 246913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99887766554433221100) == 246913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 303030303030) == 666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 303030303030) == 666: {e}')
    
    total += 1
    try:
        result = candidate(num = 4444455555) == 89010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4444455555) == 89010: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333444) == 234678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333444) == 234678: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333444555666777888999) == 12456901345788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333444555666777888999) == 12456901345788: {e}')
    
    total += 1
    try:
        result = candidate(num = 3030303030) == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3030303030) == 366: {e}')
    
    total += 1
    try:
        result = candidate(num = 111122223333444455556666777788889999) == 224466891133557798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111122223333444455556666777788889999) == 224466891133557798: {e}')
    
    total += 1
    try:
        result = candidate(num = 594939291909) == 160998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 594939291909) == 160998: {e}')
    
    total += 1
    try:
        result = candidate(num = 7070707070) == 854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7070707070) == 854: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678987654321) == 135802467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678987654321) == 135802467: {e}')
    
    total += 1
    try:
        result = candidate(num = 8642013579) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8642013579) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 8642086420) == 4936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8642086420) == 4936: {e}')
    
    total += 1
    try:
        result = candidate(num = 1298765432) == 36047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1298765432) == 36047: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333444555) == 12456900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333444555) == 12456900: {e}')
    
    total += 1
    try:
        result = candidate(num = 222333444555666777888999) == 456901345788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222333444555666777888999) == 456901345788: {e}')
    
    total += 1
    try:
        result = candidate(num = 2222222222) == 44444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2222222222) == 44444: {e}')
    
    total += 1
    try:
        result = candidate(num = 2020202020) == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2020202020) == 244: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222222222222222222222222222222) == 444444444444444444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222222222222222222222222222222) == 444444444444444444: {e}')
    
    total += 1
    try:
        result = candidate(num = 1357913579) == 27158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1357913579) == 27158: {e}')
    
    total += 1
    try:
        result = candidate(num = 2323232323) == 44566
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2323232323) == 44566: {e}')
    
    total += 1
    try:
        result = candidate(num = 6060606060) == 732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 6060606060) == 732: {e}')
    
    total += 1
    try:
        result = candidate(num = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679) == 12223444445666667888901112333355557777779999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679) == 12223444445666667888901112333355557777779999998: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 87654321) == 3825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 87654321) == 3825: {e}')
    
    total += 1
    try:
        result = candidate(num = 999998888877777666665555544444333332222211111) == 12244566890113345577898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999998888877777666665555544444333332222211111) == 12244566890113345577898: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678901234567890) == 246913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678901234567890) == 246913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111222233334444) == 22446688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111222233334444) == 22446688: {e}')
    
    total += 1
    try:
        result = candidate(num = 2468024680) == 4936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2468024680) == 4936: {e}')
    
    total += 1
    try:
        result = candidate(num = 1122334455) == 24690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1122334455) == 24690: {e}')
    
    total += 1
    try:
        result = candidate(num = 333311112222) == 224466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333311112222) == 224466: {e}')
    
    total += 1
    try:
        result = candidate(num = 999111222333) == 234738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999111222333) == 234738: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789012) == 136047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789012) == 136047: {e}')
    
    total += 1
    try:
        result = candidate(num = 999888777666555444333222111) == 12456901345788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999888777666555444333222111) == 12456901345788: {e}')
    
    total += 1
    try:
        result = candidate(num = 8080808080) == 976
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8080808080) == 976: {e}')
    
    total += 1
    try:
        result = candidate(num = 321123321123) == 224466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 321123321123) == 224466: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432109876543210) == 246913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432109876543210) == 246913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 1223334444) == 35688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1223334444) == 35688: {e}')
    
    total += 1
    try:
        result = candidate(num = 1010101010) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1010101010) == 122: {e}')
    
    total += 1
    try:
        result = candidate(num = 999988887777666655554444333322221111) == 224466891133557798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999988887777666655554444333322221111) == 224466891133557798: {e}')
    
    total += 1
    try:
        result = candidate(num = 8051726349) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8051726349) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 4040404040) == 488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4040404040) == 488: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777777777777777) == 1555555554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777777777777777) == 1555555554: {e}')
    
    total += 1
    try:
        result = candidate(num = 5959595959) == 111598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5959595959) == 111598: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 2929292929) == 45298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2929292929) == 45298: {e}')
    
    total += 1
    try:
        result = candidate(num = 54321) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 54321) == 159: {e}')
    
    total += 1
    try:
        result = candidate(num = 765432109876543210) == 24691357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 765432109876543210) == 24691357: {e}')
    
    total += 1
    try:
        result = candidate(num = 333322221111) == 224466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333322221111) == 224466: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999999) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999999) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233445566778899) == 246913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233445566778899) == 246913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890123456789) == 246913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890123456789) == 246913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 5432109876) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5432109876) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234321) == 1357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234321) == 1357: {e}')
    
    total += 1
    try:
        result = candidate(num = 5678901234) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5678901234) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 8070605040302010) == 3825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8070605040302010) == 3825: {e}')
    
    total += 1
    try:
        result = candidate(num = 5432112345) == 24690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5432112345) == 24690: {e}')
    
    total += 1
    try:
        result = candidate(num = 2468013579) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2468013579) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890987654321) == 246913578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890987654321) == 246913578: {e}')
    
    total += 1
    try:
        result = candidate(num = 12233344445555566666677777778888888899999999) == 3568911233455577779998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12233344445555566666677777778888888899999999) == 3568911233455577779998: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 9090909090) == 1098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9090909090) == 1098: {e}')
    
    total += 1
    try:
        result = candidate(num = 7654321098) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7654321098) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 8888888888888888888) == 9777777776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8888888888888888888) == 9777777776: {e}')
    
    total += 1
    try:
        result = candidate(num = 5050505050) == 610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5050505050) == 610: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333333333333333) == 666666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333333333333333) == 666666666: {e}')
    
    total += 1
    try:
        result = candidate(num = 5432109876543210) == 2469147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5432109876543210) == 2469147: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432100) == 16047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432100) == 16047: {e}')
    
    total += 1
    try:
        result = candidate(num = 90909090909090) == 10998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 90909090909090) == 10998: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 10) == 1
    assert candidate(num = 687) == 75
    assert candidate(num = 4325) == 59
    assert candidate(num = 1111111111) == 22222
    assert candidate(num = 1234) == 37
    assert candidate(num = 222) == 24
    assert candidate(num = 1000000000) == 1
    assert candidate(num = 111111) == 222
    assert candidate(num = 123456789) == 16047
    assert candidate(num = 9876543210) == 16047
    assert candidate(num = 111222333) == 12456
    assert candidate(num = 1999999999) == 119998
    assert candidate(num = 1020304050) == 159
    assert candidate(num = 29392342) == 4588
    assert candidate(num = 1001) == 2
    assert candidate(num = 543321) == 369
    assert candidate(num = 5555555555) == 111110
    assert candidate(num = 999999) == 1998
    assert candidate(num = 9191919191) == 23198
    assert candidate(num = 1000000) == 1
    assert candidate(num = 1357924680) == 16047
    assert candidate(num = 314159) == 284
    assert candidate(num = 444444444444444444) == 888888888
    assert candidate(num = 2233445566778899) == 46913578
    assert candidate(num = 567894321) == 16047
    assert candidate(num = 99991111) == 2398
    assert candidate(num = 5647382910) == 16047
    assert candidate(num = 1000000009) == 10
    assert candidate(num = 100100100100) == 22
    assert candidate(num = 4444444444) == 88888
    assert candidate(num = 99887766554433221100) == 246913578
    assert candidate(num = 303030303030) == 666
    assert candidate(num = 4444455555) == 89010
    assert candidate(num = 111222333444) == 234678
    assert candidate(num = 111222333444555666777888999) == 12456901345788
    assert candidate(num = 3030303030) == 366
    assert candidate(num = 111122223333444455556666777788889999) == 224466891133557798
    assert candidate(num = 594939291909) == 160998
    assert candidate(num = 7070707070) == 854
    assert candidate(num = 12345678987654321) == 135802467
    assert candidate(num = 8642013579) == 16047
    assert candidate(num = 8642086420) == 4936
    assert candidate(num = 1298765432) == 36047
    assert candidate(num = 111222333444555) == 12456900
    assert candidate(num = 222333444555666777888999) == 456901345788
    assert candidate(num = 2222222222) == 44444
    assert candidate(num = 2020202020) == 244
    assert candidate(num = 222222222222222222222222222222222222) == 444444444444444444
    assert candidate(num = 1357913579) == 27158
    assert candidate(num = 2323232323) == 44566
    assert candidate(num = 6060606060) == 732
    assert candidate(num = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679) == 12223444445666667888901112333355557777779999998
    assert candidate(num = 1000000001) == 2
    assert candidate(num = 87654321) == 3825
    assert candidate(num = 999998888877777666665555544444333332222211111) == 12244566890113345577898
    assert candidate(num = 12345678901234567890) == 246913578
    assert candidate(num = 1111222233334444) == 22446688
    assert candidate(num = 2468024680) == 4936
    assert candidate(num = 1122334455) == 24690
    assert candidate(num = 333311112222) == 224466
    assert candidate(num = 999111222333) == 234738
    assert candidate(num = 123456789012) == 136047
    assert candidate(num = 999888777666555444333222111) == 12456901345788
    assert candidate(num = 8080808080) == 976
    assert candidate(num = 321123321123) == 224466
    assert candidate(num = 98765432109876543210) == 246913578
    assert candidate(num = 1223334444) == 35688
    assert candidate(num = 1010101010) == 122
    assert candidate(num = 999988887777666655554444333322221111) == 224466891133557798
    assert candidate(num = 8051726349) == 16047
    assert candidate(num = 4040404040) == 488
    assert candidate(num = 777777777777777777) == 1555555554
    assert candidate(num = 5959595959) == 111598
    assert candidate(num = 987654321) == 16047
    assert candidate(num = 2929292929) == 45298
    assert candidate(num = 54321) == 159
    assert candidate(num = 765432109876543210) == 24691357
    assert candidate(num = 333322221111) == 224466
    assert candidate(num = 9999999999) == 199998
    assert candidate(num = 112233445566778899) == 246913578
    assert candidate(num = 1234567890123456789) == 246913578
    assert candidate(num = 5432109876) == 16047
    assert candidate(num = 1234321) == 1357
    assert candidate(num = 5678901234) == 16047
    assert candidate(num = 8070605040302010) == 3825
    assert candidate(num = 5432112345) == 24690
    assert candidate(num = 2468013579) == 16047
    assert candidate(num = 1234567890987654321) == 246913578
    assert candidate(num = 12233344445555566666677777778888888899999999) == 3568911233455577779998
    assert candidate(num = 1234567890) == 16047
    assert candidate(num = 9090909090) == 1098
    assert candidate(num = 7654321098) == 16047
    assert candidate(num = 8888888888888888888) == 9777777776
    assert candidate(num = 5050505050) == 610
    assert candidate(num = 333333333333333333) == 666666666
    assert candidate(num = 5432109876543210) == 2469147
    assert candidate(num = 98765432100) == 16047
    assert candidate(num = 90909090909090) == 10998


