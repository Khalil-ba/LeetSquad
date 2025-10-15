def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "xyzyxzyzxzyz",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzyxzyzxzyz",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi",k = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi",k = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzz",k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzz",k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz",k = 1) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz",k = 1) == 351: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababab",k = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababab",k = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababab",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababab",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababab",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababab",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcd",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcd",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 1) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 1) == 77: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvqrstuvqrstuv",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvqrstuvqrstuv",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrspqr",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrspqr",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzz",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzz",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba",k = 1) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba",k = 1) == 351: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhii",k = 2) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhii",k = 2) == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba",k = 1) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba",k = 1) == 31: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzz",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzz",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 46: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg",k = 1) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg",k = 1) == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcd",k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcd",k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabc",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabc",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbccc",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbccc",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde",k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde",k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababababababababababababababababababababababababababa",k = 2) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababababababababababababababababababababababababababa",k = 2) == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzxyzxyz",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzxyzxyz",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabc",k = 1) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabc",k = 1) == 114: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzyyyxx",k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzyyyxx",k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 31: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabc",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabc",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "a",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 26) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 26) == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabc",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabc",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "igigee",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "igigee",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaa",k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaa",k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 58: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "xxxxxxyyyyyzzzzz",k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xxxxxxyyyyyzzzzz",k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabc",k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabc",k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaa",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaa",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "qqqqqqqqqqqqqqqqqqqq",k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qqqqqqqqqqqqqqqqqqqq",k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbcccc",k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbcccc",k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "acacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacaca",k = 2) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacaca",k = 2) == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababab",k = 2) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababab",k = 2) == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzz",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzz",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzz",k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzz",k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzyyyxxxwwvvuuttrrqqqppponnmmllkkjjiihhggffeeddccbbbaaa",k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzyyyxxxwwvvuuttrrqqqppponnmmllkkjjiihhggffeeddccbbbaaa",k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffff",k = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffff",k = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccdddd",k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccdddd",k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa",k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa",k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbcccaabb",k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbcccaabb",k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghi",k = 1) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghi",k = 1) == 45: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababababababababababab",k = 2) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababababababababababab",k = 2) == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzyyyxxxwwwwvvvuuutttsssrrrqqqpppoonnmmmlllkkkjjjiii",k = 3) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzyyyxxxwwwwvvvuuutttsssrrrqqqpppoonnmmmlllkkkjjjiii",k = 3) == 61: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzzz",k = 1) == 354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzzz",k = 1) == 354: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzyxzyzxzyx",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzyxzyzxzyx",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzz",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzz",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacaba",k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacaba",k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaabbaabbaabb",k = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaabbaabbaabb",k = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdeabcdabcde",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdeabcdabcde",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc",k = 1) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc",k = 1) == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzz",k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzz",k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqr",k = 1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqr",k = 1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyxxyxyxyx",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyxxyxyxyx",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrsmnopqrsmnopqrsmnopqrs",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrsmnopqrsmnopqrsmnopqrs",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 47: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnm",k = 1) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnm",k = 1) == 51: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij",k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij",k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzaaa",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzaaa",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "qqwweerrtt",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qqwweerrtt",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijk",k = 1) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijk",k = 1) == 66: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == 351: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcd",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcd",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabc",k = 3) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabc",k = 3) == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzaaa",k = 1) == 354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzaaa",k = 1) == 354: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccaaaabbbbcccc",k = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccaaaabbbbcccc",k = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzz",k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzz",k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabc",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabc",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababab",k = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababab",k = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdef",k = 1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdef",k = 1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeaabbccddeeaabbccddeeddeeaabbcc",k = 2) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeaabbccddeeaabbccddeeddeeaabbcc",k = 2) == 57: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabc",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabc",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 43: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzyyyxxx",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzyyyxxx",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzzzzzyxxyzzzzzyx",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzzzzzyxxyzzzzzyx",k = 3) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "xyzyxzyzxzyz",k = 2) == 2
    assert candidate(word = "mississippi",k = 1) == 11
    assert candidate(word = "zzzzzzzzz",k = 9) == 1
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",k = 1) == 351
    assert candidate(word = "ababababab",k = 1) == 19
    assert candidate(word = "ababab",k = 2) == 3
    assert candidate(word = "ababababab",k = 2) == 7
    assert candidate(word = "abcdabcdabcd",k = 4) == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 1) == 77
    assert candidate(word = "qrstuvqrstuvqrstuv",k = 3) == 0
    assert candidate(word = "mnopqrspqr",k = 2) == 0
    assert candidate(word = "zzzzzzzzz",k = 3) == 7
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba",k = 1) == 351
    assert candidate(word = "aabbccddeeffgghhii",k = 2) == 45
    assert candidate(word = "abacabadabacaba",k = 1) == 31
    assert candidate(word = "zzzzzzzzz",k = 2) == 8
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 46
    assert candidate(word = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs",k = 4) == 0
    assert candidate(word = "abcdefg",k = 1) == 28
    assert candidate(word = "abcd",k = 1) == 10
    assert candidate(word = "abcabcabcabcabc",k = 3) == 7
    assert candidate(word = "aaabbbccc",k = 3) == 6
    assert candidate(word = "abcde",k = 1) == 15
    assert candidate(word = "abababababababababababababababababababababababababababababababababa",k = 2) == 64
    assert candidate(word = "xyzxyzxyz",k = 3) == 1
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabc",k = 1) == 114
    assert candidate(word = "zzzzzzyyyxx",k = 2) == 10
    assert candidate(word = "xyzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 31
    assert candidate(word = "abcabcabcabc",k = 4) == 1
    assert candidate(word = "a",k = 1) == 1
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 26) == 25
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 40
    assert candidate(word = "abcabcabcabc",k = 3) == 4
    assert candidate(word = "igigee",k = 2) == 3
    assert candidate(word = "aaaaaa",k = 6) == 1
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 58
    assert candidate(word = "abcabcabc",k = 3) == 1
    assert candidate(word = "xxxxxxyyyyyzzzzz",k = 5) == 7
    assert candidate(word = "abcabcabcabcabcabcabc",k = 3) == 13
    assert candidate(word = "aabbaa",k = 2) == 6
    assert candidate(word = "qqqqqqqqqqqqqqqqqqqq",k = 5) == 16
    assert candidate(word = "aaaabbbbcccc",k = 4) == 6
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 50
    assert candidate(word = "acacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacaca",k = 2) == 64
    assert candidate(word = "ababababababababababababab",k = 2) == 23
    assert candidate(word = "zzzzzz",k = 2) == 5
    assert candidate(word = "zzzzzzzzzz",k = 5) == 6
    assert candidate(word = "zzzyyyxxxwwvvuuttrrqqqppponnmmllkkjjiihhggffeeddccbbbaaa",k = 3) == 12
    assert candidate(word = "aaaabbbbccccddddeeeeffff",k = 4) == 21
    assert candidate(word = "aaaabbbbccccdddd",k = 4) == 10
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 55
    assert candidate(word = "abacabadabacaba",k = 3) == 0
    assert candidate(word = "mississippi",k = 2) == 3
    assert candidate(word = "aaa",k = 1) == 3
    assert candidate(word = "aabbbcccaabb",k = 2) == 12
    assert candidate(word = "abcdefghi",k = 1) == 45
    assert candidate(word = "ababababababababababababababababababababab",k = 2) == 39
    assert candidate(word = "zzzyyyxxxwwwwvvvuuutttsssrrrqqqpppoonnmmmlllkkkjjjiii",k = 3) == 61
    assert candidate(word = "aabbcc",k = 2) == 6
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzzz",k = 1) == 354
    assert candidate(word = "xyzyxzyzxzyx",k = 2) == 3
    assert candidate(word = "zzzzz",k = 5) == 1
    assert candidate(word = "abacaba",k = 1) == 15
    assert candidate(word = "aabbaabbaabbaabb",k = 2) == 21
    assert candidate(word = "abacabadabacaba",k = 2) == 0
    assert candidate(word = "abcdabcdeabcdabcde",k = 2) == 0
    assert candidate(word = "abcabcabc",k = 1) == 24
    assert candidate(word = "zzzzz",k = 1) == 5
    assert candidate(word = "mnopqr",k = 1) == 21
    assert candidate(word = "xyxxyxyxyx",k = 2) == 6
    assert candidate(word = "mnopqrsmnopqrsmnopqrsmnopqrs",k = 5) == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 5) == 47
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm",k = 1) == 51
    assert candidate(word = "abcdefghij",k = 1) == 55
    assert candidate(word = "zzzaaa",k = 3) == 2
    assert candidate(word = "qqwweerrtt",k = 2) == 6
    assert candidate(word = "abcdefghijk",k = 1) == 66
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == 351
    assert candidate(word = "abcdabcdabcd",k = 2) == 0
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabc",k = 3) == 22
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzaaa",k = 1) == 354
    assert candidate(word = "aaaabbbbccccaaaabbbbcccc",k = 4) == 24
    assert candidate(word = "zzzzzz",k = 1) == 6
    assert candidate(word = "abcabcabcabcabcabc",k = 3) == 10
    assert candidate(word = "abababababababababab",k = 2) == 17
    assert candidate(word = "abcdef",k = 1) == 21
    assert candidate(word = "aabbccddeeaabbccddeeaabbccddeeddeeaabbcc",k = 2) == 57
    assert candidate(word = "abcdabc",k = 2) == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 43
    assert candidate(word = "zzzyyyxxx",k = 3) == 6
    assert candidate(word = "xyzzzzzyxxyzzzzzyx",k = 3) == 6


