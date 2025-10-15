def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(currentState = "+-+-+--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-+-+--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-++-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-++-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--+-+++++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--+-+++++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-+--++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-+--++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++-") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++-") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++--++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++--++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++-++++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++-++++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-+-+--+++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-+-+--+++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+++++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+++++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-++++-++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-++++-++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-++++-++++-++++-++++-++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-++++-++++-++++-++++-++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++++++++-++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++++++++-++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++++++++--++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++++++++--++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--+++++--+++++--+++++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--+++++--+++++--+++++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-++++-++++-+") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-++++-++++-+") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--++--++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--++--++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++++--++++--++++--++++--++++--++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++++--++++--++++--++++--++++--++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++--+++++--+++++--+++++--+++++--+++++--+++++--+++++--+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++--+++++--+++++--+++++--+++++--+++++--+++++--+++++--+++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--+++++-+++++-+++++-+++++-+++++-+++++-+++++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--+++++-+++++-+++++-+++++-+++++-+++++-+++++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++-++++++-++++++-++++++-++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++-++++++-++++++-++++++-++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++++++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++++++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "----------------------------------------------------------------------------------------") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "----------------------------------------------------------------------------------------") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++--++++++--++++++--++++++--++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++--++++++--++++++--++++++--++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--++--++--++--++--++--++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--++--++--++--++--++--++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-+--++++-+--++++-+--++++-+--++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-+--++++-+--++++-+--++++-+--++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+++++++++++++++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+++++++++++++++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++++++++++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++++++++++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++--++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++--++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++--+++++--+++++--+++++--+++++--+++++--+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++--+++++--+++++--+++++--+++++--+++++--+++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--+--+--+--+--+--+--+--+--+--+") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--+--+--+--+--+--+--+--+--+--+") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++-++-++-++-++-++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++-++-++-++-++-++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+++++----+++++----+++++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+++++----+++++----+++++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++-++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++-++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++++++++++++++++++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++++++++++++++++++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++++-++++-++++-++++-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++++-++++-++++-++++-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++--++++--++++--++++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++--++++--++++--++++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++++++++++--++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++++++++++--++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--++--++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--++--++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+--++-+--++-+--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+--++-+--++-+--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-+-+-++++-+-++++-+-++++-+-++++-+-++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-+-+-++++-+-++++-+-++++-+-++++-+-++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++--++++++++--++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++--++++++++--++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-+-+-++++-+-++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-+-+-++++-+-++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++-++++++++-++++++++-++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++-++++++++-++++++++-++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++++-++++-++++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++++-++++-++++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--+++++--+++++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--+++++--+++++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++----++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++----++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-+--++-+-+") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-+--++-+-+") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++-++-++-++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++-++-++-++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++----+++++----+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++----+++++----+++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++----+++++----+++++----+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++----+++++----+++++----+++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++++++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++++++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--++--++--++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--++--++--++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--------------------------------") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--------------------------------") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++++++++++++++++++--------------------------------") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++++++++++++++++++--------------------------------") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++++++++++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++++++++++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++++++--+--++++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++++++--+--++++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++-+-++++++++++-+-++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++-+-++++++++++-+-++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++--++-++-++--++-++-++--++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++--++-++-++--++-++-++--++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++++-++++++-++++++-++++++-++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++++-++++++-++++++-++++++-++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++-++++++-++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++-++++++-++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++--++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++--++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "----++++++++++----++++++++++----++++++++++----") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "----++++++++++----++++++++++----++++++++++----") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++++++++++++++++++++++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++++++++++++++++++++++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-++-+-++-+-++-+-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-++-+-++-+-++-+-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-++-+-++-+-++-+-") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-++-+-++-+-++-+-") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-++-++-++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-++-++-++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "------------------------------------------------------------") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "------------------------------------------------------------") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++-+++++-+++++-+++++-+++++-+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++-+++++-+++++-+++++-+++++-+++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-++-+-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-++-+-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++--++--++--++--++--++--++--++--++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++--++--++--++--++--++--++--++--++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++++--++++--++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++++--++++--++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++++--+++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++++--+++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++-++++++-++++++-++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++-++++++-++++++-++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++--++++++--++++++--++++++--++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++--++++++--++++++--++++++--++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "------------------------------------") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "------------------------------------") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-++-+-++-+-++-+-++-+-++-+-++-+-++-+-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-++-+-++-+-++-+-++-+-++-+-++-+-++-+-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+++++----+++++----+++++----+++++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+++++----+++++----+++++----+++++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++++++-++++--++++--++++-++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++++++-++++--++++--++++-++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+-+++-+++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+-+++-+++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++--++++++++--++++++++--++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++--++++++++--++++++++--++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++--++++++++++--++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++--++++++++++--++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++---++++++---++++++---++++++---++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++---++++++---++++++---++++++---++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++-++++-++++-++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++-++++-++++-++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++++++++-++++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++++++++-++++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++++++--++++++--++++++--") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++++++--++++++--++++++--") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++--++--++--++--++--++--++--++--") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++--++--++--++--++--++--++--++--") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++-++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++-++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++++-++++++-++++++-") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++++-++++++-++++++-") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-++-++++-++-++++-++-++++-++-++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-++-++++-++-++++-++-++++-++-++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++++--++++++--++++++") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++++--++++++--++++++") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-++++++++-++++++++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-++++++++-++++++++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-+--++-+--++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-+--++-+--++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "--++++++++--++++++++--++++++++--++++++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "--++++++++--++++++++--++++++++--++++++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+-++-+-++-+-++-+-++-+-++-+-++-") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+-++-+-++-+-++-+-++-+-++-+-++-") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++-++++-++++-++++-++++-++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++-++++-++++-++++-++++-++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "----------------------------------------------------------------") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "----------------------------------------------------------------") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-++-++++-++-++++-++-++++-") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-++-++++-++-++++-++-++++-") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "-+++++++-++++++-") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "-+++++++-++++++-") == True: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++-++++-++++-++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++-++++-++++-++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "++++--++++--++++--++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "++++--++++--++++--++++") == False: {e}')
    
    total += 1
    try:
        result = candidate(currentState = "+++++-+++++-+++++-+++++") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(currentState = "+++++-+++++-+++++-+++++") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(currentState = "+-+-+--") == False
    assert candidate(currentState = "-+-") == False
    assert candidate(currentState = "++--") == True
    assert candidate(currentState = "++-++") == False
    assert candidate(currentState = "++++") == True
    assert candidate(currentState = "+++") == True
    assert candidate(currentState = "+++++++") == True
    assert candidate(currentState = "+") == False
    assert candidate(currentState = "+++++") == False
    assert candidate(currentState = "++++++") == True
    assert candidate(currentState = "++++++++") == True
    assert candidate(currentState = "+-++-++-") == False
    assert candidate(currentState = "--++--") == True
    assert candidate(currentState = "--+-+++++--") == False
    assert candidate(currentState = "++++++++++++++++") == True
    assert candidate(currentState = "+-+--++") == True
    assert candidate(currentState = "-++++-") == True
    assert candidate(currentState = "--++--++--") == False
    assert candidate(currentState = "-++++-++++-") == False
    assert candidate(currentState = "++++-++++") == False
    assert candidate(currentState = "-++-++-") == False
    assert candidate(currentState = "++++++++++") == True
    assert candidate(currentState = "+-+-+--+++") == True
    assert candidate(currentState = "++-++-++") == True
    assert candidate(currentState = "-+++++-") == False
    assert candidate(currentState = "+++++++++") == False
    assert candidate(currentState = "++") == True
    assert candidate(currentState = "++++-++++-++++") == True
    assert candidate(currentState = "++--++--++--++") == False
    assert candidate(currentState = "++++-++++-++++-++++-++++-++++") == False
    assert candidate(currentState = "-++++++++++-++++++++") == True
    assert candidate(currentState = "+++++++++++++--++++") == False
    assert candidate(currentState = "--+++++--+++++--+++++--") == False
    assert candidate(currentState = "++-++-++-++-++-++") == False
    assert candidate(currentState = "+-++++-++++-+") == False
    assert candidate(currentState = "++++++++++++++") == True
    assert candidate(currentState = "++--++--++--++--++") == True
    assert candidate(currentState = "--++++--++++--++++--++++--++++--++++") == False
    assert candidate(currentState = "+++++--+++++--+++++--+++++--+++++--+++++--+++++--+++++--+++++") == False
    assert candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False
    assert candidate(currentState = "--+++++-+++++-+++++-+++++-+++++-+++++-+++++--") == False
    assert candidate(currentState = "++--++--++--") == True
    assert candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++") == False
    assert candidate(currentState = "++++++-++++++-++++++-++++++-++++++") == True
    assert candidate(currentState = "--++++++--") == True
    assert candidate(currentState = "----------------------------------------------------------------------------------------") == False
    assert candidate(currentState = "++++++--++++++--++++++--++++++--++++++") == True
    assert candidate(currentState = "++--++--++--++--++--++--++--++--++--") == True
    assert candidate(currentState = "++++-+--++++-+--++++-+--++++-+--++++") == True
    assert candidate(currentState = "-+++++++++++++++++++++++++++") == True
    assert candidate(currentState = "++++++++++++++++++++++++++++++++++") == True
    assert candidate(currentState = "++++++--++++++") == False
    assert candidate(currentState = "+++++--+++++--+++++--+++++--+++++--+++++--+++++") == False
    assert candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++") == True
    assert candidate(currentState = "--+--+--+--+--+--+--+--+--+--+") == False
    assert candidate(currentState = "-++-++-++-++-++-++-++-++") == False
    assert candidate(currentState = "-+++++----+++++----+++++-") == False
    assert candidate(currentState = "++++++-++++++") == False
    assert candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False
    assert candidate(currentState = "+++++++++++++++++++++++++++++") == False
    assert candidate(currentState = "-++-++++-++++-++++-++++-++-") == False
    assert candidate(currentState = "-++++--++++--++++--++++--") == False
    assert candidate(currentState = "++++++++++++++++++++++--++++++++") == False
    assert candidate(currentState = "++--++--++--++--++--") == True
    assert candidate(currentState = "-+--++-+--++-+--") == False
    assert candidate(currentState = "+-+-+-++++-+-++++-+-++++-+-++++-+-++++") == True
    assert candidate(currentState = "++++++++--++++++++--++++++++") == True
    assert candidate(currentState = "-+-+-+-++++-+-++++") == False
    assert candidate(currentState = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-") == False
    assert candidate(currentState = "++++++++-++++++++-++++++++-++++++++") == False
    assert candidate(currentState = "++-++++-++++-++++-++") == True
    assert candidate(currentState = "--+++++--+++++--") == False
    assert candidate(currentState = "++++++----++++++") == False
    assert candidate(currentState = "-+-+--++-+-+") == True
    assert candidate(currentState = "-++-++-++-++-++-++-++") == True
    assert candidate(currentState = "+++++----+++++----+++++") == False
    assert candidate(currentState = "+++++----+++++----+++++----+++++") == False
    assert candidate(currentState = "++++++++++++++++++++++++++++++") == True
    assert candidate(currentState = "++--++--++--++--++--++") == False
    assert candidate(currentState = "--------------------------------") == False
    assert candidate(currentState = "--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++--+-++") == True
    assert candidate(currentState = "++++++++++++++++++++++++++++++--------------------------------") == True
    assert candidate(currentState = "++++++++++++++++++++++++++++++++") == True
    assert candidate(currentState = "--++++++--+--++++--") == True
    assert candidate(currentState = "++++++++++-+-++++++++++-+-++++++++++") == True
    assert candidate(currentState = "++-++-++--++-++-++--++-++-++--++-++") == True
    assert candidate(currentState = "-++++++-++++++-++++++-++++++-++++++") == True
    assert candidate(currentState = "++++++-++++++-++++++") == True
    assert candidate(currentState = "++++++++--++++++++") == False
    assert candidate(currentState = "----++++++++++----++++++++++----++++++++++----") == True
    assert candidate(currentState = "-++++++++++++++++++++++++++++++++++") == True
    assert candidate(currentState = "-+-++-+-++-+-++-+-++-") == False
    assert candidate(currentState = "-+-++-+-++-+-++-+-") == True
    assert candidate(currentState = "+++++++++++++++") == False
    assert candidate(currentState = "++-++-++-++-") == False
    assert candidate(currentState = "++-++-++-++-++-++-++-++-++") == True
    assert candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++-") == False
    assert candidate(currentState = "------------------------------------------------------------") == False
    assert candidate(currentState = "+++++-+++++-+++++-+++++-+++++-+++++") == False
    assert candidate(currentState = "-+-++-+-++-") == False
    assert candidate(currentState = "--++--++--++--++--++--++--++--++--++") == True
    assert candidate(currentState = "--++++--++++--++++") == True
    assert candidate(currentState = "+++++++++--+++++++++") == False
    assert candidate(currentState = "++++++-++++++-++++++-++++++") == False
    assert candidate(currentState = "--++--++++++--++++++--++++++--++--") == True
    assert candidate(currentState = "------------------------------------") == False
    assert candidate(currentState = "+-++-+-++-+-++-+-++-+-++-+-++-+-++-+-++-") == False
    assert candidate(currentState = "-++-++-++-++-++-++-++-++-++-++-++-++") == False
    assert candidate(currentState = "-+++++----+++++----+++++----+++++-") == False
    assert candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++") == True
    assert candidate(currentState = "+++++++++-++++--++++--++++-++++++++") == True
    assert candidate(currentState = "-+-+++-+++-") == False
    assert candidate(currentState = "++++++++--++++++++--++++++++--++++++++") == False
    assert candidate(currentState = "++++++++++--++++++++++--++++++++++") == True
    assert candidate(currentState = "++++++---++++++---++++++---++++++---++++++") == True
    assert candidate(currentState = "-++++-++++-++++-++++") == False
    assert candidate(currentState = "-++++++++++-++++++++++") == False
    assert candidate(currentState = "--++++++--++++++--++++++--") == True
    assert candidate(currentState = "++-++-++-++-++-++-++") == True
    assert candidate(currentState = "++-++-++-++") == False
    assert candidate(currentState = "++++++++++++") == True
    assert candidate(currentState = "++--++--++--++--++--++--++--++--") == False
    assert candidate(currentState = "++-++-++-++-++-++-++-++-++-++-++-++-++") == True
    assert candidate(currentState = "-++++++-++++++-++++++-") == True
    assert candidate(currentState = "++++-++-++++-++-++++-++-++++-++-++++") == True
    assert candidate(currentState = "++++++--++++++--++++++") == True
    assert candidate(currentState = "-++++++++-++++++++-") == False
    assert candidate(currentState = "+-+--++-+--++-") == False
    assert candidate(currentState = "--++++++++--++++++++--++++++++--++++++++") == False
    assert candidate(currentState = "+-++-+-++-+-++-+-++-+-++-+-++-") == False
    assert candidate(currentState = "++-++++-++++-++++-++++-++") == False
    assert candidate(currentState = "----------------------------------------------------------------") == False
    assert candidate(currentState = "++++-++-++++-++-++++-++-++++-") == True
    assert candidate(currentState = "-+++++++-++++++-") == True
    assert candidate(currentState = "++++-++++-++++-++++") == False
    assert candidate(currentState = "++++--++++--++++--++++") == False
    assert candidate(currentState = "+++++-+++++-+++++-+++++") == False


