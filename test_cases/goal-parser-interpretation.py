def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(command = "G()()()()(al)") == "Gooooal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()()()()(al)") == "Gooooal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G") == "G"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G") == "G": {e}')
    
    total += 1
    try:
        result = candidate(command = "()") == "o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()") == "o": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)()()G") == "alGalooG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)()()G") == "alGalooG": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G)()") == "Go(G)o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G)()") == "Go(G)o": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)") == "GalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)") == "GalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(al)") == "Goal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(al)") == "Goal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()()") == "oooo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()()") == "oooo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G(al)G()") == "GoGalGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G(al)G()") == "GoGalGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)") == "GalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)") == "GalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(al)(al)") == "alalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(al)(al)") == "alalal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)") == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)") == "al": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()()G(al)()()G(al)()()") == "GalooGalooGaloo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()()G(al)()()G(al)()()") == "GalooGalooGaloo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)G(al)(al)G(al)(al)") == "GalalGalalGalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)G(al)(al)G(al)(al)") == "GalalGalalGalal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()()G(al)G(al)G(al)G(al)") == "ooooGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()()G(al)G(al)G(al)G(al)") == "ooooGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()G(al)G(al)G(al)G(al)G(al)G(al)") == "oooGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()G(al)G(al)G(al)G(al)G(al)G(al)") == "oooGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G(al)G()G(al)()") == "oGalGoGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G(al)G()G(al)()") == "oGalGoGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G(al)()G(al)()G(al)()") == "oGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G(al)()G(al)()G(al)()") == "oGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G()G()G()G()G()G()G()G()G()G()G()G()G()G(al)") == "GoGoGoGoGoGoGoGoGoGoGoGoGoGoGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G()G()G()G()G()G()G()G()G()G()G()G()G()G(al)") == "GoGoGoGoGoGoGoGoGoGoGoGoGoGoGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)(al)") == "Galalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)(al)") == "Galalal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()(G(al)G(al))(G(al)G(al))") == "o(GalGal)(GalGal)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()(G(al)G(al))(G(al)G(al))") == "o(GalGal)(GalGal)": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G(al)G(al)G(al)G(al)G(al)G(al)") == "oGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G(al)G(al)G(al)G(al)G(al)G(al)") == "oGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G()G(al)G()G(al)") == "GalGoGalGoGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G()G(al)G()G(al)") == "GalGoGalGoGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(al)G()(al)G()(al)") == "GoalGoalGoal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(al)G()(al)G()(al)") == "GoalGoalGoal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)()G(al)()G(al)()G(al)()G(al)()") == "alGaloGaloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)()G(al)()G(al)()G(al)()G(al)()") == "alGaloGaloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G(al)G()G(al)") == "oGalGoGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G(al)G()G(al)") == "oGalGoGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)()()G(al)G(al)()()G(al)G(al)()()G") == "alGalooGalGalooGalGalooG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)()()G(al)G(al)()()G(al)G(al)()()G") == "alGalooGalGalooGalGalooG": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)(al)(al)") == "Galalalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)(al)(al)") == "Galalalal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)(G(al)(G(al)G(al)))G(al)") == "alGal(Gal(GalGal))Gal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)(G(al)(G(al)G(al)))G(al)") == "alGal(Gal(GalGal))Gal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()()G()()G()()") == "GooGooGoo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()()G()()G()()") == "GooGooGoo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGaloGaloGaloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGaloGaloGaloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G()G(al)(al)G()") == "GoGoGalalGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G()G(al)(al)G()") == "GoGoGalalGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)()()G(al)G(al)G(al)") == "GalGalooGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)()()G(al)G(al)G(al)") == "GalGalooGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G()(G()(G())))") == "Go(Go(Go(Go)))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G()(G()(G())))") == "Go(Go(Go(Go)))": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G()G(al)()G(al)()G(al)") == "oGoGaloGaloGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G()G(al)()G(al)()G(al)") == "oGoGaloGaloGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G()()G()()G()()G(al)G()") == "oGooGooGooGalGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G()()G()()G()()G(al)G()") == "oGooGooGooGalGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)") == "GalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)") == "GalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(al)G()(al)G()(al)G()(al)") == "GoalGoalGoalGoal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(al)G()(al)G()(al)G()(al)") == "GoalGoalGoalGoal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()()()()(al)G(al)G(al)G(al)") == "GooooalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()()()()(al)G(al)G(al)G(al)") == "GooooalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)()()G(al)G(al)()()") == "GalGalooGalGaloo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)()()G(al)G(al)()()") == "GalGalooGalGaloo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G(al))(G(al))G()(G(al))(G(al))") == "Go(Gal)(Gal)Go(Gal)(Gal)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G(al))(G(al))G()(G(al))(G(al))") == "Go(Gal)(Gal)Go(Gal)(Gal)": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(al)G(al)(al)G(al)(al)") == "alalGalalGalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(al)G(al)(al)G(al)(al)") == "alalGalalGalal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)(al)G") == "GalalalG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)(al)G") == "GalalalG": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)()G(al)()G(al)()G(al)()") == "alGaloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)()G(al)()G(al)()G(al)()") == "alGaloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)(al)G(al)(al)(al)G(al)(al)(al)G") == "GalalalGalalalGalalalG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)(al)G(al)(al)(al)G(al)(al)(al)G") == "GalalalGalalalGalalalG": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(G(al)G(al))(G(al))") == "Gal(GalGal)(Gal)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(G(al)G(al))(G(al))") == "Gal(GalGal)(Gal)": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G(al))G()(G(al))") == "Go(Gal)Go(Gal)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G(al))G()(G(al))") == "Go(Gal)Go(Gal)": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G()G()G()G()G()G()G()") == "GoGoGoGoGoGoGoGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G()G()G()G()G()G()G()") == "GoGoGoGoGoGoGoGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()G(al)G(al)G(al)()()()") == "oooGalGalGalooo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()G(al)G(al)G(al)()()()") == "oooGalGalGalooo": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)()G(al)()G(al)G(al)") == "aloGaloGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)()G(al)()G(al)G(al)") == "aloGaloGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(al)(al)(al)G(al)G()") == "alalalalGalGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(al)(al)(al)G(al)G()") == "alalalalGalGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(G)(al)(G)(al)(G)(al)") == "al(G)al(G)al(G)al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(G)(al)(G)(al)(G)(al)") == "al(G)al(G)al(G)al": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)G(al)") == "GalalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)G(al)") == "GalalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G(al)G(al)G(al)G(al)G(al)") == "oGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G(al)G(al)G(al)G(al)G(al)") == "oGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G()(al)G()(al)G()(al)G()") == "GalGoalGoalGoalGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G()(al)G()(al)G()(al)G()") == "GalGoalGoalGoalGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G()(G)())") == "Go(Go(G)o)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G()(G)())") == "Go(Go(G)o)": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()()()()()()()()()()()()()()()()()()()G(al)") == "oooooooooooooooooooooGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()()()()()()()()()()()()()()()()()()()G(al)") == "oooooooooooooooooooooGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)") == "GaloGaloGaloGaloGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)") == "GaloGaloGaloGaloGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)(al)G(al)G") == "alGalalGalG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)(al)G(al)G") == "alGalalGalG": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)()G(al)()G(al)()G(al)()") == "aloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)()G(al)()G(al)()G(al)()") == "aloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(G()(G)(G)())G(al)") == "Gal(Go(G)(G)o)Gal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(G()(G)(G)())G(al)") == "Gal(Go(G)(G)o)Gal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G(al)G()G(al)") == "GoGalGoGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G(al)G()G(al)") == "GoGalGoGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(al)(al)G(al)") == "alalalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(al)(al)G(al)") == "alalalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(G(al))(G(al))(G(al))(G(al))(G(al))") == "al(Gal)(Gal)(Gal)(Gal)(Gal)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(G(al))(G(al))(G(al))(G(al))(G(al))") == "al(Gal)(Gal)(Gal)(Gal)(Gal)": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()()()G(al)()()") == "oooooGaloo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()()()G(al)()()") == "oooooGaloo": {e}')
    
    total += 1
    try:
        result = candidate(command = "()G(al)()G(al)()") == "oGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()G(al)()G(al)()") == "oGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)(al)(al)(al)(al)(al)(al)(al)") == "alalalalalalalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)(al)(al)(al)(al)(al)(al)(al)") == "alalalalalalalal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()()(al)()()()(al)()()()") == "ooooaloooalooo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()()(al)()()()(al)()()()") == "ooooaloooalooo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)G()G(al)G()G(al)G()") == "GalGoGalGoGalGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)G()G(al)G()G(al)G()") == "GalGoGalGoGalGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G()(G()(G)())())") == "Go(Go(Go(G)o)o)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G()(G()(G)())())") == "Go(Go(Go(G)o)o)": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGaloGaloGalo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGaloGaloGalo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(al)G(al)G(al)") == "GalalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(al)G(al)G(al)") == "GalalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)(G(al))(G(al))(G(al))G(al)") == "Gal(Gal)(Gal)(Gal)Gal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)(G(al))(G(al))(G(al))G(al)") == "Gal(Gal)(Gal)(Gal)Gal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()()()()(al)G(al)G(al)G(al)G(al)") == "GooooalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()()()()(al)G(al)G(al)G(al)G(al)") == "GooooalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()(G()(G()(G()())))") == "Go(Go(Go(Goo)))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()(G()(G()(G()())))") == "Go(Go(Go(Goo)))": {e}')
    
    total += 1
    try:
        result = candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)G(al)") == "GaloGaloGaloGaloGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)G(al)") == "GaloGaloGaloGaloGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGalGalGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G()G()G()G()G()G()G()G()G()G()G()G()G()G()G()") == "GoGoGoGoGoGoGoGoGoGoGoGoGoGoGoGo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G()G()G()G()G()G()G()G()G()G()G()G()G()G()G()") == "GoGoGoGoGoGoGoGoGoGoGoGoGoGoGoGo": {e}')
    
    total += 1
    try:
        result = candidate(command = "(al)()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == "aloooooooooooooooooooooooooooo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "(al)()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == "aloooooooooooooooooooooooooooo": {e}')
    
    total += 1
    try:
        result = candidate(command = "G()G()G()G()G(al)G(al)G(al)") == "GoGoGoGoGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "G()G()G()G()G(al)G(al)G(al)") == "GoGoGoGoGalGalGal": {e}')
    
    total += 1
    try:
        result = candidate(command = "()()()()()()()()()()G(al)G(al)G(al)G(al)G(al)") == "ooooooooooGalGalGalGalGal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(command = "()()()()()()()()()()G(al)G(al)G(al)G(al)G(al)") == "ooooooooooGalGalGalGalGal": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(command = "G()()()()(al)") == "Gooooal"
    assert candidate(command = "G") == "G"
    assert candidate(command = "()") == "o"
    assert candidate(command = "(al)G(al)()()G") == "alGalooG"
    assert candidate(command = "G()(G)()") == "Go(G)o"
    assert candidate(command = "G(al)G(al)") == "GalGal"
    assert candidate(command = "G()(al)") == "Goal"
    assert candidate(command = "()()()()") == "oooo"
    assert candidate(command = "G()G(al)G()") == "GoGalGo"
    assert candidate(command = "G(al)G(al)G(al)") == "GalGalGal"
    assert candidate(command = "(al)(al)(al)") == "alalal"
    assert candidate(command = "(al)") == "al"
    assert candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGal"
    assert candidate(command = "G(al)()()G(al)()()G(al)()()") == "GalooGalooGaloo"
    assert candidate(command = "G(al)(al)G(al)(al)G(al)(al)") == "GalalGalalGalal"
    assert candidate(command = "()()()()G(al)G(al)G(al)G(al)") == "ooooGalGalGalGal"
    assert candidate(command = "()()()G(al)G(al)G(al)G(al)G(al)G(al)") == "oooGalGalGalGalGalGal"
    assert candidate(command = "()G(al)G()G(al)()") == "oGalGoGalo"
    assert candidate(command = "()G(al)()G(al)()G(al)()") == "oGaloGaloGalo"
    assert candidate(command = "G()G()G()G()G()G()G()G()G()G()G()G()G()G()G(al)") == "GoGoGoGoGoGoGoGoGoGoGoGoGoGoGal"
    assert candidate(command = "G(al)(al)(al)") == "Galalal"
    assert candidate(command = "()(G(al)G(al))(G(al)G(al))") == "o(GalGal)(GalGal)"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGal"
    assert candidate(command = "()G(al)G(al)G(al)G(al)G(al)G(al)") == "oGalGalGalGalGalGal"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGal"
    assert candidate(command = "G(al)G()G(al)G()G(al)") == "GalGoGalGoGal"
    assert candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGalGalGal"
    assert candidate(command = "G()(al)G()(al)G()(al)") == "GoalGoalGoal"
    assert candidate(command = "(al)G(al)()G(al)()G(al)()G(al)()G(al)()") == "alGaloGaloGaloGaloGalo"
    assert candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGal"
    assert candidate(command = "()G(al)G()G(al)") == "oGalGoGal"
    assert candidate(command = "(al)G(al)()()G(al)G(al)()()G(al)G(al)()()G") == "alGalooGalGalooGalGalooG"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGal"
    assert candidate(command = "G(al)(al)(al)(al)") == "Galalalal"
    assert candidate(command = "(al)G(al)(G(al)(G(al)G(al)))G(al)") == "alGal(Gal(GalGal))Gal"
    assert candidate(command = "G()()G()()G()()") == "GooGooGoo"
    assert candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGalo"
    assert candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGaloGaloGaloGaloGaloGalo"
    assert candidate(command = "G()G()G(al)(al)G()") == "GoGoGalalGo"
    assert candidate(command = "G(al)G(al)()()G(al)G(al)G(al)") == "GalGalooGalGalGal"
    assert candidate(command = "G()(G()(G()(G())))") == "Go(Go(Go(Go)))"
    assert candidate(command = "()G()G(al)()G(al)()G(al)") == "oGoGaloGaloGal"
    assert candidate(command = "()G()()G()()G()()G(al)G()") == "oGooGooGooGalGo"
    assert candidate(command = "G(al)G(al)G(al)G(al)") == "GalGalGalGal"
    assert candidate(command = "G()(al)G()(al)G()(al)G()(al)") == "GoalGoalGoalGoal"
    assert candidate(command = "G()()()()(al)G(al)G(al)G(al)") == "GooooalGalGalGal"
    assert candidate(command = "G(al)G(al)()()G(al)G(al)()()") == "GalGalooGalGaloo"
    assert candidate(command = "G()(G(al))(G(al))G()(G(al))(G(al))") == "Go(Gal)(Gal)Go(Gal)(Gal)"
    assert candidate(command = "(al)(al)G(al)(al)G(al)(al)") == "alalGalalGalal"
    assert candidate(command = "G(al)(al)(al)G") == "GalalalG"
    assert candidate(command = "(al)G(al)()G(al)()G(al)()G(al)()") == "alGaloGaloGaloGalo"
    assert candidate(command = "G(al)(al)(al)G(al)(al)(al)G(al)(al)(al)G") == "GalalalGalalalGalalalG"
    assert candidate(command = "G(al)(G(al)G(al))(G(al))") == "Gal(GalGal)(Gal)"
    assert candidate(command = "G()(G(al))G()(G(al))") == "Go(Gal)Go(Gal)"
    assert candidate(command = "G()G()G()G()G()G()G()G()") == "GoGoGoGoGoGoGoGo"
    assert candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGalo"
    assert candidate(command = "()()()G(al)G(al)G(al)()()()") == "oooGalGalGalooo"
    assert candidate(command = "(al)()G(al)()G(al)G(al)") == "aloGaloGalGal"
    assert candidate(command = "(al)(al)(al)(al)G(al)G()") == "alalalalGalGo"
    assert candidate(command = "(al)(G)(al)(G)(al)(G)(al)") == "al(G)al(G)al(G)al"
    assert candidate(command = "G(al)(al)G(al)") == "GalalGal"
    assert candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGal"
    assert candidate(command = "()G(al)G(al)G(al)G(al)G(al)") == "oGalGalGalGalGal"
    assert candidate(command = "G(al)G()(al)G()(al)G()(al)G()") == "GalGoalGoalGoalGo"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGalGal"
    assert candidate(command = "G()(G()(G)())") == "Go(Go(G)o)"
    assert candidate(command = "()()()()()()()()()()()()()()()()()()()()()G(al)") == "oooooooooooooooooooooGal"
    assert candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)") == "GaloGaloGaloGaloGal"
    assert candidate(command = "(al)G(al)(al)G(al)G") == "alGalalGalG"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGal"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGal"
    assert candidate(command = "(al)()G(al)()G(al)()G(al)()") == "aloGaloGaloGalo"
    assert candidate(command = "G(al)(G()(G)(G)())G(al)") == "Gal(Go(G)(G)o)Gal"
    assert candidate(command = "G()G(al)G()G(al)") == "GoGalGoGal"
    assert candidate(command = "(al)(al)(al)G(al)") == "alalalGal"
    assert candidate(command = "G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "GalGalGalGalGalGalGalGalGalGalGalGal"
    assert candidate(command = "(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGal"
    assert candidate(command = "(al)(G(al))(G(al))(G(al))(G(al))(G(al))") == "al(Gal)(Gal)(Gal)(Gal)(Gal)"
    assert candidate(command = "()()()()()G(al)()()") == "oooooGaloo"
    assert candidate(command = "()G(al)()G(al)()") == "oGaloGalo"
    assert candidate(command = "(al)(al)(al)(al)(al)(al)(al)(al)") == "alalalalalalalal"
    assert candidate(command = "()()()()(al)()()()(al)()()()") == "ooooaloooalooo"
    assert candidate(command = "G(al)G()G(al)G()G(al)G()") == "GalGoGalGoGalGo"
    assert candidate(command = "G()(G()(G()(G)())())") == "Go(Go(Go(G)o)o)"
    assert candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()G(al)()") == "GaloGaloGaloGaloGaloGaloGaloGalo"
    assert candidate(command = "G(al)(al)G(al)G(al)") == "GalalGalGal"
    assert candidate(command = "G(al)(G(al))(G(al))(G(al))G(al)") == "Gal(Gal)(Gal)(Gal)Gal"
    assert candidate(command = "G()()()()(al)G(al)G(al)G(al)G(al)") == "GooooalGalGalGalGal"
    assert candidate(command = "G()(G()(G()(G()())))") == "Go(Go(Go(Goo)))"
    assert candidate(command = "G(al)()G(al)()G(al)()G(al)()G(al)G(al)") == "GaloGaloGaloGaloGalGal"
    assert candidate(command = "(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)G(al)") == "alGalGalGalGalGalGalGalGalGalGalGal"
    assert candidate(command = "G()G()G()G()G()G()G()G()G()G()G()G()G()G()G()G()") == "GoGoGoGoGoGoGoGoGoGoGoGoGoGoGoGo"
    assert candidate(command = "(al)()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == "aloooooooooooooooooooooooooooo"
    assert candidate(command = "G()G()G()G()G(al)G(al)G(al)") == "GoGoGoGoGalGalGal"
    assert candidate(command = "()()()()()()()()()()G(al)G(al)G(al)G(al)G(al)") == "ooooooooooGalGalGalGalGal"


