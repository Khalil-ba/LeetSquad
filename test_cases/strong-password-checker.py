def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(password = "AAAbbb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "........##@") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "........##@") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aaaaaa1A") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aaaaaa1A") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "Passwo0rd!!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Passwo0rd!!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1b2C3") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1b2C3") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "...!!!") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "...!!!") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1b2C3d4E5f6G7") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1b2C3d4E5f6G7") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "111111111111111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "111111111111111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1B2C3D4E5F6G7H8I9J0") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1B2C3D4E5F6G7H8I9J0") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890!@#$%^") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890!@#$%^") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!Aa1!Aa1!Aa1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!Aa1!Aa1!Aa1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1111111111111111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1111111111111111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1A1A1A1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1A1A1A1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "password") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "password") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAAAaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAAAaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890Aa1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890Aa1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaAaAaAaAaAaAaAaAaAa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaAaAaAaAaAaAaAaAaAa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaa111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaa111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1B2C3D4E5F6G7H8I9J0K") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1B2C3D4E5F6G7H8I9J0K") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890123456") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890123456") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1b2C3d4") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1b2C3d4") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "12345678901234567890") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "12345678901234567890") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "!@#$%^&*()_+") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!@#$%^&*()_+") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aaa111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aaa111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "a") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "a") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890Aa1234567890") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890Aa1234567890") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaAaAaAaAaAaAaAaAaA1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaAaAaAaAaAaAaAaAaA1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aaaaaa1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aaaaaa1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "............aaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "............aaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890!@#$%^&*()") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890!@#$%^&*()") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890Aa123456") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890Aa123456") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "11111111111111111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "11111111111111111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "1337C0d3") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "1337C0d3") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Password123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Password123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaaaaaaaaaaaaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaaaaaaaaaaaaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa123456") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa123456") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "ABABABABABABABABAB") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "ABABABABABABABABAB") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "ABABABABABABABABABAB1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "ABABABABABABABABABAB1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890Aa123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890Aa123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaaaaaaaa1A") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaaaaaaaa1A") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC123!@#") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC123!@#") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1b2C3D4E5F6G7H8I9J0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1b2C3D4E5F6G7H8I9J0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbccc111111111111111111") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbccc111111111111111111") == 11: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd1111111111111111111") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd1111111111111111111") == 15: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaabbbbccccddddeee") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaabbbbccccddddeee") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "111222333444555666777888999000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "111222333444555666777888999000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC123!!!123!!!123!!!123!!!") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC123!!!123!!!123!!!123!!!") == 10: {e}')
    
    total += 1
    try:
        result = candidate(password = "P@ssw0rd!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "P@ssw0rd!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "!@#$%^&*()_+~`|}{[]:;?><,./-=!@#$%^&*()") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!@#$%^&*()_+~`|}{[]:;?><,./-=!@#$%^&*()") == 22: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaBbCc1234567890123456789012345678901234567890") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaBbCc1234567890123456789012345678901234567890") == 26: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd11111111111111111111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd11111111111111111111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1A1A1A1A1A1A1A1A1A1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1A1A1A1A1A1A1A1A1A1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aaaaaaaaaa1111111111!!!!!!!!!") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aaaaaaaaaa1111111111!!!!!!!!!") == 14: {e}')
    
    total += 1
    try:
        result = candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 15: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcdefgH1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcdefgH1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "123456789012345678901234567890") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "123456789012345678901234567890") == 12: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaAAAAAA1111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaAAAAAA1111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 28: {e}')
    
    total += 1
    try:
        result = candidate(password = "Password123Password123") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Password123Password123") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC123!@#abcABC123!@#abcABC123!@#") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC123!@#abcABC123!@#abcABC123!@#") == 16: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 56: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1") == 28: {e}')
    
    total += 1
    try:
        result = candidate(password = "!@#$%^&*()_+~`|}{[]:;?><,./-=") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!@#$%^&*()_+~`|}{[]:;?><,./-=") == 12: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd1111111111111111111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd1111111111111111111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcdefghijklmnopqrstuvwxyz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcdefghijklmnopqrstuvwxyz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == 19: {e}')
    
    total += 1
    try:
        result = candidate(password = "xX1234567890Xx1234567890Xx1234567890") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "xX1234567890Xx1234567890Xx1234567890") == 16: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Bb2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0KkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Bb2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0KkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 42: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1") == 23: {e}')
    
    total += 1
    try:
        result = candidate(password = "aabababababababababa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aabababababababababa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa123456789012345") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa123456789012345") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Password!Password!Pass") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Password!Password!Pass") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!a") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!a") == 8: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 11: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaaaaaaaaaaaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaaaaaaaaaaaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "1234567890!@#$%^&*()_+~`|}{[]:;?><,./-=") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "1234567890!@#$%^&*()_+~`|}{[]:;?><,./-=") == 21: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A1") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A1") == 7: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z1") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z1") == 33: {e}')
    
    total += 1
    try:
        result = candidate(password = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 40: {e}')
    
    total += 1
    try:
        result = candidate(password = "bbbbbbbbbbbbbbbbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "bbbbbbbbbbbbbbbbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 20: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!a") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!a") == 12: {e}')
    
    total += 1
    try:
        result = candidate(password = "!aA1!aA1!aA1!aA1!aA1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!aA1!aA1!aA1!aA1!aA1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaaBBB111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaaBBB111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!") == 44: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1A1A1A1A1A1A1A1A1A1A1") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1A1A1A1A1A1A1A1A1A1A1") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd11111111111111111111111") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd11111111111111111111111") == 19: {e}')
    
    total += 1
    try:
        result = candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaA") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaA") == 7: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaAAaaAAaaAAaaAAaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaAAaaAAaaAAaaAAaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa!b@c#d$e%f^g&h*i(j)k") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa!b@c#d$e%f^g&h*i(j)k") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1") == 23: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!Aa1!Aa1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!Aa1!Aa1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1A") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1A") == 23: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1!aA1!aA1!aA1!aA1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1!aA1!aA1!aA1!aA1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "abAB1111111111111111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abAB1111111111111111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "cccccccccccccccccccccccccccccccccccccccccccccccccccc") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "cccccccccccccccccccccccccccccccccccccccccccccccccccc") == 38: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaAAAAAA666666") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaAAAAAA666666") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaAAA111!!!") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaAAA111!!!") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaA") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaA") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa111111111111111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa111111111111111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "a!b@c#d$e%f^g&h*i(j)") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "a!b@c#d$e%f^g&h*i(j)") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaAA111111111111111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaAA111111111111111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1") == 10: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC123abcABC123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC123abcABC123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 28: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC123!@#abcABC123!@#") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC123!@#abcABC123!@#") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Bb2Ccc3Ddd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Bb2Ccc3Ddd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCccc111111111") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCccc111111111") == 7: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC!@#abcABC!@#abcABC!@#") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC!@#abcABC!@#abcABC!@#") == 8: {e}')
    
    total += 1
    try:
        result = candidate(password = "Abcde!23456789") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Abcde!23456789") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 9: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd111111111111111111111111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd111111111111111111111111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaabbbccc111222333") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaabbbccc111222333") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1bB2cC3dD4eE5fF6") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1bB2cC3dD4eE5fF6") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaAAAAAA6666666") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaAAAAAA6666666") == 6: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 40: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa!b@c#d$e%f^g&h*i(j)") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa!b@c#d$e%f^g&h*i(j)") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcABC123abcABC123abcABC123") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcABC123abcABC123abcABC123") == 7: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1234567890123456789") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1234567890123456789") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "!@#$%^&*()") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!@#$%^&*()") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "!@#$%^&*()_+~`1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!@#$%^&*()_+~`1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") == 56: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1!aA1!aA1!aA1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1!aA1!aA1!aA1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1aA1aA1aA1aA1aA1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1aA1aA1aA1aA1aA1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "111222333444555666777888999000111222333") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "111222333444555666777888999000111222333") == 21: {e}')
    
    total += 1
    try:
        result = candidate(password = "123!@#abcDEF") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "123!@#abcDEF") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1") == 22: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Abc!1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Abc!1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaAAAbBBB11111111111111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaAAAbBBB11111111111111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaaBBBcccDDD123") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaaBBBcccDDD123") == 3: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbccccdddEEF1234567890") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbccccdddEEF1234567890") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA111aA111aA111aA111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA111aA111aA111aA111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaAAAAAA66666666666666666666") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaAAAAAA66666666666666666666") == 18: {e}')
    
    total += 1
    try:
        result = candidate(password = "0123456789012345678901234567890") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "0123456789012345678901234567890") == 13: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1!aA1!aA1!aA1!aA1!aA1!") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1!aA1!aA1!aA1!aA1!aA1!") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1b2C3d4E5f6G7H8I9J0KLMN") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1b2C3d4E5f6G7H8I9J0KLMN") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "aA1234567890Aa1234567890aA1234567890") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aA1234567890Aa1234567890aA1234567890") == 16: {e}')
    
    total += 1
    try:
        result = candidate(password = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 42: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcdefghijABCD1234567890") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcdefghijABCD1234567890") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 32: {e}')
    
    total += 1
    try:
        result = candidate(password = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 12: {e}')
    
    total += 1
    try:
        result = candidate(password = "1234567890!@#$%^&*()_+") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "1234567890!@#$%^&*()_+") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd111111111111111111") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd111111111111111111") == 14: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 31: {e}')
    
    total += 1
    try:
        result = candidate(password = "123!@#abcDEF123!@#abcDEF") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "123!@#abcDEF123!@#abcDEF") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 13: {e}')
    
    total += 1
    try:
        result = candidate(password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 8: {e}')
    
    total += 1
    try:
        result = candidate(password = "AAAbbbCCCddd111111111111111111111") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "AAAbbbCCCddd111111111111111111111") == 17: {e}')
    
    total += 1
    try:
        result = candidate(password = "abcdefgHIJKLmnopQR1234567890!@#$%^&*()") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "abcdefgHIJKLmnopQR1234567890!@#$%^&*()") == 18: {e}')
    
    total += 1
    try:
        result = candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA") == 9: {e}')
    
    total += 1
    try:
        result = candidate(password = "a!B@c#D$e%F^G&H*I(J)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "a!B@c#D$e%F^G&H*I(J)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()") == 53: {e}')
    
    total += 1
    try:
        result = candidate(password = "xXyYzZ0987654321@#") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "xXyYzZ0987654321@#") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Password1Password1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Password1Password1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1aA1aA1aA1aA1aA1aA1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1aA1aA1aA1aA1aA1aA1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa12345678901234567890") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa12345678901234567890") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 46: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaAaaaAaaaAaaaAaaaAaaaA") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaAaaaAaaaAaaaAaaaAaaaA") == 5: {e}')
    
    total += 1
    try:
        result = candidate(password = "00000000000000000000000000000000") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "00000000000000000000000000000000") == 18: {e}')
    
    total += 1
    try:
        result = candidate(password = "aaaaaaaaaAAA9") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aaaaaaaaaAAA9") == 4: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aaaaabbbb1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aaaaabbbb1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(password = "111222333444555666777888999000111222333444555666777888999000") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "111222333444555666777888999000111222333444555666777888999000") == 42: {e}')
    
    total += 1
    try:
        result = candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 11: {e}')
    
    total += 1
    try:
        result = candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 16: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(password = "AAAbbb") == 2
    assert candidate(password = "aA1") == 3
    assert candidate(password = "Aa1234567890") == 0
    assert candidate(password = "........##@") == 3
    assert candidate(password = "Aaaaaa1A") == 1
    assert candidate(password = "Passwo0rd!!") == 0
    assert candidate(password = "A1b2C3") == 0
    assert candidate(password = "...!!!") == 3
    assert candidate(password = "A1b2C3d4E5f6G7") == 0
    assert candidate(password = "111111111111111111") == 6
    assert candidate(password = "A1B2C3D4E5F6G7H8I9J0") == 1
    assert candidate(password = "Aa1234567890!@#$%^") == 0
    assert candidate(password = "Aa1!Aa1!Aa1!Aa1!") == 0
    assert candidate(password = "Aa1111111111111111") == 5
    assert candidate(password = "A1A1A1A1") == 1
    assert candidate(password = "password") == 2
    assert candidate(password = "Aaaaaa") == 1
    assert candidate(password = "AAAAAaaaaaaa") == 3
    assert candidate(password = "Aa1234567890Aa1") == 0
    assert candidate(password = "Aa111") == 1
    assert candidate(password = "AaAaAaAaAaAaAaAaAaAa") == 1
    assert candidate(password = "aaa111") == 2
    assert candidate(password = "A1B2C3D4E5F6G7H8I9J0K") == 2
    assert candidate(password = "Aa1234567890123456") == 0
    assert candidate(password = "A1b2C3d4") == 0
    assert candidate(password = "12345678901234567890") == 2
    assert candidate(password = "aaaaaaa") == 2
    assert candidate(password = "Aa1234567890123") == 0
    assert candidate(password = "!@#$%^&*()_+") == 3
    assert candidate(password = "Aaa111") == 1
    assert candidate(password = "a") == 5
    assert candidate(password = "Aa1234567890Aa1234567890") == 4
    assert candidate(password = "AaAaAaAaAaAaAaAaAaA1") == 0
    assert candidate(password = "Aaaaaa1") == 1
    assert candidate(password = "............aaa") == 5
    assert candidate(password = "Aa1234567890!@#$%^&*()") == 2
    assert candidate(password = "Aa1234567890Aa123456") == 0
    assert candidate(password = "11111111111111111111") == 6
    assert candidate(password = "1337C0d3") == 0
    assert candidate(password = "Password123") == 0
    assert candidate(password = "aaaaaaaaaaaaaaaaaaaaa") == 7
    assert candidate(password = "Aa123456") == 0
    assert candidate(password = "ABABABABABABABABAB") == 2
    assert candidate(password = "ABABABABABABABABABAB1") == 2
    assert candidate(password = "Aa1234567890Aa123") == 0
    assert candidate(password = "aaaaaaaaaaaaaa1A") == 4
    assert candidate(password = "abcABC123!@#") == 0
    assert candidate(password = "A1b2C3D4E5F6G7H8I9J0") == 0
    assert candidate(password = "AAAbbbccc111111111111111111") == 11
    assert candidate(password = "AAAbbbCCCddd1111111111111111111") == 15
    assert candidate(password = "aaaabbbbccccddddeee") == 5
    assert candidate(password = "111222333444555666777888999000") == 12
    assert candidate(password = "abcABC123!!!123!!!123!!!123!!!") == 10
    assert candidate(password = "P@ssw0rd!") == 0
    assert candidate(password = "!@#$%^&*()_+~`|}{[]:;?><,./-=!@#$%^&*()") == 22
    assert candidate(password = "AaBbCc1234567890123456789012345678901234567890") == 26
    assert candidate(password = "AAAbbbCCCddd11111111111111111111") == 16
    assert candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 1
    assert candidate(password = "A1A1A1A1A1A1A1A1A1A1") == 1
    assert candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A") == 6
    assert candidate(password = "Aaaaaaaaaa1111111111!!!!!!!!!") == 14
    assert candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 15
    assert candidate(password = "abcdefgH1!") == 0
    assert candidate(password = "123456789012345678901234567890") == 12
    assert candidate(password = "aaaaaaaAAAAAA1111111") == 6
    assert candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 28
    assert candidate(password = "Password123Password123") == 2
    assert candidate(password = "abcABC123!@#abcABC123!@#abcABC123!@#") == 16
    assert candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 56
    assert candidate(password = "aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1") == 28
    assert candidate(password = "!@#$%^&*()_+~`|}{[]:;?><,./-=") == 12
    assert candidate(password = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 55
    assert candidate(password = "AAAbbbCCCddd1111111111111111111111") == 18
    assert candidate(password = "abcdefghijklmnopqrstuvwxyz") == 8
    assert candidate(password = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == 19
    assert candidate(password = "xX1234567890Xx1234567890Xx1234567890") == 16
    assert candidate(password = "Aa1Bb2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0KkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 42
    assert candidate(password = "aA1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1") == 23
    assert candidate(password = "aabababababababababa") == 2
    assert candidate(password = "Aa123456789012345") == 0
    assert candidate(password = "Password!Password!Pass") == 3
    assert candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!a") == 8
    assert candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 11
    assert candidate(password = "aaaaaaaaaaaaaaaaaaaa") == 6
    assert candidate(password = "1234567890!@#$%^&*()_+~`|}{[]:;?><,./-=") == 21
    assert candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A1") == 7
    assert candidate(password = "A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z1") == 33
    assert candidate(password = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 40
    assert candidate(password = "bbbbbbbbbbbbbbbbb") == 5
    assert candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 20
    assert candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!a") == 12
    assert candidate(password = "!aA1!aA1!aA1!aA1!aA1") == 0
    assert candidate(password = "AaaBBB111") == 2
    assert candidate(password = "Aa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!aAa!") == 44
    assert candidate(password = "A1A1A1A1A1A1A1A1A1A1A1") == 3
    assert candidate(password = "AAAbbbCCCddd11111111111111111111111") == 19
    assert candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaA") == 7
    assert candidate(password = "aaAAaaAAaaAAaaAAaa") == 1
    assert candidate(password = "Aa!b@c#d$e%f^g&h*i(j)k") == 3
    assert candidate(password = "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1") == 23
    assert candidate(password = "Aa1!Aa1!Aa1!") == 0
    assert candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1A") == 23
    assert candidate(password = "aA1!aA1!aA1!aA1!aA1!") == 0
    assert candidate(password = "abAB1111111111111111") == 5
    assert candidate(password = "cccccccccccccccccccccccccccccccccccccccccccccccccccc") == 38
    assert candidate(password = "aaaaaaaAAAAAA666666") == 6
    assert candidate(password = "aaaAAA111!!!") == 4
    assert candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaA") == 5
    assert candidate(password = "Aa111111111111111111") == 6
    assert candidate(password = "a!b@c#d$e%f^g&h*i(j)") == 2
    assert candidate(password = "aaAA111111111111111") == 5
    assert candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA1") == 10
    assert candidate(password = "abcABC123abcABC123") == 0
    assert candidate(password = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 28
    assert candidate(password = "abcABC123!@#abcABC123!@#") == 4
    assert candidate(password = "Aa1Bb2Ccc3Ddd") == 0
    assert candidate(password = "AAAbbbCCCccc111111111") == 7
    assert candidate(password = "abcABC!@#abcABC!@#abcABC!@#") == 8
    assert candidate(password = "Abcde!23456789") == 0
    assert candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 9
    assert candidate(password = "AAAbbbCCCddd111111111111111111111111") == 20
    assert candidate(password = "aaabbbccc111222333") == 6
    assert candidate(password = "aA1bB2cC3dD4eE5fF6") == 0
    assert candidate(password = "aaaaaaaAAAAAA6666666") == 6
    assert candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 40
    assert candidate(password = "Aa!b@c#d$e%f^g&h*i(j)") == 2
    assert candidate(password = "abcABC123abcABC123abcABC123") == 7
    assert candidate(password = "Aa1234567890123456789") == 1
    assert candidate(password = "!@#$%^&*()") == 3
    assert candidate(password = "!@#$%^&*()_+~`1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") == 56
    assert candidate(password = "aA1!aA1!aA1!aA1!") == 0
    assert candidate(password = "aA1aA1aA1aA1aA1aA1") == 0
    assert candidate(password = "111222333444555666777888999000111222333") == 21
    assert candidate(password = "123!@#abcDEF") == 0
    assert candidate(password = "aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1aA1") == 22
    assert candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1") == 0
    assert candidate(password = "Abc!1") == 1
    assert candidate(password = "aaaAAAbBBB11111111111111") == 8
    assert candidate(password = "AaaBBBcccDDD123") == 3
    assert candidate(password = "AAAbbccccdddEEF1234567890") == 5
    assert candidate(password = "aA111aA111aA111aA111") == 4
    assert candidate(password = "aaaaaaaAAAAAA66666666666666666666") == 18
    assert candidate(password = "0123456789012345678901234567890") == 13
    assert candidate(password = "aA1!aA1!aA1!aA1!aA1!aA1!") == 4
    assert candidate(password = "A1b2C3d4E5f6G7H8I9J0KLMN") == 4
    assert candidate(password = "aA1234567890Aa1234567890aA1234567890") == 16
    assert candidate(password = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 42
    assert candidate(password = "abcdefghijABCD1234567890") == 4
    assert candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 32
    assert candidate(password = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 15
    assert candidate(password = "Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!") == 12
    assert candidate(password = "1234567890!@#$%^&*()_+") == 4
    assert candidate(password = "AAAbbbCCCddd111111111111111111") == 14
    assert candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 31
    assert candidate(password = "123!@#abcDEF123!@#abcDEF") == 4
    assert candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 13
    assert candidate(password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 8
    assert candidate(password = "AAAbbbCCCddd111111111111111111111") == 17
    assert candidate(password = "abcdefgHIJKLmnopQR1234567890!@#$%^&*()") == 18
    assert candidate(password = "A1!aA1!aA1!aA1!aA1!aA1!aA1!aA") == 9
    assert candidate(password = "a!B@c#D$e%F^G&H*I(J)") == 1
    assert candidate(password = "!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()") == 53
    assert candidate(password = "xXyYzZ0987654321@#") == 0
    assert candidate(password = "Password1Password1") == 0
    assert candidate(password = "Aa1aA1aA1aA1aA1aA1aA1") == 1
    assert candidate(password = "Aa12345678901234567890") == 2
    assert candidate(password = "Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1Aa1") == 46
    assert candidate(password = "aaAaaaAaaaAaaaAaaaAaaaA") == 5
    assert candidate(password = "00000000000000000000000000000000") == 18
    assert candidate(password = "aaaaaaaaaAAA9") == 4
    assert candidate(password = "Aaaaabbbb1") == 2
    assert candidate(password = "111222333444555666777888999000111222333444555666777888999000") == 42
    assert candidate(password = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 11
    assert candidate(password = "Aa1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!aA1!") == 16


