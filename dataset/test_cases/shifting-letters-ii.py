def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "world",shifts = [[0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0]]) == "sknhz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "world",shifts = [[0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0]]) == "sknhz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",shifts = [[0, 2, 0]]) == "wxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",shifts = [[0, 2, 0]]) == "wxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",shifts = [[1, 4, 1], [2, 3, 0]]) == "accdff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",shifts = [[1, 4, 1], [2, 3, 0]]) == "accdff": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 1]]) == "ddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 1]]) == "ddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [[0, 4, 1], [1, 3, 0]]) == "iellp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [[0, 4, 1], [1, 3, 0]]) == "iellp": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]]) == "ignnp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]]) == "ignnp": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "dztz",shifts = [[0, 0, 0], [1, 1, 1]]) == "catz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dztz",shifts = [[0, 0, 0], [1, 1, 1]]) == "catz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0]]) == "yxwvutsrqponmlkjihgfedcbaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0]]) == "yxwvutsrqponmlkjihgfedcbaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",shifts = [[0, 0, 1], [0, 0, 0]]) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",shifts = [[0, 0, 1], [0, 0, 0]]) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [[0, 3, 1], [1, 2, 0], [2, 3, 1]]) == "bbdf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [[0, 3, 1], [1, 2, 0], [2, 3, 1]]) == "bbdf": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",shifts = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]) == "www"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",shifts = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]) == "www": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 0]]) == "zabcdefghijklmnopqrstuvwxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 0]]) == "zabcdefghijklmnopqrstuvwxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [[0, 4, 1]]) == "ifmmp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [[0, 4, 1]]) == "ifmmp": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [[0, 4, 0], [5, 9, 1], [0, 9, 1], [3, 6, 0]]) == "zzzyyaabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [[0, 4, 0], [5, 9, 1], [0, 9, 1], [3, 6, 0]]) == "zzzyyaabbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "alphabet",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [5, 5, 1]]) == "bkqgbbet"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alphabet",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [5, 5, 1]]) == "bkqgbbet": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [5, 10, 0], [15, 20, 1]]) == "bcdeffghijkmnoprstuvwwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [5, 10, 0], [15, 20, 1]]) == "bcdeffghijkmnoprstuvwwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",shifts = [[0, 51, 1], [10, 40, 0], [20, 30, 1], [30, 40, 0]]) == "bbccddeeffffgghhiijjllmmnnoopppoppqqrrsstvwwxxyyzzaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",shifts = [[0, 51, 1], [10, 40, 0], [20, 30, 1], [30, 40, 0]]) == "bbccddeeffffgghhiijjllmmnnoopppoppqqrrsstvwwxxyyzzaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacax",shifts = [[0, 5, 1], [1, 4, 0], [2, 3, 1], [0, 5, 0]]) == "aaaczx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacax",shifts = [[0, 5, 1], [1, 4, 0], [2, 3, 1], [0, 5, 0]]) == "aaaczx": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0]]) == "qrpgsanmjng"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0]]) == "qrpgsanmjng": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 9, 0], [1, 8, 1], [2, 7, 0], [3, 6, 1], [4, 5, 0]]) == "zbbddeggii"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 9, 0], [1, 8, 1], [2, 7, 0], [3, 6, 1], [4, 5, 0]]) == "zbbddeggii": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzabcdefghijkl",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1], [15, 25, 0]]) == "nopqrrstuvxyzabbdefghhijkl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzabcdefghijkl",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1], [15, 25, 0]]) == "nopqrrstuvxyzabbdefghhijkl": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 0]]) == "cdefghijklmnopqrstuvwxyzab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 0]]) == "cdefghijklmnopqrstuvwxyzab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 0], [0, 25, 1], [0, 25, 0]]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 0], [0, 25, 1], [0, 25, 0]]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",shifts = [[0, 7, 1], [1, 6, 0], [2, 5, 1], [3, 4, 0]]) == "bbbbacac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",shifts = [[0, 7, 1], [1, 6, 0], [2, 5, 1], [3, 4, 0]]) == "bbbbacac": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [2, 8, 0], [4, 6, 1]]) == "aazzaaazza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [2, 8, 0], [4, 6, 1]]) == "aazzaaazza": {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",shifts = [[0, 2, 1], [3, 5, 0], [6, 8, 1], [1, 4, 0], [2, 3, 1], [5, 7, 0], [7, 8, 1]]) == "blhnpgtio"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",shifts = [[0, 2, 1], [3, 5, 0], [6, 8, 1], [1, 4, 0], [2, 3, 1], [5, 7, 0], [7, 8, 1]]) == "blhnpgtio": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0]]) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0]]) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "codingame",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 8, 1], [0, 8, 0], [0, 8, 1], [0, 8, 0], [0, 8, 1]]) == "dpchohzlf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "codingame",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 8, 1], [0, 8, 0], [0, 8, 1], [0, 8, 0], [0, 8, 1]]) == "dpchohzlf": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",shifts = [[0, 14, 1], [1, 13, 0], [2, 12, 1], [3, 11, 0], [4, 10, 1], [5, 9, 0]]) == "bbbcbbadabbcbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",shifts = [[0, 14, 1], [1, 13, 0], [2, 12, 1], [3, 11, 0], [4, 10, 1], [5, 9, 0]]) == "bbbcbbadabbcbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 4, 1], [5, 9, 0], [0, 4, 0], [5, 9, 1], [0, 9, 1]]) == "bcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 4, 1], [5, 9, 0], [0, 4, 0], [5, 9, 1], [0, 9, 1]]) == "bcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [1, 24, 0], [2, 23, 1], [3, 22, 0], [4, 21, 1]]) == "bbddfghijklmnopqrstuvwwyya"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [1, 24, 0], [2, 23, 1], [3, 22, 0], [4, 21, 1]]) == "bbddfghijklmnopqrstuvwwyya": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0], [5, 10, 1], [15, 20, 0]]) == "yxwvuutsrqpnmlkihgfeddcbaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0], [5, 10, 1], [15, 20, 0]]) == "yxwvuutsrqpnmlkihgfeddcbaz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",shifts = [[0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 1]]) == "wwwww"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",shifts = [[0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 1]]) == "wwwww": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "bbddfggiik"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "bbddfggiik": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1]]) == "bcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1]]) == "bcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1]]) == "aaaaazzzzzaaaaaabbbbbaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1]]) == "aaaaazzzzzaaaaaabbbbbaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1]]) == "bcdefghijklmnopq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1]]) == "bcdefghijklmnopq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 12, 1], [13, 25, 0], [0, 25, 1], [0, 25, 0], [0, 25, 1]]) == "cdefghijklmnonopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 12, 1], [13, 25, 0], [0, 25, 1], [0, 25, 0], [0, 25, 1]]) == "cdefghijklmnonopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "alibabacloud",shifts = [[0, 9, 1], [2, 4, 0], [5, 7, 1], [8, 11, 0], [0, 3, 1], [6, 9, 0], [1, 8, 1], [2, 7, 0]]) == "cojcadbdlntc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alibabacloud",shifts = [[0, 9, 1], [2, 4, 0], [5, 7, 1], [8, 11, 0], [0, 3, 1], [6, 9, 0], [1, 8, 1], [2, 7, 0]]) == "cojcadbdlntc": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 0], [0, 2, 0]]) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 0], [0, 2, 0]]) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",shifts = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1]]) == "bdefghh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",shifts = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1]]) == "bdefghh": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",shifts = [[0, 4, 1], [5, 9, 0], [10, 14, 1], [0, 14, 0], [0, 14, 1]]) == "bcbdbazczabdbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",shifts = [[0, 4, 1], [5, 9, 0], [10, 14, 1], [0, 14, 0], [0, 14, 1]]) == "bcbdbazczabdbcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello world",shifts = [[0, 4, 1], [6, 10, 0], [3, 8, 1], [1, 9, 0], [0, 10, 1]]) == "jfmnqoworkd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello world",shifts = [[0, 4, 1], [6, 10, 0], [3, 8, 1], [1, 9, 0], [0, 10, 1]]) == "jfmnqoworkd": {e}')
    
    total += 1
    try:
        result = candidate(s = "example",shifts = [[0, 6, 1], [1, 5, 0], [2, 4, 1], [3, 6, 0]]) == "fxbmpke"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "example",shifts = [[0, 6, 1], [1, 5, 0], [2, 4, 1], [3, 6, 0]]) == "fxbmpke": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 4, 0], [6, 3, 1], [7, 2, 0], [8, 1, 1], [9, 0, 0]]) == "bcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 4, 0], [6, 3, 1], [7, 2, 0], [8, 1, 1], [9, 0, 0]]) == "bcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",shifts = [[0, 6, 1], [1, 5, 0], [2, 4, 1], [3, 3, 0]]) == "bbddffh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",shifts = [[0, 6, 1], [1, 5, 0], [2, 4, 1], [3, 3, 0]]) == "bbddffh": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellozworld",shifts = [[0, 4, 1], [5, 9, 0], [6, 10, 1], [7, 8, 0], [9, 10, 1], [10, 10, 0]]) == "ifmmpywnqme"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellozworld",shifts = [[0, 4, 1], [5, 9, 0], [6, 10, 1], [7, 8, 0], [9, 10, 1], [10, 10, 0]]) == "ifmmpywnqme": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",shifts = [[0, 2, 1], [3, 4, 0], [1, 3, 1], [0, 1, 0], [4, 4, 1], [2, 2, 0]]) == "acdde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",shifts = [[0, 2, 1], [3, 4, 0], [1, 3, 1], [0, 1, 0], [4, 4, 1], [2, 2, 0]]) == "acdde": {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",shifts = [[0, 8, 1], [1, 7, 0], [2, 6, 1], [3, 5, 0], [4, 4, 1]]) == "yymoqhpnf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",shifts = [[0, 8, 1], [1, 7, 0], [2, 6, 1], [3, 5, 0], [4, 4, 1]]) == "yymoqhpnf": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 0], [0, 25, 1], [0, 25, 0], [0, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 0], [0, 25, 1], [0, 25, 0], [0, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [[0, 9, 1], [4, 8, 0], [2, 6, 1], [1, 7, 0], [0, 8, 1]]) == "rsqisbnmjog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [[0, 9, 1], [4, 8, 0], [2, 6, 1], [1, 7, 0], [0, 8, 1]]) == "rsqisbnmjog": {e}')
    
    total += 1
    try:
        result = candidate(s = "shiftmeplease",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 9, 1], [10, 11, 0], [12, 12, 1]]) == "tiheundomfzrf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "shiftmeplease",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 9, 1], [10, 11, 0], [12, 12, 1]]) == "tiheundomfzrf": {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithms",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 4, 0], [6, 3, 1], [7, 2, 0], [8, 1, 1], [9, 0, 0]]) == "bmhpsjuint"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithms",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 4, 0], [6, 3, 1], [7, 2, 0], [8, 1, 1], [9, 0, 0]]) == "bmhpsjuint": {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfox",shifts = [[0, 12, 1], [1, 11, 0], [2, 10, 1], [3, 9, 0], [4, 8, 1], [5, 7, 0]]) == "rujclbroxngoy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfox",shifts = [[0, 12, 1], [1, 11, 0], [2, 10, 1], [3, 9, 0], [4, 8, 1], [5, 7, 0]]) == "rujclbroxngoy": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",shifts = [[0, 2, 1], [3, 5, 0], [0, 5, 1], [1, 4, 0]]) == "oopopr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",shifts = [[0, 2, 1], [3, 5, 0], [0, 5, 1], [1, 4, 0]]) == "oopopr": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",shifts = [[0, 15, 1], [1, 14, 0], [2, 13, 1], [3, 12, 0], [4, 11, 1], [5, 10, 0], [6, 9, 1], [7, 8, 0]]) == "bbddffhhikkmmooq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",shifts = [[0, 15, 1], [1, 14, 0], [2, 13, 1], [3, 12, 0], [4, 11, 1], [5, 10, 0], [6, 9, 1], [7, 8, 0]]) == "bbddffhhikkmmooq": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "azazaazaza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "azazaazaza": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",shifts = [[0, 4, 0], [1, 3, 1], [2, 2, 0], [3, 5, 1], [6, 8, 0], [7, 7, 1], [8, 10, 0], [9, 9, 1], [10, 10, 0]]) == "lirtitrinpg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",shifts = [[0, 4, 0], [1, 3, 1], [2, 2, 0], [3, 5, 1], [6, 8, 0], [7, 7, 1], [8, 10, 0], [9, 9, 1], [10, 10, 0]]) == "lirtitrinpg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [6, 6, 0], [7, 7, 0], [8, 8, 0], [9, 9, 0], [10, 10, 0], [11, 11, 0], [12, 12, 0], [13, 13, 0], [14, 14, 0], [15, 15, 0], [16, 16, 0], [17, 17, 0], [18, 18, 0], [19, 19, 0], [20, 20, 0], [21, 21, 0], [22, 22, 0], [23, 23, 0], [24, 24, 1], [25, 25, 1]]) == "zabcdefghijklmnopqrstuvwza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [6, 6, 0], [7, 7, 0], [8, 8, 0], [9, 9, 0], [10, 10, 0], [11, 11, 0], [12, 12, 0], [13, 13, 0], [14, 14, 0], [15, 15, 0], [16, 16, 0], [17, 17, 0], [18, 18, 0], [19, 19, 0], [20, 20, 0], [21, 21, 0], [22, 22, 0], [23, 23, 0], [24, 24, 1], [25, 25, 1]]) == "zabcdefghijklmnopqrstuvwza": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1]]) == "bcdeffghijlmnopqstuvwwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1]]) == "bcdeffghijlmnopqstuvwwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [[0, 8, 1], [3, 7, 0], [2, 5, 1], [4, 10, 0], [1, 9, 1]]) == "qtrisbmmjnf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [[0, 8, 1], [3, 7, 0], [2, 5, 1], [4, 10, 0], [1, 9, 1]]) == "qtrisbmmjnf": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1], [20, 20, 1], [21, 21, 1], [22, 22, 1], [23, 23, 1], [24, 24, 1], [25, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1], [20, 20, 1], [21, 21, 1], [22, 22, 1], [23, 23, 1], [24, 24, 1], [25, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",shifts = [[0, 0, 0], [7, 7, 1], [2, 2, 1], [5, 5, 0], [3, 3, 1]]) == "zbdeeegi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",shifts = [[0, 0, 0], [7, 7, 1], [2, 2, 1], [5, 5, 0], [3, 3, 1]]) == "zbdeeegi": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",shifts = [[0, 0, 1], [0, 0, 0], [0, 0, 1], [0, 0, 0]]) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",shifts = [[0, 0, 1], [0, 0, 0], [0, 0, 1], [0, 0, 0]]) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 1]]) == "fghijklmnopqrstuvwxyzabcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 1]]) == "fghijklmnopqrstuvwxyzabcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",shifts = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0]]) == "zzabcdf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",shifts = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0]]) == "zzabcdf": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0]]) == "nmporq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0]]) == "nmporq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 4, 0], [5, 9, 1], [0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "aaccehhjjl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 4, 0], [5, 9, 1], [0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "aaccehhjjl": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 9, 1]]) == "bcbcfgfgjk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 9, 1]]) == "bcbcfgfgjk": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",shifts = [[0, 2, 1], [2, 4, 0], [4, 6, 1], [6, 8, 0], [8, 10, 1]]) == "njsritshpqj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",shifts = [[0, 2, 1], [2, 4, 0], [4, 6, 1], [6, 8, 0], [8, 10, 1]]) == "njsritshpqj": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",shifts = [[0, 9, 1], [10, 19, 0], [20, 25, 1], [0, 19, 0], [10, 25, 1], [0, 25, 0], [0, 25, 1]]) == "qwertyuiopzrcefgijkyzexdpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",shifts = [[0, 9, 1], [10, 19, 0], [20, 25, 1], [0, 19, 0], [10, 25, 1], [0, 25, 0], [0, 25, 1]]) == "qwertyuiopzrcefgijkyzexdpo": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",shifts = [[0, 3, 1], [4, 7, 0], [8, 11, 1], [0, 11, 1]]) == "ccccbbbbeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",shifts = [[0, 3, 1], [4, 7, 0], [8, 11, 1], [0, 11, 1]]) == "ccccbbbbeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",shifts = [[0, 51, 1], [0, 51, 0], [0, 51, 1], [0, 51, 0], [0, 51, 1]]) == "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",shifts = [[0, 51, 1], [0, 51, 0], [0, 51, 1], [0, 51, 0], [0, 51, 1]]) == "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 13, 0], [13, 25, 1], [0, 25, 0], [0, 25, 1]]) == "yxwvutsrqponmmmlkjihgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 13, 0], [13, 25, 1], [0, 25, 0], [0, 25, 1]]) == "yxwvutsrqponmmmlkjihgfedcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0], [0, 25, 0], [0, 25, 0], [0, 25, 0], [0, 25, 0]]) == "utsrqponmlkjihgfedcbazyxwv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0], [0, 25, 0], [0, 25, 0], [0, 25, 0], [0, 25, 0]]) == "utsrqponmlkjihgfedcbazyxwv": {e}')
    
    total += 1
    try:
        result = candidate(s = "shiftthis",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1]]) == "tgjeusiht"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "shiftthis",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1]]) == "tgjeusiht": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [[0, 3, 1], [0, 2, 0], [1, 3, 1], [1, 2, 0], [2, 3, 1]]) == "abdg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [[0, 3, 1], [0, 2, 0], [1, 3, 1], [1, 2, 0], [2, 3, 1]]) == "abdg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyza",shifts = [[0, 25, 1], [1, 24, 0], [2, 23, 1], [3, 22, 0]]) == "bbddefghijklmnopqrstuvwyyaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyza",shifts = [[0, 25, 1], [1, 24, 0], [2, 23, 1], [3, 22, 0]]) == "bbddefghijklmnopqrstuvwyyaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1], [20, 20, 1], [21, 21, 1], [22, 22, 1], [23, 23, 1], [24, 24, 0], [25, 25, 0]]) == "bcdefghijklmnopqrstuvwxyxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1], [20, 20, 1], [21, 21, 1], [22, 22, 1], [23, 23, 1], [24, 24, 0], [25, 25, 0]]) == "bcdefghijklmnopqrstuvwxyxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "python",shifts = [[0, 5, 1], [1, 4, 0], [2, 3, 1], [0, 5, 0], [1, 4, 1]]) == "pyuion"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",shifts = [[0, 5, 1], [1, 4, 0], [2, 3, 1], [0, 5, 0], [1, 4, 1]]) == "pyuion": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0]]) == "badcfehgji"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0]]) == "badcfehgji": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1]]) == "jjjjjjjjjj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1]]) == "jjjjjjjjjj": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",shifts = [[0, 2, 1], [3, 5, 0], [6, 8, 1], [0, 5, 1], [3, 8, 0], [0, 8, 1]]) == "abcxyzyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",shifts = [[0, 2, 1], [3, 5, 0], [6, 8, 1], [0, 5, 1], [3, 8, 0], [0, 8, 1]]) == "abcxyzyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb",shifts = [[0, 3, 1], [4, 7, 0], [2, 5, 1], [1, 6, 0]]) == "babbaaza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb",shifts = [[0, 3, 1], [4, 7, 0], [2, 5, 1], [1, 6, 0]]) == "babbaaza": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzz",shifts = [[0, 7, 1], [1, 6, 0], [2, 5, 1], [3, 4, 0]]) == "azazzaza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzz",shifts = [[0, 7, 1], [1, 6, 0], [2, 5, 1], [3, 4, 0]]) == "azazzaza": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [[0, 4, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "bbddfffhhj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [[0, 4, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "bbddfffhhj": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",shifts = [[0, 3, 1], [4, 7, 0], [8, 11, 1], [0, 11, 0], [0, 11, 1]]) == "bcdezabcbcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",shifts = [[0, 3, 1], [4, 7, 0], [8, 11, 1], [0, 11, 0], [0, 11, 1]]) == "bcdezabcbcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 0], [1, 24, 0], [2, 23, 0], [3, 22, 0], [4, 21, 0], [5, 20, 0], [6, 19, 0], [7, 18, 0], [8, 17, 0], [9, 16, 0], [10, 15, 0], [11, 14, 0], [12, 13, 0], [13, 12, 1], [14, 11, 1], [15, 10, 1], [16, 9, 1], [17, 8, 1], [18, 7, 1], [19, 6, 1], [20, 5, 1], [21, 4, 1], [22, 3, 1], [23, 2, 1], [24, 1, 1], [25, 0, 1]]) == "zyxwvutsrqponoruxadgjmpsvy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 0], [1, 24, 0], [2, 23, 0], [3, 22, 0], [4, 21, 0], [5, 20, 0], [6, 19, 0], [7, 18, 0], [8, 17, 0], [9, 16, 0], [10, 15, 0], [11, 14, 0], [12, 13, 0], [13, 12, 1], [14, 11, 1], [15, 10, 1], [16, 9, 1], [17, 8, 1], [18, 7, 1], [19, 6, 1], [20, 5, 1], [21, 4, 1], [22, 3, 1], [23, 2, 1], [24, 1, 1], [25, 0, 1]]) == "zyxwvutsrqponoruxadgjmpsvy": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [0, 9, 0], [1, 8, 1], [1, 8, 0], [2, 7, 1], [2, 7, 0], [3, 6, 1], [3, 6, 0], [4, 5, 1], [4, 5, 0]]) == "zzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [0, 9, 0], [1, 8, 1], [1, 8, 0], [2, 7, 1], [2, 7, 0], [3, 6, 1], [3, 6, 0], [4, 5, 1], [4, 5, 0]]) == "zzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0], [10, 10, 1], [11, 11, 0], [12, 12, 1], [13, 13, 0], [14, 14, 1], [15, 15, 0], [16, 16, 1], [17, 17, 0], [18, 18, 1], [19, 19, 0], [20, 20, 1], [21, 21, 0], [22, 22, 1], [23, 23, 0], [24, 24, 1], [25, 25, 0]]) == "badcfehgjilknmporqtsvuxwzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0], [10, 10, 1], [11, 11, 0], [12, 12, 1], [13, 13, 0], [14, 14, 1], [15, 15, 0], [16, 16, 1], [17, 17, 0], [18, 18, 1], [19, 19, 0], [20, 20, 1], [21, 21, 0], [22, 22, 1], [23, 23, 0], [24, 24, 1], [25, 25, 0]]) == "badcfehgjilknmporqtsvuxwzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",shifts = [[0, 2, 1], [3, 5, 0], [1, 4, 1], [2, 5, 0], [0, 5, 1]]) == "zbbabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",shifts = [[0, 2, 1], [3, 5, 0], [1, 4, 1], [2, 5, 0], [0, 5, 1]]) == "zbbabb": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [[0, 3, 1], [4, 8, 0], [6, 10, 1], [7, 9, 0], [1, 5, 1]]) == "qtqiramlhnh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [[0, 3, 1], [4, 8, 0], [6, 10, 1], [7, 9, 0], [1, 5, 1]]) == "qtqiramlhnh": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "world",shifts = [[0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0]]) == "sknhz"
    assert candidate(s = "abc",shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"
    assert candidate(s = "xyz",shifts = [[0, 2, 0]]) == "wxy"
    assert candidate(s = "abcdef",shifts = [[1, 4, 1], [2, 3, 0]]) == "accdff"
    assert candidate(s = "aaa",shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 1]]) == "ddd"
    assert candidate(s = "hello",shifts = [[0, 4, 1], [1, 3, 0]]) == "iellp"
    assert candidate(s = "hello",shifts = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]]) == "ignnp"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza"
    assert candidate(s = "dztz",shifts = [[0, 0, 0], [1, 1, 1]]) == "catz"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0]]) == "yxwvutsrqponmlkjihgfedcbaz"
    assert candidate(s = "a",shifts = [[0, 0, 1], [0, 0, 0]]) == "a"
    assert candidate(s = "abcd",shifts = [[0, 3, 1], [1, 2, 0], [2, 3, 1]]) == "bbdf"
    assert candidate(s = "zzz",shifts = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]) == "www"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 0]]) == "zabcdefghijklmnopqrstuvwxy"
    assert candidate(s = "hello",shifts = [[0, 4, 1]]) == "ifmmp"
    assert candidate(s = "zzzzzzzzzz",shifts = [[0, 4, 0], [5, 9, 1], [0, 9, 1], [3, 6, 0]]) == "zzzyyaabbb"
    assert candidate(s = "alphabet",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [5, 5, 1]]) == "bkqgbbet"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [5, 10, 0], [15, 20, 1]]) == "bcdeffghijkmnoprstuvwwxyza"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",shifts = [[0, 51, 1], [10, 40, 0], [20, 30, 1], [30, 40, 0]]) == "bbccddeeffffgghhiijjllmmnnoopppoppqqrrsstvwwxxyyzzaa"
    assert candidate(s = "abacax",shifts = [[0, 5, 1], [1, 4, 0], [2, 3, 1], [0, 5, 0]]) == "aaaczx"
    assert candidate(s = "programming",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0]]) == "qrpgsanmjng"
    assert candidate(s = "abcdefghij",shifts = [[0, 9, 0], [1, 8, 1], [2, 7, 0], [3, 6, 1], [4, 5, 0]]) == "zbbddeggii"
    assert candidate(s = "mnopqrstuvwxyzabcdefghijkl",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1], [15, 25, 0]]) == "nopqrrstuvxyzabbdefghhijkl"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 0]]) == "cdefghijklmnopqrstuvwxyzab"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 0], [0, 25, 1], [0, 25, 0]]) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "abababab",shifts = [[0, 7, 1], [1, 6, 0], [2, 5, 1], [3, 4, 0]]) == "bbbbacac"
    assert candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [2, 8, 0], [4, 6, 1]]) == "aazzaaazza"
    assert candidate(s = "algorithm",shifts = [[0, 2, 1], [3, 5, 0], [6, 8, 1], [1, 4, 0], [2, 3, 1], [5, 7, 0], [7, 8, 1]]) == "blhnpgtio"
    assert candidate(s = "abcdefghij",shifts = [[0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0]]) == "abcdefghij"
    assert candidate(s = "codingame",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 8, 1], [0, 8, 0], [0, 8, 1], [0, 8, 0], [0, 8, 1]]) == "dpchohzlf"
    assert candidate(s = "abacabadabacaba",shifts = [[0, 14, 1], [1, 13, 0], [2, 12, 1], [3, 11, 0], [4, 10, 1], [5, 9, 0]]) == "bbbcbbadabbcbbb"
    assert candidate(s = "abcdefghij",shifts = [[0, 4, 1], [5, 9, 0], [0, 4, 0], [5, 9, 1], [0, 9, 1]]) == "bcdefghijk"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [1, 24, 0], [2, 23, 1], [3, 22, 0], [4, 21, 1]]) == "bbddfghijklmnopqrstuvwwyya"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0], [5, 10, 1], [15, 20, 0]]) == "yxwvuutsrqpnmlkihgfeddcbaz"
    assert candidate(s = "zzzzz",shifts = [[0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 1]]) == "wwwww"
    assert candidate(s = "abcdefghij",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "bbddfggiik"
    assert candidate(s = "abcdefghij",shifts = [[0, 9, 1], [0, 9, 0], [0, 9, 1], [0, 9, 0], [0, 9, 1]]) == "bcdefghijk"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1]]) == "aaaaazzzzzaaaaaabbbbbaaaaa"
    assert candidate(s = "abcdefghijklmnop",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1]]) == "bcdefghijklmnopq"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 12, 1], [13, 25, 0], [0, 25, 1], [0, 25, 0], [0, 25, 1]]) == "cdefghijklmnonopqrstuvwxyz"
    assert candidate(s = "alibabacloud",shifts = [[0, 9, 1], [2, 4, 0], [5, 7, 1], [8, 11, 0], [0, 3, 1], [6, 9, 0], [1, 8, 1], [2, 7, 0]]) == "cojcadbdlntc"
    assert candidate(s = "xyz",shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 0], [0, 2, 0]]) == "xyz"
    assert candidate(s = "abcdefg",shifts = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1]]) == "bdefghh"
    assert candidate(s = "abacabadabacaba",shifts = [[0, 4, 1], [5, 9, 0], [10, 14, 1], [0, 14, 0], [0, 14, 1]]) == "bcbdbazczabdbcb"
    assert candidate(s = "hello world",shifts = [[0, 4, 1], [6, 10, 0], [3, 8, 1], [1, 9, 0], [0, 10, 1]]) == "jfmnqoworkd"
    assert candidate(s = "example",shifts = [[0, 6, 1], [1, 5, 0], [2, 4, 1], [3, 6, 0]]) == "fxbmpke"
    assert candidate(s = "abcdefghij",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 4, 0], [6, 3, 1], [7, 2, 0], [8, 1, 1], [9, 0, 0]]) == "bcdefghijk"
    assert candidate(s = "abcdefg",shifts = [[0, 6, 1], [1, 5, 0], [2, 4, 1], [3, 3, 0]]) == "bbddffh"
    assert candidate(s = "hellozworld",shifts = [[0, 4, 1], [5, 9, 0], [6, 10, 1], [7, 8, 0], [9, 10, 1], [10, 10, 0]]) == "ifmmpywnqme"
    assert candidate(s = "abcde",shifts = [[0, 2, 1], [3, 4, 0], [1, 3, 1], [0, 1, 0], [4, 4, 1], [2, 2, 0]]) == "acdde"
    assert candidate(s = "xylophone",shifts = [[0, 8, 1], [1, 7, 0], [2, 6, 1], [3, 5, 0], [4, 4, 1]]) == "yymoqhpnf"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 0], [0, 25, 1], [0, 25, 0], [0, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza"
    assert candidate(s = "programming",shifts = [[0, 9, 1], [4, 8, 0], [2, 6, 1], [1, 7, 0], [0, 8, 1]]) == "rsqisbnmjog"
    assert candidate(s = "shiftmeplease",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 9, 1], [10, 11, 0], [12, 12, 1]]) == "tiheundomfzrf"
    assert candidate(s = "algorithms",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1], [5, 4, 0], [6, 3, 1], [7, 2, 0], [8, 1, 1], [9, 0, 0]]) == "bmhpsjuint"
    assert candidate(s = "quickbrownfox",shifts = [[0, 12, 1], [1, 11, 0], [2, 10, 1], [3, 9, 0], [4, 8, 1], [5, 7, 0]]) == "rujclbroxngoy"
    assert candidate(s = "mnopqr",shifts = [[0, 2, 1], [3, 5, 0], [0, 5, 1], [1, 4, 0]]) == "oopopr"
    assert candidate(s = "abcdefghijklmnop",shifts = [[0, 15, 1], [1, 14, 0], [2, 13, 1], [3, 12, 0], [4, 11, 1], [5, 10, 0], [6, 9, 1], [7, 8, 0]]) == "bbddffhhikkmmooq"
    assert candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "azazaazaza"
    assert candidate(s = "mississippi",shifts = [[0, 4, 0], [1, 3, 1], [2, 2, 0], [3, 5, 1], [6, 8, 0], [7, 7, 1], [8, 10, 0], [9, 9, 1], [10, 10, 0]]) == "lirtitrinpg"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [6, 6, 0], [7, 7, 0], [8, 8, 0], [9, 9, 0], [10, 10, 0], [11, 11, 0], [12, 12, 0], [13, 13, 0], [14, 14, 0], [15, 15, 0], [16, 16, 0], [17, 17, 0], [18, 18, 0], [19, 19, 0], [20, 20, 0], [21, 21, 0], [22, 22, 0], [23, 23, 0], [24, 24, 1], [25, 25, 1]]) == "zabcdefghijklmnopqrstuvwza"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [5, 15, 0], [10, 20, 1]]) == "bcdeffghijlmnopqstuvwwxyza"
    assert candidate(s = "programming",shifts = [[0, 8, 1], [3, 7, 0], [2, 5, 1], [4, 10, 0], [1, 9, 1]]) == "qtrisbmmjnf"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1], [20, 20, 1], [21, 21, 1], [22, 22, 1], [23, 23, 1], [24, 24, 1], [25, 25, 1]]) == "bcdefghijklmnopqrstuvwxyza"
    assert candidate(s = "abcdefgh",shifts = [[0, 0, 0], [7, 7, 1], [2, 2, 1], [5, 5, 0], [3, 3, 1]]) == "zbdeeegi"
    assert candidate(s = "a",shifts = [[0, 0, 1], [0, 0, 0], [0, 0, 1], [0, 0, 0]]) == "a"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 1], [0, 25, 1]]) == "fghijklmnopqrstuvwxyzabcde"
    assert candidate(s = "abcdefg",shifts = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0]]) == "zzabcdf"
    assert candidate(s = "mnopqr",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0]]) == "nmporq"
    assert candidate(s = "abcdefghij",shifts = [[0, 4, 0], [5, 9, 1], [0, 9, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "aaccehhjjl"
    assert candidate(s = "abcdefghij",shifts = [[0, 1, 1], [2, 3, 0], [4, 5, 1], [6, 7, 0], [8, 9, 1]]) == "bcbcfgfgjk"
    assert candidate(s = "mississippi",shifts = [[0, 2, 1], [2, 4, 0], [4, 6, 1], [6, 8, 0], [8, 10, 1]]) == "njsritshpqj"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",shifts = [[0, 9, 1], [10, 19, 0], [20, 25, 1], [0, 19, 0], [10, 25, 1], [0, 25, 0], [0, 25, 1]]) == "qwertyuiopzrcefgijkyzexdpo"
    assert candidate(s = "aaaabbbbcccc",shifts = [[0, 3, 1], [4, 7, 0], [8, 11, 1], [0, 11, 1]]) == "ccccbbbbeeee"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",shifts = [[0, 51, 1], [0, 51, 0], [0, 51, 1], [0, 51, 0], [0, 51, 1]]) == "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 13, 0], [13, 25, 1], [0, 25, 0], [0, 25, 1]]) == "yxwvutsrqponmmmlkjihgfedcb"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [[0, 25, 0], [0, 25, 0], [0, 25, 0], [0, 25, 0], [0, 25, 0]]) == "utsrqponmlkjihgfedcbazyxwv"
    assert candidate(s = "shiftthis",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1]]) == "tgjeusiht"
    assert candidate(s = "abcd",shifts = [[0, 3, 1], [0, 2, 0], [1, 3, 1], [1, 2, 0], [2, 3, 1]]) == "abdg"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyza",shifts = [[0, 25, 1], [1, 24, 0], [2, 23, 1], [3, 22, 0]]) == "bbddefghijklmnopqrstuvwyyaa"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1], [20, 20, 1], [21, 21, 1], [22, 22, 1], [23, 23, 1], [24, 24, 0], [25, 25, 0]]) == "bcdefghijklmnopqrstuvwxyxy"
    assert candidate(s = "python",shifts = [[0, 5, 1], [1, 4, 0], [2, 3, 1], [0, 5, 0], [1, 4, 1]]) == "pyuion"
    assert candidate(s = "abcdefghij",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0]]) == "badcfehgji"
    assert candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1], [0, 9, 1]]) == "jjjjjjjjjj"
    assert candidate(s = "xyzxyzxyz",shifts = [[0, 2, 1], [3, 5, 0], [6, 8, 1], [0, 5, 1], [3, 8, 0], [0, 8, 1]]) == "abcxyzyza"
    assert candidate(s = "aaaabbbb",shifts = [[0, 3, 1], [4, 7, 0], [2, 5, 1], [1, 6, 0]]) == "babbaaza"
    assert candidate(s = "zzzzzzzz",shifts = [[0, 7, 1], [1, 6, 0], [2, 5, 1], [3, 4, 0]]) == "azazzaza"
    assert candidate(s = "abcdefghij",shifts = [[0, 4, 1], [1, 8, 0], [2, 7, 1], [3, 6, 0], [4, 5, 1]]) == "bbddfffhhj"
    assert candidate(s = "abcdabcdabcd",shifts = [[0, 3, 1], [4, 7, 0], [8, 11, 1], [0, 11, 0], [0, 11, 1]]) == "bcdezabcbcde"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 25, 0], [1, 24, 0], [2, 23, 0], [3, 22, 0], [4, 21, 0], [5, 20, 0], [6, 19, 0], [7, 18, 0], [8, 17, 0], [9, 16, 0], [10, 15, 0], [11, 14, 0], [12, 13, 0], [13, 12, 1], [14, 11, 1], [15, 10, 1], [16, 9, 1], [17, 8, 1], [18, 7, 1], [19, 6, 1], [20, 5, 1], [21, 4, 1], [22, 3, 1], [23, 2, 1], [24, 1, 1], [25, 0, 1]]) == "zyxwvutsrqponoruxadgjmpsvy"
    assert candidate(s = "zzzzzzzzzz",shifts = [[0, 9, 1], [0, 9, 0], [1, 8, 1], [1, 8, 0], [2, 7, 1], [2, 7, 0], [3, 6, 1], [3, 6, 0], [4, 5, 1], [4, 5, 0]]) == "zzzzzzzzzz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0], [10, 10, 1], [11, 11, 0], [12, 12, 1], [13, 13, 0], [14, 14, 1], [15, 15, 0], [16, 16, 1], [17, 17, 0], [18, 18, 1], [19, 19, 0], [20, 20, 1], [21, 21, 0], [22, 22, 1], [23, 23, 0], [24, 24, 1], [25, 25, 0]]) == "badcfehgjilknmporqtsvuxwzy"
    assert candidate(s = "xyzabc",shifts = [[0, 2, 1], [3, 5, 0], [1, 4, 1], [2, 5, 0], [0, 5, 1]]) == "zbbabb"
    assert candidate(s = "programming",shifts = [[0, 3, 1], [4, 8, 0], [6, 10, 1], [7, 9, 0], [1, 5, 1]]) == "qtqiramlhnh"


