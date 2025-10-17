def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(licensePlate = "GrC8950",words = ['grace', 'please']) == "grace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "GrC8950",words = ['grace', 'please']) == "grace": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "Ah71752",words = ['enough', 'these', 'playground', 'point', 'president']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "Ah71752",words = ['enough', 'these', 'playground', 'point', 'president']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "xyz",words = ['xzy', 'zyx', 'yxz', 'zxy']) == "xzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "xyz",words = ['xzy', 'zyx', 'yxz', 'zxy']) == "xzy": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "44472Ml",words = ['call', 'tall', 'tell']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "44472Ml",words = ['call', 'tall', 'tell']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "a 1 b 2 c 3",words = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "a 1 b 2 c 3",words = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "1s3 456",words = ['looks', 'pest', 'stew', 'show']) == "pest"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "1s3 456",words = ['looks', 'pest', 'stew', 'show']) == "pest": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "1s3 PSt",words = ['step', 'steps', 'stripe', 'stepple']) == "steps"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "1s3 PSt",words = ['step', 'steps', 'stripe', 'stepple']) == "steps": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aBc 12c",words = ['abccdef', 'caaacab', 'cbca']) == "cbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aBc 12c",words = ['abccdef', 'caaacab', 'cbca']) == "cbca": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "a1b2c3d4e5f6g7",words = ['abcdefg', 'defghij', 'ghijklm', 'abcdefghijk', 'abcdeghijk', 'abcdefg', 'abcdefg']) == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "a1b2c3d4e5f6g7",words = ['abcdefg', 'defghij', 'ghijklm', 'abcdefghijk', 'abcdeghijk', 'abcdefg', 'abcdefg']) == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "g7h6i5j4k3l2m1n0",words = ['highlight', 'jimmy', 'mink', 'gnimmik', 'kliming', 'jimmyhighlight']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "g7h6i5j4k3l2m1n0",words = ['highlight', 'jimmy', 'mink', 'gnimmik', 'kliming', 'jimmyhighlight']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "zZyYxX",words = ['zyx', 'yxz', 'xyzzyx', 'zyxzyx', 'zzzyyx', 'zyzyzy', 'xyzzyxzyx']) == "xyzzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "zZyYxX",words = ['zyx', 'yxz', 'xyzzyx', 'zyxzyx', 'zzzyyx', 'zyzyzy', 'xyzzyxzyx']) == "xyzzyx": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "hello world!",words = ['heloworld', 'worldhello', 'helloworld', 'oworlhell', 'rldhellow']) == "worldhello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "hello world!",words = ['heloworld', 'worldhello', 'helloworld', 'oworlhell', 'rldhellow']) == "worldhello": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "q9w8e7r6t5y4u3i2o1p0",words = ['quickbrownfox', 'quizzify', 'piano', 'typewriter', 'pizzafactory', 'qwertyuiop']) == "qwertyuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "q9w8e7r6t5y4u3i2o1p0",words = ['quickbrownfox', 'quizzify', 'piano', 'typewriter', 'pizzafactory', 'qwertyuiop']) == "qwertyuiop": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "XYZ 789",words = ['xylophone', 'xyzzy', 'zyxwvutsrqponmlkjihgfedcba', 'zyxzyxzyx']) == "xyzzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "XYZ 789",words = ['xylophone', 'xyzzy', 'zyxwvutsrqponmlkjihgfedcba', 'zyxzyxzyx']) == "xyzzy": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "M1n2o3r4s5",words = ['modern', 'store', 'monarchs', 'morse', 'minors', 'modes', 'monsters']) == "minors"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "M1n2o3r4s5",words = ['modern', 'store', 'monarchs', 'morse', 'minors', 'modes', 'monsters']) == "minors": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "A1b2C3d4",words = ['completeword', 'complete', 'abcd', 'bacdc', 'badac']) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "A1b2C3d4",words = ['completeword', 'complete', 'abcd', 'bacdc', 'badac']) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "q1w2e3r4t5y6",words = ['qwerty', 'typerq', 'rqwety', 'wertyq', 'eqwrt', 'rqwet', 'qwetrt', 'qwrtqe', 'qwertyu']) == "qwerty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "q1w2e3r4t5y6",words = ['qwerty', 'typerq', 'rqwety', 'wertyq', 'eqwrt', 'rqwet', 'qwetrt', 'qwrtqe', 'qwertyu']) == "qwerty": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "A1B2C3D4E5F6",words = ['abcdef', 'defabc', 'fedcba', 'abcdfe', 'abcdefg', 'abcdefh', 'abcdefij']) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "A1B2C3D4E5F6",words = ['abcdef', 'defabc', 'fedcba', 'abcdfe', 'abcdefg', 'abcdefh', 'abcdefij']) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "z9 x8 v7",words = ['zebra', 'vex', 'vez', 'vexing', 'exhibition']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "z9 x8 v7",words = ['zebra', 'vex', 'vez', 'vexing', 'exhibition']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "zzz",words = ['zzzzzz', 'zzzz', 'zzz', 'zzzzz', 'zzzzzzz']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "zzz",words = ['zzzzzz', 'zzzz', 'zzz', 'zzzzz', 'zzzzzzz']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "9A8B7C6D5E4F3G2H1I0J",words = ['abcdefghij', 'jihgfedcba', 'abcdefghijk', 'abcdefghi', 'abcdefghijl']) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "9A8B7C6D5E4F3G2H1I0J",words = ['abcdefghij', 'jihgfedcba', 'abcdefghijk', 'abcdefghi', 'abcdefghijl']) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "z9y8x7w6v5u4t3s2r1q0",words = ['qrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'reverse', 'alphabet', 'zebra', 'quran']) == "qrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "z9y8x7w6v5u4t3s2r1q0",words = ['qrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'reverse', 'alphabet', 'zebra', 'quran']) == "qrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "qqq rrr sss",words = ['qqrrrss', 'rrssqqq', 'ssqqqrrr', 'qqqrrrsss', 'ssqqqqrrr']) == "qqqrrrsss"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "qqq rrr sss",words = ['qqrrrss', 'rrssqqq', 'ssqqqrrr', 'qqqrrrsss', 'ssqqqqrrr']) == "qqqrrrsss": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "G7H2K3L4",words = ['ghkl', 'hklg', 'klhg', 'klgh', 'gkhll', 'hgkl']) == "ghkl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "G7H2K3L4",words = ['ghkl', 'hklg', 'klhg', 'klgh', 'gkhll', 'hgkl']) == "ghkl": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "9gI2d4e5",words = ['guide', 'gifted', 'digging', 'gigged', 'gadget', 'gigged', 'gagged', 'gagged', 'gagged']) == "guide"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "9gI2d4e5",words = ['guide', 'gifted', 'digging', 'gigged', 'gadget', 'gigged', 'gagged', 'gagged', 'gagged']) == "guide": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "l3i2k4e5",words = ['like', 'liker', 'likely', 'likeable', 'likeless']) == "like"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "l3i2k4e5",words = ['like', 'liker', 'likely', 'likeable', 'likeless']) == "like": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "m1n2o3r4",words = ['immortal', 'monarch', 'romantic', 'moronic', 'motorcar']) == "monarch"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "m1n2o3r4",words = ['immortal', 'monarch', 'romantic', 'moronic', 'motorcar']) == "monarch": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "f9g8h7j6k5",words = ['fjkg', 'ghfk', 'jkhg', 'kjgf', 'hjgk']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "f9g8h7j6k5",words = ['fjkg', 'ghfk', 'jkhg', 'kjgf', 'hjgk']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "4b 5c2 D",words = ['bcd', 'bcdcd', 'bcdc', 'bbcd', 'bcdb']) == "bcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "4b 5c2 D",words = ['bcd', 'bcdcd', 'bcdc', 'bbcd', 'bcdb']) == "bcd": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "3Rd sTreet",words = ['street', 'retreat', 'store', 'restrain', 'sterret', 'druster']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "3Rd sTreet",words = ['street', 'retreat', 'store', 'restrain', 'sterret', 'druster']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aA1bB2cC",words = ['abc', 'aabbcc', 'abbc', 'aabbc', 'aabbbc', 'aabbbcc', 'aabbbccc']) == "aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aA1bB2cC",words = ['abc', 'aabbcc', 'abbc', 'aabbc', 'aabbbc', 'aabbbcc', 'aabbbccc']) == "aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "mN2mN3",words = ['mnm', 'nmn', 'mmn', 'mnn', 'nmm', 'nmmm', 'nmmn']) == "nmmn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "mN2mN3",words = ['mnm', 'nmn', 'mmn', 'mnn', 'nmm', 'nmmm', 'nmmn']) == "nmmn": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "q2w3e4r5t6y7u8i9o0p",words = ['typewriter', 'opposite', 'ipyroteur', 'preoptuitry', 'pyroteurizing']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "q2w3e4r5t6y7u8i9o0p",words = ['typewriter', 'opposite', 'ipyroteur', 'preoptuitry', 'pyroteurizing']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "1234567",words = ['abcdefg', 'bcadefg', 'cbadefg', 'bcaefdg', 'bcaefdgh']) == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "1234567",words = ['abcdefg', 'bcadefg', 'cbadefg', 'bcaefdg', 'bcaefdgh']) == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "x9Y8Z7",words = ['xyz', 'xyzz', 'yxz', 'zyx', 'zxzyx', 'zyzzzyx']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "x9Y8Z7",words = ['xyz', 'xyzz', 'yxz', 'zyx', 'zxzyx', 'zyzzzyx']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "mMnN oO pP",words = ['mnop', 'mnooop', 'mnoppp', 'mnopppp', 'mnoppppp']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "mMnN oO pP",words = ['mnop', 'mnooop', 'mnoppp', 'mnopppp', 'mnoppppp']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aBc12d3E",words = ['abcde', 'abced', 'abcdef', 'abcd', 'abcccde']) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aBc12d3E",words = ['abcde', 'abced', 'abcdef', 'abcd', 'abcccde']) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "xyz XYZ",words = ['xyzz', 'yzxx', 'zxzy', 'zyxzyx', 'zyxzyxz']) == "zyxzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "xyz XYZ",words = ['xyzz', 'yzxx', 'zxzy', 'zyxzyx', 'zyxzyxz']) == "zyxzyx": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aBc123cD",words = ['abcd', 'abcc', 'accc', 'aabbccdd', 'abcde']) == "aabbccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aBc123cD",words = ['abcd', 'abcc', 'accc', 'aabbccdd', 'abcde']) == "aabbccdd": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "z1y2x3w4",words = ['xyzz', 'yzxz', 'zxzy', 'wxyz', 'zyxw']) == "wxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "z1y2x3w4",words = ['xyzz', 'yzxz', 'zxzy', 'wxyz', 'zyxw']) == "wxyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "zzzzz",words = ['zzzz', 'zzz', 'zzzzzz', 'zzzzz', 'zzzzzzz', 'zzzzzzzz']) == "zzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "zzzzz",words = ['zzzz', 'zzz', 'zzzzzz', 'zzzzz', 'zzzzzzz', 'zzzzzzzz']) == "zzzzz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aAaAa 123",words = ['aaaaa', 'aaabc', 'aabbc', 'abcde', 'abbbb', 'abcdaa']) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aAaAa 123",words = ['aaaaa', 'aaabc', 'aabbc', 'abcde', 'abbbb', 'abcdaa']) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aAaAaA",words = ['aaaaaa', 'aaaaaab', 'aaaaaabc', 'aaaaaabcd', 'aaaaaabcde']) == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aAaAaA",words = ['aaaaaa', 'aaaaaab', 'aaaaaabc', 'aaaaaabcd', 'aaaaaabcde']) == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "9A1B2C3D4E5F6G7H",words = ['abcdefgh', 'bacdefgh', 'cabdefgh', 'abcdefghi', 'abcdefg']) == "abcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "9A1B2C3D4E5F6G7H",words = ['abcdefgh', 'bacdefgh', 'cabdefgh', 'abcdefghi', 'abcdefg']) == "abcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aA1Bb2Cc3",words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbcccc', 'aaabbbcc', 'aabbcccd']) == "aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aA1Bb2Cc3",words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbcccc', 'aaabbbcc', 'aabbcccd']) == "aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "oNe TwO thReE",words = ['onetwothree', 'twothreeone', 'onethreetwo', 'threetwoone', 'onetwoonetwo', 'twotoonetwo', 'threethreetwo']) == "onetwothree"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "oNe TwO thReE",words = ['onetwothree', 'twothreeone', 'onethreetwo', 'threetwoone', 'onetwoonetwo', 'twotoonetwo', 'threethreetwo']) == "onetwothree": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aBcDeFgHiJ1234567890",words = ['abcdefghij', 'bacdefghij', 'jihgfedcba', 'abcdefghijk', 'abcdefghijj']) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aBcDeFgHiJ1234567890",words = ['abcdefghij', 'bacdefghij', 'jihgfedcba', 'abcdefghijk', 'abcdefghijj']) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "s9p8a7t6e5",words = ['pastel', 'pasteler', 'paste', 'pastoral', 'past', 'pastor', 'pasta']) == "paste"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "s9p8a7t6e5",words = ['pastel', 'pasteler', 'paste', 'pastoral', 'past', 'pastor', 'pasta']) == "paste": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "XyZ 890",words = ['xyz', 'xyzz', 'xzyz', 'zyxzy', 'zyzzx']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "XyZ 890",words = ['xyz', 'xyzz', 'xzyz', 'zyxzy', 'zyzzx']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "XYZ",words = ['xylophone', 'xylem', 'yxz', 'zyx', 'zyxwvut']) == "yxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "XYZ",words = ['xylophone', 'xylem', 'yxz', 'zyx', 'zyxwvut']) == "yxz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "Z9y2z",words = ['buzzards', 'zyzzyva', 'yz', 'zyzzy', 'zzyzzy']) == "zyzzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "Z9y2z",words = ['buzzards', 'zyzzyva', 'yz', 'zyzzy', 'zzyzzy']) == "zyzzy": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "XyZ9",words = ['zyx', 'xyzzy', 'yzzx', 'xyzz', 'zyzzxy']) == "zyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "XyZ9",words = ['zyx', 'xyzzy', 'yzzx', 'xyzz', 'zyzzxy']) == "zyx": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "f9o8x7",words = ['fox', 'foxy', 'foxtrot', 'fix', 'fixes', 'foxtrotted', 'foxtrotter']) == "fox"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "f9o8x7",words = ['fox', 'foxy', 'foxtrot', 'fix', 'fixes', 'foxtrotted', 'foxtrotter']) == "fox": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "XYZ 123",words = ['exactly', 'xyzzyx', 'zyxzyx', 'zyzyzx', 'zyzyxzyx']) == "xyzzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "XYZ 123",words = ['exactly', 'xyzzyx', 'zyxzyx', 'zyzyzx', 'zyzyxzyx']) == "xyzzyx": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "1 2 3 a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3",words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz']) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "1 2 3 a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3",words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz']) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "b1r2e3",words = ['berber', 'bereber', 'beriberi', 'reberber', 'beerbar']) == "berber"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "b1r2e3",words = ['berber', 'bereber', 'beriberi', 'reberber', 'beerbar']) == "berber": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "a1B2c3D4",words = ['abcd', 'abdc', 'abcde', 'bacd', 'adcb']) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "a1B2c3D4",words = ['abcd', 'abdc', 'abcde', 'bacd', 'adcb']) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "123aaBBB456",words = ['aabbb', 'abbbb', 'baaabbb', 'bbbaaab', 'bbbaaabbb']) == "aabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "123aaBBB456",words = ['aabbb', 'abbbb', 'baaabbb', 'bbbaaab', 'bbbaaabbb']) == "aabbb": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "!!!abc###",words = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "!!!abc###",words = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aA1bB2cC3",words = ['abc', 'aabbcc', 'aaabbbccc', 'abbc', 'abbbcc']) == "aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aA1bB2cC3",words = ['abc', 'aabbcc', 'aaabbbccc', 'abbc', 'abbbcc']) == "aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "p1QR2",words = ['prq', 'pqr', 'pqrr', 'prqq', 'pqrrr', 'pqqrr']) == "prq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "p1QR2",words = ['prq', 'pqr', 'pqrr', 'prqq', 'pqrrr', 'pqqrr']) == "prq": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz']) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz']) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "f!@#o1b2a3r4",words = ['barfoot', 'aborfra', 'barform', 'barrofa', 'aborfar', 'barrage', 'baraffe', 'barfree']) == "barfoot"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "f!@#o1b2a3r4",words = ['barfoot', 'aborfra', 'barform', 'barrofa', 'aborfar', 'barrage', 'baraffe', 'barfree']) == "barfoot": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "bLUE cAR 2022",words = ['blueberry', 'blueprint', 'carbon', 'barcelona', 'bark']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "bLUE cAR 2022",words = ['blueberry', 'blueprint', 'carbon', 'barcelona', 'bark']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "mN9mN",words = ['minnesota', 'miamin', 'manana', 'mimic', 'mimicry', 'mining', 'minimum']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "mN9mN",words = ['minnesota', 'miamin', 'manana', 'mimic', 'mimicry', 'mining', 'minimum']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "xyZ123 456",words = ['xyzxyz', 'zyxzyx', 'xyzzx', 'yxzxz', 'zxyzyx']) == "xyzzx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "xyZ123 456",words = ['xyzxyz', 'zyxzyx', 'xyzzx', 'yxzxz', 'zxyzyx']) == "xyzzx": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "!@#$%^&*()_+aBc123",words = ['abc', 'cba', 'bac', 'bca', 'cab', 'acb', 'aab', 'abb', 'bba', 'bbc', 'bcb', 'bacb', 'bcab', 'bacab', 'bacabc', 'bacabcd', 'bacabcde', 'bacabcdef', 'bacabcdefg']) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "!@#$%^&*()_+aBc123",words = ['abc', 'cba', 'bac', 'bca', 'cab', 'acb', 'aab', 'abb', 'bba', 'bbc', 'bcb', 'bacb', 'bcab', 'bacab', 'bacabc', 'bacabcd', 'bacabcde', 'bacabcdef', 'bacabcdefg']) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "abc def ghi",words = ['abcdefghi', 'defghibac', 'ghidefab', 'bacdefghi', 'abcdefghij']) == "abcdefghi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "abc def ghi",words = ['abcdefghi', 'defghibac', 'ghidefab', 'bacdefghi', 'abcdefghij']) == "abcdefghi": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "a1b2c3d4e5",words = ['abcde', 'bcdea', 'cabde', 'decab', 'edcba', 'abcdde', 'abcdee', 'abcdeee', 'abcdeeee']) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "a1b2c3d4e5",words = ['abcde', 'bcdea', 'cabde', 'decab', 'edcba', 'abcdde', 'abcdee', 'abcdeee', 'abcdeeee']) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "Gh00t2!@#",words = ['ghostly', 'gnostic', 'ghost', 'tongue', 'tooth']) == "ghost"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "Gh00t2!@#",words = ['ghostly', 'gnostic', 'ghost', 'tongue', 'tooth']) == "ghost": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "m2i5n4i3s5",words = ['immisions', 'minimises', 'administs', 'ministers', 'misissues']) == "immisions"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "m2i5n4i3s5",words = ['immisions', 'minimises', 'administs', 'ministers', 'misissues']) == "immisions": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "!@#$%^&*()",words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf']) == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "!@#$%^&*()",words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf']) == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "a2b3c4d5e6",words = ['alphabet', 'bacded', 'abacax', 'decalbac', 'abacbac']) == "bacded"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "a2b3c4d5e6",words = ['alphabet', 'bacded', 'abacax', 'decalbac', 'abacbac']) == "bacded": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "xyZ 123",words = ['xyzzy', 'zyxwvutsrqponmlkjihgfedcba', 'zyxzyxzyx', 'xyzz', 'zyx', 'xyzx', 'xyzxy', 'xyzxyz', 'xyzxyzz', 'xyzxyzxy']) == "zyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "xyZ 123",words = ['xyzzy', 'zyxwvutsrqponmlkjihgfedcba', 'zyxzyxzyx', 'xyzz', 'zyx', 'xyzx', 'xyzxy', 'xyzxyz', 'xyzxyzz', 'xyzxyzxy']) == "zyx": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "mno890",words = ['mno', 'mon', 'nom', 'omn', 'nmo', 'omnmo', 'mnomo', 'omonomn']) == "mno"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "mno890",words = ['mno', 'mon', 'nom', 'omn', 'nmo', 'omnmo', 'mnomo', 'omonomn']) == "mno": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "mno9PQR8",words = ['mnopqr', 'nopqmr', 'pqmrno', 'mnopq', 'pqmnopr', 'mnopqrq']) == "mnopqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "mno9PQR8",words = ['mnopqr', 'nopqmr', 'pqmrno', 'mnopq', 'pqmnopr', 'mnopqrq']) == "mnopqr": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "1a2b3c4d5e",words = ['abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "1a2b3c4d5e",words = ['abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "aA bB cC",words = ['abc', 'abccba', 'cab', 'bcaac', 'acbac']) == "abccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "aA bB cC",words = ['abc', 'abccba', 'cab', 'bcaac', 'acbac']) == "abccba": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "zzz",words = ['zzzz', 'zzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "zzz",words = ['zzzz', 'zzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "123abc ABC321",words = ['cba', 'abc', 'bac', 'bca', 'cab', 'acb', 'aab', 'abb', 'bba', 'bbc', 'bcb', 'bacb', 'bcab', 'bacab', 'bacabc', 'bacabcd', 'bacabcde', 'bacabcdef', 'bacabcdefg']) == "bacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "123abc ABC321",words = ['cba', 'abc', 'bac', 'bca', 'cab', 'acb', 'aab', 'abb', 'bba', 'bbc', 'bcb', 'bacb', 'bcab', 'bacab', 'bacabc', 'bacabcd', 'bacabcde', 'bacabcdef', 'bacabcdefg']) == "bacabc": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "q9w8e7r6",words = ['qwerty', 'qwertas', 'qwertyui', 'qwertyuio', 'qwertyuiop']) == "qwerty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "q9w8e7r6",words = ['qwerty', 'qwertas', 'qwertyui', 'qwertyuio', 'qwertyuiop']) == "qwerty": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "qQwWeEr RtTyYuUiIoOpP",words = ['qwertyuiop', 'qwertyuio', 'qwertyuiopp', 'qwertyuioppq', 'qwertyuiopqq']) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "qQwWeEr RtTyYuUiIoOpP",words = ['qwertyuiop', 'qwertyuio', 'qwertyuiopp', 'qwertyuioppq', 'qwertyuiopqq']) == None: {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "xYz987",words = ['xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx', 'xxxyyzzz']) == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "xYz987",words = ['xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx', 'xxxyyzzz']) == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "XYZ 987",words = ['xyzz', 'zyxw', 'zyxv', 'zyxuv', 'zyxwvut']) == "xyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "XYZ 987",words = ['xyzz', 'zyxw', 'zyxv', 'zyxuv', 'zyxwvut']) == "xyzz": {e}')
    
    total += 1
    try:
        result = candidate(licensePlate = "P2l3l4o5",words = ['poll', 'pillar', 'pollock', 'polyope', 'plaster', 'polyope']) == "poll"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(licensePlate = "P2l3l4o5",words = ['poll', 'pillar', 'pollock', 'polyope', 'plaster', 'polyope']) == "poll": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(licensePlate = "GrC8950",words = ['grace', 'please']) == "grace"
    assert candidate(licensePlate = "Ah71752",words = ['enough', 'these', 'playground', 'point', 'president']) == None
    assert candidate(licensePlate = "xyz",words = ['xzy', 'zyx', 'yxz', 'zxy']) == "xzy"
    assert candidate(licensePlate = "44472Ml",words = ['call', 'tall', 'tell']) == None
    assert candidate(licensePlate = "a 1 b 2 c 3",words = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba']) == "abc"
    assert candidate(licensePlate = "1s3 456",words = ['looks', 'pest', 'stew', 'show']) == "pest"
    assert candidate(licensePlate = "1s3 PSt",words = ['step', 'steps', 'stripe', 'stepple']) == "steps"
    assert candidate(licensePlate = "aBc 12c",words = ['abccdef', 'caaacab', 'cbca']) == "cbca"
    assert candidate(licensePlate = "a1b2c3d4e5f6g7",words = ['abcdefg', 'defghij', 'ghijklm', 'abcdefghijk', 'abcdeghijk', 'abcdefg', 'abcdefg']) == "abcdefg"
    assert candidate(licensePlate = "g7h6i5j4k3l2m1n0",words = ['highlight', 'jimmy', 'mink', 'gnimmik', 'kliming', 'jimmyhighlight']) == None
    assert candidate(licensePlate = "zZyYxX",words = ['zyx', 'yxz', 'xyzzyx', 'zyxzyx', 'zzzyyx', 'zyzyzy', 'xyzzyxzyx']) == "xyzzyx"
    assert candidate(licensePlate = "hello world!",words = ['heloworld', 'worldhello', 'helloworld', 'oworlhell', 'rldhellow']) == "worldhello"
    assert candidate(licensePlate = "q9w8e7r6t5y4u3i2o1p0",words = ['quickbrownfox', 'quizzify', 'piano', 'typewriter', 'pizzafactory', 'qwertyuiop']) == "qwertyuiop"
    assert candidate(licensePlate = "XYZ 789",words = ['xylophone', 'xyzzy', 'zyxwvutsrqponmlkjihgfedcba', 'zyxzyxzyx']) == "xyzzy"
    assert candidate(licensePlate = "M1n2o3r4s5",words = ['modern', 'store', 'monarchs', 'morse', 'minors', 'modes', 'monsters']) == "minors"
    assert candidate(licensePlate = "A1b2C3d4",words = ['completeword', 'complete', 'abcd', 'bacdc', 'badac']) == "abcd"
    assert candidate(licensePlate = "q1w2e3r4t5y6",words = ['qwerty', 'typerq', 'rqwety', 'wertyq', 'eqwrt', 'rqwet', 'qwetrt', 'qwrtqe', 'qwertyu']) == "qwerty"
    assert candidate(licensePlate = "A1B2C3D4E5F6",words = ['abcdef', 'defabc', 'fedcba', 'abcdfe', 'abcdefg', 'abcdefh', 'abcdefij']) == "abcdef"
    assert candidate(licensePlate = "z9 x8 v7",words = ['zebra', 'vex', 'vez', 'vexing', 'exhibition']) == None
    assert candidate(licensePlate = "zzz",words = ['zzzzzz', 'zzzz', 'zzz', 'zzzzz', 'zzzzzzz']) == "zzz"
    assert candidate(licensePlate = "9A8B7C6D5E4F3G2H1I0J",words = ['abcdefghij', 'jihgfedcba', 'abcdefghijk', 'abcdefghi', 'abcdefghijl']) == "abcdefghij"
    assert candidate(licensePlate = "z9y8x7w6v5u4t3s2r1q0",words = ['qrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'reverse', 'alphabet', 'zebra', 'quran']) == "qrstuvwxyz"
    assert candidate(licensePlate = "qqq rrr sss",words = ['qqrrrss', 'rrssqqq', 'ssqqqrrr', 'qqqrrrsss', 'ssqqqqrrr']) == "qqqrrrsss"
    assert candidate(licensePlate = "G7H2K3L4",words = ['ghkl', 'hklg', 'klhg', 'klgh', 'gkhll', 'hgkl']) == "ghkl"
    assert candidate(licensePlate = "9gI2d4e5",words = ['guide', 'gifted', 'digging', 'gigged', 'gadget', 'gigged', 'gagged', 'gagged', 'gagged']) == "guide"
    assert candidate(licensePlate = "l3i2k4e5",words = ['like', 'liker', 'likely', 'likeable', 'likeless']) == "like"
    assert candidate(licensePlate = "m1n2o3r4",words = ['immortal', 'monarch', 'romantic', 'moronic', 'motorcar']) == "monarch"
    assert candidate(licensePlate = "f9g8h7j6k5",words = ['fjkg', 'ghfk', 'jkhg', 'kjgf', 'hjgk']) == None
    assert candidate(licensePlate = "4b 5c2 D",words = ['bcd', 'bcdcd', 'bcdc', 'bbcd', 'bcdb']) == "bcd"
    assert candidate(licensePlate = "3Rd sTreet",words = ['street', 'retreat', 'store', 'restrain', 'sterret', 'druster']) == None
    assert candidate(licensePlate = "aA1bB2cC",words = ['abc', 'aabbcc', 'abbc', 'aabbc', 'aabbbc', 'aabbbcc', 'aabbbccc']) == "aabbcc"
    assert candidate(licensePlate = "mN2mN3",words = ['mnm', 'nmn', 'mmn', 'mnn', 'nmm', 'nmmm', 'nmmn']) == "nmmn"
    assert candidate(licensePlate = "q2w3e4r5t6y7u8i9o0p",words = ['typewriter', 'opposite', 'ipyroteur', 'preoptuitry', 'pyroteurizing']) == None
    assert candidate(licensePlate = "1234567",words = ['abcdefg', 'bcadefg', 'cbadefg', 'bcaefdg', 'bcaefdgh']) == "abcdefg"
    assert candidate(licensePlate = "x9Y8Z7",words = ['xyz', 'xyzz', 'yxz', 'zyx', 'zxzyx', 'zyzzzyx']) == "xyz"
    assert candidate(licensePlate = "mMnN oO pP",words = ['mnop', 'mnooop', 'mnoppp', 'mnopppp', 'mnoppppp']) == None
    assert candidate(licensePlate = "aBc12d3E",words = ['abcde', 'abced', 'abcdef', 'abcd', 'abcccde']) == "abcde"
    assert candidate(licensePlate = "xyz XYZ",words = ['xyzz', 'yzxx', 'zxzy', 'zyxzyx', 'zyxzyxz']) == "zyxzyx"
    assert candidate(licensePlate = "aBc123cD",words = ['abcd', 'abcc', 'accc', 'aabbccdd', 'abcde']) == "aabbccdd"
    assert candidate(licensePlate = "z1y2x3w4",words = ['xyzz', 'yzxz', 'zxzy', 'wxyz', 'zyxw']) == "wxyz"
    assert candidate(licensePlate = "zzzzz",words = ['zzzz', 'zzz', 'zzzzzz', 'zzzzz', 'zzzzzzz', 'zzzzzzzz']) == "zzzzz"
    assert candidate(licensePlate = "aAaAa 123",words = ['aaaaa', 'aaabc', 'aabbc', 'abcde', 'abbbb', 'abcdaa']) == "aaaaa"
    assert candidate(licensePlate = "aAaAaA",words = ['aaaaaa', 'aaaaaab', 'aaaaaabc', 'aaaaaabcd', 'aaaaaabcde']) == "aaaaaa"
    assert candidate(licensePlate = "9A1B2C3D4E5F6G7H",words = ['abcdefgh', 'bacdefgh', 'cabdefgh', 'abcdefghi', 'abcdefg']) == "abcdefgh"
    assert candidate(licensePlate = "aA1Bb2Cc3",words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbcccc', 'aaabbbcc', 'aabbcccd']) == "aabbcc"
    assert candidate(licensePlate = "oNe TwO thReE",words = ['onetwothree', 'twothreeone', 'onethreetwo', 'threetwoone', 'onetwoonetwo', 'twotoonetwo', 'threethreetwo']) == "onetwothree"
    assert candidate(licensePlate = "aBcDeFgHiJ1234567890",words = ['abcdefghij', 'bacdefghij', 'jihgfedcba', 'abcdefghijk', 'abcdefghijj']) == "abcdefghij"
    assert candidate(licensePlate = "s9p8a7t6e5",words = ['pastel', 'pasteler', 'paste', 'pastoral', 'past', 'pastor', 'pasta']) == "paste"
    assert candidate(licensePlate = "XyZ 890",words = ['xyz', 'xyzz', 'xzyz', 'zyxzy', 'zyzzx']) == "xyz"
    assert candidate(licensePlate = "XYZ",words = ['xylophone', 'xylem', 'yxz', 'zyx', 'zyxwvut']) == "yxz"
    assert candidate(licensePlate = "Z9y2z",words = ['buzzards', 'zyzzyva', 'yz', 'zyzzy', 'zzyzzy']) == "zyzzy"
    assert candidate(licensePlate = "XyZ9",words = ['zyx', 'xyzzy', 'yzzx', 'xyzz', 'zyzzxy']) == "zyx"
    assert candidate(licensePlate = "f9o8x7",words = ['fox', 'foxy', 'foxtrot', 'fix', 'fixes', 'foxtrotted', 'foxtrotter']) == "fox"
    assert candidate(licensePlate = "XYZ 123",words = ['exactly', 'xyzzyx', 'zyxzyx', 'zyzyzx', 'zyzyxzyx']) == "xyzzyx"
    assert candidate(licensePlate = "1 2 3 a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3",words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz']) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(licensePlate = "b1r2e3",words = ['berber', 'bereber', 'beriberi', 'reberber', 'beerbar']) == "berber"
    assert candidate(licensePlate = "a1B2c3D4",words = ['abcd', 'abdc', 'abcde', 'bacd', 'adcb']) == "abcd"
    assert candidate(licensePlate = "123aaBBB456",words = ['aabbb', 'abbbb', 'baaabbb', 'bbbaaab', 'bbbaaabbb']) == "aabbb"
    assert candidate(licensePlate = "!!!abc###",words = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba']) == "abc"
    assert candidate(licensePlate = "aA1bB2cC3",words = ['abc', 'aabbcc', 'aaabbbccc', 'abbc', 'abbbcc']) == "aabbcc"
    assert candidate(licensePlate = "p1QR2",words = ['prq', 'pqr', 'pqrr', 'prqq', 'pqrrr', 'pqqrr']) == "prq"
    assert candidate(licensePlate = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz']) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    assert candidate(licensePlate = "f!@#o1b2a3r4",words = ['barfoot', 'aborfra', 'barform', 'barrofa', 'aborfar', 'barrage', 'baraffe', 'barfree']) == "barfoot"
    assert candidate(licensePlate = "bLUE cAR 2022",words = ['blueberry', 'blueprint', 'carbon', 'barcelona', 'bark']) == None
    assert candidate(licensePlate = "mN9mN",words = ['minnesota', 'miamin', 'manana', 'mimic', 'mimicry', 'mining', 'minimum']) == None
    assert candidate(licensePlate = "xyZ123 456",words = ['xyzxyz', 'zyxzyx', 'xyzzx', 'yxzxz', 'zxyzyx']) == "xyzzx"
    assert candidate(licensePlate = "!@#$%^&*()_+aBc123",words = ['abc', 'cba', 'bac', 'bca', 'cab', 'acb', 'aab', 'abb', 'bba', 'bbc', 'bcb', 'bacb', 'bcab', 'bacab', 'bacabc', 'bacabcd', 'bacabcde', 'bacabcdef', 'bacabcdefg']) == "abc"
    assert candidate(licensePlate = "abc def ghi",words = ['abcdefghi', 'defghibac', 'ghidefab', 'bacdefghi', 'abcdefghij']) == "abcdefghi"
    assert candidate(licensePlate = "a1b2c3d4e5",words = ['abcde', 'bcdea', 'cabde', 'decab', 'edcba', 'abcdde', 'abcdee', 'abcdeee', 'abcdeeee']) == "abcde"
    assert candidate(licensePlate = "Gh00t2!@#",words = ['ghostly', 'gnostic', 'ghost', 'tongue', 'tooth']) == "ghost"
    assert candidate(licensePlate = "m2i5n4i3s5",words = ['immisions', 'minimises', 'administs', 'ministers', 'misissues']) == "immisions"
    assert candidate(licensePlate = "!@#$%^&*()",words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf']) == "abcdef"
    assert candidate(licensePlate = "a2b3c4d5e6",words = ['alphabet', 'bacded', 'abacax', 'decalbac', 'abacbac']) == "bacded"
    assert candidate(licensePlate = "xyZ 123",words = ['xyzzy', 'zyxwvutsrqponmlkjihgfedcba', 'zyxzyxzyx', 'xyzz', 'zyx', 'xyzx', 'xyzxy', 'xyzxyz', 'xyzxyzz', 'xyzxyzxy']) == "zyx"
    assert candidate(licensePlate = "mno890",words = ['mno', 'mon', 'nom', 'omn', 'nmo', 'omnmo', 'mnomo', 'omonomn']) == "mno"
    assert candidate(licensePlate = "mno9PQR8",words = ['mnopqr', 'nopqmr', 'pqmrno', 'mnopq', 'pqmnopr', 'mnopqrq']) == "mnopqr"
    assert candidate(licensePlate = "1a2b3c4d5e",words = ['abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == "abcde"
    assert candidate(licensePlate = "aA bB cC",words = ['abc', 'abccba', 'cab', 'bcaac', 'acbac']) == "abccba"
    assert candidate(licensePlate = "zzz",words = ['zzzz', 'zzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == "zzz"
    assert candidate(licensePlate = "123abc ABC321",words = ['cba', 'abc', 'bac', 'bca', 'cab', 'acb', 'aab', 'abb', 'bba', 'bbc', 'bcb', 'bacb', 'bcab', 'bacab', 'bacabc', 'bacabcd', 'bacabcde', 'bacabcdef', 'bacabcdefg']) == "bacabc"
    assert candidate(licensePlate = "q9w8e7r6",words = ['qwerty', 'qwertas', 'qwertyui', 'qwertyuio', 'qwertyuiop']) == "qwerty"
    assert candidate(licensePlate = "qQwWeEr RtTyYuUiIoOpP",words = ['qwertyuiop', 'qwertyuio', 'qwertyuiopp', 'qwertyuioppq', 'qwertyuiopqq']) == None
    assert candidate(licensePlate = "xYz987",words = ['xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx', 'xxxyyzzz']) == "xyz"
    assert candidate(licensePlate = "XYZ 987",words = ['xyzz', 'zyxw', 'zyxv', 'zyxuv', 'zyxwvut']) == "xyzz"
    assert candidate(licensePlate = "P2l3l4o5",words = ['poll', 'pillar', 'pollock', 'polyope', 'plaster', 'polyope']) == "poll"


