def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aaa",shifts = [1, 2, 3]) == "gfd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",shifts = [1, 2, 3]) == "gfd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",shifts = [26, 52, 78]) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",shifts = [26, 52, 78]) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",shifts = [25]) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",shifts = [25]) == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",shifts = [0, 0, 0, 0, 0, 0]) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",shifts = [0, 0, 0, 0, 0, 0]) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [10, 20, 30, 40]) == "wnur"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [10, 20, 30, 40]) == "wnur": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == "nnmkhdysldukznamxhqyflquxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == "nnmkhdysldukznamxhqyflquxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",shifts = [1, 2, 3, 4, 5, 6]) == "vvuspl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",shifts = [1, 2, 3, 4, 5, 6]) == "vvuspl": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [0, 0, 0, 0]) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [0, 0, 0, 0]) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",shifts = [3, 5, 9]) == "rpl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",shifts = [3, 5, 9]) == "rpl": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",shifts = [1000000000, 1000000000, 1000000000]) == "kym"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",shifts = [1000000000, 1000000000, 1000000000]) == "kym": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",shifts = [1000000000]) == "m"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",shifts = [1000000000]) == "m": {e}')
    
    total += 1
    try:
        result = candidate(s = "z",shifts = [1]) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z",shifts = [1]) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",shifts = [1000000000, 1000000000, 1000000000]) == "jxl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",shifts = [1000000000, 1000000000, 1000000000]) == "jxl": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",shifts = [1, 2, 3]) == "ddc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",shifts = [1, 2, 3]) == "ddc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",shifts = [1, 1, 1, 1, 1, 1]) == "gggggg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",shifts = [1, 1, 1, 1, 1, 1]) == "gggggg": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",shifts = [1000000000, 1000000000, 1000000000]) == "jxl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",shifts = [1000000000, 1000000000, 1000000000]) == "jxl": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [1, 1, 1, 1]) == "eeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [1, 1, 1, 1]) == "eeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "qzcvxnbtrslkjhgf",shifts = [97, 86, 75, 64, 53, 42, 31, 20, 9, 8, 7, 6, 5, 4, 3, 2]) == "iytpfusfjbmexqlh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qzcvxnbtrslkjhgf",shifts = [97, 86, 75, 64, 53, 42, 31, 20, 9, 8, 7, 6, 5, 4, 3, 2]) == "iytpfusfjbmexqlh": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",shifts = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]) == "ipvafiklmljg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",shifts = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]) == "ipvafiklmljg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",shifts = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == "ssrmmlggf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",shifts = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == "ssrmmlggf": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "programming": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500]) == "etozspob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500]) == "etozspob": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [5, 5, 5, 5, 5]) == "gyavt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [5, 5, 5, 5, 5]) == "gyavt": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [25, 24, 23, 22]) == "qsvz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [25, 24, 23, 22]) == "qsvz": {e}')
    
    total += 1
    try:
        result = candidate(s = "python",shifts = [97, 97, 97, 97, 97, 97]) == "zprmag"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",shifts = [97, 97, 97, 97, 97, 97]) == "zprmag": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [25, 98, 23, 56, 78]) == "bzmpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [25, 98, 23, 56, 78]) == "bzmpo": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",shifts = [26, 52, 78]) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",shifts = [26, 52, 78]) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "rollingupdates",shifts = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == "ybfntimmuwirtz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rollingupdates",shifts = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == "ybfntimmuwirtz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",shifts = [26, 52, 78]) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",shifts = [26, 52, 78]) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "python",shifts = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555]) == "mjtdnw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",shifts = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555]) == "mjtdnw": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == "ghbosstgnbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == "ghbosstgnbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",shifts = [3, 2, 1, 0, 5, 4]) == "mkjjkg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",shifts = [3, 2, 1, 0, 5, 4]) == "mkjjkg": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",shifts = [9, 8, 7, 6, 5, 4, 3, 2]) == "sjcvqlif"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",shifts = [9, 8, 7, 6, 5, 4, 3, 2]) == "sjcvqlif": {e}')
    
    total += 1
    try:
        result = candidate(s = "python",shifts = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == "iutmzf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",shifts = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == "iutmzf": {e}')
    
    total += 1
    try:
        result = candidate(s = "qponmlkjihgfedcba",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "ttuwzdiovdmwhtguj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qponmlkjihgfedcba",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "ttuwzdiovdmwhtguj": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstring",shifts = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == "enhgjcrpvdzxjnfkcljtl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstring",shifts = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == "enhgjcrpvdzxjnfkcljtl": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",shifts = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000]) == "sxgtkfe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",shifts = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000]) == "sxgtkfe": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",shifts = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == "eedbuutrkkjh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",shifts = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == "eedbuutrkkjh": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "cbzwsnhasj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "cbzwsnhasj": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",shifts = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555]) == "wkzvyi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",shifts = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555]) == "wkzvyi": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",shifts = [0]) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",shifts = [0]) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 100000000]) == "ynjmwnlqcv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 100000000]) == "ynjmwnlqcv": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",shifts = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000, 11000000000, 12000000000, 13000000000, 14000000000, 15000000000, 16000000000]) == "ujmdibidmjutghwz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",shifts = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000, 11000000000, 12000000000, 13000000000, 14000000000, 15000000000, 16000000000]) == "ujmdibidmjutghwz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000]) == "nblrtrlbnv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000]) == "nblrtrlbnv": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17]) == "egjkpvzhq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17]) == "egjkpvzhq": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [1, 2, 3, 4, 5]) == "wsxut"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [1, 2, 3, 4, 5]) == "wsxut": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",shifts = [1]) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",shifts = [1]) == "b": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",shifts = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000]) == "shkbgz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",shifts = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000]) == "shkbgz": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "herulvducoj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "herulvducoj": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",shifts = [25, 2, 3, 4, 5, 6]) == "qsrpmi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",shifts = [25, 2, 3, 4, 5, 6]) == "qsrpmi": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",shifts = [5, 10, 15, 20, 25]) == "xtkwd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",shifts = [5, 10, 15, 20, 25]) == "xtkwd": {e}')
    
    total += 1
    try:
        result = candidate(s = "shift",shifts = [97, 98, 99, 100, 101]) == "tpwyq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "shift",shifts = [97, 98, 99, 100, 101]) == "tpwyq": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",shifts = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == "nrzlbvtvbl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",shifts = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == "nrzlbvtvbl": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",shifts = [10, 20, 30, 40, 50]) == "bobxm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",shifts = [10, 20, 30, 40, 50]) == "bobxm": {e}')
    
    total += 1
    try:
        result = candidate(s = "testcase",shifts = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "lntnqjxg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testcase",shifts = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "lntnqjxg": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",shifts = [1000000000, 1000000000, 1]) == "wla"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",shifts = [1000000000, 1000000000, 1]) == "wla": {e}')
    
    total += 1
    try:
        result = candidate(s = "teststring",shifts = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930, 313233, 343536]) == "iaastjjpwe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "teststring",shifts = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930, 313233, 343536]) == "iaastjjpwe": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == "nnmkhdysldukznamxhqyflquxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == "nnmkhdysldukznamxhqyflquxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",shifts = [0, 0, 0, 0]) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",shifts = [0, 0, 0, 0]) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",shifts = [26, 52, 78, 104, 130, 156]) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",shifts = [26, 52, 78, 104, 130, 156]) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abz",shifts = [1, 1, 25]) == "bby"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abz",shifts = [1, 1, 25]) == "bby": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",shifts = [26, 25, 24, 23, 22, 21]) == "xyadhm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",shifts = [26, 25, 24, 23, 22, 21]) == "xyadhm": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == "noonlieztmevlaobnyirzgmrvy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == "noonlieztmevlaobnyirzgmrvy": {e}')
    
    total += 1
    try:
        result = candidate(s = "wraparound",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "ztamtfwvgn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wraparound",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "ztamtfwvgn": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothere",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == "almwrsengj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothere",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == "almwrsengj": {e}')
    
    total += 1
    try:
        result = candidate(s = "python",shifts = [25, 24, 23, 22, 21, 20]) == "uebsdh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",shifts = [25, 24, 23, 22, 21, 20]) == "uebsdh": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",shifts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "otcpgbadkv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",shifts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "otcpgbadkv": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzz",shifts = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == "rfthvjxl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzz",shifts = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == "rfthvjxl": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",shifts = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "zaplvubtzgnwgqsoshswtibkzr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",shifts = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "zaplvubtzgnwgqsoshswtibkzr": {e}')
    
    total += 1
    try:
        result = candidate(s = "z",shifts = [26]) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z",shifts = [26]) == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",shifts = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000, 50000000, 25000000]) == "ymxdgezpckpr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",shifts = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000, 50000000, 25000000]) == "ymxdgezpckpr": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb",shifts = [1, 2, 3, 4, 5, 6, 7, 8]) == "kjhebwqj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb",shifts = [1, 2, 3, 4, 5, 6, 7, 8]) == "kjhebwqj": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",shifts = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == "kowiytxfrh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",shifts = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == "kowiytxfrh": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "zxvtrpnljhfdbzxvtrpnljhfdb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "zxvtrpnljhfdbzxvtrpnljhfdb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",shifts = [1, 2, 3, 4, 5, 6, 7]) == "ccbzwsn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",shifts = [1, 2, 3, 4, 5, 6, 7]) == "ccbzwsn": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "npswbhowfpamzncsjbuojfcazz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "npswbhowfpamzncsjbuojfcazz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyz",shifts = [0, 1, 2, 25, 50, 75]) == "xyyrtw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyz",shifts = [0, 1, 2, 25, 50, 75]) == "xyyrtw": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "mmnpswbhowfpamzncsjbuojfca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "mmnpswbhowfpamzncsjbuojfca": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",shifts = [3, 2, 1, 0, 5, 4]) == "bzyyzv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",shifts = [3, 2, 1, 0, 5, 4]) == "bzyyzv": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",shifts = [25, 50, 75]) == "rtw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",shifts = [25, 50, 75]) == "rtw": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "npswbhowfpamzncsjbuojfcazz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "npswbhowfpamzncsjbuojfcazz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == "ixsdwt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == "ixsdwt": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140]) == "kartwblxzui"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140]) == "kartwblxzui": {e}')
    
    total += 1
    try:
        result = candidate(s = "qznooo",shifts = [987654321, 123456789, 987654321, 123456789, 987654321, 123456789]) == "skxhgp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qznooo",shifts = [987654321, 123456789, 987654321, 123456789, 987654321, 123456789]) == "skxhgp": {e}')
    
    total += 1
    try:
        result = candidate(s = "bxyz",shifts = [2, 3, 25, 1]) == "gaya"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bxyz",shifts = [2, 3, 25, 1]) == "gaya": {e}')
    
    total += 1
    try:
        result = candidate(s = "boundary",shifts = [26, 26, 26, 26, 26, 26, 26, 26]) == "boundary"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "boundary",shifts = [26, 26, 26, 26, 26, 26, 26, 26]) == "boundary": {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",shifts = [26, 52, 78, 104, 130, 156, 182, 208, 234, 260, 286]) == "programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",shifts = [26, 52, 78, 104, 130, 156, 182, 208, 234, 260, 286]) == "programming": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aaa",shifts = [1, 2, 3]) == "gfd"
    assert candidate(s = "abc",shifts = [26, 52, 78]) == "abc"
    assert candidate(s = "a",shifts = [25]) == "z"
    assert candidate(s = "abcdef",shifts = [0, 0, 0, 0, 0, 0]) == "abcdef"
    assert candidate(s = "abcd",shifts = [10, 20, 30, 40]) == "wnur"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == "nnmkhdysldukznamxhqyflquxz"
    assert candidate(s = "abcdef",shifts = [1, 2, 3, 4, 5, 6]) == "vvuspl"
    assert candidate(s = "abcd",shifts = [0, 0, 0, 0]) == "abcd"
    assert candidate(s = "abc",shifts = [3, 5, 9]) == "rpl"
    assert candidate(s = "aaa",shifts = [1000000000, 1000000000, 1000000000]) == "kym"
    assert candidate(s = "a",shifts = [1000000000]) == "m"
    assert candidate(s = "z",shifts = [1]) == "a"
    assert candidate(s = "zzz",shifts = [1000000000, 1000000000, 1000000000]) == "jxl"
    assert candidate(s = "xyz",shifts = [1, 2, 3]) == "ddc"
    assert candidate(s = "abcdef",shifts = [1, 1, 1, 1, 1, 1]) == "gggggg"
    assert candidate(s = "zzz",shifts = [1000000000, 1000000000, 1000000000]) == "jxl"
    assert candidate(s = "abcd",shifts = [1, 1, 1, 1]) == "eeee"
    assert candidate(s = "qzcvxnbtrslkjhgf",shifts = [97, 86, 75, 64, 53, 42, 31, 20, 9, 8, 7, 6, 5, 4, 3, 2]) == "iytpfusfjbmexqlh"
    assert candidate(s = "aaaabbbbcccc",shifts = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]) == "ipvafiklmljg"
    assert candidate(s = "abcabcabc",shifts = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == "ssrmmlggf"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "programming",shifts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "programming"
    assert candidate(s = "abcdefgh",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500]) == "etozspob"
    assert candidate(s = "hello",shifts = [5, 5, 5, 5, 5]) == "gyavt"
    assert candidate(s = "abcd",shifts = [25, 24, 23, 22]) == "qsvz"
    assert candidate(s = "python",shifts = [97, 97, 97, 97, 97, 97]) == "zprmag"
    assert candidate(s = "hello",shifts = [25, 98, 23, 56, 78]) == "bzmpo"
    assert candidate(s = "abc",shifts = [26, 52, 78]) == "abc"
    assert candidate(s = "rollingupdates",shifts = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == "ybfntimmuwirtz"
    assert candidate(s = "xyz",shifts = [26, 52, 78]) == "xyz"
    assert candidate(s = "python",shifts = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555]) == "mjtdnw"
    assert candidate(s = "programming",shifts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == "ghbosstgnbb"
    assert candidate(s = "xyzabc",shifts = [3, 2, 1, 0, 5, 4]) == "mkjjkg"
    assert candidate(s = "aabbccdd",shifts = [9, 8, 7, 6, 5, 4, 3, 2]) == "sjcvqlif"
    assert candidate(s = "python",shifts = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == "iutmzf"
    assert candidate(s = "qponmlkjihgfedcba",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "ttuwzdiovdmwhtguj"
    assert candidate(s = "thisisaverylongstring",shifts = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == "enhgjcrpvdzxjnfkcljtl"
    assert candidate(s = "abcdefg",shifts = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000]) == "sxgtkfe"
    assert candidate(s = "abcdabcdabcd",shifts = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == "eedbuutrkkjh"
    assert candidate(s = "zzzzzzzzzz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "cbzwsnhasj"
    assert candidate(s = "zzzzzz",shifts = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555]) == "wkzvyi"
    assert candidate(s = "a",shifts = [0]) == "a"
    assert candidate(s = "zzzzzzzzzz",shifts = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 100000000]) == "ynjmwnlqcv"
    assert candidate(s = "abcdefghijklmnop",shifts = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000, 11000000000, 12000000000, 13000000000, 14000000000, 15000000000, 16000000000]) == "ujmdibidmjutghwz"
    assert candidate(s = "zzzzzzzzzz",shifts = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000]) == "nblrtrlbnv"
    assert candidate(s = "xyzxyzxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17]) == "egjkpvzhq"
    assert candidate(s = "hello",shifts = [1, 2, 3, 4, 5]) == "wsxut"
    assert candidate(s = "a",shifts = [1]) == "b"
    assert candidate(s = "abcdef",shifts = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000]) == "shkbgz"
    assert candidate(s = "programming",shifts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "herulvducoj"
    assert candidate(s = "xyzabc",shifts = [25, 2, 3, 4, 5, 6]) == "qsrpmi"
    assert candidate(s = "abcde",shifts = [5, 10, 15, 20, 25]) == "xtkwd"
    assert candidate(s = "shift",shifts = [97, 98, 99, 100, 101]) == "tpwyq"
    assert candidate(s = "zzzzzzzzzz",shifts = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == "nrzlbvtvbl"
    assert candidate(s = "hello",shifts = [10, 20, 30, 40, 50]) == "bobxm"
    assert candidate(s = "testcase",shifts = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "lntnqjxg"
    assert candidate(s = "xyz",shifts = [1000000000, 1000000000, 1]) == "wla"
    assert candidate(s = "teststring",shifts = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930, 313233, 343536]) == "iaastjjpwe"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == "nnmkhdysldukznamxhqyflquxz"
    assert candidate(s = "abcd",shifts = [0, 0, 0, 0]) == "abcd"
    assert candidate(s = "abcdef",shifts = [26, 52, 78, 104, 130, 156]) == "abcdef"
    assert candidate(s = "abz",shifts = [1, 1, 25]) == "bby"
    assert candidate(s = "mnopqr",shifts = [26, 25, 24, 23, 22, 21]) == "xyadhm"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == "noonlieztmevlaobnyirzgmrvy"
    assert candidate(s = "wraparound",shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "ztamtfwvgn"
    assert candidate(s = "hellothere",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == "almwrsengj"
    assert candidate(s = "python",shifts = [25, 24, 23, 22, 21, 20]) == "uebsdh"
    assert candidate(s = "abcdefghij",shifts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "otcpgbadkv"
    assert candidate(s = "zzzzzzzz",shifts = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == "rfthvjxl"
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",shifts = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "zaplvubtzgnwgqsoshswtibkzr"
    assert candidate(s = "z",shifts = [26]) == "z"
    assert candidate(s = "aabbccddeeff",shifts = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000, 50000000, 25000000]) == "ymxdgezpckpr"
    assert candidate(s = "aaaabbbb",shifts = [1, 2, 3, 4, 5, 6, 7, 8]) == "kjhebwqj"
    assert candidate(s = "aaaaabbbbb",shifts = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == "kowiytxfrh"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "zxvtrpnljhfdbzxvtrpnljhfdb"
    assert candidate(s = "abcdefg",shifts = [1, 2, 3, 4, 5, 6, 7]) == "ccbzwsn"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "npswbhowfpamzncsjbuojfcazz"
    assert candidate(s = "abcxyz",shifts = [0, 1, 2, 25, 50, 75]) == "xyyrtw"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "mmnpswbhowfpamzncsjbuojfca"
    assert candidate(s = "mnopqr",shifts = [3, 2, 1, 0, 5, 4]) == "bzyyzv"
    assert candidate(s = "xyz",shifts = [25, 50, 75]) == "rtw"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",shifts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "npswbhowfpamzncsjbuojfcazz"
    assert candidate(s = "mnopqr",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == "ixsdwt"
    assert candidate(s = "programming",shifts = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140]) == "kartwblxzui"
    assert candidate(s = "qznooo",shifts = [987654321, 123456789, 987654321, 123456789, 987654321, 123456789]) == "skxhgp"
    assert candidate(s = "bxyz",shifts = [2, 3, 25, 1]) == "gaya"
    assert candidate(s = "boundary",shifts = [26, 26, 26, 26, 26, 26, 26, 26]) == "boundary"
    assert candidate(s = "programming",shifts = [26, 52, 78, 104, 130, 156, 182, 208, 234, 260, 286]) == "programming"


