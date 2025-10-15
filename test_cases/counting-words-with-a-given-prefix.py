def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested', 'testing'],pref = "test") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested', 'testing'],pref = "test") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde'],pref = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde'],pref = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'helium', 'helper'],pref = "hel") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'helium', 'helper'],pref = "hel") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'bandana', 'banner', 'balance'],pref = "ban") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'bandana', 'banner', 'balance'],pref = "ban") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'hero', 'herald'],pref = "he") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'hero', 'herald'],pref = "he") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pay', 'attention', 'practice', 'attend'],pref = "at") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pay', 'attention', 'practice', 'attend'],pref = "at") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],pref = "hi") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],pref = "hi") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'helper'],pref = "hel") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'helper'],pref = "hel") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apricot', 'application'],pref = "app") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apricot', 'application'],pref = "app") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apricot', 'application', 'appetite'],pref = "app") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apricot', 'application', 'appetite'],pref = "app") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'caterpillar', 'catalog', 'category'],pref = "cat") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'caterpillar', 'catalog', 'category'],pref = "cat") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apricot', 'banana', 'apex'],pref = "ap") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apricot', 'banana', 'apex'],pref = "ap") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'band', 'ball'],pref = "ba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'band', 'ball'],pref = "ba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'bandana', 'baptism'],pref = "ban") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'bandana', 'baptism'],pref = "ban") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'application', 'apricot', 'apex'],pref = "ap") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'application', 'apricot', 'apex'],pref = "ap") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['leetcode', 'win', 'loops', 'success'],pref = "code") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['leetcode', 'win', 'loops', 'success'],pref = "code") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['database', 'datacenter', 'datamine', 'data'],pref = "data") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['database', 'datacenter', 'datamine', 'data'],pref = "data") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['integration', 'integrate', 'interact', 'interactive'],pref = "inte") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['integration', 'integrate', 'interact', 'interactive'],pref = "inte") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'array', 'application', 'arithmetic'],pref = "arr") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'array', 'application', 'arithmetic'],pref = "arr") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intersection', 'interface', 'internal', 'interact'],pref = "inter") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intersection', 'interface', 'internal', 'interact'],pref = "inter") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unpredictable', 'unpredicted', 'unpredictably', 'unpredicting'],pref = "unpred") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unpredictable', 'unpredicted', 'unpredictably', 'unpredicting'],pref = "unpred") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prepend', 'presentation', 'preference'],pref = "pre") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prepend', 'presentation', 'preference'],pref = "pre") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['challenge', 'champion', 'chance', 'character'],pref = "cha") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['challenge', 'champion', 'chance', 'character'],pref = "cha") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['management', 'manager', 'manufacture', 'maintain'],pref = "man") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['management', 'manager', 'manufacture', 'maintain'],pref = "man") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interpolation', 'interpolate', 'interpolator', 'interpolated'],pref = "inter") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interpolation', 'interpolate', 'interpolator', 'interpolated'],pref = "inter") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['technology', 'technique', 'technical', 'technological'],pref = "tech") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['technology', 'technique', 'technical', 'technological'],pref = "tech") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['universe', 'uniform', 'unique', 'unit'],pref = "uni") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['universe', 'uniform', 'unique', 'unit'],pref = "uni") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'python', 'problem', 'project', 'practice'],pref = "pro") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'python', 'problem', 'project', 'practice'],pref = "pro") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['document', 'documentation', 'documentary', 'documents'],pref = "docu") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['document', 'documentation', 'documentary', 'documents'],pref = "docu") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'envelope', 'encyclopedia', 'enterprise'],pref = "env") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'envelope', 'encyclopedia', 'enterprise'],pref = "env") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interview', 'international', 'internet', 'introduce'],pref = "inter") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interview', 'international', 'internet', 'introduce'],pref = "inter") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'community', 'commemoration', 'commentary'],pref = "comm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'community', 'commemoration', 'commentary'],pref = "comm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'array', 'application', 'apricot'],pref = "app") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'array', 'application', 'apricot'],pref = "app") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cryptography', 'cryptanalysis', 'cryptographic', 'cryptology'],pref = "crypto") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cryptography', 'cryptanalysis', 'cryptographic', 'cryptology'],pref = "crypto") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interact', 'interaction', 'interactive', 'interior', 'intercept'],pref = "inter") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interact', 'interaction', 'interactive', 'interior', 'intercept'],pref = "inter") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fantastic', 'fancy', 'fantasy', 'fanatic'],pref = "fan") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fantastic', 'fancy', 'fantasy', 'fanatic'],pref = "fan") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pseudo', 'pseudocode', 'pseudorandom', 'pseudoscience'],pref = "pseudo") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pseudo', 'pseudocode', 'pseudorandom', 'pseudoscience'],pref = "pseudo") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mathematical', 'mathematics', 'mathematically', 'mathematize'],pref = "math") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mathematical', 'mathematics', 'mathematically', 'mathematize'],pref = "math") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'problem', 'prefix', 'preference'],pref = "pre") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'problem', 'prefix', 'preference'],pref = "pre") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['biography', 'biologist', 'biological', 'biographical'],pref = "bio") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['biography', 'biologist', 'biological', 'biographical'],pref = "bio") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unbelievable', 'universe', 'unique', 'unanimous'],pref = "un") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unbelievable', 'universe', 'unique', 'unanimous'],pref = "un") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['congratulations', 'congratulate', 'congratulatory', 'congregate', 'congruity'],pref = "cong") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['congratulations', 'congratulate', 'congratulatory', 'congregate', 'congruity'],pref = "cong") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supplementary', 'supplement', 'supplier', 'suppose'],pref = "sup") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supplementary', 'supplement', 'supplier', 'suppose'],pref = "sup") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['community', 'commune', 'communicate', 'common'],pref = "comm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['community', 'commune', 'communicate', 'common'],pref = "comm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['extraterrestrial', 'extraterrestrial', 'extraterrestrial', 'extraterrestrial'],pref = "extra") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['extraterrestrial', 'extraterrestrial', 'extraterrestrial', 'extraterrestrial'],pref = "extra") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'array', 'application', 'applet'],pref = "app") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'array', 'application', 'applet'],pref = "app") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'abstract', 'absorb', 'academic'],pref = "abs") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'abstract', 'absorb', 'academic'],pref = "abs") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['congruence', 'congruent', 'congruently', 'congruency'],pref = "congru") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['congruence', 'congruent', 'congruently', 'congruency'],pref = "congru") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['meticulous', 'meticulate', 'metaphor', 'metaphysics'],pref = "metic") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['meticulous', 'meticulate', 'metaphor', 'metaphysics'],pref = "metic") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['biological', 'biography', 'biologist', 'biology', 'bioluminescence'],pref = "biol") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['biological', 'biography', 'biologist', 'biology', 'bioluminescence'],pref = "biol") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['application', 'approach', 'appetizer', 'append'],pref = "app") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['application', 'approach', 'appetizer', 'append'],pref = "app") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['scientific', 'scientist', 'science', 'sciences'],pref = "sci") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['scientific', 'scientist', 'science', 'sciences'],pref = "sci") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'community', 'common', 'commodity'],pref = "com") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'community', 'common', 'commodity'],pref = "com") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['quantization', 'quantize', 'quantitative', 'quantitative'],pref = "quant") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quantization', 'quantize', 'quantitative', 'quantitative'],pref = "quant") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prepend', 'presentation', 'premature'],pref = "pre") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prepend', 'presentation', 'premature'],pref = "pre") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['continuous', 'concurrent', 'conclusion', 'condition'],pref = "con") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['continuous', 'concurrent', 'conclusion', 'condition'],pref = "con") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro', 'professor'],pref = "pro") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro', 'professor'],pref = "pro") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['management', 'manager', 'manage', 'mandate'],pref = "man") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['management', 'manager', 'manage', 'mandate'],pref = "man") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transformation', 'transmit', 'transparent', 'transient'],pref = "tran") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transformation', 'transmit', 'transparent', 'transient'],pref = "tran") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['administrator', 'administration', 'administrative', 'administratively'],pref = "admin") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['administrator', 'administration', 'administrative', 'administratively'],pref = "admin") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['circumstance', 'circuit', 'circulate', 'circulation', 'circular'],pref = "circu") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['circumstance', 'circuit', 'circulate', 'circulation', 'circular'],pref = "circu") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['characterization', 'character', 'characteristic', 'characterization'],pref = "char") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['characterization', 'character', 'characteristic', 'characterization'],pref = "char") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'envy', 'envelope', 'evening'],pref = "env") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'envy', 'envelope', 'evening'],pref = "env") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['database', 'data', 'datagram', 'datastructure'],pref = "data") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['database', 'data', 'datagram', 'datastructure'],pref = "data") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['celebration', 'celebrate', 'celebrity', 'celebratory', 'celestial'],pref = "celeb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['celebration', 'celebrate', 'celebrity', 'celebratory', 'celestial'],pref = "celeb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cryptography', 'crypt', 'crypto', 'cryptanalysis'],pref = "crypt") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cryptography', 'crypt', 'crypto', 'cryptanalysis'],pref = "crypt") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['photography', 'photo', 'photobook', 'photographer'],pref = "photo") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['photography', 'photo', 'photobook', 'photographer'],pref = "photo") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['magnify', 'magnificent', 'magnetic', 'magnetism'],pref = "mag") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['magnify', 'magnificent', 'magnetic', 'magnetism'],pref = "mag") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['organization', 'organize', 'organ', 'organically'],pref = "org") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['organization', 'organize', 'organ', 'organically'],pref = "org") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'almond', 'alert'],pref = "alg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'almond', 'alert'],pref = "alg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'array', 'application', 'apple'],pref = "app") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'array', 'application', 'apple'],pref = "app") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'community', 'commitment', 'common'],pref = "comm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'community', 'commitment', 'common'],pref = "comm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['developer', 'debug', 'deploy', 'document'],pref = "de") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['developer', 'debug', 'deploy', 'document'],pref = "de") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['perpendicular', 'perpendicularity', 'perpendicularity', 'perpendicularly'],pref = "perpendicular") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['perpendicular', 'perpendicularity', 'perpendicularity', 'perpendicularly'],pref = "perpendicular") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'engine', 'error', 'example'],pref = "en") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'engine', 'error', 'example'],pref = "en") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['university', 'uniform', 'unique', 'universe'],pref = "uni") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['university', 'uniform', 'unique', 'universe'],pref = "uni") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['community', 'communist', 'common', 'comment'],pref = "comm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['community', 'communist', 'common', 'comment'],pref = "comm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['literature', 'literacy', 'literary', 'literate'],pref = "lit") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['literature', 'literacy', 'literary', 'literate'],pref = "lit") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['sequoia', 'sequence', 'series', 'serial'],pref = "ser") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['sequoia', 'sequence', 'series', 'serial'],pref = "ser") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'community', 'companion', 'commune'],pref = "comm") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'community', 'companion', 'commune'],pref = "comm") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'alignment', 'algorithmic'],pref = "algo") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'alignment', 'algorithmic'],pref = "algo") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['character', 'chart', 'chapter', 'charge'],pref = "char") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['character', 'chart', 'chapter', 'charge'],pref = "char") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transport', 'trap', 'trapezium', 'traverse'],pref = "tra") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transport', 'trap', 'trapezium', 'traverse'],pref = "tra") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'commute', 'community', 'commotion', 'common'],pref = "comm") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'commute', 'community', 'commotion', 'common'],pref = "comm") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'energy', 'engage', 'engageable'],pref = "en") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'energy', 'engage', 'engageable'],pref = "en") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['identification', 'individual', 'idea', 'illegal'],pref = "iden") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['identification', 'individual', 'idea', 'illegal'],pref = "iden") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supreme', 'superior', 'surpass', 'surround'],pref = "sur") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supreme', 'superior', 'surpass', 'surround'],pref = "sur") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transformation', 'transmit', 'transit', 'transformation', 'transition'],pref = "trans") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transformation', 'transmit', 'transit', 'transformation', 'transition'],pref = "trans") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['automation', 'automatic', 'automate', 'auto'],pref = "auto") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['automation', 'automatic', 'automate', 'auto'],pref = "auto") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['configuration', 'compute', 'container', 'cloud'],pref = "con") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['configuration', 'compute', 'container', 'cloud'],pref = "con") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'community', 'commitment', 'compassionate'],pref = "comm") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'community', 'commitment', 'compassionate'],pref = "comm") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'program', 'pro', 'progress'],pref = "pro") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'program', 'pro', 'progress'],pref = "pro") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['absolutely', 'absolute', 'absorb', 'abnormal'],pref = "abs") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['absolutely', 'absolute', 'absorb', 'abnormal'],pref = "abs") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['statistics', 'statistical', 'statue', 'status'],pref = "stat") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['statistics', 'statistical', 'statue', 'status'],pref = "stat") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefixes', 'preferring', 'preference'],pref = "pref") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefixes', 'preferring', 'preference'],pref = "pref") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['congratulations', 'congratulate', 'congratulatory', 'congratulated'],pref = "congrat") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['congratulations', 'congratulate', 'congratulatory', 'congratulated'],pref = "congrat") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'essential', 'establish', 'engage'],pref = "en") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'essential', 'establish', 'engage'],pref = "en") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substitution', 'substitute', 'substituted', 'substituting'],pref = "sub") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substitution', 'substitute', 'substituted', 'substituting'],pref = "sub") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['distribution', 'distribute', 'disastrous', 'discuss', 'disease'],pref = "dis") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['distribution', 'distribute', 'disastrous', 'discuss', 'disease'],pref = "dis") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['development', 'deploy', 'debug', 'document'],pref = "de") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['development', 'deploy', 'debug', 'document'],pref = "de") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['super', 'superhero', 'supercalifragilisticexpialidocious', 'supervillain'],pref = "super") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['super', 'superhero', 'supercalifragilisticexpialidocious', 'supervillain'],pref = "super") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['maintenance', 'maintain', 'maintenance', 'maintained'],pref = "maint") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['maintenance', 'maintain', 'maintenance', 'maintained'],pref = "maint") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'pyramid', 'pythia', 'pyrotechnic'],pref = "pyt") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'pyramid', 'pythia', 'pyrotechnic'],pref = "pyt") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'alibi', 'alien', 'alimony'],pref = "ali") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'alibi', 'alien', 'alimony'],pref = "ali") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['remarkable', 'remark', 'remember', 'remind'],pref = "rem") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['remarkable', 'remark', 'remember', 'remind'],pref = "rem") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['septagon', 'septagonal', 'septembre', 'septenary'],pref = "sept") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['septagon', 'septagonal', 'septembre', 'septenary'],pref = "sept") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'progress', 'prompt', 'priority'],pref = "pro") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'progress', 'prompt', 'priority'],pref = "pro") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['document', 'documentation', 'documentary', 'documents'],pref = "doc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['document', 'documentation', 'documentary', 'documents'],pref = "doc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['monarch', 'monarchy', 'monarchic', 'monarchically'],pref = "monarch") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['monarch', 'monarchy', 'monarchic', 'monarchically'],pref = "monarch") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hemisphere', 'hemispherical', 'hemispheres', 'hemispheric'],pref = "hemis") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hemisphere', 'hemispherical', 'hemispheres', 'hemispheric'],pref = "hemis") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'engage', 'enhance', 'enforce', 'ensure'],pref = "enf") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'engage', 'enhance', 'enforce', 'ensure'],pref = "enf") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['persistent', 'perspective', 'personality', 'person', 'personnel'],pref = "pers") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['persistent', 'perspective', 'personality', 'person', 'personnel'],pref = "pers") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'preference', 'presentation', 'prevent', 'president'],pref = "pre") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'preference', 'presentation', 'prevent', 'president'],pref = "pre") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['parallelogram', 'parallelepiped', 'parallel', 'parallelograms'],pref = "parallel") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['parallelogram', 'parallelepiped', 'parallel', 'parallelograms'],pref = "parallel") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['intelligence', 'integrate', 'intensity', 'interact'],pref = "inte") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['intelligence', 'integrate', 'intensity', 'interact'],pref = "inte") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['information', 'infrastructure', 'insurance', 'initial'],pref = "in") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['information', 'infrastructure', 'insurance', 'initial'],pref = "in") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transport', 'transmit', 'transformation', 'transition'],pref = "trans") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transport', 'transmit', 'transformation', 'transition'],pref = "trans") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['establish', 'estimate', 'essential', 'establishment'],pref = "est") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['establish', 'estimate', 'essential', 'establishment'],pref = "est") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'algebra', 'alchemist', 'alchemy'],pref = "alg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'algebra', 'alchemist', 'alchemy'],pref = "alg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'envelope', 'engage', 'enhance'],pref = "en") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'envelope', 'engage', 'enhance'],pref = "en") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transport', 'transmit', 'transit', 'transformation', 'transition'],pref = "trans") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transport', 'transmit', 'transit', 'transformation', 'transition'],pref = "trans") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'problem', 'process', 'productivity'],pref = "pro") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'problem', 'process', 'productivity'],pref = "pro") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'pro', 'processor', 'productivity'],pref = "pro") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'pro', 'processor', 'productivity'],pref = "pro") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['encyclopedia', 'encyclopedias', 'encyclopedic', 'encyclopedically'],pref = "ency") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['encyclopedia', 'encyclopedias', 'encyclopedic', 'encyclopedically'],pref = "ency") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'application', 'appetite', 'apparent'],pref = "app") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'application', 'appetite', 'apparent'],pref = "app") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'zephyr', 'zoo', 'zealous'],pref = "ze") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'zephyr', 'zoo', 'zealous'],pref = "ze") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefixes', 'preference', 'preferring'],pref = "pref") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefixes', 'preference', 'preferring'],pref = "pref") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'community', 'commitment', 'commission'],pref = "com") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'community', 'commitment', 'commission'],pref = "com") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hypothesis', 'historical', 'hyphen', 'hydrogen'],pref = "hy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hypothesis', 'historical', 'hyphen', 'hydrogen'],pref = "hy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transformation', 'transfer', 'transform', 'transformer'],pref = "trans") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transformation', 'transfer', 'transform', 'transformer'],pref = "trans") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['transaction', 'transfer', 'transition', 'transportation'],pref = "tran") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['transaction', 'transfer', 'transition', 'transportation'],pref = "tran") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'abrakadabras', 'abracadabrac', 'abracadabrad'],pref = "abrac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'abrakadabras', 'abracadabrac', 'abracadabrad'],pref = "abrac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interview', 'integrate', 'interaction', 'interface'],pref = "inte") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interview', 'integrate', 'interaction', 'interface'],pref = "inte") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fantastic', 'fantasy', 'fancy', 'fantastician'],pref = "fant") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fantastic', 'fantasy', 'fancy', 'fantastician'],pref = "fant") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['communication', 'communicate', 'communist', 'commune'],pref = "comm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['communication', 'communicate', 'communist', 'commune'],pref = "comm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'environ', 'environmental', 'envelope'],pref = "env") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'environ', 'environmental', 'envelope'],pref = "env") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['education', 'educational', 'educate', 'educator'],pref = "edu") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['education', 'educational', 'educate', 'educator'],pref = "edu") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['automation', 'automobile', 'automatic', 'automate'],pref = "auto") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['automation', 'automobile', 'automatic', 'automate'],pref = "auto") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['customization', 'customize', 'custom', 'customarily'],pref = "cust") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['customization', 'customize', 'custom', 'customarily'],pref = "cust") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['environment', 'encourage', 'endure', 'ensure'],pref = "en") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['environment', 'encourage', 'endure', 'ensure'],pref = "en") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'predict', 'prevent', 'preach', 'prelude'],pref = "pre") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'predict', 'prevent', 'preach', 'prelude'],pref = "pre") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['elephant', 'elegant', 'elephantine', 'election'],pref = "ele") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['elephant', 'elegant', 'elephantine', 'election'],pref = "ele") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['celebration', 'celebrity', 'celebratory', 'celebration'],pref = "celeb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['celebration', 'celebrity', 'celebratory', 'celebration'],pref = "celeb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['achievement', 'achieve', 'achiever', 'achievable'],pref = "achi") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['achievement', 'achieve', 'achiever', 'achievable'],pref = "achi") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['development', 'debug', 'document', 'disk'],pref = "de") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['development', 'debug', 'document', 'disk'],pref = "de") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'preference', 'prevent', 'president'],pref = "pre") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'preference', 'prevent', 'president'],pref = "pre") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['automobile', 'automatic', 'automate', 'automaton'],pref = "auto") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['automobile', 'automatic', 'automate', 'automaton'],pref = "auto") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['terrific', 'terrify', 'terrestrial', 'territory'],pref = "terr") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['terrific', 'terrify', 'terrestrial', 'territory'],pref = "terr") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['synchronization', 'synchronous', 'synchronize', 'synchronized'],pref = "synch") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['synchronization', 'synchronous', 'synchronize', 'synchronized'],pref = "synch") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abbreviation', 'abrupt', 'absorb', 'absolute'],pref = "abs") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abbreviation', 'abrupt', 'absorb', 'absolute'],pref = "abs") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repetition', 'reproductive', 'represent', 'reputation', 'reprehend'],pref = "rep") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repetition', 'reproductive', 'represent', 'reputation', 'reprehend'],pref = "rep") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'application', 'applicant', 'appetite'],pref = "app") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'application', 'applicant', 'appetite'],pref = "app") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'xylography', 'xylophone', 'xylophone'],pref = "xy") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'xylography', 'xylophone', 'xylophone'],pref = "xy") == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['test', 'testing', 'tested', 'testing'],pref = "test") == 4
    assert candidate(words = ['abc', 'bcd', 'cde'],pref = "a") == 1
    assert candidate(words = ['hello', 'world', 'helium', 'helper'],pref = "hel") == 3
    assert candidate(words = ['banana', 'bandana', 'banner', 'balance'],pref = "ban") == 3
    assert candidate(words = ['hello', 'hell', 'hero', 'herald'],pref = "he") == 4
    assert candidate(words = ['pay', 'attention', 'practice', 'attend'],pref = "at") == 2
    assert candidate(words = ['hello', 'world'],pref = "hi") == 0
    assert candidate(words = ['hello', 'hell', 'helper'],pref = "hel") == 3
    assert candidate(words = ['apple', 'apricot', 'application'],pref = "app") == 2
    assert candidate(words = ['apple', 'apricot', 'application', 'appetite'],pref = "app") == 3
    assert candidate(words = ['cat', 'caterpillar', 'catalog', 'category'],pref = "cat") == 4
    assert candidate(words = ['apple', 'apricot', 'banana', 'apex'],pref = "ap") == 3
    assert candidate(words = ['banana', 'band', 'ball'],pref = "ba") == 3
    assert candidate(words = ['banana', 'bandana', 'baptism'],pref = "ban") == 2
    assert candidate(words = ['apple', 'application', 'apricot', 'apex'],pref = "ap") == 4
    assert candidate(words = ['leetcode', 'win', 'loops', 'success'],pref = "code") == 0
    assert candidate(words = ['database', 'datacenter', 'datamine', 'data'],pref = "data") == 4
    assert candidate(words = ['integration', 'integrate', 'interact', 'interactive'],pref = "inte") == 4
    assert candidate(words = ['algorithm', 'array', 'application', 'arithmetic'],pref = "arr") == 1
    assert candidate(words = ['intersection', 'interface', 'internal', 'interact'],pref = "inter") == 4
    assert candidate(words = ['unpredictable', 'unpredicted', 'unpredictably', 'unpredicting'],pref = "unpred") == 4
    assert candidate(words = ['prefix', 'prepend', 'presentation', 'preference'],pref = "pre") == 4
    assert candidate(words = ['challenge', 'champion', 'chance', 'character'],pref = "cha") == 4
    assert candidate(words = ['management', 'manager', 'manufacture', 'maintain'],pref = "man") == 3
    assert candidate(words = ['interpolation', 'interpolate', 'interpolator', 'interpolated'],pref = "inter") == 4
    assert candidate(words = ['technology', 'technique', 'technical', 'technological'],pref = "tech") == 4
    assert candidate(words = ['universe', 'uniform', 'unique', 'unit'],pref = "uni") == 4
    assert candidate(words = ['programming', 'python', 'problem', 'project', 'practice'],pref = "pro") == 3
    assert candidate(words = ['document', 'documentation', 'documentary', 'documents'],pref = "docu") == 4
    assert candidate(words = ['environment', 'envelope', 'encyclopedia', 'enterprise'],pref = "env") == 2
    assert candidate(words = ['interview', 'international', 'internet', 'introduce'],pref = "inter") == 3
    assert candidate(words = ['communication', 'community', 'commemoration', 'commentary'],pref = "comm") == 4
    assert candidate(words = ['algorithm', 'array', 'application', 'apricot'],pref = "app") == 1
    assert candidate(words = ['cryptography', 'cryptanalysis', 'cryptographic', 'cryptology'],pref = "crypto") == 3
    assert candidate(words = ['interact', 'interaction', 'interactive', 'interior', 'intercept'],pref = "inter") == 5
    assert candidate(words = ['fantastic', 'fancy', 'fantasy', 'fanatic'],pref = "fan") == 4
    assert candidate(words = ['pseudo', 'pseudocode', 'pseudorandom', 'pseudoscience'],pref = "pseudo") == 4
    assert candidate(words = ['mathematical', 'mathematics', 'mathematically', 'mathematize'],pref = "math") == 4
    assert candidate(words = ['programming', 'problem', 'prefix', 'preference'],pref = "pre") == 2
    assert candidate(words = ['biography', 'biologist', 'biological', 'biographical'],pref = "bio") == 4
    assert candidate(words = ['unbelievable', 'universe', 'unique', 'unanimous'],pref = "un") == 4
    assert candidate(words = ['congratulations', 'congratulate', 'congratulatory', 'congregate', 'congruity'],pref = "cong") == 5
    assert candidate(words = ['supplementary', 'supplement', 'supplier', 'suppose'],pref = "sup") == 4
    assert candidate(words = ['community', 'commune', 'communicate', 'common'],pref = "comm") == 4
    assert candidate(words = ['extraterrestrial', 'extraterrestrial', 'extraterrestrial', 'extraterrestrial'],pref = "extra") == 4
    assert candidate(words = ['algorithm', 'array', 'application', 'applet'],pref = "app") == 2
    assert candidate(words = ['abracadabra', 'abstract', 'absorb', 'academic'],pref = "abs") == 2
    assert candidate(words = ['congruence', 'congruent', 'congruently', 'congruency'],pref = "congru") == 4
    assert candidate(words = ['meticulous', 'meticulate', 'metaphor', 'metaphysics'],pref = "metic") == 2
    assert candidate(words = ['biological', 'biography', 'biologist', 'biology', 'bioluminescence'],pref = "biol") == 4
    assert candidate(words = ['application', 'approach', 'appetizer', 'append'],pref = "app") == 4
    assert candidate(words = ['scientific', 'scientist', 'science', 'sciences'],pref = "sci") == 4
    assert candidate(words = ['communication', 'community', 'common', 'commodity'],pref = "com") == 4
    assert candidate(words = ['quantization', 'quantize', 'quantitative', 'quantitative'],pref = "quant") == 4
    assert candidate(words = ['prefix', 'prepend', 'presentation', 'premature'],pref = "pre") == 4
    assert candidate(words = ['continuous', 'concurrent', 'conclusion', 'condition'],pref = "con") == 4
    assert candidate(words = ['programming', 'program', 'pro', 'professor'],pref = "pro") == 4
    assert candidate(words = ['management', 'manager', 'manage', 'mandate'],pref = "man") == 4
    assert candidate(words = ['transformation', 'transmit', 'transparent', 'transient'],pref = "tran") == 4
    assert candidate(words = ['administrator', 'administration', 'administrative', 'administratively'],pref = "admin") == 4
    assert candidate(words = ['circumstance', 'circuit', 'circulate', 'circulation', 'circular'],pref = "circu") == 5
    assert candidate(words = ['characterization', 'character', 'characteristic', 'characterization'],pref = "char") == 4
    assert candidate(words = ['environment', 'envy', 'envelope', 'evening'],pref = "env") == 3
    assert candidate(words = ['database', 'data', 'datagram', 'datastructure'],pref = "data") == 4
    assert candidate(words = ['celebration', 'celebrate', 'celebrity', 'celebratory', 'celestial'],pref = "celeb") == 4
    assert candidate(words = ['cryptography', 'crypt', 'crypto', 'cryptanalysis'],pref = "crypt") == 4
    assert candidate(words = ['photography', 'photo', 'photobook', 'photographer'],pref = "photo") == 4
    assert candidate(words = ['magnify', 'magnificent', 'magnetic', 'magnetism'],pref = "mag") == 4
    assert candidate(words = ['organization', 'organize', 'organ', 'organically'],pref = "org") == 4
    assert candidate(words = ['algorithm', 'algebra', 'almond', 'alert'],pref = "alg") == 2
    assert candidate(words = ['algorithm', 'array', 'application', 'apple'],pref = "app") == 2
    assert candidate(words = ['communication', 'community', 'commitment', 'common'],pref = "comm") == 4
    assert candidate(words = ['developer', 'debug', 'deploy', 'document'],pref = "de") == 3
    assert candidate(words = ['perpendicular', 'perpendicularity', 'perpendicularity', 'perpendicularly'],pref = "perpendicular") == 4
    assert candidate(words = ['environment', 'engine', 'error', 'example'],pref = "en") == 2
    assert candidate(words = ['university', 'uniform', 'unique', 'universe'],pref = "uni") == 4
    assert candidate(words = ['community', 'communist', 'common', 'comment'],pref = "comm") == 4
    assert candidate(words = ['literature', 'literacy', 'literary', 'literate'],pref = "lit") == 4
    assert candidate(words = ['sequoia', 'sequence', 'series', 'serial'],pref = "ser") == 2
    assert candidate(words = ['communication', 'community', 'companion', 'commune'],pref = "comm") == 3
    assert candidate(words = ['algorithm', 'algebra', 'alignment', 'algorithmic'],pref = "algo") == 2
    assert candidate(words = ['character', 'chart', 'chapter', 'charge'],pref = "char") == 3
    assert candidate(words = ['transport', 'trap', 'trapezium', 'traverse'],pref = "tra") == 4
    assert candidate(words = ['communication', 'commute', 'community', 'commotion', 'common'],pref = "comm") == 5
    assert candidate(words = ['environment', 'energy', 'engage', 'engageable'],pref = "en") == 4
    assert candidate(words = ['identification', 'individual', 'idea', 'illegal'],pref = "iden") == 1
    assert candidate(words = ['supreme', 'superior', 'surpass', 'surround'],pref = "sur") == 2
    assert candidate(words = ['transformation', 'transmit', 'transit', 'transformation', 'transition'],pref = "trans") == 5
    assert candidate(words = ['automation', 'automatic', 'automate', 'auto'],pref = "auto") == 4
    assert candidate(words = ['configuration', 'compute', 'container', 'cloud'],pref = "con") == 2
    assert candidate(words = ['communication', 'community', 'commitment', 'compassionate'],pref = "comm") == 3
    assert candidate(words = ['programming', 'program', 'pro', 'progress'],pref = "pro") == 4
    assert candidate(words = ['absolutely', 'absolute', 'absorb', 'abnormal'],pref = "abs") == 3
    assert candidate(words = ['statistics', 'statistical', 'statue', 'status'],pref = "stat") == 4
    assert candidate(words = ['prefix', 'prefixes', 'preferring', 'preference'],pref = "pref") == 4
    assert candidate(words = ['congratulations', 'congratulate', 'congratulatory', 'congratulated'],pref = "congrat") == 4
    assert candidate(words = ['environment', 'essential', 'establish', 'engage'],pref = "en") == 2
    assert candidate(words = ['substitution', 'substitute', 'substituted', 'substituting'],pref = "sub") == 4
    assert candidate(words = ['distribution', 'distribute', 'disastrous', 'discuss', 'disease'],pref = "dis") == 5
    assert candidate(words = ['development', 'deploy', 'debug', 'document'],pref = "de") == 3
    assert candidate(words = ['super', 'superhero', 'supercalifragilisticexpialidocious', 'supervillain'],pref = "super") == 4
    assert candidate(words = ['maintenance', 'maintain', 'maintenance', 'maintained'],pref = "maint") == 4
    assert candidate(words = ['python', 'pyramid', 'pythia', 'pyrotechnic'],pref = "pyt") == 2
    assert candidate(words = ['algorithm', 'algebra', 'alibi', 'alien', 'alimony'],pref = "ali") == 3
    assert candidate(words = ['remarkable', 'remark', 'remember', 'remind'],pref = "rem") == 4
    assert candidate(words = ['septagon', 'septagonal', 'septembre', 'septenary'],pref = "sept") == 4
    assert candidate(words = ['programming', 'progress', 'prompt', 'priority'],pref = "pro") == 3
    assert candidate(words = ['document', 'documentation', 'documentary', 'documents'],pref = "doc") == 4
    assert candidate(words = ['monarch', 'monarchy', 'monarchic', 'monarchically'],pref = "monarch") == 4
    assert candidate(words = ['hemisphere', 'hemispherical', 'hemispheres', 'hemispheric'],pref = "hemis") == 4
    assert candidate(words = ['environment', 'engage', 'enhance', 'enforce', 'ensure'],pref = "enf") == 1
    assert candidate(words = ['persistent', 'perspective', 'personality', 'person', 'personnel'],pref = "pers") == 5
    assert candidate(words = ['prefix', 'preference', 'presentation', 'prevent', 'president'],pref = "pre") == 5
    assert candidate(words = ['parallelogram', 'parallelepiped', 'parallel', 'parallelograms'],pref = "parallel") == 4
    assert candidate(words = ['intelligence', 'integrate', 'intensity', 'interact'],pref = "inte") == 4
    assert candidate(words = ['information', 'infrastructure', 'insurance', 'initial'],pref = "in") == 4
    assert candidate(words = ['transport', 'transmit', 'transformation', 'transition'],pref = "trans") == 4
    assert candidate(words = ['establish', 'estimate', 'essential', 'establishment'],pref = "est") == 3
    assert candidate(words = ['algorithm', 'algebra', 'alchemist', 'alchemy'],pref = "alg") == 2
    assert candidate(words = ['environment', 'envelope', 'engage', 'enhance'],pref = "en") == 4
    assert candidate(words = ['transport', 'transmit', 'transit', 'transformation', 'transition'],pref = "trans") == 5
    assert candidate(words = ['programming', 'problem', 'process', 'productivity'],pref = "pro") == 4
    assert candidate(words = ['programming', 'pro', 'processor', 'productivity'],pref = "pro") == 4
    assert candidate(words = ['encyclopedia', 'encyclopedias', 'encyclopedic', 'encyclopedically'],pref = "ency") == 4
    assert candidate(words = ['apple', 'application', 'appetite', 'apparent'],pref = "app") == 4
    assert candidate(words = ['zebra', 'zephyr', 'zoo', 'zealous'],pref = "ze") == 3
    assert candidate(words = ['prefix', 'prefixes', 'preference', 'preferring'],pref = "pref") == 4
    assert candidate(words = ['communication', 'community', 'commitment', 'commission'],pref = "com") == 4
    assert candidate(words = ['hypothesis', 'historical', 'hyphen', 'hydrogen'],pref = "hy") == 3
    assert candidate(words = ['transformation', 'transfer', 'transform', 'transformer'],pref = "trans") == 4
    assert candidate(words = ['transaction', 'transfer', 'transition', 'transportation'],pref = "tran") == 4
    assert candidate(words = ['abracadabra', 'abrakadabras', 'abracadabrac', 'abracadabrad'],pref = "abrac") == 3
    assert candidate(words = ['interview', 'integrate', 'interaction', 'interface'],pref = "inte") == 4
    assert candidate(words = ['fantastic', 'fantasy', 'fancy', 'fantastician'],pref = "fant") == 3
    assert candidate(words = ['communication', 'communicate', 'communist', 'commune'],pref = "comm") == 4
    assert candidate(words = ['environment', 'environ', 'environmental', 'envelope'],pref = "env") == 4
    assert candidate(words = ['education', 'educational', 'educate', 'educator'],pref = "edu") == 4
    assert candidate(words = ['automation', 'automobile', 'automatic', 'automate'],pref = "auto") == 4
    assert candidate(words = ['customization', 'customize', 'custom', 'customarily'],pref = "cust") == 4
    assert candidate(words = ['environment', 'encourage', 'endure', 'ensure'],pref = "en") == 4
    assert candidate(words = ['prefix', 'predict', 'prevent', 'preach', 'prelude'],pref = "pre") == 5
    assert candidate(words = ['elephant', 'elegant', 'elephantine', 'election'],pref = "ele") == 4
    assert candidate(words = ['celebration', 'celebrity', 'celebratory', 'celebration'],pref = "celeb") == 4
    assert candidate(words = ['achievement', 'achieve', 'achiever', 'achievable'],pref = "achi") == 4
    assert candidate(words = ['development', 'debug', 'document', 'disk'],pref = "de") == 2
    assert candidate(words = ['prefix', 'preference', 'prevent', 'president'],pref = "pre") == 4
    assert candidate(words = ['automobile', 'automatic', 'automate', 'automaton'],pref = "auto") == 4
    assert candidate(words = ['terrific', 'terrify', 'terrestrial', 'territory'],pref = "terr") == 4
    assert candidate(words = ['synchronization', 'synchronous', 'synchronize', 'synchronized'],pref = "synch") == 4
    assert candidate(words = ['abbreviation', 'abrupt', 'absorb', 'absolute'],pref = "abs") == 2
    assert candidate(words = ['repetition', 'reproductive', 'represent', 'reputation', 'reprehend'],pref = "rep") == 5
    assert candidate(words = ['apple', 'application', 'applicant', 'appetite'],pref = "app") == 4
    assert candidate(words = ['xylophone', 'xylography', 'xylophone', 'xylophone'],pref = "xy") == 4


