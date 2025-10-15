def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "qpqprstuvwxyzqpqprstuvwxyzqpqprstuvwxyz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpqprstuvwxyzqpqprstuvwxyzqpqprstuvwxyz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abczabczabcz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abczabczabcz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "azza") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "azza") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "za") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "za") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qpqprstuvwxyz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpqprstuvwxyz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "zaabcdefghijklmnopqrstuvwxyz") == 352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zaabcdefghijklmnopqrstuvwxyz") == 352: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabcdefghijklmnopqrstuvwxyz") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabcdefghijklmnopqrstuvwxyz") == 377: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1027: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abczab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abczab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "cac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "cab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1053
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1053: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcdabcdeabcdefabcdefg") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcdabcdeabcdefabcdefg") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyza") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyza") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuvwxyzabcdefghijklmno") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuvwxyzabcdefghijklmno") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzabcdefghijkl") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzabcdefghijkl") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "nopqrstuvwxyzabcdefghijklmno") == 403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nopqrstuvwxyzabcdefghijklmno") == 403: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbcccccccc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbcccccccc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuv") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuv") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "vwxyzabcdefghijklmnopqrstu") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vwxyzabcdefghijklmnopqrstu") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdbca") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdbca") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabzabzabzabzabzabzabzabzabzabzabzabzabzabzab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabzabzabzabzabzabzabzabzabzabzabzabzabzabzab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1703
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1703: {e}')
    
    total += 1
    try:
        result = candidate(s = "cdefghijklmnopqrstuvwxyzab") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cdefghijklmnopqrstuvwxyzab") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefg") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefg") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3055: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdzabcde") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdzabcde") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzaabcdefghijklmnopqrstuvwxyzab") == 403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzaabcdefghijklmnopqrstuvwxyzab") == 403: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyza") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyza") == 377: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2379
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2379: {e}')
    
    total += 1
    try:
        result = candidate(s = "qpqrstuvwxyzabcdefghijklmno") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpqrstuvwxyzabcdefghijklmno") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdezyxabcdezyxabcdezyxabcdezyxabcdezyxabcdezyx") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdezyxabcdezyxabcdezyxabcdezyxabcdezyxabcdezyx") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "qpqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdefabcdefgabcdefg") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdefabcdefgabcdefg") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdzabcdezabcdefzabcdefgzabcdefgz") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdzabcdezabcdefzabcdefgzabcdefgz") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzabcdefghijklmnop") == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzabcdefghijklmnop") == 455: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdefghijklmnopqrstuvwxyz") == 429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdefghijklmnopqrstuvwxyz") == 429: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "qpqprstuvwxyzqpqprstuvwxyzqpqprstuvwxyz") == 48
    assert candidate(s = "abczabczabcz") == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 351
    assert candidate(s = "azza") == 3
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "za") == 3
    assert candidate(s = "qpqprstuvwxyz") == 48
    assert candidate(s = "zaabcdefghijklmnopqrstuvwxyz") == 352
    assert candidate(s = "a") == 1
    assert candidate(s = "abcabcabc") == 6
    assert candidate(s = "zabcdefghijklmnopqrstuvwxyz") == 377
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "xyzxyzxyz") == 6
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1027
    assert candidate(s = "abcd") == 10
    assert candidate(s = "abczab") == 9
    assert candidate(s = "cac") == 2
    assert candidate(s = "cab") == 4
    assert candidate(s = "zab") == 6
    assert candidate(s = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1053
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "abcabcdabcdeabcdefabcdefg") == 28
    assert candidate(s = "mnopqrstuvwxyza") == 120
    assert candidate(s = "pqrstuvwxyzabcdefghijklmno") == 351
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 48
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 10
    assert candidate(s = "mnopqrstuvwxyzabcdefghijkl") == 351
    assert candidate(s = "nopqrstuvwxyzabcdefghijklmno") == 403
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "aaaaaaaaaabbbbbbbbcccccccc") == 5
    assert candidate(s = "qrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuv") == 21
    assert candidate(s = "vwxyzabcdefghijklmnopqrstu") == 351
    assert candidate(s = "abcdbca") == 10
    assert candidate(s = "zabzabzabzabzabzabzabzabzabzabzabzabzabzabzab") == 6
    assert candidate(s = "abacabadabacaba") == 5
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "abcabcabcabc") == 6
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1703
    assert candidate(s = "cdefghijklmnopqrstuvwxyzab") == 351
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 55
    assert candidate(s = "abababababababababababababababababababab") == 3
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefg") == 28
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3055
    assert candidate(s = "abcdzabcde") == 21
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzaabcdefghijklmnopqrstuvwxyzab") == 403
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 351
    assert candidate(s = "abcdefghijklmnopqrstuvwxyza") == 377
    assert candidate(s = "zzzzzzzzzz") == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2379
    assert candidate(s = "qpqrstuvwxyzabcdefghijklmno") == 351
    assert candidate(s = "xyzabcdezyxabcdezyxabcdezyxabcdezyxabcdezyxabcdezyx") == 36
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 51
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 6
    assert candidate(s = "qpqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 27
    assert candidate(s = "abcdabcdeabcdefabcdefgabcdefg") == 28
    assert candidate(s = "abcdzabcdezabcdefzabcdefgzabcdefgz") == 36
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 351
    assert candidate(s = "mnopqrstuvwxyzabcdefghijklmnop") == 455
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 351
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 51
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 351
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "xyzabcdefghijklmnopqrstuvwxyz") == 429
    assert candidate(s = "xyzabc") == 21
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1


