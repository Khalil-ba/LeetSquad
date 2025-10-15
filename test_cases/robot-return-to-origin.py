def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(moves = "LULLDDRRUURRDDLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LULLDDRRUURRDDLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDRRLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDRRLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LUDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LUDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RLUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RLUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDDLLUURR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDDLLUURR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LRLRLRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LRLRLRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "ULDRULDRULDR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "ULDRULDRULDR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LDRU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LDRU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLRUDLRUDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLRUDLRUDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUUUUUDDDDDDDDDDDDDDLLLLLLLLRRRRRRRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUUUUUDDDDDDDDDDDDDDLLLLLLLLRRRRRRRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LDRRLU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LDRRLU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RLUDRLUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RLUDRLUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RULD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RULD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLLLLLRRRRRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLLLLLRRRRRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDLLLLLLLLLLLLRRRRRRRRRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDLLLLLLLLLLLLRRRRRRRRRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDDLLUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDDLLUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUDDDDLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUDDDDLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LRUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LRUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDLLRRUUDDLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDLLRRUUDDLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUDDDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUDDDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUUUDDDDDDDDDDDDLLLLRRRRRRRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUUUDDDDDDDDDDDDLLLLRRRRRRRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRRLLLDDDUUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRRLLLDDDUUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LDDRUURLDDRUURLDDRUURLDDRUURLDDR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LDDRUURLDDRUURLDDRUURLDDRUURLDDR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLLRRRRRRLLLLRRRRRRLLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLLRRRRRRLLLLRRRRRRLLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDDDUUUUUUUUUUDDDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDDDUUUUUUUUUUDDDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDUDUDUDUDUDUDUDUDUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDUDUDUDUDUDUDUDUDUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDUDUDUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDUDUDUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLRRRRUUUUDDDDLRRRLLLLUUUUDDDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLRRRRUUUUDDDDLRRRLLLLUUUUDDDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDDLLUURRDDLLUURRDDLLUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDDLLUURRDDLLUURRDDLLUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LRLRLRLRLRLRLRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LRLRLRLRLRLRLRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLRRLLRRLLRRLLRRLLRRLLRRLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLRRLLRRLLRRLLRRLLRRLLRRLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LDRULDRULDRU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LDRULDRULDRU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLRRRRLLLLRRRRLLLLRRRRLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLRRRRLLLLRRRRLLLLRRRRLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLRRDDUULLRRDDUULLRRDDUULLRRDDUULL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLRRDDUULLRRDDUULLRRDDUULLRRDDUULL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RULLDDRRULLDDRRULLDDRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RULLDDRRULLDDRRULLDDRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLUUUUUURRRRRRRRDDDDDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLUUUUUURRRRRRRRDDDDDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RULLDRLDURDURLDLURDURLDLURDURLDL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RULLDRLDURDURLDLURDURLDLURDURLDL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLRUDLRUDLRUDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLRUDLRUDLRUDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUUDDUUDDUUDDLLLLRRRRLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUUDDUUDDUUDDLLLLRRRRLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RLRLRLRLRLRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RLRLRLRLRLRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLLRRUUDDLLRRUUDDLLRRUUDDLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLLRRUUDDLLRRUUDDLLRRUUDDLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUDDDLLLRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUDDDLLLRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDDUUDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDDUUDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDLLLLRRRRUUDDLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDLLLLRRRRUUDDLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RLRLRLRLUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RLRLRLRLUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "URDLURDLURDLURDL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "URDLURDLURDLURDL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "ULDRULDRLDURDLURDLURDLURDLURDL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "ULDRULDRLDURDLURDLURDLURDLURDL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDDLLUURRDDLLUURRDDLLUURRDDLLUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDDLLUURRDDLLUURRDDLLUURRDDLLUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LUDRLUDRLUDRLUDRLUDRLUDR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LUDRLUDRLUDRLUDRLUDRLUDR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LRRLRLRLUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LRRLRLRLUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUUDDUUDDUUDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUUDDUUDDUUDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDDUULLRRDDUULL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDDUULLRRDDUULL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LRUDLRUDLRUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LRUDLRUDLRUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LURDLURDLURDLURD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LURDLURDLURDLURD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLRRRRUUDDUUDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLRRRRUUDDUUDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDLRRLRLUDUDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDLRRLRLUDUDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDDDUUDDDDUUDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDDDUUDDDDUUDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLRRRRLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLRRRRLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "ULLDRRDUULLDRRDU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "ULLDRRDUULLDRRDU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRRRRRRRRRLLLLLLLLLLDDDDDDDDDDUUUUUUUUUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRRRRRRRRRLLLLLLLLLLDDDDDDDDDDUUUUUUUUUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RLRLRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RLRLRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLDDDDUUUURRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLDDDDUUUURRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDLLRRUUDDDDLLRRUUDDLLRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDLLRRUUDDDDLLRRUUDDLLRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLRRUUDDUUDDLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLRRUUDDUUDDLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LRRLRLRLUDUDUDUDLRRLRLRLUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LRRLRLRLUDUDUDUDLRRLRLRLUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RLRLRLRLRLRLRLRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RLRLRLRLRLRLRLRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUURRDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUURRDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDUULLRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDUULLRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRRRDDDDLLLLUUUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRRRDDDDLLLLUUUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLRRRRUUUDDDUUUDDDLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLRRRRUUUDDDUUUDDDLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUDDDDDDDDLLLLLLLLRRRRRRRRRRLLRRUUDDLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUDDDDDDDDLLLLLLLLRRRRRRRRRRLLRRUUDDLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "DDUUUUDDLLRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "DDUUUUDDLLRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDLLUURRDDDDLLRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDLLUURRDDDDLLRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RURURURURURURULULULULULULULU") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RURURURURURURULULULULULULULU") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUDDDDDDLLLLRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUDDDDDDLLLLRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDDDLLLLRRRRUUDDDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDDDLLLLRRRRUUDDDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDDLLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDDLLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRRDDDLLLUUUUUDDDD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRRDDDLLLUUUUUDDDD") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLLLLLRRRRRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLLLLLRRRRRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RUDLRUDLRUDLRUDL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RUDLRUDLRUDLRUDL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDLLRRUUDDLLRRUUDDLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDLLRRUUDDLLRRUUDDLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RUDLRULDRLUDLRULDRLUDLRULDRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RUDLRULDRLUDLRULDRLUDLRULDRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDUDUDUDUDUDUDUDUDUDUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDUDUDUDUDUDUDUDUDUDUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "URDLURDLURDL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "URDLURDLURDL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUDDDDDDDLLLLRRRRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUDDDDDDDLLLLRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUDDDDDDDLLLLRRRRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUDDDDDDDLLLLRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRDDLLUURRDDLLUU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRDDLLUURRDDLLUU") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUDDDDDDDDLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUDDDDDDDDLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRRLLLLDDDUUUUUDDDLLLLURRRDDDDUUU") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRRLLLLDDDUUUUUDDDLLLLURRRDDDDUUU") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "DDDDLLLLUUUUUUUUDDDDLLLLRRRRRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "DDDDLLLLUUUUUUUUDDDDLLLLRRRRRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UDUDUDUDLRRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UDUDUDUDLRRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "LURDLURDLURDLURDLURDLURDLURDLURDL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "LURDLURDLURDLURDLURDLURDLURDLURDL") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "UUUUUUUUDDDDDDDDLLLLRRRRRRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "UUUUUUUUDDDDDDDDLLLLRRRRRRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(moves = "RRUUDDLLDDUURLLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "RRUUDDLLDDUURLLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(moves = "ULURDLDRULURDLDRULURDLDRULURDLDR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(moves = "ULURDLDRULURDLDRULURDLDRULURDLDR") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(moves = "LULLDDRRUURRDDLL") == False
    assert candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLRRRR") == True
    assert candidate(moves = "UDLR") == True
    assert candidate(moves = "UUDDRRLL") == True
    assert candidate(moves = "LUDD") == False
    assert candidate(moves = "RLUD") == True
    assert candidate(moves = "RRDDLLUURR") == False
    assert candidate(moves = "LRLRLRLR") == True
    assert candidate(moves = "ULDRULDRULDR") == True
    assert candidate(moves = "LDRU") == True
    assert candidate(moves = "UDLRUDLRUDLR") == True
    assert candidate(moves = "UUUUUUUUUUUUUUDDDDDDDDDDDDDDLLLLLLLLRRRRRRRRRRRR") == False
    assert candidate(moves = "LDRRLU") == True
    assert candidate(moves = "UUDDLLRR") == True
    assert candidate(moves = "RLUDRLUD") == True
    assert candidate(moves = "LLLLRRRR") == True
    assert candidate(moves = "RULD") == True
    assert candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLLLLLRRRRRRRR") == True
    assert candidate(moves = "UDUDUDUD") == True
    assert candidate(moves = "UUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDLLLLLLLLLLLLRRRRRRRRRRRRRR") == False
    assert candidate(moves = "RRDDLLUU") == True
    assert candidate(moves = "LL") == False
    assert candidate(moves = "UUUUDDDDLLLLRRRR") == True
    assert candidate(moves = "LRUD") == True
    assert candidate(moves = "UUDDLLRRUUDDLLRR") == True
    assert candidate(moves = "UUUUDDDD") == True
    assert candidate(moves = "RRDD") == False
    assert candidate(moves = "UUUUUUUUUUUUDDDDDDDDDDDDLLLLRRRRRRRRRRRR") == False
    assert candidate(moves = "RRRLLLDDDUUU") == True
    assert candidate(moves = "UD") == True
    assert candidate(moves = "UUUUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRR") == True
    assert candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLR") == True
    assert candidate(moves = "LDDRUURLDDRUURLDDRUURLDDRUURLDDR") == False
    assert candidate(moves = "LLLLLRRRRRRLLLLRRRRRRLLL") == True
    assert candidate(moves = "UUDDDDUUUUUUUUUUDDDD") == False
    assert candidate(moves = "UDUDUDUDUDUDUDUDUDUDUDUDUDUD") == True
    assert candidate(moves = "UDUDUDUDUDUDUDUD") == True
    assert candidate(moves = "LLLLRRRRUUUUDDDDLRRRLLLLUUUUDDDD") == False
    assert candidate(moves = "RRDDLLUURRDDLLUURRDDLLUU") == True
    assert candidate(moves = "LRLRLRLRLRLRLRLR") == True
    assert candidate(moves = "LLRRLLRRLLRRLLRRLLRRLLRRLLRR") == True
    assert candidate(moves = "LDRULDRULDRU") == True
    assert candidate(moves = "LLLLRRRRLLLLRRRRLLLLRRRRLLLLRRRR") == True
    assert candidate(moves = "LLRRDDUULLRRDDUULLRRDDUULLRRDDUULL") == False
    assert candidate(moves = "RULLDDRRULLDDRRULLDDRR") == False
    assert candidate(moves = "LLLLUUUUUURRRRRRRRDDDDDD") == False
    assert candidate(moves = "RULLDRLDURDURLDLURDURLDLURDURLDL") == False
    assert candidate(moves = "UDLRUDLRUDLRUDLR") == True
    assert candidate(moves = "UUDDUUDDUUDDUUDDLLLLRRRRLLLLRRRR") == True
    assert candidate(moves = "RLRLRLRLRLRLRLRL") == True
    assert candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDD") == True
    assert candidate(moves = "UDLLRRUUDDLLRRUUDDLLRRUUDDLLRR") == True
    assert candidate(moves = "UUUDDDLLLRRR") == True
    assert candidate(moves = "UUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRR") == True
    assert candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDDUUDD") == True
    assert candidate(moves = "UUUUDDDDLLLLRRRRUUUUDDDDLLLLRRRR") == True
    assert candidate(moves = "UUDDLLLLRRRRUUDDLLRR") == True
    assert candidate(moves = "UDUDUDUDUD") == True
    assert candidate(moves = "RLRLRLRLUDUDUDUD") == True
    assert candidate(moves = "URDLURDLURDLURDL") == True
    assert candidate(moves = "ULDRULDRLDURDLURDLURDLURDLURDL") == False
    assert candidate(moves = "RRDDLLUURRDDLLUURRDDLLUURRDDLLUU") == True
    assert candidate(moves = "LUDRLUDRLUDRLUDRLUDRLUDR") == True
    assert candidate(moves = "LRRLRLRLUDUDUDUD") == True
    assert candidate(moves = "UUDDUUDDUUDDUUDD") == True
    assert candidate(moves = "RRDDUULLRRDDUULL") == True
    assert candidate(moves = "LRUDLRUDLRUD") == True
    assert candidate(moves = "LURDLURDLURDLURD") == True
    assert candidate(moves = "LLLLRRRRUUDDUUDD") == True
    assert candidate(moves = "UDUDLRRLRLUDUDLR") == True
    assert candidate(moves = "LLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDD") == True
    assert candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLR") == True
    assert candidate(moves = "UUDDDDUUDDDDUUDD") == False
    assert candidate(moves = "LLLLRRRRLLLLRRRR") == True
    assert candidate(moves = "ULLDRRDUULLDRRDU") == True
    assert candidate(moves = "UUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDDUUDD") == True
    assert candidate(moves = "RRRRRRRRRRLLLLLLLLLLDDDDDDDDDDUUUUUUUUUU") == True
    assert candidate(moves = "RLRLRLRLRL") == True
    assert candidate(moves = "LLLLDDDDUUUURRRR") == True
    assert candidate(moves = "UUDDLLRRUUDDDDLLRRUUDDLLRR") == False
    assert candidate(moves = "LLRRUUDDUUDDLLRR") == True
    assert candidate(moves = "LRRLRLRLUDUDUDUDLRRLRLRLUDUDUDUD") == True
    assert candidate(moves = "RLRLRLRLRLRLRLRLRLRL") == True
    assert candidate(moves = "UUDDUURRDD") == False
    assert candidate(moves = "UUDDUULLRR") == False
    assert candidate(moves = "RRRRDDDDLLLLUUUU") == True
    assert candidate(moves = "UDLRUDLRUDLRUDLRUDLRUDLRUDLRUDLR") == True
    assert candidate(moves = "LLLLRRRRUUUDDDUUUDDDLLLLRRRR") == True
    assert candidate(moves = "UUUUUUUUDDDDDDDDLLLLLLLLRRRRRRRRRRLLRRUUDDLL") == True
    assert candidate(moves = "DDUUUUDDLLRRRR") == False
    assert candidate(moves = "UUDDLLUURRDDDDLLRR") == False
    assert candidate(moves = "RURURURURURURULULULULULULULU") == False
    assert candidate(moves = "UUUUUUDDDDDDLLLLRRRRRR") == False
    assert candidate(moves = "UUDDDDLLLLRRRRUUDDDD") == False
    assert candidate(moves = "LLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDDLLLLLLLLRRRRRRRRUUUUUUUUDDDDDDDD") == True
    assert candidate(moves = "RRRDDDLLLUUUUUDDDD") == False
    assert candidate(moves = "UUUUUUUUUUDDDDDDDDDDLLLLLLLLRRRRRRRRRR") == False
    assert candidate(moves = "RUDLRUDLRUDLRUDL") == True
    assert candidate(moves = "UUDDLLRRUUDDLLRRUUDDLLRR") == True
    assert candidate(moves = "RUDLRULDRLUDLRULDRLUDLRULDRL") == False
    assert candidate(moves = "UDUDUDUDUDUDUDUDUDUDUDUD") == True
    assert candidate(moves = "URDLURDLURDL") == True
    assert candidate(moves = "UUDDDDDDDLLLLRRRRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUDDDDDDDLLLLRRRR") == False
    assert candidate(moves = "RRDDLLUURRDDLLUU") == True
    assert candidate(moves = "UUUUUUUUDDDDDDDDLLLLRRRR") == True
    assert candidate(moves = "RRRLLLLDDDUUUUUDDDLLLLURRRDDDDUUU") == False
    assert candidate(moves = "DDDDLLLLUUUUUUUUDDDDLLLLRRRRRRRR") == True
    assert candidate(moves = "UDUDUDUDLRRLRLRL") == True
    assert candidate(moves = "LURDLURDLURDLURDLURDLURDLURDLURDL") == False
    assert candidate(moves = "UUUUUUUUDDDDDDDDLLLLRRRRRRRR") == False
    assert candidate(moves = "RRUUDDLLDDUURLLR") == True
    assert candidate(moves = "ULURDLDRULURDLDRULURDLDRULURDLDR") == True


