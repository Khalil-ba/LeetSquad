def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = "2718281828459045") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2718281828459045") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890123456789") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890123456789") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "257") == "IOI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "257") == "IOI": {e}')
    
    total += 1
    try:
        result = candidate(num = "3") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1") == "I"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1") == "I": {e}')
    
    total += 1
    try:
        result = candidate(num = "4095") == "FFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4095") == "FFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "16") == "IO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "16") == "IO": {e}')
    
    total += 1
    try:
        result = candidate(num = "43981") == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "43981") == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000000") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000000") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "4294967295") == "FFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4294967295") == "FFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "1048575") == "FFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1048575") == "FFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "131072") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "131072") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "94906265") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "94906265") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "11259375") == "ABCDEF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11259375") == "ABCDEF": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890123456789012345678901") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890123456789012345678901") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "18014398509481984") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "18014398509481984") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "67891011") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "67891011") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "65535") == "FFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "65535") == "FFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "1152921504606846976") == "IOOOOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1152921504606846976") == "IOOOOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "274877906944") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "274877906944") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "3074457345618258604861706883955240992") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3074457345618258604861706883955240992") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "549755813888") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "549755813888") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "14615016373309029182036848327646332848676852880698050517756256000000000000000") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "14615016373309029182036848327646332848676852880698050517756256000000000000000") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "3489163") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3489163") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "11") == "B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11") == "B": {e}')
    
    total += 1
    try:
        result = candidate(num = "10") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10") == "A": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678901234567") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678901234567") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "68719476735") == "FFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "68719476735") == "FFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "17592186044416") == "IOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "17592186044416") == "IOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "1048576") == "IOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1048576") == "IOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999999999") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999999999") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "35184372088832") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "35184372088832") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "888888888888") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "888888888888") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "16777216") == "IOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "16777216") == "IOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "4398046511104") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4398046511104") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "67000000000000000000") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "67000000000000000000") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "36893488147419103232") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "36893488147419103232") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111111") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111111") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "111111111111") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111111111111") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "72057594037927935") == "FFFFFFFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "72057594037927935") == "FFFFFFFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890123") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890123") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "4096") == "IOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4096") == "IOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "271828182845904523536028747135266249775724709369999") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "271828182845904523536028747135266249775724709369999") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "281474976710655") == "FFFFFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "281474976710655") == "FFFFFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "211106232532973781056") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "211106232532973781056") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "2199023255551") == "IFFFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2199023255551") == "IFFFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "72057594037927936") == "IOOOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "72057594037927936") == "IOOOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "15") == "F"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "15") == "F": {e}')
    
    total += 1
    try:
        result = candidate(num = "32768") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "32768") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "144115188075855872") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "144115188075855872") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "100000000000") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100000000000") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "9007199254740991") == "IFFFFFFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9007199254740991") == "IFFFFFFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "67890") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "67890") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "79228162514264337593543950336") == "IOOOOOOOOOOOOOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "79228162514264337593543950336") == "IOOOOOOOOOOOOOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "18446744073709551615") == "FFFFFFFFFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "18446744073709551615") == "FFFFFFFFFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "2199023255552") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2199023255552") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "288230376151711744") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "288230376151711744") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "777") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "777") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "678230456789123456789") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "678230456789123456789") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000001") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000001") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "43690") == "AAAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "43690") == "AAAA": {e}')
    
    total += 1
    try:
        result = candidate(num = "134217728") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "134217728") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "2147483647") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2147483647") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "57896044618658097711785492504343953926634992332820282019728792003956564819949") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "57896044618658097711785492504343953926634992332820282019728792003956564819949") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "18446744073709551616") == "IOOOOOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "18446744073709551616") == "IOOOOOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999999999") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999999999") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "61440") == "FOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "61440") == "FOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "9223372036854775807") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9223372036854775807") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "340282366920938463463374607431768211456") == "IOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "340282366920938463463374607431768211456") == "IOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "1311768467294897") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1311768467294897") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1267650600228229401496703205375") == "FFFFFFFFFFFFFFFFFFFFFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1267650600228229401496703205375") == "FFFFFFFFFFFFFFFFFFFFFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "493428704") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "493428704") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "1125899906842624") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1125899906842624") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "4611686018427387903") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4611686018427387903") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "18446744073709551614") == "FFFFFFFFFFFFFFFE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "18446744073709551614") == "FFFFFFFFFFFFFFFE": {e}')
    
    total += 1
    try:
        result = candidate(num = "281474976710656") == "IOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "281474976710656") == "IOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "6700417") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6700417") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "4503599627370496") == "IOOOOOOOOOOOOO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4503599627370496") == "IOOOOOOOOOOOOO": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789012") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789012") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "70368744177664") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "70368744177664") == "ERROR": {e}')
    
    total += 1
    try:
        result = candidate(num = "16777215") == "FFFFFF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "16777215") == "FFFFFF": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000") == "ERROR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000") == "ERROR": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = "2718281828459045") == "ERROR"
    assert candidate(num = "1234567890") == "ERROR"
    assert candidate(num = "1234567890123456789") == "ERROR"
    assert candidate(num = "257") == "IOI"
    assert candidate(num = "3") == "ERROR"
    assert candidate(num = "123456789") == "ERROR"
    assert candidate(num = "1") == "I"
    assert candidate(num = "4095") == "FFF"
    assert candidate(num = "16") == "IO"
    assert candidate(num = "43981") == "ABCD"
    assert candidate(num = "1000000000000") == "ERROR"
    assert candidate(num = "4294967295") == "FFFFFFFF"
    assert candidate(num = "1048575") == "FFFFF"
    assert candidate(num = "131072") == "ERROR"
    assert candidate(num = "94906265") == "ERROR"
    assert candidate(num = "11259375") == "ABCDEF"
    assert candidate(num = "1234567890123456789012345678901") == "ERROR"
    assert candidate(num = "18014398509481984") == "ERROR"
    assert candidate(num = "67891011") == "ERROR"
    assert candidate(num = "65535") == "FFFF"
    assert candidate(num = "1152921504606846976") == "IOOOOOOOOOOOOOOO"
    assert candidate(num = "274877906944") == "ERROR"
    assert candidate(num = "3074457345618258604861706883955240992") == "ERROR"
    assert candidate(num = "549755813888") == "ERROR"
    assert candidate(num = "14615016373309029182036848327646332848676852880698050517756256000000000000000") == "ERROR"
    assert candidate(num = "3489163") == "ERROR"
    assert candidate(num = "11") == "B"
    assert candidate(num = "10") == "A"
    assert candidate(num = "1111111111") == "ERROR"
    assert candidate(num = "12345678901234567") == "ERROR"
    assert candidate(num = "68719476735") == "FFFFFFFFF"
    assert candidate(num = "17592186044416") == "IOOOOOOOOOOO"
    assert candidate(num = "1048576") == "IOOOOO"
    assert candidate(num = "999999999999") == "ERROR"
    assert candidate(num = "35184372088832") == "ERROR"
    assert candidate(num = "888888888888") == "ERROR"
    assert candidate(num = "16777216") == "IOOOOOO"
    assert candidate(num = "4398046511104") == "ERROR"
    assert candidate(num = "67000000000000000000") == "ERROR"
    assert candidate(num = "36893488147419103232") == "ERROR"
    assert candidate(num = "1111111111111") == "ERROR"
    assert candidate(num = "111111111111") == "ERROR"
    assert candidate(num = "72057594037927935") == "FFFFFFFFFFFFFF"
    assert candidate(num = "1234567890123") == "ERROR"
    assert candidate(num = "4096") == "IOOO"
    assert candidate(num = "271828182845904523536028747135266249775724709369999") == "ERROR"
    assert candidate(num = "281474976710655") == "FFFFFFFFFFFF"
    assert candidate(num = "211106232532973781056") == "ERROR"
    assert candidate(num = "2199023255551") == "IFFFFFFFFFF"
    assert candidate(num = "72057594037927936") == "IOOOOOOOOOOOOOO"
    assert candidate(num = "15") == "F"
    assert candidate(num = "32768") == "ERROR"
    assert candidate(num = "144115188075855872") == "ERROR"
    assert candidate(num = "100000000000") == "ERROR"
    assert candidate(num = "9007199254740991") == "IFFFFFFFFFFFFF"
    assert candidate(num = "67890") == "ERROR"
    assert candidate(num = "79228162514264337593543950336") == "IOOOOOOOOOOOOOOOOOOOOOOOO"
    assert candidate(num = "18446744073709551615") == "FFFFFFFFFFFFFFFF"
    assert candidate(num = "2199023255552") == "ERROR"
    assert candidate(num = "288230376151711744") == "ERROR"
    assert candidate(num = "777") == "ERROR"
    assert candidate(num = "678230456789123456789") == "ERROR"
    assert candidate(num = "1000000000001") == "ERROR"
    assert candidate(num = "43690") == "AAAA"
    assert candidate(num = "134217728") == "ERROR"
    assert candidate(num = "2147483647") == "ERROR"
    assert candidate(num = "57896044618658097711785492504343953926634992332820282019728792003956564819949") == "ERROR"
    assert candidate(num = "1000000000") == "ERROR"
    assert candidate(num = "18446744073709551616") == "IOOOOOOOOOOOOOOOO"
    assert candidate(num = "9999999999999") == "ERROR"
    assert candidate(num = "61440") == "FOOO"
    assert candidate(num = "9223372036854775807") == "ERROR"
    assert candidate(num = "340282366920938463463374607431768211456") == "IOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    assert candidate(num = "1311768467294897") == "ERROR"
    assert candidate(num = "1267650600228229401496703205375") == "FFFFFFFFFFFFFFFFFFFFFFFFF"
    assert candidate(num = "987654321") == "ERROR"
    assert candidate(num = "493428704") == "ERROR"
    assert candidate(num = "1125899906842624") == "ERROR"
    assert candidate(num = "4611686018427387903") == "ERROR"
    assert candidate(num = "18446744073709551614") == "FFFFFFFFFFFFFFFE"
    assert candidate(num = "281474976710656") == "IOOOOOOOOOOOO"
    assert candidate(num = "6700417") == "ERROR"
    assert candidate(num = "4503599627370496") == "IOOOOOOOOOOOOO"
    assert candidate(num = "123456789012") == "ERROR"
    assert candidate(num = "70368744177664") == "ERROR"
    assert candidate(num = "16777215") == "FFFFFF"
    assert candidate(num = "1000000") == "ERROR"


