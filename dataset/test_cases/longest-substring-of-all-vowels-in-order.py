def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaauuaeiuuuuuuuuuuuuuuuuuuuuaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaauuaeiuuuuuuuuuuuuuuuuuuuuaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuaauuaeiu") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuaauuaeiu") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuuaaaaaaeiou") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuuaaaaaaeiou") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuu") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuu") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeeeiiiioooauuuaeiou") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeeeiiiioooauuuaeiou") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuuuaaaaaaaaaeeeeiiiioooouuuuuu") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuuuaaaaaaaaaeeeeiiiioooouuuuuu") == 27: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaaeiouaaaaaaaaaaeiouuuuuuuuuuuuuuuuuuuu") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaaeiouaaaaaaaaaaeiouuuuuuuuuuuuuuuuuuuu") == 33: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuuaeiouuu") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuuaeiouuu") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaouuuooauuaeiu") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaouuuooauuaeiu") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaeeeeeeeeeeiiiiiiioooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaeeeeeeeeeeiiiiiiioooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 68: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiioooaeiouuu") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiioooaeiouuu") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiooouuuaeiou") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiooouuuaeiou") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiou") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiou") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuu") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuu") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiaaaouuuooaauuaeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiaaaouuuooaauuaeiaaioaaaaeiiiiouuuooaauuaeiu") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiooouuuooauuaeiu") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiooouuuooauuaeiu") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word = "uuuuuuuuuuuuuuuuuuuu") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uuuuuuuuuuuuuuuuuuuu") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaauuaeiuuuuuuuuuuuuuuuuuuuuaaa") == 0
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuaauuaeiu") == 0
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuuaaaaaaeiou") == 10
    assert candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuu") == 7
    assert candidate(word = "aeeeiiiioooauuuaeiou") == 5
    assert candidate(word = "aeiaaioaaaaeiiiiouuuuuaaaaaaaaaeeeeiiiioooouuuuuu") == 27
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaaeiouaaaaaaaaaaeiouuuuuuuuuuuuuuuuuuuu") == 33
    assert candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuuaeiouuu") == 7
    assert candidate(word = "aeiaaioaaaaeiiaaaouuuooauuaeiu") == 0
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 5
    assert candidate(word = "aaaaaaaaaeeeeeeeeeeiiiiiiioooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 68
    assert candidate(word = "aeiaaioaaaaeiioooaeiouuu") == 7
    assert candidate(word = "aeiaaioaaaaeiiooouuuaeiou") == 13
    assert candidate(word = "a") == 0
    assert candidate(word = "aeiou") == 5
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuu") == 0
    assert candidate(word = "aeiaaioaaaaeiiaaaouuuooaauuaeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
    assert candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
    assert candidate(word = "aeiaaioaaaaeiiooouuuooauuaeiu") == 13
    assert candidate(word = "uuuuuuuuuuuuuuuuuuuu") == 0


