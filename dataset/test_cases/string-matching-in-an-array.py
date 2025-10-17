def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['leetcode', 'et', 'code']) == ['et', 'code']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['leetcode', 'et', 'code']) == ['et', 'code']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['blue', 'green', 'bu']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['blue', 'green', 'bu']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mass', 'as', 'hero', 'superhero']) == ['as', 'hero']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mass', 'as', 'hero', 'superhero']) == ['as', 'hero']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['nested', 'nest', 'sted', 'stednested', 'nestedsted', 'st']) == ['nested', 'nest', 'sted', 'st']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['nested', 'nest', 'sted', 'stednested', 'nestedsted', 'st']) == ['nested', 'nest', 'sted', 'st']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['computer', 'com', 'puter', 'put', 'ter', 'er', 'r', 'software', 'soft', 'ware', 'awe', 'awe', 're']) == ['com', 'puter', 'put', 'ter', 'er', 'r', 'soft', 'ware', 'awe', 'awe', 're']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['computer', 'com', 'puter', 'put', 'ter', 'er', 'r', 'software', 'soft', 'ware', 'awe', 'awe', 're']) == ['com', 'puter', 'put', 'ter', 'er', 'r', 'soft', 'ware', 'awe', 'awe', 're']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'pineapple', 'banana', 'app', 'pine']) == ['apple', 'app', 'pine']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'pineapple', 'banana', 'app', 'pine']) == ['apple', 'app', 'pine']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'pineapple', 'pie', 'pine']) == ['apple', 'app', 'pine']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'pineapple', 'pie', 'pine']) == ['apple', 'app', 'pine']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hello world', 'world hello', 'owor', 'dlrow', 'lohel']) == ['hello', 'world']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hello world', 'world hello', 'owor', 'dlrow', 'lohel']) == ['hello', 'world']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'once', 'only', 'no', 'on', 'o', 'onceuponatime', 'time', 'upon']) == ['once', 'on', 'o', 'time', 'upon']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'once', 'only', 'no', 'on', 'o', 'onceuponatime', 'time', 'upon']) == ['once', 'on', 'o', 'time', 'upon']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interview', 'view', 'terview', 'enter', 'viewer', 'inter']) == ['view', 'terview', 'inter']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interview', 'view', 'terview', 'enter', 'viewer', 'inter']) == ['view', 'terview', 'inter']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'ello', 'lo', 'll', 'he', 'oh', 'el', 'le', 'hellos', 'los']) == ['hello', 'hell', 'ello', 'lo', 'll', 'he', 'el', 'los']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'ello', 'lo', 'll', 'he', 'oh', 'el', 'le', 'hellos', 'los']) == ['hello', 'hell', 'ello', 'lo', 'll', 'he', 'el', 'los']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['adventure', 'venture', 'adven', 'advenu', 'tu', 'tre', 'ven', 'ure', 'enture', 'venu']) == ['venture', 'adven', 'tu', 'ven', 'ure', 'enture', 'venu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['adventure', 'venture', 'adven', 'advenu', 'tu', 'tre', 'ven', 'ure', 'enture', 'venu']) == ['venture', 'adven', 'tu', 'ven', 'ure', 'enture', 'venu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'def', 'ghij', 'jkl', 'ghijkl', 'defgh']) == ['def', 'ghij', 'jkl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'def', 'ghij', 'jkl', 'ghijkl', 'defgh']) == ['def', 'ghij', 'jkl']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hello_world', 'helloworld']) == ['hello', 'world']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hello_world', 'helloworld']) == ['hello', 'world']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'rhythm', 'thm', 'hythm', 'ythm', 'thm', 'hm', 'm', 'rythm']) == ['algo', 'thm', 'hythm', 'ythm', 'thm', 'hm', 'm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'rhythm', 'thm', 'hythm', 'ythm', 'thm', 'hm', 'm', 'rythm']) == ['algo', 'thm', 'hythm', 'ythm', 'thm', 'hm', 'm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bca', 'cab', 'abcd', 'bcda', 'cdab', 'dabc']) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bca', 'cab', 'abcd', 'bcda', 'cdab', 'dabc']) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['amazing', 'zing', 'zinga', 'zingalingo']) == ['zing', 'zinga']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['amazing', 'zing', 'zinga', 'zingalingo']) == ['zing', 'zinga']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'zyx', 'xyzz', 'zzxy', 'yxz', 'zyxz', 'xyzzyx']) == ['xyz', 'zyx', 'xyzz', 'yxz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'zyx', 'xyzz', 'zzxy', 'yxz', 'zyxz', 'xyzzyx']) == ['xyz', 'zyx', 'xyzz', 'yxz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithms', 'algo', 'rithm', 'log', 'thm', 'gms']) == ['algo', 'rithm', 'thm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithms', 'algo', 'rithm', 'log', 'thm', 'gms']) == ['algo', 'rithm', 'thm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['extraterrestrial', 'extra', 'terrestrial', 'restrial', 'estrial', 'trial', 'rial', 'ial', 'al', 'l']) == ['extra', 'terrestrial', 'restrial', 'estrial', 'trial', 'rial', 'ial', 'al', 'l']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['extraterrestrial', 'extra', 'terrestrial', 'restrial', 'estrial', 'trial', 'rial', 'ial', 'al', 'l']) == ['extra', 'terrestrial', 'restrial', 'estrial', 'trial', 'rial', 'ial', 'al', 'l']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'super', 'sub', 'superstring', 'string', 'ingsub']) == ['super', 'sub', 'string']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'super', 'sub', 'superstring', 'string', 'ingsub']) == ['super', 'sub', 'string']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'unicorn', 'unicore', 'uniques', 'unicorns', 'unicornicorns']) == ['unique', 'unicorn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'unicorn', 'unicore', 'uniques', 'unicorns', 'unicornicorns']) == ['unique', 'unicorn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gram', 'gramming', 'pro', 'ming']) == ['gram', 'gramming', 'pro', 'ming']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gram', 'gramming', 'pro', 'ming']) == ['gram', 'gramming', 'pro', 'ming']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'java', 'c', 'c++', 'javascript', 'typescript', 'script', 'type', 'java', 'script', 'scripting']) == ['java', 'c', 'script', 'type', 'java', 'script']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'java', 'c', 'c++', 'javascript', 'typescript', 'script', 'type', 'java', 'script', 'scripting']) == ['java', 'c', 'script', 'type', 'java', 'script']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'onetwo', 'twothree', 'onetwothree', 'threeonetwo']) == ['one', 'two', 'three', 'onetwo', 'twothree']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'onetwo', 'twothree', 'onetwothree', 'threeonetwo']) == ['one', 'two', 'three', 'onetwo', 'twothree']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'abcd', 'ab', 'cde', 'def', 'abcdefg']) == ['abc', 'bcd', 'abcd', 'ab', 'cde', 'def']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'abcd', 'ab', 'cde', 'def', 'abcdefg']) == ['abc', 'bcd', 'abcd', 'ab', 'cde', 'def']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcde', 'abcdef', 'def', 'cde', 'bcde']) == ['abcd', 'abcde', 'def', 'cde', 'bcde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcde', 'abcdef', 'def', 'cde', 'bcde']) == ['abcd', 'abcde', 'def', 'cde', 'bcde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'string', 'sub', 'str', 'st', 's']) == ['string', 'sub', 'str', 'st', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'string', 'sub', 'str', 'st', 's']) == ['string', 'sub', 'str', 'st', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'abcdef', 'ghijkl', 'mnop', 'mnopqr', 'abcde']) == ['abc', 'def', 'mnop', 'abcde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'abcdef', 'ghijkl', 'mnop', 'mnopqr', 'abcde']) == ['abc', 'def', 'mnop', 'abcde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'java', 'javascript', 'pythonic', 'code', 'script']) == ['python', 'java', 'script']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'java', 'javascript', 'pythonic', 'code', 'script']) == ['python', 'java', 'script']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['microcosm', 'micro', 'cosm', 'co', 'sm', 'microscopic', 'scop', 'scope', 'opic', 'pic']) == ['micro', 'cosm', 'co', 'sm', 'scop', 'opic', 'pic']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['microcosm', 'micro', 'cosm', 'co', 'sm', 'microscopic', 'scop', 'scope', 'opic', 'pic']) == ['micro', 'cosm', 'co', 'sm', 'scop', 'opic', 'pic']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['elephant', 'elephantium', 'phant', 'phantom', 'ele', 'fantastic']) == ['elephant', 'phant', 'ele']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['elephant', 'elephantium', 'phant', 'phantom', 'ele', 'fantastic']) == ['elephant', 'phant', 'ele']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['incomprehensible', 'in', 'comprehensible', 'prehensible', 'prehens', 'hensible', 'ensible', 'sible', 'ible', 'ble']) == ['in', 'comprehensible', 'prehensible', 'prehens', 'hensible', 'ensible', 'sible', 'ible', 'ble']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['incomprehensible', 'in', 'comprehensible', 'prehensible', 'prehens', 'hensible', 'ensible', 'sible', 'ible', 'ble']) == ['in', 'comprehensible', 'prehensible', 'prehens', 'hensible', 'ensible', 'sible', 'ible', 'ble']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'log', 'arithm', 'rhythm', 'mthm', 'them']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'log', 'arithm', 'rhythm', 'mthm', 'them']) == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'petition', 'iteration', 'repeat', 'pet', 'tion', 'peti', 'petit', 'petiti', 'petitio']) == ['petition', 'pet', 'tion', 'peti', 'petit', 'petiti', 'petitio']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'petition', 'iteration', 'repeat', 'pet', 'tion', 'peti', 'petit', 'petiti', 'petitio']) == ['petition', 'pet', 'tion', 'peti', 'petit', 'petiti', 'petitio']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'string', 'sub', 'substringing', 'ing']) == ['substring', 'string', 'sub', 'ing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'string', 'sub', 'substringing', 'ing']) == ['substring', 'string', 'sub', 'ing']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['quick', 'brown', 'fox', 'the', 'quickbrownfoxjumpsoverthelazydog']) == ['quick', 'brown', 'fox', 'the']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quick', 'brown', 'fox', 'the', 'quickbrownfoxjumpsoverthelazydog']) == ['quick', 'brown', 'fox', 'the']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'string', 'sub', 'ing', 'substr', 'str', 'ingstr', 'substrin']) == ['string', 'sub', 'ing', 'substr', 'str', 'substrin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'string', 'sub', 'ing', 'substr', 'str', 'ingstr', 'substrin']) == ['string', 'sub', 'ing', 'substr', 'str', 'substrin']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hel', 'lo', 'wor', 'rld', 'ldo']) == ['hel', 'lo', 'wor', 'rld']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hel', 'lo', 'wor', 'rld', 'ldo']) == ['hel', 'lo', 'wor', 'rld']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gram', 'ming', 'pro', 'gramming']) == ['gram', 'ming', 'pro', 'gramming']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gram', 'ming', 'pro', 'gramming']) == ['gram', 'ming', 'pro', 'gramming']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbaa', 'ccaa', 'aabb', 'bbcc', 'ccaabb', 'aabbccaa']) == ['aabbcc', 'ccaa', 'aabb', 'bbcc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbaa', 'ccaa', 'aabb', 'bbcc', 'ccaabb', 'aabbccaa']) == ['aabbcc', 'ccaa', 'aabb', 'bbcc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tiny', 'tinier', 'tinytinier', 'tinytiny', 'tinieriny']) == ['tiny', 'tinier']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tiny', 'tinier', 'tinytinier', 'tinytiny', 'tinieriny']) == ['tiny', 'tinier']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'le', 'banana', 'nan', 'batman', 'man', 'at']) == ['app', 'le', 'nan', 'man', 'at']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'le', 'banana', 'nan', 'batman', 'man', 'at']) == ['app', 'le', 'nan', 'man', 'at']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'aabb', 'abbc', 'bbcc', 'abcc', 'aabc', 'bccc', 'ccaa', 'aacc', 'bbca']) == ['aabb', 'abbc', 'bbcc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'aabb', 'abbc', 'bbcc', 'abcc', 'aabc', 'bccc', 'ccaa', 'aacc', 'bbca']) == ['aabb', 'abbc', 'bbcc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['random', 'rand', 'dom', 'ra', 'doma', 'mon', 'ndom', 'and', 'ran', 'domi']) == ['rand', 'dom', 'ra', 'ndom', 'and', 'ran']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['random', 'rand', 'dom', 'ra', 'doma', 'mon', 'ndom', 'and', 'ran', 'domi']) == ['rand', 'dom', 'ra', 'ndom', 'and', 'ran']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylo', 'phone', 'pho', 'ne', 'xy', 'lo', 'lopho', 'phone']) == ['xylo', 'phone', 'pho', 'ne', 'xy', 'lo', 'lopho', 'phone']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylo', 'phone', 'pho', 'ne', 'xy', 'lo', 'lopho', 'phone']) == ['xylo', 'phone', 'pho', 'ne', 'xy', 'lo', 'lopho', 'phone']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'logarithm', 'rhythm', 'algorithmic', 'logarithmic', 'rhythmic']) == ['algorithm', 'logarithm', 'rhythm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'logarithm', 'rhythm', 'algorithmic', 'logarithmic', 'rhythmic']) == ['algorithm', 'logarithm', 'rhythm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'cde', 'de', 'e']) == ['abc', 'ab', 'a', 'cde', 'de', 'e']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'cde', 'de', 'e']) == ['abc', 'ab', 'a', 'cde', 'de', 'e']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'string', 'sub', 'str', 'ing', 'sun', 'set', 'net', 'get', 'ten']) == ['string', 'sub', 'str', 'ing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'string', 'sub', 'str', 'ing', 'sun', 'set', 'net', 'get', 'ten']) == ['string', 'sub', 'str', 'ing']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['photography', 'photo', 'graphy', 'graph', 'graphy', 'photo', 'graphi', 'graphis', 'photo', 'photog']) == ['photo', 'graphy', 'graph', 'graphy', 'photo', 'graphi', 'photo', 'photog']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['photography', 'photo', 'graphy', 'graph', 'graphy', 'photo', 'graphi', 'graphis', 'photo', 'photog']) == ['photo', 'graphy', 'graph', 'graphy', 'photo', 'graphi', 'photo', 'photog']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['subsequence', 'sequence', 'sub', 'ence', 'quen']) == ['sequence', 'sub', 'ence', 'quen']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['subsequence', 'sequence', 'sub', 'ence', 'quen']) == ['sequence', 'sub', 'ence', 'quen']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == ['bcdef', 'cdefg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == ['bcdef', 'cdefg']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny', 'tinytinytinytinytiny']) == ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny', 'tinytinytinytinytiny']) == ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'substr', 'string', 'str', 'tri', 'ing', 'sub', 'subtr', 'ing', 'subtrin']) == ['substr', 'string', 'str', 'tri', 'ing', 'sub', 'subtr', 'ing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'substr', 'string', 'str', 'tri', 'ing', 'sub', 'subtr', 'ing', 'subtrin']) == ['substr', 'string', 'str', 'tri', 'ing', 'sub', 'subtr', 'ing']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['submarine', 'sub', 'marine', 'submar', 'in', 'a', 'mar', 'ne']) == ['sub', 'marine', 'submar', 'in', 'a', 'mar', 'ne']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['submarine', 'sub', 'marine', 'submar', 'in', 'a', 'mar', 'ne']) == ['sub', 'marine', 'submar', 'in', 'a', 'mar', 'ne']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'cde', 'de']) == ['abc', 'ab', 'a', 'cde', 'de']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'cde', 'de']) == ['abc', 'ab', 'a', 'cde', 'de']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f']) == ['abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f']) == ['abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gram', 'ming', 'pro', 'am', 'ing', 'gramming', 'program']) == ['gram', 'ming', 'pro', 'am', 'ing', 'gramming', 'program']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gram', 'ming', 'pro', 'am', 'ing', 'gramming', 'program']) == ['gram', 'ming', 'pro', 'am', 'ing', 'gramming', 'program']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'he', 'hell', 'lo', 'he', 'ello', 'hel', 'ell', 'llo', 'lo']) == ['he', 'hell', 'lo', 'he', 'ello', 'hel', 'ell', 'llo', 'lo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'he', 'hell', 'lo', 'he', 'ello', 'hel', 'ell', 'llo', 'lo']) == ['he', 'hell', 'lo', 'he', 'ello', 'hel', 'ell', 'llo', 'lo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'plea', 'ple', 'applepie']) == ['apple', 'ple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'plea', 'ple', 'applepie']) == ['apple', 'ple']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fantastic', 'fant', 'ast', 'astic', 'tic']) == ['fant', 'ast', 'astic', 'tic']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fantastic', 'fant', 'ast', 'astic', 'tic']) == ['fant', 'ast', 'astic', 'tic']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'cali', 'frag', 'listic', 'expiali', 'docious', 'super']) == ['cali', 'frag', 'listic', 'expiali', 'docious', 'super']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'cali', 'frag', 'listic', 'expiali', 'docious', 'super']) == ['cali', 'frag', 'listic', 'expiali', 'docious', 'super']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['subsequence', 'sequence', 'sub', 'seq', 'subseq', 'quen', 'ence', 'quence', 'suben', 'queseq']) == ['sequence', 'sub', 'seq', 'subseq', 'quen', 'ence', 'quence']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['subsequence', 'sequence', 'sub', 'seq', 'subseq', 'quen', 'ence', 'quence', 'suben', 'queseq']) == ['sequence', 'sub', 'seq', 'subseq', 'quen', 'ence', 'quence']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcd', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == ['ab', 'abc', 'abcd', 'abcde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcd', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == ['ab', 'abc', 'abcd', 'abcde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ana', 'nan', 'ban', 'an']) == ['ana', 'nan', 'ban', 'an']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ana', 'nan', 'ban', 'an']) == ['ana', 'nan', 'ban', 'an']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hello world', 'helloworld', 'lowor', 'wor']) == ['hello', 'world', 'lowor', 'wor']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hello world', 'helloworld', 'lowor', 'wor']) == ['hello', 'world', 'lowor', 'wor']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gram', 'ming', 'pro', 'gramming', 'program']) == ['gram', 'ming', 'pro', 'gramming', 'program']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gram', 'ming', 'pro', 'gramming', 'program']) == ['gram', 'ming', 'pro', 'gramming', 'program']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interdisciplinary', 'inter', 'disciplinary', 'disci', 'plinary', 'sci', 'sciency', 'interdisci', 'plin', 'sciencyplin']) == ['inter', 'disciplinary', 'disci', 'plinary', 'sci', 'sciency', 'interdisci', 'plin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interdisciplinary', 'inter', 'disciplinary', 'disci', 'plinary', 'sci', 'sciency', 'interdisci', 'plin', 'sciencyplin']) == ['inter', 'disciplinary', 'disci', 'plinary', 'sci', 'sciency', 'interdisci', 'plin']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'abcdefgh', 'efg', 'hij', 'ijk']) == ['abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'efg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'abcdefgh', 'efg', 'hij', 'ijk']) == ['abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'efg']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny']) == ['tiny', 'tinytiny', 'tinytinytiny']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny']) == ['tiny', 'tinytiny', 'tinytinytiny']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lapping', 'lap', 'lappping', 'lapppinglap']) == ['lap', 'lappping']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lapping', 'lap', 'lappping', 'lapppinglap']) == ['lap', 'lappping']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'ming', 'code', 'coding']) == ['program', 'ming']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'ming', 'code', 'coding']) == ['program', 'ming']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'rhythm', 'rhythmic', 'algothm', 'rhyth', 'thm']) == ['algo', 'rhythm', 'rhyth', 'thm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'rhythm', 'rhythmic', 'algothm', 'rhyth', 'thm']) == ['algo', 'rhythm', 'rhyth', 'thm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'string', 'sub', 'substrings', 'str']) == ['substring', 'string', 'sub', 'str']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'string', 'sub', 'substrings', 'str']) == ['substring', 'string', 'sub', 'str']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'bcde', 'cde', 'de', 'e', 'f']) == ['bcde', 'cde', 'de', 'e', 'f']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'bcde', 'cde', 'de', 'e', 'f']) == ['bcde', 'cde', 'de', 'e', 'f']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['nested', 'nest', 'nestedword', 'word', 'edword', 'st', 'sted']) == ['nested', 'nest', 'word', 'edword', 'st', 'sted']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['nested', 'nest', 'nestedword', 'word', 'edword', 'st', 'sted']) == ['nested', 'nest', 'word', 'edword', 'st', 'sted']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['photographically', 'photo', 'graphically', 'graphic', 'ically', 'ally', 'ly', 'y']) == ['photo', 'graphically', 'graphic', 'ically', 'ally', 'ly', 'y']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['photographically', 'photo', 'graphically', 'graphic', 'ically', 'ally', 'ly', 'y']) == ['photo', 'graphically', 'graphic', 'ically', 'ally', 'ly', 'y']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'phone', 'lophone', 'xylo', 'loph', 'pho', 'hon', 'xyl', 'one', 'phe']) == ['phone', 'lophone', 'xylo', 'loph', 'pho', 'hon', 'xyl', 'one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'phone', 'lophone', 'xylo', 'loph', 'pho', 'hon', 'xyl', 'one', 'phe']) == ['phone', 'lophone', 'xylo', 'loph', 'pho', 'hon', 'xyl', 'one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gram', 'ming', 'mingo', 'prog', 'ingram', 'program', 'gramming', 'programm', 'progr']) == ['gram', 'ming', 'prog', 'program', 'gramming', 'programm', 'progr']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gram', 'ming', 'mingo', 'prog', 'ingram', 'program', 'gramming', 'programm', 'progr']) == ['gram', 'ming', 'prog', 'program', 'gramming', 'programm', 'progr']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'abcdefg', 'gh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'gh']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'abcdefg', 'gh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'gh']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'log', 'rithm', 'algo', 'thm']) == ['rithm', 'algo', 'thm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'log', 'rithm', 'algo', 'thm']) == ['rithm', 'algo', 'thm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uni', 'ique', 'un', 'que', 'nique', 'niqe', 'neiq', 'uqei', 'inqeu']) == ['uni', 'ique', 'un', 'que', 'nique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uni', 'ique', 'un', 'que', 'nique', 'niqe', 'neiq', 'uqei', 'inqeu']) == ['uni', 'ique', 'un', 'que', 'nique']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gram', 'pro', 'ming', 'ring']) == ['gram', 'pro', 'ming']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gram', 'pro', 'ming', 'ring']) == ['gram', 'pro', 'ming']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['water', 'watermelon', 'melon', 'wa', 'ter', 'melonade', 'ade']) == ['water', 'melon', 'wa', 'ter', 'ade']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['water', 'watermelon', 'melon', 'wa', 'ter', 'melonade', 'ade']) == ['water', 'melon', 'wa', 'ter', 'ade']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'pineapple', 'grape', 'pinegrape', 'grapefruit', 'pineapplegrape']) == ['apple', 'pineapple', 'grape']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'pineapple', 'grape', 'pinegrape', 'grapefruit', 'pineapplegrape']) == ['apple', 'pineapple', 'grape']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'abcd', 'abcde', 'abcdef']) == ['abc', 'def', 'abcd', 'abcde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'abcd', 'abcde', 'abcdef']) == ['abc', 'def', 'abcd', 'abcde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'super', 'cali', 'fragi', 'listic', 'expiali', 'docious', 'fragilisticexpialidocious']) == ['super', 'cali', 'fragi', 'listic', 'expiali', 'docious', 'fragilisticexpialidocious']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'super', 'cali', 'fragi', 'listic', 'expiali', 'docious', 'fragilisticexpialidocious']) == ['super', 'cali', 'fragi', 'listic', 'expiali', 'docious', 'fragilisticexpialidocious']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unbelievable', 'un', 'believe', 'able', 'e', 'a', 'i', 'o', 'u']) == ['un', 'able', 'e', 'a', 'i', 'u']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unbelievable', 'un', 'believe', 'able', 'e', 'a', 'i', 'o', 'u']) == ['un', 'able', 'e', 'a', 'i', 'u']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['encyclopedia', 'encyclop', 'yclopedia', 'cloped', 'lopedia', 'pedia', 'dia', 'dialect', 'logic', 'encyclopediaic']) == ['encyclopedia', 'encyclop', 'yclopedia', 'cloped', 'lopedia', 'pedia', 'dia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['encyclopedia', 'encyclop', 'yclopedia', 'cloped', 'lopedia', 'pedia', 'dia', 'dialect', 'logic', 'encyclopediaic']) == ['encyclopedia', 'encyclop', 'yclopedia', 'cloped', 'lopedia', 'pedia', 'dia']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnop', 'qrstuvwxyz', 'mnopqrstu', 'vwxyz']) == ['abcdefghijklmnop', 'qrstuvwxyz', 'mnopqrstu', 'vwxyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnop', 'qrstuvwxyz', 'mnopqrstu', 'vwxyz']) == ['abcdefghijklmnop', 'qrstuvwxyz', 'mnopqrstu', 'vwxyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'fragilistic', 'expialidocious', 'docious', 'ious', 'ous', 'us', 's']) == ['fragilistic', 'expialidocious', 'docious', 'ious', 'ous', 'us', 's']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'fragilistic', 'expialidocious', 'docious', 'ious', 'ous', 'us', 's']) == ['fragilistic', 'expialidocious', 'docious', 'ious', 'ous', 'us', 's']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == ['a', 'ab', 'abc', 'abcd', 'abcde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == ['a', 'ab', 'abc', 'abcd', 'abcde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algo', 'rhythm', 'thm', 'rthm', 'hythmthm']) == ['algo', 'thm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algo', 'rhythm', 'thm', 'rthm', 'hythmthm']) == ['algo', 'thm']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['leetcode', 'et', 'code']) == ['et', 'code']
    assert candidate(words = ['blue', 'green', 'bu']) == []
    assert candidate(words = ['mass', 'as', 'hero', 'superhero']) == ['as', 'hero']
    assert candidate(words = ['nested', 'nest', 'sted', 'stednested', 'nestedsted', 'st']) == ['nested', 'nest', 'sted', 'st']
    assert candidate(words = ['computer', 'com', 'puter', 'put', 'ter', 'er', 'r', 'software', 'soft', 'ware', 'awe', 'awe', 're']) == ['com', 'puter', 'put', 'ter', 'er', 'r', 'soft', 'ware', 'awe', 'awe', 're']
    assert candidate(words = ['apple', 'pineapple', 'banana', 'app', 'pine']) == ['apple', 'app', 'pine']
    assert candidate(words = ['apple', 'app', 'pineapple', 'pie', 'pine']) == ['apple', 'app', 'pine']
    assert candidate(words = ['hello', 'world', 'hello world', 'world hello', 'owor', 'dlrow', 'lohel']) == ['hello', 'world']
    assert candidate(words = ['abcdefgh', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']
    assert candidate(words = ['one', 'once', 'only', 'no', 'on', 'o', 'onceuponatime', 'time', 'upon']) == ['once', 'on', 'o', 'time', 'upon']
    assert candidate(words = ['interview', 'view', 'terview', 'enter', 'viewer', 'inter']) == ['view', 'terview', 'inter']
    assert candidate(words = ['hello', 'hell', 'ello', 'lo', 'll', 'he', 'oh', 'el', 'le', 'hellos', 'los']) == ['hello', 'hell', 'ello', 'lo', 'll', 'he', 'el', 'los']
    assert candidate(words = ['adventure', 'venture', 'adven', 'advenu', 'tu', 'tre', 'ven', 'ure', 'enture', 'venu']) == ['venture', 'adven', 'tu', 'ven', 'ure', 'enture', 'venu']
    assert candidate(words = ['abcdef', 'def', 'ghij', 'jkl', 'ghijkl', 'defgh']) == ['def', 'ghij', 'jkl']
    assert candidate(words = ['hello', 'world', 'hello_world', 'helloworld']) == ['hello', 'world']
    assert candidate(words = ['algorithm', 'algo', 'rhythm', 'thm', 'hythm', 'ythm', 'thm', 'hm', 'm', 'rythm']) == ['algo', 'thm', 'hythm', 'ythm', 'thm', 'hm', 'm']
    assert candidate(words = ['abc', 'bca', 'cab', 'abcd', 'bcda', 'cdab', 'dabc']) == ['abc']
    assert candidate(words = ['amazing', 'zing', 'zinga', 'zingalingo']) == ['zing', 'zinga']
    assert candidate(words = ['xyz', 'zyx', 'xyzz', 'zzxy', 'yxz', 'zyxz', 'xyzzyx']) == ['xyz', 'zyx', 'xyzz', 'yxz']
    assert candidate(words = ['algorithms', 'algo', 'rithm', 'log', 'thm', 'gms']) == ['algo', 'rithm', 'thm']
    assert candidate(words = ['extraterrestrial', 'extra', 'terrestrial', 'restrial', 'estrial', 'trial', 'rial', 'ial', 'al', 'l']) == ['extra', 'terrestrial', 'restrial', 'estrial', 'trial', 'rial', 'ial', 'al', 'l']
    assert candidate(words = ['substring', 'super', 'sub', 'superstring', 'string', 'ingsub']) == ['super', 'sub', 'string']
    assert candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
    assert candidate(words = ['unique', 'unicorn', 'unicore', 'uniques', 'unicorns', 'unicornicorns']) == ['unique', 'unicorn']
    assert candidate(words = ['programming', 'gram', 'gramming', 'pro', 'ming']) == ['gram', 'gramming', 'pro', 'ming']
    assert candidate(words = ['python', 'java', 'c', 'c++', 'javascript', 'typescript', 'script', 'type', 'java', 'script', 'scripting']) == ['java', 'c', 'script', 'type', 'java', 'script']
    assert candidate(words = ['one', 'two', 'three', 'onetwo', 'twothree', 'onetwothree', 'threeonetwo']) == ['one', 'two', 'three', 'onetwo', 'twothree']
    assert candidate(words = ['abc', 'bcd', 'abcd', 'ab', 'cde', 'def', 'abcdefg']) == ['abc', 'bcd', 'abcd', 'ab', 'cde', 'def']
    assert candidate(words = ['abcd', 'abcde', 'abcdef', 'def', 'cde', 'bcde']) == ['abcd', 'abcde', 'def', 'cde', 'bcde']
    assert candidate(words = ['substring', 'string', 'sub', 'str', 'st', 's']) == ['string', 'sub', 'str', 'st', 's']
    assert candidate(words = ['abc', 'def', 'abcdef', 'ghijkl', 'mnop', 'mnopqr', 'abcde']) == ['abc', 'def', 'mnop', 'abcde']
    assert candidate(words = ['python', 'java', 'javascript', 'pythonic', 'code', 'script']) == ['python', 'java', 'script']
    assert candidate(words = ['microcosm', 'micro', 'cosm', 'co', 'sm', 'microscopic', 'scop', 'scope', 'opic', 'pic']) == ['micro', 'cosm', 'co', 'sm', 'scop', 'opic', 'pic']
    assert candidate(words = ['elephant', 'elephantium', 'phant', 'phantom', 'ele', 'fantastic']) == ['elephant', 'phant', 'ele']
    assert candidate(words = ['incomprehensible', 'in', 'comprehensible', 'prehensible', 'prehens', 'hensible', 'ensible', 'sible', 'ible', 'ble']) == ['in', 'comprehensible', 'prehensible', 'prehens', 'hensible', 'ensible', 'sible', 'ible', 'ble']
    assert candidate(words = ['algorithm', 'log', 'arithm', 'rhythm', 'mthm', 'them']) == []
    assert candidate(words = ['repetition', 'petition', 'iteration', 'repeat', 'pet', 'tion', 'peti', 'petit', 'petiti', 'petitio']) == ['petition', 'pet', 'tion', 'peti', 'petit', 'petiti', 'petitio']
    assert candidate(words = ['substring', 'string', 'sub', 'substringing', 'ing']) == ['substring', 'string', 'sub', 'ing']
    assert candidate(words = ['quick', 'brown', 'fox', 'the', 'quickbrownfoxjumpsoverthelazydog']) == ['quick', 'brown', 'fox', 'the']
    assert candidate(words = ['substring', 'string', 'sub', 'ing', 'substr', 'str', 'ingstr', 'substrin']) == ['string', 'sub', 'ing', 'substr', 'str', 'substrin']
    assert candidate(words = ['hello', 'world', 'hel', 'lo', 'wor', 'rld', 'ldo']) == ['hel', 'lo', 'wor', 'rld']
    assert candidate(words = ['programming', 'gram', 'ming', 'pro', 'gramming']) == ['gram', 'ming', 'pro', 'gramming']
    assert candidate(words = ['aabbcc', 'bbaa', 'ccaa', 'aabb', 'bbcc', 'ccaabb', 'aabbccaa']) == ['aabbcc', 'ccaa', 'aabb', 'bbcc']
    assert candidate(words = ['tiny', 'tinier', 'tinytinier', 'tinytiny', 'tinieriny']) == ['tiny', 'tinier']
    assert candidate(words = ['apple', 'app', 'le', 'banana', 'nan', 'batman', 'man', 'at']) == ['app', 'le', 'nan', 'man', 'at']
    assert candidate(words = ['aabbcc', 'aabb', 'abbc', 'bbcc', 'abcc', 'aabc', 'bccc', 'ccaa', 'aacc', 'bbca']) == ['aabb', 'abbc', 'bbcc']
    assert candidate(words = ['random', 'rand', 'dom', 'ra', 'doma', 'mon', 'ndom', 'and', 'ran', 'domi']) == ['rand', 'dom', 'ra', 'ndom', 'and', 'ran']
    assert candidate(words = ['xylophone', 'xylo', 'phone', 'pho', 'ne', 'xy', 'lo', 'lopho', 'phone']) == ['xylo', 'phone', 'pho', 'ne', 'xy', 'lo', 'lopho', 'phone']
    assert candidate(words = ['algorithm', 'logarithm', 'rhythm', 'algorithmic', 'logarithmic', 'rhythmic']) == ['algorithm', 'logarithm', 'rhythm']
    assert candidate(words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'cde', 'de', 'e']) == ['abc', 'ab', 'a', 'cde', 'de', 'e']
    assert candidate(words = ['substring', 'string', 'sub', 'str', 'ing', 'sun', 'set', 'net', 'get', 'ten']) == ['string', 'sub', 'str', 'ing']
    assert candidate(words = ['photography', 'photo', 'graphy', 'graph', 'graphy', 'photo', 'graphi', 'graphis', 'photo', 'photog']) == ['photo', 'graphy', 'graph', 'graphy', 'photo', 'graphi', 'photo', 'photog']
    assert candidate(words = ['subsequence', 'sequence', 'sub', 'ence', 'quen']) == ['sequence', 'sub', 'ence', 'quen']
    assert candidate(words = ['abcdefg', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == ['bcdef', 'cdefg']
    assert candidate(words = ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny', 'tinytinytinytinytiny']) == ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny']
    assert candidate(words = ['substring', 'substr', 'string', 'str', 'tri', 'ing', 'sub', 'subtr', 'ing', 'subtrin']) == ['substr', 'string', 'str', 'tri', 'ing', 'sub', 'subtr', 'ing']
    assert candidate(words = ['submarine', 'sub', 'marine', 'submar', 'in', 'a', 'mar', 'ne']) == ['sub', 'marine', 'submar', 'in', 'a', 'mar', 'ne']
    assert candidate(words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'cde', 'de']) == ['abc', 'ab', 'a', 'cde', 'de']
    assert candidate(words = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f']) == ['abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f']
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
    assert candidate(words = ['programming', 'gram', 'ming', 'pro', 'am', 'ing', 'gramming', 'program']) == ['gram', 'ming', 'pro', 'am', 'ing', 'gramming', 'program']
    assert candidate(words = ['hello', 'he', 'hell', 'lo', 'he', 'ello', 'hel', 'ell', 'llo', 'lo']) == ['he', 'hell', 'lo', 'he', 'ello', 'hel', 'ell', 'llo', 'lo']
    assert candidate(words = ['apple', 'plea', 'ple', 'applepie']) == ['apple', 'ple']
    assert candidate(words = ['fantastic', 'fant', 'ast', 'astic', 'tic']) == ['fant', 'ast', 'astic', 'tic']
    assert candidate(words = ['supercalifragilisticexpialidocious', 'cali', 'frag', 'listic', 'expiali', 'docious', 'super']) == ['cali', 'frag', 'listic', 'expiali', 'docious', 'super']
    assert candidate(words = ['subsequence', 'sequence', 'sub', 'seq', 'subseq', 'quen', 'ence', 'quence', 'suben', 'queseq']) == ['sequence', 'sub', 'seq', 'subseq', 'quen', 'ence', 'quence']
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
    assert candidate(words = ['abcdabcd', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == ['ab', 'abc', 'abcd', 'abcde']
    assert candidate(words = ['banana', 'ana', 'nan', 'ban', 'an']) == ['ana', 'nan', 'ban', 'an']
    assert candidate(words = ['hello', 'world', 'hello world', 'helloworld', 'lowor', 'wor']) == ['hello', 'world', 'lowor', 'wor']
    assert candidate(words = ['programming', 'gram', 'ming', 'pro', 'gramming', 'program']) == ['gram', 'ming', 'pro', 'gramming', 'program']
    assert candidate(words = ['interdisciplinary', 'inter', 'disciplinary', 'disci', 'plinary', 'sci', 'sciency', 'interdisci', 'plin', 'sciencyplin']) == ['inter', 'disciplinary', 'disci', 'plinary', 'sci', 'sciency', 'interdisci', 'plin']
    assert candidate(words = ['abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'abcdefgh', 'efg', 'hij', 'ijk']) == ['abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'efg']
    assert candidate(words = ['tiny', 'tinytiny', 'tinytinytiny', 'tinytinytinytiny']) == ['tiny', 'tinytiny', 'tinytinytiny']
    assert candidate(words = ['overlap', 'lapping', 'lap', 'lappping', 'lapppinglap']) == ['lap', 'lappping']
    assert candidate(words = ['programming', 'program', 'ming', 'code', 'coding']) == ['program', 'ming']
    assert candidate(words = ['algorithm', 'algo', 'rhythm', 'rhythmic', 'algothm', 'rhyth', 'thm']) == ['algo', 'rhythm', 'rhyth', 'thm']
    assert candidate(words = ['substring', 'string', 'sub', 'substrings', 'str']) == ['substring', 'string', 'sub', 'str']
    assert candidate(words = ['abcdef', 'bcde', 'cde', 'de', 'e', 'f']) == ['bcde', 'cde', 'de', 'e', 'f']
    assert candidate(words = ['nested', 'nest', 'nestedword', 'word', 'edword', 'st', 'sted']) == ['nested', 'nest', 'word', 'edword', 'st', 'sted']
    assert candidate(words = ['photographically', 'photo', 'graphically', 'graphic', 'ically', 'ally', 'ly', 'y']) == ['photo', 'graphically', 'graphic', 'ically', 'ally', 'ly', 'y']
    assert candidate(words = ['xylophone', 'phone', 'lophone', 'xylo', 'loph', 'pho', 'hon', 'xyl', 'one', 'phe']) == ['phone', 'lophone', 'xylo', 'loph', 'pho', 'hon', 'xyl', 'one']
    assert candidate(words = ['programming', 'gram', 'ming', 'mingo', 'prog', 'ingram', 'program', 'gramming', 'programm', 'progr']) == ['gram', 'ming', 'prog', 'program', 'gramming', 'programm', 'progr']
    assert candidate(words = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'abcdefg', 'gh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'gh']
    assert candidate(words = ['algorithm', 'log', 'rithm', 'algo', 'thm']) == ['rithm', 'algo', 'thm']
    assert candidate(words = ['unique', 'uni', 'ique', 'un', 'que', 'nique', 'niqe', 'neiq', 'uqei', 'inqeu']) == ['uni', 'ique', 'un', 'que', 'nique']
    assert candidate(words = ['programming', 'gram', 'pro', 'ming', 'ring']) == ['gram', 'pro', 'ming']
    assert candidate(words = ['water', 'watermelon', 'melon', 'wa', 'ter', 'melonade', 'ade']) == ['water', 'melon', 'wa', 'ter', 'ade']
    assert candidate(words = ['apple', 'pineapple', 'grape', 'pinegrape', 'grapefruit', 'pineapplegrape']) == ['apple', 'pineapple', 'grape']
    assert candidate(words = ['abc', 'def', 'abcd', 'abcde', 'abcdef']) == ['abc', 'def', 'abcd', 'abcde']
    assert candidate(words = ['supercalifragilisticexpialidocious', 'super', 'cali', 'fragi', 'listic', 'expiali', 'docious', 'fragilisticexpialidocious']) == ['super', 'cali', 'fragi', 'listic', 'expiali', 'docious', 'fragilisticexpialidocious']
    assert candidate(words = ['unbelievable', 'un', 'believe', 'able', 'e', 'a', 'i', 'o', 'u']) == ['un', 'able', 'e', 'a', 'i', 'u']
    assert candidate(words = ['encyclopedia', 'encyclop', 'yclopedia', 'cloped', 'lopedia', 'pedia', 'dia', 'dialect', 'logic', 'encyclopediaic']) == ['encyclopedia', 'encyclop', 'yclopedia', 'cloped', 'lopedia', 'pedia', 'dia']
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnop', 'qrstuvwxyz', 'mnopqrstu', 'vwxyz']) == ['abcdefghijklmnop', 'qrstuvwxyz', 'mnopqrstu', 'vwxyz']
    assert candidate(words = ['supercalifragilisticexpialidocious', 'fragilistic', 'expialidocious', 'docious', 'ious', 'ous', 'us', 's']) == ['fragilistic', 'expialidocious', 'docious', 'ious', 'ous', 'us', 's']
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == ['a', 'ab', 'abc', 'abcd', 'abcde']
    assert candidate(words = ['algorithm', 'algo', 'rhythm', 'thm', 'rthm', 'hythmthm']) == ['algo', 'thm']


