def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bac', 'bca', 'cab', 'cba', 'acb'],groups = [1, 2, 1, 2, 1, 2]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bac', 'bca', 'cab', 'cba', 'acb'],groups = [1, 2, 1, 2, 1, 2]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'same'],groups = [1, 2, 1]) == ['same', 'sane', 'same']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'same'],groups = [1, 2, 1]) == ['same', 'sane', 'same']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'best', 'rest'],groups = [1, 2, 2, 3]) == ['test', 'best', 'rest']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'best', 'rest'],groups = [1, 2, 2, 3]) == ['test', 'best', 'rest']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 2, 2, 3]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 2, 2, 3]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abgf', 'abgh'],groups = [1, 2, 2, 3]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abgf', 'abgh'],groups = [1, 2, 2, 3]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hbllo', 'hillo'],groups = [1, 1, 2, 3]) == ['hello', 'hbllo', 'hillo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hbllo', 'hillo'],groups = [1, 1, 2, 3]) == ['hello', 'hbllo', 'hillo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['bab', 'dab', 'cab'],groups = [1, 2, 2]) == ['bab', 'dab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['bab', 'dab', 'cab'],groups = [1, 2, 2]) == ['bab', 'dab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'wore', 'core'],groups = [1, 2, 1, 2]) == ['word', 'worm', 'wore', 'core']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'wore', 'core'],groups = [1, 2, 1, 2]) == ['word', 'worm', 'wore', 'core']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 2, 3]) == ['same', 'tame', 'game']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 2, 3]) == ['same', 'tame', 'game']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd'],groups = [1, 2, 3, 4]) == ['a', 'b', 'c', 'd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd'],groups = [1, 2, 3, 4]) == ['a', 'b', 'c', 'd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'appel'],groups = [1, 2, 1]) == ['apple', 'appla']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'appel'],groups = [1, 2, 1]) == ['apple', 'appla']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd'],groups = [1, 2, 3, 4]) == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd'],groups = [1, 2, 3, 4]) == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zzx', 'zzw', 'zzv'],groups = [1, 2, 3, 4]) == ['zzz', 'zzx', 'zzw', 'zzv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zzx', 'zzw', 'zzv'],groups = [1, 2, 3, 4]) == ['zzz', 'zzx', 'zzw', 'zzv']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tost', 'test'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tost', 'test']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tost', 'test'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tost', 'test']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 2, 3, 4]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 2, 3, 4]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 2, 2, 3]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 2, 2, 3]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl'],groups = [1, 1, 2, 2]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl'],groups = [1, 1, 2, 2]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 1, 2]) == ['word', 'wird', 'word', 'wird']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 1, 2]) == ['word', 'wird', 'word', 'wird']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abb', 'aba', 'aaa', 'aab'],groups = [1, 2, 3, 4, 5]) == ['abc', 'abb', 'aba', 'aaa', 'aab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abb', 'aba', 'aaa', 'aab'],groups = [1, 2, 3, 4, 5]) == ['abc', 'abb', 'aba', 'aaa', 'aab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'abab', 'abba', 'baab'],groups = [1, 2, 1, 2]) == ['aabb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'abab', 'abba', 'baab'],groups = [1, 2, 1, 2]) == ['aabb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'abab', 'babb', 'baab'],groups = [1, 2, 1, 2]) == ['babb', 'baab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'abab', 'babb', 'baab'],groups = [1, 2, 1, 2]) == ['babb', 'baab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'cot', 'dog', 'dot', 'log'],groups = [1, 2, 1, 2, 3]) == ['cat', 'cot']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'cot', 'dog', 'dot', 'log'],groups = [1, 2, 1, 2, 3]) == ['cat', 'cot']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],groups = [1, 2, 1, 2, 1, 2]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],groups = [1, 2, 1, 2, 1, 2]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyw', 'xyv', 'xyu'],groups = [1, 2, 3, 4]) == ['xyz', 'xyw', 'xyv', 'xyu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyw', 'xyv', 'xyu'],groups = [1, 2, 3, 4]) == ['xyz', 'xyw', 'xyv', 'xyu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb'],groups = [1, 2, 3, 4, 5]) == ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb'],groups = [1, 2, 3, 4, 5]) == ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bac', 'cab', 'bca', 'acb', 'cba'],groups = [1, 2, 3, 1, 2, 3]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bac', 'cab', 'bca', 'acb', 'cba'],groups = [1, 2, 3, 1, 2, 3]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abcg'],groups = [1, 2, 3, 4]) == ['abcd', 'abce', 'abcf', 'abcg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abcg'],groups = [1, 2, 3, 4]) == ['abcd', 'abce', 'abcf', 'abcg']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd', 'ace'],groups = [1, 2, 1, 2, 1]) == ['abc', 'abd', 'acd', 'bcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd', 'ace'],groups = [1, 2, 1, 2, 1]) == ['abc', 'abd', 'acd', 'bcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdf', 'abef', 'acdf', 'acef', 'bcdf', 'bcef'],groups = [1, 2, 1, 2, 1, 2, 1, 2]) == ['abcd', 'abcf', 'abdf', 'abef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdf', 'abef', 'acdf', 'acef', 'bcdf', 'bcef'],groups = [1, 2, 1, 2, 1, 2, 1, 2]) == ['abcd', 'abcf', 'abdf', 'abef']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'codd', 'cods', 'coex', 'coey'],groups = [1, 2, 2, 3, 3]) == ['code', 'codd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'codd', 'cods', 'coex', 'coey'],groups = [1, 2, 2, 3, 3]) == ['code', 'codd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg'],groups = [1, 2, 3, 4, 5]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg'],groups = [1, 2, 3, 4, 5]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apples', 'appl', 'app'],groups = [1, 2, 3, 4]) == ['apple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apples', 'appl', 'app'],groups = [1, 2, 3, 4]) == ['apple']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sate', 'site'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'sate', 'site']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sate', 'site'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'sate', 'site']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'abfde', 'abcfe', 'abcef'],groups = [1, 2, 3, 4]) == ['abcde', 'abfde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'abfde', 'abcfe', 'abcef'],groups = [1, 2, 3, 4]) == ['abcde', 'abfde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde'],groups = [1, 2, 1, 2, 1, 2]) == ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde'],groups = [1, 2, 1, 2, 1, 2]) == ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'mnoq', 'mnrp', 'mnsp', 'mntp'],groups = [1, 2, 3, 2, 1]) == ['mnop', 'mnrp', 'mnsp', 'mntp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'mnoq', 'mnrp', 'mnsp', 'mntp'],groups = [1, 2, 3, 2, 1]) == ['mnop', 'mnrp', 'mnsp', 'mntp']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apply', 'appla', 'appla'],groups = [1, 2, 1, 3]) == ['apple', 'apply', 'appla']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apply', 'appla', 'appla'],groups = [1, 2, 1, 3]) == ['apple', 'apply', 'appla']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'abaa', 'acaa', 'aada', 'aada', 'aadd'],groups = [1, 2, 3, 1, 2, 3]) == ['aaaa', 'abaa', 'acaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'abaa', 'acaa', 'aada', 'aada', 'aadd'],groups = [1, 2, 3, 1, 2, 3]) == ['aaaa', 'abaa', 'acaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'cog', 'dag', 'dog', 'dig'],groups = [1, 2, 1, 2, 1]) == ['dag', 'dog', 'dig']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'cog', 'dag', 'dog', 'dig'],groups = [1, 2, 1, 2, 1]) == ['dag', 'dog', 'dig']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'wirm', 'wirm', 'wirn'],groups = [1, 2, 3, 4, 5]) == ['word', 'worm', 'wirm', 'wirn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'wirm', 'wirm', 'wirn'],groups = [1, 2, 3, 4, 5]) == ['word', 'worm', 'wirm', 'wirn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tost', 'test', 'teat'],groups = [1, 2, 1, 2, 1]) == ['test', 'tast', 'tost', 'test', 'teat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tost', 'test', 'teat'],groups = [1, 2, 1, 2, 1]) == ['test', 'tast', 'tost', 'test', 'teat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaa', 'aaaba', 'aaaca', 'aaada'],groups = [1, 2, 1, 2]) == ['aaaaa', 'aaaba', 'aaaca', 'aaada']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaa', 'aaaba', 'aaaca', 'aaada'],groups = [1, 2, 1, 2]) == ['aaaaa', 'aaaba', 'aaaca', 'aaada']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'tat'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat', 'tat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'tat'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat', 'tat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'abcdf', 'abcgf', 'abchg', 'abchf'],groups = [1, 2, 3, 4, 3]) == ['abcde', 'abcdf', 'abcgf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'abcdf', 'abcgf', 'abchg', 'abchf'],groups = [1, 2, 3, 4, 3]) == ['abcde', 'abcdf', 'abcgf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'abcdf', 'abcef', 'abcag'],groups = [1, 2, 1, 2]) == ['abcde', 'abcdf', 'abcef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'abcdf', 'abcef', 'abcag'],groups = [1, 2, 1, 2]) == ['abcde', 'abcdf', 'abcef']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'appla', 'applb', 'applc'],groups = [1, 2, 2, 3, 3]) == ['apple', 'appla', 'applb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'appla', 'applb', 'applc'],groups = [1, 2, 2, 3, 3]) == ['apple', 'appla', 'applb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acc', 'bcd', 'bce', 'bde'],groups = [1, 2, 1, 2, 1]) == ['bcd', 'bce', 'bde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acc', 'bcd', 'bce', 'bde'],groups = [1, 2, 1, 2, 1]) == ['bcd', 'bce', 'bde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['start', 'starr', 'statr', 'strat', 'strot'],groups = [1, 2, 1, 2, 1]) == ['start', 'starr', 'statr']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['start', 'starr', 'statr', 'strat', 'strot'],groups = [1, 2, 1, 2, 1]) == ['start', 'starr', 'statr']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdg', 'abef'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdg', 'abef'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abef']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'baaa'],groups = [1, 2, 3, 4, 5]) == ['aaaa', 'aaab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'baaa'],groups = [1, 2, 3, 4, 5]) == ['aaaa', 'aaab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['kitten', 'sitten', 'bitten', 'bitter', 'bitter'],groups = [1, 2, 3, 4, 5]) == ['kitten', 'sitten', 'bitten', 'bitter']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['kitten', 'sitten', 'bitten', 'bitter', 'bitter'],groups = [1, 2, 3, 4, 5]) == ['kitten', 'sitten', 'bitten', 'bitter']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 1, 2]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 1, 2]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abcx'],groups = [1, 2, 3, 4, 5, 6]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abcx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abcx'],groups = [1, 2, 3, 4, 5, 6]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abcx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hxllo', 'hexlo', 'helxo'],groups = [1, 2, 3, 4]) == ['hello', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hxllo', 'hexlo', 'helxo'],groups = [1, 2, 3, 4]) == ['hello', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'abab', 'baba', 'bbaa'],groups = [1, 2, 1, 2]) == ['aabb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'abab', 'baba', 'bbaa'],groups = [1, 2, 1, 2]) == ['aabb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'abble', 'abble', 'abble'],groups = [1, 2, 3, 2]) == ['apple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'abble', 'abble', 'abble'],groups = [1, 2, 3, 2]) == ['apple']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci'],groups = [1, 2, 3, 4, 5, 6]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci'],groups = [1, 2, 3, 4, 5, 6]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'abe', 'bcd', 'bce'],groups = [1, 1, 2, 2, 3]) == ['abc', 'abe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'abe', 'bcd', 'bce'],groups = [1, 1, 2, 2, 3]) == ['abc', 'abe']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abcd', 'abcf'],groups = [1, 2, 1, 2]) == ['abcd', 'abcf', 'abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abcd', 'abcf'],groups = [1, 2, 1, 2]) == ['abcd', 'abcf', 'abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abcd', 'abdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abcd', 'abdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'acbd', 'abzd', 'abxc'],groups = [1, 2, 3, 4]) == ['abcd', 'abzd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'acbd', 'abzd', 'abxc'],groups = [1, 2, 3, 4]) == ['abcd', 'abzd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same', 'same'],groups = [1, 2, 3, 4]) == ['same']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same', 'same'],groups = [1, 2, 3, 4]) == ['same']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 1, 3]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 1, 3]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zeara', 'zeraa', 'zerar'],groups = [1, 2, 1, 2]) == ['zebra', 'zeara']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zeara', 'zeraa', 'zerar'],groups = [1, 2, 1, 2]) == ['zebra', 'zeara']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abdc', 'acdb', 'adcb', 'bacd', 'bcad', 'bdac', 'bdca'],groups = [1, 2, 1, 2, 1, 2, 1, 2]) == ['abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abdc', 'acdb', 'adcb', 'bacd', 'bcad', 'bdac', 'bdca'],groups = [1, 2, 1, 2, 1, 2, 1, 2]) == ['abcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apply', 'spoke', 'slope'],groups = [1, 2, 3, 4]) == ['apple', 'apply']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apply', 'spoke', 'slope'],groups = [1, 2, 3, 4]) == ['apple', 'apply']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdc', 'abcf'],groups = [1, 2, 1, 2]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdc', 'abcf'],groups = [1, 2, 1, 2]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo', 'hella', 'hillo'],groups = [1, 2, 1, 2, 1]) == ['hello', 'hallo', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo', 'hella', 'hillo'],groups = [1, 2, 1, 2, 1]) == ['hello', 'hallo', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hella', 'hell'],groups = [1, 2, 1, 2]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hella', 'hell'],groups = [1, 2, 1, 2]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tset', 'sett', 'stet'],groups = [1, 2, 1, 2]) == ['test']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tset', 'sett', 'stet'],groups = [1, 2, 1, 2]) == ['test']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'wore', 'core', 'cord', 'cred'],groups = [1, 2, 1, 2, 1, 2]) == ['word', 'worm', 'wore', 'core', 'cord']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'wore', 'core', 'cord', 'cred'],groups = [1, 2, 1, 2, 1, 2]) == ['word', 'worm', 'wore', 'core', 'cord']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zera', 'zeraa', 'zeara'],groups = [1, 2, 1, 2]) == ['zebra', 'zeara']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zera', 'zeraa', 'zeara'],groups = [1, 2, 1, 2]) == ['zebra', 'zeara']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zebra', 'zebra', 'zebra'],groups = [1, 2, 1, 2]) == ['zebra']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zebra', 'zebra', 'zebra'],groups = [1, 2, 1, 2]) == ['zebra']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abca'],groups = [1, 2, 3, 4]) == ['abcd', 'abce', 'abcf', 'abca']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abca'],groups = [1, 2, 3, 4]) == ['abcd', 'abce', 'abcf', 'abca']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'dig', 'dug', 'dot'],groups = [1, 2, 1, 2]) == ['dog', 'dig', 'dug']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'dig', 'dug', 'dot'],groups = [1, 2, 1, 2]) == ['dog', 'dig', 'dug']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abde', 'abdc'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abde', 'abdc'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 1, 3]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 1, 3]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdg', 'abeg'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdg', 'abeg'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd', 'ace', 'bce', 'abe', 'bde', 'cde', 'abc'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde', 'cde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd', 'ace', 'bce', 'abe', 'bde', 'cde', 'abc'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde', 'cde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four', 'five'],groups = [1, 2, 3, 4, 5]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four', 'five'],groups = [1, 2, 3, 4, 5]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wird', 'wurd', 'wurd', 'wurk'],groups = [1, 2, 1, 2, 3]) == ['word', 'wird', 'wurd', 'wurk']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wird', 'wurd', 'wurd', 'wurk'],groups = [1, 2, 1, 2, 3]) == ['word', 'wird', 'wurd', 'wurk']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sane', 'sane', 'same'],groups = [1, 2, 2, 3, 3]) == ['same', 'sane', 'same']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sane', 'sane', 'same'],groups = [1, 2, 2, 3, 3]) == ['same', 'sane', 'same']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc'],groups = [1, 2, 1, 2, 1, 2, 1]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc'],groups = [1, 2, 1, 2, 1, 2, 1]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abde', 'abce', 'abcd'],groups = [1, 2, 3, 4, 1]) == ['abcd', 'abcf', 'abce', 'abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abde', 'abce', 'abcd'],groups = [1, 2, 3, 4, 1]) == ['abcd', 'abcf', 'abce', 'abcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyza', 'xyzb', 'xyzc', 'xyzd'],groups = [1, 2, 3, 4]) == ['xyza', 'xyzb', 'xyzc', 'xyzd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyza', 'xyzb', 'xyzc', 'xyzd'],groups = [1, 2, 3, 4]) == ['xyza', 'xyzb', 'xyzc', 'xyzd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acd', 'bcd', 'bed'],groups = [1, 2, 1, 2]) == ['acd', 'bcd', 'bed']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acd', 'bcd', 'bed'],groups = [1, 2, 1, 2]) == ['acd', 'bcd', 'bed']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zera', 'zeraa', 'zerab', 'zercb'],groups = [1, 2, 1, 2, 1]) == ['zeraa', 'zerab', 'zercb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zera', 'zeraa', 'zerab', 'zercb'],groups = [1, 2, 1, 2, 1]) == ['zeraa', 'zerab', 'zercb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'kode', 'coke', 'cide'],groups = [1, 2, 1, 2]) == ['code', 'kode']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'kode', 'coke', 'cide'],groups = [1, 2, 1, 2]) == ['code', 'kode']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'bcd', 'bce'],groups = [1, 2, 1, 2]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'bcd', 'bce'],groups = [1, 2, 1, 2]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'worn', 'word'],groups = [1, 2, 1, 2]) == ['word', 'worm', 'worn', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'worn', 'word'],groups = [1, 2, 1, 2]) == ['word', 'worm', 'worn', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'phyton', 'phthon', 'pyhton'],groups = [1, 2, 1, 2]) == ['python']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'phyton', 'phthon', 'pyhton'],groups = [1, 2, 1, 2]) == ['python']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hillo', 'hella', 'hellb'],groups = [1, 2, 2, 3, 3]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hillo', 'hella', 'hellb'],groups = [1, 2, 2, 3, 3]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tost', 'test'],groups = [1, 2, 3, 4]) == ['test', 'tast', 'tost', 'test']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tost', 'test'],groups = [1, 2, 3, 4]) == ['test', 'tast', 'tost', 'test']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'aabb', 'abbb', 'babb', 'bbcc'],groups = [1, 2, 2, 3, 3]) == ['aabb', 'babb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'aabb', 'abbb', 'babb', 'bbcc'],groups = [1, 2, 2, 3, 3]) == ['aabb', 'babb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdf', 'acdf'],groups = [1, 2, 3, 1]) == ['abcd', 'abcf', 'abdf', 'acdf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdf', 'acdf'],groups = [1, 2, 3, 1]) == ['abcd', 'abcf', 'abdf', 'acdf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo', 'hella'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo', 'hella'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb'],groups = [1, 1, 2, 2]) == ['aaab', 'aabb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb'],groups = [1, 1, 2, 2]) == ['aaab', 'aabb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abdd', 'acdd', 'acdd', 'acde', 'acdf'],groups = [1, 2, 3, 1, 2, 3]) == ['abcd', 'abdd', 'acdd', 'acde', 'acdf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abdd', 'acdd', 'acdd', 'acde', 'acdf'],groups = [1, 2, 3, 1, 2, 3]) == ['abcd', 'abdd', 'acdd', 'acde', 'acdf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno'],groups = [1, 1, 1, 1, 1]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno'],groups = [1, 1, 1, 1, 1]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'],groups = [1, 2, 3, 4, 5, 6]) == ['aabb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'],groups = [1, 2, 3, 4, 5, 6]) == ['aabb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hillo', 'hollo'],groups = [1, 1, 2, 2]) == ['hello', 'hillo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hillo', 'hollo'],groups = [1, 1, 2, 2]) == ['hello', 'hillo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'aacc', 'aadd', 'aabb', 'aacc'],groups = [1, 2, 3, 1, 2]) == ['aabb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'aacc', 'aadd', 'aabb', 'aacc'],groups = [1, 2, 3, 1, 2]) == ['aabb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'acdf', 'bcdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'acdf', 'bcdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'thr', 'fou', 'fiv'],groups = [1, 2, 1, 2, 1]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'thr', 'fou', 'fiv'],groups = [1, 2, 1, 2, 1]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applb', 'applc', 'appld'],groups = [1, 2, 2, 2, 3]) == ['apple', 'appla', 'appld']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applb', 'applc', 'appld'],groups = [1, 2, 2, 2, 3]) == ['apple', 'appla', 'appld']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['graph', 'grapf', 'graph', 'grapt', 'grapt'],groups = [1, 2, 3, 2, 1]) == ['graph', 'grapf', 'graph', 'grapt']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['graph', 'grapf', 'graph', 'grapt', 'grapt'],groups = [1, 2, 3, 2, 1]) == ['graph', 'grapf', 'graph', 'grapt']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abcd'],groups = [1, 2, 1, 2]) == ['abcd', 'abce', 'abcf', 'abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abcd'],groups = [1, 2, 1, 2]) == ['abcd', 'abce', 'abcf', 'abcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaab', 'abab', 'abba', 'baaa'],groups = [1, 2, 3, 4]) == ['aaab', 'abab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaab', 'abab', 'abba', 'baaa'],groups = [1, 2, 3, 4]) == ['aaab', 'abab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo', 'hexxo'],groups = [1, 2, 2, 3, 3]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo', 'hexxo'],groups = [1, 2, 2, 3, 3]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'bce', 'bde', 'bdf'],groups = [1, 2, 2, 3, 4]) == ['bce', 'bde', 'bdf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'bce', 'bde', 'bdf'],groups = [1, 2, 2, 3, 4]) == ['bce', 'bde', 'bdf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abde', 'abce'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abce']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abde', 'abce'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abce']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abdg', 'abdh'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abdg', 'abdh'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'abe', 'ace', 'adf', 'aeg'],groups = [1, 2, 1, 2, 1, 2]) == ['abc', 'abd', 'abe', 'ace']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'abe', 'ace', 'adf', 'aeg'],groups = [1, 2, 1, 2, 1, 2]) == ['abc', 'abd', 'abe', 'ace']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'mat'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat', 'mat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'mat'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat', 'mat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apble', 'appla', 'applb', 'applc'],groups = [1, 2, 3, 2, 1]) == ['apple', 'appla', 'applb', 'applc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apble', 'appla', 'applb', 'applc'],groups = [1, 2, 3, 2, 1]) == ['apple', 'appla', 'applb', 'applc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa'],groups = [1, 2, 1, 2]) == ['aaaa', 'aaab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa'],groups = [1, 2, 1, 2]) == ['aaaa', 'aaab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abci', 'abcj'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf', 'abci', 'abcj']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abci', 'abcj'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf', 'abci', 'abcj']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo', 'hexxo'],groups = [1, 2, 3, 4, 5]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo', 'hexxo'],groups = [1, 2, 3, 4, 5]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'cap', 'car'],groups = [1, 2, 3, 4, 5]) == ['cat', 'bat', 'rat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'cap', 'car'],groups = [1, 2, 3, 4, 5]) == ['cat', 'bat', 'rat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'abaa', 'acaa', 'aada'],groups = [1, 1, 2, 2]) == ['aaaa', 'acaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'abaa', 'acaa', 'aada'],groups = [1, 1, 2, 2]) == ['aaaa', 'acaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'abble', 'abble', 'abble', 'abble'],groups = [1, 2, 1, 2, 1]) == ['apple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'abble', 'abble', 'abble', 'abble'],groups = [1, 2, 1, 2, 1]) == ['apple']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'zzzw', 'zzzx', 'zzzy'],groups = [1, 2, 3, 4]) == ['zzzz', 'zzzw', 'zzzx', 'zzzy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'zzzw', 'zzzx', 'zzzy'],groups = [1, 2, 3, 4]) == ['zzzz', 'zzzw', 'zzzx', 'zzzy']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcc', 'abcb', 'abca'],groups = [1, 2, 1, 2]) == ['abcd', 'abcc', 'abcb', 'abca']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcc', 'abcb', 'abca'],groups = [1, 2, 1, 2]) == ['abcd', 'abcc', 'abcb', 'abca']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'abaa', 'acaa', 'adab', 'adac'],groups = [1, 2, 3, 1, 2]) == ['aaaa', 'abaa', 'acaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'abaa', 'acaa', 'adab', 'adac'],groups = [1, 2, 3, 1, 2]) == ['aaaa', 'abaa', 'acaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylo', 'xyxo', 'xyxo', 'xylo', 'xylo'],groups = [1, 2, 3, 2, 1]) == ['xylo', 'xyxo', 'xylo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylo', 'xyxo', 'xyxo', 'xylo', 'xylo'],groups = [1, 2, 3, 2, 1]) == ['xylo', 'xyxo', 'xylo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaba', 'abaa', 'abba', 'acaa', 'acba'],groups = [1, 2, 1, 2, 1, 2]) == ['aaaa', 'aaba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaba', 'abaa', 'abba', 'acaa', 'acba'],groups = [1, 2, 1, 2, 1, 2]) == ['aaaa', 'aaba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'zzzy', 'zzzx', 'zzxw'],groups = [5, 4, 3, 2]) == ['zzzz', 'zzzy', 'zzzx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'zzzy', 'zzzx', 'zzxw'],groups = [5, 4, 3, 2]) == ['zzzz', 'zzzy', 'zzzx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abdc', 'acdb', 'adcb'],groups = [1, 2, 1, 2]) == ['abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abdc', 'acdb', 'adcb'],groups = [1, 2, 1, 2]) == ['abcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'aaaa'],groups = [1, 2, 1, 2, 1]) == ['aaaa', 'aaab', 'aaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'aaaa'],groups = [1, 2, 1, 2, 1]) == ['aaaa', 'aaab', 'aaaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hillo', 'hillo'],groups = [1, 2, 1, 3]) == ['hello', 'hallo', 'hillo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hillo', 'hillo'],groups = [1, 2, 1, 3]) == ['hello', 'hallo', 'hillo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'abxde', 'abxde', 'abcye'],groups = [1, 2, 2, 3]) == ['abcde', 'abxde']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'abxde', 'abxde', 'abcye'],groups = [1, 2, 2, 3]) == ['abcde', 'abxde']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'abaa', 'acaa', 'aada', 'aada', 'aadd', 'aadd', 'aade'],groups = [1, 2, 1, 2, 3, 3, 4, 4]) == ['aaaa', 'aada', 'aadd', 'aade']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'abaa', 'acaa', 'aada', 'aada', 'aadd', 'aadd', 'aade'],groups = [1, 2, 1, 2, 3, 3, 4, 4]) == ['aaaa', 'aada', 'aadd', 'aade']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'abble', 'abble'],groups = [1, 2, 3, 2]) == ['apple', 'appla']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'abble', 'abble'],groups = [1, 2, 3, 2]) == ['apple', 'appla']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo', 'hellu'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo', 'hellu'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tost', 'test', 'tast', 'tost', 'test'],groups = [1, 2, 1, 2, 1, 2, 1]) == ['test', 'tast', 'tost', 'test', 'tast', 'tost', 'test']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tost', 'test', 'tast', 'tost', 'test'],groups = [1, 2, 1, 2, 1, 2, 1]) == ['test', 'tast', 'tost', 'test', 'tast', 'tost', 'test']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'zzzy', 'zzzx', 'zzxw'],groups = [1, 2, 1, 2]) == ['zzzz', 'zzzy', 'zzzx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'zzzy', 'zzzx', 'zzxw'],groups = [1, 2, 1, 2]) == ['zzzz', 'zzzy', 'zzzx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apply', 'appla', 'applu'],groups = [1, 2, 3, 4]) == ['apple', 'apply', 'appla', 'applu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apply', 'appla', 'applu'],groups = [1, 2, 3, 4]) == ['apple', 'apply', 'appla', 'applu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'ward', 'wird', 'wrod', 'wore', 'core'],groups = [1, 2, 1, 2, 1, 2]) == ['word', 'ward', 'wird']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'ward', 'wird', 'wrod', 'wore', 'core'],groups = [1, 2, 1, 2, 1, 2]) == ['word', 'ward', 'wird']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'womb', 'womb'],groups = [1, 2, 1, 3]) == ['word', 'worm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'womb', 'womb'],groups = [1, 2, 1, 3]) == ['word', 'worm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'dot', 'lot', 'log', 'cog'],groups = [1, 2, 2, 3, 4]) == ['dog', 'log', 'cog']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'dot', 'lot', 'log', 'cog'],groups = [1, 2, 2, 3, 4]) == ['dog', 'log', 'cog']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'same']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'same']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd'],groups = [1, 2, 1, 2]) == ['abc', 'abd', 'acd', 'bcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd'],groups = [1, 2, 1, 2]) == ['abc', 'abd', 'acd', 'bcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],groups = [1, 2, 1]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],groups = [1, 2, 1]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 1, 2, 2]) == ['abc', 'acc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 1, 2, 2]) == ['abc', 'acc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'abc', 'abe'],groups = [1, 2, 3, 4]) == ['abc', 'abd', 'abc', 'abe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'abc', 'abe'],groups = [1, 2, 3, 4]) == ['abc', 'abd', 'abc', 'abe']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo', 'hellu'],groups = [1, 1, 2, 2]) == ['hello', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo', 'hellu'],groups = [1, 1, 2, 2]) == ['hello', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl'],groups = [1, 1, 1, 1]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl'],groups = [1, 1, 1, 1]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'abab', 'abba', 'bbaa', 'bbab', 'bbba', 'bbbb'],groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == ['aaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'abab', 'abba', 'bbaa', 'bbab', 'bbba', 'bbbb'],groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == ['aaaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'bcd', 'ace'],groups = [1, 2, 1, 2]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'bcd', 'ace'],groups = [1, 2, 1, 2]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['loop', 'loap', 'leep', 'leap'],groups = [1, 2, 3, 4]) == ['loop', 'loap', 'leap']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['loop', 'loap', 'leep', 'leap'],groups = [1, 2, 3, 4]) == ['loop', 'loap', 'leap']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'ward', 'wear', 'ware'],groups = [1, 2, 3, 2]) == ['word', 'ward']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'ward', 'wear', 'ware'],groups = [1, 2, 3, 2]) == ['word', 'ward']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abb'],groups = [1, 2, 3, 4, 5]) == ['aaa', 'aab', 'aac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abb'],groups = [1, 2, 3, 4, 5]) == ['aaa', 'aab', 'aac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fun', 'sun', 'tun', 'fum'],groups = [1, 2, 3, 4]) == ['fun', 'sun', 'tun']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fun', 'sun', 'tun', 'fum'],groups = [1, 2, 3, 4]) == ['fun', 'sun', 'tun']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdc'],groups = [1, 2, 1]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdc'],groups = [1, 2, 1]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'woro', 'work'],groups = [3, 3, 4]) == ['word', 'work']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'woro', 'work'],groups = [3, 3, 4]) == ['word', 'work']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tist', 'best'],groups = [1, 2, 3, 1]) == ['test', 'tast', 'tist']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tist', 'best'],groups = [1, 2, 3, 1]) == ['test', 'tast', 'tist']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'text', 'tast', 'tect'],groups = [1, 2, 1, 2]) == ['test', 'text']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'text', 'tast', 'tect'],groups = [1, 2, 1, 2]) == ['test', 'text']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [3, 3, 4, 4]) == ['apple', 'applb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [3, 3, 4, 4]) == ['apple', 'applb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zero', 'hero', 'hero', 'hero'],groups = [1, 2, 1, 2]) == ['zero', 'hero']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zero', 'hero', 'hero', 'hero'],groups = [1, 2, 1, 2]) == ['zero', 'hero']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 2, 3, 4]) == ['cat', 'bat', 'rat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 2, 3, 4]) == ['cat', 'bat', 'rat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abgd'],groups = [1, 2, 1]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abgd'],groups = [1, 2, 1]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'work', 'worm', 'worn'],groups = [1, 2, 1, 2]) == ['word', 'work', 'worm', 'worn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'work', 'worm', 'worn'],groups = [1, 2, 1, 2]) == ['word', 'work', 'worm', 'worn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 3, 4]) == ['word', 'wird', 'word', 'wird']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 3, 4]) == ['word', 'wird', 'word', 'wird']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zebra', 'zebra'],groups = [1, 2, 1]) == ['zebra']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zebra', 'zebra'],groups = [1, 2, 1]) == ['zebra']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hellp', 'hxllo'],groups = [5, 5, 6, 7]) == ['hello', 'hellp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hellp', 'hxllo'],groups = [5, 5, 6, 7]) == ['hello', 'hellp']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hella'],groups = [1, 2, 3]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hella'],groups = [1, 2, 3]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 1, 2, 2]) == ['hello', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 1, 2, 2]) == ['hello', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 1, 2]) == ['hello', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 1, 2]) == ['hello', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'dot', 'lot', 'log'],groups = [1, 2, 3, 4]) == ['dog', 'dot', 'lot', 'log']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'dot', 'lot', 'log'],groups = [1, 2, 3, 4]) == ['dog', 'dot', 'lot', 'log']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'text', 'tast', 'tuxt'],groups = [1, 1, 2, 2]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'text', 'tast', 'tuxt'],groups = [1, 1, 2, 2]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['star', 'tart', 'kart', 'tars'],groups = [1, 2, 3, 4]) == ['tart', 'kart']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['star', 'tart', 'kart', 'tars'],groups = [1, 2, 3, 4]) == ['tart', 'kart']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tiny', 'tint', 'tint', 'tank'],groups = [1, 2, 1, 2]) == ['tiny', 'tint']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tiny', 'tint', 'tint', 'tank'],groups = [1, 2, 1, 2]) == ['tiny', 'tint']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aba', 'aca', 'baa', 'bab', 'bac', 'caa', 'cab', 'cac'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == ['aaa', 'aab', 'aac', 'bac', 'cac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aba', 'aca', 'baa', 'bab', 'bac', 'caa', 'cab', 'cac'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == ['aaa', 'aab', 'aac', 'bac', 'cac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applu', 'appli'],groups = [1, 2, 1, 2]) == ['apple', 'appla', 'applu', 'appli']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applu', 'appli'],groups = [1, 2, 1, 2]) == ['apple', 'appla', 'applu', 'appli']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['java', 'lava', 'slava', 'flava'],groups = [1, 2, 3, 4]) == ['java', 'lava']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['java', 'lava', 'slava', 'flava'],groups = [1, 2, 3, 4]) == ['java', 'lava']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 1, 2]) == ['same', 'sane']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 1, 2]) == ['same', 'sane']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],groups = [1, 2, 3, 4, 5]) == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],groups = [1, 2, 3, 4, 5]) == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 1, 2, 2]) == ['hello', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 1, 2, 2]) == ['hello', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 2, 3]) == ['word', 'wird']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 2, 3]) == ['word', 'wird']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zyz', 'zxy', 'zyx'],groups = [1, 2, 3, 4]) == ['zzz', 'zyz', 'zyx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zyz', 'zxy', 'zyx'],groups = [1, 2, 3, 4]) == ['zzz', 'zyz', 'zyx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyx', 'yzz', 'zzy'],groups = [3, 2, 3, 2]) == ['xyz', 'xyx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyx', 'yzz', 'zzy'],groups = [3, 2, 3, 2]) == ['xyz', 'xyx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'text', 'tset', 'best'],groups = [1, 2, 3, 4]) == ['test', 'text']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'text', 'tset', 'best'],groups = [1, 2, 3, 4]) == ['test', 'text']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 3, 4]) == ['apple', 'appla', 'applb', 'applc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 3, 4]) == ['apple', 'appla', 'applb', 'applc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi'],groups = [1, 2, 3]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi'],groups = [1, 2, 3]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo', 'pxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo', 'pxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'kode', 'kode'],groups = [1, 2, 1]) == ['code', 'kode']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'kode', 'kode'],groups = [1, 2, 1]) == ['code', 'kode']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo', 'hellp'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo', 'hellp'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'west', 'lest'],groups = [1, 2, 1, 2]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'west', 'lest'],groups = [1, 2, 1, 2]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 1, 2, 2]) == ['cat', 'rat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 1, 2, 2]) == ['cat', 'rat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 1, 2]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 1, 2]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'dec'],groups = [1, 2, 3, 4]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'dec'],groups = [1, 2, 3, 4]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'fest', 'best'],groups = [1, 2, 1, 2]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'fest', 'best'],groups = [1, 2, 1, 2]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aba', 'baa', 'bbb'],groups = [1, 2, 3, 2, 1]) == ['aaa', 'aab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aba', 'baa', 'bbb'],groups = [1, 2, 3, 2, 1]) == ['aaa', 'aab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hellp', 'herlo'],groups = [1, 1, 2, 2]) == ['hello', 'hellp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hellp', 'herlo'],groups = [1, 1, 2, 2]) == ['hello', 'hellp']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tist'],groups = [1, 2, 3]) == ['test', 'tast', 'tist']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tist'],groups = [1, 2, 3]) == ['test', 'tast', 'tist']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 1, 1, 1]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 1, 1, 1]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa'],groups = [1, 2, 3, 4]) == ['aaaa', 'aaab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa'],groups = [1, 2, 3, 4]) == ['aaaa', 'aaab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 1, 2, 2]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 1, 2, 2]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hella'],groups = [1, 2, 1]) == ['hello', 'hallo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hella'],groups = [1, 2, 1]) == ['hello', 'hallo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tist', 'teat'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tist']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tist', 'teat'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tist']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tast'],groups = [1, 2, 1]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tast'],groups = [1, 2, 1]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc'],groups = [1, 2, 1]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc'],groups = [1, 2, 1]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc', 'acd'],groups = [1, 2, 3, 4]) == ['abc', 'abd', 'acd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc', 'acd'],groups = [1, 2, 3, 4]) == ['abc', 'abd', 'acd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abce'],groups = [1, 2, 3]) == ['abcd', 'abce']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abce'],groups = [1, 2, 3]) == ['abcd', 'abce']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apble', 'aagle', 'apgle', 'applu'],groups = [1, 2, 1, 2, 1]) == ['apple', 'apble']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apble', 'aagle', 'apgle', 'applu'],groups = [1, 2, 1, 2, 1]) == ['apple', 'apble']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hell'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hell'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 2, 3]) == ['hello', 'hella', 'hellu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 2, 3]) == ['hello', 'hella', 'hellu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 1, 2]) == ['same', 'sane']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 1, 2]) == ['same', 'sane']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 1, 2]) == ['apple', 'appla', 'applb', 'applc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 1, 2]) == ['apple', 'appla', 'applb', 'applc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'cide', 'codi', 'coie'],groups = [1, 1, 2, 2]) == ['code', 'codi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'cide', 'codi', 'coie'],groups = [1, 1, 2, 2]) == ['code', 'codi']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 2, 1]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 2, 1]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zoom', 'boom', 'boon', 'boom'],groups = [1, 2, 1, 3]) == ['zoom', 'boom', 'boon', 'boom']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zoom', 'boom', 'boon', 'boom'],groups = [1, 2, 1, 3]) == ['zoom', 'boom', 'boon', 'boom']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abef', 'abeg'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abef', 'abeg']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abef', 'abeg'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abef', 'abeg']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['keep', 'peek', 'peel'],groups = [1, 2, 1]) == ['peek', 'peel']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['keep', 'peek', 'peel'],groups = [1, 2, 1]) == ['peek', 'peel']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'worn'],groups = [1, 2, 3]) == ['word', 'worm', 'worn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'worn'],groups = [1, 2, 3]) == ['word', 'worm', 'worn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 2, 3]) == ['apple', 'appla', 'applc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 2, 3]) == ['apple', 'appla', 'applc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aad'],groups = [1, 2, 1, 2]) == ['aaa', 'aab', 'aac', 'aad']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aad'],groups = [1, 2, 1, 2]) == ['aaa', 'aab', 'aac', 'aad']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 1, 2, 3]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 1, 2, 3]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac'],groups = [1, 2, 3]) == ['aaa', 'aab', 'aac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac'],groups = [1, 2, 3]) == ['aaa', 'aab', 'aac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tist', 'tast'],groups = [1, 2, 3, 1]) == ['test', 'tast', 'tist', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tist', 'tast'],groups = [1, 2, 3, 1]) == ['test', 'tast', 'tist', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tekt'],groups = [1, 2, 3]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tekt'],groups = [1, 2, 3]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf'],groups = [1, 2, 3]) == ['abcd', 'abce', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf'],groups = [1, 2, 3]) == ['abcd', 'abce', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wore', 'word', 'worn'],groups = [1, 2, 3, 4]) == ['word', 'wore', 'word', 'worn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wore', 'word', 'worn'],groups = [1, 2, 3, 4]) == ['word', 'wore', 'word', 'worn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'thr'],groups = [1, 1, 1]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'thr'],groups = [1, 1, 1]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'coed', 'cdeo'],groups = [2, 2, 3]) == ['code']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'coed', 'cdeo'],groups = [2, 2, 3]) == ['code']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['loop', 'lopo', 'leep'],groups = [1, 2, 1]) == ['loop']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['loop', 'lopo', 'leep'],groups = [1, 2, 1]) == ['loop']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'safe'],groups = [1, 1, 2]) == ['same', 'safe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'safe'],groups = [1, 1, 2]) == ['same', 'safe']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apply', 'spoil', 'spied'],groups = [1, 1, 2, 2]) == ['apple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apply', 'spoil', 'spied'],groups = [1, 1, 2, 2]) == ['apple']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hxllo', 'pxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hxllo', 'pxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'text', 'tast', 'tast'],groups = [1, 2, 1, 3]) == ['test', 'text']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'text', 'tast', 'tast'],groups = [1, 2, 1, 3]) == ['test', 'text']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdf', 'abef'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abdf', 'abef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdf', 'abef'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abdf', 'abef']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'ton', 'oen'],groups = [1, 1, 2, 2]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'ton', 'oen'],groups = [1, 1, 2, 2]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wird', 'word', 'wond'],groups = [1, 1, 2, 2]) == ['wird', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wird', 'word', 'wond'],groups = [1, 1, 2, 2]) == ['wird', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'ttst'],groups = [1, 2, 3]) == ['test', 'tast', 'ttst']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'ttst'],groups = [1, 2, 3]) == ['test', 'tast', 'ttst']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac'],groups = [1, 2, 1]) == ['aaa', 'aab', 'aac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac'],groups = [1, 2, 1]) == ['aaa', 'aab', 'aac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'dot', 'lot', 'log'],groups = [1, 2, 1, 2]) == ['dog', 'dot', 'lot', 'log']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'dot', 'lot', 'log'],groups = [1, 2, 1, 2]) == ['dog', 'dot', 'lot', 'log']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'teat'],groups = [1, 2, 3]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'teat'],groups = [1, 2, 3]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'same', 'sane'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'same', 'sane']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'same', 'sane'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'same', 'sane']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'bpple', 'cppld'],groups = [1, 2, 1]) == ['apple', 'bpple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'bpple', 'cppld'],groups = [1, 2, 1]) == ['apple', 'bpple']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyx', 'xzx', 'xxz'],groups = [1, 1, 1, 1]) == ['xyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyx', 'xzx', 'xxz'],groups = [1, 1, 1, 1]) == ['xyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'bpple', 'appea'],groups = [1, 2, 3, 4]) == ['apple', 'appla', 'appea']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'bpple', 'appea'],groups = [1, 2, 3, 4]) == ['apple', 'appla', 'appea']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applp'],groups = [1, 2, 1]) == ['apple', 'appla', 'applp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applp'],groups = [1, 2, 1]) == ['apple', 'appla', 'applp']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abce', 'abdc'],groups = [1, 1, 2, 1]) == ['abcd', 'abce']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abce', 'abdc'],groups = [1, 1, 2, 1]) == ['abcd', 'abce']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sale', 'tale'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'sale', 'tale']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sale', 'tale'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'sale', 'tale']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tost', 'fest'],groups = [1, 2, 3, 4]) == ['test', 'tast', 'tost']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tost', 'fest'],groups = [1, 2, 3, 4]) == ['test', 'tast', 'tost']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 1, 2, 2]) == ['cat', 'rat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 1, 2, 2]) == ['cat', 'rat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 2, 3, 4]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 2, 3, 4]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 2, 3]) == ['hello', 'hxllo', 'pxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 2, 3]) == ['hello', 'hxllo', 'pxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 2, 3]) == ['same', 'sane', 'same']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 2, 3]) == ['same', 'sane', 'same']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'applu', 'applp'],groups = [1, 1, 2, 2]) == ['apple', 'applu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'applu', 'applp'],groups = [1, 1, 2, 2]) == ['apple', 'applu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'safe', 'same'],groups = [1, 2, 3, 1]) == ['same', 'sane', 'safe', 'same']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'safe', 'same'],groups = [1, 2, 3, 1]) == ['same', 'sane', 'safe', 'same']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyw', 'xzz', 'xyx'],groups = [1, 2, 1, 2]) == ['xyz', 'xyw']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyw', 'xzz', 'xyx'],groups = [1, 2, 1, 2]) == ['xyz', 'xyw']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'bat'],groups = [1, 2, 3]) == ['cat', 'bat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'bat'],groups = [1, 2, 3]) == ['cat', 'bat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'ward', 'cord', 'card'],groups = [1, 2, 3, 4]) == ['word', 'ward', 'card']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'ward', 'cord', 'card'],groups = [1, 2, 3, 4]) == ['word', 'ward', 'card']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sake'],groups = [1, 2, 1]) == ['same', 'sane', 'sake']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sake'],groups = [1, 2, 1]) == ['same', 'sane', 'sake']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc', 'aba'],groups = [1, 2, 3, 2]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc', 'aba'],groups = [1, 2, 3, 2]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'appla', 'abble', 'abble'],groups = [1, 2, 2, 3]) == ['apple', 'appla']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'appla', 'abble', 'abble'],groups = [1, 2, 2, 3]) == ['apple', 'appla']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'text', 'tast'],groups = [1, 2, 1]) == ['test', 'text']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'text', 'tast'],groups = [1, 2, 1]) == ['test', 'text']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdf'],groups = [1, 1, 2]) == ['abcf', 'abdf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdf'],groups = [1, 1, 2]) == ['abcf', 'abdf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'wirm', 'wirt'],groups = [1, 2, 1, 3]) == ['word', 'worm', 'wirm', 'wirt']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'wirm', 'wirt'],groups = [1, 2, 1, 3]) == ['word', 'worm', 'wirm', 'wirt']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'kode', 'cide', 'coke'],groups = [1, 2, 3, 4]) == ['code', 'kode']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'kode', 'cide', 'coke'],groups = [1, 2, 3, 4]) == ['code', 'kode']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'worn'],groups = [1, 2, 1]) == ['word', 'worm', 'worn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'worn'],groups = [1, 2, 1]) == ['word', 'worm', 'worn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyw', 'xzz', 'xyy'],groups = [2, 3, 2, 3]) == ['xyz', 'xyw']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyw', 'xzz', 'xyy'],groups = [2, 3, 2, 3]) == ['xyz', 'xyw']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyx', 'xyy', 'xyw'],groups = [1, 2, 3, 4]) == ['xyz', 'xyx', 'xyy', 'xyw']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyx', 'xyy', 'xyw'],groups = [1, 2, 3, 4]) == ['xyz', 'xyx', 'xyy', 'xyw']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 3, 4]) == ['same', 'tame', 'game']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 3, 4]) == ['same', 'tame', 'game']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tree', 'trex', 'trey', 'gree'],groups = [1, 2, 1, 2]) == ['tree', 'trex', 'trey']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tree', 'trex', 'trey', 'gree'],groups = [1, 2, 1, 2]) == ['tree', 'trex', 'trey']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 1, 2, 2]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 1, 2, 2]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tets', 'tast', 'tast'],groups = [1, 2, 2, 3]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tets', 'tast', 'tast'],groups = [1, 2, 2, 3]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdg'],groups = [1, 2, 3]) == ['abcd', 'abcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdg'],groups = [1, 2, 3]) == ['abcd', 'abcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo'],groups = [1, 2, 1]) == ['hello', 'hallo', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo'],groups = [1, 2, 1]) == ['hello', 'hallo', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde'],groups = [1, 1, 2]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde'],groups = [1, 1, 2]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'game', 'tame'],groups = [1, 2, 1, 2]) == ['same', 'sane']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'game', 'tame'],groups = [1, 2, 1, 2]) == ['same', 'sane']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'teat', 'teet'],groups = [1, 2, 3, 4]) == ['test', 'teat', 'teet']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'teat', 'teet'],groups = [1, 2, 3, 4]) == ['test', 'teat', 'teet']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc'],groups = [1, 2, 3]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc'],groups = [1, 2, 3]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'cide', 'kode', 'coda'],groups = [1, 2, 1, 2]) == ['code', 'cide']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'cide', 'kode', 'coda'],groups = [1, 2, 1, 2]) == ['code', 'cide']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'game'],groups = [1, 1, 2]) == ['same', 'game']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'game'],groups = [1, 1, 2]) == ['same', 'game']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [10, 20, 10, 30]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [10, 20, 10, 30]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 3, 4]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 3, 4]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hullo', 'hellp'],groups = [1, 2, 1, 3]) == ['hello', 'hallo', 'hullo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hullo', 'hellp'],groups = [1, 2, 1, 3]) == ['hello', 'hallo', 'hullo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['play', 'plby', 'plya', 'plax'],groups = [1, 1, 2, 2]) == ['play', 'plax']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['play', 'plby', 'plya', 'plax'],groups = [1, 1, 2, 2]) == ['play', 'plax']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tost', 'tett'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tost']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tost', 'tett'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tost']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sage', 'page'],groups = [1, 1, 2, 2]) == ['same', 'sage']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sage', 'page'],groups = [1, 1, 2, 2]) == ['same', 'sage']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'tast', 'tell', 'tall'],groups = [1, 2, 3, 4]) == ['test', 'tast']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'tast', 'tell', 'tall'],groups = [1, 2, 3, 4]) == ['test', 'tast']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'sale', 'male'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'sale', 'male']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'sale', 'male'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'sale', 'male']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdf', 'acdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abdf', 'acdf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdf', 'acdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abdf', 'acdf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apply', 'spork'],groups = [1, 2, 1]) == ['apple', 'apply']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apply', 'spork'],groups = [1, 2, 1]) == ['apple', 'apply']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'text', 'tast', 'best'],groups = [1, 2, 1, 3]) == ['test', 'text']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'text', 'tast', 'best'],groups = [1, 2, 1, 3]) == ['test', 'text']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 2, 3]) == ['hello', 'hallo', 'hxllo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 2, 3]) == ['hello', 'hallo', 'hxllo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'bcd', 'bce'],groups = [1, 2, 2, 3]) == ['abc', 'abd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'bcd', 'bce'],groups = [1, 2, 2, 3]) == ['abc', 'abd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],groups = [1, 2, 3]) == ['one']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],groups = [1, 2, 3]) == ['one']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'sane', 'safe', 'sale'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'safe', 'sale']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'sane', 'safe', 'sale'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'safe', 'sale']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'cog', 'rog'],groups = [1, 2, 3]) == ['dog', 'cog', 'rog']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'cog', 'rog'],groups = [1, 2, 3]) == ['dog', 'cog', 'rog']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['five', 'fife', 'five', 'five'],groups = [1, 2, 1, 2]) == ['five', 'fife', 'five']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['five', 'fife', 'five', 'five'],groups = [1, 2, 1, 2]) == ['five', 'fife', 'five']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'efg'],groups = [1, 1, 2, 2]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'efg'],groups = [1, 1, 2, 2]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'],groups = [1, 2, 3, 4, 5, 6, 7, 8]) == ['aaa', 'aab', 'abb', 'bbb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'],groups = [1, 2, 3, 4, 5, 6, 7, 8]) == ['aaa', 'aab', 'abb', 'bbb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zzy', 'zyy', 'yyy'],groups = [1, 2, 1, 2]) == ['zzz', 'zzy', 'zyy', 'yyy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zzy', 'zyy', 'yyy'],groups = [1, 2, 1, 2]) == ['zzz', 'zzy', 'zyy', 'yyy']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'worn', 'word'],groups = [1, 2, 1, 3]) == ['word', 'worm', 'worn', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'worn', 'word'],groups = [1, 2, 1, 3]) == ['word', 'worm', 'worn', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['code', 'mode', 'mroe'],groups = [1, 2, 1]) == ['code', 'mode']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['code', 'mode', 'mroe'],groups = [1, 2, 1]) == ['code', 'mode']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'worm', 'worn'],groups = [1, 1, 2]) == ['word', 'worn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'worm', 'worn'],groups = [1, 1, 2]) == ['word', 'worn']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apply', 'appla'],groups = [1, 1, 2]) == ['apple', 'appla']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apply', 'appla'],groups = [1, 1, 2]) == ['apple', 'appla']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 2, 3, 4]) == ['cat', 'bat', 'rat', 'hat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 2, 3, 4]) == ['cat', 'bat', 'rat', 'hat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde'],groups = [1, 1, 1]) == ['abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde'],groups = [1, 1, 1]) == ['abc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 1, 1, 2]) == ['cat', 'hat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 1, 1, 2]) == ['cat', 'hat']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wird', 'wordy'],groups = [1, 2, 3]) == ['word', 'wird']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wird', 'wordy'],groups = [1, 2, 3]) == ['word', 'wird']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['abc', 'bac', 'bca', 'cab', 'cba', 'acb'],groups = [1, 2, 1, 2, 1, 2]) == ['abc']
    assert candidate(words = ['same', 'sane', 'same'],groups = [1, 2, 1]) == ['same', 'sane', 'same']
    assert candidate(words = ['test', 'tast', 'best', 'rest'],groups = [1, 2, 2, 3]) == ['test', 'best', 'rest']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 2, 2, 3]) == ['hello', 'hallo']
    assert candidate(words = ['abcd', 'abcf', 'abgf', 'abgh'],groups = [1, 2, 2, 3]) == ['abcd', 'abcf']
    assert candidate(words = ['hello', 'hallo', 'hbllo', 'hillo'],groups = [1, 1, 2, 3]) == ['hello', 'hbllo', 'hillo']
    assert candidate(words = ['bab', 'dab', 'cab'],groups = [1, 2, 2]) == ['bab', 'dab']
    assert candidate(words = ['word', 'worm', 'wore', 'core'],groups = [1, 2, 1, 2]) == ['word', 'worm', 'wore', 'core']
    assert candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 2, 3]) == ['same', 'tame', 'game']
    assert candidate(words = ['a', 'b', 'c', 'd'],groups = [1, 2, 3, 4]) == ['a', 'b', 'c', 'd']
    assert candidate(words = ['apple', 'appla', 'appel'],groups = [1, 2, 1]) == ['apple', 'appla']
    assert candidate(words = ['a', 'ab', 'abc', 'abcd'],groups = [1, 2, 3, 4]) == ['a']
    assert candidate(words = ['zzz', 'zzx', 'zzw', 'zzv'],groups = [1, 2, 3, 4]) == ['zzz', 'zzx', 'zzw', 'zzv']
    assert candidate(words = ['test', 'tast', 'tost', 'test'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tost', 'test']
    assert candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 2, 3, 4]) == ['abc']
    assert candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 2, 2, 3]) == ['one']
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl'],groups = [1, 1, 2, 2]) == ['abc']
    assert candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 1, 2]) == ['word', 'wird', 'word', 'wird']
    assert candidate(words = ['abc', 'abb', 'aba', 'aaa', 'aab'],groups = [1, 2, 3, 4, 5]) == ['abc', 'abb', 'aba', 'aaa', 'aab']
    assert candidate(words = ['aabb', 'abab', 'abba', 'baab'],groups = [1, 2, 1, 2]) == ['aabb']
    assert candidate(words = ['aabb', 'abab', 'babb', 'baab'],groups = [1, 2, 1, 2]) == ['babb', 'baab']
    assert candidate(words = ['cat', 'cot', 'dog', 'dot', 'log'],groups = [1, 2, 1, 2, 3]) == ['cat', 'cot']
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],groups = [1, 2, 1, 2, 1, 2]) == ['abc']
    assert candidate(words = ['xyz', 'xyw', 'xyv', 'xyu'],groups = [1, 2, 3, 4]) == ['xyz', 'xyw', 'xyv', 'xyu']
    assert candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb'],groups = [1, 2, 3, 4, 5]) == ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']
    assert candidate(words = ['abc', 'bac', 'cab', 'bca', 'acb', 'cba'],groups = [1, 2, 3, 1, 2, 3]) == ['abc']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abcg'],groups = [1, 2, 3, 4]) == ['abcd', 'abce', 'abcf', 'abcg']
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd', 'ace'],groups = [1, 2, 1, 2, 1]) == ['abc', 'abd', 'acd', 'bcd']
    assert candidate(words = ['abcd', 'abcf', 'abdf', 'abef', 'acdf', 'acef', 'bcdf', 'bcef'],groups = [1, 2, 1, 2, 1, 2, 1, 2]) == ['abcd', 'abcf', 'abdf', 'abef']
    assert candidate(words = ['code', 'codd', 'cods', 'coex', 'coey'],groups = [1, 2, 2, 3, 3]) == ['code', 'codd']
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg'],groups = [1, 2, 3, 4, 5]) == ['abc']
    assert candidate(words = ['apple', 'apples', 'appl', 'app'],groups = [1, 2, 3, 4]) == ['apple']
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    assert candidate(words = ['same', 'sane', 'sate', 'site'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'sate', 'site']
    assert candidate(words = ['abcde', 'abfde', 'abcfe', 'abcef'],groups = [1, 2, 3, 4]) == ['abcde', 'abfde']
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde'],groups = [1, 2, 1, 2, 1, 2]) == ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde']
    assert candidate(words = ['mnop', 'mnoq', 'mnrp', 'mnsp', 'mntp'],groups = [1, 2, 3, 2, 1]) == ['mnop', 'mnrp', 'mnsp', 'mntp']
    assert candidate(words = ['apple', 'apply', 'appla', 'appla'],groups = [1, 2, 1, 3]) == ['apple', 'apply', 'appla']
    assert candidate(words = ['aaaa', 'abaa', 'acaa', 'aada', 'aada', 'aadd'],groups = [1, 2, 3, 1, 2, 3]) == ['aaaa', 'abaa', 'acaa']
    assert candidate(words = ['dog', 'cog', 'dag', 'dog', 'dig'],groups = [1, 2, 1, 2, 1]) == ['dag', 'dog', 'dig']
    assert candidate(words = ['word', 'worm', 'wirm', 'wirm', 'wirn'],groups = [1, 2, 3, 4, 5]) == ['word', 'worm', 'wirm', 'wirn']
    assert candidate(words = ['test', 'tast', 'tost', 'test', 'teat'],groups = [1, 2, 1, 2, 1]) == ['test', 'tast', 'tost', 'test', 'teat']
    assert candidate(words = ['aaaaa', 'aaaba', 'aaaca', 'aaada'],groups = [1, 2, 1, 2]) == ['aaaaa', 'aaaba', 'aaaca', 'aaada']
    assert candidate(words = ['cat', 'bat', 'rat', 'tat'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat', 'tat']
    assert candidate(words = ['abcde', 'abcdf', 'abcgf', 'abchg', 'abchf'],groups = [1, 2, 3, 4, 3]) == ['abcde', 'abcdf', 'abcgf']
    assert candidate(words = ['abcde', 'abcdf', 'abcef', 'abcag'],groups = [1, 2, 1, 2]) == ['abcde', 'abcdf', 'abcef']
    assert candidate(words = ['apple', 'appla', 'appla', 'applb', 'applc'],groups = [1, 2, 2, 3, 3]) == ['apple', 'appla', 'applb']
    assert candidate(words = ['abc', 'acc', 'bcd', 'bce', 'bde'],groups = [1, 2, 1, 2, 1]) == ['bcd', 'bce', 'bde']
    assert candidate(words = ['start', 'starr', 'statr', 'strat', 'strot'],groups = [1, 2, 1, 2, 1]) == ['start', 'starr', 'statr']
    assert candidate(words = ['abcd', 'abcf', 'abdg', 'abef'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abef']
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'baaa'],groups = [1, 2, 3, 4, 5]) == ['aaaa', 'aaab']
    assert candidate(words = ['kitten', 'sitten', 'bitten', 'bitter', 'bitter'],groups = [1, 2, 3, 4, 5]) == ['kitten', 'sitten', 'bitten', 'bitter']
    assert candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 1, 2]) == ['hello', 'hallo']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abcx'],groups = [1, 2, 3, 4, 5, 6]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abcx']
    assert candidate(words = ['hello', 'hxllo', 'hexlo', 'helxo'],groups = [1, 2, 3, 4]) == ['hello', 'hxllo']
    assert candidate(words = ['aabb', 'abab', 'baba', 'bbaa'],groups = [1, 2, 1, 2]) == ['aabb']
    assert candidate(words = ['apple', 'abble', 'abble', 'abble'],groups = [1, 2, 3, 2]) == ['apple']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci'],groups = [1, 2, 3, 4, 5, 6]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci']
    assert candidate(words = ['abc', 'abd', 'abe', 'bcd', 'bce'],groups = [1, 1, 2, 2, 3]) == ['abc', 'abe']
    assert candidate(words = ['abcd', 'abcf', 'abcd', 'abcf'],groups = [1, 2, 1, 2]) == ['abcd', 'abcf', 'abcd', 'abcf']
    assert candidate(words = ['abcd', 'abcf', 'abcd', 'abdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abcd']
    assert candidate(words = ['abcd', 'acbd', 'abzd', 'abxc'],groups = [1, 2, 3, 4]) == ['abcd', 'abzd']
    assert candidate(words = ['same', 'same', 'same', 'same'],groups = [1, 2, 3, 4]) == ['same']
    assert candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 1, 3]) == ['abc', 'abd']
    assert candidate(words = ['zebra', 'zeara', 'zeraa', 'zerar'],groups = [1, 2, 1, 2]) == ['zebra', 'zeara']
    assert candidate(words = ['abcd', 'abdc', 'acdb', 'adcb', 'bacd', 'bcad', 'bdac', 'bdca'],groups = [1, 2, 1, 2, 1, 2, 1, 2]) == ['abcd']
    assert candidate(words = ['apple', 'apply', 'spoke', 'slope'],groups = [1, 2, 3, 4]) == ['apple', 'apply']
    assert candidate(words = ['abcd', 'abcf', 'abdc', 'abcf'],groups = [1, 2, 1, 2]) == ['abcd', 'abcf']
    assert candidate(words = ['hello', 'hallo', 'hullo', 'hella', 'hillo'],groups = [1, 2, 1, 2, 1]) == ['hello', 'hallo', 'hullo']
    assert candidate(words = ['hello', 'hallo', 'hella', 'hell'],groups = [1, 2, 1, 2]) == ['hello', 'hallo']
    assert candidate(words = ['test', 'tset', 'sett', 'stet'],groups = [1, 2, 1, 2]) == ['test']
    assert candidate(words = ['word', 'worm', 'wore', 'core', 'cord', 'cred'],groups = [1, 2, 1, 2, 1, 2]) == ['word', 'worm', 'wore', 'core', 'cord']
    assert candidate(words = ['zebra', 'zera', 'zeraa', 'zeara'],groups = [1, 2, 1, 2]) == ['zebra', 'zeara']
    assert candidate(words = ['zebra', 'zebra', 'zebra', 'zebra'],groups = [1, 2, 1, 2]) == ['zebra']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abca'],groups = [1, 2, 3, 4]) == ['abcd', 'abce', 'abcf', 'abca']
    assert candidate(words = ['dog', 'dig', 'dug', 'dot'],groups = [1, 2, 1, 2]) == ['dog', 'dig', 'dug']
    assert candidate(words = ['abcd', 'abcf', 'abde', 'abdc'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']
    assert candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 1, 3]) == ['hello', 'hallo']
    assert candidate(words = ['abcd', 'abcf', 'abdg', 'abeg'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd', 'ace', 'bce', 'abe', 'bde', 'cde', 'abc'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['abc', 'abd', 'acd', 'bcd', 'bce', 'bde', 'cde']
    assert candidate(words = ['one', 'two', 'three', 'four', 'five'],groups = [1, 2, 3, 4, 5]) == ['one']
    assert candidate(words = ['word', 'wird', 'wurd', 'wurd', 'wurk'],groups = [1, 2, 1, 2, 3]) == ['word', 'wird', 'wurd', 'wurk']
    assert candidate(words = ['same', 'sane', 'sane', 'sane', 'same'],groups = [1, 2, 2, 3, 3]) == ['same', 'sane', 'same']
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc'],groups = [1, 2, 1, 2, 1, 2, 1]) == ['abc']
    assert candidate(words = ['abcd', 'abcf', 'abde', 'abce', 'abcd'],groups = [1, 2, 3, 4, 1]) == ['abcd', 'abcf', 'abce', 'abcd']
    assert candidate(words = ['xyza', 'xyzb', 'xyzc', 'xyzd'],groups = [1, 2, 3, 4]) == ['xyza', 'xyzb', 'xyzc', 'xyzd']
    assert candidate(words = ['abc', 'acd', 'bcd', 'bed'],groups = [1, 2, 1, 2]) == ['acd', 'bcd', 'bed']
    assert candidate(words = ['zebra', 'zera', 'zeraa', 'zerab', 'zercb'],groups = [1, 2, 1, 2, 1]) == ['zeraa', 'zerab', 'zercb']
    assert candidate(words = ['code', 'kode', 'coke', 'cide'],groups = [1, 2, 1, 2]) == ['code', 'kode']
    assert candidate(words = ['abc', 'abd', 'bcd', 'bce'],groups = [1, 2, 1, 2]) == ['abc', 'abd']
    assert candidate(words = ['word', 'worm', 'worn', 'word'],groups = [1, 2, 1, 2]) == ['word', 'worm', 'worn', 'word']
    assert candidate(words = ['python', 'phyton', 'phthon', 'pyhton'],groups = [1, 2, 1, 2]) == ['python']
    assert candidate(words = ['hello', 'hallo', 'hillo', 'hella', 'hellb'],groups = [1, 2, 2, 3, 3]) == ['hello', 'hallo']
    assert candidate(words = ['test', 'tast', 'tost', 'test'],groups = [1, 2, 3, 4]) == ['test', 'tast', 'tost', 'test']
    assert candidate(words = ['abc', 'aabb', 'abbb', 'babb', 'bbcc'],groups = [1, 2, 2, 3, 3]) == ['aabb', 'babb']
    assert candidate(words = ['abcd', 'abcf', 'abdf', 'acdf'],groups = [1, 2, 3, 1]) == ['abcd', 'abcf', 'abdf', 'acdf']
    assert candidate(words = ['hello', 'hallo', 'hullo', 'hella'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hullo']
    assert candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb'],groups = [1, 1, 2, 2]) == ['aaab', 'aabb']
    assert candidate(words = ['abcd', 'abdd', 'acdd', 'acdd', 'acde', 'acdf'],groups = [1, 2, 3, 1, 2, 3]) == ['abcd', 'abdd', 'acdd', 'acde', 'acdf']
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno'],groups = [1, 1, 1, 1, 1]) == ['abc']
    assert candidate(words = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'],groups = [1, 2, 3, 4, 5, 6]) == ['aabb']
    assert candidate(words = ['hello', 'hallo', 'hillo', 'hollo'],groups = [1, 1, 2, 2]) == ['hello', 'hillo']
    assert candidate(words = ['aabb', 'aacc', 'aadd', 'aabb', 'aacc'],groups = [1, 2, 3, 1, 2]) == ['aabb']
    assert candidate(words = ['abcd', 'abcf', 'acdf', 'bcdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf']
    assert candidate(words = ['one', 'two', 'thr', 'fou', 'fiv'],groups = [1, 2, 1, 2, 1]) == ['one']
    assert candidate(words = ['apple', 'appla', 'applb', 'applc', 'appld'],groups = [1, 2, 2, 2, 3]) == ['apple', 'appla', 'appld']
    assert candidate(words = ['graph', 'grapf', 'graph', 'grapt', 'grapt'],groups = [1, 2, 3, 2, 1]) == ['graph', 'grapf', 'graph', 'grapt']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abcd'],groups = [1, 2, 1, 2]) == ['abcd', 'abce', 'abcf', 'abcd']
    assert candidate(words = ['aaab', 'abab', 'abba', 'baaa'],groups = [1, 2, 3, 4]) == ['aaab', 'abab']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo', 'hexxo'],groups = [1, 2, 2, 3, 3]) == ['hello', 'hallo']
    assert candidate(words = ['abc', 'bcd', 'bce', 'bde', 'bdf'],groups = [1, 2, 2, 3, 4]) == ['bce', 'bde', 'bdf']
    assert candidate(words = ['abcd', 'abcf', 'abde', 'abce'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abce']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abcg', 'abch'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf', 'abcg', 'abch']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abdg', 'abdh'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf']
    assert candidate(words = ['abc', 'abd', 'abe', 'ace', 'adf', 'aeg'],groups = [1, 2, 1, 2, 1, 2]) == ['abc', 'abd', 'abe', 'ace']
    assert candidate(words = ['cat', 'bat', 'rat', 'mat'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat', 'mat']
    assert candidate(words = ['apple', 'apble', 'appla', 'applb', 'applc'],groups = [1, 2, 3, 2, 1]) == ['apple', 'appla', 'applb', 'applc']
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa'],groups = [1, 2, 1, 2]) == ['aaaa', 'aaab']
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abci', 'abcj'],groups = [1, 2, 3, 4, 5]) == ['abcd', 'abce', 'abcf', 'abci', 'abcj']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo', 'hexxo'],groups = [1, 2, 3, 4, 5]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['cat', 'bat', 'rat', 'cap', 'car'],groups = [1, 2, 3, 4, 5]) == ['cat', 'bat', 'rat']
    assert candidate(words = ['aaaa', 'abaa', 'acaa', 'aada'],groups = [1, 1, 2, 2]) == ['aaaa', 'acaa']
    assert candidate(words = ['apple', 'abble', 'abble', 'abble', 'abble'],groups = [1, 2, 1, 2, 1]) == ['apple']
    assert candidate(words = ['zzzz', 'zzzw', 'zzzx', 'zzzy'],groups = [1, 2, 3, 4]) == ['zzzz', 'zzzw', 'zzzx', 'zzzy']
    assert candidate(words = ['abcd', 'abcc', 'abcb', 'abca'],groups = [1, 2, 1, 2]) == ['abcd', 'abcc', 'abcb', 'abca']
    assert candidate(words = ['aaaa', 'abaa', 'acaa', 'adab', 'adac'],groups = [1, 2, 3, 1, 2]) == ['aaaa', 'abaa', 'acaa']
    assert candidate(words = ['xylo', 'xyxo', 'xyxo', 'xylo', 'xylo'],groups = [1, 2, 3, 2, 1]) == ['xylo', 'xyxo', 'xylo']
    assert candidate(words = ['aaaa', 'aaba', 'abaa', 'abba', 'acaa', 'acba'],groups = [1, 2, 1, 2, 1, 2]) == ['aaaa', 'aaba']
    assert candidate(words = ['zzzz', 'zzzy', 'zzzx', 'zzxw'],groups = [5, 4, 3, 2]) == ['zzzz', 'zzzy', 'zzzx']
    assert candidate(words = ['abcd', 'abdc', 'acdb', 'adcb'],groups = [1, 2, 1, 2]) == ['abcd']
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'aaaa'],groups = [1, 2, 1, 2, 1]) == ['aaaa', 'aaab', 'aaaa']
    assert candidate(words = ['hello', 'hallo', 'hillo', 'hillo'],groups = [1, 2, 1, 3]) == ['hello', 'hallo', 'hillo']
    assert candidate(words = ['abcde', 'abxde', 'abxde', 'abcye'],groups = [1, 2, 2, 3]) == ['abcde', 'abxde']
    assert candidate(words = ['aaaa', 'abaa', 'acaa', 'aada', 'aada', 'aadd', 'aadd', 'aade'],groups = [1, 2, 1, 2, 3, 3, 4, 4]) == ['aaaa', 'aada', 'aadd', 'aade']
    assert candidate(words = ['apple', 'appla', 'abble', 'abble'],groups = [1, 2, 3, 2]) == ['apple', 'appla']
    assert candidate(words = ['hello', 'hallo', 'hullo', 'hellu'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hullo']
    assert candidate(words = ['test', 'tast', 'tost', 'test', 'tast', 'tost', 'test'],groups = [1, 2, 1, 2, 1, 2, 1]) == ['test', 'tast', 'tost', 'test', 'tast', 'tost', 'test']
    assert candidate(words = ['zzzz', 'zzzy', 'zzzx', 'zzxw'],groups = [1, 2, 1, 2]) == ['zzzz', 'zzzy', 'zzzx']
    assert candidate(words = ['apple', 'apply', 'appla', 'applu'],groups = [1, 2, 3, 4]) == ['apple', 'apply', 'appla', 'applu']
    assert candidate(words = ['word', 'ward', 'wird', 'wrod', 'wore', 'core'],groups = [1, 2, 1, 2, 1, 2]) == ['word', 'ward', 'wird']
    assert candidate(words = ['word', 'worm', 'womb', 'womb'],groups = [1, 2, 1, 3]) == ['word', 'worm']
    assert candidate(words = ['dog', 'dot', 'lot', 'log', 'cog'],groups = [1, 2, 2, 3, 4]) == ['dog', 'log', 'cog']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'same']
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd'],groups = [1, 2, 1, 2]) == ['abc', 'abd', 'acd', 'bcd']
    assert candidate(words = ['one', 'two', 'three'],groups = [1, 2, 1]) == ['one']
    assert candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 1, 2, 2]) == ['abc', 'acc']
    assert candidate(words = ['abc', 'abd', 'abc', 'abe'],groups = [1, 2, 3, 4]) == ['abc', 'abd', 'abc', 'abe']
    assert candidate(words = ['hello', 'hallo', 'hullo', 'hellu'],groups = [1, 1, 2, 2]) == ['hello', 'hullo']
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl'],groups = [1, 1, 1, 1]) == ['abc']
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'abab', 'abba', 'bbaa', 'bbab', 'bbba', 'bbbb'],groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == ['aaaa']
    assert candidate(words = ['abc', 'abd', 'bcd', 'ace'],groups = [1, 2, 1, 2]) == ['abc', 'abd']
    assert candidate(words = ['loop', 'loap', 'leep', 'leap'],groups = [1, 2, 3, 4]) == ['loop', 'loap', 'leap']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['word', 'ward', 'wear', 'ware'],groups = [1, 2, 3, 2]) == ['word', 'ward']
    assert candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abb'],groups = [1, 2, 3, 4, 5]) == ['aaa', 'aab', 'aac']
    assert candidate(words = ['fun', 'sun', 'tun', 'fum'],groups = [1, 2, 3, 4]) == ['fun', 'sun', 'tun']
    assert candidate(words = ['abcd', 'abcf', 'abdc'],groups = [1, 2, 1]) == ['abcd', 'abcf']
    assert candidate(words = ['word', 'woro', 'work'],groups = [3, 3, 4]) == ['word', 'work']
    assert candidate(words = ['test', 'tast', 'tist', 'best'],groups = [1, 2, 3, 1]) == ['test', 'tast', 'tist']
    assert candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 2, 1, 2]) == ['cat', 'bat', 'rat']
    assert candidate(words = ['test', 'text', 'tast', 'tect'],groups = [1, 2, 1, 2]) == ['test', 'text']
    assert candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [3, 3, 4, 4]) == ['apple', 'applb']
    assert candidate(words = ['zero', 'hero', 'hero', 'hero'],groups = [1, 2, 1, 2]) == ['zero', 'hero']
    assert candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 2, 3, 4]) == ['cat', 'bat', 'rat']
    assert candidate(words = ['abcd', 'abcf', 'abgd'],groups = [1, 2, 1]) == ['abcd', 'abcf']
    assert candidate(words = ['word', 'work', 'worm', 'worn'],groups = [1, 2, 1, 2]) == ['word', 'work', 'worm', 'worn']
    assert candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 3, 4]) == ['word', 'wird', 'word', 'wird']
    assert candidate(words = ['zebra', 'zebra', 'zebra'],groups = [1, 2, 1]) == ['zebra']
    assert candidate(words = ['hello', 'hallo', 'hellp', 'hxllo'],groups = [5, 5, 6, 7]) == ['hello', 'hellp']
    assert candidate(words = ['hello', 'hallo', 'hella'],groups = [1, 2, 3]) == ['hello', 'hallo']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [1, 1, 2, 2]) == ['hello', 'hxllo']
    assert candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 1, 2]) == ['hello', 'hxllo']
    assert candidate(words = ['dog', 'dot', 'lot', 'log'],groups = [1, 2, 3, 4]) == ['dog', 'dot', 'lot', 'log']
    assert candidate(words = ['test', 'text', 'tast', 'tuxt'],groups = [1, 1, 2, 2]) == ['test', 'tast']
    assert candidate(words = ['star', 'tart', 'kart', 'tars'],groups = [1, 2, 3, 4]) == ['tart', 'kart']
    assert candidate(words = ['tiny', 'tint', 'tint', 'tank'],groups = [1, 2, 1, 2]) == ['tiny', 'tint']
    assert candidate(words = ['aaa', 'aab', 'aac', 'aba', 'aca', 'baa', 'bab', 'bac', 'caa', 'cab', 'cac'],groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == ['aaa', 'aab', 'aac', 'bac', 'cac']
    assert candidate(words = ['apple', 'appla', 'applu', 'appli'],groups = [1, 2, 1, 2]) == ['apple', 'appla', 'applu', 'appli']
    assert candidate(words = ['java', 'lava', 'slava', 'flava'],groups = [1, 2, 3, 4]) == ['java', 'lava']
    assert candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 1, 2]) == ['same', 'sane']
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],groups = [1, 2, 3, 4, 5]) == ['a']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 1, 2, 2]) == ['hello', 'hxllo']
    assert candidate(words = ['word', 'wird', 'word', 'wird'],groups = [1, 2, 2, 3]) == ['word', 'wird']
    assert candidate(words = ['zzz', 'zyz', 'zxy', 'zyx'],groups = [1, 2, 3, 4]) == ['zzz', 'zyz', 'zyx']
    assert candidate(words = ['xyz', 'xyx', 'yzz', 'zzy'],groups = [3, 2, 3, 2]) == ['xyz', 'xyx']
    assert candidate(words = ['test', 'text', 'tset', 'best'],groups = [1, 2, 3, 4]) == ['test', 'text']
    assert candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 3, 4]) == ['apple', 'appla', 'applb', 'applc']
    assert candidate(words = ['abc', 'def', 'ghi'],groups = [1, 2, 3]) == ['abc']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo', 'pxllo']
    assert candidate(words = ['code', 'kode', 'kode'],groups = [1, 2, 1]) == ['code', 'kode']
    assert candidate(words = ['hello', 'hallo', 'hullo', 'hellp'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hullo']
    assert candidate(words = ['test', 'tast', 'west', 'lest'],groups = [1, 2, 1, 2]) == ['test', 'tast']
    assert candidate(words = ['cat', 'bat', 'rat', 'car'],groups = [1, 1, 2, 2]) == ['cat', 'rat']
    assert candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 1, 2]) == ['abc', 'abd']
    assert candidate(words = ['abc', 'bcd', 'cde', 'dec'],groups = [1, 2, 3, 4]) == ['abc']
    assert candidate(words = ['test', 'tast', 'fest', 'best'],groups = [1, 2, 1, 2]) == ['test', 'tast']
    assert candidate(words = ['aaa', 'aab', 'aba', 'baa', 'bbb'],groups = [1, 2, 3, 2, 1]) == ['aaa', 'aab']
    assert candidate(words = ['hello', 'hallo', 'hellp', 'herlo'],groups = [1, 1, 2, 2]) == ['hello', 'hellp']
    assert candidate(words = ['test', 'tast', 'tist'],groups = [1, 2, 3]) == ['test', 'tast', 'tist']
    assert candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 1, 1, 1]) == ['one']
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa'],groups = [1, 2, 3, 4]) == ['aaaa', 'aaab']
    assert candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 1, 2, 2]) == ['one']
    assert candidate(words = ['hello', 'hallo', 'hella'],groups = [1, 2, 1]) == ['hello', 'hallo']
    assert candidate(words = ['test', 'tast', 'tist', 'teat'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tist']
    assert candidate(words = ['test', 'tast', 'tast'],groups = [1, 2, 1]) == ['test', 'tast']
    assert candidate(words = ['abc', 'abd', 'acc'],groups = [1, 2, 1]) == ['abc', 'abd']
    assert candidate(words = ['abc', 'abd', 'acc', 'acd'],groups = [1, 2, 3, 4]) == ['abc', 'abd', 'acd']
    assert candidate(words = ['abc', 'abcd', 'abce'],groups = [1, 2, 3]) == ['abcd', 'abce']
    assert candidate(words = ['apple', 'apble', 'aagle', 'apgle', 'applu'],groups = [1, 2, 1, 2, 1]) == ['apple', 'apble']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hell'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['hello', 'hallo', 'hella', 'hellu'],groups = [1, 2, 2, 3]) == ['hello', 'hella', 'hellu']
    assert candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 1, 2]) == ['same', 'sane']
    assert candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 1, 2]) == ['apple', 'appla', 'applb', 'applc']
    assert candidate(words = ['code', 'cide', 'codi', 'coie'],groups = [1, 1, 2, 2]) == ['code', 'codi']
    assert candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 2, 1]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['zoom', 'boom', 'boon', 'boom'],groups = [1, 2, 1, 3]) == ['zoom', 'boom', 'boon', 'boom']
    assert candidate(words = ['abcd', 'abcf', 'abef', 'abeg'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abef', 'abeg']
    assert candidate(words = ['keep', 'peek', 'peel'],groups = [1, 2, 1]) == ['peek', 'peel']
    assert candidate(words = ['word', 'worm', 'worn'],groups = [1, 2, 3]) == ['word', 'worm', 'worn']
    assert candidate(words = ['apple', 'appla', 'applb', 'applc'],groups = [1, 2, 2, 3]) == ['apple', 'appla', 'applc']
    assert candidate(words = ['aaa', 'aab', 'aac', 'aad'],groups = [1, 2, 1, 2]) == ['aaa', 'aab', 'aac', 'aad']
    assert candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 1, 2, 3]) == ['abc']
    assert candidate(words = ['aaa', 'aab', 'aac'],groups = [1, 2, 3]) == ['aaa', 'aab', 'aac']
    assert candidate(words = ['test', 'tast', 'tist', 'tast'],groups = [1, 2, 3, 1]) == ['test', 'tast', 'tist', 'tast']
    assert candidate(words = ['test', 'tast', 'tekt'],groups = [1, 2, 3]) == ['test', 'tast']
    assert candidate(words = ['abcd', 'abce', 'abcf'],groups = [1, 2, 3]) == ['abcd', 'abce', 'abcf']
    assert candidate(words = ['word', 'wore', 'word', 'worn'],groups = [1, 2, 3, 4]) == ['word', 'wore', 'word', 'worn']
    assert candidate(words = ['one', 'two', 'thr'],groups = [1, 1, 1]) == ['one']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hellp'],groups = [1, 2, 1, 2]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['code', 'coed', 'cdeo'],groups = [2, 2, 3]) == ['code']
    assert candidate(words = ['loop', 'lopo', 'leep'],groups = [1, 2, 1]) == ['loop']
    assert candidate(words = ['same', 'sane', 'safe'],groups = [1, 1, 2]) == ['same', 'safe']
    assert candidate(words = ['apple', 'apply', 'spoil', 'spied'],groups = [1, 1, 2, 2]) == ['apple']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 3, 4]) == ['hello', 'hallo', 'hxllo', 'pxllo']
    assert candidate(words = ['test', 'text', 'tast', 'tast'],groups = [1, 2, 1, 3]) == ['test', 'text']
    assert candidate(words = ['abcd', 'abcf', 'abdf', 'abef'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abdf', 'abef']
    assert candidate(words = ['one', 'two', 'ton', 'oen'],groups = [1, 1, 2, 2]) == ['one']
    assert candidate(words = ['word', 'wird', 'word', 'wond'],groups = [1, 1, 2, 2]) == ['wird', 'word']
    assert candidate(words = ['test', 'tast', 'ttst'],groups = [1, 2, 3]) == ['test', 'tast', 'ttst']
    assert candidate(words = ['aaa', 'aab', 'aac'],groups = [1, 2, 1]) == ['aaa', 'aab', 'aac']
    assert candidate(words = ['dog', 'dot', 'lot', 'log'],groups = [1, 2, 1, 2]) == ['dog', 'dot', 'lot', 'log']
    assert candidate(words = ['test', 'tast', 'teat'],groups = [1, 2, 3]) == ['test', 'tast']
    assert candidate(words = ['same', 'sane', 'same', 'sane'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'same', 'sane']
    assert candidate(words = ['apple', 'bpple', 'cppld'],groups = [1, 2, 1]) == ['apple', 'bpple']
    assert candidate(words = ['xyz', 'xyx', 'xzx', 'xxz'],groups = [1, 1, 1, 1]) == ['xyz']
    assert candidate(words = ['apple', 'appla', 'bpple', 'appea'],groups = [1, 2, 3, 4]) == ['apple', 'appla', 'appea']
    assert candidate(words = ['apple', 'appla', 'applp'],groups = [1, 2, 1]) == ['apple', 'appla', 'applp']
    assert candidate(words = ['abcd', 'abcf', 'abce', 'abdc'],groups = [1, 1, 2, 1]) == ['abcd', 'abce']
    assert candidate(words = ['same', 'sane', 'sale', 'tale'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'sale', 'tale']
    assert candidate(words = ['test', 'tast', 'tost', 'fest'],groups = [1, 2, 3, 4]) == ['test', 'tast', 'tost']
    assert candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 1, 2, 2]) == ['cat', 'rat']
    assert candidate(words = ['one', 'two', 'three', 'four'],groups = [1, 2, 3, 4]) == ['one']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'pxllo'],groups = [1, 2, 2, 3]) == ['hello', 'hxllo', 'pxllo']
    assert candidate(words = ['same', 'sane', 'sane', 'same'],groups = [1, 2, 2, 3]) == ['same', 'sane', 'same']
    assert candidate(words = ['apple', 'appla', 'applu', 'applp'],groups = [1, 1, 2, 2]) == ['apple', 'applu']
    assert candidate(words = ['same', 'sane', 'safe', 'same'],groups = [1, 2, 3, 1]) == ['same', 'sane', 'safe', 'same']
    assert candidate(words = ['xyz', 'xyw', 'xzz', 'xyx'],groups = [1, 2, 1, 2]) == ['xyz', 'xyw']
    assert candidate(words = ['cat', 'dog', 'bat'],groups = [1, 2, 3]) == ['cat', 'bat']
    assert candidate(words = ['word', 'ward', 'cord', 'card'],groups = [1, 2, 3, 4]) == ['word', 'ward', 'card']
    assert candidate(words = ['same', 'sane', 'sake'],groups = [1, 2, 1]) == ['same', 'sane', 'sake']
    assert candidate(words = ['abc', 'abd', 'acc', 'aba'],groups = [1, 2, 3, 2]) == ['abc', 'abd']
    assert candidate(words = ['apple', 'appla', 'abble', 'abble'],groups = [1, 2, 2, 3]) == ['apple', 'appla']
    assert candidate(words = ['test', 'text', 'tast'],groups = [1, 2, 1]) == ['test', 'text']
    assert candidate(words = ['abcd', 'abcf', 'abdf'],groups = [1, 1, 2]) == ['abcf', 'abdf']
    assert candidate(words = ['word', 'worm', 'wirm', 'wirt'],groups = [1, 2, 1, 3]) == ['word', 'worm', 'wirm', 'wirt']
    assert candidate(words = ['code', 'kode', 'cide', 'coke'],groups = [1, 2, 3, 4]) == ['code', 'kode']
    assert candidate(words = ['word', 'worm', 'worn'],groups = [1, 2, 1]) == ['word', 'worm', 'worn']
    assert candidate(words = ['xyz', 'xyw', 'xzz', 'xyy'],groups = [2, 3, 2, 3]) == ['xyz', 'xyw']
    assert candidate(words = ['xyz', 'xyx', 'xyy', 'xyw'],groups = [1, 2, 3, 4]) == ['xyz', 'xyx', 'xyy', 'xyw']
    assert candidate(words = ['same', 'sane', 'tame', 'game'],groups = [1, 2, 3, 4]) == ['same', 'tame', 'game']
    assert candidate(words = ['tree', 'trex', 'trey', 'gree'],groups = [1, 2, 1, 2]) == ['tree', 'trex', 'trey']
    assert candidate(words = ['abc', 'bcd', 'cde', 'def'],groups = [1, 1, 2, 2]) == ['abc']
    assert candidate(words = ['test', 'tets', 'tast', 'tast'],groups = [1, 2, 2, 3]) == ['test', 'tast']
    assert candidate(words = ['abcd', 'abcf', 'abdg'],groups = [1, 2, 3]) == ['abcd', 'abcf']
    assert candidate(words = ['hello', 'hallo', 'hullo'],groups = [1, 2, 1]) == ['hello', 'hallo', 'hullo']
    assert candidate(words = ['abc', 'bcd', 'cde'],groups = [1, 1, 2]) == ['abc']
    assert candidate(words = ['same', 'sane', 'game', 'tame'],groups = [1, 2, 1, 2]) == ['same', 'sane']
    assert candidate(words = ['test', 'tast', 'teat', 'teet'],groups = [1, 2, 3, 4]) == ['test', 'teat', 'teet']
    assert candidate(words = ['abc', 'abd', 'acc'],groups = [1, 2, 3]) == ['abc', 'abd']
    assert candidate(words = ['code', 'cide', 'kode', 'coda'],groups = [1, 2, 1, 2]) == ['code', 'cide']
    assert candidate(words = ['same', 'sane', 'game'],groups = [1, 1, 2]) == ['same', 'game']
    assert candidate(words = ['hello', 'hallo', 'hxllo', 'hexlo'],groups = [10, 20, 10, 30]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['abc', 'abd', 'acc', 'bcd'],groups = [1, 2, 3, 4]) == ['abc', 'abd']
    assert candidate(words = ['hello', 'hallo', 'hullo', 'hellp'],groups = [1, 2, 1, 3]) == ['hello', 'hallo', 'hullo']
    assert candidate(words = ['play', 'plby', 'plya', 'plax'],groups = [1, 1, 2, 2]) == ['play', 'plax']
    assert candidate(words = ['test', 'tast', 'tost', 'tett'],groups = [1, 2, 1, 2]) == ['test', 'tast', 'tost']
    assert candidate(words = ['same', 'sane', 'sage', 'page'],groups = [1, 1, 2, 2]) == ['same', 'sage']
    assert candidate(words = ['test', 'tast', 'tell', 'tall'],groups = [1, 2, 3, 4]) == ['test', 'tast']
    assert candidate(words = ['same', 'sane', 'sale', 'male'],groups = [1, 2, 3, 4]) == ['same', 'sane', 'sale', 'male']
    assert candidate(words = ['abcd', 'abcf', 'abdf', 'acdf'],groups = [1, 2, 3, 4]) == ['abcd', 'abcf', 'abdf', 'acdf']
    assert candidate(words = ['apple', 'apply', 'spork'],groups = [1, 2, 1]) == ['apple', 'apply']
    assert candidate(words = ['test', 'text', 'tast', 'best'],groups = [1, 2, 1, 3]) == ['test', 'text']
    assert candidate(words = ['hello', 'hallo', 'hxllo'],groups = [1, 2, 3]) == ['hello', 'hallo', 'hxllo']
    assert candidate(words = ['abc', 'abd', 'bcd', 'bce'],groups = [1, 2, 2, 3]) == ['abc', 'abd']
    assert candidate(words = ['one', 'two', 'three'],groups = [1, 2, 3]) == ['one']
    assert candidate(words = ['same', 'sane', 'safe', 'sale'],groups = [1, 2, 1, 2]) == ['same', 'sane', 'safe', 'sale']
    assert candidate(words = ['dog', 'cog', 'rog'],groups = [1, 2, 3]) == ['dog', 'cog', 'rog']
    assert candidate(words = ['five', 'fife', 'five', 'five'],groups = [1, 2, 1, 2]) == ['five', 'fife', 'five']
    assert candidate(words = ['abc', 'bcd', 'cde', 'efg'],groups = [1, 1, 2, 2]) == ['abc']
    assert candidate(words = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'],groups = [1, 2, 3, 4, 5, 6, 7, 8]) == ['aaa', 'aab', 'abb', 'bbb']
    assert candidate(words = ['zzz', 'zzy', 'zyy', 'yyy'],groups = [1, 2, 1, 2]) == ['zzz', 'zzy', 'zyy', 'yyy']
    assert candidate(words = ['word', 'worm', 'worn', 'word'],groups = [1, 2, 1, 3]) == ['word', 'worm', 'worn', 'word']
    assert candidate(words = ['code', 'mode', 'mroe'],groups = [1, 2, 1]) == ['code', 'mode']
    assert candidate(words = ['word', 'worm', 'worn'],groups = [1, 1, 2]) == ['word', 'worn']
    assert candidate(words = ['apple', 'apply', 'appla'],groups = [1, 1, 2]) == ['apple', 'appla']
    assert candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 2, 3, 4]) == ['cat', 'bat', 'rat', 'hat']
    assert candidate(words = ['abc', 'bcd', 'cde'],groups = [1, 1, 1]) == ['abc']
    assert candidate(words = ['cat', 'bat', 'rat', 'hat'],groups = [1, 1, 1, 2]) == ['cat', 'hat']
    assert candidate(words = ['word', 'wird', 'wordy'],groups = [1, 2, 3]) == ['word', 'wird']


