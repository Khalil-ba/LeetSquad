def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "QWERTYUIOPASDFGHJKLZXCVBNM") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QWERTYUIOPASDFGHJKLZXCVBNM") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZZZZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZZZZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAKE") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAKE") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "RHYTHM") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RHYTHM") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGER") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGER") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALPHABET") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALPHABET") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCD") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCD") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "QWERTYUIOPASDFGHJKLMZXCVBNM") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QWERTYUIOPASDFGHJKLMZXCVBNM") == 54: {e}')
    
    total += 1
    try:
        result = candidate(word = "NEW") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NEW") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "HAPPY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HAPPY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCMN") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCMN") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "LONGEST") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LONGEST") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "MISSISSIPPI") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MISSISSIPPI") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "YEAR") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "YEAR") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZXY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZXY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPTIMIZATION") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPTIMIZATION") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "YYYYYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "YYYYYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "MOUSE") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MOUSE") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZZZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZZZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRANSFER") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRANSFER") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOP") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOP") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHON") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHON") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "QRSTUVWXYZ") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QRSTUVWXYZ") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "KEYBOARD") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KEYBOARD") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABAB") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABAB") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "A") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "A") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFG") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFG") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "DISTANCE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DISTANCE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALGORITHMS") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALGORITHMS") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAPABILITY") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAPABILITY") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "HASHMAP") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HASHMAP") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "LONGWORDLONGWORDLONGWORDLONGWORDLONGWORDLONGWORDLONGWORD") == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LONGWORDLONGWORDLONGWORDLONGWORDLONGWORDLONGWORDLONGWORD") == 122: {e}')
    
    total += 1
    try:
        result = candidate(word = "SPECIAL") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SPECIAL") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEPLOYMENT") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEPLOYMENT") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "VOLCANOES") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VOLCANOES") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "VICTORY") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VICTORY") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "BACKSPACENOTPOSSIBLE") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BACKSPACENOTPOSSIBLE") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROSPERING") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROSPERING") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "METHOD") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "METHOD") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "ROBUST") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ROBUST") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "PLANNING") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PLANNING") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "JOY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JOY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEPTHFIRSTSEARCH") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEPTHFIRSTSEARCH") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONCEPT") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONCEPT") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTEGRATION") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTEGRATION") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "PLENTY") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PLENTY") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "COORDINATION") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COORDINATION") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACCOMPLISHED") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACCOMPLISHED") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "RUBY") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RUBY") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "SERVER") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SERVER") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHONIC") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHONIC") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRODUCT") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRODUCT") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "JUST") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JUST") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "RESEARCH") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RESEARCH") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHONCODING") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHONCODING") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "INITIATION") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INITIATION") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "OBJECTORIENTED") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OBJECTORIENTED") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "REQUIREMENT") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REQUIREMENT") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "BANANA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BANANA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINANCE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINANCE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLOFROMTHEOTHERSIDE") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLOFROMTHEOTHERSIDE") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEDICATED") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEDICATED") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUPERLONGWORD") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUPERLONGWORD") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACCOMPLISHMENT") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACCOMPLISHMENT") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROGRAMMER") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROGRAMMER") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "SPECIALCHARACTERS") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SPECIALCHARACTERS") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "NETWORK") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NETWORK") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "AWESOME") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AWESOME") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROGRESS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROGRESS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "WIN") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "WIN") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "OBJECTIVE") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OBJECTIVE") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLOURISH") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLOURISH") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROSPEROUS") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROSPEROUS") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXPERIMENT") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXPERIMENT") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERBOARD") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERBOARD") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "PATIENCE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PATIENCE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "ADJUSTMENT") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ADJUSTMENT") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXCEL") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXCEL") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS") == 59: {e}')
    
    total += 1
    try:
        result = candidate(word = "FRANK") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FRANK") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "SOFTWARE") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SOFTWARE") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "TWOPOINTERS") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TWOPOINTERS") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "ANALYSIS") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ANALYSIS") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "RESOLUTION") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RESOLUTION") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "LONGWORDFORTESTING") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LONGWORDFORTESTING") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTERACTION") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTERACTION") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "UNOBTRUDES") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UNOBTRUDES") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERMOVEMENT") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERMOVEMENT") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "PEACE") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PEACE") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEPONIBLE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEPONIBLE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "ASTARSEARCH") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ASTARSEARCH") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "ANGULAR") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ANGULAR") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "SERVICE") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SERVICE") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROSPERITY") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROSPERITY") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "RECOGNITION") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RECOGNITION") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "KINDNESS") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KINDNESS") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHONPYTHONPYTHON") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHONPYTHONPYTHON") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "PARTNER") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PARTNER") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "IDEAL") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "IDEAL") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRODUCTIVE") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRODUCTIVE") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "HARMONY") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HARMONY") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "MYSQL") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MYSQL") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHONISFUN") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHONISFUN") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "UNIVERSAL") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UNIVERSAL") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "KEYBOARDLAYOUT") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KEYBOARDLAYOUT") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "SAFE") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SAFE") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "TYPESCRIPT") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TYPESCRIPT") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "TREE") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TREE") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERFINGER") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERFINGER") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "AAAAA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AAAAA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "GENTLE") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GENTLE") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "ETHICAL") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ETHICAL") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "BACKTRACKING") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BACKTRACKING") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "AFFLUENT") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AFFLUENT") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "TIMECOMPLEXITY") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TIMECOMPLEXITY") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "HUMBLE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HUMBLE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "API") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "API") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "OVERCOME") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OVERCOME") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "DOBRE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DOBRE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRACTICE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRACTICE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "PLAIN") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PLAIN") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACHIEVEMENT") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACHIEVEMENT") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "COMPUTERSCIENCE") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COMPUTERSCIENCE") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUCCESSFUL") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUCCESSFUL") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "GOAL") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GOAL") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "CHANGE") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CHANGE") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "FULFILLMENT") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FULFILLMENT") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRINCIPLE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRINCIPLE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "CODER") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CODER") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALLOCATION") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALLOCATION") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "DIJKSTRAS") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DIJKSTRAS") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTERPRETATION") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTERPRETATION") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTEGRITY") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTEGRITY") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "HACK") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HACK") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "QWJRTYUPASDFGZXCVB") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QWJRTYUPASDFGZXCVB") == 43: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUPERLATIVE") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUPERLATIVE") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "PERSISTENT") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PERSISTENT") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "MULTIPLEFINGERS") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MULTIPLEFINGERS") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPERATION") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPERATION") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "DELIVERY") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DELIVERY") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "DETERMINATION") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DETERMINATION") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "DATASTRUCTURE") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DATASTRUCTURE") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "CALCULATION") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CALCULATION") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPULANCE") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPULANCE") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "TOP") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TOP") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SIMULATION") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SIMULATION") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "ATTENTIVE") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ATTENTIVE") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROFILING") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROFILING") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "EFFICIENT") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EFFICIENT") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "MEMORYMANAGEMENT") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MEMORYMANAGEMENT") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "STRATEGY") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STRATEGY") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "THRIVE") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "THRIVE") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "ENERGETIC") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ENERGETIC") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG") == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG") == 73: {e}')
    
    total += 1
    try:
        result = candidate(word = "CUSTOMIZATION") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CUSTOMIZATION") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPTIMIZE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPTIMIZE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "ELITE") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ELITE") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROGRAMMINGISFUN") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROGRAMMINGISFUN") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "COMMITTED") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COMMITTED") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "EFFECTIVE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EFFECTIVE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "REPORT") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REPORT") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "SPACESAVING") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SPACESAVING") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTERFACE") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTERFACE") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "NEURALNETWORKS") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NEURALNETWORKS") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "CORRECT") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CORRECT") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "KNIGHTMARCH") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KNIGHTMARCH") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "SIMPLE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SIMPLE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "TECHNOLOGY") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TECHNOLOGY") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "QUEUE") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QUEUE") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABACAXABABACAB") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABACAXABABACAB") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROGRAMMING") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROGRAMMING") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "SEARCH") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SEARCH") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "MULTIPLEWORDSHEREANDTHERE") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MULTIPLEWORDSHEREANDTHERE") == 49: {e}')
    
    total += 1
    try:
        result = candidate(word = "LOAD") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LOAD") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONFIDENT") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONFIDENT") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "HTML") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HTML") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "SECURE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SECURE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "MECHANISM") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MECHANISM") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "WEALTHY") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "WEALTHY") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLAWLESS") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLAWLESS") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "MORAL") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MORAL") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "RESPONSIBLE") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RESPONSIBLE") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEVOTED") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEVOTED") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "PASSIONATE") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PASSIONATE") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "RANDOMKEYPAD") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RANDOMKEYPAD") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "BACKSPACENEEDED") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BACKSPACENEEDED") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "JAVA") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JAVA") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "CHALLENGE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CHALLENGE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRESENTATION") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRESENTATION") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "BOOMING") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BOOMING") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLOWORLD") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLOWORLD") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "EQUITABLE") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EQUITABLE") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "GREATEST") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GREATEST") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "DATASTRUCTURES") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DATASTRUCTURES") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXCELLENCE") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXCELLENCE") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRECISE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRECISE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "OBTAINED") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OBTAINED") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXECUTION") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXECUTION") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "DELICATE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DELICATE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "KRUSKALSMST") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KRUSKALSMST") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "AAABBBCCCDDD") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AAABBBCCCDDD") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "BEST") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BEST") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJABCDEFGHIJ") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJABCDEFGHIJ") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXEMPLARY") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXEMPLARY") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRIMSMST") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRIMSMST") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "MANAGER") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MANAGER") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "RELATIONSHIP") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RELATIONSHIP") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "COMMUNICATION") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COMMUNICATION") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERPRINT") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERPRINT") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "RECOMMENDATION") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RECOMMENDATION") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "MULTITHREADING") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MULTITHREADING") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "MEETING") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MEETING") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRIUMPHANT") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRIUMPHANT") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRIDE") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRIDE") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "STRETCH") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STRETCH") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERLATERALMOVEMENT") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERLATERALMOVEMENT") == 38: {e}')
    
    total += 1
    try:
        result = candidate(word = "CLIENT") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CLIENT") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "BOOM") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BOOM") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "AFFLUENCE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AFFLUENCE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONSECUTIVE") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONSECUTIVE") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "GREAT") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GREAT") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "MARKET") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MARKET") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "GENUINE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GENUINE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "BIGDATAANALYSIS") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BIGDATAANALYSIS") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONVINCED") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONVINCED") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "UNIT") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UNIT") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONFIGURATION") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONFIGURATION") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "PLAN") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PLAN") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ADAPTABLE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ADAPTABLE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "TEAMWORK") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TEAMWORK") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "AAAAAAAAA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AAAAAAAAA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACHIEVE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACHIEVE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "UTILIZATION") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UTILIZATION") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "THRIVING") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "THRIVING") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "PERFORMANCE") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PERFORMANCE") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "MODEST") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MODEST") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEVELOPMENT") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEVELOPMENT") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACHIEVED") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACHIEVED") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "BREADTHFIRSTSEARCH") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BREADTHFIRSTSEARCH") == 35: {e}')
    
    total += 1
    try:
        result = candidate(word = "ASSURED") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ASSURED") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRIUMPH") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRIUMPH") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "ENTHUSIASTIC") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ENTHUSIASTIC") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "BUSINESS") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BUSINESS") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "PHP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PHP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "EARNED") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EARNED") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "BBBBC") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BBBBC") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "LONGKEYSEQUENCE") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LONGKEYSEQUENCE") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "RIGHT") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RIGHT") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "PERFECTION") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PERFECTION") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRINCIPLED") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRINCIPLED") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEBUGGINGISSLOW") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEBUGGINGISSLOW") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "GUARANTEED") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GUARANTEED") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROSPER") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROSPER") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "SYNCHRONIZATION") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SYNCHRONIZATION") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACCOUNTABLE") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACCOUNTABLE") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "VIVACIOUS") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VIVACIOUS") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACCURATE") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACCURATE") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "INITIALIZE") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INITIALIZE") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABUNDANCE") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABUNDANCE") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXACT") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXACT") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "PREMIERE") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PREMIERE") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "PNEUMONULA") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PNEUMONULA") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "SYNTAXERRORHANDLING") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SYNTAXERRORHANDLING") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHONANDJAVA") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHONANDJAVA") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROBLEM") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROBLEM") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "DECIDED") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DECIDED") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "INFORMATION") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INFORMATION") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "CODINGCHALLENGES") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CODINGCHALLENGES") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRANSACTION") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRANSACTION") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONTESTSAREFUN") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONTESTSAREFUN") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "DYNAMIC") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DYNAMIC") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "PATTERN") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PATTERN") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONCURRENT") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONCURRENT") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "TEST") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TEST") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUPERIOR") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUPERIOR") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "LOVEPYTHON") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LOVEPYTHON") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "COLLABORATION") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COLLABORATION") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "MINIMALIZATION") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MINIMALIZATION") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "MACHINELEARNING") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MACHINELEARNING") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "PLETHORA") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PLETHORA") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "MEMORIZATION") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MEMORIZATION") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROTECTED") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROTECTED") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "JAVASCRIPT") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JAVASCRIPT") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXCEPTIONAL") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXCEPTIONAL") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLOURISHING") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLOURISHING") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "COORDINATOR") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COORDINATOR") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "VARIABLESANDTYPES") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VARIABLESANDTYPES") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "TEAM") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TEAM") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRAVELINGSALESMANPROBLEM") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRAVELINGSALESMANPROBLEM") == 51: {e}')
    
    total += 1
    try:
        result = candidate(word = "VUE") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VUE") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "DIRECT") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DIRECT") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "AVOIDDISTANCE") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AVOIDDISTANCE") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "PREMIUM") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PREMIUM") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLEXIBLE") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLEXIBLE") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "CPLUSPLUS") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CPLUSPLUS") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "BUG") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BUG") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "COOLCODE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COOLCODE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONGRATULATIONS") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONGRATULATIONS") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "MONGODB") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MONGODB") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "NETWORKFLOW") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NETWORKFLOW") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "SIMULATEDANNEALING") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SIMULATEDANNEALING") == 34: {e}')
    
    total += 1
    try:
        result = candidate(word = "STRONG") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STRONG") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "POSTGRESQL") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "POSTGRESQL") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "TARGET") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TARGET") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROJECT") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROJECT") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "ARTIFICIALINTELLIGENCE") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ARTIFICIALINTELLIGENCE") == 37: {e}')
    
    total += 1
    try:
        result = candidate(word = "DATABASE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DATABASE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "RECURSION") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RECURSION") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "REACT") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REACT") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "FRAMEWORK") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FRAMEWORK") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPTIMAL") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPTIMAL") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "REACHED") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REACHED") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXCELLENT") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXCELLENT") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "KANGAROO") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KANGAROO") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "GENETICALGORITHM") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GENETICALGORITHM") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "STRESS") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STRESS") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHONPROGRAMMING") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHONPROGRAMMING") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "GRAPH") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GRAPH") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "MIGHTY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MIGHTY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "HONEST") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HONEST") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACCELERATION") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACCELERATION") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "XYLOPHONE") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "XYLOPHONE") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "LUXURY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LUXURY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "LOYAL") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LOYAL") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "DIVIDEANDCONQUER") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DIVIDEANDCONQUER") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "IDENTIFICATION") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "IDENTIFICATION") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "HONORABLE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HONORABLE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "TYPINGISAWAYTORELAX") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TYPINGISAWAYTORELAX") == 37: {e}')
    
    total += 1
    try:
        result = candidate(word = "ENGINEERING") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ENGINEERING") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "TYPINGWITHTWOFINGERS") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TYPINGWITHTWOFINGERS") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word = "COMPANY") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COMPANY") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 84: {e}')
    
    total += 1
    try:
        result = candidate(word = "ARRAY") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ARRAY") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "CSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "CYBER") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CYBER") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "ENGINEER") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ENGINEER") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "FUTURE") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FUTURE") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "APPLICATION") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "APPLICATION") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "STACK") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STACK") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "VICTORIOUS") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VICTORIOUS") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "IMPLEMENTATION") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "IMPLEMENTATION") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLOUNIVERSE") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLOUNIVERSE") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROCESS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROCESS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "FUNCTION") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FUNCTION") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAREER") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAREER") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "INITIATIVE") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INITIATIVE") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "RESULT") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RESULT") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "EMPATHY") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EMPATHY") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABILITY") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABILITY") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUPPLIER") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUPPLIER") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTERVENTION") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTERVENTION") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "ATTAINED") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ATTAINED") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALGORITHM") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALGORITHM") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "LEADER") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LEADER") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "SOFTWAREENGINEERING") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SOFTWAREENGINEERING") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUPERABUNDANCE") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUPERABUNDANCE") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "TENACIOUS") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TENACIOUS") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "FAIR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FAIR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLOWORLDHELLOWORLD") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLOWORLDHELLOWORLD") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "REFACTOR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REFACTOR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "SATISFACTION") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SATISFACTION") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALGORITHMSANDDATA") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALGORITHMSANDDATA") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROLIFIC") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROLIFIC") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "GRAPHALGORITHMS") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GRAPHALGORITHMS") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAREFUL") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAREFUL") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "ECONOMY") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ECONOMY") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "OUTSTANDING") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OUTSTANDING") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "GREEDYALGORITHM") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GREEDYALGORITHM") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "VIP") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "VIP") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "BAAABBBCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWWXXXXYYYYZZZZZ") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BAAABBBCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWWXXXXYYYYZZZZZ") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "COMPASSION") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COMPASSION") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "ARCHITECTURE") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ARCHITECTURE") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "BELLMANFORD") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BELLMANFORD") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "WORKFLOW") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "WORKFLOW") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "NODEJS") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NODEJS") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "RESILIENT") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RESILIENT") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZYXWVUTSRQPONMLKJIHGFEDCBA") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZYXWVUTSRQPONMLKJIHGFEDCBA") == 36: {e}')
    
    total += 1
    try:
        result = candidate(word = "HAPPINESS") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HAPPINESS") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "RELIABLE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RELIABLE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "POWERFUL") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "POWERFUL") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "PERFECT") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PERFECT") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRUSTWORTHY") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRUSTWORTHY") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRANSPARENT") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRANSPARENT") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "MINIMIZE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MINIMIZE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "COMPLEXITY") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "COMPLEXITY") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "TENDER") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TENDER") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ACCEPTANCE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ACCEPTANCE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLASK") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLASK") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "KNOWLEDGE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KNOWLEDGE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "RICH") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RICH") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "ENVIRONMENT") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ENVIRONMENT") == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "GAINED") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GAINED") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "DISCOVER") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DISCOVER") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "DOUBTFREE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DOUBTFREE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "LUXURIOUS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LUXURIOUS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "SECURITY") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SECURITY") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "INDUSTRY") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INDUSTRY") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "MOVEMENTOFKEYS") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MOVEMENTOFKEYS") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "DJANGO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DJANGO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "FUNCTIONCALLSARE") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FUNCTIONCALLSARE") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONSCIENTIOUS") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONSCIENTIOUS") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLOORLD") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLOORLD") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "REVISION") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REVISION") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "INNOVATION") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INNOVATION") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXCLUSIVE") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXCLUSIVE") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "SURE") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SURE") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRUST") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRUST") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "DYNAMICPROGRAMMING") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DYNAMICPROGRAMMING") == 31: {e}')
    
    total += 1
    try:
        result = candidate(word = "LEARN") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LEARN") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "SUCCESS") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SUCCESS") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCC") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCC") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "EVOLUTION") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EVOLUTION") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "SOLUTION") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SOLUTION") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPPORTUNITY") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPPORTUNITY") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABUNDANT") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABUNDANT") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "FAILURE") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FAILURE") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "REVOLUTION") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REVOLUTION") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "SEQUENCE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SEQUENCE") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERFINGERFINGER") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERFINGERFINGER") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "LINKEDLIST") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LINKEDLIST") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXPERIENCE") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXPERIENCE") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPEN") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPEN") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "LOVE") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LOVE") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "CONCLUSION") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CONCLUSION") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "SKILL") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SKILL") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "EVALUATION") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EVALUATION") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "FINGERTYPINGISFUN") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FINGERTYPINGISFUN") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "MAGNIFICENT") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MAGNIFICENT") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "LEETCODE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LEETCODE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "CUSTOMER") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CUSTOMER") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "STRIGHT") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STRIGHT") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "SPACECOMPLEXITY") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SPACECOMPLEXITY") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEPENDABLE") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEPENDABLE") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEVELOPER") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEVELOPER") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXPRESS") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXPRESS") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "KEYPADTYPING") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KEYPADTYPING") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "PROFESSION") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PROFESSION") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "REPOSITION") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "REPOSITION") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "KNAPSACKPROBLEM") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "KNAPSACKPROBLEM") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "DESIGN") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DESIGN") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEBUG") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEBUG") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRACING") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRACING") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "STURDY") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STURDY") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "WEALTH") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "WEALTH") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "TRANSFORMATION") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TRANSFORMATION") == 29: {e}')
    
    total += 1
    try:
        result = candidate(word = "EFFORT") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EFFORT") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "EXERCISE") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EXERCISE") == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "QWERTYUIOPASDFGHJKLZXCVBNM") == 52
    assert candidate(word = "ZZZZZ") == 0
    assert candidate(word = "CAKE") == 3
    assert candidate(word = "RHYTHM") == 9
    assert candidate(word = "FINGER") == 8
    assert candidate(word = "ALPHABET") == 12
    assert candidate(word = "ABCD") == 2
    assert candidate(word = "QWERTYUIOPASDFGHJKLMZXCVBNM") == 54
    assert candidate(word = "NEW") == 3
    assert candidate(word = "HAPPY") == 6
    assert candidate(word = "ABCMN") == 3
    assert candidate(word = "LONGEST") == 8
    assert candidate(word = "MISSISSIPPI") == 5
    assert candidate(word = "YEAR") == 7
    assert candidate(word = "ZXY") == 1
    assert candidate(word = "OPTIMIZATION") == 17
    assert candidate(word = "YYYYYY") == 0
    assert candidate(word = "ACB") == 1
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 36
    assert candidate(word = "MOUSE") == 5
    assert candidate(word = "ZZZZ") == 0
    assert candidate(word = "AA") == 0
    assert candidate(word = "TRANSFER") == 15
    assert candidate(word = "ABCDEFGHIJKLMNOP") == 18
    assert candidate(word = "PYTHON") == 6
    assert candidate(word = "QRSTUVWXYZ") == 12
    assert candidate(word = "KEYBOARD") == 15
    assert candidate(word = "ABAB") == 0
    assert candidate(word = "A") == 0
    assert candidate(word = "ABCDEFG") == 5
    assert candidate(word = "DISTANCE") == 11
    assert candidate(word = "ALGORITHMS") == 14
    assert candidate(word = "CAPABILITY") == 13
    assert candidate(word = "HASHMAP") == 9
    assert candidate(word = "LONGWORDLONGWORDLONGWORDLONGWORDLONGWORDLONGWORDLONGWORD") == 122
    assert candidate(word = "SPECIAL") == 12
    assert candidate(word = "DEPLOYMENT") == 14
    assert candidate(word = "VOLCANOES") == 15
    assert candidate(word = "VICTORY") == 10
    assert candidate(word = "BACKSPACENOTPOSSIBLE") == 35
    assert candidate(word = "PROSPERING") == 18
    assert candidate(word = "METHOD") == 7
    assert candidate(word = "ROBUST") == 7
    assert candidate(word = "PLANNING") == 11
    assert candidate(word = "JOY") == 2
    assert candidate(word = "DEPTHFIRSTSEARCH") == 29
    assert candidate(word = "CONCEPT") == 7
    assert candidate(word = "INTEGRATION") == 19
    assert candidate(word = "PLENTY") == 7
    assert candidate(word = "COORDINATION") == 18
    assert candidate(word = "ACCOMPLISHED") == 18
    assert candidate(word = "RUBY") == 7
    assert candidate(word = "SERVER") == 10
    assert candidate(word = "PYTHONIC") == 8
    assert candidate(word = "PRODUCT") == 8
    assert candidate(word = "JUST") == 3
    assert candidate(word = "RESEARCH") == 13
    assert candidate(word = "PYTHONCODING") == 15
    assert candidate(word = "INITIATION") == 9
    assert candidate(word = "OBJECTORIENTED") == 22
    assert candidate(word = "REQUIREMENT") == 15
    assert candidate(word = "BANANA") == 1
    assert candidate(word = "FINANCE") == 10
    assert candidate(word = "HELLOFROMTHEOTHERSIDE") == 35
    assert candidate(word = "DEDICATED") == 10
    assert candidate(word = "SUPERLONGWORD") == 23
    assert candidate(word = "ACCOMPLISHMENT") == 20
    assert candidate(word = "PROGRAMMER") == 13
    assert candidate(word = "SPECIALCHARACTERS") == 32
    assert candidate(word = "NETWORK") == 10
    assert candidate(word = "AWESOME") == 11
    assert candidate(word = "PROGRESS") == 9
    assert candidate(word = "WIN") == 2
    assert candidate(word = "OBJECTIVE") == 15
    assert candidate(word = "FLOURISH") == 10
    assert candidate(word = "PROSPEROUS") == 16
    assert candidate(word = "EXPERIMENT") == 14
    assert candidate(word = "FINGERBOARD") == 20
    assert candidate(word = "PATIENCE") == 13
    assert candidate(word = "ADJUSTMENT") == 13
    assert candidate(word = "EXCEL") == 6
    assert candidate(word = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS") == 59
    assert candidate(word = "FRANK") == 7
    assert candidate(word = "SOFTWARE") == 18
    assert candidate(word = "TWOPOINTERS") == 15
    assert candidate(word = "ANALYSIS") == 13
    assert candidate(word = "RESOLUTION") == 15
    assert candidate(word = "LONGWORDFORTESTING") == 32
    assert candidate(word = "INTERACTION") == 18
    assert candidate(word = "UNOBTRUDES") == 17
    assert candidate(word = "FINGERMOVEMENT") == 20
    assert candidate(word = "PEACE") == 5
    assert candidate(word = "DEPONIBLE") == 11
    assert candidate(word = "ASTARSEARCH") == 22
    assert candidate(word = "ANGULAR") == 10
    assert candidate(word = "SERVICE") == 12
    assert candidate(word = "PROSPERITY") == 19
    assert candidate(word = "RECOGNITION") == 13
    assert candidate(word = "KINDNESS") == 7
    assert candidate(word = "PYTHONPYTHONPYTHON") == 26
    assert candidate(word = "PARTNER") == 12
    assert candidate(word = "IDEAL") == 5
    assert candidate(word = "PRODUCTIVE") == 14
    assert candidate(word = "HARMONY") == 10
    assert candidate(word = "MYSQL") == 5
    assert candidate(word = "PYTHONISFUN") == 17
    assert candidate(word = "UNIVERSAL") == 16
    assert candidate(word = "KEYBOARDLAYOUT") == 29
    assert candidate(word = "SAFE") == 4
    assert candidate(word = "TYPESCRIPT") == 20
    assert candidate(word = "TREE") == 3
    assert candidate(word = "FINGERFINGER") == 20
    assert candidate(word = "AAAAA") == 0
    assert candidate(word = "GENTLE") == 7
    assert candidate(word = "ETHICAL") == 8
    assert candidate(word = "BACKTRACKING") == 21
    assert candidate(word = "AFFLUENT") == 11
    assert candidate(word = "TIMECOMPLEXITY") == 27
    assert candidate(word = "HUMBLE") == 11
    assert candidate(word = "API") == 2
    assert candidate(word = "OVERCOME") == 14
    assert candidate(word = "DOBRE") == 8
    assert candidate(word = "PRACTICE") == 13
    assert candidate(word = "PLAIN") == 8
    assert candidate(word = "ACHIEVEMENT") == 14
    assert candidate(word = "COMPUTERSCIENCE") == 28
    assert candidate(word = "SUCCESSFUL") == 9
    assert candidate(word = "GOAL") == 5
    assert candidate(word = "CHANGE") == 9
    assert candidate(word = "FULFILLMENT") == 12
    assert candidate(word = "PRINCIPLE") == 13
    assert candidate(word = "CODER") == 5
    assert candidate(word = "ALLOCATION") == 13
    assert candidate(word = "DIJKSTRAS") == 14
    assert candidate(word = "INTERPRETATION") == 22
    assert candidate(word = "INTEGRITY") == 16
    assert candidate(word = "HACK") == 4
    assert candidate(word = "QWJRTYUPASDFGZXCVB") == 43
    assert candidate(word = "SUPERLATIVE") == 23
    assert candidate(word = "PERSISTENT") == 16
    assert candidate(word = "MULTIPLEFINGERS") == 24
    assert candidate(word = "OPERATION") == 16
    assert candidate(word = "DELIVERY") == 14
    assert candidate(word = "DETERMINATION") == 20
    assert candidate(word = "DATASTRUCTURE") == 24
    assert candidate(word = "CALCULATION") == 19
    assert candidate(word = "OPULANCE") == 15
    assert candidate(word = "TOP") == 1
    assert candidate(word = "SIMULATION") == 19
    assert candidate(word = "ATTENTIVE") == 12
    assert candidate(word = "PROFILING") == 9
    assert candidate(word = "EFFICIENT") == 7
    assert candidate(word = "MEMORYMANAGEMENT") == 26
    assert candidate(word = "STRATEGY") == 18
    assert candidate(word = "THRIVE") == 9
    assert candidate(word = "ENERGETIC") == 15
    assert candidate(word = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG") == 73
    assert candidate(word = "CUSTOMIZATION") == 20
    assert candidate(word = "OPTIMIZE") == 11
    assert candidate(word = "ELITE") == 6
    assert candidate(word = "PROGRAMMINGISFUN") == 24
    assert candidate(word = "COMMITTED") == 9
    assert candidate(word = "EFFECTIVE") == 10
    assert candidate(word = "REPORT") == 6
    assert candidate(word = "SPACESAVING") == 22
    assert candidate(word = "INTERFACE") == 15
    assert candidate(word = "NEURALNETWORKS") == 29
    assert candidate(word = "CORRECT") == 9
    assert candidate(word = "KNIGHTMARCH") == 17
    assert candidate(word = "SIMPLE") == 8
    assert candidate(word = "TECHNOLOGY") == 16
    assert candidate(word = "QUEUE") == 2
    assert candidate(word = "ABACAXABABACAB") == 15
    assert candidate(word = "PROGRAMMING") == 14
    assert candidate(word = "SEARCH") == 10
    assert candidate(word = "MULTIPLEWORDSHEREANDTHERE") == 49
    assert candidate(word = "LOAD") == 7
    assert candidate(word = "CONFIDENT") == 11
    assert candidate(word = "HTML") == 4
    assert candidate(word = "SECURE") == 10
    assert candidate(word = "MECHANISM") == 13
    assert candidate(word = "WEALTHY") == 15
    assert candidate(word = "FLAWLESS") == 12
    assert candidate(word = "MORAL") == 6
    assert candidate(word = "RESPONSIBLE") == 19
    assert candidate(word = "DEVOTED") == 6
    assert candidate(word = "PASSIONATE") == 15
    assert candidate(word = "RANDOMKEYPAD") == 24
    assert candidate(word = "BACKSPACENEEDED") == 20
    assert candidate(word = "JAVA") == 2
    assert candidate(word = "CHALLENGE") == 11
    assert candidate(word = "PRESENTATION") == 17
    assert candidate(word = "BOOMING") == 7
    assert candidate(word = "HELLOWORLD") == 13
    assert candidate(word = "EQUITABLE") == 16
    assert candidate(word = "GREATEST") == 10
    assert candidate(word = "DATASTRUCTURES") == 26
    assert candidate(word = "EXCELLENCE") == 14
    assert candidate(word = "PRECISE") == 10
    assert candidate(word = "OBTAINED") == 11
    assert candidate(word = "EXECUTION") == 9
    assert candidate(word = "DELICATE") == 11
    assert candidate(word = "KRUSKALSMST") == 16
    assert candidate(word = "AAABBBCCCDDD") == 2
    assert candidate(word = "BEST") == 4
    assert candidate(word = "ABCDEFGHIJABCDEFGHIJ") == 24
    assert candidate(word = "EXEMPLARY") == 19
    assert candidate(word = "PRIMSMST") == 9
    assert candidate(word = "MANAGER") == 10
    assert candidate(word = "RELATIONSHIP") == 19
    assert candidate(word = "COMMUNICATION") == 15
    assert candidate(word = "FINGERPRINT") == 17
    assert candidate(word = "RECOMMENDATION") == 18
    assert candidate(word = "MULTITHREADING") == 24
    assert candidate(word = "MEETING") == 8
    assert candidate(word = "TRIUMPHANT") == 17
    assert candidate(word = "PRIDE") == 5
    assert candidate(word = "STRETCH") == 8
    assert candidate(word = "FINGERLATERALMOVEMENT") == 38
    assert candidate(word = "CLIENT") == 6
    assert candidate(word = "BOOM") == 2
    assert candidate(word = "AFFLUENCE") == 13
    assert candidate(word = "CONSECUTIVE") == 16
    assert candidate(word = "GREAT") == 8
    assert candidate(word = "MARKET") == 9
    assert candidate(word = "GENUINE") == 8
    assert candidate(word = "BIGDATAANALYSIS") == 24
    assert candidate(word = "CONVINCED") == 10
    assert candidate(word = "UNIT") == 3
    assert candidate(word = "CONFIGURATION") == 25
    assert candidate(word = "PLAN") == 6
    assert candidate(word = "ADAPTABLE") == 13
    assert candidate(word = "TEAMWORK") == 15
    assert candidate(word = "AAAAAAAAA") == 0
    assert candidate(word = "ACHIEVE") == 8
    assert candidate(word = "UTILIZATION") == 17
    assert candidate(word = "THRIVING") == 10
    assert candidate(word = "PERFORMANCE") == 20
    assert candidate(word = "MODEST") == 6
    assert candidate(word = "DEVELOPMENT") == 13
    assert candidate(word = "ACHIEVED") == 9
    assert candidate(word = "BREADTHFIRSTSEARCH") == 35
    assert candidate(word = "ASSURED") == 9
    assert candidate(word = "TRIUMPH") == 12
    assert candidate(word = "ENTHUSIASTIC") == 17
    assert candidate(word = "BUSINESS") == 11
    assert candidate(word = "PHP") == 0
    assert candidate(word = "EARNED") == 10
    assert candidate(word = "BBBBC") == 0
    assert candidate(word = "LONGKEYSEQUENCE") == 20
    assert candidate(word = "RIGHT") == 5
    assert candidate(word = "PERFECTION") == 14
    assert candidate(word = "PRINCIPLED") == 14
    assert candidate(word = "DEBUGGINGISSLOW") == 23
    assert candidate(word = "GUARANTEED") == 13
    assert candidate(word = "PROSPER") == 11
    assert candidate(word = "SYNCHRONIZATION") == 25
    assert candidate(word = "ACCOUNTABLE") == 14
    assert candidate(word = "VIVACIOUS") == 10
    assert candidate(word = "ACCURATE") == 14
    assert candidate(word = "INITIALIZE") == 17
    assert candidate(word = "ABUNDANCE") == 12
    assert candidate(word = "EXACT") == 10
    assert candidate(word = "PREMIERE") == 12
    assert candidate(word = "PNEUMONULA") == 19
    assert candidate(word = "SYNTAXERRORHANDLING") == 36
    assert candidate(word = "PYTHONANDJAVA") == 15
    assert candidate(word = "PROBLEM") == 10
    assert candidate(word = "DECIDED") == 4
    assert candidate(word = "INFORMATION") == 18
    assert candidate(word = "CODINGCHALLENGES") == 23
    assert candidate(word = "TRANSACTION") == 16
    assert candidate(word = "CONTESTSAREFUN") == 24
    assert candidate(word = "DYNAMIC") == 11
    assert candidate(word = "PATTERN") == 11
    assert candidate(word = "CONCURRENT") == 12
    assert candidate(word = "TEST") == 2
    assert candidate(word = "SUPERIOR") == 10
    assert candidate(word = "LOVEPYTHON") == 17
    assert candidate(word = "COLLABORATION") == 22
    assert candidate(word = "MINIMALIZATION") == 20
    assert candidate(word = "MACHINELEARNING") == 28
    assert candidate(word = "PLETHORA") == 16
    assert candidate(word = "MEMORIZATION") == 21
    assert candidate(word = "PROTECTED") == 11
    assert candidate(word = "JAVASCRIPT") == 19
    assert candidate(word = "EXCEPTIONAL") == 20
    assert candidate(word = "FLOURISHING") == 15
    assert candidate(word = "COORDINATOR") == 17
    assert candidate(word = "VARIABLESANDTYPES") == 33
    assert candidate(word = "TEAM") == 6
    assert candidate(word = "TRAVELINGSALESMANPROBLEM") == 51
    assert candidate(word = "VUE") == 1
    assert candidate(word = "DIRECT") == 10
    assert candidate(word = "AVOIDDISTANCE") == 17
    assert candidate(word = "PREMIUM") == 10
    assert candidate(word = "FLEXIBLE") == 12
    assert candidate(word = "CPLUSPLUS") == 15
    assert candidate(word = "BUG") == 2
    assert candidate(word = "COOLCODE") == 8
    assert candidate(word = "CONGRATULATIONS") == 25
    assert candidate(word = "MONGODB") == 8
    assert candidate(word = "NETWORKFLOW") == 16
    assert candidate(word = "SIMULATEDANNEALING") == 34
    assert candidate(word = "STRONG") == 6
    assert candidate(word = "POSTGRESQL") == 17
    assert candidate(word = "TARGET") == 11
    assert candidate(word = "PROJECT") == 10
    assert candidate(word = "ARTIFICIALINTELLIGENCE") == 37
    assert candidate(word = "DATABASE") == 10
    assert candidate(word = "RECURSION") == 13
    assert candidate(word = "REACT") == 9
    assert candidate(word = "FRAMEWORK") == 16
    assert candidate(word = "OPTIMAL") == 10
    assert candidate(word = "REACHED") == 8
    assert candidate(word = "EXCELLENT") == 12
    assert candidate(word = "KANGAROO") == 11
    assert candidate(word = "GENETICALGORITHM") == 24
    assert candidate(word = "STRESS") == 5
    assert candidate(word = "PYTHONPROGRAMMING") == 23
    assert candidate(word = "GRAPH") == 5
    assert candidate(word = "MIGHTY") == 6
    assert candidate(word = "HONEST") == 6
    assert candidate(word = "ACCELERATION") == 18
    assert candidate(word = "XYLOPHONE") == 15
    assert candidate(word = "LUXURY") == 6
    assert candidate(word = "LOYAL") == 8
    assert candidate(word = "DIVIDEANDCONQUER") == 25
    assert candidate(word = "IDENTIFICATION") == 19
    assert candidate(word = "HONORABLE") == 11
    assert candidate(word = "TYPINGISAWAYTORELAX") == 37
    assert candidate(word = "ENGINEERING") == 15
    assert candidate(word = "TYPINGWITHTWOFINGERS") == 39
    assert candidate(word = "COMPANY") == 10
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 84
    assert candidate(word = "ARRAY") == 4
    assert candidate(word = "CSS") == 0
    assert candidate(word = "CYBER") == 7
    assert candidate(word = "ENGINEER") == 9
    assert candidate(word = "FUTURE") == 7
    assert candidate(word = "APPLICATION") == 14
    assert candidate(word = "STACK") == 6
    assert candidate(word = "VICTORIOUS") == 13
    assert candidate(word = "IMPLEMENTATION") == 18
    assert candidate(word = "HELLOUNIVERSE") == 23
    assert candidate(word = "PROCESS") == 9
    assert candidate(word = "FUNCTION") == 9
    assert candidate(word = "CAREER") == 6
    assert candidate(word = "INITIATIVE") == 12
    assert candidate(word = "RESULT") == 8
    assert candidate(word = "EMPATHY") == 12
    assert candidate(word = "ABILITY") == 8
    assert candidate(word = "SUPPLIER") == 10
    assert candidate(word = "INTERVENTION") == 20
    assert candidate(word = "ATTAINED") == 8
    assert candidate(word = "ALGORITHM") == 13
    assert candidate(word = "LEADER") == 7
    assert candidate(word = "SOFTWAREENGINEERING") == 36
    assert candidate(word = "SUPERABUNDANCE") == 26
    assert candidate(word = "TENACIOUS") == 11
    assert candidate(word = "FAIR") == 5
    assert candidate(word = "HELLOWORLDHELLOWORLD") == 29
    assert candidate(word = "REFACTOR") == 14
    assert candidate(word = "SATISFACTION") == 20
    assert candidate(word = "ALGORITHMSANDDATA") == 26
    assert candidate(word = "PROLIFIC") == 5
    assert candidate(word = "GRAPHALGORITHMS") == 24
    assert candidate(word = "CAREFUL") == 12
    assert candidate(word = "ECONOMY") == 7
    assert candidate(word = "OUTSTANDING") == 12
    assert candidate(word = "GREEDYALGORITHM") == 27
    assert candidate(word = "VIP") == 1
    assert candidate(word = "BAAABBBCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWWXXXXYYYYZZZZZ") == 36
    assert candidate(word = "COMPASSION") == 12
    assert candidate(word = "ARCHITECTURE") == 20
    assert candidate(word = "BELLMANFORD") == 17
    assert candidate(word = "WORKFLOW") == 10
    assert candidate(word = "NODEJS") == 7
    assert candidate(word = "RESILIENT") == 14
    assert candidate(word = "ZYXWVUTSRQPONMLKJIHGFEDCBA") == 36
    assert candidate(word = "HAPPINESS") == 12
    assert candidate(word = "RELIABLE") == 10
    assert candidate(word = "POWERFUL") == 11
    assert candidate(word = "PERFECT") == 10
    assert candidate(word = "TRUSTWORTHY") == 18
    assert candidate(word = "TRANSPARENT") == 23
    assert candidate(word = "MINIMIZE") == 8
    assert candidate(word = "COMPLEXITY") == 20
    assert candidate(word = "TENDER") == 6
    assert candidate(word = "ACCEPTANCE") == 13
    assert candidate(word = "FLASK") == 5
    assert candidate(word = "KNOWLEDGE") == 13
    assert candidate(word = "RICH") == 3
    assert candidate(word = "ENVIRONMENT") == 17
    assert candidate(word = "GAINED") == 7
    assert candidate(word = "DISCOVER") == 13
    assert candidate(word = "DOUBTFREE") == 13
    assert candidate(word = "LUXURIOUS") == 9
    assert candidate(word = "SECURITY") == 14
    assert candidate(word = "INDUSTRY") == 13
    assert candidate(word = "MOVEMENTOFKEYS") == 19
    assert candidate(word = "DJANGO") == 6
    assert candidate(word = "FUNCTIONCALLSARE") == 28
    assert candidate(word = "CONSCIENTIOUS") == 16
    assert candidate(word = "HELLOORLD") == 9
    assert candidate(word = "REVISION") == 11
    assert candidate(word = "INNOVATION") == 12
    assert candidate(word = "EXCLUSIVE") == 18
    assert candidate(word = "SURE") == 5
    assert candidate(word = "TRUST") == 4
    assert candidate(word = "DYNAMICPROGRAMMING") == 31
    assert candidate(word = "LEARN") == 8
    assert candidate(word = "SUCCESS") == 5
    assert candidate(word = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCC") == 1
    assert candidate(word = "EVOLUTION") == 11
    assert candidate(word = "SOLUTION") == 10
    assert candidate(word = "OPPORTUNITY") == 14
    assert candidate(word = "ABUNDANT") == 9
    assert candidate(word = "FAILURE") == 10
    assert candidate(word = "REVOLUTION") == 14
    assert candidate(word = "SEQUENCE") == 11
    assert candidate(word = "FINGERFINGERFINGER") == 32
    assert candidate(word = "LINKEDLIST") == 14
    assert candidate(word = "EXPERIENCE") == 14
    assert candidate(word = "OPEN") == 3
    assert candidate(word = "LOVE") == 4
    assert candidate(word = "CONCLUSION") == 14
    assert candidate(word = "SKILL") == 5
    assert candidate(word = "EVALUATION") == 19
    assert candidate(word = "FINGERTYPINGISFUN") == 32
    assert candidate(word = "MAGNIFICENT") == 13
    assert candidate(word = "LEETCODE") == 8
    assert candidate(word = "CUSTOMER") == 12
    assert candidate(word = "STRIGHT") == 8
    assert candidate(word = "SPACECOMPLEXITY") == 28
    assert candidate(word = "DEPENDABLE") == 13
    assert candidate(word = "DEVELOPER") == 10
    assert candidate(word = "EXPRESS") == 11
    assert candidate(word = "KEYPADTYPING") == 24
    assert candidate(word = "PROFESSION") == 12
    assert candidate(word = "REPOSITION") == 11
    assert candidate(word = "KNAPSACKPROBLEM") == 28
    assert candidate(word = "DESIGN") == 8
    assert candidate(word = "DEBUG") == 6
    assert candidate(word = "TRACING") == 11
    assert candidate(word = "STURDY") == 9
    assert candidate(word = "WEALTH") == 11
    assert candidate(word = "TRANSFORMATION") == 29
    assert candidate(word = "EFFORT") == 5
    assert candidate(word = "EXERCISE") == 11


