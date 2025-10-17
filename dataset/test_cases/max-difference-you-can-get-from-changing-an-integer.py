def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 1001100) == 8008800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001100) == 8008800: {e}')
    
    total += 1
    try:
        result = candidate(num = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 98789) == 81018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98789) == 81018: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456) == 820000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456) == 820000: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 810000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 810000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 8000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 8000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1221) == 8228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1221) == 8228: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 820000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 820000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111) == 8888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111) == 8888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 987789) == 810018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987789) == 810018: {e}')
    
    total += 1
    try:
        result = candidate(num = 1001001) == 8008008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001001) == 8008008: {e}')
    
    total += 1
    try:
        result = candidate(num = 12321) == 82028
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12321) == 82028: {e}')
    
    total += 1
    try:
        result = candidate(num = 555) == 888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555) == 888: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999) == 8888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999) == 8888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 123321) == 820028
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123321) == 820028: {e}')
    
    total += 1
    try:
        result = candidate(num = 99100099) == 88800088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99100099) == 88800088: {e}')
    
    total += 1
    try:
        result = candidate(num = 543212345) == 800000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 543212345) == 800000008: {e}')
    
    total += 1
    try:
        result = candidate(num = 599599599) == 800800800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 599599599) == 800800800: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000) == 800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000) == 800000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 12212212) == 82282282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12212212) == 82282282: {e}')
    
    total += 1
    try:
        result = candidate(num = 8877665544332211) == 8800000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8877665544332211) == 8800000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 109080706) == 809000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 109080706) == 809000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == 888888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == 888888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 890123456) == 800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 890123456) == 800000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 543210987) == 800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 543210987) == 800000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 111000111) == 888000888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111000111) == 888000888: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432109876543210) == 81000000008100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432109876543210) == 81000000008100000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000) == 80000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000) == 80000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 90000009) == 89999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 90000009) == 89999998: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234321) == 8200028
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234321) == 8200028: {e}')
    
    total += 1
    try:
        result = candidate(num = 999111111) == 888888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999111111) == 888888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 110101010) == 880808080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 110101010) == 880808080: {e}')
    
    total += 1
    try:
        result = candidate(num = 20202020) == 80808080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20202020) == 80808080: {e}')
    
    total += 1
    try:
        result = candidate(num = 567890123) == 800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567890123) == 800000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 5566778899) == 8800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5566778899) == 8800000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 909090909) == 898989898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 909090909) == 898989898: {e}')
    
    total += 1
    try:
        result = candidate(num = 44440000) == 88880000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 44440000) == 88880000: {e}')
    
    total += 1
    try:
        result = candidate(num = 3330333) == 8880888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3330333) == 8880888: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000001) == 80000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000001) == 80000008: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333) == 888222000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333) == 888222000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210) == 8100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210) == 8100000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 9191919) == 8888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9191919) == 8888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 98709870987) == 81008100810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98709870987) == 81008100810: {e}')
    
    total += 1
    try:
        result = candidate(num = 334455667788) == 880000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 334455667788) == 880000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 122121) == 822828
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 122121) == 822828: {e}')
    
    total += 1
    try:
        result = candidate(num = 8998) == 8008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8998) == 8008: {e}')
    
    total += 1
    try:
        result = candidate(num = 77777777) == 88888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 77777777) == 88888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 88888888) == 88888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88888888) == 88888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 19000000) == 89000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 19000000) == 89000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 200200200) == 800800800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 200200200) == 800800800: {e}')
    
    total += 1
    try:
        result = candidate(num = 1919191) == 8989898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1919191) == 8989898: {e}')
    
    total += 1
    try:
        result = candidate(num = 918273645) == 880000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 918273645) == 880000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000001) == 800000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000001) == 800000008: {e}')
    
    total += 1
    try:
        result = candidate(num = 11001100) == 88008800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11001100) == 88008800: {e}')
    
    total += 1
    try:
        result = candidate(num = 59595959) == 80808080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 59595959) == 80808080: {e}')
    
    total += 1
    try:
        result = candidate(num = 209209209) == 800800800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 209209209) == 800800800: {e}')
    
    total += 1
    try:
        result = candidate(num = 1100110011) == 8800880088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1100110011) == 8800880088: {e}')
    
    total += 1
    try:
        result = candidate(num = 333222111) == 888000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333222111) == 888000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 999000) == 888999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999000) == 888999: {e}')
    
    total += 1
    try:
        result = candidate(num = 90000000) == 89999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 90000000) == 89999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1098765432) == 8090000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1098765432) == 8090000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101) == 808080808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101) == 808080808: {e}')
    
    total += 1
    try:
        result = candidate(num = 57575757) == 80808080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 57575757) == 80808080: {e}')
    
    total += 1
    try:
        result = candidate(num = 123123123) == 820820820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123123123) == 820820820: {e}')
    
    total += 1
    try:
        result = candidate(num = 777770777) == 888880888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777770777) == 888880888: {e}')
    
    total += 1
    try:
        result = candidate(num = 123212321) == 820282028
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123212321) == 820282028: {e}')
    
    total += 1
    try:
        result = candidate(num = 90009) == 89998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 90009) == 89998: {e}')
    
    total += 1
    try:
        result = candidate(num = 1122334455) == 8822000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1122334455) == 8822000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 100100100) == 800800800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100100100) == 800800800: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999999) == 88888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999999) == 88888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000) == 800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000) == 800000: {e}')
    
    total += 1
    try:
        result = candidate(num = 109090909) == 809090909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 109090909) == 809090909: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == 888888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == 888888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000100) == 8000800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000100) == 8000800: {e}')
    
    total += 1
    try:
        result = candidate(num = 19191919) == 89898989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 19191919) == 89898989: {e}')
    
    total += 1
    try:
        result = candidate(num = 202020202) == 808080808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 202020202) == 808080808: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000001) == 8000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000001) == 8000008: {e}')
    
    total += 1
    try:
        result = candidate(num = 44444444) == 88888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 44444444) == 88888888: {e}')
    
    total += 1
    try:
        result = candidate(num = 8880888) == 8880888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8880888) == 8880888: {e}')
    
    total += 1
    try:
        result = candidate(num = 191919191) == 898989898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 191919191) == 898989898: {e}')
    
    total += 1
    try:
        result = candidate(num = 1230123) == 8200820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1230123) == 8200820: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 1001100) == 8008800
    assert candidate(num = 9) == 8
    assert candidate(num = 98789) == 81018
    assert candidate(num = 123456) == 820000
    assert candidate(num = 987654321) == 810000000
    assert candidate(num = 1000000) == 8000000
    assert candidate(num = 1221) == 8228
    assert candidate(num = 123456789) == 820000000
    assert candidate(num = 1111111) == 8888888
    assert candidate(num = 987789) == 810018
    assert candidate(num = 1001001) == 8008008
    assert candidate(num = 12321) == 82028
    assert candidate(num = 555) == 888
    assert candidate(num = 9999999) == 8888888
    assert candidate(num = 123321) == 820028
    assert candidate(num = 99100099) == 88800088
    assert candidate(num = 543212345) == 800000008
    assert candidate(num = 599599599) == 800800800
    assert candidate(num = 100000000) == 800000000
    assert candidate(num = 12212212) == 82282282
    assert candidate(num = 8877665544332211) == 8800000000000000
    assert candidate(num = 109080706) == 809000000
    assert candidate(num = 888888888) == 888888888
    assert candidate(num = 890123456) == 800000000
    assert candidate(num = 543210987) == 800000000
    assert candidate(num = 111000111) == 888000888
    assert candidate(num = 98765432109876543210) == 81000000008100000000
    assert candidate(num = 10000000) == 80000000
    assert candidate(num = 90000009) == 89999998
    assert candidate(num = 1234321) == 8200028
    assert candidate(num = 999111111) == 888888888
    assert candidate(num = 110101010) == 880808080
    assert candidate(num = 20202020) == 80808080
    assert candidate(num = 567890123) == 800000000
    assert candidate(num = 5566778899) == 8800000000
    assert candidate(num = 909090909) == 898989898
    assert candidate(num = 44440000) == 88880000
    assert candidate(num = 3330333) == 8880888
    assert candidate(num = 10000001) == 80000008
    assert candidate(num = 111222333) == 888222000
    assert candidate(num = 9876543210) == 8100000000
    assert candidate(num = 9191919) == 8888888
    assert candidate(num = 98709870987) == 81008100810
    assert candidate(num = 334455667788) == 880000000000
    assert candidate(num = 122121) == 822828
    assert candidate(num = 8998) == 8008
    assert candidate(num = 77777777) == 88888888
    assert candidate(num = 88888888) == 88888888
    assert candidate(num = 19000000) == 89000000
    assert candidate(num = 200200200) == 800800800
    assert candidate(num = 1919191) == 8989898
    assert candidate(num = 918273645) == 880000000
    assert candidate(num = 100000001) == 800000008
    assert candidate(num = 11001100) == 88008800
    assert candidate(num = 59595959) == 80808080
    assert candidate(num = 209209209) == 800800800
    assert candidate(num = 1100110011) == 8800880088
    assert candidate(num = 333222111) == 888000000
    assert candidate(num = 999000) == 888999
    assert candidate(num = 90000000) == 89999999
    assert candidate(num = 1098765432) == 8090000000
    assert candidate(num = 101010101) == 808080808
    assert candidate(num = 57575757) == 80808080
    assert candidate(num = 123123123) == 820820820
    assert candidate(num = 777770777) == 888880888
    assert candidate(num = 123212321) == 820282028
    assert candidate(num = 90009) == 89998
    assert candidate(num = 1122334455) == 8822000000
    assert candidate(num = 100100100) == 800800800
    assert candidate(num = 99999999) == 88888888
    assert candidate(num = 100000) == 800000
    assert candidate(num = 109090909) == 809090909
    assert candidate(num = 999999999) == 888888888
    assert candidate(num = 1000100) == 8000800
    assert candidate(num = 19191919) == 89898989
    assert candidate(num = 202020202) == 808080808
    assert candidate(num = 1000001) == 8000008
    assert candidate(num = 44444444) == 88888888
    assert candidate(num = 8880888) == 8880888
    assert candidate(num = 191919191) == 898989898
    assert candidate(num = 1230123) == 8200820


