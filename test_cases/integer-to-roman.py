def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 44) == "XLIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 44) == "XLIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 9) == "IX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == "IX": {e}')
    
    total += 1
    try:
        result = candidate(num = 4) == "IV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4) == "IV": {e}')
    
    total += 1
    try:
        result = candidate(num = 2023) == "MMXXIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2023) == "MMXXIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 589) == "DLXXXIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 589) == "DLXXXIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 444) == "CDXLIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444) == "CDXLIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 1000) == "M"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000) == "M": {e}')
    
    total += 1
    try:
        result = candidate(num = 789) == "DCCLXXXIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 789) == "DCCLXXXIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 58) == "LVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 58) == "LVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 3999) == "MMMCMXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3999) == "MMMCMXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 399) == "CCCXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 399) == "CCCXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 3749) == "MMMDCCXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3749) == "MMMDCCXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1994) == "MCMXCIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1994) == "MCMXCIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == "I"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == "I": {e}')
    
    total += 1
    try:
        result = candidate(num = 3549) == "MMMDXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3549) == "MMMDXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 944) == "CMXLIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 944) == "CMXLIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 199) == "CXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199) == "CXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 60) == "LX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 60) == "LX": {e}')
    
    total += 1
    try:
        result = candidate(num = 621) == "DCXXI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 621) == "DCXXI": {e}')
    
    total += 1
    try:
        result = candidate(num = 3000) == "MMM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000) == "MMM": {e}')
    
    total += 1
    try:
        result = candidate(num = 1499) == "MCDXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1499) == "MCDXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1602) == "MDCII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1602) == "MDCII": {e}')
    
    total += 1
    try:
        result = candidate(num = 999) == "CMXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999) == "CMXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 207) == "CCVII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 207) == "CCVII": {e}')
    
    total += 1
    try:
        result = candidate(num = 2078) == "MMLXXVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2078) == "MMLXXVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 894) == "DCCCXCIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 894) == "DCCCXCIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 2421) == "MMCDXXI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2421) == "MMCDXXI": {e}')
    
    total += 1
    try:
        result = candidate(num = 2999) == "MMCMXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2999) == "MMCMXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 149) == "CXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 149) == "CXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 3949) == "MMMCMXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3949) == "MMMCMXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 99) == "XCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99) == "XCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1492) == "MCDXCII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1492) == "MCDXCII": {e}')
    
    total += 1
    try:
        result = candidate(num = 1234) == "MCCXXXIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234) == "MCCXXXIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 647) == "DCXLVII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 647) == "DCXLVII": {e}')
    
    total += 1
    try:
        result = candidate(num = 844) == "DCCCXLIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 844) == "DCCCXLIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 798) == "DCCXCVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 798) == "DCCXCVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 1043) == "MXLIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1043) == "MXLIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 3001) == "MMMI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3001) == "MMMI": {e}')
    
    total += 1
    try:
        result = candidate(num = 2345) == "MMCCCXLV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2345) == "MMCCCXLV": {e}')
    
    total += 1
    try:
        result = candidate(num = 500) == "D"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500) == "D": {e}')
    
    total += 1
    try:
        result = candidate(num = 746) == "DCCXLVI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 746) == "DCCXLVI": {e}')
    
    total += 1
    try:
        result = candidate(num = 2944) == "MMCMXLIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2944) == "MMCMXLIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 1500) == "MD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1500) == "MD": {e}')
    
    total += 1
    try:
        result = candidate(num = 3357) == "MMMCCCLVII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3357) == "MMMCCCLVII": {e}')
    
    total += 1
    try:
        result = candidate(num = 3388) == "MMMCCCLXXXVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3388) == "MMMCCCLXXXVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 1597) == "MDXCVII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1597) == "MDXCVII": {e}')
    
    total += 1
    try:
        result = candidate(num = 2737) == "MMDCCXXXVII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2737) == "MMDCCXXXVII": {e}')
    
    total += 1
    try:
        result = candidate(num = 40) == "XL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 40) == "XL": {e}')
    
    total += 1
    try:
        result = candidate(num = 2708) == "MMDCCVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2708) == "MMDCCVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 349) == "CCCXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 349) == "CCCXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 799) == "DCCXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 799) == "DCCXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1001) == "MI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001) == "MI": {e}')
    
    total += 1
    try:
        result = candidate(num = 583) == "DLXXXIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 583) == "DLXXXIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 2422) == "MMCDXXII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2422) == "MMCDXXII": {e}')
    
    total += 1
    try:
        result = candidate(num = 891) == "DCCCXCI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 891) == "DCCCXCI": {e}')
    
    total += 1
    try:
        result = candidate(num = 39) == "XXXIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 39) == "XXXIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1444) == "MCDXLIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1444) == "MCDXLIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 1094) == "MXCIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1094) == "MXCIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 2751) == "MMDCCLI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2751) == "MMDCCLI": {e}')
    
    total += 1
    try:
        result = candidate(num = 3888) == "MMMDCCCLXXXVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3888) == "MMMDCCCLXXXVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 2994) == "MMCMXCIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2994) == "MMCMXCIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 876) == "DCCCLXXVI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 876) == "DCCCLXXVI": {e}')
    
    total += 1
    try:
        result = candidate(num = 1009) == "MIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1009) == "MIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1648) == "MDCXLVIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1648) == "MDCXLVIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 1066) == "MLXVI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1066) == "MLXVI": {e}')
    
    total += 1
    try:
        result = candidate(num = 2349) == "MMCCCXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2349) == "MMCCCXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 2763) == "MMDCCLXIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2763) == "MMDCCLXIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 1646) == "MDCXLVI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1646) == "MDCXLVI": {e}')
    
    total += 1
    try:
        result = candidate(num = 3499) == "MMMCDXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3499) == "MMMCDXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1529) == "MDXXIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1529) == "MDXXIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1453) == "MCDLIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1453) == "MCDLIII": {e}')
    
    total += 1
    try:
        result = candidate(num = 1099) == "MXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1099) == "MXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 299) == "CCXCIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 299) == "CCXCIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 89) == "LXXXIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 89) == "LXXXIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 2074) == "MMLXXIV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2074) == "MMLXXIV": {e}')
    
    total += 1
    try:
        result = candidate(num = 2549) == "MMDXLIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2549) == "MMDXLIX": {e}')
    
    total += 1
    try:
        result = candidate(num = 1423) == "MCDXXIII"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1423) == "MCDXXIII": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 44) == "XLIV"
    assert candidate(num = 9) == "IX"
    assert candidate(num = 4) == "IV"
    assert candidate(num = 2023) == "MMXXIII"
    assert candidate(num = 589) == "DLXXXIX"
    assert candidate(num = 444) == "CDXLIV"
    assert candidate(num = 1000) == "M"
    assert candidate(num = 789) == "DCCLXXXIX"
    assert candidate(num = 58) == "LVIII"
    assert candidate(num = 3999) == "MMMCMXCIX"
    assert candidate(num = 399) == "CCCXCIX"
    assert candidate(num = 3749) == "MMMDCCXLIX"
    assert candidate(num = 1994) == "MCMXCIV"
    assert candidate(num = 1) == "I"
    assert candidate(num = 3549) == "MMMDXLIX"
    assert candidate(num = 944) == "CMXLIV"
    assert candidate(num = 199) == "CXCIX"
    assert candidate(num = 60) == "LX"
    assert candidate(num = 621) == "DCXXI"
    assert candidate(num = 3000) == "MMM"
    assert candidate(num = 1499) == "MCDXCIX"
    assert candidate(num = 1602) == "MDCII"
    assert candidate(num = 999) == "CMXCIX"
    assert candidate(num = 207) == "CCVII"
    assert candidate(num = 2078) == "MMLXXVIII"
    assert candidate(num = 894) == "DCCCXCIV"
    assert candidate(num = 2421) == "MMCDXXI"
    assert candidate(num = 2999) == "MMCMXCIX"
    assert candidate(num = 149) == "CXLIX"
    assert candidate(num = 3949) == "MMMCMXLIX"
    assert candidate(num = 99) == "XCIX"
    assert candidate(num = 1492) == "MCDXCII"
    assert candidate(num = 1234) == "MCCXXXIV"
    assert candidate(num = 647) == "DCXLVII"
    assert candidate(num = 844) == "DCCCXLIV"
    assert candidate(num = 798) == "DCCXCVIII"
    assert candidate(num = 1043) == "MXLIII"
    assert candidate(num = 3001) == "MMMI"
    assert candidate(num = 2345) == "MMCCCXLV"
    assert candidate(num = 500) == "D"
    assert candidate(num = 746) == "DCCXLVI"
    assert candidate(num = 2944) == "MMCMXLIV"
    assert candidate(num = 1500) == "MD"
    assert candidate(num = 3357) == "MMMCCCLVII"
    assert candidate(num = 3388) == "MMMCCCLXXXVIII"
    assert candidate(num = 1597) == "MDXCVII"
    assert candidate(num = 2737) == "MMDCCXXXVII"
    assert candidate(num = 40) == "XL"
    assert candidate(num = 2708) == "MMDCCVIII"
    assert candidate(num = 349) == "CCCXLIX"
    assert candidate(num = 799) == "DCCXCIX"
    assert candidate(num = 1001) == "MI"
    assert candidate(num = 583) == "DLXXXIII"
    assert candidate(num = 2422) == "MMCDXXII"
    assert candidate(num = 891) == "DCCCXCI"
    assert candidate(num = 39) == "XXXIX"
    assert candidate(num = 1444) == "MCDXLIV"
    assert candidate(num = 1094) == "MXCIV"
    assert candidate(num = 2751) == "MMDCCLI"
    assert candidate(num = 3888) == "MMMDCCCLXXXVIII"
    assert candidate(num = 2994) == "MMCMXCIV"
    assert candidate(num = 876) == "DCCCLXXVI"
    assert candidate(num = 1009) == "MIX"
    assert candidate(num = 1648) == "MDCXLVIII"
    assert candidate(num = 1066) == "MLXVI"
    assert candidate(num = 2349) == "MMCCCXLIX"
    assert candidate(num = 2763) == "MMDCCLXIII"
    assert candidate(num = 1646) == "MDCXLVI"
    assert candidate(num = 3499) == "MMMCDXCIX"
    assert candidate(num = 1529) == "MDXXIX"
    assert candidate(num = 1453) == "MCDLIII"
    assert candidate(num = 1099) == "MXCIX"
    assert candidate(num = 299) == "CCXCIX"
    assert candidate(num = 89) == "LXXXIX"
    assert candidate(num = 2074) == "MMLXXIV"
    assert candidate(num = 2549) == "MMDXLIX"
    assert candidate(num = 1423) == "MCDXXIII"


