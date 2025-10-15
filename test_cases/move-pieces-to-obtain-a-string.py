def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(start = "_R",target = "R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_R",target = "R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "___",target = "___") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "___",target = "___") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR",target = "LR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR",target = "LR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "_LL_R",target = "LL__R") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_LL_R",target = "LL__R") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "____",target = "____") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "____",target = "____") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R",target = "_LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R",target = "_LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L",target = "L__R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L",target = "L__R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_L_R",target = "LL_R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_L_R",target = "LL_R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_R",target = "_RR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_R",target = "_RR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L__R__R_",target = "L______RR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L__R__R_",target = "L______RR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R",target = "_L__R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R",target = "_L__R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LL_R",target = "R_L_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LL_R",target = "R_L_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "__L___",target = "L_____") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "__L___",target = "L_____") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRRL",target = "LRRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRRL",target = "LRRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RL",target = "LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RL",target = "LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L",target = "__LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L",target = "__LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRLR",target = "LRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRLR",target = "LRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LL_RR",target = "L_RLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LL_RR",target = "L_RLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_L",target = "LL_") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_L",target = "LL_") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLRL",target = "LRLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLRL",target = "LRLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R",target = "L___R") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R",target = "L___R") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___L",target = "L___R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___L",target = "L___R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_",target = "__LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_",target = "__LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_LRL",target = "RLR_L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_LRL",target = "RLR_L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRLL____",target = "____RRLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRLL____",target = "____RRLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L__R",target = "__LR___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L__R",target = "__LR___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R___L___L___R___R",target = "_______LL___RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R___L___L___R___R",target = "_______LL___RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR___LR___LR____",target = "_L__L___R___R___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR___LR___LR____",target = "_L__L___R___R___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R_L__",target = "L______LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R_L__",target = "L______LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "____L___R___",target = "L___________R") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "____L___R___",target = "L___________R") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_____L_______",target = "_________LR____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_____L_______",target = "_________LR____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_R_R_R_R",target = "RRRRR_____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_R_R_R_R",target = "RRRRR_____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R____L_____",target = "_____R____L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R____L_____",target = "_____R____L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R______L",target = "_____LR_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R______L",target = "_____LR_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___L__R_L",target = "_____LR__L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___L__R_L",target = "_____LR__L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L______R______L",target = "_______LR______") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L______R______L",target = "_______LR______") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_L___R_R",target = "__LR___LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_L___R_R",target = "__LR___LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L___L_",target = "___LR___L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L___L_",target = "___LR___L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L____R____L___",target = "________LR____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L____R____L___",target = "________LR____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R____R",target = "_LR_____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R____R",target = "_LR_____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L_____R",target = "_______LR___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L_____R",target = "_______LR___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_R_R_R_",target = "____RRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_R_R_R_",target = "____RRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R",target = "_L__L__RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R",target = "_L__L__RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__LR_R__",target = "__LR___R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__LR_R__",target = "__LR___R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "___L_R___L___R___",target = "L_____L____R____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "___L_R___L___R___",target = "L_____L____R____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR_L_R_L_R",target = "L_R_L_R_L_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR_L_R_L_R",target = "L_R_L_R_L_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R_L_R",target = "_L__L_R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R_L_R",target = "_L__L_R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L___R_L",target = "____LR__RL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L___R_L",target = "____LR__RL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRR_______LLL",target = "________RRRLLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRR_______LLL",target = "________RRRLLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "__LR__R",target = "____LRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "__LR__R",target = "____LRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___L",target = "____L__LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___L",target = "____L__LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R__L_R__L",target = "_______L___LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R__L_R__L",target = "_______L___LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L___L_R",target = "___LL______R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L___L_R",target = "___LL______R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R__L_R",target = "L______LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R__L_R",target = "L______LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_L_L_L_L",target = "_____LLLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_L_L_L_L",target = "_____LLLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "____L_R_L____",target = "_________LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "____L_R_L____",target = "_________LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R__L__R",target = "__LR____R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R__L__R",target = "__LR____R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R_L",target = "_LR_L_L_R_L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R_L",target = "_LR_L_L_R_L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R_L_R",target = "L___L___R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R_L_R",target = "L___L___R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L___",target = "__LR____L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L___",target = "__LR____L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R",target = "___R_L_RL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R",target = "___R_L_RL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R",target = "_LR_L__RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R",target = "_LR_L__RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___L___R___L",target = "_____R___L___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___L___R___L",target = "_____R___L___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___L___R___L___",target = "_____R____L____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___L___R___L___",target = "_____R____L____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR_LRL__",target = "LRL_L___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR_LRL__",target = "LRL_L___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R____L",target = "______LR_L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R____L",target = "______LR_L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___R___R___L___L___",target = "_______RRR____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___R___R___L___L___",target = "_______RRR____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_R____L____R",target = "____L___R_R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_R____L____R",target = "____L___R_R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_____R__L",target = "L_________RL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_____R__L",target = "L_________RL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___L___R___L___",target = "__________LRLRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___L___R___L___",target = "__________LRLRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "____R_L_R___",target = "R_L_____R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "____R_L_R___",target = "R_L_____R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "___L__R___",target = "L_______R__") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "___L__R___",target = "L_______R__") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R____L____R",target = "____R___L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R____L____R",target = "____R___L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR__LR__LR___",target = "L___R___L___RRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR__LR__LR___",target = "L___R___L___RRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L____R____",target = "____LR____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L____R____",target = "____LR____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRR___LLL",target = "___LLLRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRR___LLL",target = "___LLLRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R_L___R",target = "L___L_R__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R_L___R",target = "L___L_R__") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R___R___R___R___L",target = "___L_____RRR___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R___R___R___R___L",target = "___L_____RRR___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R_L_R_L_R",target = "LL______RRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R_L_R_L_R",target = "LL______RRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L__R_L_R",target = "L_____RLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L__R_L_R",target = "L_____RLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R__L",target = "_R___L_RL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R__L",target = "_R___L_RL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___R___L___R___L",target = "_____RR____L___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___R___L___R___L",target = "_____RR____L___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R_L_R___",target = "_L_R_L_R_L_R____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R_L_R___",target = "_L_R_L_R_L_R____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___L___R",target = "__LR___R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___L___R",target = "__LR___R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "______L_R",target = "L______R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "______L_R",target = "L______R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__L_L___R",target = "___LR____R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__L_L___R",target = "___LR____R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___L___R___R___L___",target = "_____R____R____L___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___L___R___R___L___",target = "_____R____R____L___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_L_L_L",target = "LLLL____") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_L_L_L",target = "LLLL____") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R_L_R_",target = "L_____R_R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R_L_R_",target = "L_____R_R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R_L_R_L_R",target = "_LR_L_R_L_R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R_L_R_L_R",target = "_LR_L_R_L_R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R_L_R_L_R",target = "_L_L_L_RLR_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R_L_R_L_R",target = "_L_L_L_RLR_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___R___L",target = "_____L___RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___R___L",target = "_____L___RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_______L",target = "________LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_______L",target = "________LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_____R_L____",target = "________L_R__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_____R_L____",target = "________L_R__") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R___L_R___",target = "_L_R_L___R____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R___L_R___",target = "_L_R_L___R____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R__L__R",target = "____L___LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R__L__R",target = "____L___LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R__L___R",target = "L_____R____R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R__L___R",target = "L_____R____R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R___L",target = "_LR______") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R___L",target = "_LR______") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R_L___R",target = "L___LR___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R_L___R",target = "L___LR___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R",target = "_LR_L_R_L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R",target = "_LR_L_R_L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRLR_LRL",target = "LRLR_LRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRLR_LRL",target = "LRLR_LRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_____L__",target = "_____LR__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_____L__",target = "_____LR__") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L",target = "__LR__L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L",target = "__LR__L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R_L_R_L",target = "LR_L_R_L_R_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R_L_R_L",target = "LR_L_R_L_R_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_____R___L",target = "________LRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_____R___L",target = "________LRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L____R_____",target = "L_____R_____") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L____R_____",target = "L_____R_____") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R__R__L",target = "_____RR_L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R__R__L",target = "_____RR_L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "___LR___R",target = "L_____RR_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "___LR___R",target = "L_____RR_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L___R_L_R",target = "L_____RR__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L___R_L_R",target = "L_____RR__") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R__L_R",target = "LL______RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R__L_R",target = "LL______RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "______",target = "______") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "______",target = "______") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L_R___L_R",target = "_L_R_L___RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L_R___L_R",target = "_L_R_L___RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_L_L__L___",target = "_L_L___L___L_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_L_L__L___",target = "_L_L___L___L_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R________L",target = "________LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R________L",target = "________LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L___L_R",target = "__LR__L_R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L___L_R",target = "__LR__L_R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R___________L",target = "____________LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R___________L",target = "____________LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___L",target = "__L___R_L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___L",target = "__L___R_L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R___R__L",target = "____L___R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R___R__L",target = "____L___R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_______L_L_R_R",target = "L______L___R_R") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_______L_L_R_R",target = "L______L___R_R") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRRLLL___",target = "___RRRLLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRRLLL___",target = "___RRRLLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L__R__L___R____",target = "L___L__R__R____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L__R__L___R____",target = "L___L__R__R____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R___R___R___L",target = "___L_____RR___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R___R___R___L",target = "___L_____RR___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R__L___",target = "_L_____RL__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R__L___",target = "_L_____RL__") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___L___R",target = "L___L___R___R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___L___R",target = "L___L___R___R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "____L___R__",target = "L_____R____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "____L___R__",target = "L_____R____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R__L_R",target = "_LR__LR_") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R__L_R",target = "_LR__LR_") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L___LR__L____",target = "__LR__LR__L____") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L___LR__L____",target = "__LR__LR__L____") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___R",target = "___L____R") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___R",target = "___L____R") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L___R___L_R",target = "L_____RL___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L___R___L_R",target = "L_____RL___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "__L_R__R_L",target = "L_____R__L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "__L_R__R_L",target = "L_____R__L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L___R__L",target = "L_____R__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L___R__L",target = "L_____R__") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "L_R___R___L___",target = "___L_____R___") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "L_R___R___L___",target = "___L_____R___") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L_R_L_R_R",target = "L______RRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L_R_L_R_R",target = "L______RRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_L___R_L_R",target = "L______LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_L___R_L_R",target = "L______LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "_R_L_R_L____",target = "____LR____LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "_R_L_R_L____",target = "____LR____LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "R_L__R",target = "__LR__") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "R_L__R",target = "__LR__") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(start = "_R",target = "R_") == False
    assert candidate(start = "___",target = "___") == True
    assert candidate(start = "LR",target = "LR") == True
    assert candidate(start = "_LL_R",target = "LL__R") == True
    assert candidate(start = "____",target = "____") == True
    assert candidate(start = "L_R",target = "_LR") == False
    assert candidate(start = "R__L",target = "L__R") == False
    assert candidate(start = "L_L_R",target = "LL_R_") == False
    assert candidate(start = "R_R",target = "_RR") == True
    assert candidate(start = "_L__R__R_",target = "L______RR") == True
    assert candidate(start = "L___R",target = "_L__R") == False
    assert candidate(start = "LL_R",target = "R_L_") == False
    assert candidate(start = "__L___",target = "L_____") == True
    assert candidate(start = "LRRL",target = "LRRL") == True
    assert candidate(start = "RL",target = "LR") == False
    assert candidate(start = "R__L",target = "__LR") == False
    assert candidate(start = "LRLR",target = "LRLR") == True
    assert candidate(start = "LL_RR",target = "L_RLR") == False
    assert candidate(start = "L_L",target = "LL_") == True
    assert candidate(start = "RLRL",target = "LRLR") == False
    assert candidate(start = "L___R",target = "L___R") == True
    assert candidate(start = "R___L",target = "L___R") == False
    assert candidate(start = "R_L_",target = "__LR") == False
    assert candidate(start = "R_LRL",target = "RLR_L") == False
    assert candidate(start = "RRLL____",target = "____RRLL") == False
    assert candidate(start = "R__L__R",target = "__LR___") == False
    assert candidate(start = "L_R___L___L___R___R",target = "_______LL___RR") == False
    assert candidate(start = "LR___LR___LR____",target = "_L__L___R___R___") == False
    assert candidate(start = "L___R_L__",target = "L______LR") == False
    assert candidate(start = "____L___R___",target = "L___________R") == True
    assert candidate(start = "R_____L_______",target = "_________LR____") == False
    assert candidate(start = "R_R_R_R_R",target = "RRRRR_____") == False
    assert candidate(start = "R____L_____",target = "_____R____L") == False
    assert candidate(start = "R______L",target = "_____LR_") == False
    assert candidate(start = "R___L__R_L",target = "_____LR__L") == False
    assert candidate(start = "L______R______L",target = "_______LR______") == False
    assert candidate(start = "R_L_L___R_R",target = "__LR___LR") == False
    assert candidate(start = "R__L___L_",target = "___LR___L") == False
    assert candidate(start = "L____R____L___",target = "________LR____") == False
    assert candidate(start = "L_R____R",target = "_LR_____") == False
    assert candidate(start = "R__L_____R",target = "_______LR___") == False
    assert candidate(start = "R_R_R_R_",target = "____RRRR") == True
    assert candidate(start = "R_L_R_L_R",target = "_L__L__RR") == False
    assert candidate(start = "R__LR_R__",target = "__LR___R_") == False
    assert candidate(start = "___L_R___L___R___",target = "L_____L____R____") == False
    assert candidate(start = "LR_L_R_L_R",target = "L_R_L_R_L_") == False
    assert candidate(start = "L_R_L_R",target = "_L__L_R") == False
    assert candidate(start = "R__L___R_L",target = "____LR__RL") == False
    assert candidate(start = "RRR_______LLL",target = "________RRRLLL") == False
    assert candidate(start = "__LR__R",target = "____LRR") == False
    assert candidate(start = "L___R___L",target = "____L__LR") == False
    assert candidate(start = "L_R__L_R__L",target = "_______L___LR") == False
    assert candidate(start = "R__L___L_R",target = "___LL______R") == False
    assert candidate(start = "_L_R__L_R",target = "L______LR") == False
    assert candidate(start = "L_L_L_L_L",target = "_____LLLL") == False
    assert candidate(start = "____L_R_L____",target = "_________LR") == False
    assert candidate(start = "_L_R__L__R",target = "__LR____R") == False
    assert candidate(start = "R_L_R_L_R_L",target = "_LR_L_L_R_L") == False
    assert candidate(start = "_L_R_L_R",target = "L___L___R") == False
    assert candidate(start = "R_L_R_L___",target = "__LR____L") == False
    assert candidate(start = "R_L_R_L_R",target = "___R_L_RL") == False
    assert candidate(start = "R_L_R_L_R",target = "_LR_L__RR") == False
    assert candidate(start = "R___L___R___L",target = "_____R___L___") == False
    assert candidate(start = "R___L___R___L___",target = "_____R____L____") == False
    assert candidate(start = "LR_LRL__",target = "LRL_L___") == False
    assert candidate(start = "L___R____L",target = "______LR_L") == False
    assert candidate(start = "R___R___R___L___L___",target = "_______RRR____") == False
    assert candidate(start = "_R____L____R",target = "____L___R_R") == False
    assert candidate(start = "L_____R__L",target = "L_________RL") == False
    assert candidate(start = "L___R___L___R___L___",target = "__________LRLRL") == False
    assert candidate(start = "____R_L_R___",target = "R_L_____R_") == False
    assert candidate(start = "___L__R___",target = "L_______R__") == True
    assert candidate(start = "R____L____R",target = "____R___L") == False
    assert candidate(start = "LR__LR__LR___",target = "L___R___L___RRR") == False
    assert candidate(start = "L____R____",target = "____LR____") == False
    assert candidate(start = "RRR___LLL",target = "___LLLRRR") == False
    assert candidate(start = "L_R_L___R",target = "L___L_R__") == False
    assert candidate(start = "L_R___R___R___R___L",target = "___L_____RRR___") == False
    assert candidate(start = "L_R_L_R_L_R",target = "LL______RRR") == False
    assert candidate(start = "_L__R_L_R",target = "L_____RLR") == False
    assert candidate(start = "R_L_R__L",target = "_R___L_RL") == False
    assert candidate(start = "R___R___L___R___L",target = "_____RR____L___") == False
    assert candidate(start = "R_L_R_L_R_L_R___",target = "_L_R_L_R_L_R____") == False
    assert candidate(start = "R___L___R",target = "__LR___R_") == False
    assert candidate(start = "______L_R",target = "L______R_") == False
    assert candidate(start = "R__L_L___R",target = "___LR____R") == False
    assert candidate(start = "R___L___R___R___L___",target = "_____R____R____L___") == False
    assert candidate(start = "_L_L_L_L",target = "LLLL____") == True
    assert candidate(start = "_L_R_L_R_",target = "L_____R_R") == False
    assert candidate(start = "L_R_L_R_L_R",target = "_LR_L_R_L_R") == False
    assert candidate(start = "L_R_L_R_L_R",target = "_L_L_L_RLR_") == False
    assert candidate(start = "L___R___R___L",target = "_____L___RR") == False
    assert candidate(start = "R_______L",target = "________LR") == False
    assert candidate(start = "L_____R_L____",target = "________L_R__") == False
    assert candidate(start = "R_L_R___L_R___",target = "_L_R_L___R____") == False
    assert candidate(start = "_L_R__L__R",target = "____L___LR") == False
    assert candidate(start = "_L_R__L___R",target = "L_____R____R") == False
    assert candidate(start = "R_L_R___L",target = "_LR______") == False
    assert candidate(start = "L_R_L___R",target = "L___LR___") == False
    assert candidate(start = "R_L_R_L_R",target = "_LR_L_R_L") == False
    assert candidate(start = "LRLR_LRL",target = "LRLR_LRL") == True
    assert candidate(start = "R_____L__",target = "_____LR__") == False
    assert candidate(start = "R_L_R_L",target = "__LR__L") == False
    assert candidate(start = "R_L_R_L_R_L",target = "LR_L_R_L_R_") == False
    assert candidate(start = "L_____R___L",target = "________LRL") == False
    assert candidate(start = "_L____R_____",target = "L_____R_____") == True
    assert candidate(start = "R__R__L",target = "_____RR_L") == False
    assert candidate(start = "___LR___R",target = "L_____RR_") == False
    assert candidate(start = "_L___R_L_R",target = "L_____RR__") == False
    assert candidate(start = "L___R__L_R",target = "LL______RR") == False
    assert candidate(start = "______",target = "______") == True
    assert candidate(start = "R_L_R___L_R",target = "_L_R_L___RR") == False
    assert candidate(start = "L_L_L__L___",target = "_L_L___L___L_") == False
    assert candidate(start = "R________L",target = "________LR") == False
    assert candidate(start = "R_L___L_R",target = "__LR__L_R") == False
    assert candidate(start = "R___________L",target = "____________LR") == False
    assert candidate(start = "L___R___L",target = "__L___R_L") == False
    assert candidate(start = "L_R___R__L",target = "____L___R") == False
    assert candidate(start = "_______L_L_R_R",target = "L______L___R_R") == True
    assert candidate(start = "RRRLLL___",target = "___RRRLLL") == False
    assert candidate(start = "L__R__L___R____",target = "L___L__R__R____") == False
    assert candidate(start = "L_R___R___R___L",target = "___L_____RR___") == False
    assert candidate(start = "L___R__L___",target = "_L_____RL__") == False
    assert candidate(start = "L___R___L___R",target = "L___L___R___R") == False
    assert candidate(start = "____L___R__",target = "L_____R____") == False
    assert candidate(start = "L_R__L_R",target = "_LR__LR_") == False
    assert candidate(start = "R_L___LR__L____",target = "__LR__LR__L____") == False
    assert candidate(start = "L___R___R",target = "___L____R") == False
    assert candidate(start = "L___R___L_R",target = "L_____RL___") == False
    assert candidate(start = "__L_R__R_L",target = "L_____R__L") == False
    assert candidate(start = "_L___R__L",target = "L_____R__") == False
    assert candidate(start = "L_R___R___L___",target = "___L_____R___") == False
    assert candidate(start = "_L_R_L_R_R",target = "L______RRR") == False
    assert candidate(start = "_L___R_L_R",target = "L______LR") == False
    assert candidate(start = "_R_L_R_L____",target = "____LR____LR") == False
    assert candidate(start = "R_L__R",target = "__LR__") == False


