def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(beginWord = "leet",endWord = "code",wordList = ['lest', 'leet', 'lose', 'code', 'lode', 'robe', 'home', 'dote', 'cake']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "leet",endWord = "code",wordList = ['lest', 'leet', 'lose', 'code', 'lode', 'robe', 'home', 'dote', 'cake']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "talk",endWord = "tell",wordList = ['talk', 'tell', 'tall', 'toll', 'toll']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "talk",endWord = "tell",wordList = ['talk', 'tell', 'tall', 'toll', 'toll']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "talk",endWord = "walk",wordList = ['talk', 'walk', 'tall', 'tale', 'tali', 'wali', 'wali', 'wale', 'wall', 'walk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "talk",endWord = "walk",wordList = ['talk', 'walk', 'tall', 'tale', 'tali', 'wali', 'wali', 'wale', 'wall', 'walk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "leet",endWord = "code",wordList = ['lest', 'leet', 'lose', 'code', 'lode', 'robe', 'lost']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "leet",endWord = "code",wordList = ['lest', 'leet', 'lose', 'code', 'lode', 'robe', 'lost']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "red",endWord = "tax",wordList = ['ted', 'tex', 'red', 'tax', 'tad', 'den', 'rex', 'pee']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "red",endWord = "tax",wordList = ['ted', 'tex', 'red', 'tax', 'tad', 'den', 'rex', 'pee']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "cat",endWord = "dog",wordList = ['bat', 'rat', 'hat', 'hot', 'dot', 'dog']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "cat",endWord = "dog",wordList = ['bat', 'rat', 'hat', 'hot', 'dot', 'dog']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "hit",endWord = "cog",wordList = ['hot', 'dot', 'dog', 'lot', 'log']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "hit",endWord = "cog",wordList = ['hot', 'dot', 'dog', 'lot', 'log']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "hit",endWord = "cog",wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "hit",endWord = "cog",wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "abcf",endWord = "aefh",wordList = ['abcf', 'aefg', 'aefh', 'aegh', 'cefh', 'cefh', 'aegh', 'cefg', 'abcf', 'abef']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "abcf",endWord = "aefh",wordList = ['abcf', 'aefg', 'aefh', 'aegh', 'cefh', 'cefh', 'aegh', 'cefg', 'abcf', 'abef']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "machine",endWord = "natural",wordList = ['machene', 'machenr', 'machrne', 'machren', 'machenl', 'machenm', 'machene', 'machrne', 'machren', 'machenl', 'machenm', 'machane', 'machrne', 'machren', 'machenl', 'machenm', 'machenl', 'machene', 'machrne', 'machren', 'machenl', 'machenm', 'nachenl', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'natural']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "machine",endWord = "natural",wordList = ['machene', 'machenr', 'machrne', 'machren', 'machenl', 'machenm', 'machene', 'machrne', 'machren', 'machenl', 'machenm', 'machane', 'machrne', 'machren', 'machenl', 'machenm', 'machenl', 'machene', 'machrne', 'machren', 'machenl', 'machenm', 'nachenl', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'natural']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "listen",endWord = "silent",wordList = ['lisen', 'litesn', 'litens', 'listne', 'listen', 'siltne', 'silent', 'linset', 'lintes', 'sleint', 'ltsine', 'lintse', 'lisnet', 'lsitne', 'lnties', 'lintes', 'lintes', 'linsat', 'slient', 'lsinte', 'linset']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "listen",endWord = "silent",wordList = ['lisen', 'litesn', 'litens', 'listne', 'listen', 'siltne', 'silent', 'linset', 'lintes', 'sleint', 'ltsine', 'lintse', 'lisnet', 'lsitne', 'lnties', 'lintes', 'lintes', 'linsat', 'slient', 'lsinte', 'linset']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "algorithm",endWord = "rhythm",wordList = ['alorhythm', 'alohrhythm', 'alohrhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "algorithm",endWord = "rhythm",wordList = ['alorhythm', 'alohrhythm', 'alohrhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(beginWord = "physics",endWord = "chemist",wordList = ['phyiscs', 'phyisic', 'phyisct', 'phyisci', 'phyicsi', 'physics', 'physisi', 'physcii', 'physici', 'phyiscs', 'phyiscs', 'phyiscs', 'phyiscs', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'chemics', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(beginWord = "physics",endWord = "chemist",wordList = ['phyiscs', 'phyisic', 'phyisct', 'phyisci', 'phyicsi', 'physics', 'physisi', 'physcii', 'physici', 'phyiscs', 'phyiscs', 'phyiscs', 'phyiscs', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'chemics', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist']) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(beginWord = "leet",endWord = "code",wordList = ['lest', 'leet', 'lose', 'code', 'lode', 'robe', 'home', 'dote', 'cake']) == 0
    assert candidate(beginWord = "talk",endWord = "tell",wordList = ['talk', 'tell', 'tall', 'toll', 'toll']) == 3
    assert candidate(beginWord = "talk",endWord = "walk",wordList = ['talk', 'walk', 'tall', 'tale', 'tali', 'wali', 'wali', 'wale', 'wall', 'walk']) == 2
    assert candidate(beginWord = "leet",endWord = "code",wordList = ['lest', 'leet', 'lose', 'code', 'lode', 'robe', 'lost']) == 6
    assert candidate(beginWord = "red",endWord = "tax",wordList = ['ted', 'tex', 'red', 'tax', 'tad', 'den', 'rex', 'pee']) == 4
    assert candidate(beginWord = "cat",endWord = "dog",wordList = ['bat', 'rat', 'hat', 'hot', 'dot', 'dog']) == 5
    assert candidate(beginWord = "hit",endWord = "cog",wordList = ['hot', 'dot', 'dog', 'lot', 'log']) == 0
    assert candidate(beginWord = "hit",endWord = "cog",wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5
    assert candidate(beginWord = "abcf",endWord = "aefh",wordList = ['abcf', 'aefg', 'aefh', 'aegh', 'cefh', 'cefh', 'aegh', 'cefg', 'abcf', 'abef']) == 0
    assert candidate(beginWord = "machine",endWord = "natural",wordList = ['machene', 'machenr', 'machrne', 'machren', 'machenl', 'machenm', 'machene', 'machrne', 'machren', 'machenl', 'machenm', 'machane', 'machrne', 'machren', 'machenl', 'machenm', 'machenl', 'machene', 'machrne', 'machren', 'machenl', 'machenm', 'nachenl', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'nachene', 'nachrne', 'nachren', 'nachenl', 'nachenm', 'natural']) == 0
    assert candidate(beginWord = "listen",endWord = "silent",wordList = ['lisen', 'litesn', 'litens', 'listne', 'listen', 'siltne', 'silent', 'linset', 'lintes', 'sleint', 'ltsine', 'lintse', 'lisnet', 'lsitne', 'lnties', 'lintes', 'lintes', 'linsat', 'slient', 'lsinte', 'linset']) == 0
    assert candidate(beginWord = "algorithm",endWord = "rhythm",wordList = ['alorhythm', 'alohrhythm', 'alohrhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'alorhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm', 'rhythm']) == 0
    assert candidate(beginWord = "physics",endWord = "chemist",wordList = ['phyiscs', 'phyisic', 'phyisct', 'phyisci', 'phyicsi', 'physics', 'physisi', 'physcii', 'physici', 'phyiscs', 'phyiscs', 'phyiscs', 'phyiscs', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'physcis', 'chemics', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist', 'chemist']) == 0


