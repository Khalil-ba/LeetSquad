def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccrroooaaakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccrroooaaakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcoakroak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcoakroak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrcooakak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrcooakak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "k") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "k") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakroak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakroak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrooooaaaakkkk") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrooooaaaakkkk") == 4: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrroooaaaakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrroooaaaakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccroooakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccroooakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccroakroak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccroakroak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrroooookkkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrroooookkkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrroooaaaaakkkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrroooaaaaakkkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "kakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "kakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "kkkrrrooocccaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "kkkrrrooocccaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrroooaaaaakkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrroooaaaaakkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcrook") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcrook") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crorocroakakak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crorocroakakak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "c") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "c") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crorocakak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crorocakak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrroooaaaakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrroooaaaakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "kroac") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "kroac") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcroaoakk") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcroaoakk") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "kraoc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "kraoc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrooookkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrooookkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrroookkaak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrroookkaak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkaaaaaaaaaaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkaaaaaaaaaaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccccroooooorrrraaaaaakkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccccroooooorrrraaaaaakkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrrrroooooooooookkkkkkkkaaaaaaaaaacrrrrrrroooooooooookkkkkkkkaaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrrrroooooooooookkkkkkkkaaaaaaaaaacrrrrrrroooooooooookkkkkkkkaaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakccccrrroooookkkkroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakccccrrroooookkkkroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcrocroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcrocroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccrroooakkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccrroooakkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakccroakrrrooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakccroakrrrooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrooookaaaakkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrooookaaaakkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkroakkkkroakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkroakkkkroakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkkkkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkkkkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrroookaaaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrroookaaaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakakro") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakakro") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakroakcroakcroakcroakcroak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakroakcroakcroakcroakcroak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcroakccccrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcroakccccrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrooooookkkkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrooooookkkkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccrrrrooooaaaakkkkccrrrrooooaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccrrrrooooaaaakkkkccrrrrooooaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrccrooaaakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrccrooaaakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccrrooookkkkraaacroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccrrooookkkkraaacroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakccroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakccroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrroooookkkkaaaakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrroooookkkkaaaakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccrooookkkkrrrooookkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccrooookkkkrrrooookkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrcroakroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrcroakroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakccroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakccroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrroooookkkkkaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrroooookkkkkaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcrocroakcrocroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcrocroakcrocroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkrooocrakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkrooocrakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakrakok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakrakok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakrocakrocak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakrocakrocak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcrocakcroakcrocakcrocak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcrocakcroakcrocakcrocak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkrooocrakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkrooocrakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcoakrcoak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcoakrcoak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrrooooookkkkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrrooooookkkkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroooaaaaakkkakkkakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroooaaaaakkkakkkakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroooaaaaakkkakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroooaaaaakkkakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crorocokakak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crorocokakak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcrrooakroakroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcrrooakroakroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakkaakrook") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakkaakrook") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakroakroakroakroakroakroakroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakroakroakroakroakroakroakroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrooookaaaakkkkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrooookaaaakkkkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakccrookraaaakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakccrookraaaakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccccccrrrrrroooooookkkkkkkkkkkaaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccccccrrrrrroooooookkkkkkkkkkkaaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakrcoakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakrcoakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkrooocrakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkrooocrakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrooooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrooooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrocrocrocroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrocrocrocroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrroooookkkkaaaak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrroooookkkkaaaak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkkkrrroooooooaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkkkrrroooooooaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcoakroakcrcoakroak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcoakroakcrcoakroak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrocrocrocrocroakroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrocrocrocrocroakroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakroakcroakcroak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakroakcroakcroak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrcooakokrakraokakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrcooakokrakraokakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrroooookkkkaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrroooookkkkaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroooaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroooaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkkkkkkkkroakroakroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkkkkkkkkroakroakroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccccroooooorrrraaaaaakkkkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccccroooooorrrraaaaaakkkkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcroakroakcrcoak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcroakroakcrcoak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrrroooookkkkaaaak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrrroooookkkkaaaak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcoakrcoakrcoak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcoakrcoakrcoak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrooookkkkaaaakkkkroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrooookkkkaaaakkkkroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccccccrrrrrrrrrrroooooooooookkkkkkkkaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccccccrrrrrrrrrrroooooooooookkkkkkkkaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrooakrkkaocroakcraok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrooakrkkaocroakcraok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crorarokkorakocraok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crorarokkorakocraok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakroakroakcroakroakroakroakcroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakroakroakcroakroakroakroakcroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkaaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkaaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccrroooraaakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccrroooraaakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrocrocrocroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrocrocrocroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroooraaaakkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroooraaaakkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcrorocroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcrorocroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrrroooookkkkaaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrrroooookkkkaaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroooaarrrkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroooaarrrkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroooaaaaakkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroooaaaaakkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrrrrrrroooooooooookkkkkkkkaaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrrrrrrroooooooooookkkkkkkkaaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrroooaakkccrooakaakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrroooaakkccrooakaakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrrroooookkkkaaaacccrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrrroooookkkkaaaacccrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccroakcroakcroakroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccroakcroakcroakroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakakroccrooakakro") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakakroccrooakakro") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakroakroakroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakroakroakroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrokakakcroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrokakakcroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccroakccroakccroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccroakccroakccroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccrroooookkkkaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccrroooookkkkaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrroooookkkkac") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrroooookkkkac") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crorokokokakakc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crorokokokakakc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrooookkkkaaacrrrooookkkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrooookkkkaaacrrrooookkkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrroookkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrroookkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrooookkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrooookkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrokakakcroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrokakakcroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccrroooaakkccrooakaakkccrroooaakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccrroooaakkccrooakaakkccrroooaakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkaaaacrrroooookkkkaaaacrrroooookkkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkaaaacrrroooookkkkaaaacrrroooookkkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrrooookkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrrooookkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakroakroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakroakroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrcroakroakroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrcroakroakroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrroookkkkrrroooookkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrroookkkkrrroooookkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrooookkkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrooookkkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrokrocroakakak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrokrocroakakak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrookkcraaacroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrookkcraaacroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrcooakokrakraokak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrcooakokrakraokak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakcrocroakcrocroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakcrocroakcrocroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakccroooaakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakccroooaakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrrrrooooooookkkkkkkaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrrrrooooooookkkkkkkaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakccroaaaakkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakccroaaaakkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakroakroakroakroakroakroakroakroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakroakroakroakroakroakroakroakroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrroooookkkkaaaakkkkkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrroooookkkkaaaakkkkkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrooookkkkaaakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrooookkkkaaakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrcroakroakcroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrcroakroakcroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrroooookkkkaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrroooookkkkaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrroooookkkkaaaakkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrroooookkkkaaaakkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccroakcroakcroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccroakcroakcroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcrocakcroakcrocak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcrocakcroakcrocak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcrcoakroakcrocroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcrcoakroakcrocroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakakroccrooakakroccrooakakro") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakakroccrooakakroccrooakakro") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocroakroakcroakcroakcroakcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocroakroakcroakcroakcroakcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakkkcroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakkkcroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrooorkkkaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrooorkkkaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakok") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakok") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccroooraakk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccroooraakk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrooookkkkkaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrooookkkkkaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrroookkkkrrroooookkkkrrroooookkkk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrroookkkkrrroooookkkkrrroooookkkk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrocrocroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrocrocroakroakroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crocrocrocrocrocrocrocrocrocrocrocrocroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crocrocrocrocrocrocrocrocrocrocrocrocroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcroakcroakcroak") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcroakcroakcroak") == 1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crrrrroooookkkkaaaaacrrrrroooookkkkaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crrrrroooookkkkaaaaacrrrrroooookkkkaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "ccccrrrooookkkkaaaaaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "ccccrrrooookkkkaaaaaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "cccroaaakkkkroooraak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "cccroaaakkkkroooraak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "croakcroakcrocroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "croakcroakcrocroakroak") == -1: {e}')
    
    total += 1
    try:
        result = candidate(croakOfFrogs = "crcroakroakroakroakroakroak") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(croakOfFrogs = "crcroakroakroakroakroakroak") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(croakOfFrogs = "croakcroakcroak") == 1
    assert candidate(croakOfFrogs = "croak") == 1
    assert candidate(croakOfFrogs = "cccrroooaaakkk") == -1
    assert candidate(croakOfFrogs = "crcoakroak") == 2
    assert candidate(croakOfFrogs = "crrcooakak") == -1
    assert candidate(croakOfFrogs = "k") == -1
    assert candidate(croakOfFrogs = "crocakroak") == 2
    assert candidate(croakOfFrogs = "ccccrrrrooooaaaakkkk") == 4
    assert candidate(croakOfFrogs = "crrrroooaaaakkk") == -1
    assert candidate(croakOfFrogs = "ccroooakk") == -1
    assert candidate(croakOfFrogs = "ccroakroak") == 2
    assert candidate(croakOfFrogs = "crrrroooookkkkaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrrroooaaaaakkkkkk") == -1
    assert candidate(croakOfFrogs = "kakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakak") == -1
    assert candidate(croakOfFrogs = "ccccroakroakroak") == -1
    assert candidate(croakOfFrogs = "kkkrrrooocccaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrrroooaaaaakkkkk") == -1
    assert candidate(croakOfFrogs = "croakcrook") == -1
    assert candidate(croakOfFrogs = "crorocroakakak") == -1
    assert candidate(croakOfFrogs = "crocroak") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "c") == -1
    assert candidate(croakOfFrogs = "crorocakak") == -1
    assert candidate(croakOfFrogs = "ccccrrrroooaaaakkk") == -1
    assert candidate(croakOfFrogs = "kroac") == -1
    assert candidate(croakOfFrogs = "crocak") == -1
    assert candidate(croakOfFrogs = "crcroaoakk") == 2
    assert candidate(croakOfFrogs = "kraoc") == -1
    assert candidate(croakOfFrogs = "ccccrrooookkkk") == -1
    assert candidate(croakOfFrogs = "") == 0
    assert candidate(croakOfFrogs = "ccrroookkaak") == -1
    assert candidate(croakOfFrogs = "crocroakakroak") == -1
    assert candidate(croakOfFrogs = "croakcroak") == 1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkaaaaaaaaaaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "ccccccroooooorrrraaaaaakkkkk") == -1
    assert candidate(croakOfFrogs = "ccccrrrrrrroooooooooookkkkkkkkaaaaaaaaaacrrrrrrroooooooooookkkkkkkkaaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "croakccccrrroooookkkkroak") == -1
    assert candidate(croakOfFrogs = "crocroakcrocroakcroak") == -1
    assert candidate(croakOfFrogs = "cccrroooakkkaaaa") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "crocakroakroakroak") == -1
    assert candidate(croakOfFrogs = "croakccroakrrrooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkk") == -1
    assert candidate(croakOfFrogs = "ccccrooookaaaakkkkk") == -1
    assert candidate(croakOfFrogs = "crocakcroakcroak") == -1
    assert candidate(croakOfFrogs = "croakkkkroakkkkroakkkk") == -1
    assert candidate(croakOfFrogs = "croakkkkkkkkkk") == -1
    assert candidate(croakOfFrogs = "crrrroookaaaaaakkkk") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "crcrooakakro") == -1
    assert candidate(croakOfFrogs = "crocakroakcroakcroakcroakcroak") == 2
    assert candidate(croakOfFrogs = "crocroakcroakccccrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrrooooookkkkkaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccrrrrooooaaaakkkkccrrrrooooaaaakkkk") == -1
    assert candidate(croakOfFrogs = "crcrccrooaaakk") == -1
    assert candidate(croakOfFrogs = "cccrrooookkkkraaacroak") == -1
    assert candidate(croakOfFrogs = "croakccroakcroak") == -1
    assert candidate(croakOfFrogs = "ccccrrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "crrroooookkkkaaaakkk") == -1
    assert candidate(croakOfFrogs = "cccrooookkkkrrrooookkkk") == -1
    assert candidate(croakOfFrogs = "crrrcroakroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "croakcroakccroakcroak") == -1
    assert candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crrroooookkkkkaaaakkkk") == -1
    assert candidate(croakOfFrogs = "crocroakcrocroakcrocroak") == -1
    assert candidate(croakOfFrogs = "croakkkkrooocrakcroak") == -1
    assert candidate(croakOfFrogs = "crcrooakrakok") == -1
    assert candidate(croakOfFrogs = "crocakrocakrocak") == -1
    assert candidate(croakOfFrogs = "croakcrocakcroakcrocakcrocak") == -1
    assert candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4
    assert candidate(croakOfFrogs = "croakkkkrooocrakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crcoakrcoak") == -1
    assert candidate(croakOfFrogs = "crrrrooooookkkkkkaaaa") == -1
    assert candidate(croakOfFrogs = "ccccroooaaaaakkkakkkakkk") == -1
    assert candidate(croakOfFrogs = "ccccroooaaaaakkkakkk") == -1
    assert candidate(croakOfFrogs = "crorocokakak") == -1
    assert candidate(croakOfFrogs = "crrrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "croakcrrooakroakroakcroak") == -1
    assert candidate(croakOfFrogs = "crcrooakkaakrook") == -1
    assert candidate(croakOfFrogs = "crocakroakroakroakroakroakroakroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakok") == -1
    assert candidate(croakOfFrogs = "ccccrooookaaaakkkkkkk") == -1
    assert candidate(croakOfFrogs = "ccrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "croakccrookraaaakkk") == -1
    assert candidate(croakOfFrogs = "ccccccccrrrrrroooooookkkkkkkkkkkaaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "crocroakkkk") == -1
    assert candidate(croakOfFrogs = "croakrcoakcroak") == -1
    assert candidate(croakOfFrogs = "croakkkkrooocrakcroakcroak") == -1
    assert candidate(croakOfFrogs = "ccccrrrooooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "crocrocrocrocroakroakroak") == -1
    assert candidate(croakOfFrogs = "crrrroooookkkkaaaak") == -1
    assert candidate(croakOfFrogs = "croakkkkkkrrroooooooaaaaaaa") == -1
    assert candidate(croakOfFrogs = "crcoakroakcrcoakroak") == 2
    assert candidate(croakOfFrogs = "crocrocrocrocrocroakroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkkaaaa") == -1
    assert candidate(croakOfFrogs = "crocakroakcroakcroak") == 2
    assert candidate(croakOfFrogs = "crcrcooakokrakraokakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crrrroooookkkkaaaakkkk") == -1
    assert candidate(croakOfFrogs = "ccccroooaaaakkkk") == -1
    assert candidate(croakOfFrogs = "croakkkkkkkkkkroakroakroakcroak") == -1
    assert candidate(croakOfFrogs = "ccccccroooooorrrraaaaaakkkkkkk") == -1
    assert candidate(croakOfFrogs = "crcroakroakcrcoak") == -1
    assert candidate(croakOfFrogs = "ccrrroooookkkkaaaak") == -1
    assert candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crcoakrcoakrcoak") == -1
    assert candidate(croakOfFrogs = "ccccrrrooookkkkaaaakkkkroakroak") == -1
    assert candidate(croakOfFrogs = "ccccccccrrrrrrrrrrroooooooooookkkkkkkkaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "ccrooakrkkaocroakcraok") == -1
    assert candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakok") == -1
    assert candidate(croakOfFrogs = "crorarokkorakocraok") == -1
    assert candidate(croakOfFrogs = "croakroakroakcroakroakroakroakcroakroakroak") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkaaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "cccrroooraaakk") == -1
    assert candidate(croakOfFrogs = "crocrocrocrocroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "crocroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "ccccroooraaaakkkkk") == -1
    assert candidate(croakOfFrogs = "crocroakroakcroak") == -1
    assert candidate(croakOfFrogs = "crocroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "croakcroakcrorocroak") == -1
    assert candidate(croakOfFrogs = "croakcroakroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crrrrroooookkkkaaaaakkkk") == -1
    assert candidate(croakOfFrogs = "ccccroooaarrrkkk") == -1
    assert candidate(croakOfFrogs = "ccccroooaaaaakkkaaa") == -1
    assert candidate(croakOfFrogs = "crrrrrrrrroooooooooookkkkkkkkaaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "ccrroooaakkccrooakaakk") == -1
    assert candidate(croakOfFrogs = "ccrrroooookkkkaaaacccrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "ccccroakcroakcroakroakcroak") == -1
    assert candidate(croakOfFrogs = "crcrooakakroccrooakakro") == -1
    assert candidate(croakOfFrogs = "croakcroakroakroakroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "ccroakroakroak") == -1
    assert candidate(croakOfFrogs = "crocrokakakcroakroakroak") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4
    assert candidate(croakOfFrogs = "ccroakccroakccroak") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkkk") == -1
    assert candidate(croakOfFrogs = "cccrroooookkkkaaaakkkk") == -1
    assert candidate(croakOfFrogs = "crrrroooookkkkac") == -1
    assert candidate(croakOfFrogs = "crorokokokakakc") == -1
    assert candidate(croakOfFrogs = "crocakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crrrooookkkkaaacrrrooookkkkaaa") == -1
    assert candidate(croakOfFrogs = "crocroakroakroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "ccrroookkaaa") == -1
    assert candidate(croakOfFrogs = "crrrooookkkk") == -1
    assert candidate(croakOfFrogs = "crocrokakakcroakroak") == -1
    assert candidate(croakOfFrogs = "ccrroooaakkccrooakaakkccrroooaakk") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkaaaacrrroooookkkkaaaacrrroooookkkkaaa") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "crcrrooookkkaaa") == -1
    assert candidate(croakOfFrogs = "crocroakroakroakroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crocroakcroak") == -1
    assert candidate(croakOfFrogs = "crrrcroakroakroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "crrroookkkkrrroooookkkk") == -1
    assert candidate(croakOfFrogs = "crrrooookkkkaaa") == -1
    assert candidate(croakOfFrogs = "crocrokrocroakakak") == -1
    assert candidate(croakOfFrogs = "crrookkcraaacroakcroak") == -1
    assert candidate(croakOfFrogs = "crcrcooakokrakraokak") == -1
    assert candidate(croakOfFrogs = "crocroakcrocroakcrocroakcroak") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakccroooaakk") == -1
    assert candidate(croakOfFrogs = "ccccrrrrrrrooooooookkkkkkkaaaaaaa") == -1
    assert candidate(croakOfFrogs = "croakcroakccroaaaakkk") == -1
    assert candidate(croakOfFrogs = "crocroakroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crocroakroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crocroakroakroakroakroakroakroakroakroakroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crrroooookkkkaaaakkkkkkk") == -1
    assert candidate(croakOfFrogs = "ccccrrrooookkkkaaakk") == -1
    assert candidate(croakOfFrogs = "crrcroakroakcroakroakroak") == -1
    assert candidate(croakOfFrogs = "ccccrrrrroooookkkkaaaakkkk") == -1
    assert candidate(croakOfFrogs = "ccccrrroooookkkkaaaakkkk") == -1
    assert candidate(croakOfFrogs = "ccroakcroakcroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "croakcrocakcroakcrocak") == -1
    assert candidate(croakOfFrogs = "ccccrrrrooooaaaakkkkccccrrrrooooaaaakkkk") == 4
    assert candidate(croakOfFrogs = "croakcroakcrcoakroakcrocroak") == -1
    assert candidate(croakOfFrogs = "crcrooakakroccrooakakroccrooakakro") == -1
    assert candidate(croakOfFrogs = "crocakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "crocroakroakcroakcroakcroakcroak") == -1
    assert candidate(croakOfFrogs = "croakkkcroak") == -1
    assert candidate(croakOfFrogs = "ccroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "ccccrooorkkkaa") == -1
    assert candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakok") == -1
    assert candidate(croakOfFrogs = "crcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakokcrcrooakrakok") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "cccroooraakk") == -1
    assert candidate(croakOfFrogs = "crrrooookkkkkaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "crrroookkkkrrroooookkkkrrroooookkkk") == -1
    assert candidate(croakOfFrogs = "crocrocrocroakroakroakroak") == -1
    assert candidate(croakOfFrogs = "crocrocrocrocrocrocrocrocrocrocrocrocroak") == -1
    assert candidate(croakOfFrogs = "croakcroakcroakcroakcroak") == 1
    assert candidate(croakOfFrogs = "crrrooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "crrrrroooookkkkaaaaacrrrrroooookkkkaaaa") == -1
    assert candidate(croakOfFrogs = "ccccrrrooookkkkaaaaaaaaaa") == -1
    assert candidate(croakOfFrogs = "cccroaaakkkkroooraak") == -1
    assert candidate(croakOfFrogs = "croakcroakcrocroakroak") == -1
    assert candidate(croakOfFrogs = "crcroakroakroakroakroakroak") == -1


