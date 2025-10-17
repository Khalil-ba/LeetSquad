def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'ace', 'bce']) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'ace', 'bce']) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'ac', 'ab', 'abc', 'a']) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'ac', 'ab', 'abc', 'a']) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde']) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde']) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'ab', 'cde']) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'ab', 'cde']) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'ab', 'cd', 'a', 'b', 'c', 'd']) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'ab', 'cd', 'a', 'b', 'c', 'd']) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == [9, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == [9, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc']) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc']) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 26]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abde', 'acde', 'bcde']) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abde', 'acde', 'bcde']) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'ace', 'xyz']) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'ace', 'xyz']) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'yz', 'xz', 'x', 'y', 'z']) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'yz', 'xz', 'x', 'y', 'z']) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'ace', 'bd', 'abcde']) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'ace', 'bd', 'abcde']) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijl', 'abcdefghijkml', 'abcdefghijkmn', 'abcdefghijkop', 'abcdefghijkmnop', 'abcdefghijkmnopq']) == [5, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijl', 'abcdefghijkml', 'abcdefghijkmn', 'abcdefghijkop', 'abcdefghijkmnop', 'abcdefghijkmnopq']) == [5, 30]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyz']) == [1, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyz']) == [1, 21]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrs']) == [2, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrs']) == [2, 15]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'ab', 'a', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == [1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'ab', 'a', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == [1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqrst', 'pqrstuvw', 'pqrstu', 'pqrs', 'pqr', 'pq', 'p', 'qrstuv', 'qrstu', 'qrst', 'qrs', 'qr', 'q', 'rstuv', 'rstu', 'rst', 'rs', 'r', 'stuv', 'stu', 'st', 's', 'tuv', 'tu', 't', 'uv', 'u', 'v']) == [2, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqrst', 'pqrstuvw', 'pqrstu', 'pqrs', 'pqr', 'pq', 'p', 'qrstuv', 'qrstu', 'qrst', 'qrs', 'qr', 'q', 'rstuv', 'rstu', 'rst', 'rs', 'r', 'stuv', 'stu', 'st', 's', 'tuv', 'tu', 't', 'uv', 'u', 'v']) == [2, 27]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu']) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu']) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'ab', 'a', 'bc', 'b', 'c', 'ac', 'd', 'de', 'def', 'defg', 'defgh', 'defghi', 'defghij', 'defghijk', 'defghijkl', 'defghijklm', 'defghijklmn', 'defghijklmno', 'defghijklmnop', 'defghijklmnopq', 'defghijklmnopqr', 'defghijklmnopqrs', 'defghijklmnopqrst', 'defghijklmnopqrstu', 'defghijklmnopqrstuv', 'defghijklmnopqrstuvw', 'defghijklmnopqrstuvwx', 'defghijklmnopqrstuvwxy', 'defghijklmnopqrstuvwxyz']) == [1, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'ab', 'a', 'bc', 'b', 'c', 'ac', 'd', 'de', 'def', 'defg', 'defgh', 'defghi', 'defghij', 'defghijk', 'defghijkl', 'defghijklm', 'defghijklmn', 'defghijklmno', 'defghijklmnop', 'defghijklmnopq', 'defghijklmnopqr', 'defghijklmnopqrs', 'defghijklmnopqrst', 'defghijklmnopqrstu', 'defghijklmnopqrstuv', 'defghijklmnopqrstuvw', 'defghijklmnopqrstuvwx', 'defghijklmnopqrstuvwxy', 'defghijklmnopqrstuvwxyz']) == [1, 31]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abc', 'abd', 'acd', 'bcd', 'abcd', 'abcde', 'abcf', 'abcdg', 'abde', 'acde', 'bcde', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [4, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abc', 'abd', 'acd', 'bcd', 'abcd', 'abcde', 'abcf', 'abcdg', 'abde', 'acde', 'bcde', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [4, 17]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyza', 'xyzab', 'xyzabc', 'xyzabcd', 'xyzabcde', 'xyzabcdef', 'xyzabcdefg', 'xyzabcdefgh', 'xyzabcdefghi', 'xyzabcdefghij', 'xyzabcdefghijk', 'xyzabcdefghijkl', 'xyzabcdefghijklm', 'xyzabcdefghijklmn', 'xyzabcdefghijklmno', 'xyzabcdefghijklmnop', 'xyzabcdefghijklmnopq', 'xyzabcdefghijklmnopqr', 'xyzabcdefghijklmnopqrst', 'xyzabcdefghijklmnopqrstu', 'xyzabcdefghijklmnopqrstuv', 'xyzabcdefghijklmnopqrstuvw', 'xyzabcdefghijklmnopqrstuvwxy', 'xyzabcdefghijklmnopqrstuvwxyz']) == [2, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyza', 'xyzab', 'xyzabc', 'xyzabcd', 'xyzabcde', 'xyzabcdef', 'xyzabcdefg', 'xyzabcdefgh', 'xyzabcdefghi', 'xyzabcdefghij', 'xyzabcdefghijk', 'xyzabcdefghijkl', 'xyzabcdefghijklm', 'xyzabcdefghijklmn', 'xyzabcdefghijklmno', 'xyzabcdefghijklmnop', 'xyzabcdefghijklmnopq', 'xyzabcdefghijklmnopqr', 'xyzabcdefghijklmnopqrst', 'xyzabcdefghijklmnopqrstu', 'xyzabcdefghijklmnopqrstuv', 'xyzabcdefghijklmnopqrstuvw', 'xyzabcdefghijklmnopqrstuvwxy', 'xyzabcdefghijklmnopqrstuvwxyz']) == [2, 25]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abcd', 'abef', 'acde', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == [3, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abcd', 'abef', 'acde', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == [3, 24]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl', 'abm', 'abn', 'abo', 'abp', 'abq', 'abr', 'abs', 'abt', 'abu', 'abv', 'abw', 'abx', 'aby', 'abz', 'acb', 'adb', 'aeb', 'afb', 'agb', 'ahb', 'aib', 'ajb', 'akb', 'alb', 'amb', 'anb', 'aob', 'apb', 'aqb', 'arb', 'asb', 'atb', 'aub', 'avb', 'awb', 'axb', 'ayb', 'azb']) == [1, 48]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl', 'abm', 'abn', 'abo', 'abp', 'abq', 'abr', 'abs', 'abt', 'abu', 'abv', 'abw', 'abx', 'aby', 'abz', 'acb', 'adb', 'aeb', 'afb', 'agb', 'ahb', 'aib', 'ajb', 'akb', 'alb', 'amb', 'anb', 'aob', 'apb', 'aqb', 'arb', 'asb', 'atb', 'aub', 'avb', 'awb', 'axb', 'ayb', 'azb']) == [1, 48]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'acdf', 'bcdf', 'abcdg', 'abcfg', 'abdfg', 'acdfg', 'bcdfg', 'abcdef', 'abcdfg', 'abcfgh', 'abcdefg', 'abcdefh', 'abcddef', 'abcedef', 'abcfdef', 'abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefk', 'abcdefl', 'abcdefm', 'abcdefn', 'abcdefo', 'abcdefp', 'abcdefq', 'abcdefr', 'abcdefs', 'abcdeft', 'abcdefu', 'abcdefv', 'abcdefw', 'abcdefx', 'abcdefy', 'abcdefz']) == [1, 37]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'acdf', 'bcdf', 'abcdg', 'abcfg', 'abdfg', 'acdfg', 'bcdfg', 'abcdef', 'abcdfg', 'abcfgh', 'abcdefg', 'abcdefh', 'abcddef', 'abcedef', 'abcfdef', 'abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefk', 'abcdefl', 'abcdefm', 'abcdefn', 'abcdefo', 'abcdefp', 'abcdefq', 'abcdefr', 'abcdefs', 'abcdeft', 'abcdefu', 'abcdefv', 'abcdefw', 'abcdefx', 'abcdefy', 'abcdefz']) == [1, 37]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == [1, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == [1, 9]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'abc', 'ab', 'ac', 'bc', 'a', 'b', 'c', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop']) == [2, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'abc', 'ab', 'ac', 'bc', 'a', 'b', 'c', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop']) == [2, 30]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'yz', 'xz', 'x', 'y', 'z', 'xyw', 'yzw', 'xzw', 'w', 'xyzw']) == [1, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'yz', 'xz', 'x', 'y', 'z', 'xyw', 'yzw', 'xzw', 'w', 'xyzw']) == [1, 12]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'ac', 'ab', 'b', 'c', 'bcd', 'bc', 'cd', 'd', 'abcd', 'abdc', 'bacd', 'cabd', 'acbd', 'bcad', 'bcda']) == [1, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'ac', 'ab', 'b', 'c', 'bcd', 'bc', 'cd', 'd', 'abcd', 'abdc', 'bacd', 'cabd', 'acbd', 'bcad', 'bcda']) == [1, 16]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno']) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno']) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'abc', 'def', 'ghijkl', 'mnopqr', 'stuv', 'wxyz', 'abcdefghij']) == [8, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'abc', 'def', 'ghijkl', 'mnopqr', 'stuv', 'wxyz', 'abcdefghij']) == [8, 1]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'xz', 'yz', 'a', 'b', 'c', 'abc', 'abcd']) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'xz', 'yz', 'a', 'b', 'c', 'abc', 'abcd']) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdf', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [2, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdf', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [2, 20]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zabcd', 'efghi', 'jklmn', 'opqrs', 'tuvwx', 'yzabc', 'defgh', 'ijklm', 'nopqr', 'stuvw', 'xyzab', 'cdefg', 'hijkl', 'mnopq', 'rstuv', 'wxyza', 'bcdef', 'ghijk', 'lmnop', 'opqrs', 'tuvwx', 'yzabc']) == [11, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zabcd', 'efghi', 'jklmn', 'opqrs', 'tuvwx', 'yzabc', 'defgh', 'ijklm', 'nopqr', 'stuvw', 'xyzab', 'cdefg', 'hijkl', 'mnopq', 'rstuv', 'wxyza', 'bcdef', 'ghijk', 'lmnop', 'opqrs', 'tuvwx', 'yzabc']) == [11, 22]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == [14, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == [14, 3]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzq', 'abcdefghijklmnopqrstuvwxyzp', 'abcdefghijklmnopqrstuvwxyzr', 'abcdefghijklmnopqrstuvwxyzs']) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzq', 'abcdefghijklmnopqrstuvwxyzp', 'abcdefghijklmnopqrstuvwxyzr', 'abcdefghijklmnopqrstuvwxyzs']) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcf', 'abdf', 'acdf', 'bcdf', 'abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxy']) == [2, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcf', 'abdf', 'acdf', 'bcdf', 'abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxy']) == [2, 21]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqr', 'pq', 'pr', 'qr', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqr', 'pq', 'pr', 'qr', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 30]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw']) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw']) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']) == [1, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']) == [1, 31]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abef', 'acgh', 'bcdf', 'cdef', 'efgh', 'efgi', 'efgj', 'efgk', 'efgl', 'efgm', 'efgn', 'efgo', 'efgp', 'efgq', 'efgr', 'efgs', 'efgt', 'efgu', 'efgv', 'efgw', 'efgx', 'efgy', 'efgz']) == [4, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abef', 'acgh', 'bcdf', 'cdef', 'efgh', 'efgi', 'efgj', 'efgk', 'efgl', 'efgm', 'efgn', 'efgo', 'efgp', 'efgq', 'efgr', 'efgs', 'efgt', 'efgu', 'efgv', 'efgw', 'efgx', 'efgy', 'efgz']) == [4, 19]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == [2, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == [2, 18]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 26]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde']) == [1, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde']) == [1, 14]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == [1, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == [1, 30]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [3, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [3, 24]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'abc', 'def', 'abcd', 'abef', 'acdf', 'bcde', 'abcf', 'abcdg', 'abcde', 'abcdefg']) == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'abc', 'def', 'abcd', 'abef', 'acdf', 'bcde', 'abcf', 'abcdg', 'abcde', 'abcdefg']) == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'mno', 'mnp', 'mop', 'nop', 'npp', 'ppp', 'pp', 'p', 'z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == [1, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'mno', 'mnp', 'mop', 'nop', 'npp', 'ppp', 'pp', 'p', 'z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == [1, 19]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdefghi', 'jklmnopqr', 'stuvwxyz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z', 'abcdefghijkl', 'mnopqrstu', 'vwxyz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz']) == [18, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdefghi', 'jklmnopqr', 'stuvwxyz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z', 'abcdefghijkl', 'mnopqrstu', 'vwxyz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz']) == [18, 4]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzab', 'cdefgh', 'ijklmn', 'opqrst', 'uvwxyl', 'zabcde', 'fghijk', 'lmnopq', 'rstuvw', 'xylzab', 'cdefgh', 'ijklmn', 'opqrst', 'vwxyza', 'yzabcd', 'efghij', 'klmnop', 'qrstuv', 'wxylza', 'bcdefg', 'hijklm', 'nopqrs', 'tuvwxy', 'zabcde', 'fghijk', 'lmnopq', 'rstuvw', 'wxylza', 'cdefgh', 'ijklmn', 'opqrst', 'vwxyza', 'yzabcd']) == [15, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzab', 'cdefgh', 'ijklmn', 'opqrst', 'uvwxyl', 'zabcde', 'fghijk', 'lmnopq', 'rstuvw', 'xylzab', 'cdefgh', 'ijklmn', 'opqrst', 'vwxyza', 'yzabcd', 'efghij', 'klmnop', 'qrstuv', 'wxylza', 'bcdefg', 'hijklm', 'nopqrs', 'tuvwxy', 'zabcde', 'fghijk', 'lmnopq', 'rstuvw', 'wxylza', 'cdefgh', 'ijklmn', 'opqrst', 'vwxyza', 'yzabcd']) == [15, 9]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyza', 'xyzb', 'xyzc', 'xyzd', 'xyze', 'xyzf', 'xyzg', 'xyzh', 'xyzi', 'xyzj', 'xyzk', 'xyzl', 'xyzm', 'xyzn', 'xyzo', 'xyzp', 'xyzq', 'xyxr', 'xyxs', 'xyxt', 'xyxu', 'xyxv', 'xyxw', 'xyxx', 'xyxy', 'xyxz']) == [1, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyza', 'xyzb', 'xyzc', 'xyzd', 'xyze', 'xyzf', 'xyzg', 'xyzh', 'xyzi', 'xyzj', 'xyzk', 'xyzl', 'xyzm', 'xyzn', 'xyzo', 'xyzp', 'xyzq', 'xyxr', 'xyxs', 'xyxt', 'xyxu', 'xyxv', 'xyxw', 'xyxx', 'xyxy', 'xyxz']) == [1, 33]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [2, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [2, 15]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == [1, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == [1, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij']) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij']) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'abcdeg', 'abcef', 'bcdef', 'acdef', 'abdef', 'abcdf', 'abcdg', 'abc', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == [2, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'abcdeg', 'abcef', 'bcdef', 'acdef', 'abdef', 'abcdf', 'abcdg', 'abc', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == [2, 14]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'ba', 'ca', 'da', 'ea', 'fa', 'ga', 'ha', 'ia', 'ja', 'ka', 'la', 'ma', 'na', 'oa', 'pa', 'qa', 'ra', 'sa', 'ta', 'ua', 'va', 'wa', 'xa', 'ya', 'za']) == [1, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'ba', 'ca', 'da', 'ea', 'fa', 'ga', 'ha', 'ia', 'ja', 'ka', 'la', 'ma', 'na', 'oa', 'pa', 'qa', 'ra', 'sa', 'ta', 'ua', 'va', 'wa', 'xa', 'ya', 'za']) == [1, 50]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy']) == [1, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy']) == [1, 25]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'abcde', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']) == [1, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'abcde', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']) == [1, 9]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'ac', 'abc', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz', 'mnopqrstuvwxy', 'mnopqrstuvwx', 'mnopqrstuvw', 'mnopqrstuv', 'mnopqrstu', 'mnopqrst', 'mnopqr', 'mnopq', 'mnop', 'mon', 'mo', 'm', 'nopqrstuvwxyz', 'nopqrstuvwx', 'nopqrstuvw', 'nopqrstuv', 'nopqrstu', 'nopqrst', 'nopqr', 'nopq', 'nop', 'no', 'n', 'opqrstuvwxyz', 'opqrstuvwx', 'opqrstuvw', 'opqrstuv', 'opqrstu', 'opqrst', 'opqr', 'opq', 'op', 'o', 'pqrstuvwxyz', 'pqrstuvwx', 'pqrstuvw', 'pqrstuv', 'pqrstu', 'pqrs', 'pqr', 'pq', 'p']) == [3, 42]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'ac', 'abc', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz', 'mnopqrstuvwxy', 'mnopqrstuvwx', 'mnopqrstuvw', 'mnopqrstuv', 'mnopqrstu', 'mnopqrst', 'mnopqr', 'mnopq', 'mnop', 'mon', 'mo', 'm', 'nopqrstuvwxyz', 'nopqrstuvwx', 'nopqrstuvw', 'nopqrstuv', 'nopqrstu', 'nopqrst', 'nopqr', 'nopq', 'nop', 'no', 'n', 'opqrstuvwxyz', 'opqrstuvwx', 'opqrstuvw', 'opqrstuv', 'opqrstu', 'opqrst', 'opqr', 'opq', 'op', 'o', 'pqrstuvwxyz', 'pqrstuvwx', 'pqrstuvw', 'pqrstuv', 'pqrstu', 'pqrs', 'pqr', 'pq', 'p']) == [3, 42]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnopqr', 'mnopqs', 'mnopqt', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrs', 'mnoqrt', 'mnoqst', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrt', 'mnoqst', 'mnoprt', 'mnopst', 'mnoqrs', 'mnopqr', 'mnopqs', 'mnopqt', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrt', 'mnoqst', 'mnoprt', 'mnopst']) == [1, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnopqr', 'mnopqs', 'mnopqt', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrs', 'mnoqrt', 'mnoqst', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrt', 'mnoqst', 'mnoprt', 'mnopst', 'mnoqrs', 'mnopqr', 'mnopqs', 'mnopqt', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrt', 'mnoqst', 'mnoprt', 'mnopst']) == [1, 27]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'bcdef', 'acdef', 'abcef', 'abdef', 'acdefg', 'bcdefg', 'cdefgh', 'defghi']) == [1, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'bcdef', 'acdef', 'abcef', 'abdef', 'acdefg', 'bcdefg', 'cdefgh', 'defghi']) == [1, 15]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyzu', 'xyvz', 'xywz', 'xyxz', 'xyyz', 'xyzv', 'xyzw', 'xyzz', 'xzu', 'xvz', 'xwz', 'xxz', 'xzz', 'yzu', 'yvz', 'ywz', 'yyz', 'yzv', 'yzw', 'yzz', 'zvu', 'zwv', 'zzv', 'zzw', 'zzz', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz', 'vwxyz', 'vwxyza', 'vwxyzab', 'vwxyzabc', 'vwxyzabcd']) == [1, 84]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyzu', 'xyvz', 'xywz', 'xyxz', 'xyyz', 'xyzv', 'xyzw', 'xyzz', 'xzu', 'xvz', 'xwz', 'xxz', 'xzz', 'yzu', 'yvz', 'ywz', 'yyz', 'yzv', 'yzw', 'yzz', 'zvu', 'zwv', 'zzv', 'zzw', 'zzz', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz', 'vwxyz', 'vwxyza', 'vwxyzab', 'vwxyzabc', 'vwxyzabcd']) == [1, 84]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == [1, 51]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == [1, 51]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstu']) == [1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstu']) == [1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcd', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'a', 'b', 'c', 'd']) == [1, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcd', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'a', 'b', 'c', 'd']) == [1, 15]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu']) == [1, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu']) == [1, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcd', 'ab', 'bc', 'cd', 'ac', 'a', 'b', 'c', 'd']) == [1, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcd', 'ab', 'bc', 'cd', 'ac', 'a', 'b', 'c', 'd']) == [1, 13]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqrst', 'pqsrt', 'pqrst', 'pqrsu', 'pqrs', 'pqrt', 'pqst', 'prst', 'qrst', 'pq', 'qr', 'qs', 'qt', 'pr', 'ps', 'pt', 'rs', 'rt', 'st', 'p', 'q', 'r', 's', 't']) == [2, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqrst', 'pqsrt', 'pqrst', 'pqrsu', 'pqrs', 'pqrt', 'pqst', 'prst', 'qrst', 'pq', 'qr', 'qs', 'qt', 'pr', 'ps', 'pt', 'rs', 'rt', 'st', 'p', 'q', 'r', 's', 't']) == [2, 15]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghij', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']) == [2, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghij', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']) == [2, 33]: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrt', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == [3, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrt', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == [3, 20]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['abc', 'bcd', 'ace', 'bce']) == [1, 4]
    assert candidate(words = ['abcd', 'ac', 'ab', 'abc', 'a']) == [1, 5]
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde']) == [1, 7]
    assert candidate(words = ['a', 'b', 'ab', 'cde']) == [2, 3]
    assert candidate(words = ['abcd', 'ab', 'cd', 'a', 'b', 'c', 'd']) == [2, 6]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == [1, 7]
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == [9, 1]
    assert candidate(words = ['a', 'ab', 'abc']) == [1, 3]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 26]
    assert candidate(words = ['abc', 'abcd', 'abde', 'acde', 'bcde']) == [1, 5]
    assert candidate(words = ['abc', 'bcd', 'ace', 'xyz']) == [2, 3]
    assert candidate(words = ['xyz', 'xy', 'yz', 'xz', 'x', 'y', 'z']) == [1, 7]
    assert candidate(words = ['abc', 'bcd', 'ace', 'bd', 'abcde']) == [2, 4]
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijl', 'abcdefghijkml', 'abcdefghijkmn', 'abcdefghijkop', 'abcdefghijkmnop', 'abcdefghijkmnopq']) == [5, 30]
    assert candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyz']) == [1, 21]
    assert candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrs']) == [2, 15]
    assert candidate(words = ['abc', 'ab', 'a', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == [1, 10]
    assert candidate(words = ['pqrst', 'pqrstuvw', 'pqrstu', 'pqrs', 'pqr', 'pq', 'p', 'qrstuv', 'qrstu', 'qrst', 'qrs', 'qr', 'q', 'rstuv', 'rstu', 'rst', 'rs', 'r', 'stuv', 'stu', 'st', 's', 'tuv', 'tu', 't', 'uv', 'u', 'v']) == [2, 27]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu']) == [2, 4]
    assert candidate(words = ['abc', 'abcd', 'ab', 'a', 'bc', 'b', 'c', 'ac', 'd', 'de', 'def', 'defg', 'defgh', 'defghi', 'defghij', 'defghijk', 'defghijkl', 'defghijklm', 'defghijklmn', 'defghijklmno', 'defghijklmnop', 'defghijklmnopq', 'defghijklmnopqr', 'defghijklmnopqrs', 'defghijklmnopqrst', 'defghijklmnopqrstu', 'defghijklmnopqrstuv', 'defghijklmnopqrstuvw', 'defghijklmnopqrstuvwx', 'defghijklmnopqrstuvwxy', 'defghijklmnopqrstuvwxyz']) == [1, 31]
    assert candidate(words = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abc', 'abd', 'acd', 'bcd', 'abcd', 'abcde', 'abcf', 'abcdg', 'abde', 'acde', 'bcde', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [4, 17]
    assert candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyza', 'xyzab', 'xyzabc', 'xyzabcd', 'xyzabcde', 'xyzabcdef', 'xyzabcdefg', 'xyzabcdefgh', 'xyzabcdefghi', 'xyzabcdefghij', 'xyzabcdefghijk', 'xyzabcdefghijkl', 'xyzabcdefghijklm', 'xyzabcdefghijklmn', 'xyzabcdefghijklmno', 'xyzabcdefghijklmnop', 'xyzabcdefghijklmnopq', 'xyzabcdefghijklmnopqr', 'xyzabcdefghijklmnopqrst', 'xyzabcdefghijklmnopqrstu', 'xyzabcdefghijklmnopqrstuv', 'xyzabcdefghijklmnopqrstuvw', 'xyzabcdefghijklmnopqrstuvwxy', 'xyzabcdefghijklmnopqrstuvwxyz']) == [2, 25]
    assert candidate(words = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abcd', 'abef', 'acde', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == [3, 24]
    assert candidate(words = ['abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl', 'abm', 'abn', 'abo', 'abp', 'abq', 'abr', 'abs', 'abt', 'abu', 'abv', 'abw', 'abx', 'aby', 'abz', 'acb', 'adb', 'aeb', 'afb', 'agb', 'ahb', 'aib', 'ajb', 'akb', 'alb', 'amb', 'anb', 'aob', 'apb', 'aqb', 'arb', 'asb', 'atb', 'aub', 'avb', 'awb', 'axb', 'ayb', 'azb']) == [1, 48]
    assert candidate(words = ['abcd', 'abcf', 'acdf', 'bcdf', 'abcdg', 'abcfg', 'abdfg', 'acdfg', 'bcdfg', 'abcdef', 'abcdfg', 'abcfgh', 'abcdefg', 'abcdefh', 'abcddef', 'abcedef', 'abcfdef', 'abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefk', 'abcdefl', 'abcdefm', 'abcdefn', 'abcdefo', 'abcdefp', 'abcdefq', 'abcdefr', 'abcdefs', 'abcdeft', 'abcdefu', 'abcdefv', 'abcdefw', 'abcdefx', 'abcdefy', 'abcdefz']) == [1, 37]
    assert candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == [1, 9]
    assert candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'abc', 'ab', 'ac', 'bc', 'a', 'b', 'c', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop']) == [2, 30]
    assert candidate(words = ['xyz', 'xy', 'yz', 'xz', 'x', 'y', 'z', 'xyw', 'yzw', 'xzw', 'w', 'xyzw']) == [1, 12]
    assert candidate(words = ['abc', 'ac', 'ab', 'b', 'c', 'bcd', 'bc', 'cd', 'd', 'abcd', 'abdc', 'bacd', 'cabd', 'acbd', 'bcad', 'bcda']) == [1, 16]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno']) == [3, 4]
    assert candidate(words = ['abcdefg', 'abc', 'def', 'ghijkl', 'mnopqr', 'stuv', 'wxyz', 'abcdefghij']) == [8, 1]
    assert candidate(words = ['xyz', 'xy', 'xz', 'yz', 'a', 'b', 'c', 'abc', 'abcd']) == [3, 4]
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdf', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [2, 20]
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zabcd', 'efghi', 'jklmn', 'opqrs', 'tuvwx', 'yzabc', 'defgh', 'ijklm', 'nopqr', 'stuvw', 'xyzab', 'cdefg', 'hijkl', 'mnopq', 'rstuv', 'wxyza', 'bcdef', 'ghijk', 'lmnop', 'opqrs', 'tuvwx', 'yzabc']) == [11, 22]
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == [14, 3]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzq', 'abcdefghijklmnopqrstuvwxyzp', 'abcdefghijklmnopqrstuvwxyzr', 'abcdefghijklmnopqrstuvwxyzs']) == [1, 5]
    assert candidate(words = ['abcd', 'abcf', 'abdf', 'acdf', 'bcdf', 'abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxy']) == [2, 21]
    assert candidate(words = ['pqr', 'pq', 'pr', 'qr', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 30]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw']) == [1, 4]
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']) == [1, 31]
    assert candidate(words = ['abcd', 'abef', 'acgh', 'bcdf', 'cdef', 'efgh', 'efgi', 'efgj', 'efgk', 'efgl', 'efgm', 'efgn', 'efgo', 'efgp', 'efgq', 'efgr', 'efgs', 'efgt', 'efgu', 'efgv', 'efgw', 'efgx', 'efgy', 'efgz']) == [4, 19]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == [2, 18]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == [1, 26]
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde']) == [1, 14]
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == [1, 30]
    assert candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [3, 24]
    assert candidate(words = ['abcdef', 'abc', 'def', 'abcd', 'abef', 'acdf', 'bcde', 'abcf', 'abcdg', 'abcde', 'abcdefg']) == [2, 10]
    assert candidate(words = ['mnop', 'mno', 'mnp', 'mop', 'nop', 'npp', 'ppp', 'pp', 'p', 'z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == [1, 19]
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdefghi', 'jklmnopqr', 'stuvwxyz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z', 'abcdefghijkl', 'mnopqrstu', 'vwxyz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz']) == [18, 4]
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzab', 'cdefgh', 'ijklmn', 'opqrst', 'uvwxyl', 'zabcde', 'fghijk', 'lmnopq', 'rstuvw', 'xylzab', 'cdefgh', 'ijklmn', 'opqrst', 'vwxyza', 'yzabcd', 'efghij', 'klmnop', 'qrstuv', 'wxylza', 'bcdefg', 'hijklm', 'nopqrs', 'tuvwxy', 'zabcde', 'fghijk', 'lmnopq', 'rstuvw', 'wxylza', 'cdefgh', 'ijklmn', 'opqrst', 'vwxyza', 'yzabcd']) == [15, 9]
    assert candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyza', 'xyzb', 'xyzc', 'xyzd', 'xyze', 'xyzf', 'xyzg', 'xyzh', 'xyzi', 'xyzj', 'xyzk', 'xyzl', 'xyzm', 'xyzn', 'xyzo', 'xyzp', 'xyzq', 'xyxr', 'xyxs', 'xyxt', 'xyxu', 'xyxv', 'xyxw', 'xyxx', 'xyxy', 'xyxz']) == [1, 33]
    assert candidate(words = ['a', 'b', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']) == [2, 15]
    assert candidate(words = ['abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == [1, 13]
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij']) == [2, 6]
    assert candidate(words = ['abcdef', 'abcdeg', 'abcef', 'bcdef', 'acdef', 'abdef', 'abcdf', 'abcdg', 'abc', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'a', 'b', 'c', 'd', 'e', 'f', 'g']) == [2, 14]
    assert candidate(words = ['ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'ba', 'ca', 'da', 'ea', 'fa', 'ga', 'ha', 'ia', 'ja', 'ka', 'la', 'ma', 'na', 'oa', 'pa', 'qa', 'ra', 'sa', 'ta', 'ua', 'va', 'wa', 'xa', 'ya', 'za']) == [1, 50]
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy']) == [1, 25]
    assert candidate(words = ['abcdef', 'abcde', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']) == [1, 9]
    assert candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'ac', 'abc', 'abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz', 'mnopqrstuvwxy', 'mnopqrstuvwx', 'mnopqrstuvw', 'mnopqrstuv', 'mnopqrstu', 'mnopqrst', 'mnopqr', 'mnopq', 'mnop', 'mon', 'mo', 'm', 'nopqrstuvwxyz', 'nopqrstuvwx', 'nopqrstuvw', 'nopqrstuv', 'nopqrstu', 'nopqrst', 'nopqr', 'nopq', 'nop', 'no', 'n', 'opqrstuvwxyz', 'opqrstuvwx', 'opqrstuvw', 'opqrstuv', 'opqrstu', 'opqrst', 'opqr', 'opq', 'op', 'o', 'pqrstuvwxyz', 'pqrstuvwx', 'pqrstuvw', 'pqrstuv', 'pqrstu', 'pqrs', 'pqr', 'pq', 'p']) == [3, 42]
    assert candidate(words = ['mnopqr', 'mnopqs', 'mnopqt', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrs', 'mnoqrt', 'mnoqst', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrt', 'mnoqst', 'mnoprt', 'mnopst', 'mnoqrs', 'mnopqr', 'mnopqs', 'mnopqt', 'mnoprs', 'mnoprt', 'mnopst', 'mnoqrt', 'mnoqst', 'mnoprt', 'mnopst']) == [1, 27]
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abde', 'acde', 'bcde', 'abcde', 'bcdef', 'acdef', 'abcef', 'abdef', 'acdefg', 'bcdefg', 'cdefgh', 'defghi']) == [1, 15]
    assert candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyzu', 'xyvz', 'xywz', 'xyxz', 'xyyz', 'xyzv', 'xyzw', 'xyzz', 'xzu', 'xvz', 'xwz', 'xxz', 'xzz', 'yzu', 'yvz', 'ywz', 'yyz', 'yzv', 'yzw', 'yzz', 'zvu', 'zwv', 'zzv', 'zzw', 'zzz', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz', 'vwxyz', 'vwxyza', 'vwxyzab', 'vwxyzabc', 'vwxyzabcd']) == [1, 84]
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == [1, 51]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstu']) == [1, 10]
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcd', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'a', 'b', 'c', 'd']) == [1, 15]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu']) == [1, 13]
    assert candidate(words = ['abc', 'abd', 'acd', 'bcd', 'abcd', 'ab', 'bc', 'cd', 'ac', 'a', 'b', 'c', 'd']) == [1, 13]
    assert candidate(words = ['pqrst', 'pqsrt', 'pqrst', 'pqrsu', 'pqrs', 'pqrt', 'pqst', 'prst', 'qrst', 'pq', 'qr', 'qs', 'qt', 'pr', 'ps', 'pt', 'rs', 'rt', 'st', 'p', 'q', 'r', 's', 't']) == [2, 15]
    assert candidate(words = ['abcdefghij', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']) == [2, 33]
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrt', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == [3, 20]


