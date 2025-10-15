def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababab",x = 1,y = 1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababab",x = 1,y = 1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba",x = 7,y = 8) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba",x = 7,y = 8) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",x = 10,y = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",x = 10,y = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab",x = 10,y = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab",x = 10,y = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaabab",x = 3,y = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaabab",x = 3,y = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",x = 2,y = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",x = 2,y = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaabab",x = 10,y = 5) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaabab",x = 10,y = 5) == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",x = 1,y = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",x = 1,y = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "baabaa",x = 3,y = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baabaa",x = 3,y = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",x = 7,y = 8) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",x = 7,y = 8) == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "ba",x = 1,y = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ba",x = 1,y = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",x = 1,y = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",x = 1,y = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",x = 1,y = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",x = 1,y = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba",x = 7,y = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba",x = 7,y = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",x = 2,y = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",x = 2,y = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",x = 1,y = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",x = 1,y = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaxybbaabb",x = 5,y = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaxybbaabb",x = 5,y = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",x = 1,y = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",x = 1,y = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",x = 10,y = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",x = 10,y = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "",x = 100,y = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",x = 100,y = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaabab",x = 2,y = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaabab",x = 2,y = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "cdbcbbaaabab",x = 4,y = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cdbcbbaaabab",x = 4,y = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",x = 100,y = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",x = 100,y = 200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "baabbaabba",x = 500,y = 500) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baabbaabba",x = 500,y = 500) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(s = "",x = 100,y = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",x = 100,y = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "",x = 1,y = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",x = 1,y = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbaaaa",x = 8,y = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbaaaa",x = 8,y = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",x = 1000,y = 1000) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",x = 1000,y = 1000) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaab",x = 10,y = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaab",x = 10,y = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbbaaaaabbbb",x = 10,y = 15) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbbaaaaabbbb",x = 10,y = 15) == 115: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababab",x = 7,y = 3) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababab",x = 7,y = 3) == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",x = 10000,y = 10000) == 80000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",x = 10000,y = 10000) == 80000: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbbabbbabbbabbbabbbabb",x = 15,y = 25) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbbabbbabbbabbbabbbabb",x = 15,y = 25) == 150: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbaabababababab",x = 6,y = 7) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbaabababababab",x = 6,y = 7) == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbba",x = 1000,y = 1000) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbba",x = 1000,y = 1000) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbabaabababbabaabababbba",x = 100,y = 50) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbabaabababbabaabababbba",x = 100,y = 50) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababa",x = 10,y = 15) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababa",x = 10,y = 15) == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba",x = 3,y = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba",x = 3,y = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbaaaabbbbbaaaabbbb",x = 4,y = 6) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbaaaabbbbbaaaabbbb",x = 4,y = 6) == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbbaaabbba",x = 10,y = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbbaaabbba",x = 10,y = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababa",x = 7,y = 7) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababa",x = 7,y = 7) == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "baabababababab",x = 5,y = 5) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baabababababab",x = 5,y = 5) == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababababababa",x = 20,y = 20) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababababababa",x = 20,y = 20) == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababababababababababababababababa",x = 2,y = 3) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababababababababababababababababa",x = 2,y = 3) == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababaabababababababab",x = 1000,y = 1000) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababaabababababababab",x = 1000,y = 1000) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbbaaaaabbbb",x = 6,y = 9) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbbaaaaabbbb",x = 6,y = 9) == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaabababab",x = 1000,y = 500) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaabababab",x = 1000,y = 500) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabbaaa",x = 10,y = 5) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabbaaa",x = 10,y = 5) == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababa",x = 1,y = 10000) == 240000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababa",x = 1,y = 10000) == 240000: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbaaabbaaa",x = 5,y = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbaaabbaaa",x = 5,y = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbbbabbbbabbbbabbb",x = 12,y = 15) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbbbabbbbabbbbabbb",x = 12,y = 15) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababbababbaabab",x = 4,y = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababbababbaabab",x = 4,y = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbbaababba",x = 100,y = 200) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbbaababba",x = 100,y = 200) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbabababababababbaa",x = 8,y = 6) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbabababababababbaa",x = 8,y = 6) == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbb",x = 100,y = 100) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbb",x = 100,y = 100) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 10000,y = 1) == 160000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 10000,y = 1) == 160000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba",x = 10,y = 20) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba",x = 10,y = 20) == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazbzabzbabzbabz",x = 5,y = 6) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazbzabzbabzbabz",x = 5,y = 6) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababbbabababa",x = 1,y = 10000) == 60000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababbbabababa",x = 1,y = 10000) == 60000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababab",x = 2,y = 1) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababab",x = 2,y = 1) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaabbbaaabbbaaabbbaa",x = 15,y = 5) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaabbbaaabbbaaabbbaa",x = 15,y = 5) == 170: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaa",x = 1000,y = 500) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaa",x = 1000,y = 500) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbabababbaabba",x = 10,y = 5) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbabababbaabba",x = 10,y = 5) == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababa",x = 10000,y = 10000) == 280000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababa",x = 10000,y = 10000) == 280000: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzababxyzbaaxyzbaxyz",x = 15,y = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzababxyzbaaxyzbaxyz",x = 15,y = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "zababxyzab",x = 4,y = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zababxyzab",x = 4,y = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabbbabbbabbbabbbabbb",x = 20,y = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabbbabbbabbbabbbabbb",x = 20,y = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaabbbaaabbbaab",x = 7,y = 3) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaabbbaaabbbaab",x = 7,y = 3) == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 10,y = 10) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 10,y = 10) == 160: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababa",x = 1,y = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababa",x = 1,y = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababab",x = 1,y = 1) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababab",x = 1,y = 1) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 90,y = 100) == 1590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 90,y = 100) == 1590: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbbaabbbbaabbbbaab",x = 200,y = 300) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbbaabbbbaabbbbaab",x = 200,y = 300) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababab",x = 1,y = 1) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababab",x = 1,y = 1) == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 50,y = 50) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 50,y = 50) == 800: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaabababab",x = 10,y = 15) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaabababab",x = 10,y = 15) == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabababba",x = 500,y = 400) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabababba",x = 500,y = 400) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaababbaab",x = 10,y = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaababbaab",x = 10,y = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzxzyz",x = 100,y = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzxzyz",x = 100,y = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbaababba",x = 3,y = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbaababba",x = 3,y = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababab",x = 1,y = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababab",x = 1,y = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxy",x = 3,y = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxy",x = 3,y = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababa",x = 2,y = 3) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababa",x = 2,y = 3) == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababa",x = 1000,y = 500) == 15500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababa",x = 1000,y = 500) == 15500: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 25,y = 30) == 475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 25,y = 30) == 475: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababab",x = 5,y = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababab",x = 5,y = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 1,y = 100) == 1501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 1,y = 100) == 1501: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaabbaabbabab",x = 10000,y = 1) == 70000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaabbaabbabab",x = 10000,y = 1) == 70000: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbababbababbababbababb",x = 5,y = 4) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbababbababbababbababb",x = 5,y = 4) == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",x = 1000,y = 2000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",x = 1000,y = 2000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababababa",x = 1,y = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababababa",x = 1,y = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbbaaaaaaaaaaabbbbbbbbbbbbb",x = 15,y = 25) == 425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbbaaaaaaaaaaabbbbbbbbbbbbb",x = 15,y = 25) == 425: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbababababababababab",x = 1,y = 9999) == 109989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbababababababababab",x = 1,y = 9999) == 109989: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabba",x = 10,y = 10) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabba",x = 10,y = 10) == 80: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabaabbaaabaabbaabb",x = 1,y = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabaabbaaabaabbaabb",x = 1,y = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbababbaabbababbaabbbaabababbbabababababababa",x = 8000,y = 9000) == 180000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbababbaabbababbaabbbaabababbbabababababababa",x = 8000,y = 9000) == 180000: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababa",x = 7,y = 7) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababa",x = 7,y = 7) == 112: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababababababababababababababa",x = 1000,y = 1000) == 28000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababababababababababababababa",x = 1000,y = 1000) == 28000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 10,y = 9) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 10,y = 9) == 160: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbababababababababababababababab",x = 100,y = 90) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbababababababababababababababab",x = 100,y = 90) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 6,y = 4) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 6,y = 4) == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbababababba",x = 20,y = 15) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbababababba",x = 20,y = 15) == 135: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbbbabbbbabbaa",x = 8,y = 6) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbbbabbbbabbaa",x = 8,y = 6) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabba",x = 8,y = 3) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabba",x = 8,y = 3) == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababababa",x = 20,y = 15) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababababa",x = 20,y = 15) == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbaababbaababba",x = 7,y = 9) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbaababbaababba",x = 7,y = 9) == 79: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbabababbaababababab",x = 20,y = 10) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbabababbaababababab",x = 20,y = 10) == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbbaabab",x = 5,y = 10) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbbaabab",x = 5,y = 10) == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbaaaaabbbbbbaaaaabbbbb",x = 1000,y = 500) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbaaaaabbbbbbaaaaabbbbb",x = 1000,y = 500) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(s = "baaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbb",x = 500,y = 1000) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbb",x = 500,y = 1000) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababa",x = 1,y = 100) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababa",x = 1,y = 100) == 800: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaabaaaaba",x = 20,y = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaabaaaaba",x = 20,y = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababab",x = 7,y = 8) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababab",x = 7,y = 8) == 103: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaababaababbbbababba",x = 3,y = 2) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaababaababbbbababba",x = 3,y = 2) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "baaababababababaabaababb",x = 10,y = 20) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baaababababababaabaababb",x = 10,y = 20) == 200: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababaabab",x = 3,y = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababaabab",x = 3,y = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababababababababababa",x = 1,y = 2) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababababababababababa",x = 1,y = 2) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbbbbbbbaaaaaaaa",x = 20,y = 18) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbbbbbbbaaaaaaaa",x = 20,y = 18) == 164: {e}')
    
    total += 1
    try:
        result = candidate(s = "baabbaabbaabbaabbaabbaabbaabbaab",x = 30,y = 25) == 475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baabbaabbaabbaabbaabbaabbaabbaab",x = 30,y = 25) == 475: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",x = 5,y = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",x = 5,y = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababab",x = 100,y = 1) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababab",x = 100,y = 1) == 900: {e}')
    
    total += 1
    try:
        result = candidate(s = "baabbaabbaabbaabbaab",x = 4,y = 3) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baabbaabbaabbaabbaab",x = 4,y = 3) == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaabbaaabbaa",x = 1,y = 10000) == 60000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaabbaaabbaa",x = 1,y = 10000) == 60000: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbaaaaabbbbbaaaaabbbbbaaaaa",x = 100,y = 1) == 1005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbaaaaabbbbbaaaaabbbbbaaaaa",x = 100,y = 1) == 1005: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababa",x = 50,y = 25) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababa",x = 50,y = 25) == 550: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababababaab",x = 100,y = 100) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababababaab",x = 100,y = 100) == 500: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababa",x = 2000,y = 2000) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababa",x = 2000,y = 2000) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbbabbaabababbababbaabbbbaabab",x = 20,y = 15) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbbabbaabababbababbaabbbbaabab",x = 20,y = 15) == 255: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababaab",x = 8,y = 7) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababaab",x = 8,y = 7) == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababa",x = 100,y = 90) == 790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababa",x = 100,y = 90) == 790: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaabbaabbbaabbaabbba",x = 2,y = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaabbaabbbaabbaabbba",x = 2,y = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababababa",x = 1,y = 2) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababababa",x = 1,y = 2) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgg",x = 10,y = 20) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgg",x = 10,y = 20) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbbaaaaabbb",x = 5,y = 3) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbbaaaaabbb",x = 5,y = 3) == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbaababbaab",x = 6,y = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbaababbaab",x = 6,y = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaababababba",x = 3,y = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaababababba",x = 3,y = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab",x = 9999,y = 1) == 119988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab",x = 9999,y = 1) == 119988: {e}')
    
    total += 1
    try:
        result = candidate(s = "baabaabaabaabaabaabaabaabaabaabaab",x = 5000,y = 4000) == 59000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baabaabaabaabaabaabaabaabaabaabaab",x = 5000,y = 4000) == 59000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",x = 1,y = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",x = 1,y = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababa",x = 2,y = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababa",x = 2,y = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabbaabba",x = 10,y = 15) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabbaabba",x = 10,y = 15) == 175: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababababababababababa",x = 5000,y = 4000) == 119000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababababababababababa",x = 5000,y = 4000) == 119000: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabaaaabbbbbaaaab",x = 3,y = 2) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabaaaabbbbbaaaab",x = 3,y = 2) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababa",x = 2000,y = 2000) == 48000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababa",x = 2000,y = 2000) == 48000: {e}')
    
    total += 1
    try:
        result = candidate(s = "baababababababababababababababab",x = 4,y = 4) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baababababababababababababababab",x = 4,y = 4) == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababababababababababababababa",x = 3,y = 2) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababababababababababababababa",x = 3,y = 2) == 83: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbabaabbbbab",x = 7,y = 3) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbabaabbbbab",x = 7,y = 3) == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 1000,y = 1000) == 16000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 1000,y = 1000) == 16000: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",x = 1000,y = 2000) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",x = 1000,y = 2000) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabaababaabbaaaabbbbaaabbabab",x = 5,y = 6) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabaababaabbaaaabbbbaaabbabab",x = 5,y = 6) == 93: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",x = 1000,y = 1000) == 16000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",x = 1000,y = 1000) == 16000: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababa",x = 5,y = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababa",x = 5,y = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaababbabbaab",x = 3,y = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaababbabbaab",x = 3,y = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababababababababababababababa",x = 8,y = 5) == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababababababababababababababa",x = 8,y = 5) == 221: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "ababababababababababababababababababababab",x = 1,y = 1) == 21
    assert candidate(s = "abbaabba",x = 7,y = 8) == 31
    assert candidate(s = "abababab",x = 10,y = 10) == 40
    assert candidate(s = "ababab",x = 10,y = 10) == 30
    assert candidate(s = "babaabab",x = 3,y = 2) == 11
    assert candidate(s = "aabbcc",x = 2,y = 2) == 4
    assert candidate(s = "babaabab",x = 10,y = 5) == 35
    assert candidate(s = "abcde",x = 1,y = 2) == 1
    assert candidate(s = "baabaa",x = 3,y = 2) == 5
    assert candidate(s = "aaaaabbbbb",x = 7,y = 8) == 35
    assert candidate(s = "ba",x = 1,y = 1) == 1
    assert candidate(s = "aabbcc",x = 1,y = 1) == 2
    assert candidate(s = "ab",x = 1,y = 1) == 1
    assert candidate(s = "abbaabba",x = 7,y = 3) == 24
    assert candidate(s = "abcabcabcabc",x = 2,y = 3) == 8
    assert candidate(s = "abababab",x = 1,y = 1) == 4
    assert candidate(s = "aabbaaxybbaabb",x = 5,y = 4) == 20
    assert candidate(s = "ababababab",x = 1,y = 1) == 5
    assert candidate(s = "abcde",x = 10,y = 20) == 10
    assert candidate(s = "",x = 100,y = 200) == 0
    assert candidate(s = "babaabab",x = 2,y = 3) == 11
    assert candidate(s = "cdbcbbaaabab",x = 4,y = 5) == 19
    assert candidate(s = "abcde",x = 100,y = 200) == 100
    assert candidate(s = "baabbaabba",x = 500,y = 500) == 2500
    assert candidate(s = "",x = 100,y = 100) == 0
    assert candidate(s = "",x = 1,y = 1) == 0
    assert candidate(s = "bbbbbbaaaa",x = 8,y = 7) == 28
    assert candidate(s = "ababababab",x = 1000,y = 1000) == 5000
    assert candidate(s = "babaab",x = 10,y = 5) == 25
    assert candidate(s = "aaaabbbbbaaaaabbbb",x = 10,y = 15) == 115
    assert candidate(s = "babababababababababababab",x = 7,y = 3) == 84
    assert candidate(s = "abababababababab",x = 10000,y = 10000) == 80000
    assert candidate(s = "babbbabbbabbbabbbabbbabb",x = 15,y = 25) == 150
    assert candidate(s = "ababbaabababababab",x = 6,y = 7) == 62
    assert candidate(s = "aabbaabbaabbba",x = 1000,y = 1000) == 7000
    assert candidate(s = "bbabaabababbabaabababbba",x = 100,y = 50) == 1050
    assert candidate(s = "babababababa",x = 10,y = 15) == 90
    assert candidate(s = "abbaabbaabba",x = 3,y = 2) == 17
    assert candidate(s = "bbbbbaaaabbbbbaaaabbbb",x = 4,y = 6) == 48
    assert candidate(s = "bbaabbbaaabbba",x = 10,y = 5) == 55
    assert candidate(s = "babababababa",x = 7,y = 7) == 42
    assert candidate(s = "baabababababab",x = 5,y = 5) == 35
    assert candidate(s = "bababababababababababa",x = 20,y = 20) == 220
    assert candidate(s = "bababababababababababababababababababababa",x = 2,y = 3) == 63
    assert candidate(s = "babababaabababababababab",x = 1000,y = 1000) == 12000
    assert candidate(s = "aaaabbbbbaaaaabbbb",x = 6,y = 9) == 69
    assert candidate(s = "babaabababab",x = 1000,y = 500) == 5500
    assert candidate(s = "abbbabbaaa",x = 10,y = 5) == 35
    assert candidate(s = "ababababababababababababababababababababababababa",x = 1,y = 10000) == 240000
    assert candidate(s = "aaaaaabbaaabbaaa",x = 5,y = 5) == 20
    assert candidate(s = "babbbbabbbbabbbbabbb",x = 12,y = 15) == 60
    assert candidate(s = "abababababbababbaabab",x = 4,y = 4) == 40
    assert candidate(s = "ababbbbaababba",x = 100,y = 200) == 1100
    assert candidate(s = "bbabababababababbaa",x = 8,y = 6) == 68
    assert candidate(s = "aaaaaaaaaabbbbbbbbbb",x = 100,y = 100) == 1000
    assert candidate(s = "abababababababababababababababab",x = 10000,y = 1) == 160000
    assert candidate(s = "abbaabbaabba",x = 10,y = 20) == 110
    assert candidate(s = "zazbzabzbabzbabz",x = 5,y = 6) == 17
    assert candidate(s = "bababbbabababa",x = 1,y = 10000) == 60000
    assert candidate(s = "abababababababababababababababababab",x = 2,y = 1) == 36
    assert candidate(s = "aabbbaaabbbaaabbbaaabbbaa",x = 15,y = 5) == 170
    assert candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaa",x = 1000,y = 500) == 12000
    assert candidate(s = "bbaabbabababbaabba",x = 10,y = 5) == 75
    assert candidate(s = "ababababababababababababababababababababababababababababa",x = 10000,y = 10000) == 280000
    assert candidate(s = "xyzababxyzbaaxyzbaxyz",x = 15,y = 10) == 50
    assert candidate(s = "zababxyzab",x = 4,y = 5) == 13
    assert candidate(s = "abbbabbbabbbabbbabbbabbb",x = 20,y = 10) == 120
    assert candidate(s = "aabbbaaabbbaaabbbaab",x = 7,y = 3) == 66
    assert candidate(s = "abababababababababababababababab",x = 10,y = 10) == 160
    assert candidate(s = "babababababababa",x = 1,y = 2) == 16
    assert candidate(s = "ababababababababababababab",x = 1,y = 1) == 13
    assert candidate(s = "abababababababababababababababab",x = 90,y = 100) == 1590
    assert candidate(s = "abbbbaabbbbaabbbbaab",x = 200,y = 300) == 2000
    assert candidate(s = "abababababababababababababababababababababababababababab",x = 1,y = 1) == 28
    assert candidate(s = "abababababababababababababababab",x = 50,y = 50) == 800
    assert candidate(s = "babaabababab",x = 10,y = 15) == 85
    assert candidate(s = "abbbabababba",x = 500,y = 400) == 2400
    assert candidate(s = "babaababbaab",x = 10,y = 5) == 55
    assert candidate(s = "xyxzyzyzxzyz",x = 100,y = 200) == 0
    assert candidate(s = "ababbaababba",x = 3,y = 2) == 17
    assert candidate(s = "ababababababababababababababababab",x = 1,y = 1) == 17
    assert candidate(s = "xyxyxyxyxy",x = 3,y = 3) == 0
    assert candidate(s = "ababababababababababababababababababababababababababababa",x = 2,y = 3) == 84
    assert candidate(s = "babababababababababababababababa",x = 1000,y = 500) == 15500
    assert candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 25,y = 30) == 475
    assert candidate(s = "ababababababababababab",x = 5,y = 5) == 55
    assert candidate(s = "abababababababababababababababab",x = 1,y = 100) == 1501
    assert candidate(s = "abaabbaabbabab",x = 10000,y = 1) == 70000
    assert candidate(s = "babbababbababbababbababb",x = 5,y = 4) == 45
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",x = 1000,y = 2000) == 0
    assert candidate(s = "bababababababababa",x = 1,y = 2) == 18
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbbaaaaaaaaaaabbbbbbbbbbbbb",x = 15,y = 25) == 425
    assert candidate(s = "bbaabbababababababababab",x = 1,y = 9999) == 109989
    assert candidate(s = "abbaabbaabbaabba",x = 10,y = 10) == 80
    assert candidate(s = "aabbaaabaabbaaabaabbaabb",x = 1,y = 1) == 10
    assert candidate(s = "bbbababbaabbababbaabbbaabababbbabababababababa",x = 8000,y = 9000) == 180000
    assert candidate(s = "babababababababababababababababa",x = 7,y = 7) == 112
    assert candidate(s = "babababababababababababababababababababababababababababa",x = 1000,y = 1000) == 28000
    assert candidate(s = "abababababababababababababababab",x = 10,y = 9) == 160
    assert candidate(s = "bbababababababababababababababab",x = 100,y = 90) == 1500
    assert candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 6,y = 4) == 94
    assert candidate(s = "ababbbababababba",x = 20,y = 15) == 135
    assert candidate(s = "babbbbabbbbabbaa",x = 8,y = 6) == 36
    assert candidate(s = "abbaabbaabbaabbaabba",x = 8,y = 3) == 75
    assert candidate(s = "aabababababa",x = 20,y = 15) == 100
    assert candidate(s = "ababbaababbaababba",x = 7,y = 9) == 79
    assert candidate(s = "ababbbabababbaababababab",x = 20,y = 10) == 210
    assert candidate(s = "ababbbbaabab",x = 5,y = 10) == 45
    assert candidate(s = "bbbbbaaaaabbbbbbaaaaabbbbb",x = 1000,y = 500) == 10000
    assert candidate(s = "baaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbb",x = 500,y = 1000) == 12500
    assert candidate(s = "babababababababa",x = 1,y = 100) == 800
    assert candidate(s = "bbaaabaaaaba",x = 20,y = 10) == 60
    assert candidate(s = "ababababababababababababab",x = 7,y = 8) == 103
    assert candidate(s = "aabbbaababaababbbbababba",x = 3,y = 2) == 32
    assert candidate(s = "baaababababababaabaababb",x = 10,y = 20) == 200
    assert candidate(s = "babababababababaabab",x = 3,y = 2) == 29
    assert candidate(s = "bababababababababababababababa",x = 1,y = 2) == 30
    assert candidate(s = "abbbbbbbbbaaaaaaaa",x = 20,y = 18) == 164
    assert candidate(s = "baabbaabbaabbaabbaabbaabbaabbaab",x = 30,y = 25) == 475
    assert candidate(s = "abcabcabcabc",x = 5,y = 5) == 20
    assert candidate(s = "ababababababababab",x = 100,y = 1) == 900
    assert candidate(s = "baabbaabbaabbaabbaab",x = 4,y = 3) == 39
    assert candidate(s = "bbaaabbaaabbaa",x = 1,y = 10000) == 60000
    assert candidate(s = "bbbbbaaaaabbbbbaaaaabbbbbaaaaa",x = 100,y = 1) == 1005
    assert candidate(s = "abababababababababababa",x = 50,y = 25) == 550
    assert candidate(s = "aababababaab",x = 100,y = 100) == 500
    assert candidate(s = "babababababa",x = 2000,y = 2000) == 12000
    assert candidate(s = "babbbabbaabababbababbaabbbbaabab",x = 20,y = 15) == 255
    assert candidate(s = "babababababaab",x = 8,y = 7) == 55
    assert candidate(s = "babababababababa",x = 100,y = 90) == 790
    assert candidate(s = "aabbbaabbaabbbaabbaabbba",x = 2,y = 3) == 31
    assert candidate(s = "babababababababababababababababababa",x = 1,y = 2) == 36
    assert candidate(s = "aabbaabbccddeeffgg",x = 10,y = 20) == 60
    assert candidate(s = "aaaabbbbbaaaaabbb",x = 5,y = 3) == 38
    assert candidate(s = "ababbaababbaab",x = 6,y = 4) == 40
    assert candidate(s = "babaababababba",x = 3,y = 2) == 20
    assert candidate(s = "abababababababababababab",x = 9999,y = 1) == 119988
    assert candidate(s = "baabaabaabaabaabaabaabaabaabaabaab",x = 5000,y = 4000) == 59000
    assert candidate(s = "abababababababababab",x = 1,y = 2) == 19
    assert candidate(s = "bababababa",x = 2,y = 3) == 15
    assert candidate(s = "abbaabbaabbaabbaabbaabba",x = 10,y = 15) == 175
    assert candidate(s = "babababababababababababababababababababababababa",x = 5000,y = 4000) == 119000
    assert candidate(s = "bbaabaaaabbbbbaaaab",x = 3,y = 2) == 25
    assert candidate(s = "ababababababababababababababababababababababababa",x = 2000,y = 2000) == 48000
    assert candidate(s = "baababababababababababababababab",x = 4,y = 4) == 64
    assert candidate(s = "babababababababababababababababababababababababababababa",x = 3,y = 2) == 83
    assert candidate(s = "ababbbabaabbbbab",x = 7,y = 3) == 42
    assert candidate(s = "abbaabbaabbaabbaabbaabbaabbaabba",x = 1000,y = 1000) == 16000
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",x = 1000,y = 2000) == 2000
    assert candidate(s = "abbbabaababaabbaaaabbbbaaabbabab",x = 5,y = 6) == 93
    assert candidate(s = "abababababababababababababababab",x = 1000,y = 1000) == 16000
    assert candidate(s = "babababababababababababa",x = 5,y = 5) == 60
    assert candidate(s = "ababaababbabbaab",x = 3,y = 4) == 30
    assert candidate(s = "babababababababababababababababababababababababababababa",x = 8,y = 5) == 221


