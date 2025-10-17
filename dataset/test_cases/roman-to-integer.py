def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "XCIX") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XCIX") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCMXCIX") == 2999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCMXCIX") == 2999: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCMXCIX") == 3999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCMXCIX") == 3999: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCXXI") == 621
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCXXI") == 621: {e}')
    
    total += 1
    try:
        result = candidate(s = "XC") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XC") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "VIII") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VIII") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "XV") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XV") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXVII") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXVII") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "IX") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IX") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCLXXIX") == 779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCLXXIX") == 779: {e}')
    
    total += 1
    try:
        result = candidate(s = "XX") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XX") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "CDXLIV") == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CDXLIV") == 444: {e}')
    
    total += 1
    try:
        result = candidate(s = "LVIII") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LVIII") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "CM") == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CM") == 900: {e}')
    
    total += 1
    try:
        result = candidate(s = "D") == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "D") == 500: {e}')
    
    total += 1
    try:
        result = candidate(s = "X") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "X") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "IV") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "IV") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXV") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXV") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXX") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXX") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "XL") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XL") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMDCCCLXXXVIII") == 3888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMDCCCLXXXVIII") == 3888: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXIX") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXIX") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "XLIV") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XLIV") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "CCCXCIX") == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CCCXCIX") == 399: {e}')
    
    total += 1
    try:
        result = candidate(s = "CD") == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CD") == 400: {e}')
    
    total += 1
    try:
        result = candidate(s = "LXX") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LXX") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "CCC") == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CCC") == 300: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMM") == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMM") == 3000: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMXCIV") == 1994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMXCIV") == 1994: {e}')
    
    total += 1
    try:
        result = candidate(s = "III") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "III") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "MDCCCLXXIV") == 1874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MDCCCLXXIV") == 1874: {e}')
    
    total += 1
    try:
        result = candidate(s = "CMXCIX") == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CMXCIX") == 999: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCDXCIX") == 2499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCDXCIX") == 2499: {e}')
    
    total += 1
    try:
        result = candidate(s = "M") == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M") == 1000: {e}')
    
    total += 1
    try:
        result = candidate(s = "CCXLVI") == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CCXLVI") == 246: {e}')
    
    total += 1
    try:
        result = candidate(s = "CC") == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CC") == 200: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCLXXIV") == 774
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCLXXIV") == 774: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCCCLXXXIX") == 1389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCCCLXXXIX") == 1389: {e}')
    
    total += 1
    try:
        result = candidate(s = "CMLXXXVII") == 987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CMLXXXVII") == 987: {e}')
    
    total += 1
    try:
        result = candidate(s = "XCIV") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XCIV") == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "MDCCLXXVI") == 1776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MDCCLXXVI") == 1776: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCLXXVI") == 776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCLXXVI") == 776: {e}')
    
    total += 1
    try:
        result = candidate(s = "CMXLVII") == 947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CMXLVII") == 947: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCMLXXIV") == 3974
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCMLXXIV") == 3974: {e}')
    
    total += 1
    try:
        result = candidate(s = "MDCCCLXXI") == 1871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MDCCCLXXI") == 1871: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMDCCCLXXVII") == 3877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMDCCCLXXVII") == 3877: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCMXCXCIX") == 4089
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCMXCXCIX") == 4089: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMLXXVIII") == 3078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMLXXVIII") == 3078: {e}')
    
    total += 1
    try:
        result = candidate(s = "CCCLXXIV") == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CCCLXXIV") == 374: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMXLIV") == 1944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMXLIV") == 1944: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCDLXXI") == 2471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCDLXXI") == 2471: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCCLXXXVIII") == 888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCCLXXXVIII") == 888: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMDCCCLXXIV") == 2874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMDCCCLXXIV") == 2874: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCDXLIV") == 2444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCDXLIV") == 2444: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMDCCCLXXVII") == 2877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMDCCCLXXVII") == 2877: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMDCCCXCIX") == 3899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMDCCCXCIX") == 3899: {e}')
    
    total += 1
    try:
        result = candidate(s = "LXXXIX") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LXXXIX") == 89: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCCLXXVIII") == 878
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCCLXXVIII") == 878: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMXXIII") == 2023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMXXIII") == 2023: {e}')
    
    total += 1
    try:
        result = candidate(s = "LXXXVII") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LXXXVII") == 87: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCMXCXC") == 4080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCMXCXC") == 4080: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCCXC") == 890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCCXC") == 890: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCMCCXCIX") == 3199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCMCCXCIX") == 3199: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMDCCCLXXX") == 3880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMDCCCLXXX") == 3880: {e}')
    
    total += 1
    try:
        result = candidate(s = "MDCCCCLXXV") == 1975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MDCCCCLXXV") == 1975: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMXCMLXXIX") == 2869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMXCMLXXIX") == 2869: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMDCCCLXXIX") == 3879
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMDCCCLXXIX") == 3879: {e}')
    
    total += 1
    try:
        result = candidate(s = "CDXC") == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CDXC") == 490: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMLXXI") == 1971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMLXXI") == 1971: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMLIV") == 1954
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMLIV") == 1954: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMDCCCXCIX") == 2899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMDCCCXCIX") == 2899: {e}')
    
    total += 1
    try:
        result = candidate(s = "CCXCIX") == 299
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CCXCIX") == 299: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCMXCCLXXVIII") == 4168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCMXCCLXXVIII") == 4168: {e}')
    
    total += 1
    try:
        result = candidate(s = "CDXCIX") == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CDXCIX") == 499: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCMLXXIX") == 3979
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCMLXXIX") == 3979: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCLXXVIII") == 778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCLXXVIII") == 778: {e}')
    
    total += 1
    try:
        result = candidate(s = "MDCCCLXXVIII") == 1878
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MDCCCLXXVIII") == 1878: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMDCCCLXXXVIII") == 2888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMDCCCLXXXVIII") == 2888: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMXLVII") == 1947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMXLVII") == 1947: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCXXVIII") == 628
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCXXVIII") == 628: {e}')
    
    total += 1
    try:
        result = candidate(s = "CCXLVIII") == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CCXLVIII") == 248: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCDXLIV") == 3444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCDXLIV") == 3444: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCCXCIX") == 899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCCXCIX") == 899: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCCXCIV") == 894
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCCXCIV") == 894: {e}')
    
    total += 1
    try:
        result = candidate(s = "DCCCLXXIV") == 874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DCCCLXXIV") == 874: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMLXXIII") == 1973
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMLXXIII") == 1973: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMMCDXCIX") == 3499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMMCDXCIX") == 3499: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCDLXXVIII") == 2478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCDLXXVIII") == 2478: {e}')
    
    total += 1
    try:
        result = candidate(s = "LVIV") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LVIV") == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "MMCDXXI") == 2421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MMCDXXI") == 2421: {e}')
    
    total += 1
    try:
        result = candidate(s = "MDCCCLXXVII") == 1877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MDCCCLXXVII") == 1877: {e}')
    
    total += 1
    try:
        result = candidate(s = "LXXXIV") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LXXXIV") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "CMXLIV") == 944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CMXLIV") == 944: {e}')
    
    total += 1
    try:
        result = candidate(s = "MCMLXXXIV") == 1984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MCMLXXXIV") == 1984: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "XCIX") == 99
    assert candidate(s = "MMCMXCIX") == 2999
    assert candidate(s = "MMMCMXCIX") == 3999
    assert candidate(s = "DCXXI") == 621
    assert candidate(s = "XC") == 90
    assert candidate(s = "VIII") == 8
    assert candidate(s = "XV") == 15
    assert candidate(s = "XXVII") == 27
    assert candidate(s = "IX") == 9
    assert candidate(s = "DCCLXXIX") == 779
    assert candidate(s = "XX") == 20
    assert candidate(s = "CDXLIV") == 444
    assert candidate(s = "LVIII") == 58
    assert candidate(s = "CM") == 900
    assert candidate(s = "D") == 500
    assert candidate(s = "X") == 10
    assert candidate(s = "IV") == 4
    assert candidate(s = "XXV") == 25
    assert candidate(s = "XXX") == 30
    assert candidate(s = "XL") == 40
    assert candidate(s = "MMMDCCCLXXXVIII") == 3888
    assert candidate(s = "XXXIX") == 39
    assert candidate(s = "XLIV") == 44
    assert candidate(s = "CCCXCIX") == 399
    assert candidate(s = "CD") == 400
    assert candidate(s = "LXX") == 70
    assert candidate(s = "CCC") == 300
    assert candidate(s = "MMM") == 3000
    assert candidate(s = "MCMXCIV") == 1994
    assert candidate(s = "III") == 3
    assert candidate(s = "MDCCCLXXIV") == 1874
    assert candidate(s = "CMXCIX") == 999
    assert candidate(s = "MMCDXCIX") == 2499
    assert candidate(s = "M") == 1000
    assert candidate(s = "CCXLVI") == 246
    assert candidate(s = "CC") == 200
    assert candidate(s = "DCCLXXIV") == 774
    assert candidate(s = "MCCCLXXXIX") == 1389
    assert candidate(s = "CMLXXXVII") == 987
    assert candidate(s = "XCIV") == 94
    assert candidate(s = "MDCCLXXVI") == 1776
    assert candidate(s = "DCCLXXVI") == 776
    assert candidate(s = "CMXLVII") == 947
    assert candidate(s = "MMMCMLXXIV") == 3974
    assert candidate(s = "MDCCCLXXI") == 1871
    assert candidate(s = "MMMDCCCLXXVII") == 3877
    assert candidate(s = "MMMCMXCXCIX") == 4089
    assert candidate(s = "MMMLXXVIII") == 3078
    assert candidate(s = "CCCLXXIV") == 374
    assert candidate(s = "MCMXLIV") == 1944
    assert candidate(s = "MMCDLXXI") == 2471
    assert candidate(s = "DCCCLXXXVIII") == 888
    assert candidate(s = "MMDCCCLXXIV") == 2874
    assert candidate(s = "MMCDXLIV") == 2444
    assert candidate(s = "MMDCCCLXXVII") == 2877
    assert candidate(s = "MMMDCCCXCIX") == 3899
    assert candidate(s = "LXXXIX") == 89
    assert candidate(s = "DCCCLXXVIII") == 878
    assert candidate(s = "MMXXIII") == 2023
    assert candidate(s = "LXXXVII") == 87
    assert candidate(s = "MMMCMXCXC") == 4080
    assert candidate(s = "DCCCXC") == 890
    assert candidate(s = "MMCMCCXCIX") == 3199
    assert candidate(s = "MMMDCCCLXXX") == 3880
    assert candidate(s = "MDCCCCLXXV") == 1975
    assert candidate(s = "MCMXCMLXXIX") == 2869
    assert candidate(s = "MMMDCCCLXXIX") == 3879
    assert candidate(s = "CDXC") == 490
    assert candidate(s = "MCMLXXI") == 1971
    assert candidate(s = "MCMLIV") == 1954
    assert candidate(s = "MMDCCCXCIX") == 2899
    assert candidate(s = "CCXCIX") == 299
    assert candidate(s = "MMMCMXCCLXXVIII") == 4168
    assert candidate(s = "CDXCIX") == 499
    assert candidate(s = "MMMCMLXXIX") == 3979
    assert candidate(s = "DCCLXXVIII") == 778
    assert candidate(s = "MDCCCLXXVIII") == 1878
    assert candidate(s = "MMDCCCLXXXVIII") == 2888
    assert candidate(s = "MCMXLVII") == 1947
    assert candidate(s = "DCXXVIII") == 628
    assert candidate(s = "CCXLVIII") == 248
    assert candidate(s = "MMMCDXLIV") == 3444
    assert candidate(s = "DCCCXCIX") == 899
    assert candidate(s = "DCCCXCIV") == 894
    assert candidate(s = "DCCCLXXIV") == 874
    assert candidate(s = "MCMLXXIII") == 1973
    assert candidate(s = "MMMCDXCIX") == 3499
    assert candidate(s = "MMCDLXXVIII") == 2478
    assert candidate(s = "LVIV") == 59
    assert candidate(s = "MMCDXXI") == 2421
    assert candidate(s = "MDCCCLXXVII") == 1877
    assert candidate(s = "LXXXIV") == 84
    assert candidate(s = "CMXLIV") == 944
    assert candidate(s = "MCMLXXXIV") == 1984


