def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aaabbbccc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbccc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvut") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvut") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnbvcxzlkjhgfdsapoiuytrewq") == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnbvcxzlkjhgfdsapoiuytrewq") == 178: {e}')
    
    total += 1
    try:
        result = candidate(word = "qpwoeirutyalskdjfhgzmxncbv") == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qpwoeirutyalskdjfhgzmxncbv") == 191: {e}')
    
    total += 1
    try:
        result = candidate(word = "zjpc") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zjpc") == 34: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxyzabcdefghijklmno") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxyzabcdefghijklmno") == 62: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyzabcdefghijkl") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyzabcdefghijkl") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "z") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "z") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaa") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaa") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "qpwoeirutyalskdjfhgzmxncbva") == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qpwoeirutyalskdjfhgzmxncbva") == 197: {e}')
    
    total += 1
    try:
        result = candidate(word = "za") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "za") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "qpwoeirutyalskdjfhgzmxcvbn") == 193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qpwoeirutyalskdjfhgzmxcvbn") == 193: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnonmonmomnonmon") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnonmonmomnonmon") == 47: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "bza") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bza") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "az") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "az") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba") == 37: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq") == 348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq") == 348: {e}')
    
    total += 1
    try:
        result = candidate(word = "adgjmpsvxzbehiklnortuwfyqc") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "adgjmpsvxzbehiklnortuwfyqc") == 110: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 79: {e}')
    
    total += 1
    try:
        result = candidate(word = "aazzbbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aazzbbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 81: {e}')
    
    total += 1
    try:
        result = candidate(word = "mamamamamamamamamamamamamam") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mamamamamamamamamamamamamam") == 351: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 47: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdezyxwvut") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdezyxwvut") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "zaqwsxcderfvgytujnhytgfrdxcvbnmzaqwsxcderfv") == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zaqwsxcderfvgytujnhytgfrdxcvbnmzaqwsxcderfv") == 328: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvmnopqrstuvmnopqrstuv") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvmnopqrstuvmnopqrstuv") == 87: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuioplkjhgfdsazxcvbnmnbvcxzlkjhgfdsapoiuytrewq") == 323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuioplkjhgfdsazxcvbnmnbvcxzlkjhgfdsapoiuytrewq") == 323: {e}')
    
    total += 1
    try:
        result = candidate(word = "mamamamamamamamamamamamamamamamamamamamamamamamamamama") == 702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mamamamamamamamamamamamamamamamamamamamamamamamamamama") == 702: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 70: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 346: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjhgfdsapoiuytrewqzxcvbnm") == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjhgfdsapoiuytrewqzxcvbnm") == 174: {e}')
    
    total += 1
    try:
        result = candidate(word = "mjmlkdjfhakjdhfkahdfkldshfklsjdhfkjd") == 217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mjmlkdjfhakjdhfkahdfkldshfklsjdhfkjd") == 217: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 130: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 44: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjhgfdsapoiuytrewqmasdfghjkl") == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjhgfdsapoiuytrewqmasdfghjkl") == 178: {e}')
    
    total += 1
    try:
        result = candidate(word = "qponmlkjihgfedcba") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qponmlkjihgfedcba") == 43: {e}')
    
    total += 1
    try:
        result = candidate(word = "jklmnopqrstuvwxyzaaaazzzzz") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jklmnopqrstuvwxyzaaaazzzzz") == 53: {e}')
    
    total += 1
    try:
        result = candidate(word = "wvutsrqponmlkjihgfedcba") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wvutsrqponmlkjihgfedcba") == 49: {e}')
    
    total += 1
    try:
        result = candidate(word = "wertyuioplkjhgfdsamnbvcxzabcd") == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wertyuioplkjhgfdsamnbvcxzabcd") == 164: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdpqrsuvxyzefghijkmnotwxyz") == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdpqrsuvxyzefghijkmnotwxyz") == 79: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertypasdfghjklzxcvbnmqwertypasdfghjklzxcvbnm") == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertypasdfghjklzxcvbnmqwertypasdfghjklzxcvbnm") == 312: {e}')
    
    total += 1
    try:
        result = candidate(word = "bdfhjlnprtvxz") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bdfhjlnprtvxz") == 38: {e}')
    
    total += 1
    try:
        result = candidate(word = "qzcvmlkjhgfdsapoiuytrwer") == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qzcvmlkjhgfdsapoiuytrwer") == 157: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxynmlkjihgfedcbazyxw") == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxynmlkjihgfedcbazyxw") == 83: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyza") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyza") == 53: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyzzzzzzzzzzzzzzzzzzzzzzzzz") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyzzzzzzzzzzzzzzzzzzzzzzzzz") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwerasdfzxcv") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwerasdfzxcv") == 99: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklnmopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklnmopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdpqrsuvxyzefghijkmnotw") == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdpqrsuvxyzefghijkmnotw") == 73: {e}')
    
    total += 1
    try:
        result = candidate(word = "dcbazyxwvutsrqponmlkjihgfedcba") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dcbazyxwvutsrqponmlkjihgfedcba") == 62: {e}')
    
    total += 1
    try:
        result = candidate(word = "fedcbaZYXWVUTSRQPONMLKJIHGFEDCBA") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fedcbaZYXWVUTSRQPONMLKJIHGFEDCBA") == 74: {e}')
    
    total += 1
    try:
        result = candidate(word = "acdfghjklmnpqrstvwxyz") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acdfghjklmnpqrstvwxyz") == 46: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuzyxwvutsrqponmlkjihgfedcba") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuzyxwvutsrqponmlkjihgfedcba") == 85: {e}')
    
    total += 1
    try:
        result = candidate(word = "zxcvbnmlkjhgfdsapoiuytrewqzxcvbnmlkjhgfdsapoiuytrewq") == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zxcvbnmlkjhgfdsapoiuytrewqzxcvbnmlkjhgfdsapoiuytrewq") == 320: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjhgfdsapoiuytrewqzxcvbnmzxcvbnmlkjhgfdsapoiuytrewq") == 342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjhgfdsapoiuytrewqzxcvbnmzxcvbnmlkjhgfdsapoiuytrewq") == 342: {e}')
    
    total += 1
    try:
        result = candidate(word = "fedcbazyxwvutsrqponmlkjihg") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fedcbazyxwvutsrqponmlkjihg") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb") == 40: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrlkjihgfedcbazyxwvut") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrlkjihgfedcbazyxwvut") == 66: {e}')
    
    total += 1
    try:
        result = candidate(word = "qpwoeirutyalskdjfhgzxcvbnm") == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qpwoeirutyalskdjfhgzxcvbnm") == 172: {e}')
    
    total += 1
    try:
        result = candidate(word = "mlkjihgfedcba") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mlkjihgfedcba") == 37: {e}')
    
    total += 1
    try:
        result = candidate(word = "yzab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yzab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 102: {e}')
    
    total += 1
    try:
        result = candidate(word = "qzmlkihgfedcba") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qzmlkihgfedcba") == 58: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcadefghijklmnopqrstuvwxyz") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcadefghijklmnopqrstuvwxyz") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaabbbbbbbbccccccccdddddd") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaabbbbbbbbccccccccdddddd") == 37: {e}')
    
    total += 1
    try:
        result = candidate(word = "llllllllllllllllllllllllllllllllllllllllllllllllllllllll") == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "llllllllllllllllllllllllllllllllllllllllllllllllllllllll") == 67: {e}')
    
    total += 1
    try:
        result = candidate(word = "nlbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkb") == 392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nlbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkb") == 392: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjhgfdsazxcvbnmmnbvcxzlkjhgfdsa") == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjhgfdsazxcvbnmmnbvcxzlkjhgfdsa") == 176: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrsvxyz") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrsvxyz") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "poiuytrewqlkjhgfdsamnbvcxzpoiuytrewqlkjhgfdsamnbvcxz") == 341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "poiuytrewqlkjhgfdsamnbvcxzpoiuytrewqlkjhgfdsamnbvcxz") == 341: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertypoiuytrewertyuiop") == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertypoiuytrewertyuiop") == 178: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaabbbbbcccccdddddeeeee") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaabbbbbcccccdddddeeeee") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "uqwertyuioplkjhgfdsamnbvcxz") == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uqwertyuioplkjhgfdsamnbvcxz") == 170: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvzxcvbnmlkjhgfedcba") == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvzxcvbnmlkjhgfedcba") == 88: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwerasdfzxcvqwerasdfzxcvqwerasdfzxcv") == 287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwerasdfzxcvqwerasdfzxcvqwerasdfzxcv") == 287: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkm") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkm") == 136: {e}')
    
    total += 1
    try:
        result = candidate(word = "zazazazazazazazazazazazazazazaz") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zazazazazazazazazazazazazazazaz") == 62: {e}')
    
    total += 1
    try:
        result = candidate(word = "aazzzzyyyyxxxwwvvuuttrrssqqppoonnmmlkkjjiihhggffeeddaa") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aazzzzyyyyxxxwwvvuuttrrssqqppoonnmmlkkjjiihhggffeeddaa") == 82: {e}')
    
    total += 1
    try:
        result = candidate(word = "jqpnfjwmsvkmrekjijgqpxvukz") == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jqpnfjwmsvkmrekjijgqpxvukz") == 175: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjhgfdsapoiuytrewqasdfghjklmnbvcxz") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjhgfdsapoiuytrewqasdfghjklmnbvcxz") == 212: {e}')
    
    total += 1
    try:
        result = candidate(word = "ejpmytlrzwhgodicuvnkxfsab") == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ejpmytlrzwhgodicuvnkxfsab") == 190: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm") == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm") == 310: {e}')
    
    total += 1
    try:
        result = candidate(word = "qrstuvwxyzaeiou") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qrstuvwxyzaeiou") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouyaeiouyaeiouyaeiouy") == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouyaeiouyaeiouyaeiouy") == 126: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcbaa") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcbaa") == 53: {e}')
    
    total += 1
    try:
        result = candidate(word = "poiuytrewqasdfghjklzxcvbnmpoiuytrewqasdfghjklzxcvbnmpoiuytrewq") == 414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "poiuytrewqasdfghjklzxcvbnmpoiuytrewqasdfghjklzxcvbnmpoiuytrewq") == 414: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghjklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghjklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 101: {e}')
    
    total += 1
    try:
        result = candidate(word = "qazwsxedcrfvtgbyhnujmikolpqwazxsedcrfvtgbyhnujmikolpqwaz") == 361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qazwsxedcrfvtgbyhnujmikolpqwazxsedcrfvtgbyhnujmikolpqwaz") == 361: {e}')
    
    total += 1
    try:
        result = candidate(word = "mzaixmsdcvnbmqwerty") == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mzaixmsdcvnbmqwerty") == 169: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdefghijklmnopqrstuvwxyz") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdefghijklmnopqrstuvwxyz") == 54: {e}')
    
    total += 1
    try:
        result = candidate(word = "poiuytrewqlkjhgfdsamnbvcxz") == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "poiuytrewqlkjhgfdsamnbvcxz") == 171: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 111: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaab") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaab") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "pppppppppppppppppppppppppppp") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pppppppppppppppppppppppppppp") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 103: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkmnopqrstuvwxyz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkmnopqrstuvwxyz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word = "azzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "azzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 58: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 97: {e}')
    
    total += 1
    try:
        result = candidate(word = "zaazaaazzaa") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zaazaaazzaa") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzaaazzzaaazzzaaazzzaaazzzaaazzz") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzaaazzzaaazzzaaazzzaaazzzaaazzz") == 44: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxcbaqwertyuiopasdfghjklmnbvcxz") == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxcbaqwertyuiopasdfghjklmnbvcxz") == 181: {e}')
    
    total += 1
    try:
        result = candidate(word = "asdfghjklqwertyuiopzxcvbnm") == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "asdfghjklqwertyuiopzxcvbnm") == 158: {e}')
    
    total += 1
    try:
        result = candidate(word = "pqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 82: {e}')
    
    total += 1
    try:
        result = candidate(word = "zabcdefghijklmnopqrstuvwxyza") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zabcdefghijklmnopqrstuvwxyza") == 56: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzza") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzza") == 54: {e}')
    
    total += 1
    try:
        result = candidate(word = "tgbnhyujmkiolpvcxz") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tgbnhyujmkiolpvcxz") == 125: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnm") == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnm") == 176: {e}')
    
    total += 1
    try:
        result = candidate(word = "qazwsxedcrfvtgbyhnujmikolp") == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qazwsxedcrfvtgbyhnujmikolp") == 177: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 118: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 77: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqasdfghjklpoiuytrewq") == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqasdfghjklpoiuytrewq") == 295: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkj") == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkj") == 135: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 103: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwx") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwx") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcbaqwertyuiop") == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcbaqwertyuiop") == 129: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacaba") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacaba") == 59: {e}')
    
    total += 1
    try:
        result = candidate(word = "fedcbazyxwvutsrqponmlkjihgfedcba") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fedcbazyxwvutsrqponmlkjihgfedcba") == 68: {e}')
    
    total += 1
    try:
        result = candidate(word = "zaqwsxcderfvgytuhjnmkiolp") == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zaqwsxcderfvgytuhjnmkiolp") == 156: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aaabbbccc") == 11
    assert candidate(word = "zyxwvut") == 14
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 29
    assert candidate(word = "mnbvcxzlkjhgfdsapoiuytrewq") == 178
    assert candidate(word = "qpwoeirutyalskdjfhgzmxncbv") == 191
    assert candidate(word = "zjpc") == 34
    assert candidate(word = "abcdz") == 12
    assert candidate(word = "pqrstuvwxyzabcdefghijklmno") == 62
    assert candidate(word = "aaa") == 3
    assert candidate(word = "mnopqrstuvwxyzabcdefghijkl") == 63
    assert candidate(word = "z") == 2
    assert candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaa") == 26
    assert candidate(word = "qpwoeirutyalskdjfhgzmxncbva") == 197
    assert candidate(word = "za") == 4
    assert candidate(word = "zzz") == 4
    assert candidate(word = "qpwoeirutyalskdjfhgzmxcvbn") == 193
    assert candidate(word = "mnonmonmomnonmon") == 47
    assert candidate(word = "a") == 1
    assert candidate(word = "bza") == 7
    assert candidate(word = "abc") == 5
    assert candidate(word = "az") == 3
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 51
    assert candidate(word = "abacabadabacaba") == 37
    assert candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq") == 348
    assert candidate(word = "adgjmpsvxzbehiklnortuwfyqc") == 110
    assert candidate(word = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 79
    assert candidate(word = "aazzbbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 81
    assert candidate(word = "mamamamamamamamamamamamamam") == 351
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 47
    assert candidate(word = "abcdezyxwvut") == 27
    assert candidate(word = "zaqwsxcderfvgytujnhytgfrdxcvbnmzaqwsxcderfv") == 328
    assert candidate(word = "mnopqrstuvmnopqrstuvmnopqrstuv") == 87
    assert candidate(word = "qwertyuioplkjhgfdsazxcvbnmnbvcxzlkjhgfdsapoiuytrewq") == 323
    assert candidate(word = "mamamamamamamamamamamamamamamamamamamamamamamamamamama") == 702
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 70
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 346
    assert candidate(word = "lkjhgfdsapoiuytrewqzxcvbnm") == 174
    assert candidate(word = "mjmlkdjfhakjdhfkahdfkldshfklsjdhfkjd") == 217
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 130
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 44
    assert candidate(word = "lkjhgfdsapoiuytrewqmasdfghjkl") == 178
    assert candidate(word = "qponmlkjihgfedcba") == 43
    assert candidate(word = "jklmnopqrstuvwxyzaaaazzzzz") == 53
    assert candidate(word = "wvutsrqponmlkjihgfedcba") == 49
    assert candidate(word = "wertyuioplkjhgfdsamnbvcxzabcd") == 164
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 33
    assert candidate(word = "abcdpqrsuvxyzefghijkmnotwxyz") == 79
    assert candidate(word = "qwertypasdfghjklzxcvbnmqwertypasdfghjklzxcvbnm") == 312
    assert candidate(word = "bdfhjlnprtvxz") == 38
    assert candidate(word = "qzcvmlkjhgfdsapoiuytrwer") == 157
    assert candidate(word = "mnopqrstuvwxynmlkjihgfedcbazyxw") == 83
    assert candidate(word = "abcdefghijklmnopqrstuvwxyza") == 53
    assert candidate(word = "zyzzzzzzzzzzzzzzzzzzzzzzzzz") == 30
    assert candidate(word = "qwerasdfzxcv") == 99
    assert candidate(word = "abcdefghijklnmopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 104
    assert candidate(word = "abcdpqrsuvxyzefghijkmnotw") == 73
    assert candidate(word = "dcbazyxwvutsrqponmlkjihgfedcba") == 62
    assert candidate(word = "fedcbaZYXWVUTSRQPONMLKJIHGFEDCBA") == 74
    assert candidate(word = "acdfghjklmnpqrstvwxyz") == 46
    assert candidate(word = "mnopqrstuzyxwvutsrqponmlkjihgfedcba") == 85
    assert candidate(word = "zxcvbnmlkjhgfdsapoiuytrewqzxcvbnmlkjhgfdsapoiuytrewq") == 320
    assert candidate(word = "lkjhgfdsapoiuytrewqzxcvbnmzxcvbnmlkjhgfdsapoiuytrewq") == 342
    assert candidate(word = "fedcbazyxwvutsrqponmlkjihg") == 56
    assert candidate(word = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb") == 40
    assert candidate(word = "mnopqrlkjihgfedcbazyxwvut") == 66
    assert candidate(word = "qpwoeirutyalskdjfhgzxcvbnm") == 172
    assert candidate(word = "mlkjihgfedcba") == 37
    assert candidate(word = "yzab") == 9
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 102
    assert candidate(word = "qzmlkihgfedcba") == 58
    assert candidate(word = "bcadefghijklmnopqrstuvwxyz") == 55
    assert candidate(word = "aaaaaaaaaaaabbbbbbbbccccccccdddddd") == 37
    assert candidate(word = "llllllllllllllllllllllllllllllllllllllllllllllllllllllll") == 67
    assert candidate(word = "nlbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkbnlkb") == 392
    assert candidate(word = "lkjhgfdsazxcvbnmmnbvcxzlkjhgfdsa") == 176
    assert candidate(word = "mnopqrsvxyz") == 36
    assert candidate(word = "poiuytrewqlkjhgfdsamnbvcxzpoiuytrewqlkjhgfdsamnbvcxz") == 341
    assert candidate(word = "qwertypoiuytrewertyuiop") == 178
    assert candidate(word = "aaaaabbbbbcccccdddddeeeee") == 29
    assert candidate(word = "uqwertyuioplkjhgfdsamnbvcxz") == 170
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 104
    assert candidate(word = "qrstuvzxcvbnmlkjhgfedcba") == 88
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 35
    assert candidate(word = "qwerasdfzxcvqwerasdfzxcvqwerasdfzxcv") == 287
    assert candidate(word = "lkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkmlkm") == 136
    assert candidate(word = "zazazazazazazazazazazazazazazaz") == 62
    assert candidate(word = "aazzzzyyyyxxxwwvvuuttrrssqqppoonnmmlkkjjiihhggffeeddaa") == 82
    assert candidate(word = "jqpnfjwmsvkmrekjijgqpxvukz") == 175
    assert candidate(word = "lkjhgfdsapoiuytrewqasdfghjklmnbvcxz") == 212
    assert candidate(word = "ejpmytlrzwhgodicuvnkxfsab") == 190
    assert candidate(word = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm") == 310
    assert candidate(word = "qrstuvwxyzaeiou") == 55
    assert candidate(word = "aeiouyaeiouyaeiouyaeiouy") == 126
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcbaa") == 53
    assert candidate(word = "poiuytrewqasdfghjklzxcvbnmpoiuytrewqasdfghjklzxcvbnmpoiuytrewq") == 414
    assert candidate(word = "abcdefghjklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 101
    assert candidate(word = "qazwsxedcrfvtgbyhnujmikolpqwazxsedcrfvtgbyhnujmikolpqwaz") == 361
    assert candidate(word = "mzaixmsdcvnbmqwerty") == 169
    assert candidate(word = "zabcdefghijklmnopqrstuvwxyz") == 54
    assert candidate(word = "poiuytrewqlkjhgfdsamnbvcxz") == 171
    assert candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 111
    assert candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaab") == 29
    assert candidate(word = "pppppppppppppppppppppppppppp") == 39
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 103
    assert candidate(word = "abcdefghijkmnopqrstuvwxyz") == 50
    assert candidate(word = "azzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 58
    assert candidate(word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 97
    assert candidate(word = "zaazaaazzaa") == 17
    assert candidate(word = "zzzaaazzzaaazzzaaazzzaaazzzaaazzz") == 44
    assert candidate(word = "zyxcbaqwertyuiopasdfghjklmnbvcxz") == 181
    assert candidate(word = "asdfghjklqwertyuiopzxcvbnm") == 158
    assert candidate(word = "pqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 82
    assert candidate(word = "zabcdefghijklmnopqrstuvwxyza") == 56
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzza") == 54
    assert candidate(word = "tgbnhyujmkiolpvcxz") == 125
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm") == 176
    assert candidate(word = "qazwsxedcrfvtgbyhnujmikolp") == 177
    assert candidate(word = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 118
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 77
    assert candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqasdfghjklpoiuytrewq") == 295
    assert candidate(word = "lkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkjlkj") == 135
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 103
    assert candidate(word = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 64
    assert candidate(word = "mnopqrstuvwx") == 35
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcbaqwertyuiop") == 129
    assert candidate(word = "abacabadabacabadabacaba") == 59
    assert candidate(word = "fedcbazyxwvutsrqponmlkjihgfedcba") == 68
    assert candidate(word = "zaqwsxcderfvgytuhjnmkiolp") == 156


