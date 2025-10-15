def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "ghijkl") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ghijkl") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "npqrstvwxy") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "npqrstvwxy") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghi") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghi") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopq") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopq") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrs") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrs") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstu") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstu") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstu") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstu") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkl") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkl") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijk") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijk") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvw") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvw") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghi") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghi") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklm") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklm") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "efghijkl") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "efghijkl") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmn") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmn") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvw") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvw") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "uvwxyza") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uvwxyza") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdefg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdefg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "tuvwxy") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tuvwxy") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuv") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuv") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "tuvwxyz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tuvwxyz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "wxyzabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wxyzabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrs") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrs") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrst") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrst") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "xycdefghij") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xycdefghij") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "hijklmno") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hijklmno") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstu") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstu") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyza") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyza") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqr") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqr") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnopqrstuvwxyzabc") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnopqrstuvwxyzabc") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "rstvwxy") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rstvwxy") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdef") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdef") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnop") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnop") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "klmnopq") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "klmnopq") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "stuvwx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "stuvwx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnop") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnop") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijlkmnopqrstuvwxyz") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijlkmnopqrstuvwxyz") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "yz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "lmnopqrs") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lmnopqrs") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "ab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "ijklmn") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ijklmn") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "klmnop") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "klmnop") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqr") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqr") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ghijklm") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ghijklm") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "ijklmnop") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ijklmnop") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcde") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcde") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrst") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrst") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "opqrstuv") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "opqrstuv") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "hijklm") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hijklm") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuv") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuv") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnopqrstuvwx") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnopqrstuvwx") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghij") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghij") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "efghij") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "efghij") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyz") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyz") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzabcdef") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzabcdef") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghijkl") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghijkl") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "jklmno") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jklmno") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgh") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgh") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdfghjkl") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdfghjkl") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdefghijklmnopqrstuvwxyzafe") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdefghijklmnopqrstuvwxyzafe") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwx") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwx") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "stuvwxyzabcdefghij") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "stuvwxyzabcdefghij") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "wxyzabcdefghijklmnopqrstuv") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wxyzabcdefghijklmnopqrstuv") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzmnopqrstuabc") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzmnopqrstuabc") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "stuvwxyzabcdefghijkl") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "stuvwxyzabcdefghijkl") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyzabcdefghij") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyzabcdefghij") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabcdefghijk") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabcdefghijk") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "lmnopqrstuvwxyzabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lmnopqrstuvwxyzabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "opqrstuvwxyzabcde") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "opqrstuvwxyzabcde") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "uvwxyzabcdefghijklmnopqrstuvwxy") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uvwxyzabcdefghijklmnopqrstuvwxy") == 76: {e}')
    
    total += 1
    try:
        result = candidate(word = "lmnopqrstuvwxyzabcdefghijk") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lmnopqrstuvwxyzabcdefghijk") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "zxcvbnmlkjhgfedcba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zxcvbnmlkjhgfedcba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabcdefghijklmnop") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabcdefghijklmnop") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyzzzzz") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyzzzzz") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijlmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijlmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "jklmnopqrstuvwx") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jklmnopqrstuvwx") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "klmnopqrstuvwxyzabcdefghij") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "klmnopqrstuvwxyzabcdefghij") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "zxcvbnmlkjhgfdsapoiuytrewq") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zxcvbnmlkjhgfdsapoiuytrewq") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabcdefghijklmno") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabcdefghijklmno") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "opqrstuvwxyzabcdefghijklmnop") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "opqrstuvwxyzabcdefghijklmnop") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabcdefghijklm") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabcdefghijklm") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxy") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxy") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "efghijklmnop") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "efghijklmnop") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzabcdefghijklmnopqrstuvwx") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzabcdefghijklmnopqrstuvwx") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "tuvxyzabcdefghijklmnopqrs") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tuvxyzabcdefghijklmnopqrs") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxzyabc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxzyabc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "lmnopqrstu") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lmnopqrstu") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "bdfhjlnprtvxz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bdfhjlnprtvxz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyzabc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyzabc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrst") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrst") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxzy") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxzy") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdpqrs") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdpqrs") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxzy") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxzy") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiou") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiou") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabcdefghijklmnopqrstuvwx") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabcdefghijklmnopqrstuvwx") == 60: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgxyz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgxyz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghijklmnopqrstuvwxyzabc") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghijklmnopqrstuvwxyzabc") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "klmnopqrstuabcdefghij") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "klmnopqrstuabcdefghij") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnop") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnop") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgxyzijklmnop") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgxyzijklmnop") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "stuvxyzabcdefghijklmnopqr") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "stuvxyzabcdefghijklmnopqr") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "ghijklmnopqrstuvwxyzabcde") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ghijklmnopqrstuvwxyzabcde") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxcvbnm") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxcvbnm") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabcdefghijkl") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabcdefghijkl") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghjklmno") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghjklmno") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "hijklmnopqrstuvwxyz") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hijklmnopqrstuvwxyz") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyzabcd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyzabcd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwlmnoefghij") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwlmnoefghij") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzabcdefghijklmnopqrstuvwxy") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzabcdefghijklmnopqrstuvwxy") == 60: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdefghijklmnopq") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdefghijklmnopq") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghijklmnopqrstuvwxyza") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghijklmnopqrstuvwxyza") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "opqrstuvwxyzabcdefghijklmn") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "opqrstuvwxyzabcdefghijklmn") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyzabcdefghijxyz") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyzabcdefghijxyz") == 60: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyzaefghijkl") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyzaefghijkl") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "wxyzabcdefghijklmnopqrstuvwxy") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wxyzabcdefghijklmnopqrstuvwxy") == 68: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijmnopqrstuvwxyz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijmnopqrstuvwxyz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdefghijklmnopqrstuvwxyza") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdefghijklmnopqrstuvwxyza") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "poiuytrewq") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "poiuytrewq") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdfghjklmnpqrstvwxyz") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdfghjklmnpqrstvwxyz") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiop") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiop") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefhijklmno") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefhijklmno") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "uvwxyzaeiou") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uvwxyzaeiou") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghilmnopqrstuvwxyz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghilmnopqrstuvwxyz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijxyzklmnopqr") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijxyzklmnopqr") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzdefghijklmnopqrstuvw") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzdefghijklmnopqrstuvw") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnopqrst") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnopqrst") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "wxyzabcdefghijklmnopqrst") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wxyzabcdefghijklmnopqrst") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "tuvwxyzabcdefghijklmnopqrs") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tuvwxyzabcdefghijklmnopqrs") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyzabcdefghijklmnop") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyzabcdefghijklmnop") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "ghijklmnopqrstuvwxyzab") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ghijklmnopqrstuvwxyzab") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghiklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghiklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ghijklmnopqrstu") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ghijklmnopqrstu") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyzabcdefghijklmnopqrstu") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyzabcdefghijklmnopqrstu") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyzabcdefghijklmnopq") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyzabcdefghijklmnopq") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdefghijklmnop") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdefghijklmnop") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "ijklmnopqrstuvwxyzabcdefgh") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ijklmnopqrstuvwxyzabcdefgh") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjihgfedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjihgfedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "klmno") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "klmno") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxyzabcdefghijklmno") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxyzabcdefghijklmno") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "stuvwxyzabcdefghijklmnopqr") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "stuvwxyzabcdefghijklmnopqr") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg hijklmnop qrstuv wxyz") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg hijklmnop qrstuv wxyz") == 68: {e}')
    
    total += 1
    try:
        result = candidate(word = "lmnopqrstuvwxyz") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lmnopqrstuvwxyz") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "rstuvxyzabcdefghijklmnopqrst") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rstuvxyzabcdefghijklmnopqrst") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyza") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyza") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghilmnopqr") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghilmnopqr") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzabcdefghijklmnopqrstuvw") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzabcdefghijklmnopqrstuvw") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabcdefghijklmnopq") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabcdefghijklmnopq") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdefghijklmnopqrstuvwx") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdefghijklmnopqrstuvwx") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvmnop") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvmnop") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "zxcvbnm") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zxcvbnm") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabcdefghijklmnopqrstuvw") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabcdefghijklmnopqrstuvw") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyzabcdefg") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyzabcdefg") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnopqrstuvwxy") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnopqrstuvwxy") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghilmnopqrstuvwxyzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghilmnopqrstuvwxyzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghijklmnopqrstu") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghijklmnopqrstu") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyzabcdefghijklmno") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyzabcdefghijklmno") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "vwxyzabcdefghijklmnopqrstuvwx") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vwxyzabcdefghijklmnopqrstuvwx") == 68: {e}')
    
    total += 1
    try:
        result = candidate(word = "zxcvbnmasdfghjklqwertyuiop") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zxcvbnmasdfghjklqwertyuiop") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuv") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuv") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdefghijklmnopqrstuvwxy") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdefghijklmnopqrstuvwxy") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "defghijklmnopqrstuabcdefgh") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "defghijklmnopqrstuabcdefgh") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "asdfghjkl") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "asdfghjkl") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmno") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmno") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "ghijklmnopqrstuvwxyzabcdef") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ghijklmnopqrstuvwxyzabcdef") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzabcdefghijklmnop") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzabcdefghijklmnop") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyzabcdefghijklmnoprstuvw") == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyzabcdefghijklmnoprstuvw") == 80: {e}')
    
    total += 1
    try:
        result = candidate(word = "rstuvwxyzabcdefghijklmnopq") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rstuvwxyzabcdefghijklmnopq") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdefghijklmnopqrstuvwx") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdefghijklmnopqrstuvwx") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabcd") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabcd") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdefghijkl") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdefghijkl") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "nopqrstuvwxyzabcde") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nopqrstuvwxyzabcde") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefhijklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefhijklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnopqrstuv") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnopqrstuv") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "tuvwx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tuvwx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxyzabcdef") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxyzabcdef") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "jklmnopqrst") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jklmnopqrst") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdefghijklmnopqrstvwxyz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdefghijklmnopqrstvwxyz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjhgfdsa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjhgfdsa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxyzabc") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxyzabc") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "jklmnopqr") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jklmnopqr") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "uvwxyzabcdefghijklmnopqrst") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uvwxyzabcdefghijklmnopqrst") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwlmnop") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwlmnop") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "acdegikmoqsuwy") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acdegikmoqsuwy") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxyza") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxyza") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuabcdefghijk") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuabcdefghijk") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwx") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwx") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "hgfedcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hgfedcba") == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "ghijkl") == 6
    assert candidate(word = "npqrstvwxy") == 12
    assert candidate(word = "abcdefghi") == 10
    assert candidate(word = "vwxyz") == 5
    assert candidate(word = "abcdefghijklmnopq") == 27
    assert candidate(word = "abcdefghijklmnopqrs") == 33
    assert candidate(word = "abcdefghijklmnopqrstu") == 39
    assert candidate(word = "pqrstu") == 6
    assert candidate(word = "abcdefghijkl") == 16
    assert candidate(word = "abcdefghijk") == 14
    assert candidate(word = "pqrstuvw") == 8
    assert candidate(word = "defghi") == 6
    assert candidate(word = "abcdefghijklm") == 18
    assert candidate(word = "efghijkl") == 8
    assert candidate(word = "abcdef") == 6
    assert candidate(word = "abcdefghijklmn") == 20
    assert candidate(word = "qrstuvw") == 7
    assert candidate(word = "uvwxyza") == 7
    assert candidate(word = "bcdefg") == 6
    assert candidate(word = "tuvwxy") == 6
    assert candidate(word = "qrstuv") == 6
    assert candidate(word = "tuvwxyz") == 7
    assert candidate(word = "wxyzabc") == 7
    assert candidate(word = "abcdefghij") == 12
    assert candidate(word = "nopqrs") == 6
    assert candidate(word = "nopqrst") == 7
    assert candidate(word = "xycdefghij") == 12
    assert candidate(word = "hijklmno") == 8
    assert candidate(word = "mnopqrstu") == 10
    assert candidate(word = "vwxyza") == 6
    assert candidate(word = "abcdefghijklmnopqr") == 30
    assert candidate(word = "abcdefghijkmnopqrstuvwxyzabc") == 64
    assert candidate(word = "rstvwxy") == 7
    assert candidate(word = "zabcdef") == 7
    assert candidate(word = "abcdefghijklmnop") == 24
    assert candidate(word = "klmnopq") == 7
    assert candidate(word = "stuvwx") == 6
    assert candidate(word = "mnop") == 4
    assert candidate(word = "xyz") == 3
    assert candidate(word = "qrstuvwx") == 8
    assert candidate(word = "abcdefghijlkmnopqrstuvwxyz") == 56
    assert candidate(word = "yz") == 2
    assert candidate(word = "lmnopqrs") == 8
    assert candidate(word = "ab") == 2
    assert candidate(word = "abcde") == 5
    assert candidate(word = "abcd") == 4
    assert candidate(word = "abcdefg") == 7
    assert candidate(word = "a") == 1
    assert candidate(word = "ijklmn") == 6
    assert candidate(word = "klmnop") == 6
    assert candidate(word = "mnopqr") == 6
    assert candidate(word = "ghijklm") == 7
    assert candidate(word = "ijklmnop") == 8
    assert candidate(word = "zabcde") == 6
    assert candidate(word = "abcdefghijklmnopqrst") == 36
    assert candidate(word = "abc") == 3
    assert candidate(word = "opqrstuv") == 8
    assert candidate(word = "hijklm") == 6
    assert candidate(word = "abcdefghijklmnopqrstuv") == 42
    assert candidate(word = "abcdefghijkmnopqrstuvwx") == 45
    assert candidate(word = "defghij") == 7
    assert candidate(word = "efghij") == 6
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 56
    assert candidate(word = "mnopqrstuvwxyz") == 20
    assert candidate(word = "yzabcdef") == 8
    assert candidate(word = "defghijkl") == 10
    assert candidate(word = "jklmno") == 6
    assert candidate(word = "abcdefgh") == 8
    assert candidate(word = "bcdfghjkl") == 10
    assert candidate(word = "bcdefghijklmnopqrstuvwxyzafe") == 64
    assert candidate(word = "abcdefghijklmnopqrstuvwx") == 48
    assert candidate(word = "nopqrstuvwxyz") == 18
    assert candidate(word = "stuvwxyzabcdefghij") == 30
    assert candidate(word = "wxyzabcdefghijklmnopqrstuv") == 56
    assert candidate(word = "xyzmnopqrstuabc") == 22
    assert candidate(word = "stuvwxyzabcdefghijkl") == 36
    assert candidate(word = "qrstuvwxyzabcdefghij") == 36
    assert candidate(word = "nopqrstuvwxyzabcdefghijk") == 48
    assert candidate(word = "lmnopqrstuvwxyzabc") == 30
    assert candidate(word = "opqrstuvwxyzabcde") == 27
    assert candidate(word = "uvwxyzabcdefghijklmnopqrstuvwxy") == 76
    assert candidate(word = "lmnopqrstuvwxyzabcdefghijk") == 56
    assert candidate(word = "zxcvbnmlkjhgfedcba") == 30
    assert candidate(word = "xyzabcdefghijklmnop") == 33
    assert candidate(word = "qrstuvwxyzzzzz") == 20
    assert candidate(word = "abcdefghijlmnopqrstuvwxyz") == 52
    assert candidate(word = "jklmnopqrstuvwx") == 22
    assert candidate(word = "klmnopqrstuvwxyzabcdefghij") == 56
    assert candidate(word = "zxcvbnmlkjhgfdsapoiuytrewq") == 56
    assert candidate(word = "nopqrstuvwxyzabcdefghijklmno") == 64
    assert candidate(word = "opqrstuvwxyzabcdefghijklmnop") == 64
    assert candidate(word = "nopqrstuvwxyzabcdefghijklm") == 56
    assert candidate(word = "pqrstuvwxy") == 12
    assert candidate(word = "efghijklmnop") == 16
    assert candidate(word = "yzabcdefghijklmnopqrstuvwx") == 56
    assert candidate(word = "tuvxyzabcdefghijklmnopqrs") == 52
    assert candidate(word = "mnopqrstuvwxzyabc") == 27
    assert candidate(word = "lmnopqrstu") == 12
    assert candidate(word = "bdfhjlnprtvxz") == 18
    assert candidate(word = "mnopqrstuvwxyzabc") == 27
    assert candidate(word = "mnopqrst") == 8
    assert candidate(word = "mnopqrstuvwxzy") == 20
    assert candidate(word = "abcdpqrs") == 8
    assert candidate(word = "abcdefghijklmnopqrstuvwxzy") == 56
    assert candidate(word = "aeiouaeiou") == 12
    assert candidate(word = "xyzabcdefghijklmnopqrstuvwx") == 60
    assert candidate(word = "abcdefgxyz") == 12
    assert candidate(word = "defghijklmnopqrstuvwxyzabc") == 56
    assert candidate(word = "klmnopqrstuabcdefghij") == 39
    assert candidate(word = "abcdefghijkmnop") == 22
    assert candidate(word = "abcdefgxyzijklmnop") == 30
    assert candidate(word = "stuvxyzabcdefghijklmnopqr") == 52
    assert candidate(word = "ghijklmnopqrstuvwxyzabcde") == 52
    assert candidate(word = "zyxcvbnm") == 8
    assert candidate(word = "nopqrstuvwxyzabcdefghijkl") == 52
    assert candidate(word = "abcdefghjklmno") == 20
    assert candidate(word = "hijklmnopqrstuvwxyz") == 33
    assert candidate(word = "vwxyzabcd") == 10
    assert candidate(word = "pqrstuvwlmnoefghij") == 30
    assert candidate(word = "yzabcdefghijklmnopqrstuvwxy") == 60
    assert candidate(word = "zabcdefghijklmnopq") == 30
    assert candidate(word = "defghijklmnopqrstuvwxyza") == 48
    assert candidate(word = "opqrstuvwxyzabcdefghijklmn") == 56
    assert candidate(word = "mnopqrstuvwxyzabcdefghijxyz") == 60
    assert candidate(word = "mnopqrstuvwxyzaefghijkl") == 45
    assert candidate(word = "wxyzabcdefghijklmnopqrstuvwxy") == 68
    assert candidate(word = "abcdefghijmnopqrstuvwxyz") == 48
    assert candidate(word = "bcdefghijklmnopqrstuvwxyza") == 56
    assert candidate(word = "xyzabc") == 6
    assert candidate(word = "poiuytrewq") == 12
    assert candidate(word = "bcdfghjklmnpqrstvwxyz") == 39
    assert candidate(word = "qwertyuiop") == 12
    assert candidate(word = "abcdefhijklmno") == 20
    assert candidate(word = "qrstuvwxyz") == 12
    assert candidate(word = "uvwxyzaeiou") == 14
    assert candidate(word = "abcdefghilmnopqrstuvwxyz") == 48
    assert candidate(word = "abcdefghijxyzklmnopqr") == 39
    assert candidate(word = "xyzdefghijklmnopqrstuvw") == 45
    assert candidate(word = "abcdefghijkmnopqrst") == 33
    assert candidate(word = "wxyzabcdefghijklmnopqrst") == 48
    assert candidate(word = "tuvwxyzabcdefghijklmnopqrs") == 56
    assert candidate(word = "qrstuvwxyzabcdefghijklmnop") == 56
    assert candidate(word = "ghijklmnopqrstuvwxyzab") == 42
    assert candidate(word = "nopqrstuvwxyzabc") == 24
    assert candidate(word = "abcdefghiklmnopqrstuvwxyz") == 52
    assert candidate(word = "yzabcd") == 6
    assert candidate(word = "ghijklmnopqrstu") == 22
    assert candidate(word = "vwxyzabcdefghijklmnopqrstu") == 56
    assert candidate(word = "vwxyzabcdefghijklmnopq") == 42
    assert candidate(word = "zabcdefghijklmnop") == 27
    assert candidate(word = "ijklmnopqrstuvwxyzabcdefgh") == 56
    assert candidate(word = "lkjihgfedcba") == 16
    assert candidate(word = "klmno") == 5
    assert candidate(word = "pqrstuvwxyzabcdefghijklmno") == 56
    assert candidate(word = "stuvwxyzabcdefghijklmnopqr") == 56
    assert candidate(word = "abcdefg hijklmnop qrstuv wxyz") == 68
    assert candidate(word = "lmnopqrstuvwxyz") == 22
    assert candidate(word = "rstuvxyzabcdefghijklmnopqrst") == 64
    assert candidate(word = "qrstuvwxyza") == 14
    assert candidate(word = "abcdefghilmnopqr") == 24
    assert candidate(word = "yzabcdefghijklmnopqrstuvw") == 52
    assert candidate(word = "xyzabcdefghijklmnopq") == 36
    assert candidate(word = "bcdefghijklmnopqrstuvwx") == 45
    assert candidate(word = "abcdefghijklmnopqrstuvmnop") == 56
    assert candidate(word = "zxcvbnm") == 7
    assert candidate(word = "xyzabcdefghijklmnopqrstuvw") == 56
    assert candidate(word = "qrstuvwxyzabcdefg") == 27
    assert candidate(word = "abcdefghijkmnopqrstuvwxy") == 48
    assert candidate(word = "abcdefghilmnopqrstuvwxyzz") == 52
    assert candidate(word = "defghijklmnopqrstu") == 30
    assert candidate(word = "vwxyzabcdefghijklmno") == 36
    assert candidate(word = "vwxyzabcdefghijklmnopqrstuvwx") == 68
    assert candidate(word = "zxcvbnmasdfghjklqwertyuiop") == 56
    assert candidate(word = "mnopqrstuv") == 12
    assert candidate(word = "zabcdefghijklmnopqrstuvwxy") == 56
    assert candidate(word = "defghijklmnopqrstuabcdefgh") == 56
    assert candidate(word = "asdfghjkl") == 10
    assert candidate(word = "abcdefghijklmno") == 22
    assert candidate(word = "ghijklmnopqrstuvwxyzabcdef") == 56
    assert candidate(word = "yzabcdefghijklmnop") == 30
    assert candidate(word = "qrstuvwxyzabcdefghijklmnoprstuvw") == 80
    assert candidate(word = "rstuvwxyzabcdefghijklmnopq") == 56
    assert candidate(word = "zabcdefghijklmnopqrstuvwx") == 52
    assert candidate(word = "nopqrstuvwxyzabcd") == 27
    assert candidate(word = "bcdefghijkl") == 14
    assert candidate(word = "nopqrstuvwxyzabcde") == 30
    assert candidate(word = "abcdefhijklmnopqrstuvwxyz") == 52
    assert candidate(word = "abcdefghijkmnopqrstuv") == 39
    assert candidate(word = "tuvwx") == 5
    assert candidate(word = "pqrstuvwxyzabcdef") == 27
    assert candidate(word = "jklmnopqrst") == 14
    assert candidate(word = "bcdefghijklmnopqrstvwxyz") == 48
    assert candidate(word = "lkjhgfdsa") == 10
    assert candidate(word = "pqrstuvwxyzabc") == 20
    assert candidate(word = "jklmnopqr") == 10
    assert candidate(word = "uvwxyzabcdefghijklmnopqrst") == 56
    assert candidate(word = "qrstuvwlmnop") == 16
    assert candidate(word = "acdegikmoqsuwy") == 20
    assert candidate(word = "pqrstuvwxyza") == 16
    assert candidate(word = "qrstuabcdefghijk") == 24
    assert candidate(word = "mnopqrstuvwx") == 16
    assert candidate(word = "hgfedcba") == 8


