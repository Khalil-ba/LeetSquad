def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['adc', 'wzy', 'abc']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['adc', 'wzy', 'abc']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zyx', 'zwy', 'zvx']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zyx', 'zwy', 'zvx']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zyz', 'zxz', 'wyz']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zyz', 'zxz', 'wyz']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'bob', 'ccc', 'ddd']) == "bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'bob', 'ccc', 'ddd']) == "bob": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aac', 'aad', 'abe']) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aac', 'aad', 'abe']) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'abc', 'uvw', 'aaa']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'abc', 'uvw', 'aaa']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aaa', 'aab', 'aaa']) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aaa', 'aab', 'aaa']) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'aaa', 'zzz', 'aaa', 'zzz', 'aab']) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'aaa', 'zzz', 'aaa', 'zzz', 'aab']) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'uvw', 'rst', 'qpo']) == "qpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'uvw', 'rst', 'qpo']) == "qpo": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aac', 'aba', 'aaa']) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aac', 'aba', 'aaa']) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'cba', 'bac']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'cba', 'bac']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrst', 'qrsu', 'rstv', 'rstw']) == "qrst"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrst', 'qrsu', 'rstv', 'rstw']) == "qrst": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrst', 'qrst', 'qrst', 'qrsu', 'qrst']) == "qrsu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrst', 'qrst', 'qrst', 'qrsu', 'qrst']) == "qrsu": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'ade']) == "ade"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'ade']) == "ade": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aac', 'aba', 'aaa', 'aab', 'aac', 'aba', 'aac', 'aba', 'aab', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aac', 'aba', 'aaa', 'aab', 'aac', 'aba', 'aac', 'aba', 'aab', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'bce']) == "bce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'bce']) == "bce": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bde', 'cef', 'dfg', 'efh', 'fij', 'gjk', 'hkl', 'ilm', 'jmn', 'kno', 'lop', 'mqr', 'nrs', 'ots', 'puv', 'qvw', 'rxy', 'syz', 'tza', 'uab', 'vbc', 'wcd', 'xey', 'yfz', 'zga']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bde', 'cef', 'dfg', 'efh', 'fij', 'gjk', 'hkl', 'ilm', 'jmn', 'kno', 'lop', 'mqr', 'nrs', 'ots', 'puv', 'qvw', 'rxy', 'syz', 'tza', 'uab', 'vbc', 'wcd', 'xey', 'yfz', 'zga']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(words = ['jkl', 'klm', 'lmn', 'mno', 'jklm']) == "jklm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['jkl', 'klm', 'lmn', 'mno', 'jklm']) == "jklm": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'abc', 'bcd', 'cde']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'abc', 'bcd', 'cde']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['uvw', 'vwx', 'wxy', 'vxz', 'wyz']) == "vxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['uvw', 'vwx', 'wxy', 'vxz', 'wyz']) == "vxz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'wxy', 'vwx', 'uvw', 'tuv', 'stu', 'rst', 'qrs', 'pqr', 'opq', 'nop', 'mno', 'lnm', 'klj', 'ijk', 'hgf', 'fed', 'edc', 'dcb', 'cba', 'bca', 'cab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'bac']) == "lnm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'wxy', 'vwx', 'uvw', 'tuv', 'stu', 'rst', 'qrs', 'pqr', 'opq', 'nop', 'mno', 'lnm', 'klj', 'ijk', 'hgf', 'fed', 'edc', 'dcb', 'cba', 'bca', 'cab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'bac']) == "lnm": {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqr', 'qrs', 'rst', 'uvw', 'vwx', 'wxy', 'xyz', 'xya']) == "xya"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqr', 'qrs', 'rst', 'uvw', 'vwx', 'wxy', 'xyz', 'xya']) == "xya": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefg']) == "abcdefh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefg']) == "abcdefh": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'abb', 'acc', 'add', 'aee', 'aff', 'agg', 'aeh', 'aei', 'aej', 'aek', 'ael', 'aem', 'aen', 'aeo', 'aep', 'aeq', 'aer', 'aes', 'aet', 'aeu', 'aev', 'aew', 'aex', 'aey', 'aez', 'afa', 'afb', 'afc', 'afd', 'afe', 'aff', 'afg', 'afh']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'abb', 'acc', 'add', 'aee', 'aff', 'agg', 'aeh', 'aei', 'aej', 'aek', 'ael', 'aem', 'aen', 'aeo', 'aep', 'aeq', 'aer', 'aes', 'aet', 'aeu', 'aev', 'aew', 'aex', 'aey', 'aez', 'afa', 'afb', 'afc', 'afd', 'afe', 'aff', 'afg', 'afh']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xza', 'ywb', 'ywa']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xza', 'ywb', 'ywa']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zzy', 'zzx', 'zzw', 'zzv']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zzy', 'zzx', 'zzw', 'zzv']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'nqpo', 'opqr', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwz', 'vwxy', 'wxza', 'xyzb', 'yzca', 'zcab', 'cabc', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrt', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwz', 'vwxy', 'wxza', 'xyzb', 'yzca', 'zcab', 'cabc', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno']) == "nqpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'nqpo', 'opqr', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwz', 'vwxy', 'wxza', 'xyzb', 'yzca', 'zcab', 'cabc', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrt', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwz', 'vwxy', 'wxza', 'xyzb', 'yzca', 'zcab', 'cabc', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno']) == "nqpo": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'bbaacceeddffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'ccaabbeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz']) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'bbaacceeddffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'ccaabbeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz']) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'geh', 'hif', 'iji', 'jik']) == "geh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'geh', 'hif', 'iji', 'jik']) == "geh": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qwert', 'wertr', 'ertty', 'rtyui', 'tyuio']) == "qwert"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qwert', 'wertr', 'ertty', 'rtyui', 'tyuio']) == "qwert": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aad', 'zaa']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aad', 'zaa']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzza']) == "zzzzzzzzza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzza']) == "zzzzzzzzza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zyz', 'xyx', 'wxw', 'vuq', 'tsr']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zyz', 'xyx', 'wxw', 'vuq', 'tsr']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'mnoq', 'mnop', 'mnoo', 'mnop']) == "mnoq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'mnoq', 'mnop', 'mnoo', 'mnop']) == "mnoq": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mno', 'nop', 'opo', 'npp', 'mqq']) == "opo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mno', 'nop', 'opo', 'npp', 'mqq']) == "opo": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aba', 'aca', 'ada', 'aea', 'afa', 'aga', 'aha']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aba', 'aca', 'ada', 'aea', 'afa', 'aga', 'aha']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnopqr', 'mnopqs', 'mnopqt', 'mnopqu', 'mnopqv']) == "mnopqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnopqr', 'mnopqs', 'mnopqt', 'mnopqu', 'mnopqv']) == "mnopqr": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qwe', 'rft', 'sgh', 'tij', 'ukl', 'vmo']) == "qwe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qwe', 'rft', 'sgh', 'tij', 'ukl', 'vmo']) == "qwe": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'abcefg', 'abcdgg', 'abcdef', 'abcdeg']) == "abcefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'abcefg', 'abcdgg', 'abcdef', 'abcdeg']) == "abcefg": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abz', 'bca', 'cab', 'bac', 'acb', 'baa', 'aaa', 'aab']) == "abz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abz', 'bca', 'cab', 'bac', 'acb', 'baa', 'aaa', 'aab']) == "abz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abz', 'bca', 'cab', 'abc']) == "abz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abz', 'bca', 'cab', 'abc']) == "abz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah', 'aai', 'aaj', 'aak', 'aal', 'aam', 'aan', 'aao', 'aap', 'aaq', 'aar', 'aas', 'aat', 'aau', 'aav', 'aaw', 'aax', 'aay', 'aaz', 'abb', 'abc']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah', 'aai', 'aaj', 'aak', 'aal', 'aam', 'aan', 'aao', 'aap', 'aaq', 'aar', 'aas', 'aat', 'aau', 'aav', 'aaw', 'aax', 'aay', 'aaz', 'abb', 'abc']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aac', 'aab', 'aac', 'aab', 'aac', 'aad', 'aac']) == "aad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aac', 'aab', 'aac', 'aab', 'aac', 'aad', 'aac']) == "aad": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zyz', 'zyx', 'zzx', 'zyw']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zyz', 'zyx', 'zzx', 'zyw']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['uvw', 'uvx', 'uwy', 'uxz']) == "uvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['uvw', 'uvx', 'uwy', 'uxz']) == "uvw": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'nqpr', 'opqs', 'pqrt']) == "mnop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'nqpr', 'opqs', 'pqrt']) == "mnop": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzza']) == "zzzzzzzzzzzzzzzzzzza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzza']) == "zzzzzzzzzzzzzzzzzzza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'yza', 'zab', 'xba', 'xza']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'yza', 'zab', 'xba', 'xza']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'mnoq', 'mnop', 'mnop']) == "mnoq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'mnoq', 'mnop', 'mnop']) == "mnoq": {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqr', 'qrs', 'rst', 'qst', 'qrt']) == "qst"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqr', 'qrs', 'rst', 'qst', 'qrt']) == "qst": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aba', 'aca', 'ada', 'aea']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aba', 'aca', 'ada', 'aea']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aba', 'aca', 'baa']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aba', 'aca', 'baa']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxzz']) == "abcdefghijklmnopqrstuvwxzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxzz']) == "abcdefghijklmnopqrstuvwxzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'aefghi']) == "aefghi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'aefghi']) == "aefghi": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'yza', 'zab', 'abc']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'yza', 'zab', 'abc']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xwv', 'xut', 'xsr']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xwv', 'xut', 'xsr']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aaa', 'aab', 'aac', 'aad', 'abe', 'acd']) == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aaa', 'aab', 'aac', 'aad', 'abe', 'acd']) == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyx', 'vwxyxw', 'wxyxwy', 'xyxwyx', 'yxwyxy']) == "uvwxyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyx', 'vwxyxw', 'wxyxwy', 'xyxwyx', 'yxwyxy']) == "uvwxyx": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']) == "aaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']) == "aaaab": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnop', 'bcdefghijklmno', 'cdefghijklmnop', 'dEefghijklmnop', 'efghijklmnopqr', 'fghijklmnopqrs', 'ghijklmnopqrst', 'hijklmnopqrstu', 'ijklmnopqrstuv', 'jklmnopqrstuvw', 'klmnopqrstuvwx', 'lmnopqrstuvwxy', 'mnopqrstuvwxyz']) == "abcdefghijklmnop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnop', 'bcdefghijklmno', 'cdefghijklmnop', 'dEefghijklmnop', 'efghijklmnopqr', 'fghijklmnopqrs', 'ghijklmnopqrst', 'hijklmnopqrstu', 'ijklmnopqrstuv', 'jklmnopqrstuvw', 'klmnopqrstuvwx', 'lmnopqrstuvwxy', 'mnopqrstuvwxyz']) == "abcdefghijklmnop": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aaa', 'aab', 'aac', 'aad', 'abe']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aaa', 'aab', 'aac', 'aad', 'abe']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'zzy', 'zyz', 'yzz', 'zyx', 'yxz', 'xzy', 'xyz', 'yxw', 'xyw', 'xwy', 'ywx', 'wxy', 'wyz', 'xzy', 'xyz', 'xwy', 'ywx', 'wxy', 'wyz', 'xzy', 'xyz', 'xwy', 'ywx']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'zzy', 'zyz', 'yzz', 'zyx', 'yxz', 'xzy', 'xyz', 'yxw', 'xyw', 'xwy', 'ywx', 'wxy', 'wyz', 'xzy', 'xyz', 'xwy', 'ywx', 'wxy', 'wyz', 'xzy', 'xyz', 'xwy', 'ywx']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyx', 'yzy', 'zzz', 'yzy', 'xyx', 'vwx', 'uvw', 'tuv', 'stu', 'qrs', 'pqr', 'opq', 'nop', 'mno', 'zyz', 'zzz']) == "zyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyx', 'yzy', 'zzz', 'yzy', 'xyx', 'vwx', 'uvw', 'tuv', 'stu', 'qrs', 'pqr', 'opq', 'nop', 'mno', 'zyz', 'zzz']) == "zyz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'aaa', 'aab', 'aac', 'aad']) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'aaa', 'aab', 'aac', 'aad']) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hero', 'helq', 'herl']) == "hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hero', 'helq', 'herl']) == "hello": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'yza', 'zab', 'cab', 'bcd']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'yza', 'zab', 'cab', 'bcd']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aba', 'bab', 'bba', 'aab', 'aaa', 'aab', 'aba', 'abb', 'abc']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aba', 'bab', 'bba', 'aab', 'aaa', 'aab', 'aba', 'abb', 'abc']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'yyy', 'xxz', 'xxy']) == "xxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'yyy', 'xxz', 'xxy']) == "xxz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xza', 'xya', 'xwa']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xza', 'xya', 'xwa']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['ghi', 'hij', 'ijk', 'jkl', 'gij']) == "gij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ghi', 'hij', 'ijk', 'jkl', 'gij']) == "gij": {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqr', 'qrs', 'rst', 'str']) == "str"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqr', 'qrs', 'rst', 'str']) == "str": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zxy', 'zyx', 'yxz', 'yzy']) == "zxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zxy', 'zyx', 'yxz', 'yzy']) == "zxy": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abce', 'abcf', 'abcd', 'abcg']) == "abce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abce', 'abcf', 'abcd', 'abcg']) == "abce": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'cab', 'bca', 'abc', 'bca', 'cab', 'bac', 'acb', 'baa', 'aaa', 'aab', 'aac', 'aad', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc']) == "yza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'cab', 'bca', 'abc', 'bca', 'cab', 'bac', 'acb', 'baa', 'aaa', 'aab', 'aac', 'aad', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc']) == "yza": {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'applf', 'applg', 'applh']) == "apple"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'applf', 'applg', 'applh']) == "apple": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'yyz', 'xxz', 'wwz', 'vvz', 'uuz', 'ttz', 'ssz', 'rrz', 'qqz', 'ppz', 'opo', 'ono', 'nnm', 'nml', 'nkl', 'nlj', 'nik', 'ihj', 'igh', 'ifh', 'ieh', 'idh', 'ich', 'ibh', 'iah', 'azg', 'azy', 'ayx', 'axw', 'avv', 'auu', 'att', 'ass', 'arr', 'aqq', 'app', 'aoo', 'ano', 'aml', 'akl', 'ajk', 'aik', 'aih', 'aig', 'aif', 'aie', 'aid', 'aic', 'abh', 'aag', 'aaf', 'aae', 'aad', 'aac', 'aab']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'yyz', 'xxz', 'wwz', 'vvz', 'uuz', 'ttz', 'ssz', 'rrz', 'qqz', 'ppz', 'opo', 'ono', 'nnm', 'nml', 'nkl', 'nlj', 'nik', 'ihj', 'igh', 'ifh', 'ieh', 'idh', 'ich', 'ibh', 'iah', 'azg', 'azy', 'ayx', 'axw', 'avv', 'auu', 'att', 'ass', 'arr', 'aqq', 'app', 'aoo', 'ano', 'aml', 'akl', 'ajk', 'aik', 'aih', 'aig', 'aif', 'aie', 'aid', 'aic', 'abh', 'aag', 'aaf', 'aae', 'aad', 'aac', 'aab']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['qwe', 'rty', 'uio', 'pas', 'qdf']) == "qwe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qwe', 'rty', 'uio', 'pas', 'qdf']) == "qwe": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aac', 'aad', 'abe', 'bbf', 'ccg', 'ddd']) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aac', 'aad', 'abe', 'bbf', 'ccg', 'ddd']) == "aab": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['adc', 'wzy', 'abc']) == "abc"
    assert candidate(words = ['zzz', 'zyx', 'zwy', 'zvx']) == "zzz"
    assert candidate(words = ['zzz', 'zyz', 'zxz', 'wyz']) == "zzz"
    assert candidate(words = ['aaa', 'bob', 'ccc', 'ddd']) == "bob"
    assert candidate(words = ['aab', 'aac', 'aad', 'abe']) == "aab"
    assert candidate(words = ['xyz', 'abc', 'uvw', 'aaa']) == "aaa"
    assert candidate(words = ['aaa', 'aaa', 'aab', 'aaa']) == "aab"
    assert candidate(words = ['zzz', 'aaa', 'zzz', 'aaa', 'zzz', 'aab']) == "aab"
    assert candidate(words = ['xyz', 'uvw', 'rst', 'qpo']) == "qpo"
    assert candidate(words = ['aab', 'aac', 'aba', 'aaa']) == "aab"
    assert candidate(words = ['qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'cba', 'bac']) == "yza"
    assert candidate(words = ['qrst', 'qrsu', 'rstv', 'rstw']) == "qrst"
    assert candidate(words = ['qrst', 'qrst', 'qrst', 'qrsu', 'qrst']) == "qrsu"
    assert candidate(words = ['abc', 'bcd', 'cde', 'ade']) == "ade"
    assert candidate(words = ['aab', 'aac', 'aba', 'aaa', 'aab', 'aac', 'aba', 'aac', 'aba', 'aab', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba', 'aac', 'aba']) == "aaa"
    assert candidate(words = ['abc', 'bcd', 'cde', 'bce']) == "bce"
    assert candidate(words = ['qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza']) == "yza"
    assert candidate(words = ['abc', 'bde', 'cef', 'dfg', 'efh', 'fij', 'gjk', 'hkl', 'ilm', 'jmn', 'kno', 'lop', 'mqr', 'nrs', 'ots', 'puv', 'qvw', 'rxy', 'syz', 'tza', 'uab', 'vbc', 'wcd', 'xey', 'yfz', 'zga']) == "abc"
    assert candidate(words = ['jkl', 'klm', 'lmn', 'mno', 'jklm']) == "jklm"
    assert candidate(words = ['mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'abc', 'bcd', 'cde']) == "yza"
    assert candidate(words = ['uvw', 'vwx', 'wxy', 'vxz', 'wyz']) == "vxz"
    assert candidate(words = ['xyz', 'wxy', 'vwx', 'uvw', 'tuv', 'stu', 'rst', 'qrs', 'pqr', 'opq', 'nop', 'mno', 'lnm', 'klj', 'ijk', 'hgf', 'fed', 'edc', 'dcb', 'cba', 'bca', 'cab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'bac']) == "lnm"
    assert candidate(words = ['pqr', 'qrs', 'rst', 'uvw', 'vwx', 'wxy', 'xyz', 'xya']) == "xya"
    assert candidate(words = ['abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefg']) == "abcdefh"
    assert candidate(words = ['aaa', 'abb', 'acc', 'add', 'aee', 'aff', 'agg', 'aeh', 'aei', 'aej', 'aek', 'ael', 'aem', 'aen', 'aeo', 'aep', 'aeq', 'aer', 'aes', 'aet', 'aeu', 'aev', 'aew', 'aex', 'aey', 'aez', 'afa', 'afb', 'afc', 'afd', 'afe', 'aff', 'afg', 'afh']) == "aaa"
    assert candidate(words = ['xyz', 'xza', 'ywb', 'ywa']) == "xyz"
    assert candidate(words = ['zzz', 'zzy', 'zzx', 'zzw', 'zzv']) == "zzz"
    assert candidate(words = ['mnop', 'nqpo', 'opqr', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwz', 'vwxy', 'wxza', 'xyzb', 'yzca', 'zcab', 'cabc', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrt', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwz', 'vwxy', 'wxza', 'xyzb', 'yzca', 'zcab', 'cabc', 'abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno']) == "nqpo"
    assert candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'bbaacceeddffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'ccaabbeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz']) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'geh', 'hif', 'iji', 'jik']) == "geh"
    assert candidate(words = ['qwert', 'wertr', 'ertty', 'rtyui', 'tyuio']) == "qwert"
    assert candidate(words = ['aaa', 'aab', 'aac', 'aad', 'zaa']) == "aaa"
    assert candidate(words = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzza']) == "zzzzzzzzza"
    assert candidate(words = ['zzz', 'zyz', 'xyx', 'wxw', 'vuq', 'tsr']) == "zzz"
    assert candidate(words = ['mnop', 'mnoq', 'mnop', 'mnoo', 'mnop']) == "mnoq"
    assert candidate(words = ['mno', 'nop', 'opo', 'npp', 'mqq']) == "opo"
    assert candidate(words = ['aaa', 'aba', 'aca', 'ada', 'aea', 'afa', 'aga', 'aha']) == "aaa"
    assert candidate(words = ['mnopqr', 'mnopqs', 'mnopqt', 'mnopqu', 'mnopqv']) == "mnopqr"
    assert candidate(words = ['qwe', 'rft', 'sgh', 'tij', 'ukl', 'vmo']) == "qwe"
    assert candidate(words = ['abcdef', 'abcefg', 'abcdgg', 'abcdef', 'abcdeg']) == "abcefg"
    assert candidate(words = ['abz', 'bca', 'cab', 'bac', 'acb', 'baa', 'aaa', 'aab']) == "abz"
    assert candidate(words = ['abz', 'bca', 'cab', 'abc']) == "abz"
    assert candidate(words = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah', 'aai', 'aaj', 'aak', 'aal', 'aam', 'aan', 'aao', 'aap', 'aaq', 'aar', 'aas', 'aat', 'aau', 'aav', 'aaw', 'aax', 'aay', 'aaz', 'abb', 'abc']) == "aaa"
    assert candidate(words = ['aab', 'aac', 'aab', 'aac', 'aab', 'aac', 'aad', 'aac']) == "aad"
    assert candidate(words = ['zzz', 'zyz', 'zyx', 'zzx', 'zyw']) == "zzz"
    assert candidate(words = ['uvw', 'uvx', 'uwy', 'uxz']) == "uvw"
    assert candidate(words = ['mnop', 'nqpr', 'opqs', 'pqrt']) == "mnop"
    assert candidate(words = ['zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzza']) == "zzzzzzzzzzzzzzzzzzza"
    assert candidate(words = ['xyz', 'yza', 'zab', 'xba', 'xza']) == "xyz"
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza']) == "yza"
    assert candidate(words = ['mnop', 'mnoq', 'mnop', 'mnop']) == "mnoq"
    assert candidate(words = ['pqr', 'qrs', 'rst', 'qst', 'qrt']) == "qst"
    assert candidate(words = ['aaa', 'aba', 'aca', 'ada', 'aea']) == "aaa"
    assert candidate(words = ['aaa', 'aab', 'aba', 'aca', 'baa']) == "aaa"
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxzz']) == "abcdefghijklmnopqrstuvwxzz"
    assert candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'aefghi']) == "aefghi"
    assert candidate(words = ['xyz', 'yza', 'zab', 'abc']) == "yza"
    assert candidate(words = ['xyz', 'xwv', 'xut', 'xsr']) == "xyz"
    assert candidate(words = ['uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aaa', 'aab', 'aac', 'aad', 'abe', 'acd']) == "aaa"
    assert candidate(words = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyx', 'vwxyxw', 'wxyxwy', 'xyxwyx', 'yxwyxy']) == "uvwxyx"
    assert candidate(words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']) == "aaaab"
    assert candidate(words = ['abcdefghijklmnop', 'bcdefghijklmno', 'cdefghijklmnop', 'dEefghijklmnop', 'efghijklmnopqr', 'fghijklmnopqrs', 'ghijklmnopqrst', 'hijklmnopqrstu', 'ijklmnopqrstuv', 'jklmnopqrstuvw', 'klmnopqrstuvwx', 'lmnopqrstuvwxy', 'mnopqrstuvwxyz']) == "abcdefghijklmnop"
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aaa', 'aab', 'aac', 'aad', 'abe']) == "yza"
    assert candidate(words = ['zzz', 'zzy', 'zyz', 'yzz', 'zyx', 'yxz', 'xzy', 'xyz', 'yxw', 'xyw', 'xwy', 'ywx', 'wxy', 'wyz', 'xzy', 'xyz', 'xwy', 'ywx', 'wxy', 'wyz', 'xzy', 'xyz', 'xwy', 'ywx']) == "zzz"
    assert candidate(words = ['mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyx', 'yzy', 'zzz', 'yzy', 'xyx', 'vwx', 'uvw', 'tuv', 'stu', 'qrs', 'pqr', 'opq', 'nop', 'mno', 'zyz', 'zzz']) == "zyz"
    assert candidate(words = ['zzz', 'aaa', 'aab', 'aac', 'aad']) == "aab"
    assert candidate(words = ['hello', 'hero', 'helq', 'herl']) == "hello"
    assert candidate(words = ['xyz', 'yza', 'zab', 'cab', 'bcd']) == "yza"
    assert candidate(words = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'aba', 'bab', 'bba', 'aab', 'aaa', 'aab', 'aba', 'abb', 'abc']) == "yza"
    assert candidate(words = ['zzz', 'yyy', 'xxz', 'xxy']) == "xxz"
    assert candidate(words = ['xyz', 'xza', 'xya', 'xwa']) == "xyz"
    assert candidate(words = ['ghi', 'hij', 'ijk', 'jkl', 'gij']) == "gij"
    assert candidate(words = ['pqr', 'qrs', 'rst', 'str']) == "str"
    assert candidate(words = ['zxy', 'zyx', 'yxz', 'yzy']) == "zxy"
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abcd', 'abcg']) == "abce"
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'yza', 'zab', 'cab', 'bca', 'abc', 'bca', 'cab', 'bac', 'acb', 'baa', 'aaa', 'aab', 'aac', 'aad', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc']) == "yza"
    assert candidate(words = ['apple', 'applf', 'applg', 'applh']) == "apple"
    assert candidate(words = ['zzz', 'yyz', 'xxz', 'wwz', 'vvz', 'uuz', 'ttz', 'ssz', 'rrz', 'qqz', 'ppz', 'opo', 'ono', 'nnm', 'nml', 'nkl', 'nlj', 'nik', 'ihj', 'igh', 'ifh', 'ieh', 'idh', 'ich', 'ibh', 'iah', 'azg', 'azy', 'ayx', 'axw', 'avv', 'auu', 'att', 'ass', 'arr', 'aqq', 'app', 'aoo', 'ano', 'aml', 'akl', 'ajk', 'aik', 'aih', 'aig', 'aif', 'aie', 'aid', 'aic', 'abh', 'aag', 'aaf', 'aae', 'aad', 'aac', 'aab']) == "zzz"
    assert candidate(words = ['qwe', 'rty', 'uio', 'pas', 'qdf']) == "qwe"
    assert candidate(words = ['aab', 'aac', 'aad', 'abe', 'bbf', 'ccg', 'ddd']) == "aab"


