def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(start = "XXL",result = "LXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXL",result = "LXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXL",result = "XRLXXRRLX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXL",result = "XRLXXRRLX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLR",result = "RRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLR",result = "RRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXL",result = "XRXL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXL",result = "XRXL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXL",result = "LXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXL",result = "LXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RL",result = "LR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RL",result = "LR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLX",result = "LXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLX",result = "LXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXLXXXX",result = "LXXXXXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXLXXXX",result = "LXXXXXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXXLXXXX",result = "XXXXRXXLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXXLXXXX",result = "XXXXRXXLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXRXXX",result = "XXXLXXRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXRXXX",result = "XXXLXXRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXRRLL",result = "RXXRLXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXRRLL",result = "RXXRLXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXX",result = "XXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXX",result = "XXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXR",result = "XRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXR",result = "XRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXX",result = "XXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXX",result = "XXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRLR",result = "LRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRLR",result = "LRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXRX",result = "XXRRX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXRX",result = "XXRRX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LL",result = "RR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LL",result = "RR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "X",result = "L") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "X",result = "L") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRRXXLRR",result = "XXLLRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRRXXLRR",result = "XXLLRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXLXLRRXL",result = "LXXRXRXLRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXLXLRRXL",result = "LXXRXRXLRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXLXXR",result = "XXLXLXLRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXLXXR",result = "XXLXLXLRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXRXXRXX",result = "XXRXXRXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXRXXRXX",result = "XXRXXRXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXLXRXXR",result = "LXRXRXRXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXLXRXXR",result = "LXRXRXRXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLXXRXLXXL",result = "XRLXXXRXLXXL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLXXRXLXXL",result = "XRLXXXRXLXXL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXR",result = "RRXLXXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXR",result = "RRXLXXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXLXXL",result = "XXLXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXLXXL",result = "XXLXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXLXL",result = "LXRXRXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXLXL",result = "LXRXRXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLLLLXXXXXX",result = "XXXXXXXXLLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLLLLXXXXXX",result = "XXXXXXXXLLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXLXX",result = "XRLXLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXLXX",result = "XRLXLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXXLXXLR",result = "XLXXRXXRLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXXLXXLR",result = "XLXXRXXRLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRRRRRXXXXX",result = "XXXXXRRRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRRRRRXXXXX",result = "XXXXXRRRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXXLXXR",result = "XRLXXLXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXXLXXR",result = "XRLXXLXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXRXLR",result = "XXLRXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXRXLR",result = "XXLRXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXRXLX",result = "XLXRLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXRXLX",result = "XLXRLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXXXRXX",result = "XXLXXXXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXXXRXX",result = "XXLXXXXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXL",result = "XXLRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXL",result = "XXLRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRXLRXLRXLR",result = "RXLRXLRXLRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRXLRXLRXLR",result = "RXLRXLRXLRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXLXXR",result = "XXRXLXXRXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXLXXR",result = "XXRXLXXRXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLRLRXRXRX",result = "LLRXRXRXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLRLRXRXRX",result = "LLRXRXRXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRRXLXXR",result = "XLLRXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRRXLXXR",result = "XLLRXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXXXLXX",result = "XXXXXXLRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXXXLXX",result = "XXXXXXLRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XLXRXLXRXLX",result = "LXRLXRLXRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XLXRXLXRXLX",result = "LXRLXRLXRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXRXRXRXR",result = "XRXRXRXRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXRXRXRXR",result = "XRXRXRXRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXLXRLX",result = "XRLXXRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXLXRLX",result = "XRLXXRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLXLXXRL",result = "XLRXRXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLXLXXRL",result = "XLRXRXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXLRXLXXL",result = "XRLXXLRXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXLRXLXXL",result = "XRLXXLRXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRRXLXXL",result = "XXLRXXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRRXLXXL",result = "XXLRXXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRLRLRLRLRL",result = "RLRLRLRLRLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRLRLRLRLRL",result = "RLRLRLRLRLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRRXXXXXXXL",result = "XXXXXXLRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRRXXXXXXXL",result = "XXXXXXLRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLRXXLXXR",result = "XXRXXLXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLRXXLXXR",result = "XXRXXLXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXLXXLXX",result = "LXXLXXLXXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXLXXLXX",result = "LXXLXXLXXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXLRRXXL",result = "XXLRXRXRLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXLRRXXL",result = "XXLRXRXRLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXXLXXRLXX",result = "XLXXLXXLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXXLXXRLXX",result = "XLXXLXXLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXLXXL",result = "XRLXXRRLXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXLXXL",result = "XRLXXRRLXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXRXRXRXRLX",result = "XRLXRXRXLXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXRXRXRXRLX",result = "XRLXRXRXLXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXLXXR",result = "LLXXRXRXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXLXXR",result = "LLXXRXRXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXRXR",result = "XLXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXRXR",result = "XLXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRXXLXXR",result = "LXXRXXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRXXLXXR",result = "LXXRXXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXXL",result = "XRLXXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXXL",result = "XRLXXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXRXXL",result = "XLRXLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXRXXL",result = "XLRXLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXLR",result = "XRLXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXLR",result = "XRLXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXR",result = "XXRXXRRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXR",result = "XXRXXRRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRXRXLXRXL",result = "RXLXLRXLRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRXRXLXRXL",result = "RXLXLRXLRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXLXXXR",result = "XXLXXXRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXLXXXR",result = "XXLXXXRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXRXL",result = "XXLXRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXRXL",result = "XXLXRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXRXRXRXRX",result = "RXRXRXRXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXRXRXRXRX",result = "RXRXRXRXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXLX",result = "XRLXXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXLX",result = "XRLXXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXLXXXXLXXX",result = "LXXXXXXXXXXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXLXXXXLXXX",result = "LXXXXXXXXXXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLXXRXLXX",result = "XXLRXRXLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLXXRXLXX",result = "XXLRXRXLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLRXRXL",result = "LXXRXXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLRXRXL",result = "LXXRXXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXRXLXX",result = "XXLXXRXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXRXLXX",result = "XXLXXRXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXRXRXRX",result = "XXRXXRXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXRXRXRX",result = "XXRXXRXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXLXXL",result = "XXLXRXRXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXLXXL",result = "XXLXRXRXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXLXLXLXL",result = "XLXLXLXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXLXLXLXL",result = "XLXLXLXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXRXRXL",result = "LXRXRXRXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXRXRXL",result = "LXRXRXRXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXLXXRXL",result = "XXLXXRXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXLXXRXL",result = "XXLXXRXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXLXRXLL",result = "XXRXLRXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXLXRXLL",result = "XXRXLRXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLRLXXLR",result = "XLRLXLRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLRLXXLR",result = "XLRLXLRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXRXRXRX",result = "XRXRXRXRXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXRXRXRX",result = "XRXRXRXRXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXXXLL",result = "LLXXXXRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXXXLL",result = "LLXXXXRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXRXRXLXX",result = "XXRXXRXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXRXRXLXX",result = "XXRXXRXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXXL",result = "LXXRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXXL",result = "LXXRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXLXLXLXL",result = "LXRXRXRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXLXLXLXL",result = "LXRXRXRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXLXL",result = "XLXLXLXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXLXL",result = "XLXLXLXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXXXXXXX",result = "XXXXXXXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXXXXXXX",result = "XXXXXXXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXXLXXR",result = "XXLXXRXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXXLXXR",result = "XXLXXRXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXLXR",result = "XRLXLXLXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXLXR",result = "XRLXLXLXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXRXXLXXR",result = "XXLXXLXXRXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXRXXLXXR",result = "XXLXXLXXRXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRRXLX",result = "XRLXXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRRXLX",result = "XRLXXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXRXXL",result = "XXLRXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXRXXL",result = "XXLRXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXRXRXLXR",result = "XXLXLXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXRXRXLXR",result = "XXLXLXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXRX",result = "LXRXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXRX",result = "LXRXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXLXRXL",result = "XRLXXRXLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXLXRXL",result = "XRLXXRXLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLLRXXXR",result = "XXLRRLXXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLLRXXXR",result = "XXLRRLXXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRXLX",result = "XXLXXRLRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRXLX",result = "XXLXXRLRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XLRXLRXLRXL",result = "LXRLXRLXRLX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XLRXLRXLRXL",result = "LXRLXRLXRLX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXXLXXRXL",result = "XRLXXRXLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXXLXXRXL",result = "XRLXXRXLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRLRXXL",result = "LXXLRXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRLRXXL",result = "LXXLRXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXXL",result = "XXLXXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXXL",result = "XXLXXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXRXLXR",result = "XRLXRXRXLXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXRXLXR",result = "XRLXRXRXLXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXRXRXRXLXXL",result = "XXLXXLXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXRXRXRXLXXL",result = "XXLXXLXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXXRXLX",result = "XRLXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXXRXLX",result = "XRLXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLRRXXLXXR",result = "LXXLXXRXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLRRXXLXXR",result = "LXXLXXRXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLRXXLXX",result = "LXXRXXLXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLRXXLXX",result = "LXXRXXLXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXL",result = "XXLXXLRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXL",result = "XXLXXLRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLXXXL",result = "XXLXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLXXXL",result = "XXLXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXRXRXRXL",result = "XXLXXRXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXRXRXRXL",result = "XXLXXRXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXR",result = "XXRRLXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXR",result = "XXRRLXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLRRLRRRLL",result = "RLLLLRRRLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLRRLRRRLL",result = "RLLLLRRRLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXLXXXXR",result = "XXXXLXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXLXXXXR",result = "XXXXLXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXLXR",result = "XRLXRXLRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXLXR",result = "XRLXRXLRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRXXLXRXXRL",result = "XRLXLXXRRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRXXLXRXXRL",result = "XRLXLXXRRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLXXLXXR",result = "LXXRXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLXXLXXR",result = "LXXRXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRLXXRX",result = "XRLXXLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRLXXRX",result = "XRLXXLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXXXRRRR",result = "RRRRXXXXXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXXXRRRR",result = "RRRRXXXXXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXXLXX",result = "XLRXXLXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXXLXX",result = "XLRXXLXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXXLXXL",result = "XXLXXLXXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXXLXXL",result = "XXLXXLXXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRXXLXXRL",result = "LXXRXXLRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRXXLXXRL",result = "LXXRXXLRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXRXLXRX",result = "LXRXRXRXRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXRXLXRX",result = "LXRXRXRXRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRLXXLXXR",result = "LXXRXXRXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRLXXLXXR",result = "LXXRXXRXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXXRXXR",result = "XXRXXLXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXXRXXR",result = "XXRXXLXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXRXLXXL",result = "XLXXLXXLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXRXLXXL",result = "XLXXLXXLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXRXRXR",result = "RRRRRXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXRXRXR",result = "RRRRRXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXXLRXLX",result = "XXLXXRXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXXLRXLX",result = "XXLXXRXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXXRXXL",result = "XXLRXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXXRXXL",result = "XXLRXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRRRRRXXL",result = "XXLRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRRRRRXXL",result = "XXLRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXXLXXLX",result = "LXLXLXLXXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXXLXXLX",result = "LXLXLXLXXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXXLXXRXXL",result = "XXLXXRXRXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXXLXXRXXL",result = "XXLXXRXRXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXXXXXX",result = "XXXXXXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXXXXXX",result = "XXXXXXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLR",result = "LXRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLR",result = "LXRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRLR",result = "RLLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRLR",result = "RLLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXRXLXXR",result = "RLXXRXLXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXRXLXXR",result = "RLXXRXLXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXL",result = "XXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXL",result = "XXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXXLXL",result = "XRLXXXL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXXLXL",result = "XRLXXXL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRX",result = "XRLXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRX",result = "XRLXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXR",result = "LRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXR",result = "LRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXRXLXL",result = "XRLXXLRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXRXLXL",result = "XRLXXLRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXRXXL",result = "XXLXXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXRXXL",result = "XXLXXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXLXLXX",result = "XLXXXLRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXLXLXX",result = "XLXXXLRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXRXRX",result = "XRXRXRXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXRXRX",result = "XRXRXRXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXRRXXL",result = "RLXXXXXRRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXRRXXL",result = "RLXXXXXRRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXL",result = "LXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXL",result = "LXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXR",result = "XLRXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXR",result = "XLRXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXXXXXXXXRXXL",result = "XRLXXXXXXXXXXRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXXXXXXXXRXXL",result = "XRLXXXXXXXXXXRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXRRXXL",result = "RLXXXRXLXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXRRXXL",result = "RLXXXRXLXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXXXXL",result = "LXXXXXXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXXXXL",result = "LXXXXXXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXLXXXX",result = "XXXXXXXXLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXLXXXX",result = "XXXXXXXXLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLRXXRLLXL",result = "RLRXRLLXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLRXXRLLXL",result = "RLRXRLLXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXRXLX",result = "LXRXRXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXRXLX",result = "LXRXRXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLX",result = "XLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLX",result = "XLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRLXXRLXXX",result = "XXXRLXXRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRLXXRLXXX",result = "XXXRLXXRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXRXX",result = "XXLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXRXX",result = "XXLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXX",result = "XXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXX",result = "XXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLR",result = "LXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLR",result = "LXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXRXL",result = "XXRLXXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXRXL",result = "XXRLXXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXXLXXX",result = "XXXXXXLRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXXLXXX",result = "XXXXXXLRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXRXXLX",result = "XXXLXXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXRXXLX",result = "XXXLXXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXLX",result = "XRLXXRRXLX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXLX",result = "XRLXXRRXLX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXXXXXR",result = "XXXXXXXXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXXXXXR",result = "XXXXXXXXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXL",result = "LXXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXL",result = "LXXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXR",result = "XRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXR",result = "XRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLRRLRLLRL",result = "LRLRLLRLRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLRRLRLLRL",result = "LRLRLLRLRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXLXX",result = "XRLXXRRLXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXLXX",result = "XRLXXRRLXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXL",result = "XXRLXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXL",result = "XXRLXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXX",result = "XLRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXX",result = "XLRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRLR",result = "LRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRLR",result = "LRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXRXXL",result = "LXXXXRXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXRXXL",result = "LXXXXRXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXR",result = "RXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXR",result = "RXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXXLXXXL",result = "XLRXXXXXXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXXLXXXL",result = "XLRXXXXXXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLX",result = "LXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLX",result = "LXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXRXLXLX",result = "LRXXRXLXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXRXLXLX",result = "LRXXRXLXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLRXXRXL",result = "LXXLRXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLRXXRXL",result = "LXXLRXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRXRXRXXLX",result = "XXLRXRXLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRXRXRXXLX",result = "XXLRXRXLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXL",result = "XRLXRXRXL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXL",result = "XRLXRXRXL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXLXXXX",result = "XXXXXXXXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXLXXXX",result = "XXXXXXXXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXR",result = "XLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXR",result = "XLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXLXRXRXXLXXXXL",result = "XXXLLXXXXXXLRLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXLXRXRXXLXXXXL",result = "XXXLLXXXXXXLRLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXL",result = "XRLXXRRXL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXL",result = "XRLXXRRXL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXR",result = "LXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXR",result = "LXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXXX",result = "XXXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXXX",result = "XXXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXLXXRXX",result = "XXLXXXXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXLXXRXX",result = "XXLXXXXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXLXXXXL",result = "LXLXLXLXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXLXXXXL",result = "LXLXLXLXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXL",result = "LXRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXL",result = "LXRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXRXXXX",result = "XXXXXXXXXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXRXXXX",result = "XXXXXXXXXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRLR",result = "LRRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRLR",result = "LRRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXXXXLRLX",result = "LXXXXXXXXXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXXXXLRLX",result = "LXXXXXXXXXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXLXX",result = "LXXLXXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXLXX",result = "LXXLXXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXRXL",result = "XRLXXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXRXL",result = "XRLXXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXRXRX",result = "XRXRXRXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXRXRX",result = "XRXRXRXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXLXR",result = "XRLXXRRLXXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXLXR",result = "XRLXXRRLXXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLLL",result = "LLLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLLL",result = "LLLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRLXXL",result = "XLLXRXXLXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRLXXL",result = "XLLXRXXLXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRL",result = "LXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRL",result = "LXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXL",result = "LXXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXL",result = "LXXRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRXXLXXR",result = "RXLXXRRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRXXLXXR",result = "RXLXXRRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRRR",result = "RRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRRR",result = "RRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXLXXXX",result = "LXLXXXXXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXLXXXX",result = "LXLXXXXXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRXRXL",result = "XLLXRXXRXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRXRXL",result = "XLLXRXXRXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXL",result = "XRLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXL",result = "XRLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LRXXRXLX",result = "LXRLXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LRXXRXLX",result = "LXRLXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXL",result = "XLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXL",result = "XLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXXXLXX",result = "XXLXXXXLXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXXXLXX",result = "XXLXXXXLXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXRXL",result = "XXRLXLXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXRXL",result = "XXRLXLXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXLXLXX",result = "LXXRXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXLXLXX",result = "LXXRXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXX",result = "XXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXX",result = "XXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXL",result = "XRXXLXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXL",result = "XRXXLXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXLXR",result = "LXRXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXLXR",result = "LXRXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXXXLXX",result = "LXXXXXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXXXLXX",result = "LXXXXXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXLXLXX",result = "XXRLXXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXLXLXX",result = "XXRLXXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXL",result = "XLRXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXL",result = "XLRXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXR",result = "XLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXR",result = "XLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXLXL",result = "XRLXXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXLXL",result = "XRLXXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXLXXXX",result = "LXXXXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXLXXXX",result = "LXXXXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXXXXXR",result = "RXXXXXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXXXXXR",result = "RXXXXXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRLXX",result = "XLLXRXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRLXX",result = "XLLXRXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLR",result = "LXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLR",result = "LXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXLXXXX",result = "XXXXLXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXLXXXX",result = "XXXXLXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRXRXXL",result = "XLLXRRLXXXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRXRXXL",result = "XLLXRRLXXXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXR",result = "RXR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXR",result = "RXR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLXXXXXX",result = "XXXXXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLXXXXXX",result = "XXXXXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXXXRXL",result = "XRLXXRXLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXXXRXL",result = "XRLXXRXLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXLRXRXL",result = "LRXXRXLXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXLRXRXL",result = "LRXXRXLXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RRLL",result = "LLRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RRLL",result = "LLRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXR",result = "XXLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXR",result = "XXLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLXRXRXL",result = "XRLXXRRLX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLXRXRXL",result = "XRLXXRRLX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR",result = "LR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR",result = "LR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXL",result = "XLRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXL",result = "XLRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXLXXXRXX",result = "LXXXXXXRX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXLXXXRXX",result = "LXXXXXXRX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXRX",result = "XLXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXRX",result = "XLXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLRR",result = "LLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLRR",result = "LLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLRXRXL",result = "LRXRLXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLRXRXL",result = "LRXRLXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXR",result = "XRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXR",result = "XRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXL",result = "XRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXL",result = "XRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXL",result = "XRLXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXL",result = "XRLXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRLXXL",result = "XLLXRXLXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRLXXL",result = "XLLXRXLXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXRXLXR",result = "XRLXXLRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXRXLXR",result = "XRLXXLRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXXXXLXXXL",result = "XXXXXXXXLRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXXXXLXXXL",result = "XXXXXXXXLRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXXRRLL",result = "RLXXRXXLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXXRRLL",result = "RLXXRXXLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXL",result = "XLRXXRRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXL",result = "XLRXXRRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXXXXL",result = "XXXXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXXXXL",result = "XXXXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXL",result = "XLXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXL",result = "XLXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXLX",result = "XRLXXRXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXLX",result = "XRLXXRXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXXLRXRXL",result = "RXXLRXRXL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXXLRXRXL",result = "RXXLRXRXL") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLXXRRLXXL",result = "LXRXRLXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLXXRRLXXL",result = "LXRXRLXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LR",result = "RL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LR",result = "RL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RLXXLRXRXL",result = "LRXXLXLXXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RLXXLRXRXL",result = "LRXXLXLXXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXX",result = "XXXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXX",result = "XXXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXR",result = "LRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXR",result = "LRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRLXXRRLX",result = "RXXLRXRXL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRLXXRRLX",result = "RXXLRXRXL") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LXXLXRXRXL",result = "XLLXRXRXLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LXXLXRXRXL",result = "XLLXRXRXLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXR",result = "RXX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXR",result = "RXX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "LLRXXRXLX",result = "XLLXRXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "LLRXXRXLX",result = "XLLXRXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXRXL",result = "LXXRX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXRXL",result = "LXXRX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XRLXL",result = "LXRLX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XRLXL",result = "LXRLX") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "XXXXXLXXXX",result = "XXXXXLXXXX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "XXXXXLXXXX",result = "XXXXXLXXXX") == True: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXLR",result = "LRXR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXLR",result = "LRXR") == False: {e}')
    
    total += 1
    try:
        result = candidate(start = "RXRXXRXL",result = "XXRXLXRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = "RXRXXRXL",result = "XXRXLXRL") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(start = "XXL",result = "LXX") == True
    assert candidate(start = "RXXLRXRXL",result = "XRLXXRRLX") == True
    assert candidate(start = "LLR",result = "RRL") == False
    assert candidate(start = "RXXL",result = "XRXL") == True
    assert candidate(start = "XRXL",result = "LXXR") == False
    assert candidate(start = "RL",result = "LR") == False
    assert candidate(start = "RLX",result = "LXR") == False
    assert candidate(start = "XXXXXLXXXX",result = "LXXXXXXXXX") == True
    assert candidate(start = "XXRXXLXXXX",result = "XXXXRXXLXX") == False
    assert candidate(start = "XXLXXRXXX",result = "XXXLXXRXX") == False
    assert candidate(start = "RLXXXRRLL",result = "RXXRLXXLR") == False
    assert candidate(start = "XXXX",result = "XXXX") == True
    assert candidate(start = "LXXR",result = "XRXL") == False
    assert candidate(start = "RXX",result = "XXR") == True
    assert candidate(start = "XRLR",result = "LRXR") == False
    assert candidate(start = "XRXRX",result = "XXRRX") == True
    assert candidate(start = "LL",result = "RR") == False
    assert candidate(start = "X",result = "L") == False
    assert candidate(start = "LRRXXLRR",result = "XXLLRRRR") == False
    assert candidate(start = "XXRXLXLRRXL",result = "LXXRXRXLRXR") == False
    assert candidate(start = "RXLXLXLXXR",result = "XXLXLXLRXR") == False
    assert candidate(start = "RXXRXXRXX",result = "XXRXXRXXR") == True
    assert candidate(start = "RXLXLXLXRXXR",result = "LXRXRXRXLXXR") == False
    assert candidate(start = "RXXLXXRXLXXL",result = "XRLXXXRXLXXL") == True
    assert candidate(start = "RRXXLXXR",result = "RRXLXXXR") == True
    assert candidate(start = "RRXLXXL",result = "XXLXXLR") == False
    assert candidate(start = "RXLXLXLXL",result = "LXRXRXRXL") == False
    assert candidate(start = "LLLLLXXXXXX",result = "XXXXXXXXLLL") == False
    assert candidate(start = "RXLXRXLXX",result = "XRLXLXXRX") == False
    assert candidate(start = "LXXRXXLXXLR",result = "XLXXRXXRLXR") == False
    assert candidate(start = "RRRRRRXXXXX",result = "XXXXXRRRRRR") == True
    assert candidate(start = "RXLXXLXXR",result = "XRLXXLXXR") == True
    assert candidate(start = "LXXRXRXLR",result = "XXLRXRXLX") == False
    assert candidate(start = "LXXRXRXLX",result = "XLXRLXXRX") == False
    assert candidate(start = "LXXXXXXRXX",result = "XXLXXXXXRX") == False
    assert candidate(start = "RXXXXL",result = "XXLRXX") == False
    assert candidate(start = "LRXLRXLRXLR",result = "RXLRXLRXLRX") == False
    assert candidate(start = "RRXXLXXLXXR",result = "XXRXLXXRXLR") == False
    assert candidate(start = "XXLRLRXRXRX",result = "LLRXRXRXRXR") == False
    assert candidate(start = "LRRXLXXR",result = "XLLRXRXR") == False
    assert candidate(start = "RXXXXXXLXX",result = "XXXXXXLRXX") == False
    assert candidate(start = "XLXRXLXRXLX",result = "LXRLXRLXRLX") == False
    assert candidate(start = "RXRXRXRXRXR",result = "XRXRXRXRXRX") == False
    assert candidate(start = "XXRXLXRLX",result = "XRLXXRXRX") == False
    assert candidate(start = "RXXLXLXXRL",result = "XLRXRXRXLX") == False
    assert candidate(start = "RRXLRXLXXL",result = "XRLXXLRXLR") == False
    assert candidate(start = "LRRXLXXL",result = "XXLRXXRL") == False
    assert candidate(start = "LRLRLRLRLRL",result = "RLRLRLRLRLR") == False
    assert candidate(start = "RRRXXXXXXXL",result = "XXXXXXLRRRR") == False
    assert candidate(start = "LXXLRXXLXXR",result = "XXRXXLXXLR") == False
    assert candidate(start = "XXLXXLXXLXX",result = "LXXLXXLXXLX") == False
    assert candidate(start = "RXXXXLRRXXL",result = "XXLRXRXRLXX") == False
    assert candidate(start = "RXLXXLXXRLXX",result = "XLXXLXXLXXRX") == False
    assert candidate(start = "RXXLRXRXLXXL",result = "XRLXXRRLXRXL") == False
    assert candidate(start = "LXRXRXRXRLX",result = "XRLXRXRXLXL") == False
    assert candidate(start = "RRXXLXXLXXR",result = "LLXXRXRXRXR") == False
    assert candidate(start = "XXLXXRXR",result = "XLXXLXXR") == False
    assert candidate(start = "LRXXLXXR",result = "LXXRXXRL") == False
    assert candidate(start = "RLXXXXL",result = "XRLXXXX") == False
    assert candidate(start = "LXXRXRXXL",result = "XLRXLXXRX") == False
    assert candidate(start = "RLXXXLR",result = "XRLXXLR") == False
    assert candidate(start = "RRXXLXXR",result = "XXRXXRRL") == False
    assert candidate(start = "LRXRXLXRXL",result = "RXLXLRXLRX") == False
    assert candidate(start = "RXXXXLXXXR",result = "XXLXXXRXRX") == False
    assert candidate(start = "LXXRXRXL",result = "XXLXRXRX") == False
    assert candidate(start = "XRXRXRXRXRX",result = "RXRXRXRXRXR") == False
    assert candidate(start = "RXLXRXLX",result = "XRLXXLXR") == False
    assert candidate(start = "XXXXLXXXXLXXX",result = "LXXXXXXXXXXLX") == False
    assert candidate(start = "RXXLXXRXLXX",result = "XXLRXRXLXX") == False
    assert candidate(start = "RXLRXRXL",result = "LXXRXXRXL") == False
    assert candidate(start = "LXXRXRXLXX",result = "XXLXXRXLXR") == False
    assert candidate(start = "RXXRXRXRX",result = "XXRXXRXXR") == False
    assert candidate(start = "RRXXLXXLXXL",result = "XXLXRXRXLXR") == False
    assert candidate(start = "LXLXLXLXL",result = "XLXLXLXLX") == False
    assert candidate(start = "RXLXRXRXRXL",result = "LXRXRXRXRXL") == False
    assert candidate(start = "XRXLXXRXL",result = "XXLXXRXXR") == False
    assert candidate(start = "RRXLXRXLL",result = "XXRXLRXLR") == False
    assert candidate(start = "RXLRLXXLR",result = "XLRLXLRXR") == False
    assert candidate(start = "RXRXRXRXRX",result = "XRXRXRXRXR") == True
    assert candidate(start = "RRXXXXLL",result = "LLXXXXRR") == False
    assert candidate(start = "RXXRXRXLXX",result = "XXRXXRXLXR") == False
    assert candidate(start = "XXRXXL",result = "LXXRXX") == False
    assert candidate(start = "XRXLXLXLXL",result = "LXRXRXRXRX") == False
    assert candidate(start = "RXLXLXLXL",result = "XLXLXLXLR") == False
    assert candidate(start = "XXXXXXXXXXX",result = "XXXXXXXXXXX") == True
    assert candidate(start = "RXLXXLXXR",result = "XXLXXRXLR") == False
    assert candidate(start = "RXLXLXLXR",result = "XRLXLXLXR") == True
    assert candidate(start = "XXLXXRXXLXXR",result = "XXLXXLXXRXXR") == False
    assert candidate(start = "RXLXRRXLX",result = "XRLXXRXLX") == False
    assert candidate(start = "LXXRXRXXL",result = "XXLRXRXLX") == False
    assert candidate(start = "LXRXRXLXR",result = "XXLXLXLXR") == False
    assert candidate(start = "RXLXLXRX",result = "LXRXLXXR") == False
    assert candidate(start = "RXXXXLXRXL",result = "XRLXXRXLXX") == False
    assert candidate(start = "RRXXLLRXXXR",result = "XXLRRLXXRXR") == False
    assert candidate(start = "LXXLXRXLX",result = "XXLXXRLRX") == False
    assert candidate(start = "XLRXLRXLRXL",result = "LXRLXRLXRLX") == True
    assert candidate(start = "XRXXLXXRXL",result = "XRLXXRXLXX") == False
    assert candidate(start = "XXRLRXXL",result = "LXXLRXXR") == False
    assert candidate(start = "LXXRXXL",result = "XXLXXRXL") == False
    assert candidate(start = "RXLXRXRXLXR",result = "XRLXRXRXLXR") == True
    assert candidate(start = "LXRXRXRXLXXL",result = "XXLXXLXXLXXR") == False
    assert candidate(start = "RXLXXRXLX",result = "XRLXXLXXR") == False
    assert candidate(start = "XXLRRXXLXXR",result = "LXXLXXRXXRX") == False
    assert candidate(start = "XXLRXXLXX",result = "LXXRXXLXX") == True
    assert candidate(start = "RRXXLXXL",result = "XXLXXLRX") == False
    assert candidate(start = "RXXLXXXL",result = "XXLXRXLX") == False
    assert candidate(start = "LXRXRXRXL",result = "XXLXXRXXLR") == False
    assert candidate(start = "RRXXLXXR",result = "XXRRLXXR") == True
    assert candidate(start = "LLRRLRRRLL",result = "RLLLLRRRLL") == False
    assert candidate(start = "LXXXXLXXXXR",result = "XXXXLXXLXXR") == False
    assert candidate(start = "RXLXRXLXR",result = "XRLXRXLRX") == False
    assert candidate(start = "LRXXLXRXXRL",result = "XRLXLXXRRLX") == False
    assert candidate(start = "RXXLXXLXXR",result = "LXXRXXLXXR") == False
    assert candidate(start = "RXXLRLXXRX",result = "XRLXXLXXRX") == False
    assert candidate(start = "LXXXXXXRRRR",result = "RRRRXXXXXXL") == False
    assert candidate(start = "LXXRXXLXX",result = "XLRXXLXXX") == False
    assert candidate(start = "LXXLXXLXXL",result = "XXLXXLXXLX") == False
    assert candidate(start = "LRXXLXXRL",result = "LXXRXXLRL") == False
    assert candidate(start = "RXLXRXRXLXRX",result = "LXRXRXRXRXRX") == False
    assert candidate(start = "XXRLXXLXXR",result = "LXXRXXRXXL") == False
    assert candidate(start = "LXXLXXRXXR",result = "XXRXXLXXL") == False
    assert candidate(start = "RXLXRXRXLXXL",result = "XLXXLXXLXXRX") == False
    assert candidate(start = "RXRXRXRXR",result = "RRRRRXRXR") == False
    assert candidate(start = "RXLXXLRXLX",result = "XXLXXRXRXL") == False
    assert candidate(start = "RXLXXRXXL",result = "XXLRXRXLX") == False
    assert candidate(start = "LRRRRRXXL",result = "XXLRRRRRR") == False
    assert candidate(start = "LXXLXXLXXLX",result = "LXLXLXLXXLX") == False
    assert candidate(start = "RXXLRXXLXXRXXL",result = "XXLXXRXRXLXXR") == False
    assert candidate(start = "XXXXXXXXXX",result = "XXXXXXXXXX") == True
    assert candidate(start = "RXLR",result = "LXRR") == False
    assert candidate(start = "LRLR",result = "RLLR") == False
    assert candidate(start = "RLXXRXLXXR",result = "RLXXRXLXXR") == True
    assert candidate(start = "XXRXL",result = "XXLXR") == False
    assert candidate(start = "XRXXLXL",result = "XRLXXXL") == True
    assert candidate(start = "RXLXRX",result = "XRLXXR") == True
    assert candidate(start = "LXXR",result = "LRXX") == False
    assert candidate(start = "RLXXRXLXL",result = "XRLXXLRXL") == False
    assert candidate(start = "LXXRXXL",result = "XXLXXRL") == False
    assert candidate(start = "XXRXLXLXX",result = "XLXXXLRXX") == False
    assert candidate(start = "RXRXRXRX",result = "XRXRXRXR") == True
    assert candidate(start = "RLXXXRRXXL",result = "RLXXXXXRRXLX") == False
    assert candidate(start = "RXL",result = "LXR") == False
    assert candidate(start = "RXLXLXR",result = "XLRXRXL") == False
    assert candidate(start = "RLXXXXXXXXXXRXXL",result = "XRLXXXXXXXXXXRLX") == False
    assert candidate(start = "RLXXXRRXXL",result = "RLXXXRXLXL") == False
    assert candidate(start = "RLXXXXXXL",result = "LXXXXXXXX") == False
    assert candidate(start = "LXXXXLXXXX",result = "XXXXXXXXLL") == False
    assert candidate(start = "RLRXXRLLXL",result = "RLRXRLLXXL") == False
    assert candidate(start = "RLXXRXLX",result = "LXRXRXXL") == False
    assert candidate(start = "RXLX",result = "XLXR") == False
    assert candidate(start = "XRLXXRLXXX",result = "XXXRLXXRLX") == False
    assert candidate(start = "LXXXRXX",result = "XXLXXRX") == False
    assert candidate(start = "XXXXX",result = "XXXXX") == True
    assert candidate(start = "RXLR",result = "LXRX") == False
    assert candidate(start = "RXLXLXRXL",result = "XXRLXXLXR") == False
    assert candidate(start = "RXXXXXLXXX",result = "XXXXXXLRXX") == False
    assert candidate(start = "XXLXXRXXLX",result = "XXXLXXRXLX") == False
    assert candidate(start = "RXXLRXRXLX",result = "XRLXXRRXLX") == True
    assert candidate(start = "RXXXXXXXXR",result = "XXXXXXXXXR") == False
    assert candidate(start = "RXXXL",result = "LXXXX") == False
    assert candidate(start = "RXR",result = "XRX") == False
    assert candidate(start = "LLRRLRLLRL",result = "LRLRLLRLRL") == False
    assert candidate(start = "RXXLRXRXLXX",result = "XRLXXRRLXXX") == True
    assert candidate(start = "RRXXLXXL",result = "XXRLXXLR") == False
    assert candidate(start = "RLXX",result = "XLRX") == False
    assert candidate(start = "LRLR",result = "LRLR") == True
    assert candidate(start = "XXLXXRXXL",result = "LXXXXRXXX") == False
    assert candidate(start = "XRXR",result = "RXXR") == False
    assert candidate(start = "RXXXXXLXXXL",result = "XLRXXXXXXRL") == False
    assert candidate(start = "XXLX",result = "LXXX") == True
    assert candidate(start = "RLXXRXLXLX",result = "LRXXRXLXLX") == False
    assert candidate(start = "LLRXXRXL",result = "LXXLRXRL") == False
    assert candidate(start = "XRXRXRXXLX",result = "XXLRXRXLXX") == False
    assert candidate(start = "RXXLRXRXL",result = "XRLXRXRXL") == True
    assert candidate(start = "LXXXXLXXXX",result = "XXXXXXXXXX") == False
    assert candidate(start = "LXXR",result = "XLXR") == False
    assert candidate(start = "XXLXLXRXRXXLXXXXL",result = "XXXLLXXXXXXLRLXXR") == False
    assert candidate(start = "RXXLRXRXL",result = "XRLXXRRXL") == True
    assert candidate(start = "XXLXR",result = "LXXRX") == False
    assert candidate(start = "XXXXXXX",result = "XXXXXXX") == True
    assert candidate(start = "XXXLXXRXX",result = "XXLXXXXXR") == True
    assert candidate(start = "LXXXXLXXXXL",result = "LXLXLXLXL") == False
    assert candidate(start = "RXLXL",result = "LXRXR") == False
    assert candidate(start = "RXXXXRXXXX",result = "XXXXXXXXXX") == False
    assert candidate(start = "LRLR",result = "LRRL") == False
    assert candidate(start = "RLXXXXXXLRLX",result = "LXXXXXXXXXRL") == False
    assert candidate(start = "XXLXXLXX",result = "LXXLXXLX") == False
    assert candidate(start = "RLXXXRXL",result = "XRLXXRXL") == False
    assert candidate(start = "RXLXRXRXRX",result = "XRXRXRXLXR") == False
    assert candidate(start = "RXXLRXRXLXR",result = "XRLXXRRLXXR") == True
    assert candidate(start = "LLLL",result = "LLLL") == True
    assert candidate(start = "LXXLXRLXXL",result = "XLLXRXXLXL") == False
    assert candidate(start = "XRL",result = "LXR") == False
    assert candidate(start = "RLXXL",result = "LXXRL") == False
    assert candidate(start = "RRXXLXXR",result = "RXLXXRRX") == False
    assert candidate(start = "RRRR",result = "RRRR") == True
    assert candidate(start = "XXLXXLXXXX",result = "LXLXXXXXXL") == False
    assert candidate(start = "LXXLXRXRXL",result = "XLLXRXXRXX") == False
    assert candidate(start = "RXRXL",result = "XRLXR") == False
    assert candidate(start = "LRXXRXLX",result = "LXRLXXRX") == False
    assert candidate(start = "RXL",result = "XLR") == False
    assert candidate(start = "XXLXXXXLXX",result = "XXLXXXXLXX") == True
    assert candidate(start = "RXLXLXRXL",result = "XXRLXLXLX") == False
    assert candidate(start = "XXRXLXLXX",result = "LXXRXLXXR") == False
    assert candidate(start = "LXX",result = "XXL") == False
    assert candidate(start = "RXXLRXRXL",result = "XRXXLXRXL") == False
    assert candidate(start = "RXLXLXR",result = "LXRXLXR") == False
    assert candidate(start = "XXXXXXXLXX",result = "LXXXXXXXXX") == True
    assert candidate(start = "RXRXLXLXX",result = "XXRLXXLXR") == False
    assert candidate(start = "RLXXXL",result = "XLRXRX") == False
    assert candidate(start = "LXR",result = "XLR") == False
    assert candidate(start = "RXRXLXL",result = "XRLXXLR") == False
    assert candidate(start = "XXXXLXXXX",result = "LXXXXXXXX") == True
    assert candidate(start = "LXXXXXXR",result = "RXXXXXXL") == False
    assert candidate(start = "LXXLXRLXX",result = "XLLXRXXRX") == False
    assert candidate(start = "RXLR",result = "LXXR") == False
    assert candidate(start = "XXXXXLXXXX",result = "XXXXLXXXXX") == True
    assert candidate(start = "LXXLXRXRXXL",result = "XLLXRRLXXXL") == False
    assert candidate(start = "RXR",result = "RXR") == True
    assert candidate(start = "RXXLXXXXXX",result = "XXXXXXLXXR") == False
    assert candidate(start = "RLXXXXXRXL",result = "XRLXXRXLXR") == False
    assert candidate(start = "RLXXLRXRXL",result = "LRXXRXLXRX") == False
    assert candidate(start = "RRLL",result = "LLRR") == False
    assert candidate(start = "LXXR",result = "XXLR") == False
    assert candidate(start = "RXLXRXRXL",result = "XRLXXRRLX") == True
    assert candidate(start = "LR",result = "LR") == True
    assert candidate(start = "RLXXL",result = "XLRXL") == False
    assert candidate(start = "XXLXXXRXX",result = "LXXXXXXRX") == True
    assert candidate(start = "LXRX",result = "XLXR") == False
    assert candidate(start = "LLRR",result = "LLRR") == True
    assert candidate(start = "LLRXRXL",result = "LRXRLXL") == False
    assert candidate(start = "LXXR",result = "XRLX") == False
    assert candidate(start = "RXL",result = "XRL") == True
    assert candidate(start = "XXRXL",result = "XRLXX") == False
    assert candidate(start = "LXXLXRLXXL",result = "XLLXRXLXLX") == False
    assert candidate(start = "RLXXRXLXR",result = "XRLXXLRXR") == False
    assert candidate(start = "RXXXXXLXXXL",result = "XXXXXXXXLRL") == False
    assert candidate(start = "RLXXXRRLL",result = "RLXXRXXLL") == False
    assert candidate(start = "RXXLRXRXL",result = "XLRXXRRLX") == False
    assert candidate(start = "XXRXXXXL",result = "XXXXLXXR") == False
    assert candidate(start = "LXXL",result = "XLXL") == False
    assert candidate(start = "RXXLRXRXLX",result = "XRLXXRXRXL") == False
    assert candidate(start = "RXXLRXRXL",result = "RXXLRXRXL") == True
    assert candidate(start = "LLXXRRLXXL",result = "LXRXRLXLX") == False
    assert candidate(start = "LR",result = "RL") == False
    assert candidate(start = "RLXXLRXRXL",result = "LRXXLXLXXR") == False
    assert candidate(start = "XXXXXX",result = "XXXXXX") == True
    assert candidate(start = "LXR",result = "LRX") == False
    assert candidate(start = "XRLXXRRLX",result = "RXXLRXRXL") == False
    assert candidate(start = "LXXLXRXRXL",result = "XLLXRXRXLX") == False
    assert candidate(start = "XXR",result = "RXX") == False
    assert candidate(start = "LLRXXRXLX",result = "XLLXRXXRX") == False
    assert candidate(start = "XXRXL",result = "LXXRX") == False
    assert candidate(start = "XRLXL",result = "LXRLX") == False
    assert candidate(start = "XXXXXLXXXX",result = "XXXXXLXXXX") == True
    assert candidate(start = "RXLR",result = "LRXR") == False
    assert candidate(start = "RXRXXRXL",result = "XXRXLXRL") == False


