def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx', 'xy', 'yx', 'xy', 'yx']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx', 'xy', 'yx', 'xy', 'yx']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'xy', 'yx', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'xy', 'yx', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cc', 'dd', 'dc', 'ca', 'ac']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cc', 'dd', 'dc', 'ca', 'ac']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cc', 'll', 'xx']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cc', 'll', 'xx']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 104: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mn', 'nm', 'op', 'po', 'qp', 'pq', 'rs', 'sr', 'tu', 'ut', 'vu', 'uv']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mn', 'nm', 'op', 'po', 'qp', 'pq', 'rs', 'sr', 'tu', 'ut', 'vu', 'uv']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zz', 'aa', 'bb', 'cc', 'zz', 'aa']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zz', 'aa', 'bb', 'cc', 'zz', 'aa']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 52: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ty', 'yt', 'lc', 'cl', 'ab']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ty', 'yt', 'lc', 'cl', 'ab']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['lc', 'cl', 'gg']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['lc', 'cl', 'gg']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aa', 'aa', 'aa']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aa', 'aa', 'aa']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aa', 'aa', 'aa', 'aa']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aa', 'aa', 'aa', 'aa']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cc', 'dd', 'ab', 'ba']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cc', 'dd', 'ab', 'ba']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 52: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']) == 52: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aa', 'aa', 'aa', 'ab', 'ba', 'ab', 'ba', 'ac', 'ca', 'ac', 'ca', 'ad', 'da', 'ad', 'da', 'ae', 'ea', 'ae', 'ea', 'af', 'fa', 'af', 'fa', 'ag', 'ga', 'ag', 'ga', 'ah', 'ha', 'ah', 'ha', 'ai', 'ia', 'ai', 'ia', 'aj', 'ja', 'aj', 'ja', 'ak', 'ka', 'ak', 'ka', 'al', 'la', 'al', 'la', 'am', 'ma', 'am', 'ma', 'an', 'na', 'an', 'na', 'ao', 'oa', 'ao', 'oa', 'ap', 'pa', 'ap', 'pa', 'aq', 'qa', 'aq', 'qa', 'ar', 'ra', 'ar', 'ra', 'as', 'sa', 'as', 'sa', 'at', 'ta', 'at', 'ta', 'au', 'ua', 'au', 'ua', 'av', 'va', 'av', 'va', 'aw', 'wa', 'aw', 'wa', 'ax', 'xa', 'ax', 'xa', 'ay', 'ya', 'ay', 'ya', 'az', 'za', 'az', 'za', 'bb', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd', 'ee', 'ee', 'ee', 'ee', 'ff', 'ff', 'ff', 'ff', 'gg', 'gg', 'gg', 'gg', 'hh', 'hh', 'hh', 'hh', 'ii', 'ii', 'ii', 'ii', 'jj', 'jj', 'jj', 'jj', 'kk', 'kk', 'kk', 'kk', 'll', 'll', 'll', 'll', 'mm', 'mm', 'mm', 'mm', 'nn', 'nn', 'nn', 'nn', 'oo', 'oo', 'oo', 'oo', 'pp', 'pp', 'pp', 'pp', 'qq', 'qq', 'qq', 'qq', 'rr', 'rr', 'rr', 'rr', 'ss', 'ss', 'ss', 'ss', 'tt', 'tt', 'tt', 'tt', 'uu', 'uu', 'uu', 'uu', 'vv', 'vv', 'vv', 'vv', 'ww', 'ww', 'ww', 'ww', 'xx', 'xx', 'xx', 'xx', 'yy', 'yy', 'yy', 'yy', 'zz', 'zz', 'zz', 'zz']) == 408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aa', 'aa', 'aa', 'ab', 'ba', 'ab', 'ba', 'ac', 'ca', 'ac', 'ca', 'ad', 'da', 'ad', 'da', 'ae', 'ea', 'ae', 'ea', 'af', 'fa', 'af', 'fa', 'ag', 'ga', 'ag', 'ga', 'ah', 'ha', 'ah', 'ha', 'ai', 'ia', 'ai', 'ia', 'aj', 'ja', 'aj', 'ja', 'ak', 'ka', 'ak', 'ka', 'al', 'la', 'al', 'la', 'am', 'ma', 'am', 'ma', 'an', 'na', 'an', 'na', 'ao', 'oa', 'ao', 'oa', 'ap', 'pa', 'ap', 'pa', 'aq', 'qa', 'aq', 'qa', 'ar', 'ra', 'ar', 'ra', 'as', 'sa', 'as', 'sa', 'at', 'ta', 'at', 'ta', 'au', 'ua', 'au', 'ua', 'av', 'va', 'av', 'va', 'aw', 'wa', 'aw', 'wa', 'ax', 'xa', 'ax', 'xa', 'ay', 'ya', 'ay', 'ya', 'az', 'za', 'az', 'za', 'bb', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd', 'ee', 'ee', 'ee', 'ee', 'ff', 'ff', 'ff', 'ff', 'gg', 'gg', 'gg', 'gg', 'hh', 'hh', 'hh', 'hh', 'ii', 'ii', 'ii', 'ii', 'jj', 'jj', 'jj', 'jj', 'kk', 'kk', 'kk', 'kk', 'll', 'll', 'll', 'll', 'mm', 'mm', 'mm', 'mm', 'nn', 'nn', 'nn', 'nn', 'oo', 'oo', 'oo', 'oo', 'pp', 'pp', 'pp', 'pp', 'qq', 'qq', 'qq', 'qq', 'rr', 'rr', 'rr', 'rr', 'ss', 'ss', 'ss', 'ss', 'tt', 'tt', 'tt', 'tt', 'uu', 'uu', 'uu', 'uu', 'vv', 'vv', 'vv', 'vv', 'ww', 'ww', 'ww', 'ww', 'xx', 'xx', 'xx', 'xx', 'yy', 'yy', 'yy', 'yy', 'zz', 'zz', 'zz', 'zz']) == 408: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'zz', 'yy', 'xx', 'ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'ee', 'dd', 'cc', 'bb', 'aa']) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'zz', 'yy', 'xx', 'ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'ee', 'dd', 'cc', 'bb', 'aa']) == 104: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zz', 'zz', 'xy', 'yx', 'yx', 'xy', 'ab', 'ba', 'ab', 'ba', 'zz', 'zz']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zz', 'zz', 'xy', 'yx', 'yx', 'xy', 'ab', 'ba', 'ab', 'ba', 'zz', 'zz']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz']) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz']) == 72: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx', 'xx', 'yy', 'xy', 'yx', 'xx', 'yy', 'xy', 'yx', 'xx', 'yy']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx', 'xx', 'yy', 'xy', 'yx', 'xx', 'yy', 'xy', 'yx', 'xx', 'yy']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'aa', 'bb', 'cc', 'dd', 'cc', 'dd', 'ee', 'ff', 'ee', 'ff']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'aa', 'bb', 'cc', 'dd', 'cc', 'dd', 'ee', 'ff', 'ee', 'ff']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']) == 64: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx', 'zz', 'zz', 'yx', 'xz', 'zx', 'zz']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx', 'zz', 'zz', 'yx', 'xz', 'zx', 'zz']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aa', 'aa', 'aa', 'bb', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd', 'ee', 'ee', 'ee', 'ee', 'ff', 'ff', 'ff', 'ff', 'gg', 'gg', 'gg', 'gg', 'hh', 'hh', 'hh', 'hh']) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aa', 'aa', 'aa', 'bb', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd', 'ee', 'ee', 'ee', 'ee', 'ff', 'ff', 'ff', 'ff', 'gg', 'gg', 'gg', 'gg', 'hh', 'hh', 'hh', 'hh']) == 64: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 112: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'cd', 'dc', 'cd', 'dc', 'ef', 'fe', 'ef', 'fe', 'gh', 'hg', 'gh', 'hg']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'cd', 'dc', 'cd', 'dc', 'ef', 'fe', 'ef', 'fe', 'gh', 'hg', 'gh', 'hg']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 54: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx', 'yx', 'xy', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx']) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx', 'yx', 'xy', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx']) == 304: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz']) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz']) == 112: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx', 'yy', 'xx', 'zz', 'zz', 'zz', 'zz', 'xy', 'yx', 'xx', 'yy', 'zz', 'zz']) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx', 'yy', 'xx', 'zz', 'zz', 'zz', 'zz', 'xy', 'yx', 'xx', 'yy', 'zz', 'zz']) == 28: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'xy', 'yx', 'xz', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy']) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'xy', 'yx', 'xz', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy']) == 30: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'cd', 'dc', 'ab', 'ba', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg']) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'cd', 'dc', 'ab', 'ba', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg']) == 76: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'af', 'fa', 'ag', 'ga', 'ah', 'ha', 'ai', 'ia', 'aj', 'ja', 'ak', 'ka', 'al', 'la', 'am', 'ma', 'an', 'na', 'ao', 'oa', 'ap', 'pa', 'aq', 'qa', 'ar', 'ra', 'as', 'sa', 'at', 'ta', 'au', 'ua', 'av', 'va', 'aw', 'wa', 'ax', 'xa', 'ay', 'ya', 'az', 'za', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'af', 'fa', 'ag', 'ga', 'ah', 'ha', 'ai', 'ia', 'aj', 'ja', 'ak', 'ka', 'al', 'la', 'am', 'ma', 'an', 'na', 'ao', 'oa', 'ap', 'pa', 'aq', 'qa', 'ar', 'ra', 'as', 'sa', 'at', 'ta', 'au', 'ua', 'av', 'va', 'aw', 'wa', 'ax', 'xa', 'ay', 'ya', 'az', 'za', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 102: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'aa', 'bb', 'cc', 'dd']) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'aa', 'bb', 'cc', 'dd']) == 30: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz']) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz']) == 88: {e}')
    
    total += 1
    try:
        result = candidate(words = ['qq', 'ww', 'ee', 'rr', 'tt', 'yy', 'uu', 'ii', 'oo', 'pp', 'aa', 'ss', 'dd', 'ff', 'gg', 'hh', 'jj', 'kk', 'll', 'zz', 'xx', 'cc', 'vv', 'bb', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'dd', 'ss', 'aa', 'pp', 'oo', 'nn', 'mm', 'zz', 'xx', 'vv', 'cc', 'uu', 'tt', 'rr', 'ee', 'ww', 'qq']) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qq', 'ww', 'ee', 'rr', 'tt', 'yy', 'uu', 'ii', 'oo', 'pp', 'aa', 'ss', 'dd', 'ff', 'gg', 'hh', 'jj', 'kk', 'll', 'zz', 'xx', 'cc', 'vv', 'bb', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'dd', 'ss', 'aa', 'pp', 'oo', 'nn', 'mm', 'zz', 'xx', 'vv', 'cc', 'uu', 'tt', 'rr', 'ee', 'ww', 'qq']) == 98: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz']) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz']) == 92: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zz', 'aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'dd', 'dd', 'ee', 'ee', 'ff', 'ff', 'gg', 'gg', 'hh', 'hh', 'ii', 'ii', 'jj', 'jj', 'kk', 'kk', 'll', 'll', 'mm', 'mm', 'nn', 'nn', 'oo', 'oo', 'pp', 'pp', 'qq', 'qq', 'rr', 'rr', 'ss', 'ss', 'tt', 'tt', 'uu', 'uu', 'vv', 'vv', 'ww', 'ww', 'xx', 'xx', 'yy', 'yy']) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zz', 'aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'dd', 'dd', 'ee', 'ee', 'ff', 'ff', 'gg', 'gg', 'hh', 'hh', 'ii', 'ii', 'jj', 'jj', 'kk', 'kk', 'll', 'll', 'mm', 'mm', 'nn', 'nn', 'oo', 'oo', 'pp', 'pp', 'qq', 'qq', 'rr', 'rr', 'ss', 'ss', 'tt', 'tt', 'uu', 'uu', 'vv', 'vv', 'ww', 'ww', 'xx', 'xx', 'yy', 'yy']) == 156: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc']) == 26: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['xy', 'yx', 'xy', 'yx', 'xy', 'yx']) == 12
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee']) == 2
    assert candidate(words = ['ab', 'ba', 'xy', 'yx', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz']) == 22
    assert candidate(words = ['ab', 'ba', 'cc', 'dd', 'dc', 'ca', 'ac']) == 10
    assert candidate(words = ['cc', 'll', 'xx']) == 2
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 104
    assert candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 16
    assert candidate(words = ['mn', 'nm', 'op', 'po', 'qp', 'pq', 'rs', 'sr', 'tu', 'ut', 'vu', 'uv']) == 24
    assert candidate(words = ['zz', 'aa', 'bb', 'cc', 'zz', 'aa']) == 10
    assert candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 52
    assert candidate(words = ['ab', 'ty', 'yt', 'lc', 'cl', 'ab']) == 8
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']) == 2
    assert candidate(words = ['lc', 'cl', 'gg']) == 6
    assert candidate(words = ['aa', 'aa', 'aa', 'aa']) == 8
    assert candidate(words = ['aa', 'aa', 'aa', 'aa', 'aa']) == 10
    assert candidate(words = ['ab', 'ba', 'cc', 'dd', 'ab', 'ba']) == 10
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 52
    assert candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 12
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 2
    assert candidate(words = ['aa', 'aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd']) == 26
    assert candidate(words = ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']) == 52
    assert candidate(words = ['aa', 'aa', 'aa', 'aa', 'ab', 'ba', 'ab', 'ba', 'ac', 'ca', 'ac', 'ca', 'ad', 'da', 'ad', 'da', 'ae', 'ea', 'ae', 'ea', 'af', 'fa', 'af', 'fa', 'ag', 'ga', 'ag', 'ga', 'ah', 'ha', 'ah', 'ha', 'ai', 'ia', 'ai', 'ia', 'aj', 'ja', 'aj', 'ja', 'ak', 'ka', 'ak', 'ka', 'al', 'la', 'al', 'la', 'am', 'ma', 'am', 'ma', 'an', 'na', 'an', 'na', 'ao', 'oa', 'ao', 'oa', 'ap', 'pa', 'ap', 'pa', 'aq', 'qa', 'aq', 'qa', 'ar', 'ra', 'ar', 'ra', 'as', 'sa', 'as', 'sa', 'at', 'ta', 'at', 'ta', 'au', 'ua', 'au', 'ua', 'av', 'va', 'av', 'va', 'aw', 'wa', 'aw', 'wa', 'ax', 'xa', 'ax', 'xa', 'ay', 'ya', 'ay', 'ya', 'az', 'za', 'az', 'za', 'bb', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd', 'ee', 'ee', 'ee', 'ee', 'ff', 'ff', 'ff', 'ff', 'gg', 'gg', 'gg', 'gg', 'hh', 'hh', 'hh', 'hh', 'ii', 'ii', 'ii', 'ii', 'jj', 'jj', 'jj', 'jj', 'kk', 'kk', 'kk', 'kk', 'll', 'll', 'll', 'll', 'mm', 'mm', 'mm', 'mm', 'nn', 'nn', 'nn', 'nn', 'oo', 'oo', 'oo', 'oo', 'pp', 'pp', 'pp', 'pp', 'qq', 'qq', 'qq', 'qq', 'rr', 'rr', 'rr', 'rr', 'ss', 'ss', 'ss', 'ss', 'tt', 'tt', 'tt', 'tt', 'uu', 'uu', 'uu', 'uu', 'vv', 'vv', 'vv', 'vv', 'ww', 'ww', 'ww', 'ww', 'xx', 'xx', 'xx', 'xx', 'yy', 'yy', 'yy', 'yy', 'zz', 'zz', 'zz', 'zz']) == 408
    assert candidate(words = ['ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji']) == 24
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'zz', 'yy', 'xx', 'ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'ee', 'dd', 'cc', 'bb', 'aa']) == 104
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']) == 18
    assert candidate(words = ['zz', 'zz', 'xy', 'yx', 'yx', 'xy', 'ab', 'ba', 'ab', 'ba', 'zz', 'zz']) == 24
    assert candidate(words = ['ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'ab', 'ba', 'xy', 'yx', 'zy', 'yz']) == 72
    assert candidate(words = ['xy', 'yx', 'xx', 'yy', 'xy', 'yx', 'xx', 'yy', 'xy', 'yx', 'xx', 'yy']) == 22
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 18
    assert candidate(words = ['aa', 'bb', 'aa', 'bb', 'cc', 'dd', 'cc', 'dd', 'ee', 'ff', 'ee', 'ff']) == 24
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']) == 64
    assert candidate(words = ['xy', 'yx', 'zz', 'zz', 'yx', 'xz', 'zx', 'zz']) == 14
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd', 'aa']) == 18
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk']) == 24
    assert candidate(words = ['aa', 'aa', 'aa', 'aa', 'bb', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc', 'cc', 'dd', 'dd', 'dd', 'dd', 'ee', 'ee', 'ee', 'ee', 'ff', 'ff', 'ff', 'ff', 'gg', 'gg', 'gg', 'gg', 'hh', 'hh', 'hh', 'hh']) == 64
    assert candidate(words = ['ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'xy', 'yx', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 112
    assert candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba', 'cd', 'dc', 'cd', 'dc', 'ef', 'fe', 'ef', 'fe', 'gh', 'hg', 'gh', 'hg']) == 36
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 54
    assert candidate(words = ['xy', 'yx', 'yx', 'xy', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx', 'xy', 'xy', 'yx', 'yx']) == 304
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db']) == 20
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz']) == 112
    assert candidate(words = ['xy', 'yx', 'yy', 'xx', 'zz', 'zz', 'zz', 'zz', 'xy', 'yx', 'xx', 'yy', 'zz', 'zz']) == 28
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'xy', 'yx', 'xz', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy', 'yx', 'zx', 'yz', 'zy']) == 30
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'cd', 'dc', 'ab', 'ba', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg']) == 76
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'af', 'fa', 'ag', 'ga', 'ah', 'ha', 'ai', 'ia', 'aj', 'ja', 'ak', 'ka', 'al', 'la', 'am', 'ma', 'an', 'na', 'ao', 'oa', 'ap', 'pa', 'aq', 'qa', 'ar', 'ra', 'as', 'sa', 'at', 'ta', 'au', 'ua', 'av', 'va', 'aw', 'wa', 'ax', 'xa', 'ay', 'ya', 'az', 'za', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 102
    assert candidate(words = ['mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'aa', 'bb', 'cc', 'dd']) == 30
    assert candidate(words = ['ab', 'ba', 'xy', 'yx', 'zy', 'yz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp']) == 14
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz', 'yz', 'zy', 'zx', 'xz']) == 88
    assert candidate(words = ['qq', 'ww', 'ee', 'rr', 'tt', 'yy', 'uu', 'ii', 'oo', 'pp', 'aa', 'ss', 'dd', 'ff', 'gg', 'hh', 'jj', 'kk', 'll', 'zz', 'xx', 'cc', 'vv', 'bb', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'dd', 'ss', 'aa', 'pp', 'oo', 'nn', 'mm', 'zz', 'xx', 'vv', 'cc', 'uu', 'tt', 'rr', 'ee', 'ww', 'qq']) == 98
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz', 'zz']) == 92
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zz', 'aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'dd', 'dd', 'ee', 'ee', 'ff', 'ff', 'gg', 'gg', 'hh', 'hh', 'ii', 'ii', 'jj', 'jj', 'kk', 'kk', 'll', 'll', 'mm', 'mm', 'nn', 'nn', 'oo', 'oo', 'pp', 'pp', 'qq', 'qq', 'rr', 'rr', 'ss', 'ss', 'tt', 'tt', 'uu', 'uu', 'vv', 'vv', 'ww', 'ww', 'xx', 'xx', 'yy', 'yy']) == 156
    assert candidate(words = ['aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc']) == 26


