def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sentences = ['short', 'tiny', 'minuscule']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['short', 'tiny', 'minuscule']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['alice and bob love leetcode', 'i think so too', 'this is great thanks very much']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['alice and bob love leetcode', 'i think so too', 'this is great thanks very much']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['singleword', 'two words', 'three words here']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['singleword', 'two words', 'three words here']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one two three four five six seven eight nine ten']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one two three four five six seven eight nine ten']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['please wait', 'continue to fight', 'continue to win']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['please wait', 'continue to fight', 'continue to win']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['hello world', 'hi there']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['hello world', 'hi there']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['singleword', 'another word', 'yet another example']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['singleword', 'another word', 'yet another example']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a quick brown fox', 'jumps over the lazy dog']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a quick brown fox', 'jumps over the lazy dog']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one two three', 'four five six seven', 'eight nine ten eleven twelve']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one two three', 'four five six seven', 'eight nine ten eleven twelve']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['longer sentences with more words to test the function', 'another sentence to check the word count correctly', 'yet another example sentence for validation', 'this is the last sentence for this test case']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['longer sentences with more words to test the function', 'another sentence to check the word count correctly', 'yet another example sentence for validation', 'this is the last sentence for this test case']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['word1', 'word1 word2', 'word1 word2 word3', 'word1 word2 word3 word4', 'word1 word2 word3 word4 word5']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['word1', 'word1 word2', 'word1 word2 word3', 'word1 word2 word3 word4', 'word1 word2 word3 word4 word5']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['all questions asked by five watched experts amaze the judge', 'jackdaws love my big sphinx of quartz', 'the five boxing wizards jump quickly on this new sentence']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['all questions asked by five watched experts amaze the judge', 'jackdaws love my big sphinx of quartz', 'the five boxing wizards jump quickly on this new sentence']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['tiny', 'shorter', 'shortest', 'a bit longer', 'the longest sentence in the list']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['tiny', 'shorter', 'shortest', 'a bit longer', 'the longest sentence in the list']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'this sentence is longer than the previous one', 'a']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'this sentence is longer than the previous one', 'a']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['once upon a time in a world far far away', 'there lived a king and a queen', 'who were very very happy together']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['once upon a time in a world far far away', 'there lived a king and a queen', 'who were very very happy together']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['singleword', 'two words', 'three words are', 'four words are here', 'five words are here now', 'six words are here now indeed', 'seven words are here now indeed truly']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['singleword', 'two words', 'three words are', 'four words are here', 'five words are here now', 'six words are here now indeed', 'seven words are here now indeed truly']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this sentence has twelve words in it indeed', 'this one has seven words']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this sentence has twelve words in it indeed', 'this one has seven words']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a short sentence', 'a much longer sentence with many more words in it', 'tiny', 'an even longer sentence that seems to go on and on and on']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a short sentence', 'a much longer sentence with many more words in it', 'tiny', 'an even longer sentence that seems to go on and on and on']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one two three', 'four five six seven', 'eight nine ten eleven twelve', 'thirteen fourteen fifteen sixteen seventeen']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one two three', 'four five six seven', 'eight nine ten eleven twelve', 'thirteen fourteen fifteen sixteen seventeen']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['equal number of words here', 'equal number of words here', 'equal number of words here']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['equal number of words here', 'equal number of words here', 'equal number of words here']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this is a single word', 'this is a two word phrase', 'this sentence has three words in it']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this is a single word', 'this is a two word phrase', 'this sentence has three words in it']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one two three', 'four five six seven eight', 'nine ten eleven twelve thirteen fourteen fifteen']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one two three', 'four five six seven eight', 'nine ten eleven twelve thirteen fourteen fifteen']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'this is a sentence with many many many words indeed']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'this is a sentence with many many many words indeed']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this is a test sentence with exactly ten words in it', 'another test sentence here with ten words too', 'and yet another test sentence that has ten words']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this is a test sentence with exactly ten words in it', 'another test sentence here with ten words too', 'and yet another test sentence that has ten words']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['singleword', 'anotherword', 'yetanotherword', 'onemoreword']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['singleword', 'anotherword', 'yetanotherword', 'onemoreword']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['python is fun', 'data structures and algorithms', 'object oriented programming is powerful']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['python is fun', 'data structures and algorithms', 'object oriented programming is powerful']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this is a test', 'another test sentence', 'yet another example to consider', 'the longest sentence in this batch is this one here']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this is a test', 'another test sentence', 'yet another example to consider', 'the longest sentence in this batch is this one here']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'pack my box with five dozen liquor jugs']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'pack my box with five dozen liquor jugs']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['abcd efgh ijkl mnop qrst uvwx yz', 'abcd efgh ijkl mnop qrst uvwx yz abcd', 'abcd efgh ijkl mnop qrst uvwx yz abcd efgh', 'abcd efgh ijkl mnop qrst uvwx yz abcd efgh ijkl mnop']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['abcd efgh ijkl mnop qrst uvwx yz', 'abcd efgh ijkl mnop qrst uvwx yz abcd', 'abcd efgh ijkl mnop qrst uvwx yz abcd efgh', 'abcd efgh ijkl mnop qrst uvwx yz abcd efgh ijkl mnop']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'every good boy does fine', 'to be or not to be that is the question']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'every good boy does fine', 'to be or not to be that is the question']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'the rain in spain stays mainly in the plain', 'i am six']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'the rain in spain stays mainly in the plain', 'i am six']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y', 'a b c d e f g h i j k l m n o p q r s t u v w x']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y', 'a b c d e f g h i j k l m n o p q r s t u v w x']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['lorem ipsum dolor sit amet consectetur adipiscing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 'ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat']) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['lorem ipsum dolor sit amet consectetur adipiscing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 'ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat']) == 17: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['words words words words words words words words words words', 'just a couple', 'quite a bit more words than before']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['words words words words words words words words words words', 'just a couple', 'quite a bit more words than before']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['Python is an interpreted high-level general-purpose programming language', 'Java is a class-based, object-oriented programming language', 'C++ is a general-purpose programming language']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['Python is an interpreted high-level general-purpose programming language', 'Java is a class-based, object-oriented programming language', 'C++ is a general-purpose programming language']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the best way to achieve success is through hard work', 'persistence is key to overcoming challenges', 'never give up on your dreams']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the best way to achieve success is through hard work', 'persistence is key to overcoming challenges', 'never give up on your dreams']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'quick fox jumps', 'lazy dog']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'quick fox jumps', 'lazy dog']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one', 'two words', 'three words here', 'four words here now', 'five words here now indeed', 'six words here now indeed truly']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one', 'two words', 'three words here', 'four words here now', 'five words here now indeed', 'six words here now indeed truly']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'every good boy does fine', 'pack my box with five dozen liquor jugs']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'every good boy does fine', 'pack my box with five dozen liquor jugs']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'short sentence']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'short sentence']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one', 'two three', 'four five six', 'seven eight nine ten', 'eleven twelve thirteen fourteen fifteen']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one', 'two three', 'four five six', 'seven eight nine ten', 'eleven twelve thirteen fourteen fifteen']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'pack my box with five dozen liquor jugs', 'how vexingly quick daft zebras jump']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'pack my box with five dozen liquor jugs', 'how vexingly quick daft zebras jump']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat', 'different repeat different repeat', 'unique sentence']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat', 'different repeat different repeat', 'unique sentence']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a quick brown fox jumps over the lazy dog', 'this is a longer sentence with more words in it', 'short']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a quick brown fox jumps over the lazy dog', 'this is a longer sentence with more words in it', 'short']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['equal length words here', 'equal length words here', 'equal length words here']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['equal length words here', 'equal length words here', 'equal length words here']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one two three four five', 'six seven eight nine ten eleven', 'twelve thirteen fourteen fifteen sixteen seventeen', 'eighteen nineteen twenty']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one two three four five', 'six seven eight nine ten eleven', 'twelve thirteen fourteen fifteen sixteen seventeen', 'eighteen nineteen twenty']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['equal length', 'equal length', 'equal length', 'equal length', 'equal length', 'equal length']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['equal length', 'equal length', 'equal length', 'equal length', 'equal length', 'equal length']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['lorem ipsum dolor sit amet', 'consectetur adipiscing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['lorem ipsum dolor sit amet', 'consectetur adipiscing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'a quick movement of the enemy will jeopardize six gunboats', 'five boxing wizards jump quickly']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'a quick movement of the enemy will jeopardize six gunboats', 'five boxing wizards jump quickly']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['an apple a day keeps the doctor away', 'once upon a time in a land far far away', 'hello world hello universe']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['an apple a day keeps the doctor away', 'once upon a time in a land far far away', 'hello world hello universe']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the longest sentence in this list is the last one which contains many many words indeed']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the longest sentence in this list is the last one which contains many many words indeed']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'how now brown cow', 'she sells sea shells by the sea shore']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'how now brown cow', 'she sells sea shells by the sea shore']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'jumps over the lazy dog']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'jumps over the lazy dog']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['the secret to a happy life is simple', 'be kind to others', 'live each day to the fullest', 'love what you do']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['the secret to a happy life is simple', 'be kind to others', 'live each day to the fullest', 'love what you do']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'i am a sentence with many words indeed', 'this is another test sentence']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'i am a sentence with many words indeed', 'this is another test sentence']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['abc', 'def ghi jkl', 'mno pqr stu vwx yz', 'a b c d e f g h i j k l m n o p q r s t u v w x y z']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['abc', 'def ghi jkl', 'mno pqr stu vwx yz', 'a b c d e f g h i j k l m n o p q r s t u v w x y z']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['python is a great programming language', 'java is also a great programming language', 'c plus plus is another popular language']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['python is a great programming language', 'java is also a great programming language', 'c plus plus is another popular language']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['singleword', 'two words', 'three words here', 'four words are in this', 'five words make a phrase', 'six words is a complete sentence']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['singleword', 'two words', 'three words here', 'four words are in this', 'five words make a phrase', 'six words is a complete sentence']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['longer sentences are more challenging to process correctly', 'even longer sentences that contain a greater number of words for testing', 'tiny']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['longer sentences are more challenging to process correctly', 'even longer sentences that contain a greater number of words for testing', 'tiny']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['to be or not to be that is the question', 'that is the question indeed', 'whether tis nobler in the mind to suffer']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['to be or not to be that is the question', 'that is the question indeed', 'whether tis nobler in the mind to suffer']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['python is great', 'i love programming', 'data science is fascinating', 'machine learning and ai are transforming industries']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['python is great', 'i love programming', 'data science is fascinating', 'machine learning and ai are transforming industries']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this is a very long sentence indeed that should test the boundaries of the problem constraints']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this is a very long sentence indeed that should test the boundaries of the problem constraints']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['singleword', 'two words', 'three words here', 'four words make a sentence', 'five words in this sentence']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['singleword', 'two words', 'three words here', 'four words make a sentence', 'five words in this sentence']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['complex sentences are interesting', 'they can have many clauses and ideas', 'and sometimes they even have subordinate clauses']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['complex sentences are interesting', 'they can have many clauses and ideas', 'and sometimes they even have subordinate clauses']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['very very very long sentence to test the length', 'short sentence', 'another medium length sentence here']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['very very very long sentence to test the length', 'short sentence', 'another medium length sentence here']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['very long sentence with many many many words indeed', 'short one', 'medium length sentence']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['very long sentence with many many many words indeed', 'short one', 'medium length sentence']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a singleword', 'two words here', 'three words in this', 'four words make up']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a singleword', 'two words here', 'three words in this', 'four words make up']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this is a sentence with seven words', 'another one with five words', 'and yet another with eight words here']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this is a sentence with seven words', 'another one with five words', 'and yet another with eight words here']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'the cat in the hat']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'the cat in the hat']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['this is a longer sentence with more words', 'tiny', 'another sentence with quite a few words indeed']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['this is a longer sentence with more words', 'tiny', 'another sentence with quite a few words indeed']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['python is an amazing language for data science and machine learning', 'the early morning sun illuminated the dew covered grass', 'she sells sea shells by the sea shore']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['python is an amazing language for data science and machine learning', 'the early morning sun illuminated the dew covered grass', 'she sells sea shells by the sea shore']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['same same same same same same same', 'another same same same', 'and yet another same same']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['same same same same same same same', 'another same same same', 'and yet another same same']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sentences = ['one', 'two three', 'four five six', 'seven eight nine ten']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentences = ['one', 'two three', 'four five six', 'seven eight nine ten']) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sentences = ['short', 'tiny', 'minuscule']) == 1
    assert candidate(sentences = ['one']) == 1
    assert candidate(sentences = ['alice and bob love leetcode', 'i think so too', 'this is great thanks very much']) == 6
    assert candidate(sentences = ['singleword', 'two words', 'three words here']) == 3
    assert candidate(sentences = ['one two three four five six seven eight nine ten']) == 10
    assert candidate(sentences = ['please wait', 'continue to fight', 'continue to win']) == 3
    assert candidate(sentences = ['hello world', 'hi there']) == 2
    assert candidate(sentences = ['singleword', 'another word', 'yet another example']) == 3
    assert candidate(sentences = ['a quick brown fox', 'jumps over the lazy dog']) == 5
    assert candidate(sentences = ['one two three', 'four five six seven', 'eight nine ten eleven twelve']) == 5
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z']) == 26
    assert candidate(sentences = ['longer sentences with more words to test the function', 'another sentence to check the word count correctly', 'yet another example sentence for validation', 'this is the last sentence for this test case']) == 9
    assert candidate(sentences = ['equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal', 'equal']) == 1
    assert candidate(sentences = ['word1', 'word1 word2', 'word1 word2 word3', 'word1 word2 word3 word4', 'word1 word2 word3 word4 word5']) == 5
    assert candidate(sentences = ['all questions asked by five watched experts amaze the judge', 'jackdaws love my big sphinx of quartz', 'the five boxing wizards jump quickly on this new sentence']) == 10
    assert candidate(sentences = ['tiny', 'shorter', 'shortest', 'a bit longer', 'the longest sentence in the list']) == 6
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'this sentence is longer than the previous one', 'a']) == 9
    assert candidate(sentences = ['once upon a time in a world far far away', 'there lived a king and a queen', 'who were very very happy together']) == 10
    assert candidate(sentences = ['singleword', 'two words', 'three words are', 'four words are here', 'five words are here now', 'six words are here now indeed', 'seven words are here now indeed truly']) == 7
    assert candidate(sentences = ['this sentence has twelve words in it indeed', 'this one has seven words']) == 8
    assert candidate(sentences = ['a short sentence', 'a much longer sentence with many more words in it', 'tiny', 'an even longer sentence that seems to go on and on and on']) == 13
    assert candidate(sentences = ['one two three', 'four five six seven', 'eight nine ten eleven twelve', 'thirteen fourteen fifteen sixteen seventeen']) == 5
    assert candidate(sentences = ['equal number of words here', 'equal number of words here', 'equal number of words here']) == 5
    assert candidate(sentences = ['this is a single word', 'this is a two word phrase', 'this sentence has three words in it']) == 7
    assert candidate(sentences = ['one two three', 'four five six seven eight', 'nine ten eleven twelve thirteen fourteen fifteen']) == 7
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'this is a sentence with many many many words indeed']) == 26
    assert candidate(sentences = ['this is a test sentence with exactly ten words in it', 'another test sentence here with ten words too', 'and yet another test sentence that has ten words']) == 11
    assert candidate(sentences = ['singleword', 'anotherword', 'yetanotherword', 'onemoreword']) == 1
    assert candidate(sentences = ['python is fun', 'data structures and algorithms', 'object oriented programming is powerful']) == 5
    assert candidate(sentences = ['this is a test', 'another test sentence', 'yet another example to consider', 'the longest sentence in this batch is this one here']) == 10
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'pack my box with five dozen liquor jugs']) == 9
    assert candidate(sentences = ['abcd efgh ijkl mnop qrst uvwx yz', 'abcd efgh ijkl mnop qrst uvwx yz abcd', 'abcd efgh ijkl mnop qrst uvwx yz abcd efgh', 'abcd efgh ijkl mnop qrst uvwx yz abcd efgh ijkl mnop']) == 11
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'every good boy does fine', 'to be or not to be that is the question']) == 10
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'the rain in spain stays mainly in the plain', 'i am six']) == 26
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y', 'a b c d e f g h i j k l m n o p q r s t u v w x']) == 26
    assert candidate(sentences = ['lorem ipsum dolor sit amet consectetur adipiscing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 'ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat']) == 17
    assert candidate(sentences = ['words words words words words words words words words words', 'just a couple', 'quite a bit more words than before']) == 10
    assert candidate(sentences = ['Python is an interpreted high-level general-purpose programming language', 'Java is a class-based, object-oriented programming language', 'C++ is a general-purpose programming language']) == 8
    assert candidate(sentences = ['the best way to achieve success is through hard work', 'persistence is key to overcoming challenges', 'never give up on your dreams']) == 10
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'quick fox jumps', 'lazy dog']) == 26
    assert candidate(sentences = ['one', 'two words', 'three words here', 'four words here now', 'five words here now indeed', 'six words here now indeed truly']) == 6
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'every good boy does fine', 'pack my box with five dozen liquor jugs']) == 9
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'short sentence']) == 26
    assert candidate(sentences = ['one', 'two three', 'four five six', 'seven eight nine ten', 'eleven twelve thirteen fourteen fifteen']) == 5
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'pack my box with five dozen liquor jugs', 'how vexingly quick daft zebras jump']) == 9
    assert candidate(sentences = ['repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat', 'different repeat different repeat', 'unique sentence']) == 10
    assert candidate(sentences = ['a quick brown fox jumps over the lazy dog', 'this is a longer sentence with more words in it', 'short']) == 10
    assert candidate(sentences = ['equal length words here', 'equal length words here', 'equal length words here']) == 4
    assert candidate(sentences = ['one two three four five', 'six seven eight nine ten eleven', 'twelve thirteen fourteen fifteen sixteen seventeen', 'eighteen nineteen twenty']) == 6
    assert candidate(sentences = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl']) == 1
    assert candidate(sentences = ['equal length', 'equal length', 'equal length', 'equal length', 'equal length', 'equal length']) == 2
    assert candidate(sentences = ['lorem ipsum dolor sit amet', 'consectetur adipiscing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua']) == 11
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'a quick movement of the enemy will jeopardize six gunboats', 'five boxing wizards jump quickly']) == 10
    assert candidate(sentences = ['an apple a day keeps the doctor away', 'once upon a time in a land far far away', 'hello world hello universe']) == 10
    assert candidate(sentences = ['the longest sentence in this list is the last one which contains many many words indeed']) == 16
    assert candidate(sentences = ['the quick brown fox jumps over the lazy dog', 'how now brown cow', 'she sells sea shells by the sea shore']) == 9
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'jumps over the lazy dog']) == 26
    assert candidate(sentences = ['the secret to a happy life is simple', 'be kind to others', 'live each day to the fullest', 'love what you do']) == 8
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'i am a sentence with many words indeed', 'this is another test sentence']) == 26
    assert candidate(sentences = ['abc', 'def ghi jkl', 'mno pqr stu vwx yz', 'a b c d e f g h i j k l m n o p q r s t u v w x y z']) == 26
    assert candidate(sentences = ['python is a great programming language', 'java is also a great programming language', 'c plus plus is another popular language']) == 7
    assert candidate(sentences = ['singleword', 'two words', 'three words here', 'four words are in this', 'five words make a phrase', 'six words is a complete sentence']) == 6
    assert candidate(sentences = ['longer sentences are more challenging to process correctly', 'even longer sentences that contain a greater number of words for testing', 'tiny']) == 12
    assert candidate(sentences = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 1
    assert candidate(sentences = ['to be or not to be that is the question', 'that is the question indeed', 'whether tis nobler in the mind to suffer']) == 10
    assert candidate(sentences = ['python is great', 'i love programming', 'data science is fascinating', 'machine learning and ai are transforming industries']) == 7
    assert candidate(sentences = ['this is a very long sentence indeed that should test the boundaries of the problem constraints']) == 16
    assert candidate(sentences = ['singleword', 'two words', 'three words here', 'four words make a sentence', 'five words in this sentence']) == 5
    assert candidate(sentences = ['complex sentences are interesting', 'they can have many clauses and ideas', 'and sometimes they even have subordinate clauses']) == 7
    assert candidate(sentences = ['very very very long sentence to test the length', 'short sentence', 'another medium length sentence here']) == 9
    assert candidate(sentences = ['very long sentence with many many many words indeed', 'short one', 'medium length sentence']) == 9
    assert candidate(sentences = ['a singleword', 'two words here', 'three words in this', 'four words make up']) == 4
    assert candidate(sentences = ['this is a sentence with seven words', 'another one with five words', 'and yet another with eight words here']) == 7
    assert candidate(sentences = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'the cat in the hat']) == 26
    assert candidate(sentences = ['this is a longer sentence with more words', 'tiny', 'another sentence with quite a few words indeed']) == 8
    assert candidate(sentences = ['python is an amazing language for data science and machine learning', 'the early morning sun illuminated the dew covered grass', 'she sells sea shells by the sea shore']) == 11
    assert candidate(sentences = ['same same same same same same same', 'another same same same', 'and yet another same same']) == 7
    assert candidate(sentences = ['one', 'two three', 'four five six', 'seven eight nine ten']) == 4


