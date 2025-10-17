def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 338: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",t = "qrpmno") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",t = "qrpmno") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "edbac") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "edbac") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyz",t = "xyzabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyz",t = "xyzabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuv",t = "vutsrq") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuv",t = "vutsrq") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",t = "bac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",t = "bac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",t = "rqponm") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",t = "rqponm") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "uvwxy",t = "yxuvw") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uvwxy",t = "yxuvw") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",t = "qrponm") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",t = "qrponm") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "dcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "dcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "zyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "zyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",t = "ba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",t = "ba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzabcdefghijkl",t = "qrstuvwxyzabcdefghijklmno") == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzabcdefghijkl",t = "qrstuvwxyzabcdefghijklmno") == 154: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdpqrs",t = "srqpdcba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdpqrs",t = "srqpdcba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "qazwsxedcrfvtgbyhnujmiklop",t = "plokmijnuhbygvtfcrdxeszwaq") == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qazwsxedcrfvtgbyhnujmiklop",t = "plokmijnuhbygvtfcrdxeszwaq") == 338: {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcba",t = "abcdef") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcba",t = "abcdef") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjhgfedcba",t = "abcdefghjkl") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjhgfedcba",t = "abcdefghjkl") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "gfedcba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "gfedcba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdfghijklmnopqrstuvwxyzef",t = "efghijklmnopqrstuvwxyzabcd") == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdfghijklmnopqrstuvwxyzef",t = "efghijklmnopqrstuvwxyzabcd") == 198: {e}')
    
    total += 1
    try:
        result = candidate(s = "lmnopqrstuvwxy",t = "yxwvutsrqponml") == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lmnopqrstuvwxy",t = "yxwvutsrqponml") == 98: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstu",t = "tusrqpmon") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstu",t = "tusrqpmon") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "ijklmnopqr",t = "rqponmlkji") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ijklmnopqr",t = "rqponmlkji") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijl",t = "ljihgfedcba") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijl",t = "ljihgfedcba") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "hijklmnop",t = "ponmlkjih") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hijklmnop",t = "ponmlkjih") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "qzjrwbyfc",t = "bfywzcrjq") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qzjrwbyfc",t = "bfywzcrjq") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "wvutsrqponmlkjihgfedcbazyx") == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "wvutsrqponmlkjihgfedcbazyx") == 338: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop",t = "ponmlkjihgfedcba") == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop",t = "ponmlkjihgfedcba") == 128: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "ghijabcdfe") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "ghijabcdfe") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "kjihgfedcba") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "kjihgfedcba") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabcdefghijklmnopqrstuvwxy",t = "yzxwvutsrqponmlkjihgfedcba") == 314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabcdefghijklmnopqrstuvwxy",t = "yzxwvutsrqponmlkjihgfedcba") == 314: {e}')
    
    total += 1
    try:
        result = candidate(s = "jklmnopqrabcdefghistuvwxy",t = "tuvxyabcdefghistuvwklmnoj") == 267
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jklmnopqrabcdefghistuvwxy",t = "tuvxyabcdefghistuvwklmnoj") == 267: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jabcdefghi") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jabcdefghi") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuv",t = "vutsrqp") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuv",t = "vutsrqp") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "vwxyzabcdefghijklmnopqrst",t = "rstqponmlkjihgfedcbazyxwv") == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vwxyzabcdefghijklmnopqrst",t = "rstqponmlkjihgfedcbazyxwv") == 312: {e}')
    
    total += 1
    try:
        result = candidate(s = "asdfghjkl",t = "lkjhgfdsa") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "asdfghjkl",t = "lkjhgfdsa") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "ihgfedcbaj") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "ihgfedcbaj") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "fedcba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "fedcba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuvw",t = "vutsrqwp") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuvw",t = "vutsrqwp") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "fedcbaghijk") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "fedcbaghijk") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyza") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyza") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "vutsrqponmlkjihgfedcbazyxw") == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "vutsrqponmlkjihgfedcbazyxw") == 312: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrown",t = "nkbrohwiqctue") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrown",t = "nkbrohwiqctue") == 82: {e}')
    
    total += 1
    try:
        result = candidate(s = "lmnopqrt",t = "tqrponml") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lmnopqrt",t = "tqrponml") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkmnopqrstuvwxyzl",t = "lmnopqrstuvwxyzabcdefghijk") == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkmnopqrstuvwxyzl",t = "lmnopqrstuvwxyzabcdefghijk") == 330: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzuvw",t = "uvwzyx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzuvw",t = "uvwzyx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghilmnopqrstuvwxyzjk",t = "jklmnopqrstuvwxyzabcdefghi") == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghilmnopqrstuvwxyzjk",t = "jklmnopqrstuvwxyzabcdefghi") == 306: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",t = "cba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",t = "cba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkmnopqrstvuwxyz",t = "xyzuvwtpqrsmnkjihgfedcba") == 297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkmnopqrstvuwxyz",t = "xyzuvwtpqrsmnkjihgfedcba") == 297: {e}')
    
    total += 1
    try:
        result = candidate(s = "acdefghijklmnopqrstuvwxyzb",t = "bzabcdefghijklmnopqrstuvwxy") == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acdefghijklmnopqrstuvwxyzb",t = "bzabcdefghijklmnopqrstuvwxy") == 141: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "qpjohuxivtnrckdsmgflweazyb") == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "qpjohuxivtnrckdsmgflweazyb") == 246: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdxyz",t = "zyxcba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdxyz",t = "zyxcba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "qrstuvwxyabcdefghijklmnop") == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "qrstuvwxyabcdefghijklmnop") == 288: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkmnopqrstuvwxyzl",t = "lnopqrstuvwxyzabcdefghijkml") == 337
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkmnopqrstuvwxyzl",t = "lnopqrstuvwxyzabcdefghijkml") == 337: {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuv",t = "tvusqr") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuv",t = "tvusqr") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "kabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "kabcdefghij") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "rplumabc",t = "mucrlpba") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rplumabc",t = "mucrlpba") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzabcde",t = "edcbamnopqrstuvwxyz") == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzabcde",t = "edcbamnopqrstuvwxyz") == 140: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouy",t = "uyioea") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouy",t = "uyioea") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bacdefghijklmnopqrstuvwxyza") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bacdefghijklmnopqrstuvwxyza") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxy",t = "yxwvutsrqponmlkjihgfedcba") == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxy",t = "yxwvutsrqponmlkjihgfedcba") == 312: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnm",t = "mnbvcxz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnm",t = "mnbvcxz") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjhgfdsapoiuytrewqmnbvcxz",t = "xcvbnmqwertypoiuytsdfghjkl") == 318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjhgfdsapoiuytrewqmnbvcxz",t = "xcvbnmqwertypoiuytsdfghjkl") == 318: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyz",t = "zzzyyx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyz",t = "zzzyyx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "stuvwxabcdefghijklmnopqrzy") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "stuvwxabcdefghijklmnopqrzy") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "ijhgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "ijhgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq") == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq") == 338: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcazdefghijklmnopqrstuvwxy") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcazdefghijklmnopqrstuvwxy") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "tuvrstxyzwqpomnlkjihgfedcba",t = "cabfedghijklmnopqrstuvwxyz") == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tuvrstxyzwqpomnlkjihgfedcba",t = "cabfedghijklmnopqrstuvwxyz") == 338: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcxyz",t = "zyxcba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcxyz",t = "zyxcba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiop",t = "poiuytrewq") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiop",t = "poiuytrewq") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "kijhgfedcba") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "kijhgfedcba") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijlm",t = "mljihgfedcba") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijlm",t = "mljihgfedcba") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstu",t = "ustqrpmno") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstu",t = "ustqrpmno") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "hgfedcba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "hgfedcba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "qrstuvw",t = "tuvwsrq") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrstuvw",t = "tuvwsrq") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklm",t = "mlkjihgfedcba") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklm",t = "mlkjihgfedcba") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghij") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghij") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ghijklmn",t = "nmlkjihg") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ghijklmn",t = "nmlkjihg") == 32: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 338
    assert candidate(s = "mnopqr",t = "qrpmno") == 18
    assert candidate(s = "abcde",t = "edbac") == 12
    assert candidate(s = "abcxyz",t = "xyzabc") == 18
    assert candidate(s = "qrstuv",t = "vutsrq") == 18
    assert candidate(s = "abc",t = "bac") == 2
    assert candidate(s = "mnopqr",t = "rqponm") == 18
    assert candidate(s = "uvwxy",t = "yxuvw") == 12
    assert candidate(s = "mnopqr",t = "qrponm") == 18
    assert candidate(s = "a",t = "a") == 0
    assert candidate(s = "abcd",t = "dcba") == 8
    assert candidate(s = "xyz",t = "zyx") == 4
    assert candidate(s = "ab",t = "ba") == 2
    assert candidate(s = "mnopqrstuvwxyzabcdefghijkl",t = "qrstuvwxyzabcdefghijklmno") == 154
    assert candidate(s = "abcdpqrs",t = "srqpdcba") == 32
    assert candidate(s = "qazwsxedcrfvtgbyhnujmiklop",t = "plokmijnuhbygvtfcrdxeszwaq") == 338
    assert candidate(s = "fedcba",t = "abcdef") == 18
    assert candidate(s = "lkjhgfedcba",t = "abcdefghjkl") == 60
    assert candidate(s = "abcdefg",t = "gfedcba") == 24
    assert candidate(s = "abcdfghijklmnopqrstuvwxyzef",t = "efghijklmnopqrstuvwxyzabcd") == 198
    assert candidate(s = "lmnopqrstuvwxy",t = "yxwvutsrqponml") == 98
    assert candidate(s = "mnopqrstu",t = "tusrqpmon") == 40
    assert candidate(s = "ijklmnopqr",t = "rqponmlkji") == 50
    assert candidate(s = "abcdefghijl",t = "ljihgfedcba") == 60
    assert candidate(s = "hijklmnop",t = "ponmlkjih") == 40
    assert candidate(s = "qzjrwbyfc",t = "bfywzcrjq") == 38
    assert candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "wvutsrqponmlkjihgfedcbazyx") == 338
    assert candidate(s = "abcdefghijklmnop",t = "ponmlkjihgfedcba") == 128
    assert candidate(s = "abcdefghij",t = "ghijabcdfe") == 48
    assert candidate(s = "abcdefghijk",t = "kjihgfedcba") == 60
    assert candidate(s = "zabcdefghijklmnopqrstuvwxy",t = "yzxwvutsrqponmlkjihgfedcba") == 314
    assert candidate(s = "jklmnopqrabcdefghistuvwxy",t = "tuvxyabcdefghistuvwklmnoj") == 267
    assert candidate(s = "abcdefghij",t = "jabcdefghi") == 18
    assert candidate(s = "pqrstuv",t = "vutsrqp") == 24
    assert candidate(s = "vwxyzabcdefghijklmnopqrst",t = "rstqponmlkjihgfedcbazyxwv") == 312
    assert candidate(s = "asdfghjkl",t = "lkjhgfdsa") == 40
    assert candidate(s = "abcdefghij",t = "ihgfedcbaj") == 40
    assert candidate(s = "abcdefghij",t = "jihgfedcba") == 50
    assert candidate(s = "abcdef",t = "fedcba") == 18
    assert candidate(s = "pqrstuvw",t = "vutsrqwp") == 26
    assert candidate(s = "abcdefghijk",t = "fedcbaghijk") == 18
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyza") == 26
    assert candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "vutsrqponmlkjihgfedcbazyxw") == 312
    assert candidate(s = "thequickbrown",t = "nkbrohwiqctue") == 82
    assert candidate(s = "lmnopqrt",t = "tqrponml") == 32
    assert candidate(s = "abcdefghijkmnopqrstuvwxyzl",t = "lmnopqrstuvwxyzabcdefghijk") == 330
    assert candidate(s = "xyzuvw",t = "uvwzyx") == 18
    assert candidate(s = "abcdefghilmnopqrstuvwxyzjk",t = "jklmnopqrstuvwxyzabcdefghi") == 306
    assert candidate(s = "abc",t = "cba") == 4
    assert candidate(s = "abcdefghijkmnopqrstvuwxyz",t = "xyzuvwtpqrsmnkjihgfedcba") == 297
    assert candidate(s = "acdefghijklmnopqrstuvwxyzb",t = "bzabcdefghijklmnopqrstuvwxy") == 141
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "qpjohuxivtnrckdsmgflweazyb") == 246
    assert candidate(s = "abcdxyz",t = "zyxcba") == 21
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "qrstuvwxyabcdefghijklmnop") == 288
    assert candidate(s = "abcdefghijkmnopqrstuvwxyzl",t = "lnopqrstuvwxyzabcdefghijkml") == 337
    assert candidate(s = "qrstuv",t = "tvusqr") == 18
    assert candidate(s = "abcdefghijk",t = "kabcdefghij") == 20
    assert candidate(s = "rplumabc",t = "mucrlpba") == 22
    assert candidate(s = "mnopqrstuvwxyzabcde",t = "edcbamnopqrstuvwxyz") == 140
    assert candidate(s = "aeiouy",t = "uyioea") == 16
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bacdefghijklmnopqrstuvwxyza") == 28
    assert candidate(s = "abcdefghijklmnopqrstuvwxy",t = "yxwvutsrqponmlkjihgfedcba") == 312
    assert candidate(s = "zxcvbnm",t = "mnbvcxz") == 24
    assert candidate(s = "lkjhgfdsapoiuytrewqmnbvcxz",t = "xcvbnmqwertypoiuytsdfghjkl") == 318
    assert candidate(s = "xyzxyz",t = "zzzyyx") == 15
    assert candidate(s = "xyzabcdefghijklmnopqrstuvw",t = "stuvwxabcdefghijklmnopqrzy") == 210
    assert candidate(s = "abcdefghij",t = "ijhgfedcba") == 50
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq") == 338
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcazdefghijklmnopqrstuvwxy") == 48
    assert candidate(s = "tuvrstxyzwqpomnlkjihgfedcba",t = "cabfedghijklmnopqrstuvwxyz") == 338
    assert candidate(s = "abcxyz",t = "zyxcba") == 18
    assert candidate(s = "qwertyuiop",t = "poiuytrewq") == 50
    assert candidate(s = "abcdefghijk",t = "kijhgfedcba") == 60
    assert candidate(s = "abcdefghijlm",t = "mljihgfedcba") == 72
    assert candidate(s = "mnopqrstu",t = "ustqrpmno") == 40
    assert candidate(s = "abcdefgh",t = "hgfedcba") == 32
    assert candidate(s = "qrstuvw",t = "tuvwsrq") == 24
    assert candidate(s = "abcdefghijklm",t = "mlkjihgfedcba") == 84
    assert candidate(s = "abcdefghij",t = "abcdefghij") == 0
    assert candidate(s = "ghijklmn",t = "nmlkjihg") == 32


