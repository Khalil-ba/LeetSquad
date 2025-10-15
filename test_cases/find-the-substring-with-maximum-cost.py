def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "programming",chars = "pg",vals = [-1, -2]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",chars = "pg",vals = [-1, -2]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",chars = "a",vals = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",chars = "a",vals = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",chars = "z",vals = [26]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",chars = "z",vals = [26]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",chars = "xyz",vals = [24, 25, 26]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",chars = "xyz",vals = [24, 25, 26]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "adaa",chars = "d",vals = [-1000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "adaa",chars = "d",vals = [-1000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",chars = "abc",vals = [1, 2, 3]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",chars = "abc",vals = [1, 2, 3]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",chars = "z",vals = [26]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",chars = "z",vals = [26]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",chars = "he",vals = [5, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",chars = "he",vals = [5, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",chars = "abc",vals = [-1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",chars = "abc",vals = [-1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",chars = "abc",vals = [-1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",chars = "abc",vals = [-1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyx",chars = "zxy",vals = [100, 200, 300]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyx",chars = "zxy",vals = [100, 200, 300]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",chars = "a",vals = [1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",chars = "a",vals = [1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",chars = "aeiou",vals = [1, 2, 3, 4, 5]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",chars = "aeiou",vals = [1, 2, 3, 4, 5]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",chars = "pg",vals = [-5, -10]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",chars = "pg",vals = [-5, -10]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",chars = "z",vals = [1000]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",chars = "z",vals = [1000]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",chars = "helo",vals = [5, 10, 15, 20]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",chars = "helo",vals = [5, 10, 15, 20]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyz",chars = "abcdefgxyz",vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyz",chars = "abcdefgxyz",vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyza",chars = "a",vals = [1000]) == 2350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyza",chars = "a",vals = [1000]) == 2350: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [1000]) == 26000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [1000]) == 26000: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [100]) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [100]) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "z",vals = [-26]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "z",vals = [-26]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, -2, -3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, -2, -3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [3, 2, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [3, 2, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "",vals = []) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "",vals = []) == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "programmingisfun",chars = "progfun",vals = [5, 4, 3, 2, 1]) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programmingisfun",chars = "progfun",vals = [5, 4, 3, 2, 1]) == 134: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",chars = "abc",vals = [1, -2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",chars = "abc",vals = [1, -2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyyxx",chars = "xyz",vals = [100, 200, -300]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyyxx",chars = "xyz",vals = [100, 200, -300]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyxzyxzyxzyx",chars = "xyz",vals = [10, 20, 30]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyxzyxzyxzyx",chars = "xyz",vals = [10, 20, 30]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",chars = "lo",vals = [-1, -2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",chars = "lo",vals = [-1, -2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxy",vals = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxy",vals = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 702: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",chars = "mnopqr",vals = [1, 2, 3, 4, 5, 6]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",chars = "mnopqr",vals = [1, 2, 3, 4, 5, 6]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",chars = "he",vals = [10, -5]) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",chars = "he",vals = [10, -5]) == 132: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [26]) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [26]) == 520: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyz",chars = "xyz",vals = [100, 100, 100]) == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyz",chars = "xyz",vals = [100, 100, 100]) == 328: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",chars = "abcdefg",vals = [-1, -2, -3, -4, -5, -6, -7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",chars = "abcdefg",vals = [-1, -2, -3, -4, -5, -6, -7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzaaa",chars = "mno",vals = [13, 14, 15]) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzaaa",chars = "mno",vals = [13, 14, 15]) == 276: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyz",chars = "abcxyz",vals = [-1, -2, -3, -4, -5, -6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyz",chars = "abcxyz",vals = [-1, -2, -3, -4, -5, -6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisatemporarystring",chars = "aeiou",vals = [1, -1, 2, -2, 3]) == 259
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisatemporarystring",chars = "aeiou",vals = [1, -1, 2, -2, 3]) == 259: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",chars = "def",vals = [100, 200, 300]) == 1818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",chars = "def",vals = [100, 200, 300]) == 1818: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzz",chars = "z",vals = [1000]) == 11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzz",chars = "z",vals = [1000]) == 11000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij",chars = "acegikmoqsuwy",vals = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij",chars = "acegikmoqsuwy",vals = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",chars = "abcde",vals = [-1, -2, -3, -4, -5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",chars = "abcde",vals = [-1, -2, -3, -4, -5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzyx",chars = "xyz",vals = [-1, -2, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzyx",chars = "xyz",vals = [-1, -2, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwpwoeirutyiuyweoiuqweoiuyt",chars = "qwertyuiopasdfghjklzxcvbnm",vals = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwpwoeirutyiuyweoiuqweoiuyt",chars = "qwertyuiopasdfghjklzxcvbnm",vals = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",chars = "mno",vals = [10, 20, -30]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",chars = "mno",vals = [10, 20, -30]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababa",chars = "ab",vals = [-1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababa",chars = "ab",vals = [-1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello world",chars = "lo",vals = [10, -10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello world",chars = "lo",vals = [10, -10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",chars = "ism",vals = [-1, -2, 10]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",chars = "ism",vals = [-1, -2, 10]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "def",vals = [-10, 0, 5]) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "def",vals = [-10, 0, 5]) == 335: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",chars = "",vals = []) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",chars = "",vals = []) == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklm",chars = "def",vals = [10, 20, 30]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklm",chars = "def",vals = [10, 20, 30]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [10, 20, 30]) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [10, 20, 30]) == 224: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwertyuiop",vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwertyuiop",vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 732: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaa",chars = "a",vals = [5]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaa",chars = "a",vals = [5]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",chars = "z",vals = [100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",chars = "z",vals = [100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(s = "v",chars = "v",vals = [1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "v",chars = "v",vals = [1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",chars = "xyzabc",vals = [6, 5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",chars = "xyzabc",vals = [6, 5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxy",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxy",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklm",chars = "def",vals = [-5, -6, -7]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklm",chars = "def",vals = [-5, -6, -7]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "acegikmoqsuwy",vals = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "acegikmoqsuwy",vals = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 378: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc",chars = "abc",vals = [1, -1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc",chars = "abc",vals = [1, -1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, -1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, -1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",chars = "a",vals = [1]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",chars = "a",vals = [1]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaa",chars = "a",vals = [-1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaa",chars = "a",vals = [-1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabaaaaaaab",chars = "a",vals = [-1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabaaaaaaab",chars = "a",vals = [-1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [3, -2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [3, -2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabaaaaaaab",chars = "a",vals = [1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabaaaaaaab",chars = "a",vals = [1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab",chars = "ab",vals = [1000, -1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab",chars = "ab",vals = [1000, -1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",chars = "xyz",vals = [10, 20, 30]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",chars = "xyz",vals = [10, 20, 30]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",chars = "abc",vals = [10, 20, 30]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",chars = "abc",vals = [10, 20, 30]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyz",chars = "adg",vals = [10, -5, 20]) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyz",chars = "adg",vals = [10, -5, 20]) == 116: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",chars = "abc",vals = [-1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",chars = "abc",vals = [-1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",chars = "test",vals = [-1, -2, -3, -4]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",chars = "test",vals = [-1, -2, -3, -4]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qz",vals = [-100, 100]) == 408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qz",vals = [-100, 100]) == 408: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "zyx",vals = [26, 25, 24]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "zyx",vals = [26, 25, 24]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyz",chars = "xyz",vals = [-1, -2, -3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyz",chars = "xyz",vals = [-1, -2, -3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [1, -2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [1, -2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyz",chars = "aceg",vals = [-1, -2, -3, -4]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyz",chars = "aceg",vals = [-1, -2, -3, -4]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "a",vals = [-1]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "a",vals = [-1]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 702: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",chars = "z",vals = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",chars = "z",vals = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [5, -1, 10]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [5, -1, 10]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwertyuiopasdfghjklzxcvbnm",vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwertyuiopasdfghjklzxcvbnm",vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",chars = "aeiou",vals = [-10, -20, -30, -40, -50]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",chars = "aeiou",vals = [-10, -20, -30, -40, -50]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyz",chars = "mnop",vals = [10, 20, 30, 40]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyz",chars = "mnop",vals = [10, 20, 30, 40]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",chars = "abc",vals = [1, 2, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",chars = "abc",vals = [1, 2, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananabananabanana",chars = "ban",vals = [1, -1, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananabananabanana",chars = "ban",vals = [1, -1, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",chars = "ehllo",vals = [-100, 10, 20, 30, -5]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",chars = "ehllo",vals = [-100, 10, 20, 30, -5]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "aeiou",vals = [10, 20, 30, 40, 50]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "aeiou",vals = [10, 20, 30, 40, 50]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "zyxwvutsrqponmlkjihgfedcba",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "zyxwvutsrqponmlkjihgfedcba",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdxyz",chars = "abcd",vals = [4, 3, 2, 1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdxyz",chars = "abcd",vals = [4, 3, 2, 1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfoxjumpsoverthelazydog",chars = "quickbrownfoxjumpsoverthelazydog",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfoxjumpsoverthelazydog",chars = "quickbrownfoxjumpsoverthelazydog",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 372: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzyx",chars = "z",vals = [-5]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzyx",chars = "z",vals = [-5]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",chars = "abcdef",vals = [-1, -2, -3, -4, -5, -6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",chars = "abcdef",vals = [-1, -2, -3, -4, -5, -6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwerty",vals = [-1, -2, -3, -4, -5, -6]) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwerty",vals = [-1, -2, -3, -4, -5, -6]) == 243: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",chars = "aceg",vals = [-1, -2, -3, -4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",chars = "aceg",vals = [-1, -2, -3, -4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "",chars = "",vals = []) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",chars = "",vals = []) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",chars = "sip",vals = [1, 2, -3]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",chars = "sip",vals = [1, 2, -3]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",chars = "",vals = []) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",chars = "",vals = []) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",chars = "sip",vals = [10, -5, 15]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",chars = "sip",vals = [10, -5, 15]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",chars = "abcd",vals = [1, -1, 2, -2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",chars = "abcd",vals = [1, -1, 2, -2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 2, -3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 2, -3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "a",vals = [26]) == 376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "a",vals = [26]) == 376: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertypoiuytrewq",chars = "qwertyuiop",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertypoiuytrewq",chars = "qwertyuiop",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 702: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "z",vals = [1000]) == 1325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "z",vals = [1000]) == 1325: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "mnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "mnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyz",chars = "mnopqrstuvwxyz",vals = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyz",chars = "mnopqrstuvwxyz",vals = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstu",chars = "mnopqrstu",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstu",chars = "mnopqrstu",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog",chars = "aeiou",vals = [5, 5, 5, 5, 5]) == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog",chars = "aeiou",vals = [5, 5, 5, 5, 5]) == 401: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",chars = "abc",vals = [-1, -2, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",chars = "abc",vals = [-1, -2, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 3, -2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 3, -2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "baaabbbccc",chars = "abc",vals = [26, 25, 24]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baaabbbccc",chars = "abc",vals = [26, 25, 24]) == 250: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "programming",chars = "pg",vals = [-1, -2]) == 99
    assert candidate(s = "a",chars = "a",vals = [-1]) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
    assert candidate(s = "zzzzz",chars = "z",vals = [26]) == 130
    assert candidate(s = "xyz",chars = "xyz",vals = [24, 25, 26]) == 75
    assert candidate(s = "adaa",chars = "d",vals = [-1000]) == 2
    assert candidate(s = "abacaba",chars = "abc",vals = [1, 2, 3]) == 11
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
    assert candidate(s = "zzzz",chars = "z",vals = [26]) == 104
    assert candidate(s = "hello",chars = "he",vals = [5, 10]) == 54
    assert candidate(s = "abc",chars = "abc",vals = [-1, -1, -1]) == 0
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0
    assert candidate(s = "abc",chars = "abc",vals = [-1, -1, -1]) == 0
    assert candidate(s = "zzyx",chars = "zxy",vals = [100, 200, 300]) == 700
    assert candidate(s = "aaa",chars = "a",vals = [1]) == 3
    assert candidate(s = "hello",chars = "aeiou",vals = [1, 2, 3, 4, 5]) == 38
    assert candidate(s = "programming",chars = "pg",vals = [-5, -10]) == 91
    assert candidate(s = "zzz",chars = "z",vals = [1000]) == 3000
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
    assert candidate(s = "hello",chars = "helo",vals = [5, 10, 15, 20]) == 65
    assert candidate(s = "abcdefgxyz",chars = "abcdefgxyz",vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13]) == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyza",chars = "a",vals = [1000]) == 2350
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [1000]) == 26000
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [100]) == 2800
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-1]) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "z",vals = [-26]) == 325
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, -2, -3]) == 4
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [3, 2, 1]) == 38
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "",vals = []) == 351
    assert candidate(s = "programmingisfun",chars = "progfun",vals = [5, 4, 3, 2, 1]) == 134
    assert candidate(s = "aaaabbbbcccc",chars = "abc",vals = [1, -2, 3]) == 12
    assert candidate(s = "zzyyxx",chars = "xyz",vals = [100, 200, -300]) == 600
    assert candidate(s = "xyzzyxzyxzyxzyxzyxzyx",chars = "xyz",vals = [10, 20, 30]) == 420
    assert candidate(s = "hello",chars = "lo",vals = [-1, -2]) == 13
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxy",vals = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 702
    assert candidate(s = "mnopqr",chars = "mnopqr",vals = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(s = "hellohellohello",chars = "he",vals = [10, -5]) == 132
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [26]) == 520
    assert candidate(s = "abcdefgxyz",chars = "xyz",vals = [100, 100, 100]) == 328
    assert candidate(s = "aabbccddeeffgg",chars = "abcdefg",vals = [-1, -2, -3, -4, -5, -6, -7]) == 0
    assert candidate(s = "mnopqrstuvwxyzaaa",chars = "mno",vals = [13, 14, 15]) == 276
    assert candidate(s = "abcxyz",chars = "abcxyz",vals = [-1, -2, -3, -4, -5, -6]) == 0
    assert candidate(s = "thisisatemporarystring",chars = "aeiou",vals = [1, -1, 2, -2, 3]) == 259
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-1]) == 0
    assert candidate(s = "abcdefabcdefabcdef",chars = "def",vals = [100, 200, 300]) == 1818
    assert candidate(s = "zzzzzzzzzzz",chars = "z",vals = [1000]) == 11000
    assert candidate(s = "abcdefghijabcdefghij",chars = "acegikmoqsuwy",vals = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 120
    assert candidate(s = "abcdef",chars = "abcde",vals = [-1, -2, -3, -4, -5]) == 6
    assert candidate(s = "xyzzzzyx",chars = "xyz",vals = [-1, -2, -3]) == 0
    assert candidate(s = "qwpwoeirutyiuyweoiuqweoiuyt",chars = "qwertyuiopasdfghjklzxcvbnm",vals = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
    assert candidate(s = "mnopqr",chars = "mno",vals = [10, 20, -30]) == 51
    assert candidate(s = "babababababababababababa",chars = "ab",vals = [-1, 1]) == 1
    assert candidate(s = "hello world",chars = "lo",vals = [10, -10]) == 45
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
    assert candidate(s = "mississippi",chars = "ism",vals = [-1, -2, 10]) == 32
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "def",vals = [-10, 0, 5]) == 335
    assert candidate(s = "abcdefg",chars = "",vals = []) == 28
    assert candidate(s = "abcdefghijklm",chars = "def",vals = [10, 20, 30]) == 136
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [10, 20, 30]) == 224
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwertyuiop",vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 732
    assert candidate(s = "aaaabaaa",chars = "a",vals = [5]) == 37
    assert candidate(s = "zzzzzzzzzz",chars = "z",vals = [100]) == 1000
    assert candidate(s = "v",chars = "v",vals = [1000]) == 1000
    assert candidate(s = "xyzabc",chars = "xyzabc",vals = [6, 5, 4, 3, 2, 1]) == 21
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxy",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25]) == 52
    assert candidate(s = "abcdefghijklm",chars = "def",vals = [-5, -6, -7]) == 70
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "acegikmoqsuwy",vals = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 378
    assert candidate(s = "aaaaabbbbbccccc",chars = "abc",vals = [1, -1, 0]) == 5
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, -1, -1]) == 4
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",chars = "a",vals = [1]) == 32
    assert candidate(s = "aaaaabaaaabaaaa",chars = "a",vals = [-1]) == 2
    assert candidate(s = "aabaaaabaaaaaaab",chars = "a",vals = [-1]) == 2
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [3, -2, 1]) == 22
    assert candidate(s = "aabaaaabaaaaaaab",chars = "a",vals = [1]) == 19
    assert candidate(s = "abababababababababababababab",chars = "ab",vals = [1000, -1000]) == 1000
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 2, 3]) == 12
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-5]) == 0
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [0]) == 0
    assert candidate(s = "abcdefg",chars = "xyz",vals = [10, 20, 30]) == 28
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",chars = "abc",vals = [10, 20, 30]) == 600
    assert candidate(s = "abcdefgxyz",chars = "adg",vals = [10, -5, 20]) == 116
    assert candidate(s = "abcabcabc",chars = "abc",vals = [-1, -1, -1]) == 0
    assert candidate(s = "thisisateststring",chars = "test",vals = [-1, -2, -3, -4]) == 49
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-26]) == 0
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qz",vals = [-100, 100]) == 408
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "zyx",vals = [26, 25, 24]) == 351
    assert candidate(s = "abcdexyz",chars = "xyz",vals = [-1, -2, -3]) == 15
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [1, -2, 3]) == 12
    assert candidate(s = "abcdefgxyz",chars = "aceg",vals = [-1, -2, -3, -4]) == 78
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "a",vals = [-1]) == 350
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 702
    assert candidate(s = "zzzzzzzzzz",chars = "z",vals = [-1]) == 0
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [5, -1, 10]) == 60
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwertyuiopasdfghjklzxcvbnm",vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13]) == 13
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",chars = "aeiou",vals = [-10, -20, -30, -40, -50]) == 53
    assert candidate(s = "mnopqrstuvwxyz",chars = "mnop",vals = [10, 20, 30, 40]) == 315
    assert candidate(s = "abcabcabcabcabc",chars = "abc",vals = [1, 2, 3]) == 30
    assert candidate(s = "bananabananabanana",chars = "ban",vals = [1, -1, 2]) == 7
    assert candidate(s = "hellohellohello",chars = "ehllo",vals = [-100, 10, 20, 30, -5]) == 65
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "aeiou",vals = [10, 20, 30, 40, 50]) == 900
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",chars = "zyxwvutsrqponmlkjihgfedcba",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 351
    assert candidate(s = "abcdxyz",chars = "abcd",vals = [4, 3, 2, 1]) == 85
    assert candidate(s = "quickbrownfoxjumpsoverthelazydog",chars = "quickbrownfoxjumpsoverthelazydog",vals = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 372
    assert candidate(s = "xyzzzzzzzzzyx",chars = "z",vals = [-5]) == 53
    assert candidate(s = "aabbccddeeff",chars = "abcdef",vals = [-1, -2, -3, -4, -5, -6]) == 0
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",chars = "qwerty",vals = [-1, -2, -3, -4, -5, -6]) == 243
    assert candidate(s = "abcdefgabcdefg",chars = "aceg",vals = [-1, -2, -3, -4]) == 9
    assert candidate(s = "",chars = "",vals = []) == 0
    assert candidate(s = "mississippi",chars = "sip",vals = [1, 2, -3]) == 23
    assert candidate(s = "abcdef",chars = "",vals = []) == 21
    assert candidate(s = "mississippi",chars = "sip",vals = [10, -5, 15]) == 68
    assert candidate(s = "abcdabcdabcdabcd",chars = "abcd",vals = [1, -1, 2, -2]) == 2
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 2, -3]) == 6
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "a",vals = [26]) == 376
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",chars = "z",vals = [-500]) == 0
    assert candidate(s = "qwertypoiuytrewq",chars = "qwertyuiop",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 76
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 702
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "z",vals = [1000]) == 1325
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",chars = "mnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 78
    assert candidate(s = "mnopqrstuvwxyz",chars = "mnopqrstuvwxyz",vals = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 119
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",chars = "abcdefghijklmnopqrstuvwxyz",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26]) == 0
    assert candidate(s = "mnopqrstu",chars = "mnopqrstu",vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",chars = "aeiou",vals = [5, 5, 5, 5, 5]) == 401
    assert candidate(s = "aaabbbccc",chars = "abc",vals = [-1, -2, -3]) == 0
    assert candidate(s = "abacabadabacaba",chars = "abc",vals = [-1, 3, -2]) == 8
    assert candidate(s = "baaabbbccc",chars = "abc",vals = [26, 25, 24]) == 250


