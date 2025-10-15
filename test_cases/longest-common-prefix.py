def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(strs = ['hello', 'helium', 'helper']) == "hel"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['hello', 'helium', 'helper']) == "hel": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', '', '', '']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', '', '', '']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['apple', 'app', 'apricot']) == "ap"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['apple', 'app', 'apricot']) == "ap": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abce', 'abcf']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abce', 'abcf']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['apple', 'app', 'application']) == "app"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['apple', 'app', 'application']) == "app": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['interview', 'interrupt', 'inter']) == "inter"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['interview', 'interrupt', 'inter']) == "inter": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['test', 'testing', 'tester']) == "test"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['test', 'testing', 'tester']) == "test": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['hello', 'hell', 'hella']) == "hell"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['hello', 'hell', 'hella']) == "hell": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['flower', 'flow', 'flight']) == "fl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['flower', 'flow', 'flight']) == "fl": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['same', 'same', 'same']) == "same"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['same', 'same', 'same']) == "same": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['single']) == "single"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['single']) == "single": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['ab', 'abc', 'abcd']) == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['ab', 'abc', 'abcd']) == "ab": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abc', 'abc', 'abc']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abc', 'abc', 'abc']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'dcba', 'abdc']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'dcba', 'abdc']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', 'b', 'abc']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', 'b', 'abc']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'ab', 'abc']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'ab', 'abc']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['dog', 'racecar', 'car']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['dog', 'racecar', 'car']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'a', 'a', 'a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'a', 'a', 'a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', '', 'abc']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', '', 'abc']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abc', 'abcd', 'abcde']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abc', 'abcd', 'abcde']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abc', 'ab', 'a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abc', 'ab', 'a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['banana', 'bandana', 'banner']) == "ban"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['banana', 'bandana', 'banner']) == "ban": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aaaa', 'aaab', 'aaac']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aaaa', 'aaab', 'aaac']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['mississippi', 'mississauga', 'mission', 'missed']) == "miss"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['mississippi', 'mississauga', 'mission', 'missed']) == "miss": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['commonality', 'commonwealth', 'common', 'commons']) == "common"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['commonality', 'commonwealth', 'common', 'commons']) == "common": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['different', 'prefixes', 'here']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['different', 'prefixes', 'here']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['repetition', 'repetitive', 'repeat', 'repel', 'repeal', 'repetend']) == "repe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['repetition', 'repetitive', 'repeat', 'repel', 'repeal', 'repetend']) == "repe": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['million', 'millionaire', 'millionth', 'millionfold']) == "million"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['million', 'millionaire', 'millionth', 'millionfold']) == "million": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algorithmic', 'algebra', 'alignment']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algorithmic', 'algebra', 'alignment']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['difficult', 'difficulty', 'differ']) == "diff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['difficult', 'difficulty', 'differ']) == "diff": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['environment', 'environmental', 'envision', 'enzyme']) == "en"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['environment', 'environmental', 'envision', 'enzyme']) == "en": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'aa', 'aaa', 'aaaa']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'aa', 'aaa', 'aaaa']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['xylophone', 'xylotomy', 'xylography', 'xylograph']) == "xylo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['xylophone', 'xylotomy', 'xylography', 'xylograph']) == "xylo": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'abc', 'ab', 'a', 'abcde']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'abc', 'ab', 'a', 'abcde']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['unique', 'unit', 'universe', 'unity', 'un']) == "un"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['unique', 'unit', 'universe', 'unity', 'un']) == "un": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['same', 'same', 'same', 'same']) == "same"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['same', 'same', 'same', 'same']) == "same": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['short', 'small', 'shallow', 'shrink']) == "s"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['short', 'small', 'shallow', 'shrink']) == "s": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zebra', 'zoo', 'zenith', 'zest', 'zone', 'zephyr']) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zebra', 'zoo', 'zenith', 'zest', 'zone', 'zephyr']) == "z": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['multidimensional', 'multidimensionalities', 'multidimensionally', 'multidimensionalization']) == "multidimensional"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['multidimensional', 'multidimensionalities', 'multidimensionally', 'multidimensionalization']) == "multidimensional": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['computation', 'compute', 'computer', 'comedy']) == "com"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['computation', 'compute', 'computer', 'comedy']) == "com": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'ab', 'a', 'abcde']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'ab', 'a', 'abcde']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'abcdf', 'abcde', 'abcda', 'abcde', 'abcdf']) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'abcdf', 'abcde', 'abcda', 'abcde', 'abcdf']) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zebra', 'zoo', 'zealot']) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zebra', 'zoo', 'zealot']) == "z": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abcde', 'ab', 'a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abcde', 'ab', 'a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['microphone', 'microwave', 'microscope', 'microbial']) == "micro"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['microphone', 'microwave', 'microscope', 'microbial']) == "micro": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['longest', 'long', 'lonely']) == "lon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['longest', 'long', 'lonely']) == "lon": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'preprocessor', 'prevent']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'preprocessor', 'prevent']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algorithmically', '', 'algorithmic']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algorithmically', '', 'algorithmic']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'alert', 'alibaba', 'allied']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'alert', 'alibaba', 'allied']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['unbelievable', 'unbeliever', 'unbelievably', 'unbelievability']) == "unbeliev"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['unbelievable', 'unbeliever', 'unbelievably', 'unbelievability']) == "unbeliev": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'preposition', 'prevent', 'premier']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'preposition', 'prevent', 'premier']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'prefixes', 'prefixation', 'prefixed']) == "prefix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'prefixes', 'prefixation', 'prefixed']) == "prefix": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'b', 'c', 'd']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'b', 'c', 'd']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', 'same', 'same', 'same', 'same']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', 'same', 'same', 'same', 'same']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['same', 'same', 'same', 'same', 'same']) == "same"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['same', 'same', 'same', 'same', 'same']) == "same": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['optimization', 'optimization', 'optimized', 'optimizer']) == "optimiz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['optimization', 'optimization', 'optimized', 'optimizer']) == "optimiz": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['communication', 'communicate', 'commune', 'communist']) == "commun"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['communication', 'communicate', 'commune', 'communist']) == "commun": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algorithmically', 'algebra', 'allegro']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algorithmically', 'algebra', 'allegro']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['common', 'commotion', 'communicate', 'community']) == "comm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['common', 'commotion', 'communicate', 'community']) == "comm": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['flower', 'flow', 'flight', 'flew', 'flying', 'flowing']) == "fl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['flower', 'flow', 'flight', 'flew', 'flying', 'flowing']) == "fl": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['single', 'singlehandedly', 'singlemindedness', 'singlehanded']) == "single"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['single', 'singlehandedly', 'singlemindedness', 'singlehanded']) == "single": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algebra', 'alaska']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algebra', 'alaska']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['congratulations', 'congruity', 'congruent']) == "congr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['congratulations', 'congruity', 'congruent']) == "congr": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'ab', 'abc', 'abcd']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'ab', 'abc', 'abcd']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algorithmic', 'algorithmically', 'algorithmically']) == "algorithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algorithmic', 'algorithmically', 'algorithmically']) == "algorithm": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['preference', 'prefix', 'prevent', 'prey']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['preference', 'prefix', 'prevent', 'prey']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abracadabra', 'abracadabras', 'abracadabaster', 'abracadabration']) == "abracadab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abracadabra', 'abracadabras', 'abracadabaster', 'abracadabration']) == "abracadab": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['supercalifragilisticexpialidocious', 'super', 'supersonic']) == "super"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['supercalifragilisticexpialidocious', 'super', 'supersonic']) == "super": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['unanimity', 'unanimous', 'unanimously', 'unanimated']) == "unanim"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['unanimity', 'unanimous', 'unanimously', 'unanimated']) == "unanim": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['orthogonal', 'orthodox', 'orthopedic', 'orthography']) == "ortho"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['orthogonal', 'orthodox', 'orthopedic', 'orthography']) == "ortho": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abcde', 'abcdef', 'abcdefg']) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abcde', 'abcdef', 'abcdefg']) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['programming', 'programmer', 'programmatic', 'program']) == "program"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['programming', 'programmer', 'programmatic', 'program']) == "program": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['sequential', 'sequence', 'sequent', 'sequel']) == "seque"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['sequential', 'sequence', 'sequent', 'sequel']) == "seque": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abracadabra', 'abr', 'abracadabrador', 'abrac']) == "abr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abracadabra', 'abr', 'abracadabrador', 'abrac']) == "abr": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['consistent', 'consistency', 'consistently', 'consist']) == "consist"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['consistent', 'consistency', 'consistently', 'consist']) == "consist": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['common', 'community', 'comma', 'communist']) == "comm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['common', 'community', 'comma', 'communist']) == "comm": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zebra', 'zoo', 'zealot', 'zest']) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zebra', 'zoo', 'zealot', 'zest']) == "z": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'a', 'a', 'a', 'a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'a', 'a', 'a', 'a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algebra', 'altitude', 'altimeter']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algebra', 'altitude', 'altimeter']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['supercalifragilisticexpialidocious', 'super', 'supercal']) == "super"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['supercalifragilisticexpialidocious', 'super', 'supercal']) == "super": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['maximum', 'maximize', 'maximal']) == "maxim"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['maximum', 'maximize', 'maximal']) == "maxim": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['complex', 'complicated', 'complect', 'complete']) == "compl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['complex', 'complicated', 'complect', 'complete']) == "compl": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'pre', 'preface', 'prefer', 'preference', 'prefixing']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'pre', 'preface', 'prefer', 'preference', 'prefixing']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghij', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghij', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'abcde', 'abcde', 'abcde']) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'abcde', 'abcde', 'abcde']) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algorhythm', 'algae']) == "alg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algorhythm', 'algae']) == "alg": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', '', '', '', 'a']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', '', '', '', 'a']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['xylophone', 'xylography', 'xylogen', 'xylophonist']) == "xylo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['xylophone', 'xylography', 'xylogen', 'xylophonist']) == "xylo": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['onomatopoeia', 'onomatopoetic', 'onomatope', 'onomatologist']) == "onomato"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['onomatopoeia', 'onomatopoetic', 'onomatope', 'onomatologist']) == "onomato": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['rehabilitation', 'rehabilitate', 'rehabilitative', 'rehabilitated']) == "rehabilitat"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['rehabilitation', 'rehabilitate', 'rehabilitative', 'rehabilitated']) == "rehabilitat": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['mississippi', 'missile', 'mission', 'missive']) == "missi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['mississippi', 'missile', 'mission', 'missive']) == "missi": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['longest', 'longevity', 'longitudinal']) == "long"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['longest', 'longevity', 'longitudinal']) == "long": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['psychological', 'psychologist', 'psychology', 'psychic']) == "psych"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['psychological', 'psychologist', 'psychology', 'psychic']) == "psych": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['environment', 'envelope', 'envoy', 'evening']) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['environment', 'envelope', 'envoy', 'evening']) == "e": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['short', 'shorthand', 'shortfall']) == "short"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['short', 'shorthand', 'shortfall']) == "short": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['parallel', 'parallelogram', 'parallactic', 'paralactic']) == "paral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['parallel', 'parallelogram', 'parallactic', 'paralactic']) == "paral": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['cryptography', 'cryptographic', 'cryptanalysis', 'cryptanalytic']) == "crypt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['cryptography', 'cryptographic', 'cryptanalysis', 'cryptanalytic']) == "crypt": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zebra', 'zoo', 'zero', 'zapper']) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zebra', 'zoo', 'zero', 'zapper']) == "z": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['singleword', 'single', 'singleton']) == "single"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['singleword', 'single', 'singleton']) == "single": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['anthropomorphic', 'anthropologist', 'anthropology', 'anthropocentric']) == "anthropo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['anthropomorphic', 'anthropologist', 'anthropology', 'anthropocentric']) == "anthropo": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', '', '', 'a']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', '', '', 'a']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'ab', 'abc', 'abcd', 'abcde']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'ab', 'abc', 'abcd', 'abcde']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['common', 'commune', 'command', 'community']) == "comm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['common', 'commune', 'command', 'community']) == "comm": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['same', 'samsung', 'sample', 'sand', 'satellite', 'saturn']) == "sa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['same', 'samsung', 'sample', 'sand', 'satellite', 'saturn']) == "sa": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algebra', 'altitude']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algebra', 'altitude']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['implementation', 'implement', 'implementing', 'implementor']) == "implement"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['implementation', 'implement', 'implementing', 'implementor']) == "implement": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abracadabra', 'abracadabra', 'abracadabra']) == "abracadabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abracadabra', 'abracadabra', 'abracadabra']) == "abracadabra": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['reorganization', 'reorganize', 'reorganized', 'reorganizing']) == "reorganiz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['reorganization', 'reorganize', 'reorganized', 'reorganizing']) == "reorganiz": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['university', 'universe', 'unique', 'unicorn']) == "uni"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['university', 'universe', 'unique', 'unicorn']) == "uni": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', 'longest', 'longevity', 'logistics']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', 'longest', 'longevity', 'logistics']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', '', '', 'abc']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', '', '', 'abc']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['environment', 'envy', 'envelop', 'enviable']) == "env"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['environment', 'envy', 'envelop', 'enviable']) == "env": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['unique', 'unicorn', 'unify', 'unity']) == "uni"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['unique', 'unicorn', 'unify', 'unity']) == "uni": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa']) == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa']) == "aa": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zebra', 'zoo', 'zeal', 'zither']) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zebra', 'zoo', 'zeal', 'zither']) == "z": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', 'a', 'ab', 'abc', 'abcd']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', 'a', 'ab', 'abc', 'abcd']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aardvark', 'aardwolf', 'aardvark', 'aard']) == "aard"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aardvark', 'aardwolf', 'aardvark', 'aard']) == "aard": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == "z": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['separation', 'separately', 'separated', 'separating']) == "separat"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['separation', 'separately', 'separated', 'separating']) == "separat": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['mississippi', 'missile', 'mission', 'miss']) == "miss"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['mississippi', 'missile', 'mission', 'miss']) == "miss": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algebra', 'alien', 'alert']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algebra', 'alien', 'alert']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['commonality', 'common', 'commune', 'community', 'communicate', 'commemorative']) == "comm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['commonality', 'common', 'commune', 'community', 'communicate', 'commemorative']) == "comm": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'supercalifragili', 'super']) == "super"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'supercalifragili', 'super']) == "super": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['parallel', 'parallelepiped', 'paralleled', 'paralegal']) == "paral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['parallel', 'parallelepiped', 'paralleled', 'paralegal']) == "paral": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'preference', 'presentation']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'preference', 'presentation']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['unified', 'uniform', 'universe', 'unique']) == "uni"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['unified', 'uniform', 'universe', 'unique']) == "uni": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['anagram', 'anagrams', 'anagrammatic', 'anagrammatical']) == "anagram"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['anagram', 'anagrams', 'anagrammatic', 'anagrammatical']) == "anagram": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['environment', 'environmental', 'environments', 'environmentally']) == "environment"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['environment', 'environmental', 'environments', 'environmentally']) == "environment": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['xylophone', 'xylography', 'xylophonist', 'xylophonics']) == "xylo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['xylophone', 'xylography', 'xylophonist', 'xylophonics']) == "xylo": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', '', 'prefix', 'prefix']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', '', 'prefix', 'prefix']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['algorithm', 'algebra', 'altimeter']) == "al"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['algorithm', 'algebra', 'altimeter']) == "al": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['recognition', 'recognizable', 'recognize', 'recognizably']) == "recogni"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['recognition', 'recognizable', 'recognize', 'recognizably']) == "recogni": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'preposition', 'presentation']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'preposition', 'presentation']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['challenges', 'challenging', 'challenge', 'challengingly']) == "challeng"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['challenges', 'challenging', 'challenge', 'challengingly']) == "challeng": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['universally', 'universe', 'universal', 'universality', 'universes', 'universally']) == "univers"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['universally', 'universe', 'universal', 'universality', 'universes', 'universally']) == "univers": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['mississippi', 'missile', 'missionary', 'misspell']) == "miss"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['mississippi', 'missile', 'missionary', 'misspell']) == "miss": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['photosynthesis', 'photosynthetic', 'photosynthesize', 'photosynthetically']) == "photosynthe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['photosynthesis', 'photosynthetic', 'photosynthesize', 'photosynthetically']) == "photosynthe": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['apple', 'apply', 'appetite', 'apparatus']) == "app"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['apple', 'apply', 'appetite', 'apparatus']) == "app": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'pretext', 'prevent']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'pretext', 'prevent']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['development', 'develop', 'developer', 'developmental', 'developing', 'devel']) == "devel"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['development', 'develop', 'developer', 'developmental', 'developing', 'devel']) == "devel": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['prefix', 'preference', 'presentation', 'president', 'pressure', 'premier']) == "pre"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['prefix', 'preference', 'presentation', 'president', 'pressure', 'premier']) == "pre": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['', 'unique', 'unanimous', 'unicorn', 'unicycle', 'unify']) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['', 'unique', 'unanimous', 'unicorn', 'unicycle', 'unify']) == "": {e}')
    
    total += 1
    try:
        result = candidate(strs = ['complex', 'complicated', 'completion']) == "compl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['complex', 'complicated', 'completion']) == "compl": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(strs = ['hello', 'helium', 'helper']) == "hel"
    assert candidate(strs = ['a']) == "a"
    assert candidate(strs = ['', '', '', '']) == ""
    assert candidate(strs = ['apple', 'app', 'apricot']) == "ap"
    assert candidate(strs = ['abcd', 'abce', 'abcf']) == "abc"
    assert candidate(strs = ['apple', 'app', 'application']) == "app"
    assert candidate(strs = ['interview', 'interrupt', 'inter']) == "inter"
    assert candidate(strs = ['test', 'testing', 'tester']) == "test"
    assert candidate(strs = ['hello', 'hell', 'hella']) == "hell"
    assert candidate(strs = ['flower', 'flow', 'flight']) == "fl"
    assert candidate(strs = ['same', 'same', 'same']) == "same"
    assert candidate(strs = ['single']) == "single"
    assert candidate(strs = ['ab', 'abc', 'abcd']) == "ab"
    assert candidate(strs = ['abc', 'abc', 'abc']) == "abc"
    assert candidate(strs = ['abcd', 'dcba', 'abdc']) == ""
    assert candidate(strs = ['', 'b', 'abc']) == ""
    assert candidate(strs = ['a', 'ab', 'abc']) == "a"
    assert candidate(strs = ['dog', 'racecar', 'car']) == ""
    assert candidate(strs = ['a', 'a', 'a', 'a']) == "a"
    assert candidate(strs = ['', '', 'abc']) == ""
    assert candidate(strs = ['abc', 'abcd', 'abcde']) == "abc"
    assert candidate(strs = ['abcd', 'abc', 'ab', 'a']) == "a"
    assert candidate(strs = ['banana', 'bandana', 'banner']) == "ban"
    assert candidate(strs = ['aaaa', 'aaab', 'aaac']) == "aaa"
    assert candidate(strs = ['mississippi', 'mississauga', 'mission', 'missed']) == "miss"
    assert candidate(strs = ['commonality', 'commonwealth', 'common', 'commons']) == "common"
    assert candidate(strs = ['different', 'prefixes', 'here']) == ""
    assert candidate(strs = ['repetition', 'repetitive', 'repeat', 'repel', 'repeal', 'repetend']) == "repe"
    assert candidate(strs = ['million', 'millionaire', 'millionth', 'millionfold']) == "million"
    assert candidate(strs = ['algorithm', 'algorithmic', 'algebra', 'alignment']) == "al"
    assert candidate(strs = ['difficult', 'difficulty', 'differ']) == "diff"
    assert candidate(strs = ['environment', 'environmental', 'envision', 'enzyme']) == "en"
    assert candidate(strs = ['a', 'aa', 'aaa', 'aaaa']) == "a"
    assert candidate(strs = ['xylophone', 'xylotomy', 'xylography', 'xylograph']) == "xylo"
    assert candidate(strs = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == "a"
    assert candidate(strs = ['abcde', 'abc', 'ab', 'a', 'abcde']) == "a"
    assert candidate(strs = ['unique', 'unit', 'universe', 'unity', 'un']) == "un"
    assert candidate(strs = ['same', 'same', 'same', 'same']) == "same"
    assert candidate(strs = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "a"
    assert candidate(strs = ['short', 'small', 'shallow', 'shrink']) == "s"
    assert candidate(strs = ['zebra', 'zoo', 'zenith', 'zest', 'zone', 'zephyr']) == "z"
    assert candidate(strs = ['multidimensional', 'multidimensionalities', 'multidimensionally', 'multidimensionalization']) == "multidimensional"
    assert candidate(strs = ['computation', 'compute', 'computer', 'comedy']) == "com"
    assert candidate(strs = ['abcd', 'ab', 'a', 'abcde']) == "a"
    assert candidate(strs = ['abcde', 'abcdf', 'abcde', 'abcda', 'abcde', 'abcdf']) == "abcd"
    assert candidate(strs = ['zebra', 'zoo', 'zealot']) == "z"
    assert candidate(strs = ['abcd', 'abcde', 'ab', 'a']) == "a"
    assert candidate(strs = ['microphone', 'microwave', 'microscope', 'microbial']) == "micro"
    assert candidate(strs = ['longest', 'long', 'lonely']) == "lon"
    assert candidate(strs = ['prefix', 'preprocessor', 'prevent']) == "pre"
    assert candidate(strs = ['algorithm', 'algorithmically', '', 'algorithmic']) == ""
    assert candidate(strs = ['algorithm', 'alert', 'alibaba', 'allied']) == "al"
    assert candidate(strs = ['unbelievable', 'unbeliever', 'unbelievably', 'unbelievability']) == "unbeliev"
    assert candidate(strs = ['prefix', 'preposition', 'prevent', 'premier']) == "pre"
    assert candidate(strs = ['prefix', 'prefixes', 'prefixation', 'prefixed']) == "prefix"
    assert candidate(strs = ['a', 'b', 'c', 'd']) == ""
    assert candidate(strs = ['', 'same', 'same', 'same', 'same']) == ""
    assert candidate(strs = ['same', 'same', 'same', 'same', 'same']) == "same"
    assert candidate(strs = ['optimization', 'optimization', 'optimized', 'optimizer']) == "optimiz"
    assert candidate(strs = ['communication', 'communicate', 'commune', 'communist']) == "commun"
    assert candidate(strs = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == "a"
    assert candidate(strs = ['algorithm', 'algorithmically', 'algebra', 'allegro']) == "al"
    assert candidate(strs = ['common', 'commotion', 'communicate', 'community']) == "comm"
    assert candidate(strs = ['flower', 'flow', 'flight', 'flew', 'flying', 'flowing']) == "fl"
    assert candidate(strs = ['single', 'singlehandedly', 'singlemindedness', 'singlehanded']) == "single"
    assert candidate(strs = ['algorithm', 'algebra', 'alaska']) == "al"
    assert candidate(strs = ['congratulations', 'congruity', 'congruent']) == "congr"
    assert candidate(strs = ['a', 'ab', 'abc', 'abcd']) == "a"
    assert candidate(strs = ['algorithm', 'algorithmic', 'algorithmically', 'algorithmically']) == "algorithm"
    assert candidate(strs = ['preference', 'prefix', 'prevent', 'prey']) == "pre"
    assert candidate(strs = ['abracadabra', 'abracadabras', 'abracadabaster', 'abracadabration']) == "abracadab"
    assert candidate(strs = ['supercalifragilisticexpialidocious', 'super', 'supersonic']) == "super"
    assert candidate(strs = ['unanimity', 'unanimous', 'unanimously', 'unanimated']) == "unanim"
    assert candidate(strs = ['orthogonal', 'orthodox', 'orthopedic', 'orthography']) == "ortho"
    assert candidate(strs = ['abcd', 'abcde', 'abcdef', 'abcdefg']) == "abcd"
    assert candidate(strs = ['programming', 'programmer', 'programmatic', 'program']) == "program"
    assert candidate(strs = ['sequential', 'sequence', 'sequent', 'sequel']) == "seque"
    assert candidate(strs = ['abracadabra', 'abr', 'abracadabrador', 'abrac']) == "abr"
    assert candidate(strs = ['consistent', 'consistency', 'consistently', 'consist']) == "consist"
    assert candidate(strs = ['common', 'community', 'comma', 'communist']) == "comm"
    assert candidate(strs = ['zebra', 'zoo', 'zealot', 'zest']) == "z"
    assert candidate(strs = ['a', 'a', 'a', 'a', 'a']) == "a"
    assert candidate(strs = ['algorithm', 'algebra', 'altitude', 'altimeter']) == "al"
    assert candidate(strs = ['supercalifragilisticexpialidocious', 'super', 'supercal']) == "super"
    assert candidate(strs = ['maximum', 'maximize', 'maximal']) == "maxim"
    assert candidate(strs = ['complex', 'complicated', 'complect', 'complete']) == "compl"
    assert candidate(strs = ['prefix', 'pre', 'preface', 'prefer', 'preference', 'prefixing']) == "pre"
    assert candidate(strs = ['abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']) == "abcd"
    assert candidate(strs = ['abcdefghij', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "a"
    assert candidate(strs = ['abcde', 'abcde', 'abcde', 'abcde']) == "abcde"
    assert candidate(strs = ['algorithm', 'algorhythm', 'algae']) == "alg"
    assert candidate(strs = ['', '', '', '', 'a']) == ""
    assert candidate(strs = ['xylophone', 'xylography', 'xylogen', 'xylophonist']) == "xylo"
    assert candidate(strs = ['onomatopoeia', 'onomatopoetic', 'onomatope', 'onomatologist']) == "onomato"
    assert candidate(strs = ['rehabilitation', 'rehabilitate', 'rehabilitative', 'rehabilitated']) == "rehabilitat"
    assert candidate(strs = ['mississippi', 'missile', 'mission', 'missive']) == "missi"
    assert candidate(strs = ['longest', 'longevity', 'longitudinal']) == "long"
    assert candidate(strs = ['psychological', 'psychologist', 'psychology', 'psychic']) == "psych"
    assert candidate(strs = ['environment', 'envelope', 'envoy', 'evening']) == "e"
    assert candidate(strs = ['short', 'shorthand', 'shortfall']) == "short"
    assert candidate(strs = ['parallel', 'parallelogram', 'parallactic', 'paralactic']) == "paral"
    assert candidate(strs = ['cryptography', 'cryptographic', 'cryptanalysis', 'cryptanalytic']) == "crypt"
    assert candidate(strs = ['zebra', 'zoo', 'zero', 'zapper']) == "z"
    assert candidate(strs = ['singleword', 'single', 'singleton']) == "single"
    assert candidate(strs = ['anthropomorphic', 'anthropologist', 'anthropology', 'anthropocentric']) == "anthropo"
    assert candidate(strs = ['', '', '', 'a']) == ""
    assert candidate(strs = ['a', 'ab', 'abc', 'abcd', 'abcde']) == "a"
    assert candidate(strs = ['common', 'commune', 'command', 'community']) == "comm"
    assert candidate(strs = ['same', 'samsung', 'sample', 'sand', 'satellite', 'saturn']) == "sa"
    assert candidate(strs = ['algorithm', 'algebra', 'altitude']) == "al"
    assert candidate(strs = ['implementation', 'implement', 'implementing', 'implementor']) == "implement"
    assert candidate(strs = ['abracadabra', 'abracadabra', 'abracadabra']) == "abracadabra"
    assert candidate(strs = ['reorganization', 'reorganize', 'reorganized', 'reorganizing']) == "reorganiz"
    assert candidate(strs = ['university', 'universe', 'unique', 'unicorn']) == "uni"
    assert candidate(strs = ['', 'longest', 'longevity', 'logistics']) == ""
    assert candidate(strs = ['', '', '', 'abc']) == ""
    assert candidate(strs = ['environment', 'envy', 'envelop', 'enviable']) == "env"
    assert candidate(strs = ['unique', 'unicorn', 'unify', 'unity']) == "uni"
    assert candidate(strs = ['aabbcc', 'aabbc', 'aabb', 'aab', 'aa']) == "aa"
    assert candidate(strs = ['zebra', 'zoo', 'zeal', 'zither']) == "z"
    assert candidate(strs = ['', 'a', 'ab', 'abc', 'abcd']) == ""
    assert candidate(strs = ['aardvark', 'aardwolf', 'aardvark', 'aard']) == "aard"
    assert candidate(strs = ['zzzzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == "z"
    assert candidate(strs = ['separation', 'separately', 'separated', 'separating']) == "separat"
    assert candidate(strs = ['mississippi', 'missile', 'mission', 'miss']) == "miss"
    assert candidate(strs = ['algorithm', 'algebra', 'alien', 'alert']) == "al"
    assert candidate(strs = ['commonality', 'common', 'commune', 'community', 'communicate', 'commemorative']) == "comm"
    assert candidate(strs = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'supercalifragili', 'super']) == "super"
    assert candidate(strs = ['parallel', 'parallelepiped', 'paralleled', 'paralegal']) == "paral"
    assert candidate(strs = ['prefix', 'preference', 'presentation']) == "pre"
    assert candidate(strs = ['unified', 'uniform', 'universe', 'unique']) == "uni"
    assert candidate(strs = ['anagram', 'anagrams', 'anagrammatic', 'anagrammatical']) == "anagram"
    assert candidate(strs = ['environment', 'environmental', 'environments', 'environmentally']) == "environment"
    assert candidate(strs = ['xylophone', 'xylography', 'xylophonist', 'xylophonics']) == "xylo"
    assert candidate(strs = ['prefix', '', 'prefix', 'prefix']) == ""
    assert candidate(strs = ['algorithm', 'algebra', 'altimeter']) == "al"
    assert candidate(strs = ['recognition', 'recognizable', 'recognize', 'recognizably']) == "recogni"
    assert candidate(strs = ['prefix', 'preposition', 'presentation']) == "pre"
    assert candidate(strs = ['challenges', 'challenging', 'challenge', 'challengingly']) == "challeng"
    assert candidate(strs = ['universally', 'universe', 'universal', 'universality', 'universes', 'universally']) == "univers"
    assert candidate(strs = ['mississippi', 'missile', 'missionary', 'misspell']) == "miss"
    assert candidate(strs = ['photosynthesis', 'photosynthetic', 'photosynthesize', 'photosynthetically']) == "photosynthe"
    assert candidate(strs = ['apple', 'apply', 'appetite', 'apparatus']) == "app"
    assert candidate(strs = ['prefix', 'pretext', 'prevent']) == "pre"
    assert candidate(strs = ['development', 'develop', 'developer', 'developmental', 'developing', 'devel']) == "devel"
    assert candidate(strs = ['prefix', 'preference', 'presentation', 'president', 'pressure', 'premier']) == "pre"
    assert candidate(strs = ['', 'unique', 'unanimous', 'unicorn', 'unicycle', 'unify']) == ""
    assert candidate(strs = ['complex', 'complicated', 'completion']) == "compl"


