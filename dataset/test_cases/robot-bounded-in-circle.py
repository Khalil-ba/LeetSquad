def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(instructions = "GGLGRGLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLGRGLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLLRLLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLLRLLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRGL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRGL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLGRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLGRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLGRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLGRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRRRLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRRRLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRGRRG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRGRRG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGRRGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGRRGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLLGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLLGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "L") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "L") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "R") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "R") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGLGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGLGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "G") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "G") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGRRG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGRRG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLLRLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLLRLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLLGLLGRRRRGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLLGLLGRRRRGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGRRGRRGRRGRRGLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGRRGRRGRRGRRGLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRGLRGLRGLRGLRGLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRGLRGLRGLRGLRGLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGGRRRRRLLLLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGGRRRRRLLLLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGRRLLGGRRLLGGRRLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGRRLLGGRRLLGGRRLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGGRRGGRRGGRRG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGGRRGGRRGGRRG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRLLLLGGGGRRRLLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRLLLLGGGGRRRLLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLRRLLRRLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLRRLLRRLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRGLRGLRGLRGLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRGLRGLRGLRGLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRRGGGGLLGGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRRGGGGLLGGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGLGLGLGLGLGLGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGLGLGLGLGLGLGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRRRRRRRRRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRRRRRRRRRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLGGGLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLGGGLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLLGLGLLGLGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLLGLGLLGLGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGRRLLGGLLRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGRRLLGGLLRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGGLLLRRRGGGGGLLLRRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGGLLLRRRGGGGGLLLRRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRLRLRLRLRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRLRLRLRLRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLLLRRRRLLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLLLRRRRLLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGRGLGRGLGRGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGRGLGRGLGRGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRRLGLRRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRRLGLRRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGRRGRRGRRGRRGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGRRGRRGRRGRRGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLLLRRRRLLLLRRRRGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLLLRRRRLLLLRRRRGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGRRRLLLLGGGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGRRRLLLLGGGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGRLGLGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGRLGLGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLGGGGLLRRLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLGGGGLLRRLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLLGGRRLLRRGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLLGGRRLLRRGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGRRGLLGLLRRGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGRRGLLGLLRRGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRLGRLGRLGRLRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRLGRLGRLGRLRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLLRRGGLLRRGGLLRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLLRRGGLLRRGGLLRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGRRRGRRRRGGGRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGRRRGRRRRGGGRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLGGGGLLRRG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLGGGGLLRRG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRRRLLRRRRLLRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRRRLLRRRRLLRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGRRGRRGRRGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGRRGRRGRRGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGLGGGLGGGLGGGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGLGGGLGGGLGGGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGRRGGRRGGRRGGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGRRGGRRGGRRGGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLRRGGGGLLRRGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLRRGGGGLLRRGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLRLRGGRRLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLRLRGGRRLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRGGLLLGGRRGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRGGLLLGGRRGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRRGLRRGLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRRGLRRGLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLLLGRRGGGLLRLLRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLLLGRRGGGLLRLLRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRLRLRLRLRRGGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRLRLRLRLRRGGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRGLLRRGLLRRGLLRRG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRGLLRRGLLRRGLLRRG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLLGRRGRRGLLGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLLGRRGRRGLLGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGGGGRLRRRRGLLGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGGGGRLRRRRGLLGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGGLLLGGRRGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGGLLLGGRRGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLLLRRRLLLLRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLLLRRRLLLLRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRLLRRLLRRLLRRLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRLLRRLLRRLLRRLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLGGGLLLRRGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLGGGLLLRRGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRGRLGGRLGRLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRGRLGGRLGRLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGLLLGGRRRRGGGL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGLLLGGRRRRGGGL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGGRLGRLGLGRLGLGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGGRLGRLGLGRLGLGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLGGLGGRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLGGLGGRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLRLGLRLGLRLGLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLRLGLRLGLRLGLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGLGLGRRGRRGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGLGLGRRGRRGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGGRLGRRGLLGRRGLGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGGRLGRRGLLGRRGLGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRLLLLRRRLLLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRLLLLRRRLLLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRGLRLRLGRRGGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRGLRLRLGRRGGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGGRRGLGGLLRRGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGGRRGLGGLLRRGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGLLLRRRGGRRRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGLLLRRRGGRRRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRLRLRLRLRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRLRLRLRLRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGRRGGLLRRGGLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGRRGGLLRRGGLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGRRRLLLLLGGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGRRRLLLLLGGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRGLLGGLLLGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRGLLGGLLLGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGRRLLGGRRLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGRRLLGGRRLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGRGLRLRLGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGRGLRLRLGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGGRRGRRLLGGRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGGRRGRRLLGGRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLLLRRRRGLLLRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLLLRRRRGLLLRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGLLLGGGLLLGGGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGLLLGGGLLLGGGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRLGLRLGLRLGLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRLGLRLGLRLGLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLLGLGLLGLGRRGLGRR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLLGLGLLGLGRRGLGRR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGRLLRLRRRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGRLLRLRRRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLGLLRLRLRLRL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLGLLRLRLRLRL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGLGLGLGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGLGLGLGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLGGRRLLGGRRLLGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLGGRRLLGGRRLLGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGGRLGRLGLGRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGGRLGRLGLGRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLLGLGLGLGLLGLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLLGLGLGLGLLGLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRLRLRLRLRLRLRLRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRLRLRLRLRLRLRLRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLRLRRLLGLGGGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLRLRRLLGLGGGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGGGGGGGGGGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGGGGGGGGGGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRRLRLLGLGLGRLR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRRLRLLGLGLGRLR") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGLGGGLGGGLGGGLGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGLGGGLGGGLGGGLGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLRLGLRLGLRLGLRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLRLGLRLGLRLGLRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGLGLGLGLGLGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGLGLGLGLGLGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLGLGLGLGLGLGLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLGLGLGLGLGLGLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LLLLLLLLLLLLLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LLLLLLLLLLLLLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLGLGLGLGLGLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLGLGLGLGLGLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGRRGLGRRGRRGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGRRGLGRRGRRGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRLRLRLRLRLRLRLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRLRLRLRLRLRLRLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGLGLGLGL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGLGLGLGL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGRRGRRGRRGRRG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGRRGRRGRRGRRG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGLLRLLGRGLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGLLRLLGRGLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGLRLGLRLG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGLRLGLRLG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLRLGLLGGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLRLGLLGGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRRLLRRLLRRLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRRLLRRLLRRLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLRRLLRRLLRRLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLRRLLRRLLRRLLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRLRLRLRLRLRLRLGG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRLRLRLRLRLRLRLGG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRGGLLRGGLLRRGLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRGGLLRGGLLRRGLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGGGGGGGGGGGGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGGGGGGGGGGGGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGLRGGGLLRLLGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGLRGGGLLRLLGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRRGLLLGGGGRRRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRRGLLLGGGGRRRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRRRLLLLGGGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRRRLLLLGGGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRRGLGLRLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRRGLGLRLRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LGGRLGRRGLG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LGGRLGRRGLG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGGRRRRLLLL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGGRRRRLLLL") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RGLLRLGLGRRG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RGLLRLGLGRRG") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "RRLLRRLLRRLLRRLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "RRLLRRLLRRLLRRLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLRLGLRLGLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLRLGLRLGLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GLGRRRRRGGGLLGLGRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GLGRRRRRGGGLLGLGRR") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGGLRRLLGLRRLL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGGLRRLLGLRRLL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GGLLGGGGLLGGGG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GGLLGGGGLLGGGG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRLRLRLRL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRLRLRLRL") == True: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "GRRGGGGLLLRRGGLG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "GRRGGGGLLLRRGGLG") == False: {e}')
    
    total += 1
    try:
        result = candidate(instructions = "LRRGLLRRGLLRRGLLRR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = "LRRGLLRRGLLRRGLLRR") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(instructions = "GGLGRGLL") == True
    assert candidate(instructions = "LLLL") == True
    assert candidate(instructions = "GLLRLLRL") == True
    assert candidate(instructions = "GRGL") == False
    assert candidate(instructions = "LLGRL") == True
    assert candidate(instructions = "LRRL") == True
    assert candidate(instructions = "LLGRR") == False
    assert candidate(instructions = "LRRRRLL") == True
    assert candidate(instructions = "LL") == True
    assert candidate(instructions = "RRGRRG") == True
    assert candidate(instructions = "GGGG") == False
    assert candidate(instructions = "GGRRGG") == True
    assert candidate(instructions = "GLGLG") == True
    assert candidate(instructions = "GGLLGG") == True
    assert candidate(instructions = "L") == True
    assert candidate(instructions = "GL") == True
    assert candidate(instructions = "R") == True
    assert candidate(instructions = "GG") == False
    assert candidate(instructions = "GLGLGLGL") == True
    assert candidate(instructions = "RRRR") == True
    assert candidate(instructions = "G") == False
    assert candidate(instructions = "GLGLGRRG") == False
    assert candidate(instructions = "GLLRLLRR") == True
    assert candidate(instructions = "RR") == True
    assert candidate(instructions = "LGLLGLLGRRRRGG") == True
    assert candidate(instructions = "LGR") == False
    assert candidate(instructions = "GLGLGRRR") == True
    assert candidate(instructions = "GRRG") == True
    assert candidate(instructions = "GRRGRRGRRGRRGRRGLG") == True
    assert candidate(instructions = "GLRGLRGLRGLRGLRGLR") == False
    assert candidate(instructions = "GGGGGRRRRRLLLLL") == False
    assert candidate(instructions = "GGRRLLGGRRLLGGRRLL") == False
    assert candidate(instructions = "LGGRRGGRRGGRRG") == True
    assert candidate(instructions = "RRRLLLLGGGGRRRLLL") == True
    assert candidate(instructions = "RRLLRRLLRRLLRR") == True
    assert candidate(instructions = "GLRGLRGLRGLRGLR") == False
    assert candidate(instructions = "RRRRGGGGLLGGGG") == True
    assert candidate(instructions = "GLGLGLGLGLGLGLGLGL") == True
    assert candidate(instructions = "RRRRRRRRRRRRRR") == True
    assert candidate(instructions = "RRLLGGGLLLRRRR") == True
    assert candidate(instructions = "LGLLGLGLLGLGRR") == True
    assert candidate(instructions = "GGRRLLGGLLRR") == False
    assert candidate(instructions = "GGGGGLLLRRRGGGGGLLLRRR") == False
    assert candidate(instructions = "LRRLRLRLRLRLRLRL") == True
    assert candidate(instructions = "LLLLRRRRLLLLRRRR") == True
    assert candidate(instructions = "GLGRGLGRGLGRGL") == True
    assert candidate(instructions = "GLRRLGLRRL") == False
    assert candidate(instructions = "GRRGRRGRRGRRGRRGRR") == True
    assert candidate(instructions = "LLLLRRRRLLLLRRRRGG") == False
    assert candidate(instructions = "GGGGRRRLLLLGGGRR") == True
    assert candidate(instructions = "GRRGRLGLGG") == True
    assert candidate(instructions = "RRLLGGGGLLRRLG") == True
    assert candidate(instructions = "GGLLGGRRLLRRGG") == False
    assert candidate(instructions = "GLGRRGLLGLLRRGGG") == True
    assert candidate(instructions = "LRRLGRLGRLGRLRLR") == True
    assert candidate(instructions = "GLLRRGGLLRRGGLLRR") == False
    assert candidate(instructions = "GGGRRRGRRRRGGGRRR") == True
    assert candidate(instructions = "RRLLGGGGLLRRG") == False
    assert candidate(instructions = "LRRRRLLRRRRLLRRR") == True
    assert candidate(instructions = "GRRGRRGRRGRRGG") == False
    assert candidate(instructions = "GGGLGGGLGGGLGGGL") == True
    assert candidate(instructions = "GGRRGGRRGGRRGGRR") == True
    assert candidate(instructions = "LLRRGGGGLLRRGG") == False
    assert candidate(instructions = "GGLRLRGGRRLL") == False
    assert candidate(instructions = "LRRGGLLLGGRRGG") == False
    assert candidate(instructions = "GLRRGLRRGLRR") == True
    assert candidate(instructions = "LLLLGRRGGGLLRLLRRR") == True
    assert candidate(instructions = "GLRLRLRLRLRRGGGG") == True
    assert candidate(instructions = "RRGLLRRGLLRRGLLRRG") == True
    assert candidate(instructions = "GLLGRRGRRGLLGRR") == True
    assert candidate(instructions = "LGGGGRLRRRRGLLGG") == True
    assert candidate(instructions = "GRRGGLLLGGRRGG") == True
    assert candidate(instructions = "LLLLRRRLLLLRRR") == True
    assert candidate(instructions = "LRLLRRLLRRLLRRLL") == True
    assert candidate(instructions = "RRLLGGGLLLRRGG") == True
    assert candidate(instructions = "RRGRLGGRLGRLG") == True
    assert candidate(instructions = "GGGLLLGGRRRRGGGL") == False
    assert candidate(instructions = "GLGGRLGRLGLGRLGLGG") == True
    assert candidate(instructions = "GGLGGLGGRRRR") == True
    assert candidate(instructions = "LGLRLGLRLGLRLGLRL") == True
    assert candidate(instructions = "GLGLGLGLGRRGRRGL") == True
    assert candidate(instructions = "LGGRLGRRGLLGRRGLGRR") == True
    assert candidate(instructions = "RRRLLLLRRRLLLL") == True
    assert candidate(instructions = "GLRGLRLRLGRRGGGG") == True
    assert candidate(instructions = "LGGRRGLGGLLRRGL") == True
    assert candidate(instructions = "GGGGLLLRRRGGRRRL") == True
    assert candidate(instructions = "GLRLRLRLRLRLRLRL") == True
    assert candidate(instructions = "GLGRRGGLLRRGGLLRR") == True
    assert candidate(instructions = "GGGGRRRLLLLLGGGG") == True
    assert candidate(instructions = "RRRGLLGGLLLGGG") == True
    assert candidate(instructions = "GGRRLLGGRRLL") == False
    assert candidate(instructions = "LGRGLRLRLGRR") == True
    assert candidate(instructions = "LGGRRGRRLLGGRL") == True
    assert candidate(instructions = "GLLLRRRRGLLLRRRR") == True
    assert candidate(instructions = "GGGLLLGGGLLLGGGL") == True
    assert candidate(instructions = "GLRLGLRLGLRLGLRL") == True
    assert candidate(instructions = "LGLLGLGLLGLGRRGLGRR") == False
    assert candidate(instructions = "GLGRLLRLRRRL") == False
    assert candidate(instructions = "LGLGLLRLRLRLRL") == False
    assert candidate(instructions = "GLGLGLGLGLGL") == True
    assert candidate(instructions = "LLGGRRLLGGRRLLGG") == True
    assert candidate(instructions = "GLGGRLGRLGLGRL") == True
    assert candidate(instructions = "LGLLGLGLGLGLLGLL") == True
    assert candidate(instructions = "LRLRLRLRLRLRLRLRLR") == True
    assert candidate(instructions = "GGLRLRRLLGLGGGG") == True
    assert candidate(instructions = "GGGGGGGGGGGGGG") == False
    assert candidate(instructions = "GRRRLRLLGLGLGRLR") == False
    assert candidate(instructions = "GGGLGGGLGGGLGGGLGG") == False
    assert candidate(instructions = "LGLRLGLRLGLRLGLRLR") == True
    assert candidate(instructions = "GLGLGLGLGLGLGLGL") == True
    assert candidate(instructions = "LGLGLGLGLGLGLGLG") == True
    assert candidate(instructions = "LLLLLLLLLLLLLL") == True
    assert candidate(instructions = "LGLGLGLGLGLGLG") == True
    assert candidate(instructions = "GGRRGLGRRGRRGRR") == True
    assert candidate(instructions = "LRLRLRLRLRLRLRLR") == True
    assert candidate(instructions = "GLGLGLGLGL") == True
    assert candidate(instructions = "GRRGRRGRRGRRGRRG") == True
    assert candidate(instructions = "GRRGLLRLLGRGLL") == True
    assert candidate(instructions = "LGLRLGLRLG") == True
    assert candidate(instructions = "GGLRLGLLGGRR") == True
    assert candidate(instructions = "GLRRLLRRLLRRLLRR") == True
    assert candidate(instructions = "RRLLRRLLRRLLRRLLRR") == True
    assert candidate(instructions = "GLRLRLRLRLRLRLRLGG") == True
    assert candidate(instructions = "RRGGLLRGGLLRRGLL") == True
    assert candidate(instructions = "GGGGGGGGGGGGGGGG") == False
    assert candidate(instructions = "GRRGLRGGGLLRLLGRR") == True
    assert candidate(instructions = "GLRRGLLLGGGGRRRR") == True
    assert candidate(instructions = "RRRRLLLLGGGG") == False
    assert candidate(instructions = "GLRRGLGLRLRR") == True
    assert candidate(instructions = "LGGRLGRRGLG") == False
    assert candidate(instructions = "GGGGRRRRLLLL") == False
    assert candidate(instructions = "RGLLRLGLGRRG") == True
    assert candidate(instructions = "RRLLRRLLRRLLRRLL") == True
    assert candidate(instructions = "GLRLGLRLGLRL") == True
    assert candidate(instructions = "GLGRRRRRGGGLLGLGRR") == True
    assert candidate(instructions = "GGGLRRLLGLRRLL") == True
    assert candidate(instructions = "GGLLGGGGLLGGGG") == False
    assert candidate(instructions = "LRRLRLRLRL") == True
    assert candidate(instructions = "GRRGGGGLLLRRGGLG") == False
    assert candidate(instructions = "LRRGLLRRGLLRRGLLRR") == True


