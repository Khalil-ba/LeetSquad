def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(products = ['keyboard', 'keypad', 'keys', 'kick'],searchWord = "key") == [['keyboard', 'keypad', 'keys'], ['keyboard', 'keypad', 'keys'], ['keyboard', 'keypad', 'keys']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['keyboard', 'keypad', 'keys', 'kick'],searchWord = "key") == [['keyboard', 'keypad', 'keys'], ['keyboard', 'keypad', 'keys'], ['keyboard', 'keypad', 'keys']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['keyboard', 'keypad', 'mousepad'],searchWord = "key") == [['keyboard', 'keypad'], ['keyboard', 'keypad'], ['keyboard', 'keypad']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['keyboard', 'keypad', 'mousepad'],searchWord = "key") == [['keyboard', 'keypad'], ['keyboard', 'keypad'], ['keyboard', 'keypad']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'banana', 'grape', 'orange'],searchWord = "or") == [['orange'], ['orange']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'banana', 'grape', 'orange'],searchWord = "or") == [['orange'], ['orange']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aaa', 'aaab', 'aaac', 'aab'],searchWord = "aa") == [['aaa', 'aaab', 'aaac'], ['aaa', 'aaab', 'aaac']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aaa', 'aaab', 'aaac', 'aab'],searchWord = "aa") == [['aaa', 'aaab', 'aaac'], ['aaa', 'aaab', 'aaac']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['charger', 'cable', 'case'],searchWord = "ca") == [['cable', 'case', 'charger'], ['cable', 'case']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['charger', 'cable', 'case'],searchWord = "ca") == [['cable', 'case', 'charger'], ['cable', 'case']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['bag', 'bags', 'banner', 'box', 'car'],searchWord = "ba") == [['bag', 'bags', 'banner'], ['bag', 'bags', 'banner']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['bag', 'bags', 'banner', 'box', 'car'],searchWord = "ba") == [['bag', 'bags', 'banner'], ['bag', 'bags', 'banner']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aaa', 'aab', 'aac', 'aad', 'aae'],searchWord = "aa") == [['aaa', 'aab', 'aac'], ['aaa', 'aab', 'aac']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aaa', 'aab', 'aac', 'aad', 'aae'],searchWord = "aa") == [['aaa', 'aab', 'aac'], ['aaa', 'aab', 'aac']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aaa', 'aab', 'aac', 'aad'],searchWord = "aa") == [['aaa', 'aab', 'aac'], ['aaa', 'aab', 'aac']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aaa', 'aab', 'aac', 'aad'],searchWord = "aa") == [['aaa', 'aab', 'aac'], ['aaa', 'aab', 'aac']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apples', 'application'],searchWord = "app") == [['apple', 'apples', 'application'], ['apple', 'apples', 'application'], ['apple', 'apples', 'application']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apples', 'application'],searchWord = "app") == [['apple', 'apples', 'application'], ['apple', 'apples', 'application'], ['apple', 'apples', 'application']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'banana', 'grape', 'orange'],searchWord = "ba") == [['banana'], ['banana']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'banana', 'grape', 'orange'],searchWord = "ba") == [['banana'], ['banana']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['keyboard', 'keypad', 'keyboard', 'keychain'],searchWord = "key") == [['keyboard', 'keyboard', 'keychain'], ['keyboard', 'keyboard', 'keychain'], ['keyboard', 'keyboard', 'keychain']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['keyboard', 'keypad', 'keyboard', 'keychain'],searchWord = "key") == [['keyboard', 'keyboard', 'keychain'], ['keyboard', 'keyboard', 'keychain'], ['keyboard', 'keyboard', 'keychain']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['havana'],searchWord = "havana") == [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['havana'],searchWord = "havana") == [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['keyboard', 'keypad', 'kiosk'],searchWord = "key") == [['keyboard', 'keypad', 'kiosk'], ['keyboard', 'keypad'], ['keyboard', 'keypad']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['keyboard', 'keypad', 'kiosk'],searchWord = "key") == [['keyboard', 'keypad', 'kiosk'], ['keyboard', 'keypad'], ['keyboard', 'keypad']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'banana', 'grape', 'orange', 'peach'],searchWord = "app") == [['apple'], ['apple'], ['apple']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'banana', 'grape', 'orange', 'peach'],searchWord = "app") == [['apple'], ['apple'], ['apple']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['keyboard', 'keypad', 'keyboardpad'],searchWord = "key") == [['keyboard', 'keyboardpad', 'keypad'], ['keyboard', 'keyboardpad', 'keypad'], ['keyboard', 'keyboardpad', 'keypad']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['keyboard', 'keypad', 'keyboardpad'],searchWord = "key") == [['keyboard', 'keyboardpad', 'keypad'], ['keyboard', 'keyboardpad', 'keypad'], ['keyboard', 'keyboardpad', 'keypad']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'],searchWord = "mouse") == [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'],searchWord = "mouse") == [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aardvark', 'aardwolf', 'albatross', 'alligator', 'alpaca', 'antelope', 'anteater'],searchWord = "aa") == [['aardvark', 'aardwolf', 'albatross'], ['aardvark', 'aardwolf']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aardvark', 'aardwolf', 'albatross', 'alligator', 'alpaca', 'antelope', 'anteater'],searchWord = "aa") == [['aardvark', 'aardwolf', 'albatross'], ['aardvark', 'aardwolf']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['xylophone', 'xylography', 'xylem', 'xenon', 'xerox', 'xerophyte', 'xenodochial'],searchWord = "xero") == [['xenodochial', 'xenon', 'xerophyte'], ['xenodochial', 'xenon', 'xerophyte'], ['xerophyte', 'xerox'], ['xerophyte', 'xerox']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['xylophone', 'xylography', 'xylem', 'xenon', 'xerox', 'xerophyte', 'xenodochial'],searchWord = "xero") == [['xenodochial', 'xenon', 'xerophyte'], ['xenodochial', 'xenon', 'xerophyte'], ['xerophyte', 'xerox'], ['xerophyte', 'xerox']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['jacket', 'jaguar', 'jar', 'jasmine', 'jeep'],searchWord = "ja") == [['jacket', 'jaguar', 'jar'], ['jacket', 'jaguar', 'jar']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['jacket', 'jaguar', 'jar', 'jasmine', 'jeep'],searchWord = "ja") == [['jacket', 'jaguar', 'jar'], ['jacket', 'jaguar', 'jar']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['ant', 'anteater', 'antelope', 'antenna', 'antique', 'antfarm', 'antler'],searchWord = "ant") == [['ant', 'anteater', 'antelope'], ['ant', 'anteater', 'antelope'], ['ant', 'anteater', 'antelope']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['ant', 'anteater', 'antelope', 'antenna', 'antique', 'antfarm', 'antler'],searchWord = "ant") == [['ant', 'anteater', 'antelope'], ['ant', 'anteater', 'antelope'], ['ant', 'anteater', 'antelope']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['television', 'telescope', 'temperature', 'tennis', 'tense'],searchWord = "te") == [['telescope', 'television', 'temperature'], ['telescope', 'television', 'temperature']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['television', 'telescope', 'temperature', 'tennis', 'tense'],searchWord = "te") == [['telescope', 'television', 'temperature'], ['telescope', 'television', 'temperature']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry'],searchWord = "b") == [['banana', 'bat', 'berry']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry'],searchWord = "b") == [['banana', 'bat', 'berry']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['grape', 'grapefruit', 'grapevine', 'graph', 'grapejuice'],searchWord = "gr") == [['grape', 'grapefruit', 'grapejuice'], ['grape', 'grapefruit', 'grapejuice']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['grape', 'grapefruit', 'grapevine', 'graph', 'grapejuice'],searchWord = "gr") == [['grape', 'grapefruit', 'grapejuice'], ['grape', 'grapefruit', 'grapejuice']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['dog', 'dolphin', 'dome', 'domestic', 'domino'],searchWord = "dom") == [['dog', 'dolphin', 'dome'], ['dog', 'dolphin', 'dome'], ['dome', 'domestic', 'domino']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['dog', 'dolphin', 'dome', 'domestic', 'domino'],searchWord = "dom") == [['dog', 'dolphin', 'dome'], ['dog', 'dolphin', 'dome'], ['dome', 'domestic', 'domino']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['magnifier', 'magnificent', 'magnet', 'magnolia', 'magnitude'],searchWord = "magn") == [['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['magnifier', 'magnificent', 'magnet', 'magnolia', 'magnitude'],searchWord = "magn") == [['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'application', 'appliance', 'appropriate', 'appetizer'],searchWord = "appl") == [['appetizer', 'apple', 'appliance'], ['appetizer', 'apple', 'appliance'], ['appetizer', 'apple', 'appliance'], ['apple', 'appliance', 'application']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'application', 'appliance', 'appropriate', 'appetizer'],searchWord = "appl") == [['appetizer', 'apple', 'appliance'], ['appetizer', 'apple', 'appliance'], ['appetizer', 'apple', 'appliance'], ['apple', 'appliance', 'application']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['grape', 'grapefruit', 'grapejuice', 'graphite', 'grapevine', 'grapefruitjuice'],searchWord = "grape") == [['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['grape', 'grapefruit', 'grapejuice', 'graphite', 'grapevine', 'grapefruitjuice'],searchWord = "grape") == [['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['algorithm', 'array', 'binary', 'bit', 'bitset', 'bucket', 'class', 'collection', 'datatype', 'enumerate', 'file', 'float', 'function', 'garbage', 'graph', 'hash', 'id', 'implementation', 'integer', 'java', 'keyword', 'list', 'map', 'namespace', 'None', 'object', 'operator', 'pair', 'pointer', 'queue', 'range', 'reference', 'set', 'stack', 'string', 'struct', 'template', 'typedef', 'union', 'variable', 'while', 'xor'],searchWord = "algo") == [['algorithm', 'array'], ['algorithm'], ['algorithm'], ['algorithm']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['algorithm', 'array', 'binary', 'bit', 'bitset', 'bucket', 'class', 'collection', 'datatype', 'enumerate', 'file', 'float', 'function', 'garbage', 'graph', 'hash', 'id', 'implementation', 'integer', 'java', 'keyword', 'list', 'map', 'namespace', 'None', 'object', 'operator', 'pair', 'pointer', 'queue', 'range', 'reference', 'set', 'stack', 'string', 'struct', 'template', 'typedef', 'union', 'variable', 'while', 'xor'],searchWord = "algo") == [['algorithm', 'array'], ['algorithm'], ['algorithm'], ['algorithm']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['hamburger', 'hammock', 'hammer', 'hammerhead', 'handheld'],searchWord = "ham") == [['hamburger', 'hammer', 'hammerhead'], ['hamburger', 'hammer', 'hammerhead'], ['hamburger', 'hammer', 'hammerhead']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['hamburger', 'hammock', 'hammer', 'hammerhead', 'handheld'],searchWord = "ham") == [['hamburger', 'hammer', 'hammerhead'], ['hamburger', 'hammer', 'hammerhead'], ['hamburger', 'hammer', 'hammerhead']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['watermelon', 'water', 'wave', 'wonder', 'wonderland'],searchWord = "wat") == [['water', 'watermelon', 'wave'], ['water', 'watermelon', 'wave'], ['water', 'watermelon']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['watermelon', 'water', 'wave', 'wonder', 'wonderland'],searchWord = "wat") == [['water', 'watermelon', 'wave'], ['water', 'watermelon', 'wave'], ['water', 'watermelon']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['amazon', 'amazing', 'ambassador', 'ambient', 'amplifier'],searchWord = "ambi") == [['amazing', 'amazon', 'ambassador'], ['amazing', 'amazon', 'ambassador'], ['ambassador', 'ambient'], ['ambient']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['amazon', 'amazing', 'ambassador', 'ambient', 'amplifier'],searchWord = "ambi") == [['amazing', 'amazon', 'ambassador'], ['amazing', 'amazon', 'ambassador'], ['ambassador', 'ambient'], ['ambient']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['xylophone', 'xylography', 'xylophone', 'xylophone', 'xylophone'],searchWord = "xylo") == [['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['xylophone', 'xylography', 'xylophone', 'xylophone', 'xylophone'],searchWord = "xylo") == [['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['car', 'card', 'cardboard', 'cargo', 'cartoon'],searchWord = "car") == [['car', 'card', 'cardboard'], ['car', 'card', 'cardboard'], ['car', 'card', 'cardboard']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['car', 'card', 'cardboard', 'cargo', 'cartoon'],searchWord = "car") == [['car', 'card', 'cardboard'], ['car', 'card', 'cardboard'], ['car', 'card', 'cardboard']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm'],searchWord = "abc") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm'],searchWord = "abc") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zinc', 'zoo', 'zesty', 'zoning', 'zest', 'zookeeper'],searchWord = "ze") == [['zebra', 'zest', 'zesty'], ['zebra', 'zest', 'zesty']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zinc', 'zoo', 'zesty', 'zoning', 'zest', 'zookeeper'],searchWord = "ze") == [['zebra', 'zest', 'zesty'], ['zebra', 'zest', 'zesty']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aardvark', 'aardwolf', 'aardvark', 'aardvark', 'aardvark'],searchWord = "aard") == [['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aardvark', 'aardwolf', 'aardvark', 'aardvark', 'aardvark'],searchWord = "aard") == [['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['umbrella', 'umber', 'umbilical', 'umbrella', 'umbrella'],searchWord = "umb") == [['umber', 'umbilical', 'umbrella'], ['umber', 'umbilical', 'umbrella'], ['umber', 'umbilical', 'umbrella']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['umbrella', 'umber', 'umbilical', 'umbrella', 'umbrella'],searchWord = "umb") == [['umber', 'umbilical', 'umbrella'], ['umber', 'umbilical', 'umbrella'], ['umber', 'umbilical', 'umbrella']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij'],searchWord = "abcdefghijk") == [['a', 'ab', 'abc'], ['ab', 'abc', 'abcd'], ['abc', 'abcd', 'abcde'], ['abcd', 'abcde', 'abcdef'], ['abcde', 'abcdef', 'abcdefg'], ['abcdef', 'abcdefg', 'abcdefgh'], ['abcdefg', 'abcdefgh', 'abcdefghi'], ['abcdefgh', 'abcdefghi', 'abcdefghij'], ['abcdefghi', 'abcdefghij'], ['abcdefghij'], []]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij'],searchWord = "abcdefghijk") == [['a', 'ab', 'abc'], ['ab', 'abc', 'abcd'], ['abc', 'abcd', 'abcde'], ['abcd', 'abcde', 'abcdef'], ['abcde', 'abcdef', 'abcdefg'], ['abcdef', 'abcdefg', 'abcdefgh'], ['abcdefg', 'abcdefgh', 'abcdefghi'], ['abcdefgh', 'abcdefghi', 'abcdefghij'], ['abcdefghi', 'abcdefghij'], ['abcdefghij'], []]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blueberry', 'blackberry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blueberry', 'blackberry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zebrafish', 'zebrafly', 'zebratail', 'zebralight', 'zebrashoe', 'zebragram', 'zebratic', 'zebrastriped'],searchWord = "zebra") == [['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zebrafish', 'zebrafly', 'zebratail', 'zebralight', 'zebrashoe', 'zebragram', 'zebratic', 'zebrastriped'],searchWord = "zebra") == [['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['infinite', 'infinity', 'infinitesimal', 'infinity', 'infinitary'],searchWord = "inf") == [['infinitary', 'infinite', 'infinitesimal'], ['infinitary', 'infinite', 'infinitesimal'], ['infinitary', 'infinite', 'infinitesimal']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['infinite', 'infinity', 'infinitesimal', 'infinity', 'infinitary'],searchWord = "inf") == [['infinitary', 'infinite', 'infinitesimal'], ['infinitary', 'infinite', 'infinitesimal'], ['infinitary', 'infinite', 'infinitesimal']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['orange', 'oregano', 'organ', 'organize', 'organism'],searchWord = "org") == [['orange', 'oregano', 'organ'], ['orange', 'oregano', 'organ'], ['organ', 'organism', 'organize']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['orange', 'oregano', 'organ', 'organize', 'organism'],searchWord = "org") == [['orange', 'oregano', 'organ'], ['orange', 'oregano', 'organ'], ['organ', 'organism', 'organize']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['xenon', 'xerox', 'xenophobe', 'xenial', 'xenolith', 'xenoliths', 'xenonarc', 'xenonarcosis', 'xenolithologist'],searchWord = "xen") == [['xenial', 'xenolith', 'xenolithologist'], ['xenial', 'xenolith', 'xenolithologist'], ['xenial', 'xenolith', 'xenolithologist']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['xenon', 'xerox', 'xenophobe', 'xenial', 'xenolith', 'xenoliths', 'xenonarc', 'xenonarcosis', 'xenolithologist'],searchWord = "xen") == [['xenial', 'xenolith', 'xenolithologist'], ['xenial', 'xenolith', 'xenolithologist'], ['xenial', 'xenolith', 'xenolithologist']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aab', 'aac', 'aad', 'aaf', 'aag'],searchWord = "aa") == [['a', 'aa', 'aaa'], ['aa', 'aaa', 'aaaa']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aab', 'aac', 'aad', 'aaf', 'aag'],searchWord = "aa") == [['a', 'aa', 'aaa'], ['aa', 'aaa', 'aaaa']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['laptop', 'laptopbag', 'laser', 'lateral', 'latitude'],searchWord = "lap") == [['laptop', 'laptopbag', 'laser'], ['laptop', 'laptopbag', 'laser'], ['laptop', 'laptopbag']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['laptop', 'laptopbag', 'laser', 'lateral', 'latitude'],searchWord = "lap") == [['laptop', 'laptopbag', 'laser'], ['laptop', 'laptopbag', 'laser'], ['laptop', 'laptopbag']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['cherry', 'cranberry', 'cantaloupe', 'carrot', 'corn', 'cucumber'],searchWord = "car") == [['cantaloupe', 'carrot', 'cherry'], ['cantaloupe', 'carrot'], ['carrot']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['cherry', 'cranberry', 'cantaloupe', 'carrot', 'corn', 'cucumber'],searchWord = "car") == [['cantaloupe', 'carrot', 'cherry'], ['cantaloupe', 'carrot'], ['carrot']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella'],searchWord = "umbrella") == [['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella'],searchWord = "umbrella") == [['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aardvark', 'aardwolf', 'albatross', 'albino', 'alligator', 'alpaca', 'almighty'],searchWord = "al") == [['aardvark', 'aardwolf', 'albatross'], ['albatross', 'albino', 'alligator']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aardvark', 'aardwolf', 'albatross', 'albino', 'alligator', 'alpaca', 'almighty'],searchWord = "al") == [['aardvark', 'aardwolf', 'albatross'], ['albatross', 'albino', 'alligator']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zealot', 'zealous', 'zebrafish', 'zebra', 'zebrahead'],searchWord = "ze") == [['zealot', 'zealous', 'zebra'], ['zealot', 'zealous', 'zebra']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zealot', 'zealous', 'zebrafish', 'zebra', 'zebrahead'],searchWord = "ze") == [['zealot', 'zealous', 'zebra'], ['zealot', 'zealous', 'zebra']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['navigate', 'navigation', 'navigator', 'navy', 'navel'],searchWord = "nav") == [['navel', 'navigate', 'navigation'], ['navel', 'navigate', 'navigation'], ['navel', 'navigate', 'navigation']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['navigate', 'navigation', 'navigator', 'navy', 'navel'],searchWord = "nav") == [['navel', 'navigate', 'navigation'], ['navel', 'navigate', 'navigation'], ['navel', 'navigate', 'navigation']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['electronics', 'electric', 'elephant', 'elbow', 'eleven'],searchWord = "ele") == [['elbow', 'electric', 'electronics'], ['elbow', 'electric', 'electronics'], ['electric', 'electronics', 'elephant']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['electronics', 'electric', 'elephant', 'elbow', 'eleven'],searchWord = "ele") == [['elbow', 'electric', 'electronics'], ['elbow', 'electric', 'electronics'], ['electric', 'electronics', 'elephant']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry', 'bluebird', 'bluetooth'],searchWord = "bl") == [['banana', 'bat', 'berry'], ['blackberry', 'blueberry', 'bluebird']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry', 'bluebird', 'bluetooth'],searchWord = "bl") == [['banana', 'bat', 'berry'], ['blackberry', 'blueberry', 'bluebird']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['abacaxi', 'abalone', 'abana', 'abanga', 'abaperture', 'abara', 'abaraxas', 'abarth', 'abart', 'abat', 'abate', 'abati', 'abatis', 'abator', 'abatt', 'abature', 'abavure', 'abaya', 'abaze', 'abba', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe'],searchWord = "ab") == [['abacaxi', 'abalone', 'abana'], ['abacaxi', 'abalone', 'abana']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['abacaxi', 'abalone', 'abana', 'abanga', 'abaperture', 'abara', 'abaraxas', 'abarth', 'abart', 'abat', 'abate', 'abati', 'abatis', 'abator', 'abatt', 'abature', 'abavure', 'abaya', 'abaze', 'abba', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe'],searchWord = "ab") == [['abacaxi', 'abalone', 'abana'], ['abacaxi', 'abalone', 'abana']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['applepie', 'applesauce', 'appleskin', 'apple', 'applejack'],searchWord = "appl") == [['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['applepie', 'applesauce', 'appleskin', 'apple', 'applejack'],searchWord = "appl") == [['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['camera', 'camcorder', 'cameralens', 'cameraman', 'cameraobscura', 'camouflage', 'camcorder', 'camera', 'camcorder'],searchWord = "cam") == [['camcorder', 'camcorder', 'camcorder'], ['camcorder', 'camcorder', 'camcorder'], ['camcorder', 'camcorder', 'camcorder']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['camera', 'camcorder', 'cameralens', 'cameraman', 'cameraobscura', 'camouflage', 'camcorder', 'camera', 'camcorder'],searchWord = "cam") == [['camcorder', 'camcorder', 'camcorder'], ['camcorder', 'camcorder', 'camcorder'], ['camcorder', 'camcorder', 'camcorder']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['chocolate', 'chocolatebar', 'chocolatechip', 'chocolate', 'chocolatefudge'],searchWord = "chocolate") == [['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['chocolate', 'chocolatebar', 'chocolatechip', 'chocolate', 'chocolatefudge'],searchWord = "chocolate") == [['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['queen', 'queens', 'queenship', 'queer', 'queue'],searchWord = "quee") == [['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['queen', 'queens', 'queenship', 'queer', 'queue'],searchWord = "quee") == [['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apricot', 'avocado', 'banana', 'bat', 'berry', 'blackberry', 'blueberry', 'cherry', 'cantaloupe', 'cranberry'],searchWord = "ap") == [['apple', 'apricot', 'avocado'], ['apple', 'apricot']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apricot', 'avocado', 'banana', 'bat', 'berry', 'blackberry', 'blueberry', 'cherry', 'cantaloupe', 'cranberry'],searchWord = "ap") == [['apple', 'apricot', 'avocado'], ['apple', 'apricot']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['applepie', 'applesauce', 'apple', 'appletart', 'apples', 'apricot'],searchWord = "apple") == [['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['applepie', 'applesauce', 'apple', 'appletart', 'apples', 'apricot'],searchWord = "apple") == [['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['guitar', 'guitarcase', 'guitarhero', 'guitarpick', 'guitarstand', 'guitartuner', 'guitarstring'],searchWord = "gu") == [['guitar', 'guitarcase', 'guitarhero'], ['guitar', 'guitarcase', 'guitarhero']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['guitar', 'guitarcase', 'guitarhero', 'guitarpick', 'guitarstand', 'guitartuner', 'guitarstring'],searchWord = "gu") == [['guitar', 'guitarcase', 'guitarhero'], ['guitar', 'guitarcase', 'guitarhero']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['ocean', 'ocelot', 'octopus', 'octagon', 'octagonal'],searchWord = "oct") == [['ocean', 'ocelot', 'octagon'], ['ocean', 'ocelot', 'octagon'], ['octagon', 'octagonal', 'octopus']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['ocean', 'ocelot', 'octopus', 'octagon', 'octagonal'],searchWord = "oct") == [['ocean', 'ocelot', 'octagon'], ['ocean', 'ocelot', 'octagon'], ['octagon', 'octagonal', 'octopus']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant'],searchWord = "elephant") == [['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant'],searchWord = "elephant") == [['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['chocolate', 'chips', 'chipmunk', 'cheese', 'cherry', 'chili'],searchWord = "ch") == [['cheese', 'cherry', 'chili'], ['cheese', 'cherry', 'chili']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['chocolate', 'chips', 'chipmunk', 'cheese', 'cherry', 'chili'],searchWord = "ch") == [['cheese', 'cherry', 'chili'], ['cheese', 'cherry', 'chili']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch'],searchWord = "abc") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch'],searchWord = "abc") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zulu', 'zymurgy', 'zestful', 'zestfully', 'zestless', 'zippy', 'zoo', 'zoology', 'zucchini'],searchWord = "zoo") == [['zebra', 'zestful', 'zestfully'], ['zoo', 'zoology'], ['zoo', 'zoology']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zulu', 'zymurgy', 'zestful', 'zestfully', 'zestless', 'zippy', 'zoo', 'zoology', 'zucchini'],searchWord = "zoo") == [['zebra', 'zestful', 'zestfully'], ['zoo', 'zoology'], ['zoo', 'zoology']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['fishing', 'fishtank', 'fish', 'fishmonger', 'fisherman', 'fishhook', 'fishnet'],searchWord = "fish") == [['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['fishing', 'fishtank', 'fish', 'fishmonger', 'fisherman', 'fishhook', 'fishnet'],searchWord = "fish") == [['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['watermelon', 'water', 'waterproof', 'watering', 'waterfall', 'watermelon', 'watercolor', 'watergun', 'watermelon', 'watermark'],searchWord = "waterm") == [['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['watermark', 'watermelon', 'watermelon']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['watermelon', 'water', 'waterproof', 'watering', 'waterfall', 'watermelon', 'watercolor', 'watergun', 'watermelon', 'watermark'],searchWord = "waterm") == [['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['watermark', 'watermelon', 'watermelon']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['banana', 'band', 'bangalore', 'bank', 'banner'],searchWord = "ban") == [['banana', 'band', 'bangalore'], ['banana', 'band', 'bangalore'], ['banana', 'band', 'bangalore']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['banana', 'band', 'bangalore', 'bank', 'banner'],searchWord = "ban") == [['banana', 'band', 'bangalore'], ['banana', 'band', 'bangalore'], ['banana', 'band', 'bangalore']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['paint', 'painter', 'painting', 'paintball', 'paintbrush'],searchWord = "pain") == [['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['paint', 'painter', 'painting', 'paintball', 'paintbrush'],searchWord = "pain") == [['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['xyz', 'xylophone', 'xylography', 'xylograph', 'xylography', 'xylographer', 'xylographs', 'xylography', 'xylography'],searchWord = "xylo") == [['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['xyz', 'xylophone', 'xylography', 'xylograph', 'xylography', 'xylographer', 'xylographs', 'xylography', 'xylography'],searchWord = "xylo") == [['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['microphone', 'microwave', 'microscope', 'microphone', 'micronutrient'],searchWord = "micr") == [['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['microphone', 'microwave', 'microscope', 'microphone', 'micronutrient'],searchWord = "micr") == [['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['flower', 'flour', 'flow', 'flourish', 'flourmill'],searchWord = "flow") == [['flour', 'flourish', 'flourmill'], ['flour', 'flourish', 'flourmill'], ['flour', 'flourish', 'flourmill'], ['flow', 'flower']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['flower', 'flour', 'flow', 'flourish', 'flourmill'],searchWord = "flow") == [['flour', 'flourish', 'flourmill'], ['flour', 'flourish', 'flourmill'], ['flour', 'flourish', 'flourmill'], ['flow', 'flower']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['car', 'card', 'care', 'careful', 'careless'],searchWord = "ca") == [['car', 'card', 'care'], ['car', 'card', 'care']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['car', 'card', 'care', 'careful', 'careless'],searchWord = "ca") == [['car', 'card', 'care'], ['car', 'card', 'care']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['football', 'footwear', 'footbridge', 'footnote', 'footrest', 'footlocker', 'footrace', 'footlight'],searchWord = "foot") == [['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['football', 'footwear', 'footbridge', 'footnote', 'footrest', 'footlocker', 'footrace', 'footlight'],searchWord = "foot") == [['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['bicycle', 'bicycling', 'bicycle', 'bicycle', 'bicycle'],searchWord = "bicy") == [['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['bicycle', 'bicycling', 'bicycle', 'bicycle', 'bicycle'],searchWord = "bicy") == [['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe'],searchWord = "giraff") == [['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe'],searchWord = "giraff") == [['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['strawberry', 'straw', 'stratosphere', 'stranger', 'strategy'],searchWord = "stra") == [['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['strawberry', 'straw', 'stratosphere', 'stranger', 'strategy'],searchWord = "stra") == [['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['watermelon', 'water', 'waterfall', 'watershed', 'watercolor'],searchWord = "water") == [['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['watermelon', 'water', 'waterfall', 'watershed', 'watercolor'],searchWord = "water") == [['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['computer', 'computational', 'compute', 'computing', 'computerized'],searchWord = "compute") == [['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['compute', 'computer', 'computerized']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['computer', 'computational', 'compute', 'computing', 'computerized'],searchWord = "compute") == [['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['compute', 'computer', 'computerized']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['photography', 'photoalbum', 'photobook', 'photoframe', 'photograph', 'photokino', 'photocopy', 'photography'],searchWord = "phot") == [['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['photography', 'photoalbum', 'photobook', 'photoframe', 'photograph', 'photokino', 'photocopy', 'photography'],searchWord = "phot") == [['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['strawberry', 'straw', 'strange', 'strategy', 'stranger'],searchWord = "stra") == [['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['strawberry', 'straw', 'strange', 'strategy', 'stranger'],searchWord = "stra") == [['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['elephant', 'elephantine', 'elegant', 'elevate', 'elementary'],searchWord = "ele") == [['elegant', 'elementary', 'elephant'], ['elegant', 'elementary', 'elephant'], ['elegant', 'elementary', 'elephant']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['elephant', 'elephantine', 'elegant', 'elevate', 'elementary'],searchWord = "ele") == [['elegant', 'elementary', 'elephant'], ['elegant', 'elementary', 'elephant'], ['elegant', 'elementary', 'elephant']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['orange', 'ornament', 'organ', 'orchid', 'orchard', 'organize'],searchWord = "or") == [['orange', 'orchard', 'orchid'], ['orange', 'orchard', 'orchid']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['orange', 'ornament', 'organ', 'orchid', 'orchard', 'organize'],searchWord = "or") == [['orange', 'orchard', 'orchid'], ['orange', 'orchard', 'orchid']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['aaab', 'aaac', 'aaad', 'aaae', 'aaaf', 'aaag', 'aaah', 'aaai', 'aaaj', 'aaak', 'aaal', 'aaam', 'aaan', 'aaao', 'aaap', 'aaaq', 'aaar', 'aaas', 'aaat', 'aaau', 'aaav', 'aaaw', 'aaax', 'aaay', 'aaaz'],searchWord = "aaa") == [['aaab', 'aaac', 'aaad'], ['aaab', 'aaac', 'aaad'], ['aaab', 'aaac', 'aaad']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['aaab', 'aaac', 'aaad', 'aaae', 'aaaf', 'aaag', 'aaah', 'aaai', 'aaaj', 'aaak', 'aaal', 'aaam', 'aaan', 'aaao', 'aaap', 'aaaq', 'aaar', 'aaas', 'aaat', 'aaau', 'aaav', 'aaaw', 'aaax', 'aaay', 'aaaz'],searchWord = "aaa") == [['aaab', 'aaac', 'aaad'], ['aaab', 'aaac', 'aaad'], ['aaab', 'aaac', 'aaad']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano'],searchWord = "piano") == [['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano'],searchWord = "piano") == [['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['firefly', 'fireworks', 'firefly', 'firearm', 'firetruck', 'firewall', 'firefly', 'firefly', 'firefly', 'firefly'],searchWord = "fire") == [['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['firefly', 'fireworks', 'firefly', 'firearm', 'firetruck', 'firewall', 'firefly', 'firefly', 'firefly', 'firefly'],searchWord = "fire") == [['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['internet', 'interact', 'interest', 'interior', 'interfere'],searchWord = "inte") == [['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['internet', 'interact', 'interest', 'interior', 'interfere'],searchWord = "inte") == [['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['computer', 'compute', 'computation', 'compositor', 'composite', 'compress', 'compression', 'compressor', 'compressed'],searchWord = "compre") == [['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['compress', 'compressed', 'compression'], ['compress', 'compressed', 'compression']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['computer', 'compute', 'computation', 'compositor', 'composite', 'compress', 'compression', 'compressor', 'compressed'],searchWord = "compre") == [['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['compress', 'compressed', 'compression'], ['compress', 'compressed', 'compression']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yellow', 'zucchini'],searchWord = "a") == [['apple']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yellow', 'zucchini'],searchWord = "a") == [['apple']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['dog', 'doghouse', 'dogwood', 'dog', 'doghouse'],searchWord = "dog") == [['dog', 'dog', 'doghouse'], ['dog', 'dog', 'doghouse'], ['dog', 'dog', 'doghouse']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['dog', 'doghouse', 'dogwood', 'dog', 'doghouse'],searchWord = "dog") == [['dog', 'dog', 'doghouse'], ['dog', 'dog', 'doghouse'], ['dog', 'dog', 'doghouse']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['abcd', 'abce', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn', 'abcd', 'abce', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn'],searchWord = "abc") == [['abcd', 'abcd', 'abce'], ['abcd', 'abcd', 'abce'], ['abcd', 'abcd', 'abce']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['abcd', 'abce', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn', 'abcd', 'abce', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn'],searchWord = "abc") == [['abcd', 'abcd', 'abce'], ['abcd', 'abcd', 'abce'], ['abcd', 'abcd', 'abce']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['radio', 'radiance', 'radiant', 'radioactive', 'radioactivity'],searchWord = "radi") == [['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['radio', 'radiance', 'radiant', 'radioactive', 'radioactivity'],searchWord = "radi") == [['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['keyboard', 'keychain', 'keyhole', 'keylogger', 'keynote'],searchWord = "key") == [['keyboard', 'keychain', 'keyhole'], ['keyboard', 'keychain', 'keyhole'], ['keyboard', 'keychain', 'keyhole']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['keyboard', 'keychain', 'keyhole', 'keylogger', 'keynote'],searchWord = "key") == [['keyboard', 'keychain', 'keyhole'], ['keyboard', 'keychain', 'keyhole'], ['keyboard', 'keychain', 'keyhole']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['starship', 'stars', 'start', 'star', 'startrek', 'starfish'],searchWord = "star") == [['star', 'starfish', 'stars'], ['star', 'starfish', 'stars'], ['star', 'starfish', 'stars'], ['star', 'starfish', 'stars']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['starship', 'stars', 'start', 'star', 'startrek', 'starfish'],searchWord = "star") == [['star', 'starfish', 'stars'], ['star', 'starfish', 'stars'], ['star', 'starfish', 'stars'], ['star', 'starfish', 'stars']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['ant', 'antelope', 'antibody', 'antacid', 'antaeus', 'antarctica', 'anteater', 'antelope', 'antelope', 'antler'],searchWord = "ante") == [['ant', 'antacid', 'antaeus'], ['ant', 'antacid', 'antaeus'], ['ant', 'antacid', 'antaeus'], ['anteater', 'antelope', 'antelope']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['ant', 'antelope', 'antibody', 'antacid', 'antaeus', 'antarctica', 'anteater', 'antelope', 'antelope', 'antler'],searchWord = "ante") == [['ant', 'antacid', 'antaeus'], ['ant', 'antacid', 'antaeus'], ['ant', 'antacid', 'antaeus'], ['anteater', 'antelope', 'antelope']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['dog', 'dove', 'donkey', 'dragon', 'drone', 'drill', 'door'],searchWord = "dr") == [['dog', 'donkey', 'door'], ['dragon', 'drill', 'drone']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['dog', 'dove', 'donkey', 'dragon', 'drone', 'drill', 'door'],searchWord = "dr") == [['dog', 'donkey', 'door'], ['dragon', 'drill', 'drone']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['guitar', 'guitarist', 'guilt', 'guilty', 'gully'],searchWord = "guil") == [['guilt', 'guilty', 'guitar'], ['guilt', 'guilty', 'guitar'], ['guilt', 'guilty', 'guitar'], ['guilt', 'guilty']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['guitar', 'guitarist', 'guilt', 'guilty', 'gully'],searchWord = "guil") == [['guilt', 'guilty', 'guitar'], ['guilt', 'guilty', 'guitar'], ['guilt', 'guilty', 'guitar'], ['guilt', 'guilty']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['algorithm', 'algebra', 'alabama', 'alaska', 'alligator'],searchWord = "al") == [['alabama', 'alaska', 'algebra'], ['alabama', 'alaska', 'algebra']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['algorithm', 'algebra', 'alabama', 'alaska', 'alligator'],searchWord = "al") == [['alabama', 'alaska', 'algebra'], ['alabama', 'alaska', 'algebra']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zebrafish', 'zebra', 'zebrahead', 'zebra'],searchWord = "zebra") == [['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zebrafish', 'zebra', 'zebrahead', 'zebra'],searchWord = "zebra") == [['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn'],searchWord = "abcd") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn'],searchWord = "abcd") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zeal', 'zero', 'zone', 'zoo', 'zap', 'zest'],searchWord = "ze") == [['zap', 'zeal', 'zebra'], ['zeal', 'zebra', 'zero']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zeal', 'zero', 'zone', 'zoo', 'zap', 'zest'],searchWord = "ze") == [['zap', 'zeal', 'zebra'], ['zeal', 'zebra', 'zero']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['zebra', 'zoo', 'zoom', 'zoning', 'zone', 'zany', 'zap', 'zest', 'zigzag', 'zither'],searchWord = "z") == [['zany', 'zap', 'zebra']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['zebra', 'zoo', 'zoom', 'zoning', 'zone', 'zany', 'zap', 'zest', 'zigzag', 'zither'],searchWord = "z") == [['zany', 'zap', 'zebra']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['piano', 'piccolo', 'pipe', 'pipeorgan', 'pitchfork'],searchWord = "pi") == [['piano', 'piccolo', 'pipe'], ['piano', 'piccolo', 'pipe']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['piano', 'piccolo', 'pipe', 'pipeorgan', 'pitchfork'],searchWord = "pi") == [['piano', 'piccolo', 'pipe'], ['piano', 'piccolo', 'pipe']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['umbrella', 'underwear', 'universe', 'unique', 'unit', 'unity', 'university', 'unicycle', 'unicorn', 'unzip'],searchWord = "uni") == [['umbrella', 'underwear', 'unicorn'], ['underwear', 'unicorn', 'unicycle'], ['unicorn', 'unicycle', 'unique']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['umbrella', 'underwear', 'universe', 'unique', 'unit', 'unity', 'university', 'unicycle', 'unicorn', 'unzip'],searchWord = "uni") == [['umbrella', 'underwear', 'unicorn'], ['underwear', 'unicorn', 'unicycle'], ['unicorn', 'unicycle', 'unique']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['product', 'produces', 'productivity', 'productive', 'productize', 'production', 'productivity', 'productize', 'productivity', 'productize'],searchWord = "product") == [['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['product', 'production', 'productive']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['product', 'produces', 'productivity', 'productive', 'productize', 'production', 'productivity', 'productize', 'productivity', 'productize'],searchWord = "product") == [['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['product', 'production', 'productive']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['umbrella', 'umbilical', 'umbrella', 'umbrella', 'umbrella'],searchWord = "umb") == [['umbilical', 'umbrella', 'umbrella'], ['umbilical', 'umbrella', 'umbrella'], ['umbilical', 'umbrella', 'umbrella']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['umbrella', 'umbilical', 'umbrella', 'umbrella', 'umbrella'],searchWord = "umb") == [['umbilical', 'umbrella', 'umbrella'], ['umbilical', 'umbrella', 'umbrella'], ['umbilical', 'umbrella', 'umbrella']]: {e}')
    
    total += 1
    try:
        result = candidate(products = ['banana', 'bandanna', 'bandage', 'band', 'bandwidth'],searchWord = "band") == [['banana', 'band', 'bandage'], ['banana', 'band', 'bandage'], ['banana', 'band', 'bandage'], ['band', 'bandage', 'bandanna']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(products = ['banana', 'bandanna', 'bandage', 'band', 'bandwidth'],searchWord = "band") == [['banana', 'band', 'bandage'], ['banana', 'band', 'bandage'], ['banana', 'band', 'bandage'], ['band', 'bandage', 'bandanna']]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(products = ['keyboard', 'keypad', 'keys', 'kick'],searchWord = "key") == [['keyboard', 'keypad', 'keys'], ['keyboard', 'keypad', 'keys'], ['keyboard', 'keypad', 'keys']]
    assert candidate(products = ['keyboard', 'keypad', 'mousepad'],searchWord = "key") == [['keyboard', 'keypad'], ['keyboard', 'keypad'], ['keyboard', 'keypad']]
    assert candidate(products = ['apple', 'banana', 'grape', 'orange'],searchWord = "or") == [['orange'], ['orange']]
    assert candidate(products = ['aaa', 'aaab', 'aaac', 'aab'],searchWord = "aa") == [['aaa', 'aaab', 'aaac'], ['aaa', 'aaab', 'aaac']]
    assert candidate(products = ['charger', 'cable', 'case'],searchWord = "ca") == [['cable', 'case', 'charger'], ['cable', 'case']]
    assert candidate(products = ['bag', 'bags', 'banner', 'box', 'car'],searchWord = "ba") == [['bag', 'bags', 'banner'], ['bag', 'bags', 'banner']]
    assert candidate(products = ['aaa', 'aab', 'aac', 'aad', 'aae'],searchWord = "aa") == [['aaa', 'aab', 'aac'], ['aaa', 'aab', 'aac']]
    assert candidate(products = ['aaa', 'aab', 'aac', 'aad'],searchWord = "aa") == [['aaa', 'aab', 'aac'], ['aaa', 'aab', 'aac']]
    assert candidate(products = ['apple', 'apples', 'application'],searchWord = "app") == [['apple', 'apples', 'application'], ['apple', 'apples', 'application'], ['apple', 'apples', 'application']]
    assert candidate(products = ['apple', 'banana', 'grape', 'orange'],searchWord = "ba") == [['banana'], ['banana']]
    assert candidate(products = ['keyboard', 'keypad', 'keyboard', 'keychain'],searchWord = "key") == [['keyboard', 'keyboard', 'keychain'], ['keyboard', 'keyboard', 'keychain'], ['keyboard', 'keyboard', 'keychain']]
    assert candidate(products = ['havana'],searchWord = "havana") == [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]
    assert candidate(products = ['keyboard', 'keypad', 'kiosk'],searchWord = "key") == [['keyboard', 'keypad', 'kiosk'], ['keyboard', 'keypad'], ['keyboard', 'keypad']]
    assert candidate(products = ['apple', 'banana', 'grape', 'orange', 'peach'],searchWord = "app") == [['apple'], ['apple'], ['apple']]
    assert candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]
    assert candidate(products = ['keyboard', 'keypad', 'keyboardpad'],searchWord = "key") == [['keyboard', 'keyboardpad', 'keypad'], ['keyboard', 'keyboardpad', 'keypad'], ['keyboard', 'keyboardpad', 'keypad']]
    assert candidate(products = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'],searchWord = "mouse") == [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]
    assert candidate(products = ['aardvark', 'aardwolf', 'albatross', 'alligator', 'alpaca', 'antelope', 'anteater'],searchWord = "aa") == [['aardvark', 'aardwolf', 'albatross'], ['aardvark', 'aardwolf']]
    assert candidate(products = ['xylophone', 'xylography', 'xylem', 'xenon', 'xerox', 'xerophyte', 'xenodochial'],searchWord = "xero") == [['xenodochial', 'xenon', 'xerophyte'], ['xenodochial', 'xenon', 'xerophyte'], ['xerophyte', 'xerox'], ['xerophyte', 'xerox']]
    assert candidate(products = ['jacket', 'jaguar', 'jar', 'jasmine', 'jeep'],searchWord = "ja") == [['jacket', 'jaguar', 'jar'], ['jacket', 'jaguar', 'jar']]
    assert candidate(products = ['ant', 'anteater', 'antelope', 'antenna', 'antique', 'antfarm', 'antler'],searchWord = "ant") == [['ant', 'anteater', 'antelope'], ['ant', 'anteater', 'antelope'], ['ant', 'anteater', 'antelope']]
    assert candidate(products = ['television', 'telescope', 'temperature', 'tennis', 'tense'],searchWord = "te") == [['telescope', 'television', 'temperature'], ['telescope', 'television', 'temperature']]
    assert candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry'],searchWord = "b") == [['banana', 'bat', 'berry']]
    assert candidate(products = ['grape', 'grapefruit', 'grapevine', 'graph', 'grapejuice'],searchWord = "gr") == [['grape', 'grapefruit', 'grapejuice'], ['grape', 'grapefruit', 'grapejuice']]
    assert candidate(products = ['dog', 'dolphin', 'dome', 'domestic', 'domino'],searchWord = "dom") == [['dog', 'dolphin', 'dome'], ['dog', 'dolphin', 'dome'], ['dome', 'domestic', 'domino']]
    assert candidate(products = ['magnifier', 'magnificent', 'magnet', 'magnolia', 'magnitude'],searchWord = "magn") == [['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier'], ['magnet', 'magnificent', 'magnifier']]
    assert candidate(products = ['apple', 'application', 'appliance', 'appropriate', 'appetizer'],searchWord = "appl") == [['appetizer', 'apple', 'appliance'], ['appetizer', 'apple', 'appliance'], ['appetizer', 'apple', 'appliance'], ['apple', 'appliance', 'application']]
    assert candidate(products = ['grape', 'grapefruit', 'grapejuice', 'graphite', 'grapevine', 'grapefruitjuice'],searchWord = "grape") == [['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice'], ['grape', 'grapefruit', 'grapefruitjuice']]
    assert candidate(products = ['algorithm', 'array', 'binary', 'bit', 'bitset', 'bucket', 'class', 'collection', 'datatype', 'enumerate', 'file', 'float', 'function', 'garbage', 'graph', 'hash', 'id', 'implementation', 'integer', 'java', 'keyword', 'list', 'map', 'namespace', 'None', 'object', 'operator', 'pair', 'pointer', 'queue', 'range', 'reference', 'set', 'stack', 'string', 'struct', 'template', 'typedef', 'union', 'variable', 'while', 'xor'],searchWord = "algo") == [['algorithm', 'array'], ['algorithm'], ['algorithm'], ['algorithm']]
    assert candidate(products = ['hamburger', 'hammock', 'hammer', 'hammerhead', 'handheld'],searchWord = "ham") == [['hamburger', 'hammer', 'hammerhead'], ['hamburger', 'hammer', 'hammerhead'], ['hamburger', 'hammer', 'hammerhead']]
    assert candidate(products = ['watermelon', 'water', 'wave', 'wonder', 'wonderland'],searchWord = "wat") == [['water', 'watermelon', 'wave'], ['water', 'watermelon', 'wave'], ['water', 'watermelon']]
    assert candidate(products = ['amazon', 'amazing', 'ambassador', 'ambient', 'amplifier'],searchWord = "ambi") == [['amazing', 'amazon', 'ambassador'], ['amazing', 'amazon', 'ambassador'], ['ambassador', 'ambient'], ['ambient']]
    assert candidate(products = ['xylophone', 'xylography', 'xylophone', 'xylophone', 'xylophone'],searchWord = "xylo") == [['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone'], ['xylography', 'xylophone', 'xylophone']]
    assert candidate(products = ['car', 'card', 'cardboard', 'cargo', 'cartoon'],searchWord = "car") == [['car', 'card', 'cardboard'], ['car', 'card', 'cardboard'], ['car', 'card', 'cardboard']]
    assert candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm'],searchWord = "abc") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf']]
    assert candidate(products = ['zebra', 'zinc', 'zoo', 'zesty', 'zoning', 'zest', 'zookeeper'],searchWord = "ze") == [['zebra', 'zest', 'zesty'], ['zebra', 'zest', 'zesty']]
    assert candidate(products = ['aardvark', 'aardwolf', 'aardvark', 'aardvark', 'aardvark'],searchWord = "aard") == [['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark'], ['aardvark', 'aardvark', 'aardvark']]
    assert candidate(products = ['umbrella', 'umber', 'umbilical', 'umbrella', 'umbrella'],searchWord = "umb") == [['umber', 'umbilical', 'umbrella'], ['umber', 'umbilical', 'umbrella'], ['umber', 'umbilical', 'umbrella']]
    assert candidate(products = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij'],searchWord = "abcdefghijk") == [['a', 'ab', 'abc'], ['ab', 'abc', 'abcd'], ['abc', 'abcd', 'abcde'], ['abcd', 'abcde', 'abcdef'], ['abcde', 'abcdef', 'abcdefg'], ['abcdef', 'abcdefg', 'abcdefgh'], ['abcdefg', 'abcdefgh', 'abcdefghi'], ['abcdefgh', 'abcdefghi', 'abcdefghij'], ['abcdefghi', 'abcdefghij'], ['abcdefghij'], []]
    assert candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blueberry', 'blackberry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]
    assert candidate(products = ['zebra', 'zebrafish', 'zebrafly', 'zebratail', 'zebralight', 'zebrashoe', 'zebragram', 'zebratic', 'zebrastriped'],searchWord = "zebra") == [['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly'], ['zebra', 'zebrafish', 'zebrafly']]
    assert candidate(products = ['infinite', 'infinity', 'infinitesimal', 'infinity', 'infinitary'],searchWord = "inf") == [['infinitary', 'infinite', 'infinitesimal'], ['infinitary', 'infinite', 'infinitesimal'], ['infinitary', 'infinite', 'infinitesimal']]
    assert candidate(products = ['orange', 'oregano', 'organ', 'organize', 'organism'],searchWord = "org") == [['orange', 'oregano', 'organ'], ['orange', 'oregano', 'organ'], ['organ', 'organism', 'organize']]
    assert candidate(products = ['xenon', 'xerox', 'xenophobe', 'xenial', 'xenolith', 'xenoliths', 'xenonarc', 'xenonarcosis', 'xenolithologist'],searchWord = "xen") == [['xenial', 'xenolith', 'xenolithologist'], ['xenial', 'xenolith', 'xenolithologist'], ['xenial', 'xenolith', 'xenolithologist']]
    assert candidate(products = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aab', 'aac', 'aad', 'aaf', 'aag'],searchWord = "aa") == [['a', 'aa', 'aaa'], ['aa', 'aaa', 'aaaa']]
    assert candidate(products = ['laptop', 'laptopbag', 'laser', 'lateral', 'latitude'],searchWord = "lap") == [['laptop', 'laptopbag', 'laser'], ['laptop', 'laptopbag', 'laser'], ['laptop', 'laptopbag']]
    assert candidate(products = ['cherry', 'cranberry', 'cantaloupe', 'carrot', 'corn', 'cucumber'],searchWord = "car") == [['cantaloupe', 'carrot', 'cherry'], ['cantaloupe', 'carrot'], ['carrot']]
    assert candidate(products = ['umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella'],searchWord = "umbrella") == [['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella'], ['umbrella', 'umbrella', 'umbrella']]
    assert candidate(products = ['aardvark', 'aardwolf', 'albatross', 'albino', 'alligator', 'alpaca', 'almighty'],searchWord = "al") == [['aardvark', 'aardwolf', 'albatross'], ['albatross', 'albino', 'alligator']]
    assert candidate(products = ['zebra', 'zealot', 'zealous', 'zebrafish', 'zebra', 'zebrahead'],searchWord = "ze") == [['zealot', 'zealous', 'zebra'], ['zealot', 'zealous', 'zebra']]
    assert candidate(products = ['navigate', 'navigation', 'navigator', 'navy', 'navel'],searchWord = "nav") == [['navel', 'navigate', 'navigation'], ['navel', 'navigate', 'navigation'], ['navel', 'navigate', 'navigation']]
    assert candidate(products = ['electronics', 'electric', 'elephant', 'elbow', 'eleven'],searchWord = "ele") == [['elbow', 'electric', 'electronics'], ['elbow', 'electric', 'electronics'], ['electric', 'electronics', 'elephant']]
    assert candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry', 'bluebird', 'bluetooth'],searchWord = "bl") == [['banana', 'bat', 'berry'], ['blackberry', 'blueberry', 'bluebird']]
    assert candidate(products = ['abacaxi', 'abalone', 'abana', 'abanga', 'abaperture', 'abara', 'abaraxas', 'abarth', 'abart', 'abat', 'abate', 'abati', 'abatis', 'abator', 'abatt', 'abature', 'abavure', 'abaya', 'abaze', 'abba', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe', 'abbe'],searchWord = "ab") == [['abacaxi', 'abalone', 'abana'], ['abacaxi', 'abalone', 'abana']]
    assert candidate(products = ['applepie', 'applesauce', 'appleskin', 'apple', 'applejack'],searchWord = "appl") == [['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie'], ['apple', 'applejack', 'applepie']]
    assert candidate(products = ['camera', 'camcorder', 'cameralens', 'cameraman', 'cameraobscura', 'camouflage', 'camcorder', 'camera', 'camcorder'],searchWord = "cam") == [['camcorder', 'camcorder', 'camcorder'], ['camcorder', 'camcorder', 'camcorder'], ['camcorder', 'camcorder', 'camcorder']]
    assert candidate(products = ['chocolate', 'chocolatebar', 'chocolatechip', 'chocolate', 'chocolatefudge'],searchWord = "chocolate") == [['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar'], ['chocolate', 'chocolate', 'chocolatebar']]
    assert candidate(products = ['queen', 'queens', 'queenship', 'queer', 'queue'],searchWord = "quee") == [['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship'], ['queen', 'queens', 'queenship']]
    assert candidate(products = ['apple', 'apricot', 'avocado', 'banana', 'bat', 'berry', 'blackberry', 'blueberry', 'cherry', 'cantaloupe', 'cranberry'],searchWord = "ap") == [['apple', 'apricot', 'avocado'], ['apple', 'apricot']]
    assert candidate(products = ['applepie', 'applesauce', 'apple', 'appletart', 'apples', 'apricot'],searchWord = "apple") == [['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples'], ['apple', 'applepie', 'apples']]
    assert candidate(products = ['guitar', 'guitarcase', 'guitarhero', 'guitarpick', 'guitarstand', 'guitartuner', 'guitarstring'],searchWord = "gu") == [['guitar', 'guitarcase', 'guitarhero'], ['guitar', 'guitarcase', 'guitarhero']]
    assert candidate(products = ['ocean', 'ocelot', 'octopus', 'octagon', 'octagonal'],searchWord = "oct") == [['ocean', 'ocelot', 'octagon'], ['ocean', 'ocelot', 'octagon'], ['octagon', 'octagonal', 'octopus']]
    assert candidate(products = ['elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant', 'elephant'],searchWord = "elephant") == [['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant'], ['elephant', 'elephant', 'elephant']]
    assert candidate(products = ['chocolate', 'chips', 'chipmunk', 'cheese', 'cherry', 'chili'],searchWord = "ch") == [['cheese', 'cherry', 'chili'], ['cheese', 'cherry', 'chili']]
    assert candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch'],searchWord = "abc") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf']]
    assert candidate(products = ['zebra', 'zulu', 'zymurgy', 'zestful', 'zestfully', 'zestless', 'zippy', 'zoo', 'zoology', 'zucchini'],searchWord = "zoo") == [['zebra', 'zestful', 'zestfully'], ['zoo', 'zoology'], ['zoo', 'zoology']]
    assert candidate(products = ['fishing', 'fishtank', 'fish', 'fishmonger', 'fisherman', 'fishhook', 'fishnet'],searchWord = "fish") == [['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook'], ['fish', 'fisherman', 'fishhook']]
    assert candidate(products = ['watermelon', 'water', 'waterproof', 'watering', 'waterfall', 'watermelon', 'watercolor', 'watergun', 'watermelon', 'watermark'],searchWord = "waterm") == [['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['watermark', 'watermelon', 'watermelon']]
    assert candidate(products = ['banana', 'band', 'bangalore', 'bank', 'banner'],searchWord = "ban") == [['banana', 'band', 'bangalore'], ['banana', 'band', 'bangalore'], ['banana', 'band', 'bangalore']]
    assert candidate(products = ['paint', 'painter', 'painting', 'paintball', 'paintbrush'],searchWord = "pain") == [['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush'], ['paint', 'paintball', 'paintbrush']]
    assert candidate(products = ['xyz', 'xylophone', 'xylography', 'xylograph', 'xylography', 'xylographer', 'xylographs', 'xylography', 'xylography'],searchWord = "xylo") == [['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs'], ['xylograph', 'xylographer', 'xylographs']]
    assert candidate(products = ['microphone', 'microwave', 'microscope', 'microphone', 'micronutrient'],searchWord = "micr") == [['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone'], ['micronutrient', 'microphone', 'microphone']]
    assert candidate(products = ['flower', 'flour', 'flow', 'flourish', 'flourmill'],searchWord = "flow") == [['flour', 'flourish', 'flourmill'], ['flour', 'flourish', 'flourmill'], ['flour', 'flourish', 'flourmill'], ['flow', 'flower']]
    assert candidate(products = ['car', 'card', 'care', 'careful', 'careless'],searchWord = "ca") == [['car', 'card', 'care'], ['car', 'card', 'care']]
    assert candidate(products = ['football', 'footwear', 'footbridge', 'footnote', 'footrest', 'footlocker', 'footrace', 'footlight'],searchWord = "foot") == [['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight'], ['football', 'footbridge', 'footlight']]
    assert candidate(products = ['bicycle', 'bicycling', 'bicycle', 'bicycle', 'bicycle'],searchWord = "bicy") == [['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle'], ['bicycle', 'bicycle', 'bicycle']]
    assert candidate(products = ['giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe'],searchWord = "giraff") == [['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe'], ['giraffe', 'giraffe', 'giraffe']]
    assert candidate(products = ['strawberry', 'straw', 'stratosphere', 'stranger', 'strategy'],searchWord = "stra") == [['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere'], ['stranger', 'strategy', 'stratosphere']]
    assert candidate(products = ['apple', 'apricot', 'banana', 'bat', 'berry', 'blackberry', 'blueberry'],searchWord = "ba") == [['banana', 'bat', 'berry'], ['banana', 'bat']]
    assert candidate(products = ['watermelon', 'water', 'waterfall', 'watershed', 'watercolor'],searchWord = "water") == [['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall'], ['water', 'watercolor', 'waterfall']]
    assert candidate(products = ['computer', 'computational', 'compute', 'computing', 'computerized'],searchWord = "compute") == [['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['computational', 'compute', 'computer'], ['compute', 'computer', 'computerized']]
    assert candidate(products = ['photography', 'photoalbum', 'photobook', 'photoframe', 'photograph', 'photokino', 'photocopy', 'photography'],searchWord = "phot") == [['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy'], ['photoalbum', 'photobook', 'photocopy']]
    assert candidate(products = ['strawberry', 'straw', 'strange', 'strategy', 'stranger'],searchWord = "stra") == [['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy'], ['strange', 'stranger', 'strategy']]
    assert candidate(products = ['elephant', 'elephantine', 'elegant', 'elevate', 'elementary'],searchWord = "ele") == [['elegant', 'elementary', 'elephant'], ['elegant', 'elementary', 'elephant'], ['elegant', 'elementary', 'elephant']]
    assert candidate(products = ['orange', 'ornament', 'organ', 'orchid', 'orchard', 'organize'],searchWord = "or") == [['orange', 'orchard', 'orchid'], ['orange', 'orchard', 'orchid']]
    assert candidate(products = ['aaab', 'aaac', 'aaad', 'aaae', 'aaaf', 'aaag', 'aaah', 'aaai', 'aaaj', 'aaak', 'aaal', 'aaam', 'aaan', 'aaao', 'aaap', 'aaaq', 'aaar', 'aaas', 'aaat', 'aaau', 'aaav', 'aaaw', 'aaax', 'aaay', 'aaaz'],searchWord = "aaa") == [['aaab', 'aaac', 'aaad'], ['aaab', 'aaac', 'aaad'], ['aaab', 'aaac', 'aaad']]
    assert candidate(products = ['piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano', 'piano'],searchWord = "piano") == [['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano'], ['piano', 'piano', 'piano']]
    assert candidate(products = ['firefly', 'fireworks', 'firefly', 'firearm', 'firetruck', 'firewall', 'firefly', 'firefly', 'firefly', 'firefly'],searchWord = "fire") == [['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly'], ['firearm', 'firefly', 'firefly']]
    assert candidate(products = ['internet', 'interact', 'interest', 'interior', 'interfere'],searchWord = "inte") == [['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere'], ['interact', 'interest', 'interfere']]
    assert candidate(products = ['computer', 'compute', 'computation', 'compositor', 'composite', 'compress', 'compression', 'compressor', 'compressed'],searchWord = "compre") == [['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['composite', 'compositor', 'compress'], ['compress', 'compressed', 'compression'], ['compress', 'compressed', 'compression']]
    assert candidate(products = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yellow', 'zucchini'],searchWord = "a") == [['apple']]
    assert candidate(products = ['dog', 'doghouse', 'dogwood', 'dog', 'doghouse'],searchWord = "dog") == [['dog', 'dog', 'doghouse'], ['dog', 'dog', 'doghouse'], ['dog', 'dog', 'doghouse']]
    assert candidate(products = ['abcd', 'abce', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn', 'abcd', 'abce', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn'],searchWord = "abc") == [['abcd', 'abcd', 'abce'], ['abcd', 'abcd', 'abce'], ['abcd', 'abcd', 'abce']]
    assert candidate(products = ['radio', 'radiance', 'radiant', 'radioactive', 'radioactivity'],searchWord = "radi") == [['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio'], ['radiance', 'radiant', 'radio']]
    assert candidate(products = ['keyboard', 'keychain', 'keyhole', 'keylogger', 'keynote'],searchWord = "key") == [['keyboard', 'keychain', 'keyhole'], ['keyboard', 'keychain', 'keyhole'], ['keyboard', 'keychain', 'keyhole']]
    assert candidate(products = ['starship', 'stars', 'start', 'star', 'startrek', 'starfish'],searchWord = "star") == [['star', 'starfish', 'stars'], ['star', 'starfish', 'stars'], ['star', 'starfish', 'stars'], ['star', 'starfish', 'stars']]
    assert candidate(products = ['ant', 'antelope', 'antibody', 'antacid', 'antaeus', 'antarctica', 'anteater', 'antelope', 'antelope', 'antler'],searchWord = "ante") == [['ant', 'antacid', 'antaeus'], ['ant', 'antacid', 'antaeus'], ['ant', 'antacid', 'antaeus'], ['anteater', 'antelope', 'antelope']]
    assert candidate(products = ['dog', 'dove', 'donkey', 'dragon', 'drone', 'drill', 'door'],searchWord = "dr") == [['dog', 'donkey', 'door'], ['dragon', 'drill', 'drone']]
    assert candidate(products = ['guitar', 'guitarist', 'guilt', 'guilty', 'gully'],searchWord = "guil") == [['guilt', 'guilty', 'guitar'], ['guilt', 'guilty', 'guitar'], ['guilt', 'guilty', 'guitar'], ['guilt', 'guilty']]
    assert candidate(products = ['algorithm', 'algebra', 'alabama', 'alaska', 'alligator'],searchWord = "al") == [['alabama', 'alaska', 'algebra'], ['alabama', 'alaska', 'algebra']]
    assert candidate(products = ['zebra', 'zebrafish', 'zebra', 'zebrahead', 'zebra'],searchWord = "zebra") == [['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra'], ['zebra', 'zebra', 'zebra']]
    assert candidate(products = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn'],searchWord = "abcd") == [['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd', 'abce', 'abcf'], ['abcd']]
    assert candidate(products = ['zebra', 'zeal', 'zero', 'zone', 'zoo', 'zap', 'zest'],searchWord = "ze") == [['zap', 'zeal', 'zebra'], ['zeal', 'zebra', 'zero']]
    assert candidate(products = ['zebra', 'zoo', 'zoom', 'zoning', 'zone', 'zany', 'zap', 'zest', 'zigzag', 'zither'],searchWord = "z") == [['zany', 'zap', 'zebra']]
    assert candidate(products = ['piano', 'piccolo', 'pipe', 'pipeorgan', 'pitchfork'],searchWord = "pi") == [['piano', 'piccolo', 'pipe'], ['piano', 'piccolo', 'pipe']]
    assert candidate(products = ['umbrella', 'underwear', 'universe', 'unique', 'unit', 'unity', 'university', 'unicycle', 'unicorn', 'unzip'],searchWord = "uni") == [['umbrella', 'underwear', 'unicorn'], ['underwear', 'unicorn', 'unicycle'], ['unicorn', 'unicycle', 'unique']]
    assert candidate(products = ['product', 'produces', 'productivity', 'productive', 'productize', 'production', 'productivity', 'productize', 'productivity', 'productize'],searchWord = "product") == [['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['produces', 'product', 'production'], ['product', 'production', 'productive']]
    assert candidate(products = ['umbrella', 'umbilical', 'umbrella', 'umbrella', 'umbrella'],searchWord = "umb") == [['umbilical', 'umbrella', 'umbrella'], ['umbilical', 'umbrella', 'umbrella'], ['umbilical', 'umbrella', 'umbrella']]
    assert candidate(products = ['banana', 'bandanna', 'bandage', 'band', 'bandwidth'],searchWord = "band") == [['banana', 'band', 'bandage'], ['banana', 'band', 'bandage'], ['banana', 'band', 'bandage'], ['band', 'bandage', 'bandanna']]


