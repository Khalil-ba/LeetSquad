def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbaalllooonn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbaalllooonn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "ppooaallbboonn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ppooaallbboonn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "leetcode") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leetcode") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "loonbalxballpoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "loonbalxballpoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkklmmooppqqrrssttuuvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkklmmooppqqrrssttuuvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "axbxcxdxeoylno") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "axbxcxdxeoylno") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbonnallloo") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbonnallloo") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "bal") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bal") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "balon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "bnlbaonlbaonlbaon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bnlbaonlbaonlbaon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "nlaebolko") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "nlaebolko") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balblablaballlaalllooonnnnnnnnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balblablaballlaalllooonnnnnnnnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbaalllllooooonnnnballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbaalllllooooonnnnballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbbaaaaaallllllloooooonnnnnn") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbbaaaaaallllllloooooonnnnnn") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabraballoonballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabraballoonballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "bnlaebolkoonnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bnlaebolkoonnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "blbaloonnnballoonballoonballoonballoonballoonballoonballoonballoon") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "blbaloonnnballoonballoonballoonballoonballoonballoonballoonballoon") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "bablllooonnnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bablllooonnnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "blllllaaaaoonnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "blllllaaaaoonnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "bnaloonballoonballoonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bnaloonballoonballoonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllllllllooooooonnnnnnnnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllllllllooooooonnnnnnnnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balbalbalbalbal") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balbalbalbalbal") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "baloonballoonballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baloonballoonballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "bnllobbannolllobnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bnllobbannolllobnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballlooballlloon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballlooballlloon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "baanlloonnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baanlloonnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloon") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloon") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoon") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoon") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "balooba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balooba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeballoonabcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeballoonabcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbaallonnnbballoonnballoonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbaallonnnbballoonnballoonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "lnoobaalllnobo") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "lnoobaalllnobo") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "blbaloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "blbaloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "balonbalonbalonbalon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balonbalonbalonbalon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonyballoonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonyballoonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoon") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoon") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "blbloonnbaalononballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "blbloonnbaalononballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballbaloonn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballbaloonn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "loballoonbaloonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "loballoonbaloonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonbaloonbaloonballoon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonbaloonbaloonballoon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 17: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballbalbalbalbalbalbal") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballbalbalbalbalbalbal") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonbaloon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonbaloon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "nballoonballoonballoonbaloon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "nballoonballoonballoonbaloon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbblllooonnnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbblllooonnnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllllllllooooonnnnnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllllllllooooonnnnnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balonbalonbalonbalonbalonbalonbalon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balonbalonbalonbalonbalonbalonbalon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonbaloon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonbaloon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllonballlonballlon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllonballlonballlon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonbaloonballoonballoonballoon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonbaloonballoonballoonballoon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonbaloonballoonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonbaloonballoonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "baloobaloobalooballoonballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baloobaloobalooballoonballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "noenolbballo") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noenolbballo") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "bllbaaoonnnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bllbaaoonnnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "baloonbaloonbaloonbaloonbaloonbaloonbaloonbaloon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baloonbaloonbaloonbaloonbaloonbaloonbaloonbaloon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbbaaaaalllllooooonn") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbbaaaaalllllooooonn") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloonballoon") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloonballoon") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballooballloonballoonbaloon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballooballloonballoonbaloon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloonbaloonballoon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloonbaloonballoon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "balbaloobnoallnoobbaalllnoonnoob") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balbaloobnoallnoobbaalllnoonnoob") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonbaloonbaloon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonbaloonbaloon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcbabcabcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcbabcabcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "blablablablablablablablablablaloboon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "blablablablablablablablablablaloboon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "bloonboonballoonbalo") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bloonboonballoonbalo") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballonballoonballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballonballoonballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballooonnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballooonnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 13: {e}')
    
    total += 1
    try:
        result = candidate(text = "bloonbaloonballonballoonballoon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bloonbaloonballonballoonballoon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "bnaloonballoonballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bnaloonballoonballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "loonballballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "loonballballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "baloobaloobaloobalooballoona") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baloobaloobaloobalooballoona") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "blllaaooonnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "blllaaooonnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "lalalallballboonbaloon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "lalalallballboonbaloon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllonballlonballlonballlon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllonballlonballlonballlon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballooonballoonballoonballoon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballooonballoonballoonballoon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbbaaaaalllllooooonnnn") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbbaaaaalllllooooonnnn") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllllllllllooonnnnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllllllllllooonnnnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballooonballoonballoonballoonballoon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballooonballoonballoonballoonballoon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "xxxxxyyyyyzzzzzbbaalllooonn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xxxxxyyyyyzzzzzbbaalllooonn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbaalllllooonnxxxx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbaalllllooonnxxxx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balonbalonbalon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balonbalonbalon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "baaalllooonnballoonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baaalllooonnballoonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijklmnopqrstuvwxyzballoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijklmnopqrstuvwxyzballoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "lllaaabbbooonnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "lllaaabbbooonnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbaalllllooonnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbaalllllooonnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "baloonbaloonbaloonbaloonbaloon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baloonbaloonbaloonbaloonbaloon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "baloobaloobaloobaloobalooballoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baloobaloobaloobaloobalooballoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonbaloonbaloonbaloonbaloon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonbaloonbaloonbaloonbaloon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonbaloonbaloonbaloonballoon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonbaloonbaloonbaloonballoon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllllloooneeeennn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllllloooneeeennn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "lloonnbbaaallooonnxx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "lloonnbbaaallooonnxx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballballoonloonballoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballballoonloonballoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "balltooloon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balltooloon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "xxxxxxxxxxxxxxxx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xxxxxxxxxxxxxxxx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoon") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoon") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "ballllooooooonnn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ballllooooooonnn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllllooonnnnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllllooonnnnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "looballonnoballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "looballonnoballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "balllllllllllllllllllllllllllllllllooonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnballoon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "balllllllllllllllllllllllllllllllllooonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnballoon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "bnllobbannolllobnballoonbnllobbannolllobnballoon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bnllobbannolllobnballoonbnllobbannolllobnballoon") == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "") == 0
    assert candidate(text = "bbaalllooonn") == 1
    assert candidate(text = "ppooaallbboonn") == 1
    assert candidate(text = "leetcode") == 0
    assert candidate(text = "balloonballoonballoonballoonballoon") == 5
    assert candidate(text = "loonbalxballpoon") == 2
    assert candidate(text = "aabbccddeeffgghhiijjkklmmooppqqrrssttuuvvwwxxyyzz") == 0
    assert candidate(text = "axbxcxdxeoylno") == 0
    assert candidate(text = "bbonnallloo") == 1
    assert candidate(text = "bal") == 0
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(text = "ballon") == 0
    assert candidate(text = "balon") == 0
    assert candidate(text = "bnlbaonlbaonlbaon") == 1
    assert candidate(text = "balloonballoon") == 2
    assert candidate(text = "abcde") == 0
    assert candidate(text = "nlaebolko") == 1
    assert candidate(text = "balblablaballlaalllooonnnnnnnnn") == 1
    assert candidate(text = "balloonballoonballoon") == 3
    assert candidate(text = "bbbaalllllooooonnnnballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 12
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 10
    assert candidate(text = "bbbbbaaaaaallllllloooooonnnnnn") == 3
    assert candidate(text = "abracadabraballoonballoon") == 2
    assert candidate(text = "bnlaebolkoonnballoon") == 2
    assert candidate(text = "blbaloonnnballoonballoonballoonballoonballoonballoonballoonballoon") == 9
    assert candidate(text = "bablllooonnnballoon") == 2
    assert candidate(text = "blllllaaaaoonnballoon") == 2
    assert candidate(text = "bnaloonballoonballoonballoon") == 3
    assert candidate(text = "balllllllllooooooonnnnnnnnn") == 1
    assert candidate(text = "balbalbalbalbal") == 0
    assert candidate(text = "baloonballoonballoon") == 2
    assert candidate(text = "bnllobbannolllobnballoon") == 2
    assert candidate(text = "balloonballlooballlloon") == 2
    assert candidate(text = "baanlloonnn") == 1
    assert candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloon") == 6
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoon") == 7
    assert candidate(text = "balooba") == 0
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 16
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 11
    assert candidate(text = "abcdeballoonabcde") == 1
    assert candidate(text = "bbaallonnnbballoonnballoonballoon") == 3
    assert candidate(text = "lnoobaalllnobo") == 2
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 14
    assert candidate(text = "blbaloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 16
    assert candidate(text = "balonbalonbalonbalon") == 2
    assert candidate(text = "balloonyballoonballoon") == 3
    assert candidate(text = "balloonballoonballoonballoonballoonballoon") == 6
    assert candidate(text = "blbloonnbaalononballoon") == 2
    assert candidate(text = "ballbaloonn") == 1
    assert candidate(text = "loballoonbaloonballoon") == 3
    assert candidate(text = "balloonballoonballoonbaloonbaloonballoon") == 5
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 17
    assert candidate(text = "ballbalbalbalbalbalbal") == 0
    assert candidate(text = "balloonballoonbaloon") == 2
    assert candidate(text = "nballoonballoonballoonbaloon") == 3
    assert candidate(text = "abbblllooonnnn") == 1
    assert candidate(text = "balllllllllooooonnnnnn") == 1
    assert candidate(text = "balonbalonbalonbalonbalonbalonbalon") == 3
    assert candidate(text = "balloonbaloon") == 1
    assert candidate(text = "balllonballlonballlon") == 1
    assert candidate(text = "balloonbaloonballoonballoonballoon") == 4
    assert candidate(text = "balloonbaloonballoonballoon") == 3
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 12
    assert candidate(text = "baloobaloobalooballoonballoon") == 2
    assert candidate(text = "noenolbballo") == 1
    assert candidate(text = "bllbaaoonnnballoon") == 2
    assert candidate(text = "baloonbaloonbaloonbaloonbaloonbaloonbaloonbaloon") == 4
    assert candidate(text = "bbbbbaaaaalllllooooonn") == 2
    assert candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloonballoon") == 7
    assert candidate(text = "ballooballloonballoonbaloon") == 3
    assert candidate(text = "balloonballoonbaloonballoonbaloonballoonballoonbaloonbaloonballoon") == 8
    assert candidate(text = "balbaloobnoallnoobbaalllnoonnoob") == 3
    assert candidate(text = "balloonballoonballoonbaloonbaloon") == 4
    assert candidate(text = "abcbabcabcabc") == 0
    assert candidate(text = "blablablablablablablablablablaloboon") == 1
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzballoon") == 2
    assert candidate(text = "bloonboonballoonbalo") == 2
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 15
    assert candidate(text = "ballonballoonballoon") == 2
    assert candidate(text = "balloonballoonballoonballoon") == 4
    assert candidate(text = "ballooonnballoon") == 2
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 13
    assert candidate(text = "bloonbaloonballonballoonballoon") == 4
    assert candidate(text = "bnaloonballoonballoon") == 2
    assert candidate(text = "loonballballoon") == 2
    assert candidate(text = "baloobaloobaloobalooballoona") == 1
    assert candidate(text = "blllaaooonnballoon") == 2
    assert candidate(text = "lalalallballboonbaloon") == 2
    assert candidate(text = "balllonballlonballlonballlon") == 2
    assert candidate(text = "ballooonballoonballoonballoon") == 4
    assert candidate(text = "bbbbbaaaaalllllooooonnnn") == 2
    assert candidate(text = "balllllllllllooonnnnballoon") == 2
    assert candidate(text = "ballooonballoonballoonballoonballoon") == 5
    assert candidate(text = "xxxxxyyyyyzzzzzbbaalllooonn") == 1
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoon") == 8
    assert candidate(text = "abbaalllllooonnxxxx") == 1
    assert candidate(text = "balonbalonbalon") == 1
    assert candidate(text = "baaalllooonnballoonballoon") == 3
    assert candidate(text = "abcdefghijklmnopqrstuvwxyzballoon") == 1
    assert candidate(text = "lllaaabbbooonnn") == 1
    assert candidate(text = "bbaalllllooonnballoon") == 2
    assert candidate(text = "baloonbaloonbaloonbaloonbaloon") == 2
    assert candidate(text = "baloobaloobaloobaloobalooballoon") == 1
    assert candidate(text = "balloonbaloonbaloonbaloonbaloon") == 3
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoonballoon") == 18
    assert candidate(text = "balloonballoonballoonbaloonbaloonbaloonballoon") == 5
    assert candidate(text = "balllllloooneeeennn") == 1
    assert candidate(text = "lloonnbbaaallooonnxx") == 2
    assert candidate(text = "ballballoonloonballoon") == 3
    assert candidate(text = "balltooloon") == 1
    assert candidate(text = "xxxxxxxxxxxxxxxx") == 0
    assert candidate(text = "balloonballoonballoonballoonballoonballoonballoonballoonballoon") == 9
    assert candidate(text = "ballllooooooonnn") == 1
    assert candidate(text = "balllllooonnnnballoon") == 2
    assert candidate(text = "looballonnoballoon") == 2
    assert candidate(text = "balllllllllllllllllllllllllllllllllooonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnballoon") == 2
    assert candidate(text = "bnllobbannolllobnballoonbnllobbannolllobnballoon") == 4


