def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abc', 'abc']) == ['a', 'b', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abc', 'abc']) == ['a', 'b', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['bella', 'label', 'roller']) == ['e', 'l', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['bella', 'label', 'roller']) == ['e', 'l', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'java', 'javascript']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'java', 'javascript']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hold']) == ['l', 'o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hold']) == ['l', 'o']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'aabbc', 'abc']) == ['a', 'b', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'aabbc', 'abc']) == ['a', 'b', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cool', 'lock', 'cook']) == ['c', 'o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cool', 'lock', 'cook']) == ['c', 'o']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'a', 'a', 'a']) == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'a', 'a', 'a']) == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apricot', 'peach']) == ['a', 'p']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apricot', 'peach']) == ['a', 'p']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['happy', 'happy', 'happy']) == ['h', 'a', 'p', 'p', 'y']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['happy', 'happy', 'happy']) == ['h', 'a', 'p', 'p', 'y']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'a', 'a']) == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'a', 'a']) == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['flower', 'flow', 'flight']) == ['f', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['flower', 'flow', 'flight']) == ['f', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['common', 'commons', 'commonground']) == ['c', 'o', 'o', 'm', 'm', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['common', 'commons', 'commonground']) == ['c', 'o', 'o', 'm', 'm', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['sophistication', 'sophisticated', 'sophisticating']) == ['s', 's', 'o', 'p', 'h', 'i', 'i', 't', 't', 'c', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['sophistication', 'sophisticated', 'sophisticating']) == ['s', 's', 'o', 'p', 'h', 'i', 'i', 't', 't', 'c', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['encyclopedia', 'encyclopedia', 'encyclopedic']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['encyclopedia', 'encyclopedia', 'encyclopedic']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'abrakadabrac', 'abrakadabracd']) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'abrakadabrac', 'abrakadabracd']) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['multifaceted', 'multimodal', 'multiplicity']) == ['m', 'u', 'l', 't', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['multifaceted', 'multimodal', 'multiplicity']) == ['m', 'u', 'l', 't', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['encyclopedia', 'encyclopedic', 'encyclopediae']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['encyclopedia', 'encyclopedic', 'encyclopediae']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'perception', 'competition']) == ['e', 'p', 't', 'i', 'o', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'perception', 'competition']) == ['e', 'p', 't', 'i', 'o', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'logarithm', 'rhythm', 'harmony']) == ['r', 'h', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'logarithm', 'rhythm', 'harmony']) == ['r', 'h', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'zoo', 'ozone']) == ['o', 'o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'zoo', 'ozone']) == ['o', 'o']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'bandana', 'panama']) == ['a', 'a', 'a', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'bandana', 'panama']) == ['a', 'a', 'a', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'logarithm', 'altruism']) == ['a', 'l', 'r', 'i', 't', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'logarithm', 'altruism']) == ['a', 'l', 'r', 'i', 't', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['floccinaucinihilipilification', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'supercalifragilisticexpialidocious']) == ['l', 'l', 'l', 'o', 'o', 'c', 'c', 'c', 'i', 'i', 'i', 'i', 'i', 'i', 'a', 'a', 'u', 'p', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['floccinaucinihilipilification', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'supercalifragilisticexpialidocious']) == ['l', 'l', 'l', 'o', 'o', 'c', 'c', 'c', 'i', 'i', 'i', 'i', 'i', 'i', 'a', 'a', 'u', 'p', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'venture', 'ambient']) == ['e', 'n', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'venture', 'ambient']) == ['e', 'n', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algorithms', 'algebra']) == ['a', 'l', 'g', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algorithms', 'algebra']) == ['a', 'l', 'g', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'replication', 'repetitive']) == ['r', 'e', 'p', 't', 'i', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'replication', 'repetitive']) == ['r', 'e', 'p', 't', 'i', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['characterization', 'character', 'charisma']) == ['c', 'h', 'a', 'a', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['characterization', 'character', 'charisma']) == ['c', 'h', 'a', 'a', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'petition', 'portion']) == ['p', 't', 'i', 'o', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'petition', 'portion']) == ['p', 't', 'i', 'o', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unbelievable', 'believable', 'believability']) == ['b', 'b', 'e', 'e', 'l', 'l', 'i', 'v', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unbelievable', 'believable', 'believability']) == ['b', 'b', 'e', 'e', 'l', 'l', 'i', 'v', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylophones', 'xylophonist']) == ['x', 'y', 'l', 'o', 'o', 'p', 'h', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylophones', 'xylophonist']) == ['x', 'y', 'l', 'o', 'o', 'p', 'h', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'ambient', 'administrate']) == ['e', 'n', 'i', 'm', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'ambient', 'administrate']) == ['e', 'n', 'i', 'm', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'environments', 'environmental']) == ['e', 'e', 'n', 'n', 'n', 'v', 'i', 'r', 'o', 'm', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'environments', 'environmental']) == ['e', 'e', 'n', 'n', 'n', 'v', 'i', 'r', 'o', 'm', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'intersects', 'intercept']) == ['i', 'n', 't', 't', 'e', 'e', 'r', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'intersects', 'intercept']) == ['i', 'n', 't', 't', 'e', 'e', 'r', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'abrakadabras', 'abrakadabratic']) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'abrakadabras', 'abrakadabratic']) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'interact', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'interact', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fantastic', 'fantasy', 'fantasia']) == ['f', 'a', 'a', 'n', 't', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fantastic', 'fantasy', 'fantasia']) == ['f', 'a', 'a', 'n', 't', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'missouri', 'missile']) == ['m', 'i', 'i', 's', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'missouri', 'missile']) == ['m', 'i', 'i', 's', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['reducibility', 'reductiveness', 'reductive']) == ['r', 'e', 'd', 'u', 'c', 'i', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['reducibility', 'reductiveness', 'reductive']) == ['r', 'e', 'd', 'u', 'c', 'i', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['alphabet', 'alphabetic', 'alphanumeric']) == ['a', 'a', 'l', 'p', 'h', 'e']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['alphabet', 'alphabetic', 'alphanumeric']) == ['a', 'a', 'l', 'p', 'h', 'e']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'petition', 'representation']) == ['e', 'p', 't', 't', 'i', 'o', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'petition', 'representation']) == ['e', 'p', 't', 't', 'i', 'o', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['congratulations', 'congratulate', 'congratulatory']) == ['c', 'o', 'n', 'g', 'r', 'a', 'a', 't', 't', 'u', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['congratulations', 'congratulate', 'congratulatory']) == ['c', 'o', 'n', 'g', 'r', 'a', 'a', 't', 't', 'u', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzz']) == ['z', 'z', 'z', 'z', 'z', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzz']) == ['z', 'z', 'z', 'z', 'z', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro']) == ['p', 'r', 'o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro']) == ['p', 'r', 'o']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'environmental', 'environments']) == ['e', 'e', 'n', 'n', 'n', 'v', 'i', 'r', 'o', 'm', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'environmental', 'environments']) == ['e', 'e', 'n', 'n', 'n', 'v', 'i', 'r', 'o', 'm', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abbreviation', 'abbreviate', 'abbreviations']) == ['a', 'a', 'b', 'b', 'r', 'e', 'v', 'i', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abbreviation', 'abbreviate', 'abbreviations']) == ['a', 'a', 'b', 'b', 'r', 'e', 'v', 'i', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'interior', 'interesting']) == ['i', 'i', 'n', 't', 'e', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'interior', 'interesting']) == ['i', 'i', 'n', 't', 'e', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghij', 'jihgfedcba', 'fedcba', 'abcdefghij']) == ['a', 'b', 'c', 'd', 'e', 'f']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghij', 'jihgfedcba', 'fedcba', 'abcdefghij']) == ['a', 'b', 'c', 'd', 'e', 'f']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'supercalifragilisticexpialidos']) == ['s', 's', 'u', 'p', 'e', 'r', 'r', 'c', 'c', 'a', 'a', 'l', 'l', 'i', 'i', 'i', 'i', 'f', 'g', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'supercalifragilisticexpialidos']) == ['s', 's', 'u', 'p', 'e', 'r', 'r', 'c', 'c', 'a', 'a', 'l', 'l', 'i', 'i', 'i', 'i', 'f', 'g', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['development', 'delivery', 'department']) == ['d', 'e', 'e']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['development', 'delivery', 'department']) == ['d', 'e', 'e']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'missionary', 'pessimism']) == ['m', 'i', 'i', 's', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'missionary', 'pessimism']) == ['m', 'i', 'i', 's', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gramming', 'paring']) == ['r', 'g', 'a', 'i', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gramming', 'paring']) == ['r', 'g', 'a', 'i', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == ['z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == ['z']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'programmer', 'program']) == ['p', 'r', 'r', 'o', 'g', 'a', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'programmer', 'program']) == ['p', 'r', 'r', 'o', 'g', 'a', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylography', 'xylophonist']) == ['x', 'y', 'l', 'o', 'p', 'h']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylography', 'xylophonist']) == ['x', 'y', 'l', 'o', 'p', 'h']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['characterization', 'characterization', 'characterize']) == ['c', 'c', 'h', 'a', 'a', 'r', 'r', 't', 'e', 'i', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['characterization', 'characterization', 'characterize']) == ['c', 'c', 'h', 'a', 'a', 'r', 'r', 't', 'e', 'i', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['orchestration', 'orchestrated', 'orchestrator']) == ['o', 'r', 'r', 'c', 'h', 'e', 's', 't', 't', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['orchestration', 'orchestrated', 'orchestrator']) == ['o', 'r', 'r', 'c', 'h', 'e', 's', 't', 't', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['characterization', 'character', 'characterization']) == ['c', 'c', 'h', 'a', 'a', 'r', 'r', 't', 'e']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['characterization', 'character', 'characterization']) == ['c', 'c', 'h', 'a', 'a', 'r', 'r', 't', 'e']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersectionality', 'interact', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'r', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersectionality', 'interact', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'r', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'academia', 'barbara']) == ['a', 'a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'academia', 'barbara']) == ['a', 'a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbc', 'abbcc', 'aaccb', 'abcabc']) == ['a', 'b', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbc', 'abbcc', 'aaccb', 'abcabc']) == ['a', 'b', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'bacana', 'cabana']) == ['a', 'a', 'a', 'b', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'bacana', 'cabana']) == ['a', 'a', 'a', 'b', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'interact', 'interactive']) == ['i', 'n', 't', 't', 'e', 'r', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'interact', 'interactive']) == ['i', 'n', 't', 't', 'e', 'r', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'programmer', 'programmatic']) == ['p', 'r', 'r', 'o', 'g', 'a', 'm', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'programmer', 'programmatic']) == ['p', 'r', 'r', 'o', 'g', 'a', 'm', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['exemplification', 'exemplary', 'exemplify']) == ['e', 'e', 'x', 'm', 'p', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['exemplification', 'exemplary', 'exemplify']) == ['e', 'e', 'x', 'm', 'p', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['congratulations', 'congratulate', 'congratulations']) == ['c', 'o', 'n', 'g', 'r', 'a', 'a', 't', 't', 'u', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['congratulations', 'congratulate', 'congratulations']) == ['c', 'o', 'n', 'g', 'r', 'a', 'a', 't', 't', 'u', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'alakazam', 'alchemy']) == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'alakazam', 'alchemy']) == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'missouri', 'missed']) == ['m', 'i', 's', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'missouri', 'missed']) == ['m', 'i', 's', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a']) == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a']) == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylophones', 'xylophonist', 'xylophonists']) == ['x', 'y', 'l', 'o', 'o', 'p', 'h', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylophones', 'xylophonist', 'xylophonists']) == ['x', 'y', 'l', 'o', 'o', 'p', 'h', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'misstep', 'misspell']) == ['m', 'i', 's', 's', 'p']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'misstep', 'misspell']) == ['m', 'i', 's', 's', 'p']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['bookkeeper', 'bookstore', 'keeper']) == ['k', 'e', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['bookkeeper', 'bookstore', 'keeper']) == ['k', 'e', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['multifaceted', 'multifarious', 'multitude']) == ['m', 'u', 'l', 't', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['multifaceted', 'multifarious', 'multitude']) == ['m', 'u', 'l', 't', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['multiple', 'multiplication', 'multiplicity']) == ['m', 'u', 'l', 'l', 't', 'i', 'p']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['multiple', 'multiplication', 'multiplicity']) == ['m', 'u', 'l', 'l', 't', 'i', 'p']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbccddeeff', 'bbaacceeddff', 'ccaabbeeffdd', 'aabbeeffccdd', 'aabbccdde', 'bbccddeeff', 'aaccbbeeff']) == ['b', 'b', 'c', 'c', 'e']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbccddeeff', 'bbaacceeddff', 'ccaabbeeffdd', 'aabbeeffccdd', 'aabbccdde', 'bbccddeeff', 'aaccbbeeff']) == ['b', 'b', 'c', 'c', 'e']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xenon', 'xerox', 'xylography']) == ['x', 'o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xenon', 'xerox', 'xylography']) == ['x', 'o']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'repetitions', 'repetitive']) == ['r', 'e', 'e', 'p', 't', 't', 'i', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'repetitions', 'repetitive']) == ['r', 'e', 'e', 'p', 't', 't', 'i', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'missouri', 'missisipi']) == ['m', 'i', 'i', 's', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'missouri', 'missisipi']) == ['m', 'i', 'i', 's', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['beautiful', 'beautify', 'beautification']) == ['b', 'e', 'a', 'u', 't', 'i', 'f']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['beautiful', 'beautify', 'beautification']) == ['b', 'e', 'a', 'u', 't', 'i', 'f']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'alignment']) == ['a', 'l', 'g']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'alignment']) == ['a', 'l', 'g']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'interact', 'interaction']) == ['i', 'n', 't', 't', 'e', 'r', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'interact', 'interaction']) == ['i', 'n', 't', 't', 'e', 'r', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['exceedingly', 'excellent', 'exceptional']) == ['e', 'e', 'x', 'c', 'n', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['exceedingly', 'excellent', 'exceptional']) == ['e', 'e', 'x', 'c', 'n', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'cadabra', 'abraca']) == ['a', 'a', 'a', 'b', 'r', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'cadabra', 'abraca']) == ['a', 'a', 'a', 'b', 'r', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'logarithm', 'rhythm']) == ['r', 't', 'h', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'logarithm', 'rhythm']) == ['r', 't', 'h', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['quizzing', 'quizzes', 'quizzed']) == ['q', 'u', 'i', 'z', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quizzing', 'quizzes', 'quizzed']) == ['q', 'u', 'i', 'z', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['sophisticated', 'sophistication', 'sophistry']) == ['s', 's', 'o', 'p', 'h', 'i', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['sophisticated', 'sophistication', 'sophistry']) == ['s', 's', 'o', 'p', 'h', 'i', 't']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['strength', 'strengths', 'stressed']) == ['s', 't', 'r', 'e']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['strength', 'strengths', 'stressed']) == ['s', 't', 'r', 'e']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['encyclopedia', 'encyclopediae', 'encyclopedias']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['encyclopedia', 'encyclopediae', 'encyclopedias']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'petition', 'competition']) == ['e', 'p', 't', 't', 'i', 'i', 'o', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'petition', 'competition']) == ['e', 'p', 't', 't', 'i', 'i', 'o', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unbelievable', 'unbeliever', 'unbelievably']) == ['u', 'n', 'b', 'e', 'e', 'l', 'i', 'v']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unbelievable', 'unbeliever', 'unbelievably']) == ['u', 'n', 'b', 'e', 'e', 'l', 'i', 'v']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interpolation', 'interpretation', 'internationalization']) == ['i', 'i', 'n', 'n', 't', 't', 'e', 'r', 'o', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interpolation', 'interpretation', 'internationalization']) == ['i', 'i', 'n', 'n', 't', 't', 'e', 'r', 'o', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'intercept', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'e', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'intercept', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'e', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcde', 'cdef', 'defg']) == ['d']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcde', 'cdef', 'defg']) == ['d']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pterodactyl', 'pterodactyl', 'pterodactyls']) == ['p', 't', 't', 'e', 'r', 'o', 'd', 'a', 'c', 'y', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pterodactyl', 'pterodactyl', 'pterodactyls']) == ['p', 't', 't', 'e', 'r', 'o', 'd', 'a', 'c', 'y', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'missouri', 'missed', 'missives']) == ['m', 'i', 's', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'missouri', 'missed', 'missives']) == ['m', 'i', 's', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'replicate', 'repetitive']) == ['r', 'e', 'e', 'p', 't', 'i']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'replicate', 'repetitive']) == ['r', 'e', 'e', 'p', 't', 'i']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algorithmic', 'algorithms']) == ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algorithmic', 'algorithms']) == ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['encyclopedia', 'encyclopedia', 'encyclopedia']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['encyclopedia', 'encyclopedia', 'encyclopedia']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'bandana', 'bananas']) == ['b', 'a', 'a', 'a', 'n', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'bandana', 'bananas']) == ['b', 'a', 'a', 'a', 'n', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'perpetuation', 'petition']) == ['e', 'p', 't', 't', 'i', 'o', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'perpetuation', 'petition']) == ['e', 'p', 't', 't', 'i', 'o', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'logarithm', 'anthology']) == ['a', 'l', 'g', 'o', 't', 'h']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'logarithm', 'anthology']) == ['a', 'l', 'g', 'o', 't', 'h']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'interview', 'interstellar']) == ['i', 'n', 't', 'e', 'e', 'r']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'interview', 'interstellar']) == ['i', 'n', 't', 'e', 'e', 'r']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'missouri', 'dismiss']) == ['m', 'i', 'i', 's', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'missouri', 'dismiss']) == ['m', 'i', 'i', 's', 's']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['abc', 'abc', 'abc']) == ['a', 'b', 'c']
    assert candidate(words = ['bella', 'label', 'roller']) == ['e', 'l', 'l']
    assert candidate(words = ['python', 'java', 'javascript']) == []
    assert candidate(words = ['hello', 'world', 'hold']) == ['l', 'o']
    assert candidate(words = ['aabbcc', 'aabbc', 'abc']) == ['a', 'b', 'c']
    assert candidate(words = ['cool', 'lock', 'cook']) == ['c', 'o']
    assert candidate(words = ['a', 'a', 'a', 'a']) == ['a']
    assert candidate(words = ['apple', 'apricot', 'peach']) == ['a', 'p']
    assert candidate(words = ['happy', 'happy', 'happy']) == ['h', 'a', 'p', 'p', 'y']
    assert candidate(words = ['a', 'a', 'a']) == ['a']
    assert candidate(words = ['flower', 'flow', 'flight']) == ['f', 'l']
    assert candidate(words = ['a', 'b', 'c']) == []
    assert candidate(words = ['common', 'commons', 'commonground']) == ['c', 'o', 'o', 'm', 'm', 'n']
    assert candidate(words = ['sophistication', 'sophisticated', 'sophisticating']) == ['s', 's', 'o', 'p', 'h', 'i', 'i', 't', 't', 'c', 'a']
    assert candidate(words = ['encyclopedia', 'encyclopedia', 'encyclopedic']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i']
    assert candidate(words = ['abracadabra', 'abrakadabrac', 'abrakadabracd']) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
    assert candidate(words = ['multifaceted', 'multimodal', 'multiplicity']) == ['m', 'u', 'l', 't', 'i']
    assert candidate(words = ['encyclopedia', 'encyclopedic', 'encyclopediae']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i']
    assert candidate(words = ['repetition', 'perception', 'competition']) == ['e', 'p', 't', 'i', 'o', 'n']
    assert candidate(words = ['algorithm', 'logarithm', 'rhythm', 'harmony']) == ['r', 'h', 'm']
    assert candidate(words = ['xylophone', 'zoo', 'ozone']) == ['o', 'o']
    assert candidate(words = ['banana', 'bandana', 'panama']) == ['a', 'a', 'a', 'n']
    assert candidate(words = ['algorithm', 'logarithm', 'altruism']) == ['a', 'l', 'r', 'i', 't', 'm']
    assert candidate(words = ['floccinaucinihilipilification', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'supercalifragilisticexpialidocious']) == ['l', 'l', 'l', 'o', 'o', 'c', 'c', 'c', 'i', 'i', 'i', 'i', 'i', 'i', 'a', 'a', 'u', 'p', 't']
    assert candidate(words = ['environment', 'venture', 'ambient']) == ['e', 'n', 't']
    assert candidate(words = ['algorithm', 'algorithms', 'algebra']) == ['a', 'l', 'g', 'r']
    assert candidate(words = ['repetition', 'replication', 'repetitive']) == ['r', 'e', 'p', 't', 'i', 'i']
    assert candidate(words = ['characterization', 'character', 'charisma']) == ['c', 'h', 'a', 'a', 'r']
    assert candidate(words = ['repetition', 'petition', 'portion']) == ['p', 't', 'i', 'o', 'n']
    assert candidate(words = ['unbelievable', 'believable', 'believability']) == ['b', 'b', 'e', 'e', 'l', 'l', 'i', 'v', 'a']
    assert candidate(words = ['xylophone', 'xylophones', 'xylophonist']) == ['x', 'y', 'l', 'o', 'o', 'p', 'h', 'n']
    assert candidate(words = ['environment', 'ambient', 'administrate']) == ['e', 'n', 'i', 'm', 't']
    assert candidate(words = ['environment', 'environments', 'environmental']) == ['e', 'e', 'n', 'n', 'n', 'v', 'i', 'r', 'o', 'm', 't']
    assert candidate(words = ['intersection', 'intersects', 'intercept']) == ['i', 'n', 't', 't', 'e', 'e', 'r', 'c']
    assert candidate(words = ['abracadabra', 'abrakadabras', 'abrakadabratic']) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'd']
    assert candidate(words = ['intersection', 'interact', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'r']
    assert candidate(words = ['fantastic', 'fantasy', 'fantasia']) == ['f', 'a', 'a', 'n', 't', 's']
    assert candidate(words = ['mississippi', 'missouri', 'missile']) == ['m', 'i', 'i', 's', 's']
    assert candidate(words = ['reducibility', 'reductiveness', 'reductive']) == ['r', 'e', 'd', 'u', 'c', 'i', 't']
    assert candidate(words = ['alphabet', 'alphabetic', 'alphanumeric']) == ['a', 'a', 'l', 'p', 'h', 'e']
    assert candidate(words = ['repetition', 'petition', 'representation']) == ['e', 'p', 't', 't', 'i', 'o', 'n']
    assert candidate(words = ['congratulations', 'congratulate', 'congratulatory']) == ['c', 'o', 'n', 'g', 'r', 'a', 'a', 't', 't', 'u', 'l']
    assert candidate(words = ['zzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzz']) == ['z', 'z', 'z', 'z', 'z', 'z']
    assert candidate(words = ['programming', 'program', 'pro']) == ['p', 'r', 'o']
    assert candidate(words = ['environment', 'environmental', 'environments']) == ['e', 'e', 'n', 'n', 'n', 'v', 'i', 'r', 'o', 'm', 't']
    assert candidate(words = ['abbreviation', 'abbreviate', 'abbreviations']) == ['a', 'a', 'b', 'b', 'r', 'e', 'v', 'i', 't']
    assert candidate(words = ['intersection', 'interior', 'interesting']) == ['i', 'i', 'n', 't', 'e', 'r']
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'fedcba', 'abcdefghij']) == ['a', 'b', 'c', 'd', 'e', 'f']
    assert candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'supercalifragilisticexpialidos']) == ['s', 's', 'u', 'p', 'e', 'r', 'r', 'c', 'c', 'a', 'a', 'l', 'l', 'i', 'i', 'i', 'i', 'f', 'g', 't']
    assert candidate(words = ['development', 'delivery', 'department']) == ['d', 'e', 'e']
    assert candidate(words = ['mississippi', 'missionary', 'pessimism']) == ['m', 'i', 'i', 's', 's']
    assert candidate(words = ['programming', 'gramming', 'paring']) == ['r', 'g', 'a', 'i', 'n']
    assert candidate(words = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == ['z']
    assert candidate(words = ['programming', 'programmer', 'program']) == ['p', 'r', 'r', 'o', 'g', 'a', 'm']
    assert candidate(words = ['xylophone', 'xylography', 'xylophonist']) == ['x', 'y', 'l', 'o', 'p', 'h']
    assert candidate(words = ['characterization', 'characterization', 'characterize']) == ['c', 'c', 'h', 'a', 'a', 'r', 'r', 't', 'e', 'i', 'z']
    assert candidate(words = ['orchestration', 'orchestrated', 'orchestrator']) == ['o', 'r', 'r', 'c', 'h', 'e', 's', 't', 't', 'a']
    assert candidate(words = ['characterization', 'character', 'characterization']) == ['c', 'c', 'h', 'a', 'a', 'r', 'r', 't', 'e']
    assert candidate(words = ['intersectionality', 'interact', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'r', 'a']
    assert candidate(words = ['abracadabra', 'academia', 'barbara']) == ['a', 'a', 'a']
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbc', 'abbcc', 'aaccb', 'abcabc']) == ['a', 'b', 'c']
    assert candidate(words = ['abacaxi', 'bacana', 'cabana']) == ['a', 'a', 'a', 'b', 'c']
    assert candidate(words = ['intersection', 'interact', 'interactive']) == ['i', 'n', 't', 't', 'e', 'r', 'c']
    assert candidate(words = ['programming', 'programmer', 'programmatic']) == ['p', 'r', 'r', 'o', 'g', 'a', 'm', 'm']
    assert candidate(words = ['exemplification', 'exemplary', 'exemplify']) == ['e', 'e', 'x', 'm', 'p', 'l']
    assert candidate(words = ['congratulations', 'congratulate', 'congratulations']) == ['c', 'o', 'n', 'g', 'r', 'a', 'a', 't', 't', 'u', 'l']
    assert candidate(words = ['abracadabra', 'alakazam', 'alchemy']) == ['a']
    assert candidate(words = ['mississippi', 'missouri', 'missed']) == ['m', 'i', 's', 's']
    assert candidate(words = ['aaa', 'aa', 'a']) == ['a']
    assert candidate(words = ['xylophone', 'xylophones', 'xylophonist', 'xylophonists']) == ['x', 'y', 'l', 'o', 'o', 'p', 'h', 'n']
    assert candidate(words = ['mississippi', 'misstep', 'misspell']) == ['m', 'i', 's', 's', 'p']
    assert candidate(words = ['bookkeeper', 'bookstore', 'keeper']) == ['k', 'e', 'r']
    assert candidate(words = ['multifaceted', 'multifarious', 'multitude']) == ['m', 'u', 'l', 't', 'i']
    assert candidate(words = ['multiple', 'multiplication', 'multiplicity']) == ['m', 'u', 'l', 'l', 't', 'i', 'p']
    assert candidate(words = ['aabbccddeeff', 'bbaacceeddff', 'ccaabbeeffdd', 'aabbeeffccdd', 'aabbccdde', 'bbccddeeff', 'aaccbbeeff']) == ['b', 'b', 'c', 'c', 'e']
    assert candidate(words = ['xylophone', 'xenon', 'xerox', 'xylography']) == ['x', 'o']
    assert candidate(words = ['repetition', 'repetitions', 'repetitive']) == ['r', 'e', 'e', 'p', 't', 't', 'i', 'i']
    assert candidate(words = ['mississippi', 'missouri', 'missisipi']) == ['m', 'i', 'i', 's', 's']
    assert candidate(words = ['beautiful', 'beautify', 'beautification']) == ['b', 'e', 'a', 'u', 't', 'i', 'f']
    assert candidate(words = ['algorithm', 'algebra', 'alignment']) == ['a', 'l', 'g']
    assert candidate(words = ['intersection', 'interact', 'interaction']) == ['i', 'n', 't', 't', 'e', 'r', 'c']
    assert candidate(words = ['exceedingly', 'excellent', 'exceptional']) == ['e', 'e', 'x', 'c', 'n', 'l']
    assert candidate(words = ['abracadabra', 'cadabra', 'abraca']) == ['a', 'a', 'a', 'b', 'r', 'c']
    assert candidate(words = ['algorithm', 'logarithm', 'rhythm']) == ['r', 't', 'h', 'm']
    assert candidate(words = ['quizzing', 'quizzes', 'quizzed']) == ['q', 'u', 'i', 'z', 'z']
    assert candidate(words = ['sophisticated', 'sophistication', 'sophistry']) == ['s', 's', 'o', 'p', 'h', 'i', 't']
    assert candidate(words = ['strength', 'strengths', 'stressed']) == ['s', 't', 'r', 'e']
    assert candidate(words = ['encyclopedia', 'encyclopediae', 'encyclopedias']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i', 'a']
    assert candidate(words = ['repetition', 'petition', 'competition']) == ['e', 'p', 't', 't', 'i', 'i', 'o', 'n']
    assert candidate(words = ['unbelievable', 'unbeliever', 'unbelievably']) == ['u', 'n', 'b', 'e', 'e', 'l', 'i', 'v']
    assert candidate(words = ['interpolation', 'interpretation', 'internationalization']) == ['i', 'i', 'n', 'n', 't', 't', 'e', 'r', 'o', 'a']
    assert candidate(words = ['intersection', 'intercept', 'interstellar']) == ['i', 'n', 't', 't', 'e', 'e', 'r']
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg']) == ['d']
    assert candidate(words = ['pterodactyl', 'pterodactyl', 'pterodactyls']) == ['p', 't', 't', 'e', 'r', 'o', 'd', 'a', 'c', 'y', 'l']
    assert candidate(words = ['mississippi', 'missouri', 'missed', 'missives']) == ['m', 'i', 's', 's']
    assert candidate(words = ['repetition', 'replicate', 'repetitive']) == ['r', 'e', 'e', 'p', 't', 'i']
    assert candidate(words = ['algorithm', 'algorithmic', 'algorithms']) == ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']
    assert candidate(words = ['encyclopedia', 'encyclopedia', 'encyclopedia']) == ['e', 'e', 'n', 'c', 'c', 'y', 'l', 'o', 'p', 'd', 'i', 'a']
    assert candidate(words = ['banana', 'bandana', 'bananas']) == ['b', 'a', 'a', 'a', 'n', 'n']
    assert candidate(words = ['repetition', 'perpetuation', 'petition']) == ['e', 'p', 't', 't', 'i', 'o', 'n']
    assert candidate(words = ['algorithm', 'logarithm', 'anthology']) == ['a', 'l', 'g', 'o', 't', 'h']
    assert candidate(words = ['intersection', 'interview', 'interstellar']) == ['i', 'n', 't', 'e', 'e', 'r']
    assert candidate(words = ['mississippi', 'missouri', 'dismiss']) == ['m', 'i', 'i', 's', 's']


