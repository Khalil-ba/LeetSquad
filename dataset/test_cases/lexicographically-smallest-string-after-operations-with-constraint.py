def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zbbz",k = 3) == "aaaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zbbz",k = 3) == "aaaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",k = 1) == "aac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 1) == "aac": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",k = 0) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 0) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",k = 9) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",k = 9) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 50) == "aaaaaaaaalponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 50) == "aaaaaaaaalponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",k = 10) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",k = 10) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",k = 5) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",k = 5) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",k = 2) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 2) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s = "vwxyz",k = 25) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vwxyz",k = 25) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",k = 7) == "aello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",k = 7) == "aello": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 10) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 10) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",k = 10) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",k = 10) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrst",k = 20) == "aart"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrst",k = 20) == "aart": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == "aaaaaaacijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == "aaaaaaacijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xaxcd",k = 4) == "aawcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xaxcd",k = 4) == "aawcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",k = 26) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 26) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 25) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 25) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 10) == "aaaaaf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 10) == "aaaaaf": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 1) == "azzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 1) == "azzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnop",k = 15) == "akop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnop",k = 15) == "akop": {e}')
    
    total += 1
    try:
        result = candidate(s = "lol",k = 0) == "lol"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lol",k = 0) == "lol": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",k = 6) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",k = 6) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 26) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 26) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",k = 1) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",k = 1) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 26) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 26) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 0) == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 0) == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 100) == "aaaaaaaaaaaaadlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 100) == "aaaaaaaaaaaaadlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",k = 12) == "aaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",k = 12) == "aaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 16) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 16) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 30) == "aaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 30) == "aaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 30) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 30) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",k = 12) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",k = 12) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuv",k = 50) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuv",k = 50) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 12) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 12) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuvwxyz",k = 26) == "aaltuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuvwxyz",k = 26) == "aaltuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",k = 15) == "akopqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",k = 15) == "akopqr": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",k = 50) == "aaaaaajming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",k = 50) == "aaaaaajming": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnop",k = 25) == "aaop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnop",k = 25) == "aaop": {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqq",k = 50) == "aaaaaqqqqqqq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqq",k = 50) == "aaaaaqqqqqqq": {e}')
    
    total += 1
    try:
        result = candidate(s = "cryptography",k = 100) == "aaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cryptography",k = 100) == "aaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "nopqrs",k = 100) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nopqrs",k = 100) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 50) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 50) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 18) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 18) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 52) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 52) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwerasdfzxcv",k = 15) == "aadrasdfzxcv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwerasdfzxcv",k = 15) == "aadrasdfzxcv": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",k = 9) == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",k = 9) == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuv",k = 30) == "aaaquv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuv",k = 30) == "aaaquv": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyza",k = 26) == "aaaaaaacijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyza",k = 26) == "aaaaaaacijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 25) == "aaaaaaadijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 25) == "aaaaaaadijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "vutsrqponmlkjihgfedcba",k = 500) == "aaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vutsrqponmlkjihgfedcba",k = 500) == "aaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 25) == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 25) == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 5) == "aaabefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 5) == "aaabefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklm",k = 39) == "aaaaaaaaagklm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklm",k = 39) == "aaaaaaaaagklm": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 400) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 400) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 150) == "aaaaaaaaaaaaaaaaaaaaaaaahm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 150) == "aaaaaaaaaaaaaaaaaaaaaaaahm": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 9) == "aaaaaaaaaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 9) == "aaaaaaaaaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 25) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 25) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 20) == "aaaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 20) == "aaaaaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 0) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 0) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "wxyz",k = 8) == "aaxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wxyz",k = 8) == "aaxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 260) == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 260) == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mmmm",k = 15) == "ajmm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmm",k = 15) == "ajmm": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 12) == "aaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 12) == "aaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 15) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 15) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",k = 50) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",k = 50) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 35) == "aaaaaaaabj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 35) == "aaaaaaaabj": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",k = 30) == "aajpqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",k = 30) == "aajpqr": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 1300) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 1300) == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 500) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 500) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",k = 16) == "aaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",k = 16) == "aaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "nopqrstuvwxyz",k = 78) == "aaaaaaaatwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nopqrstuvwxyz",k = 78) == "aaaaaaaatwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzz",k = 18) == "aaaaaaaaaxzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzz",k = 18) == "aaaaaaaaaxzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "wxyz",k = 11) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wxyz",k = 11) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 26) == "aaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 26) == "aaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 26) == "aaaaaaacij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 26) == "aaaaaaacij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 15) == "aaaaaaghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 15) == "aaaaaaghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb",k = 7) == "aaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb",k = 7) == "aaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 8) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 8) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrst",k = 100) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrst",k = 100) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",k = 10) == "cnopqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",k = 10) == "cnopqr": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",k = 15) == "aahlo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",k = 15) == "aahlo": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 50) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 50) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqq",k = 64) == "aaaaaamq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqq",k = 64) == "aaaaaamq": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 100) == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 100) == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdxyz",k = 50) == "aaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdxyz",k = 50) == "aaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aquickbrownfoxjumps",k = 50) == "aaaaaaaakwnfoxjumps"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aquickbrownfoxjumps",k = 50) == "aaaaaaaakwnfoxjumps": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyz",k = 12) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyz",k = 12) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 13) == "aaaaac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 13) == "aaaaac": {e}')
    
    total += 1
    try:
        result = candidate(s = "wxyz",k = 5) == "awyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wxyz",k = 5) == "awyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 100) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 100) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 1300) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 1300) == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 50) == "aaaaaaaaijhgfdsapoiuytrewq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 50) == "aaaaaaaaijhgfdsapoiuytrewq": {e}')
    
    total += 1
    try:
        result = candidate(s = "vwxyz",k = 30) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vwxyz",k = 30) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 200) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 200) == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuv",k = 10) == "arstuv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuv",k = 10) == "arstuv": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",k = 20) == "afopqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",k = 20) == "afopqr": {e}')
    
    total += 1
    try:
        result = candidate(s = "jklmno",k = 15) == "aelmno"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jklmno",k = 15) == "aelmno": {e}')
    
    total += 1
    try:
        result = candidate(s = "qzab",k = 5) == "lzab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qzab",k = 5) == "lzab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 45) == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 45) == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 500) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 500) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnop",k = 20) == "afop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnop",k = 20) == "afop": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == "aaaaaaosrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == "aaaaaaosrqponmlkjihgfedcba": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zbbz",k = 3) == "aaaz"
    assert candidate(s = "abc",k = 1) == "aac"
    assert candidate(s = "abc",k = 0) == "abc"
    assert candidate(s = "zzz",k = 9) == "aaa"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 50) == "aaaaaaaaalponmlkjihgfedcba"
    assert candidate(s = "xyz",k = 10) == "aaa"
    assert candidate(s = "aaa",k = 5) == "aaa"
    assert candidate(s = "abc",k = 2) == "aab"
    assert candidate(s = "vwxyz",k = 25) == "aaaaa"
    assert candidate(s = "hello",k = 7) == "aello"
    assert candidate(s = "abcd",k = 10) == "aaaa"
    assert candidate(s = "aaaa",k = 10) == "aaaa"
    assert candidate(s = "qrst",k = 20) == "aart"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == "aaaaaaacijklmnopqrstuvwxyz"
    assert candidate(s = "xaxcd",k = 4) == "aawcd"
    assert candidate(s = "abc",k = 26) == "aaa"
    assert candidate(s = "zzzz",k = 25) == "aaaa"
    assert candidate(s = "abcdef",k = 10) == "aaaaaf"
    assert candidate(s = "zzzz",k = 1) == "azzz"
    assert candidate(s = "mnop",k = 15) == "akop"
    assert candidate(s = "lol",k = 0) == "lol"
    assert candidate(s = "zzz",k = 6) == "aaa"
    assert candidate(s = "zzzz",k = 26) == "aaaa"
    assert candidate(s = "aaaa",k = 1) == "aaaa"
    assert candidate(s = "abcdef",k = 26) == "aaaaaa"
    assert candidate(s = "abcdefg",k = 0) == "abcdefg"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 100) == "aaaaaaaaaaaaadlkjihgfedcba"
    assert candidate(s = "aaaabbbbcccc",k = 12) == "aaaaaaaaaaaa"
    assert candidate(s = "zzzz",k = 16) == "aaaa"
    assert candidate(s = "abcdabcdabcd",k = 30) == "aaaaaaaaaaaa"
    assert candidate(s = "abcdef",k = 30) == "aaaaaa"
    assert candidate(s = "xyzabc",k = 12) == "aaaaaa"
    assert candidate(s = "qrstuv",k = 50) == "aaaaaa"
    assert candidate(s = "aabbcc",k = 12) == "aaaaaa"
    assert candidate(s = "qrstuvwxyz",k = 26) == "aaltuvwxyz"
    assert candidate(s = "mnopqr",k = 15) == "akopqr"
    assert candidate(s = "programming",k = 50) == "aaaaaajming"
    assert candidate(s = "mnop",k = 25) == "aaop"
    assert candidate(s = "qqqqqqqqqqqq",k = 50) == "aaaaaqqqqqqq"
    assert candidate(s = "cryptography",k = 100) == "aaaaaaaaaaaa"
    assert candidate(s = "nopqrs",k = 100) == "aaaaaa"
    assert candidate(s = "abcde",k = 50) == "aaaaa"
    assert candidate(s = "abcdef",k = 18) == "aaaaaa"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 52) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "qwerasdfzxcv",k = 15) == "aadrasdfzxcv"
    assert candidate(s = "aaaaaaaaaa",k = 9) == "aaaaaaaaaa"
    assert candidate(s = "qrstuv",k = 30) == "aaaquv"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyza",k = 26) == "aaaaaaacijklmnopqrstuvwxyza"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 25) == "aaaaaaadijklmnopqrstuvwxyz"
    assert candidate(s = "vutsrqponmlkjihgfedcba",k = 500) == "aaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "zzzzzzzzzz",k = 25) == "aaaaaaaaaa"
    assert candidate(s = "abcdefg",k = 5) == "aaabefg"
    assert candidate(s = "abcdefghijklm",k = 39) == "aaaaaaaaagklm"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 400) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 150) == "aaaaaaaaaaaaaaaaaaaaaaaahm"
    assert candidate(s = "zzzzzzzzzz",k = 9) == "aaaaaaaaaz"
    assert candidate(s = "abcdef",k = 25) == "aaaaaa"
    assert candidate(s = "abcdefg",k = 20) == "aaaaaab"
    assert candidate(s = "abcdef",k = 0) == "abcdef"
    assert candidate(s = "wxyz",k = 8) == "aaxz"
    assert candidate(s = "zzzzzzzzzz",k = 260) == "aaaaaaaaaa"
    assert candidate(s = "mmmm",k = 15) == "ajmm"
    assert candidate(s = "abcabcabcabc",k = 12) == "aaaaaaaaaaaa"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "zzzz",k = 15) == "aaaa"
    assert candidate(s = "zzzzzz",k = 50) == "aaaaaa"
    assert candidate(s = "abcdefghij",k = 35) == "aaaaaaaabj"
    assert candidate(s = "mnopqr",k = 30) == "aajpqr"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 2000) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 1300) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k = 500) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abcdabcd",k = 16) == "aaaaaaaa"
    assert candidate(s = "nopqrstuvwxyz",k = 78) == "aaaaaaaatwxyz"
    assert candidate(s = "xyzzxyzzxyzz",k = 18) == "aaaaaaaaaxzz"
    assert candidate(s = "wxyz",k = 11) == "aaaa"
    assert candidate(s = "abcdabcdabcd",k = 26) == "aaaaaaaaaaaa"
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abcdefghij",k = 26) == "aaaaaaacij"
    assert candidate(s = "abcdefghij",k = 15) == "aaaaaaghij"
    assert candidate(s = "aaaabbbb",k = 7) == "aaaaaaaa"
    assert candidate(s = "zzzz",k = 8) == "aaaa"
    assert candidate(s = "qrst",k = 100) == "aaaa"
    assert candidate(s = "mnopqr",k = 10) == "cnopqr"
    assert candidate(s = "hello",k = 15) == "aahlo"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 50) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabdabcd"
    assert candidate(s = "qqqqqqqq",k = 64) == "aaaaaamq"
    assert candidate(s = "zzzzzzzzzz",k = 100) == "aaaaaaaaaa"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "abcdxyz",k = 50) == "aaaaaaa"
    assert candidate(s = "aquickbrownfoxjumps",k = 50) == "aaaaaaaakwnfoxjumps"
    assert candidate(s = "abcxyz",k = 12) == "aaaaaa"
    assert candidate(s = "abcdef",k = 13) == "aaaaac"
    assert candidate(s = "wxyz",k = 5) == "awyz"
    assert candidate(s = "abcd",k = 100) == "aaaa"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 1300) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 50) == "aaaaaaaaijhgfdsapoiuytrewq"
    assert candidate(s = "vwxyz",k = 30) == "aaaaa"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",k = 200) == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "qrstuv",k = 10) == "arstuv"
    assert candidate(s = "mnopqr",k = 20) == "afopqr"
    assert candidate(s = "jklmno",k = 15) == "aelmno"
    assert candidate(s = "qzab",k = 5) == "lzab"
    assert candidate(s = "abcdefghij",k = 45) == "aaaaaaaaaa"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 500) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "mnop",k = 20) == "afop"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == "aaaaaaosrqponmlkjihgfedcba"


