def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 31) == "1f"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 31) == "1f": {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == "a": {e}')
    
    total += 1
    try:
        result = candidate(num = -4294967296) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -4294967296) == "": {e}')
    
    total += 1
    try:
        result = candidate(num = 16777215) == "ffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16777215) == "ffffff": {e}')
    
    total += 1
    try:
        result = candidate(num = -16777215) == "ff000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -16777215) == "ff000001": {e}')
    
    total += 1
    try:
        result = candidate(num = -1) == "ffffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1) == "ffffffff": {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967295) == "ffffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967295) == "ffffffff": {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == "0": {e}')
    
    total += 1
    try:
        result = candidate(num = -2147483648) == "80000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2147483648) == "80000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -255) == "ffffff01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -255) == "ffffff01": {e}')
    
    total += 1
    try:
        result = candidate(num = 255) == "ff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 255) == "ff": {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = -10) == "fffffff6"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -10) == "fffffff6": {e}')
    
    total += 1
    try:
        result = candidate(num = -4095) == "fffff001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -4095) == "fffff001": {e}')
    
    total += 1
    try:
        result = candidate(num = 4095) == "fff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4095) == "fff": {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == "7fffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == "7fffffff": {e}')
    
    total += 1
    try:
        result = candidate(num = 16) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16) == "10": {e}')
    
    total += 1
    try:
        result = candidate(num = 26) == "1a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 26) == "1a": {e}')
    
    total += 1
    try:
        result = candidate(num = 2097152) == "200000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2097152) == "200000": {e}')
    
    total += 1
    try:
        result = candidate(num = -4096) == "fffff000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -4096) == "fffff000": {e}')
    
    total += 1
    try:
        result = candidate(num = -1048575) == "fff00001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1048575) == "fff00001": {e}')
    
    total += 1
    try:
        result = candidate(num = -16777216) == "ff000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -16777216) == "ff000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1099511627776) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1099511627776) == "": {e}')
    
    total += 1
    try:
        result = candidate(num = -2147483647) == "80000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2147483647) == "80000001": {e}')
    
    total += 1
    try:
        result = candidate(num = 67553994410557436) == "fffffffc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 67553994410557436) == "fffffffc": {e}')
    
    total += 1
    try:
        result = candidate(num = 1048575) == "fffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048575) == "fffff": {e}')
    
    total += 1
    try:
        result = candidate(num = -1024) == "fffffc00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1024) == "fffffc00": {e}')
    
    total += 1
    try:
        result = candidate(num = -134217728) == "f8000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -134217728) == "f8000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -8589934591) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -8589934591) == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = -31) == "ffffffe1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -31) == "ffffffe1": {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == "75bcd15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == "75bcd15": {e}')
    
    total += 1
    try:
        result = candidate(num = 65535) == "ffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65535) == "ffff": {e}')
    
    total += 1
    try:
        result = candidate(num = -15) == "fffffff1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -15) == "fffffff1": {e}')
    
    total += 1
    try:
        result = candidate(num = 32768) == "8000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32768) == "8000": {e}')
    
    total += 1
    try:
        result = candidate(num = -131072) == "fffe0000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -131072) == "fffe0000": {e}')
    
    total += 1
    try:
        result = candidate(num = -89478485) == "faaaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -89478485) == "faaaaaab": {e}')
    
    total += 1
    try:
        result = candidate(num = -65535) == "ffff0001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -65535) == "ffff0001": {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483646) == "7ffffffe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483646) == "7ffffffe": {e}')
    
    total += 1
    try:
        result = candidate(num = 134217728) == "8000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 134217728) == "8000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -987654321) == "c521974f"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -987654321) == "c521974f": {e}')
    
    total += 1
    try:
        result = candidate(num = 268435456) == "10000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 268435456) == "10000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 8589934591) == "ffffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8589934591) == "ffffffff": {e}')
    
    total += 1
    try:
        result = candidate(num = 4096) == "1000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4096) == "1000": {e}')
    
    total += 1
    try:
        result = candidate(num = -268435456) == "f0000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -268435456) == "f0000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1048576) == "100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048576) == "100000": {e}')
    
    total += 1
    try:
        result = candidate(num = -1073741825) == "bfffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1073741825) == "bfffffff": {e}')
    
    total += 1
    try:
        result = candidate(num = -123456789) == "f8a432eb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -123456789) == "f8a432eb": {e}')
    
    total += 1
    try:
        result = candidate(num = 1024) == "400"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024) == "400": {e}')
    
    total += 1
    try:
        result = candidate(num = -4294967294) == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -4294967294) == "2": {e}')
    
    total += 1
    try:
        result = candidate(num = -256) == "ffffff00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -256) == "ffffff00": {e}')
    
    total += 1
    try:
        result = candidate(num = 16777216) == "1000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16777216) == "1000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -1000000) == "fff0bdc0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1000000) == "fff0bdc0": {e}')
    
    total += 1
    try:
        result = candidate(num = -1048576) == "fff00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1048576) == "fff00000": {e}')
    
    total += 1
    try:
        result = candidate(num = -16) == "fffffff0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -16) == "fffffff0": {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == "f4240"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == "f4240": {e}')
    
    total += 1
    try:
        result = candidate(num = 89478485) == "5555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 89478485) == "5555555": {e}')
    
    total += 1
    try:
        result = candidate(num = 65536) == "10000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65536) == "10000": {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967294) == "fffffffe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967294) == "fffffffe": {e}')
    
    total += 1
    try:
        result = candidate(num = -2) == "fffffffe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2) == "fffffffe": {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == "f"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == "f": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 31) == "1f"
    assert candidate(num = 10) == "a"
    assert candidate(num = -4294967296) == ""
    assert candidate(num = 16777215) == "ffffff"
    assert candidate(num = -16777215) == "ff000001"
    assert candidate(num = -1) == "ffffffff"
    assert candidate(num = 4294967295) == "ffffffff"
    assert candidate(num = 0) == "0"
    assert candidate(num = -2147483648) == "80000000"
    assert candidate(num = -255) == "ffffff01"
    assert candidate(num = 255) == "ff"
    assert candidate(num = 1) == "1"
    assert candidate(num = -10) == "fffffff6"
    assert candidate(num = -4095) == "fffff001"
    assert candidate(num = 4095) == "fff"
    assert candidate(num = 2147483647) == "7fffffff"
    assert candidate(num = 16) == "10"
    assert candidate(num = 26) == "1a"
    assert candidate(num = 2097152) == "200000"
    assert candidate(num = -4096) == "fffff000"
    assert candidate(num = -1048575) == "fff00001"
    assert candidate(num = -16777216) == "ff000000"
    assert candidate(num = 1099511627776) == ""
    assert candidate(num = -2147483647) == "80000001"
    assert candidate(num = 67553994410557436) == "fffffffc"
    assert candidate(num = 1048575) == "fffff"
    assert candidate(num = -1024) == "fffffc00"
    assert candidate(num = -134217728) == "f8000000"
    assert candidate(num = -8589934591) == "1"
    assert candidate(num = -31) == "ffffffe1"
    assert candidate(num = 123456789) == "75bcd15"
    assert candidate(num = 65535) == "ffff"
    assert candidate(num = -15) == "fffffff1"
    assert candidate(num = 32768) == "8000"
    assert candidate(num = -131072) == "fffe0000"
    assert candidate(num = -89478485) == "faaaaaab"
    assert candidate(num = -65535) == "ffff0001"
    assert candidate(num = 2147483646) == "7ffffffe"
    assert candidate(num = 134217728) == "8000000"
    assert candidate(num = -987654321) == "c521974f"
    assert candidate(num = 268435456) == "10000000"
    assert candidate(num = 8589934591) == "ffffffff"
    assert candidate(num = 4096) == "1000"
    assert candidate(num = -268435456) == "f0000000"
    assert candidate(num = 1048576) == "100000"
    assert candidate(num = -1073741825) == "bfffffff"
    assert candidate(num = -123456789) == "f8a432eb"
    assert candidate(num = 1024) == "400"
    assert candidate(num = -4294967294) == "2"
    assert candidate(num = -256) == "ffffff00"
    assert candidate(num = 16777216) == "1000000"
    assert candidate(num = -1000000) == "fff0bdc0"
    assert candidate(num = -1048576) == "fff00000"
    assert candidate(num = -16) == "fffffff0"
    assert candidate(num = 1000000) == "f4240"
    assert candidate(num = 89478485) == "5555555"
    assert candidate(num = 65536) == "10000"
    assert candidate(num = 4294967294) == "fffffffe"
    assert candidate(num = -2) == "fffffffe"
    assert candidate(num = 15) == "f"


