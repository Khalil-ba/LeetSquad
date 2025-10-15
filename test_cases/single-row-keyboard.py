def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "pqrstuvwxyzabcdefghijklmno") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "pqrstuvwxyzabcdefghijklmno") == 64: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "internationalization") == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "internationalization") == 188: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "cba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "cba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "thequickbrownfoxjumpsoverthelazydog") == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "thequickbrownfoxjumpsoverthelazydog") == 328: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "pqrstuvwxyzabcdefghijklmno",word = "leetcode") == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "pqrstuvwxyzabcdefghijklmno",word = "leetcode") == 73: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 19: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "programmingcontestisfun") == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "programmingcontestisfun") == 224: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "abacabadabacaba") == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "abacabadabacaba") == 162: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "supercalifragilisticexpialidocious") == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "supercalifragilisticexpialidocious") == 275: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "hellofromtheotherworld") == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "hellofromtheotherworld") == 174: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "abcdefghijklmnopqrstuvwxyz") == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "abcdefghijklmnopqrstuvwxyz") == 229: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "thequickbrownfoxjumpsoverthelazydog") == 322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "thequickbrownfoxjumpsoverthelazydog") == 322: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "rhythm") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "rhythm") == 37: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "xylophone") == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "xylophone") == 79: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "lkjhgfdsapoiuytrewqmnbvcxz",word = "softwareengineering") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "lkjhgfdsapoiuytrewqmnbvcxz",word = "softwareengineering") == 114: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "bazinga") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "bazinga") == 82: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "neuromuscular") == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "neuromuscular") == 151: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 75: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "supercalifragilisticexpialidocious") == 278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "supercalifragilisticexpialidocious") == 278: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "fedcbaonmlkjihgtsrqpzyxwvu",word = "programmingisfun") == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "fedcbaonmlkjihgtsrqpzyxwvu",word = "programmingisfun") == 139: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "quantization") == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "quantization") == 119: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "antidisestablishmentarianism") == 367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "antidisestablishmentarianism") == 367: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "mississippi") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "mississippi") == 63: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "aquickbrownfoxjumpsoverthelazydog") == 317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "aquickbrownfoxjumpsoverthelazydog") == 317: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "ejkflqzcvbnpitywrdxhgmosau",word = "exponentially") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "ejkflqzcvbnpitywrdxhgmosau",word = "exponentially") == 114: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "antidisestablishmentarianism") == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "antidisestablishmentarianism") == 295: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 447: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "abacabadabacaba") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "abacabadabacaba") == 47: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "algorithm") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "algorithm") == 66: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqasdfghjklzxcvbnm",word = "congratulations") == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqasdfghjklzxcvbnm",word = "congratulations") == 161: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "thequickbrownfoxjumpsoverthelazydog") == 339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "thequickbrownfoxjumpsoverthelazydog") == 339: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "racecar") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "racecar") == 96: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "honorificabilitudinitatibus") == 313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "honorificabilitudinitatibus") == 313: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "alibabacloud") == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "alibabacloud") == 121: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "supercalifragilisticexpialidocious") == 283
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "supercalifragilisticexpialidocious") == 283: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "extraterrestrialization") == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "extraterrestrialization") == 181: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "yuiophgfdlkjhgfdsazxcvbnmqwerty",word = "abcdefghijklmnopqrstuvwxyz") == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "yuiophgfdlkjhgfdsazxcvbnmqwerty",word = "abcdefghijklmnopqrstuvwxyz") == 246: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "lkjhgfdsazxcvbnmqwertyuiop",word = "thisisaverylongwordthatwilltestthekeyboardlayout") == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "lkjhgfdsazxcvbnmqwertyuiop",word = "thisisaverylongwordthatwilltestthekeyboardlayout") == 510: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "abcdefghijklmnopqrstuvwxyz") == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "abcdefghijklmnopqrstuvwxyz") == 224: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "floccinaucinihilipilification") == 271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "floccinaucinihilipilification") == 271: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "juxtaposition") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "juxtaposition") == 104: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "rhythm") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "rhythm") == 66: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 18: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "reverseengineering") == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "reverseengineering") == 149: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "congratulationsonwinningthetournament") == 397
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "congratulationsonwinningthetournament") == 397: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "vbnm,asdfghjklpoiuytrewqzxc",word = "elephant") == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "vbnm,asdfghjklpoiuytrewqzxc",word = "elephant") == 73: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "hellohellohellohellohellohellohellohello") == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "hellohellohellohellohellohellohellohello") == 160: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "ploazxykrmnghijfdscwutevbq",word = "characterization") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "ploazxykrmnghijfdscwutevbq",word = "characterization") == 136: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "lkjhgfdsazxcvbnm qwertyuiop",word = "serendipitously") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "lkjhgfdsazxcvbnm qwertyuiop",word = "serendipitously") == 110: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "quixotically") == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "quixotically") == 122: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "aabbccddeeffgghhiijjkkllmmooppqqrrssttuuvvwwxxyyzz") == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "aabbccddeeffgghhiijjkkllmmooppqqrrssttuuvvwwxxyyzz") == 215: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "antidisestablishmentarianism") == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "antidisestablishmentarianism") == 232: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "supercalifragilisticexpialidocious") == 293
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "supercalifragilisticexpialidocious") == 293: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "everygoodboydoesfine") == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "everygoodboydoesfine") == 166: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qazwsxedcrfvtgbyhnujmiklop",word = "pneumonoultramicroscopicsilicovolcanoconiosis") == 442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qazwsxedcrfvtgbyhnujmiklop",word = "pneumonoultramicroscopicsilicovolcanoconiosis") == 442: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "ejkflsdcxzivhnutybgrqompatwe",word = "thequickbrownfoxjumpsoverthelazydog") == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "ejkflsdcxzivhnutybgrqompatwe",word = "thequickbrownfoxjumpsoverthelazydog") == 380: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "thelazybrownfoxjumpsoverthelazydog") == 394
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "thelazybrownfoxjumpsoverthelazydog") == 394: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "fghijklmnopqrstuvwxyzabcde",word = "pythonprogramming") == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "fghijklmnopqrstuvwxyzabcde",word = "pythonprogramming") == 109: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "pseudopseudohypoparathyroidism") == 441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "pseudopseudohypoparathyroidism") == 441: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poeiuytrewqkjhgfdsalcvbnmzx",word = "algorithmsanddatastructures") == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poeiuytrewqkjhgfdsalcvbnmzx",word = "algorithmsanddatastructures") == 175: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzasdfghjklpoiuytrewq",word = "quixotically") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzasdfghjklpoiuytrewq",word = "quixotically") == 94: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "floccinaucinihilipilification") == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "floccinaucinihilipilification") == 330: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "cvbnmloiuytrqwedpasdfgzxhbkj",word = "microelectromechanical") == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "cvbnmloiuytrqwedpasdfgzxhbkj",word = "microelectromechanical") == 197: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "fghijklmnopqrstuvwxyzabcde",word = "fedcbazyxwvutsrqponmlkjihgf") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "fghijklmnopqrstuvwxyzabcde",word = "fedcbazyxwvutsrqponmlkjihgf") == 50: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "programmingisfun") == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "programmingisfun") == 174: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 215: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "programmingisfun") == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "programmingisfun") == 149: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "ghijklmnopqrstuvwxyzabcdef",word = "thisisaverylongwordthatwilltestyouralgorithm") == 362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "ghijklmnopqrstuvwxyzabcdef",word = "thisisaverylongwordthatwilltestyouralgorithm") == 362: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "congratulationsyouhavecompletedthelastlevel") == 383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "congratulationsyouhavecompletedthelastlevel") == 383: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "mississippi") == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "mississippi") == 115: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "ejkpfghizxncovmwbartldsqyu",word = "onomatopoeia") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "ejkpfghizxncovmwbartldsqyu",word = "onomatopoeia") == 77: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "racecar") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "racecar") == 50: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "abcdefgxyzhijklmnopqrtuvw",word = "programminglanguage") == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "abcdefgxyzhijklmnopqrtuvw",word = "programminglanguage") == 196: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "bnmzxcvbnmlkjhgfdsapoiuytrewq",word = "cryptographically") == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "bnmzxcvbnmlkjhgfdsapoiuytrewq",word = "cryptographically") == 129: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "qwertyuioplkjhgfdsazxcvbnm") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "qwertyuioplkjhgfdsazxcvbnm") == 66: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "floccinaucinihilipilification") == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "floccinaucinihilipilification") == 242: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "incomprehensible") == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "incomprehensible") == 178: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "thequickbrownfoxjumpsoverthelazydog") == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "thequickbrownfoxjumpsoverthelazydog") == 378: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "abababababababababababababababababababababababababababababab") == 782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "abababababababababababababababababababababababababababababab") == 782: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "algorithmically") == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "algorithmically") == 130: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "mnbvcxzasdfghjklpoiuytrewq",word = "floccinaucinihilipilification") == 237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "mnbvcxzasdfghjklpoiuytrewq",word = "floccinaucinihilipilification") == 237: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "thelazybrownfoxjumpsoverthelazydog") == 354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "thelazybrownfoxjumpsoverthelazydog") == 354: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "supercalifragilisticexpialidocious") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "supercalifragilisticexpialidocious") == 377: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "anexampleofaverylongwordthatneedstobechecked") == 387
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "anexampleofaverylongwordthatneedstobechecked") == 387: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "lkjhgfdsapoiuytrewqzxcvbnm",word = "mellifluous") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "lkjhgfdsapoiuytrewqzxcvbnm",word = "mellifluous") == 93: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "bipartisan") == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "bipartisan") == 86: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "poiuytrewqlkjhgfdsazxcvbnm",word = "interstellar") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "poiuytrewqlkjhgfdsazxcvbnm",word = "interstellar") == 94: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 224: {e}')
    
    total += 1
    try:
        result = candidate(keyboard = "asdfghjklpoiuytrewqzxcvbnm",word = "mississippi") == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(keyboard = "asdfghjklpoiuytrewqzxcvbnm",word = "mississippi") == 83: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "a") == 0
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "pqrstuvwxyzabcdefghijklmno") == 64
    assert candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "internationalization") == 188
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "cba") == 4
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "thequickbrownfoxjumpsoverthelazydog") == 328
    assert candidate(keyboard = "pqrstuvwxyzabcdefghijklmno",word = "leetcode") == 73
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 19
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "programmingcontestisfun") == 224
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "abacabadabacaba") == 162
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "supercalifragilisticexpialidocious") == 275
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "hellofromtheotherworld") == 174
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "abcdefghijklmnopqrstuvwxyz") == 229
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "thequickbrownfoxjumpsoverthelazydog") == 322
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "rhythm") == 37
    assert candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "xylophone") == 79
    assert candidate(keyboard = "lkjhgfdsapoiuytrewqmnbvcxz",word = "softwareengineering") == 114
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "bazinga") == 82
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "neuromuscular") == 151
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 75
    assert candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 50
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "supercalifragilisticexpialidocious") == 278
    assert candidate(keyboard = "fedcbaonmlkjihgtsrqpzyxwvu",word = "programmingisfun") == 139
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "quantization") == 119
    assert candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "antidisestablishmentarianism") == 367
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "mississippi") == 63
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "aquickbrownfoxjumpsoverthelazydog") == 317
    assert candidate(keyboard = "ejkflqzcvbnpitywrdxhgmosau",word = "exponentially") == 114
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "antidisestablishmentarianism") == 295
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 447
    assert candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "abacabadabacaba") == 47
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "algorithm") == 66
    assert candidate(keyboard = "poiuytrewqasdfghjklzxcvbnm",word = "congratulations") == 161
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "thequickbrownfoxjumpsoverthelazydog") == 339
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "racecar") == 96
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "honorificabilitudinitatibus") == 313
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "alibabacloud") == 121
    assert candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "supercalifragilisticexpialidocious") == 283
    assert candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "extraterrestrialization") == 181
    assert candidate(keyboard = "yuiophgfdlkjhgfdsazxcvbnmqwerty",word = "abcdefghijklmnopqrstuvwxyz") == 246
    assert candidate(keyboard = "lkjhgfdsazxcvbnmqwertyuiop",word = "thisisaverylongwordthatwilltestthekeyboardlayout") == 510
    assert candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "abcdefghijklmnopqrstuvwxyz") == 224
    assert candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "floccinaucinihilipilification") == 271
    assert candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "juxtaposition") == 104
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "rhythm") == 66
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 18
    assert candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "reverseengineering") == 149
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "congratulationsonwinningthetournament") == 397
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzz") == 25
    assert candidate(keyboard = "vbnm,asdfghjklpoiuytrewqzxc",word = "elephant") == 73
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "hellohellohellohellohellohellohellohello") == 160
    assert candidate(keyboard = "ploazxykrmnghijfdscwutevbq",word = "characterization") == 136
    assert candidate(keyboard = "lkjhgfdsazxcvbnm qwertyuiop",word = "serendipitously") == 110
    assert candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "quixotically") == 122
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "aabbccddeeffgghhiijjkkllmmooppqqrrssttuuvvwwxxyyzz") == 215
    assert candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "antidisestablishmentarianism") == 232
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "supercalifragilisticexpialidocious") == 293
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "everygoodboydoesfine") == 166
    assert candidate(keyboard = "qazwsxedcrfvtgbyhnujmiklop",word = "pneumonoultramicroscopicsilicovolcanoconiosis") == 442
    assert candidate(keyboard = "ejkflsdcxzivhnutybgrqompatwe",word = "thequickbrownfoxjumpsoverthelazydog") == 380
    assert candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "thelazybrownfoxjumpsoverthelazydog") == 394
    assert candidate(keyboard = "fghijklmnopqrstuvwxyzabcde",word = "pythonprogramming") == 109
    assert candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "pseudopseudohypoparathyroidism") == 441
    assert candidate(keyboard = "poeiuytrewqkjhgfdsalcvbnmzx",word = "algorithmsanddatastructures") == 175
    assert candidate(keyboard = "mnbvcxzasdfghjklpoiuytrewq",word = "quixotically") == 94
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "floccinaucinihilipilification") == 330
    assert candidate(keyboard = "cvbnmloiuytrqwedpasdfgzxhbkj",word = "microelectromechanical") == 197
    assert candidate(keyboard = "fghijklmnopqrstuvwxyzabcde",word = "fedcbazyxwvutsrqponmlkjihgf") == 50
    assert candidate(keyboard = "asdfghjklqwertyuiopzxcvbnm",word = "programmingisfun") == 174
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 215
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "programmingisfun") == 149
    assert candidate(keyboard = "ghijklmnopqrstuvwxyzabcdef",word = "thisisaverylongwordthatwilltestyouralgorithm") == 362
    assert candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "congratulationsyouhavecompletedthelastlevel") == 383
    assert candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "mississippi") == 115
    assert candidate(keyboard = "ejkpfghizxncovmwbartldsqyu",word = "onomatopoeia") == 77
    assert candidate(keyboard = "zyxwvutsrqponmlkjihgfedcba",word = "racecar") == 50
    assert candidate(keyboard = "abcdefghijklmnopqrstuvwxyz",word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
    assert candidate(keyboard = "abcdefgxyzhijklmnopqrtuvw",word = "programminglanguage") == 196
    assert candidate(keyboard = "bnmzxcvbnmlkjhgfdsapoiuytrewq",word = "cryptographically") == 129
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "qwertyuioplkjhgfdsazxcvbnm") == 66
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "floccinaucinihilipilification") == 242
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "incomprehensible") == 178
    assert candidate(keyboard = "asdfghjklzxcvbnmqwertyuiop",word = "thequickbrownfoxjumpsoverthelazydog") == 378
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "abababababababababababababababababababababababababababababab") == 782
    assert candidate(keyboard = "mnbvcxzlkjhgfdsapoiuytrewq",word = "algorithmically") == 130
    assert candidate(keyboard = "mnbvcxzasdfghjklpoiuytrewq",word = "floccinaucinihilipilification") == 237
    assert candidate(keyboard = "qwertyuiopasdfghjklzxcvbnm",word = "thelazybrownfoxjumpsoverthelazydog") == 354
    assert candidate(keyboard = "poiuytrewqlkjhgfdsamnbvcxz",word = "supercalifragilisticexpialidocious") == 377
    assert candidate(keyboard = "cvbnmasdfghjklpoiuytrewqzxc",word = "anexampleofaverylongwordthatneedstobechecked") == 387
    assert candidate(keyboard = "lkjhgfdsapoiuytrewqzxcvbnm",word = "mellifluous") == 93
    assert candidate(keyboard = "qwertyuioplkjhgfdsazxcvbnm",word = "bipartisan") == 86
    assert candidate(keyboard = "poiuytrewqlkjhgfdsazxcvbnm",word = "interstellar") == 94
    assert candidate(keyboard = "zxcvbnmlkjhgfdsapoiuytrewq",word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 224
    assert candidate(keyboard = "asdfghjklpoiuytrewqzxcvbnm",word = "mississippi") == 83


