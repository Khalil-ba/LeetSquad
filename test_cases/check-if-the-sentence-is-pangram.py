def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sentence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "quickbrownfoxjumpsoverthelazydog") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "quickbrownfoxjumpsoverthelazydog") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aaaaabbbbbccccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aaaaabbbbbccccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandmorelettersjusttoextendthelengthofthesentenceevenmorejustformeasurements") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandmorelettersjusttoextendthelengthofthesentenceevenmorejustformeasurements") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hellothere") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hellothere") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazy") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijjklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijjklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello world") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello world") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxyzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxyzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "leetcode") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "leetcode") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thisisaverylongsentencebutnotapangram") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thisisaverylongsentencebutnotapangram") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydog") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydog") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxyzabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxyzabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "mississippi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "mississippi") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelaz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelaz") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijlkmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijlkmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandthenomeofthezebra") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandthenomeofthezebra") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickmovementsoftheenemywilljeopardizethesecurityofthefort") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickmovementsoftheenemywilljeopardizethesecurityofthefort") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "neverjumpoveraslydogquicklyasmyfastcat") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "neverjumpoveraslydogquicklyasmyfastcat") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jumpedoverthelazybrownfoxquickly") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jumpedoverthelazybrownfoxquickly") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thisisaverylongsentencethatwantsyoumakesurethatispangram") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thisisaverylongsentencethatwantsyoumakesurethatispangram") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "everygoodboydoesfine") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "everygoodboydoesfine") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthefly") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthefly") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thefoxjumpedoveralazydogandquicklymunchedberries") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thefoxjumpedoveralazydogandquicklymunchedberries") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickmovofjumpsbxngthevlackdwarf") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickmovofjumpsbxngthevlackdwarf") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "sphinxofblackquartzjudgemyvowels") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "sphinxofblackquartzjudgemyvowels") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydozzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydozzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aabbbcccdddeeefffggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssttttuuuuvvvvwwwwxxxxyyyyzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aabbbcccdddeeefffggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssttttuuuuvvvvwwwwxxxxyyyyzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thisisaverylongsentencethatshouldcontainalllettersquickly") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thisisaverylongsentencethatshouldcontainalllettersquickly") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thebrownfoxjumpsovertheleazydog") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thebrownfoxjumpsovertheleazydog") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "phinxofquizzingjudgesbringsmywonder") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "phinxofquizzingjudgesbringsmywonder") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "packmyboxwithfivedozenliquorjugsquicklyandjudgeeachvowel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "packmyboxwithfivedozenliquorjugsquicklyandjudgeeachvowel") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "vowelsaeiouyzqjfdxhcntrbplsmkgw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "vowelsaeiouyzqjfdxhcntrbplsmkgw") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jumpsquickonthisbrownfox") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jumpsquickonthisbrownfox") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "fivexwiseguysjumpquicklyonthiszanyboat") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "fivexwiseguysjumpquicklyonthiszanyboat") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickmovewiththiszestyjuicebringsvexflation") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickmovewiththiszestyjuicebringsvexflation") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "quickbrownfoxjumpsoverthelazydogquickbrownfoxjumpsoverthelazydog") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "quickbrownfoxjumpsoverthelazydogquickbrownfoxjumpsoverthelazydog") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "pythonprogramminglanguage") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "pythonprogramminglanguage") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "xylophonesarefunbutquickbrownfoxjumpsoverthelazydog") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "xylophonesarefunbutquickbrownfoxjumpsoverthelazydog") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydogy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydogy") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "qwertypoiuytrewqasdfghjklzxcvbnmasdfghjklzxcvbnmqwertyuiopcvbnm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "qwertypoiuytrewqasdfghjklzxcvbnmasdfghjklzxcvbnmqwertyuiopcvbnm") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thesixfatfingersjumpquicklyonthisverylazydog") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thesixfatfingersjumpquicklyonthisverylazydog") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jumpsfoxoverthelazydogquickb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jumpsfoxoverthelazydogquickb") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "sixjovialfellowshavequicklyzippedanddrunkmanybeers") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "sixjovialfellowshavequicklyzippedanddrunkmanybeers") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abacaxypromiseyouanelephantwhoxylophones") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abacaxypromiseyouanelephantwhoxylophones") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jumpedoverthelazydogthequickbrownfox") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jumpedoverthelazydogthequickbrownfox") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "sphinxofblackquartzjudgemyvexzwift") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "sphinxofblackquartzjudgemyvexzwift") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpedoverthelazydogquickly") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpedoverthelazydogquickly") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxy") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "foxjumpsoverthelazydogquickbrown") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "foxjumpsoverthelazydogquickbrown") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thisquestionaboutpangramsissomewhatredundant") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thisquestionaboutpangramsissomewhatredundant") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickbrownfoxjumpsoverthelazydog") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickbrownfoxjumpsoverthelazydog") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jumpedoverthelazydogquickbrownfox") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jumpedoverthelazydogquickbrownfox") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickmovingtonafleetofsixgreyhounds") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickmovingtonafleetofsixgreyhounds") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydogg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydogg") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "howvexinglyquickdaftzebrasjump") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "howvexinglyquickdaftzebrasjump") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "quickbrownfoxjumpsoverthelazydogzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "quickbrownfoxjumpsoverthelazydogzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickmovementsofthejaguarzephyr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickmovementsofthejaguarzephyr") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "quicklyjudginghowvexingzebraflowscanbeverytricky") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "quicklyjudginghowvexingzebraflowscanbeverytricky") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickbrownfoxjumpsoverthelazydogandbackagain") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickbrownfoxjumpsoverthelazydogandbackagain") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklnopqrstuvwxyzabcdefghijklnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklnopqrstuvwxyzabcdefghijklnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jellyoftheplumlovesmeandthemonkeyrinsesupwithgrapejuicequickly") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jellyoftheplumlovesmeandthemonkeyrinsesupwithgrapejuicequickly") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thebrownfoxjumpedoveralazylazydog") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thebrownfoxjumpedoveralazylazydog") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "packmyboxwithfivedozenliquorjugs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "packmyboxwithfivedozenliquorjugs") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "foxjumpsoverthelazydogquickbrownzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "foxjumpsoverthelazydogquickbrownzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "althoughsomehumansareabsolutelyastonishing") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "althoughsomehumansareabsolutelyastonishing") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jovialwaltzsexemplifiesquickbymyflyfriend") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jovialwaltzsexemplifiesquickbymyflyfriend") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "aquickbrownfoxjumpsoverthelazydogs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "aquickbrownfoxjumpsoverthelazydogs") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydo") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghjklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghjklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "veryfewlazydogslikejumpingoverthebigbrownfox") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "veryfewlazydogslikejumpingoverthebigbrownfox") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "therearemanysmallpacksofdifferentbooksinthelibrary") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "therearemanysmallpacksofdifferentbooksinthelibrary") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "jimquicklyzippedvexedfowlsbymyplushog") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "jimquicklyzippedvexedfowlsbymyplushog") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "quickbrownfoxjumpsoverthelazydogs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "quickbrownfoxjumpsoverthelazydogs") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abcdefghijkllllmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abcdefghijkllllmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandmore") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandmore") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "everygoodboydoesfinejustkickslovingmonkeysnearpianoquicksly") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "everygoodboydoesfinejustkickslovingmonkeysnearpianoquicksly") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "pqrsghijklmnabcdefwxyzotuvcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "pqrsghijklmnabcdefwxyzotuvcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "pangramsarefunnywordsusedinyogamatclasses") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "pangramsarefunnywordsusedinyogamatclasses") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpedoverthelazydogandthenranoff") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpedoverthelazydogandthenranoff") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "fourxsixtwoseveneleveneightfivenineninetwozero") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "fourxsixtwoseveneleveneightfivenineninetwozero") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "abracadabracabracadabra") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "abracadabracabracadabra") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "mjklqrswxzytfpuhncideaoxbgvlozmt") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "mjklqrswxzytfpuhncideaoxbgvlozmt") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandcat") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandcat") == True: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thisisaverylongstringsentencethatwillnotbepangram") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thisisaverylongstringsentencethatwillnotbepangram") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "quovadis") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "quovadis") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "thisisaverylongsentencethatjustmightcontainallthelettersofthealphabet") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "thisisaverylongsentencethatjustmightcontainallthelettersofthealphabet") == False: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "everygoodboydoesfineandzestfullyjumpoverlazysnails") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "everygoodboydoesfineandzestfullyjumpoverlazysnails") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sentence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
    assert candidate(sentence = "quickbrownfoxjumpsoverthelazydog") == True
    assert candidate(sentence = "aaaaabbbbbccccc") == False
    assert candidate(sentence = "a") == False
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandmorelettersjusttoextendthelengthofthesentenceevenmorejustformeasurements") == True
    assert candidate(sentence = "hellothere") == False
    assert candidate(sentence = "hello") == False
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazy") == False
    assert candidate(sentence = "abcdefghijjklmnopqrstuvwxyz") == True
    assert candidate(sentence = "hello world") == False
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyzzzzz") == True
    assert candidate(sentence = "leetcode") == False
    assert candidate(sentence = "thisisaverylongsentencebutnotapangram") == False
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydog") == True
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyzabc") == True
    assert candidate(sentence = "mississippi") == False
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelaz") == False
    assert candidate(sentence = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(sentence = "abcdefghijlkmnopqrstuvwxyz") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandthenomeofthezebra") == True
    assert candidate(sentence = "aquickmovementsoftheenemywilljeopardizethesecurityofthefort") == False
    assert candidate(sentence = "neverjumpoveraslydogquicklyasmyfastcat") == False
    assert candidate(sentence = "jumpedoverthelazybrownfoxquickly") == False
    assert candidate(sentence = "thisisaverylongsentencethatwantsyoumakesurethatispangram") == False
    assert candidate(sentence = "everygoodboydoesfine") == False
    assert candidate(sentence = "thequickbrownfoxjumpsoverthefly") == False
    assert candidate(sentence = "thefoxjumpedoveralazydogandquicklymunchedberries") == False
    assert candidate(sentence = "aquickmovofjumpsbxngthevlackdwarf") == False
    assert candidate(sentence = "abcdefghijklnopqrstuvwxyz") == False
    assert candidate(sentence = "sphinxofblackquartzjudgemyvowels") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydozzzzzzzzzz") == False
    assert candidate(sentence = "aabbbcccdddeeefffggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssttttuuuuvvvvwwwwxxxxyyyyzzzz") == True
    assert candidate(sentence = "thisisaverylongsentencethatshouldcontainalllettersquickly") == False
    assert candidate(sentence = "thebrownfoxjumpsovertheleazydog") == False
    assert candidate(sentence = "phinxofquizzingjudgesbringsmywonder") == False
    assert candidate(sentence = "packmyboxwithfivedozenliquorjugsquicklyandjudgeeachvowel") == True
    assert candidate(sentence = "vowelsaeiouyzqjfdxhcntrbplsmkgw") == True
    assert candidate(sentence = "jumpsquickonthisbrownfox") == False
    assert candidate(sentence = "fivexwiseguysjumpquicklyonthiszanyboat") == False
    assert candidate(sentence = "aquickmovewiththiszestyjuicebringsvexflation") == False
    assert candidate(sentence = "quickbrownfoxjumpsoverthelazydogquickbrownfoxjumpsoverthelazydog") == True
    assert candidate(sentence = "pythonprogramminglanguage") == False
    assert candidate(sentence = "xylophonesarefunbutquickbrownfoxjumpsoverthelazydog") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydogy") == True
    assert candidate(sentence = "qwertypoiuytrewqasdfghjklzxcvbnmasdfghjklzxcvbnmqwertyuiopcvbnm") == True
    assert candidate(sentence = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == True
    assert candidate(sentence = "thesixfatfingersjumpquicklyonthisverylazydog") == False
    assert candidate(sentence = "jumpsfoxoverthelazydogquickb") == False
    assert candidate(sentence = "sixjovialfellowshavequicklyzippedanddrunkmanybeers") == False
    assert candidate(sentence = "abacaxypromiseyouanelephantwhoxylophones") == False
    assert candidate(sentence = "jumpedoverthelazydogthequickbrownfox") == False
    assert candidate(sentence = "sphinxofblackquartzjudgemyvexzwift") == True
    assert candidate(sentence = "thequickbrownfoxjumpedoverthelazydogquickly") == False
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxy") == False
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz") == True
    assert candidate(sentence = "foxjumpsoverthelazydogquickbrown") == True
    assert candidate(sentence = "thisquestionaboutpangramsissomewhatredundant") == False
    assert candidate(sentence = "aquickbrownfoxjumpsoverthelazydog") == True
    assert candidate(sentence = "jumpedoverthelazydogquickbrownfox") == False
    assert candidate(sentence = "aquickmovingtonafleetofsixgreyhounds") == False
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydogg") == True
    assert candidate(sentence = "howvexinglyquickdaftzebrasjump") == True
    assert candidate(sentence = "quickbrownfoxjumpsoverthelazydogzzzzzzzzzz") == True
    assert candidate(sentence = "aquickmovementsofthejaguarzephyr") == False
    assert candidate(sentence = "quicklyjudginghowvexingzebraflowscanbeverytricky") == False
    assert candidate(sentence = "aquickbrownfoxjumpsoverthelazydogandbackagain") == True
    assert candidate(sentence = "abcdefghijklnopqrstuvwxyzabcdefghijklnopqrstuvwxyz") == False
    assert candidate(sentence = "jellyoftheplumlovesmeandthemonkeyrinsesupwithgrapejuicequickly") == False
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(sentence = "thebrownfoxjumpedoveralazylazydog") == False
    assert candidate(sentence = "packmyboxwithfivedozenliquorjugs") == True
    assert candidate(sentence = "foxjumpsoverthelazydogquickbrownzzzzzzzzzz") == True
    assert candidate(sentence = "althoughsomehumansareabsolutelyastonishing") == False
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == True
    assert candidate(sentence = "jovialwaltzsexemplifiesquickbymyflyfriend") == False
    assert candidate(sentence = "aquickbrownfoxjumpsoverthelazydogs") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydo") == False
    assert candidate(sentence = "abcdefghjklmnopqrstuvwxyz") == False
    assert candidate(sentence = "veryfewlazydogslikejumpingoverthebigbrownfox") == False
    assert candidate(sentence = "therearemanysmallpacksofdifferentbooksinthelibrary") == False
    assert candidate(sentence = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(sentence = "jimquicklyzippedvexedfowlsbymyplushog") == False
    assert candidate(sentence = "quickbrownfoxjumpsoverthelazydogs") == True
    assert candidate(sentence = "abcdefghijkllllmnopqrstuvwxyz") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandmore") == True
    assert candidate(sentence = "everygoodboydoesfinejustkickslovingmonkeysnearpianoquicksly") == False
    assert candidate(sentence = "pqrsghijklmnabcdefwxyzotuvcd") == True
    assert candidate(sentence = "pangramsarefunnywordsusedinyogamatclasses") == False
    assert candidate(sentence = "thequickbrownfoxjumpedoverthelazydogandthenranoff") == False
    assert candidate(sentence = "fourxsixtwoseveneleveneightfivenineninetwozero") == False
    assert candidate(sentence = "abracadabracabracadabra") == False
    assert candidate(sentence = "mjklqrswxzytfpuhncideaoxbgvlozmt") == True
    assert candidate(sentence = "thequickbrownfoxjumpsoverthelazydogandcat") == True
    assert candidate(sentence = "thisisaverylongstringsentencethatwillnotbepangram") == False
    assert candidate(sentence = "quovadis") == False
    assert candidate(sentence = "thisisaverylongsentencethatjustmightcontainallthelettersofthealphabet") == False
    assert candidate(sentence = "everygoodboydoesfineandzestfullyjumpoverlazysnails") == False


