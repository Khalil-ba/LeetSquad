def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "hello world hello hello world",first = "hello",second = "world") == ['hello']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "hello world hello hello world",first = "hello",second = "world") == ['hello']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat']: {e}')
    
    total += 1
    try:
        result = candidate(text = "look at the stars look at the moon",first = "look",second = "at") == ['the', 'the']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "look at the stars look at the moon",first = "look",second = "at") == ['the', 'the']: {e}')
    
    total += 1
    try:
        result = candidate(text = "in the beginning there was the word",first = "the",second = "beginning") == ['there']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "in the beginning there was the word",first = "the",second = "beginning") == ['there']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a test this is only a test",first = "this",second = "is") == ['a', 'only']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a test this is only a test",first = "this",second = "is") == ['a', 'only']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one two three two three four three five",first = "two",second = "three") == ['two', 'four']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one two three two three four three five",first = "two",second = "three") == ['two', 'four']: {e}')
    
    total += 1
    try:
        result = candidate(text = "every good boy does fine every good boy does fine",first = "good",second = "boy") == ['does', 'does']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "every good boy does fine every good boy does fine",first = "good",second = "boy") == ['does', 'does']: {e}')
    
    total += 1
    try:
        result = candidate(text = "alice is a good girl she is a good student",first = "a",second = "good") == ['girl', 'student']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "alice is a good girl she is a good student",first = "a",second = "good") == ['girl', 'student']: {e}')
    
    total += 1
    try:
        result = candidate(text = "we will we will rock you",first = "we",second = "will") == ['we', 'rock']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "we will we will rock you",first = "we",second = "will") == ['we', 'rock']: {e}')
    
    total += 1
    try:
        result = candidate(text = "foo bar foo bar foo",first = "foo",second = "bar") == ['foo', 'foo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "foo bar foo bar foo",first = "foo",second = "bar") == ['foo', 'foo']: {e}')
    
    total += 1
    try:
        result = candidate(text = "in a village of la mancha the name of which i have no desire to call to mind",first = "village",second = "of") == ['la']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "in a village of la mancha the name of which i have no desire to call to mind",first = "village",second = "of") == ['la']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a test this is only a test",first = "is",second = "a") == ['test']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a test this is only a test",first = "is",second = "a") == ['test']: {e}')
    
    total += 1
    try:
        result = candidate(text = "foo bar foo foo bar bar foo",first = "foo",second = "bar") == ['foo', 'bar']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "foo bar foo foo bar bar foo",first = "foo",second = "bar") == ['foo', 'bar']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog",first = "the",second = "lazy") == ['dog']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog",first = "the",second = "lazy") == ['dog']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog",first = "quick",second = "brown") == ['fox', 'fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog",first = "quick",second = "brown") == ['fox', 'fox']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeat repeat repeat repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeat repeat repeat repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one two three four five six seven eight nine ten eleven twelve",first = "five",second = "six") == ['seven']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one two three four five six seven eight nine ten eleven twelve",first = "five",second = "six") == ['seven']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox",first = "quick",second = "brown") == ['fox', 'fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox",first = "quick",second = "brown") == ['fox', 'fox']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a tale of two cities a tale of two brothers a tale of two sisters",first = "tale",second = "of") == ['two', 'two', 'two']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a tale of two cities a tale of two brothers a tale of two sisters",first = "tale",second = "of") == ['two', 'two', 'two']: {e}')
    
    total += 1
    try:
        result = candidate(text = "once upon a time in a land far far away once upon a time in a magical land",first = "once",second = "upon") == ['a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "once upon a time in a land far far away once upon a time in a magical land",first = "once",second = "upon") == ['a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple test this is a more complex test this is a simple test",first = "is",second = "a") == ['simple', 'more', 'simple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple test this is a more complex test this is a simple test",first = "is",second = "a") == ['simple', 'more', 'simple']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the rain in spain stays mainly in the plain the rain in spain",first = "rain",second = "in") == ['spain', 'spain']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the rain in spain stays mainly in the plain the rain in spain",first = "rain",second = "in") == ['spain', 'spain']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one fish two fish red fish blue fish one fish two fish red fish blue fish",first = "fish",second = "red") == ['fish', 'fish']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one fish two fish red fish blue fish one fish two fish red fish blue fish",first = "fish",second = "red") == ['fish', 'fish']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one two three four five six seven eight nine ten one two three four five six",first = "three",second = "four") == ['five', 'five']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one two three four five six seven eight nine ten one two three four five six",first = "three",second = "four") == ['five', 'five']: {e}')
    
    total += 1
    try:
        result = candidate(text = "x y z x y z x y z x y z x y z x y z x y z x y z",first = "x",second = "y") == ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "x y z x y z x y z x y z x y z x y z x y z x y z",first = "x",second = "y") == ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple sentence to test the function this is a simple test",first = "simple",second = "sentence") == ['to']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple sentence to test the function this is a simple test",first = "simple",second = "sentence") == ['to']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a a a a a a a a a a a a a a a a a a a a a",first = "a",second = "a") == ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a a a a a a a a a a a a a a a a a a a a a",first = "a",second = "a") == ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "once upon a time in a land far far away once upon a time",first = "once",second = "upon") == ['a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "once upon a time in a land far far away once upon a time",first = "once",second = "upon") == ['a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeated repeated repeated repeated repeated repeated",first = "repeated",second = "repeated") == ['repeated', 'repeated', 'repeated', 'repeated']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeated repeated repeated repeated repeated repeated",first = "repeated",second = "repeated") == ['repeated', 'repeated', 'repeated', 'repeated']: {e}')
    
    total += 1
    try:
        result = candidate(text = "abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl mno",first = "def",second = "ghi") == ['jkl', 'jkl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl mno",first = "def",second = "ghi") == ['jkl', 'jkl']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d",first = "a",second = "b") == ['c', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d",first = "a",second = "b") == ['c', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple test case this is a very simple test case",first = "is",second = "a") == ['simple', 'very']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple test case this is a very simple test case",first = "is",second = "a") == ['simple', 'very']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps",first = "quick",second = "brown") == ['fox', 'fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps",first = "quick",second = "brown") == ['fox', 'fox']: {e}')
    
    total += 1
    try:
        result = candidate(text = "once upon a time in a land far far away once upon a time in a land",first = "once",second = "upon") == ['a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "once upon a time in a land far far away once upon a time in a land",first = "once",second = "upon") == ['a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "find these occurrences carefully find these occurrences again find these occurrences one more time",first = "find",second = "these") == ['occurrences', 'occurrences', 'occurrences']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "find these occurrences carefully find these occurrences again find these occurrences one more time",first = "find",second = "these") == ['occurrences', 'occurrences', 'occurrences']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick and silent movement of the enemy will jeopardize five gunboats",first = "quick",second = "and") == ['silent']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick and silent movement of the enemy will jeopardize five gunboats",first = "quick",second = "and") == ['silent']: {e}')
    
    total += 1
    try:
        result = candidate(text = "complex example with multiple matches and no matches complex example with multiple matches and no matches",first = "with",second = "multiple") == ['matches', 'matches']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "complex example with multiple matches and no matches complex example with multiple matches and no matches",first = "with",second = "multiple") == ['matches', 'matches']: {e}')
    
    total += 1
    try:
        result = candidate(text = "she sells sea shells by the sea shore she sells sea shells by the sea shore",first = "sea",second = "shells") == ['by', 'by']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "she sells sea shells by the sea shore she sells sea shells by the sea shore",first = "sea",second = "shells") == ['by', 'by']: {e}')
    
    total += 1
    try:
        result = candidate(text = "complex scenario with different words complex scenario with different words complex",first = "with",second = "different") == ['words', 'words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "complex scenario with different words complex scenario with different words complex",first = "with",second = "different") == ['words', 'words']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeated repeated repeated words words words in a sentence",first = "words",second = "in") == ['a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeated repeated repeated words words words in a sentence",first = "words",second = "in") == ['a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "unique words with no repetitions should return empty list",first = "no",second = "repetitions") == ['should']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "unique words with no repetitions should return empty list",first = "no",second = "repetitions") == ['should']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the quick brown fox",first = "quick",second = "brown") == ['fox', 'fox', 'fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the quick brown fox",first = "quick",second = "brown") == ['fox', 'fox', 'fox']: {e}')
    
    total += 1
    try:
        result = candidate(text = "x y z a b c x y z a b c x y z a b c x y z a b c",first = "x",second = "y") == ['z', 'z', 'z', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "x y z a b c x y z a b c x y z a b c x y z a b c",first = "x",second = "y") == ['z', 'z', 'z', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(text = "word word word word word word word word word word word word word word word word word word word word",first = "word",second = "word") == ['word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "word word word word word word word word word word word word word word word word word word word word",first = "word",second = "word") == ['word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(text = "edge case where the last word is the second",first = "second",second = "word") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "edge case where the last word is the second",first = "second",second = "word") == []: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "f",second = "g") == ['h', 'h']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "f",second = "g") == ['h', 'h']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the cat sat on the mat the dog sat on the log the cat sat on the mat the dog sat on the log",first = "sat",second = "on") == ['the', 'the', 'the', 'the']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the cat sat on the mat the dog sat on the log the cat sat on the mat the dog sat on the log",first = "sat",second = "on") == ['the', 'the', 'the', 'the']: {e}')
    
    total += 1
    try:
        result = candidate(text = "hello there hello there hello there hello there hello there",first = "hello",second = "there") == ['hello', 'hello', 'hello', 'hello']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "hello there hello there hello there hello there hello there",first = "hello",second = "there") == ['hello', 'hello', 'hello', 'hello']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one fish two fish red fish blue fish one fish two fish red fish blue fish",first = "two",second = "fish") == ['red', 'red']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one fish two fish red fish blue fish one fish two fish red fish blue fish",first = "two",second = "fish") == ['red', 'red']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeat after me repeat after me repeat after me repeat after me",first = "repeat",second = "after") == ['me', 'me', 'me', 'me']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeat after me repeat after me repeat after me repeat after me",first = "repeat",second = "after") == ['me', 'me', 'me', 'me']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one two three four five six seven eight nine ten eleven twelve",first = "three",second = "four") == ['five']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one two three four five six seven eight nine ten eleven twelve",first = "three",second = "four") == ['five']: {e}')
    
    total += 1
    try:
        result = candidate(text = "in the heart of the night the old owl hooted and the stars twinkled in the dark",first = "the",second = "old") == ['owl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "in the heart of the night the old owl hooted and the stars twinkled in the dark",first = "the",second = "old") == ['owl']: {e}')
    
    total += 1
    try:
        result = candidate(text = "finding the third word after first second finding the third word after first",first = "finding",second = "the") == ['third', 'third']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "finding the third word after first second finding the third word after first",first = "finding",second = "the") == ['third', 'third']: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabra abracadabra abracadabra abracadabra abracadabra",first = "abracadabra",second = "abracadabra") == ['abracadabra', 'abracadabra', 'abracadabra']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabra abracadabra abracadabra abracadabra abracadabra",first = "abracadabra",second = "abracadabra") == ['abracadabra', 'abracadabra', 'abracadabra']: {e}')
    
    total += 1
    try:
        result = candidate(text = "find the pattern in this text pattern in this text pattern in this text pattern",first = "pattern",second = "in") == ['this', 'this', 'this']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "find the pattern in this text pattern in this text pattern in this text pattern",first = "pattern",second = "in") == ['this', 'this', 'this']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a longer sentence with a variety of words and phrases to test the function properly",first = "variety",second = "of") == ['words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a longer sentence with a variety of words and phrases to test the function properly",first = "variety",second = "of") == ['words']: {e}')
    
    total += 1
    try:
        result = candidate(text = "she sells sea shells by the sea shore and the shells she sells are sea shells",first = "sea",second = "shells") == ['by']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "she sells sea shells by the sea shore and the shells she sells are sea shells",first = "sea",second = "shells") == ['by']: {e}')
    
    total += 1
    try:
        result = candidate(text = "example of a longer sentence where the pattern can be found multiple times example of a longer",first = "example",second = "of") == ['a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "example of a longer sentence where the pattern can be found multiple times example of a longer",first = "example",second = "of") == ['a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "multiple words in sequence are repeated multiple times multiple words in sequence",first = "multiple",second = "words") == ['in', 'in']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "multiple words in sequence are repeated multiple times multiple words in sequence",first = "multiple",second = "words") == ['in', 'in']: {e}')
    
    total += 1
    try:
        result = candidate(text = "abc def ghi jkl mno pqr stu vwx yza abc def ghi jkl mno pqr stu vwx yza",first = "ghi",second = "jkl") == ['mno', 'mno']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abc def ghi jkl mno pqr stu vwx yza abc def ghi jkl mno pqr stu vwx yza",first = "ghi",second = "jkl") == ['mno', 'mno']: {e}')
    
    total += 1
    try:
        result = candidate(text = "abc abc abc abc abc abc abc abc abc abc",first = "abc",second = "abc") == ['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abc abc abc abc abc abc abc abc abc abc",first = "abc",second = "abc") == ['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a quick movement of the enemy will jeopardize five gunboats a quick movement of the army will jeopardize five gunboats",first = "quick",second = "movement") == ['of', 'of']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a quick movement of the enemy will jeopardize five gunboats a quick movement of the army will jeopardize five gunboats",first = "quick",second = "movement") == ['of', 'of']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick movement of the enemy will jeopardize five gunboats",first = "quick",second = "movement") == ['of', 'of']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick movement of the enemy will jeopardize five gunboats",first = "quick",second = "movement") == ['of', 'of']: {e}')
    
    total += 1
    try:
        result = candidate(text = "complex pattern with complex pattern and another complex pattern",first = "complex",second = "pattern") == ['with', 'and']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "complex pattern with complex pattern and another complex pattern",first = "complex",second = "pattern") == ['with', 'and']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple test to see if the function works correctly with multiple occurrences of first second third",first = "first",second = "second") == ['third']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple test to see if the function works correctly with multiple occurrences of first second third",first = "first",second = "second") == ['third']: {e}')
    
    total += 1
    try:
        result = candidate(text = "once upon a time in a galaxy far far away once upon a time in a galaxy",first = "once",second = "upon") == ['a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "once upon a time in a galaxy far far away once upon a time in a galaxy",first = "once",second = "upon") == ['a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "cycling in the mountains mountains are beautiful cycling in the mountains",first = "cycling",second = "in") == ['the', 'the']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "cycling in the mountains mountains are beautiful cycling in the mountains",first = "cycling",second = "in") == ['the', 'the']: {e}')
    
    total += 1
    try:
        result = candidate(text = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty",first = "one",second = "two") == ['three']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty",first = "one",second = "two") == ['three']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple sentence with multiple occurrences of the same word word",first = "the",second = "same") == ['word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple sentence with multiple occurrences of the same word word",first = "the",second = "same") == ['word']: {e}')
    
    total += 1
    try:
        result = candidate(text = "if you are reading this text then you are doing a great job reading",first = "reading",second = "this") == ['text']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "if you are reading this text then you are doing a great job reading",first = "reading",second = "this") == ['text']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple test case with multiple matches this is a simple test",first = "this",second = "is") == ['a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple test case with multiple matches this is a simple test",first = "this",second = "is") == ['a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "to be or not to be that is the question to be or not to be that is the question",first = "be",second = "or") == ['not', 'not']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "to be or not to be that is the question to be or not to be that is the question",first = "be",second = "or") == ['not', 'not']: {e}')
    
    total += 1
    try:
        result = candidate(text = "in the heart of the city in the heart of the heart in the heart of the city",first = "heart",second = "of") == ['the', 'the', 'the']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "in the heart of the city in the heart of the heart in the heart of the city",first = "heart",second = "of") == ['the', 'the', 'the']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the lazy dog jumps over the quick brown fox",first = "the",second = "lazy") == ['dog', 'dog']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the lazy dog jumps over the quick brown fox",first = "the",second = "lazy") == ['dog', 'dog']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a simple test this is a simple test this is a simple test",first = "is",second = "a") == ['simple', 'simple', 'simple']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a simple test this is a simple test this is a simple test",first = "is",second = "a") == ['simple', 'simple', 'simple']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c",first = "a",second = "b") == ['c', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c",first = "a",second = "b") == ['c', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(text = "last two words do not match first second",first = "first",second = "second") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "last two words do not match first second",first = "first",second = "second") == []: {e}')
    
    total += 1
    try:
        result = candidate(text = "every good boy does fine every good boy does fine every good boy does fine",first = "good",second = "boy") == ['does', 'does', 'does']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "every good boy does fine every good boy does fine every good boy does fine",first = "good",second = "boy") == ['does', 'does', 'does']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog again",first = "quick",second = "brown") == ['fox', 'fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog again",first = "quick",second = "brown") == ['fox', 'fox']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeat repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat', 'repeat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeat repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat', 'repeat']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "x",second = "y") == ['z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "x",second = "y") == ['z']: {e}')
    
    total += 1
    try:
        result = candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox is quick",first = "quick",second = "brown") == ['fox', 'fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox is quick",first = "quick",second = "brown") == ['fox', 'fox']: {e}')
    
    total += 1
    try:
        result = candidate(text = "cycling through the words cycling through the words cycling",first = "through",second = "the") == ['words', 'words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "cycling through the words cycling through the words cycling",first = "through",second = "the") == ['words', 'words']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a b c a b c a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "b",second = "c") == ['a', 'a', 'd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a b c a b c a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "b",second = "c") == ['a', 'a', 'd']: {e}')
    
    total += 1
    try:
        result = candidate(text = "she sells sea shells by the sea shore she sells sea shells",first = "sea",second = "shells") == ['by']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "she sells sea shells by the sea shore she sells sea shells",first = "sea",second = "shells") == ['by']: {e}')
    
    total += 1
    try:
        result = candidate(text = "hello world hello world hello world hello world hello world hello world",first = "hello",second = "world") == ['hello', 'hello', 'hello', 'hello', 'hello']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "hello world hello world hello world hello world hello world hello world",first = "hello",second = "world") == ['hello', 'hello', 'hello', 'hello', 'hello']: {e}')
    
    total += 1
    try:
        result = candidate(text = "consecutive consecutive words words words words in this sequence sequence",first = "words",second = "words") == ['words', 'words', 'in']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "consecutive consecutive words words words words in this sequence sequence",first = "words",second = "words") == ['words', 'words', 'in']: {e}')
    
    total += 1
    try:
        result = candidate(text = "complex sentence with multiple occurrences of first second third first second third",first = "first",second = "second") == ['third', 'third']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "complex sentence with multiple occurrences of first second third first second third",first = "first",second = "second") == ['third', 'third']: {e}')
    
    total += 1
    try:
        result = candidate(text = "every good boy does fine every good boy does fine every good boy does fine",first = "every",second = "good") == ['boy', 'boy', 'boy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "every good boy does fine every good boy does fine every good boy does fine",first = "every",second = "good") == ['boy', 'boy', 'boy']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a test this is only a test this is a test this is a test",first = "this",second = "is") == ['a', 'only', 'a', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a test this is only a test this is a test this is a test",first = "this",second = "is") == ['a', 'only', 'a', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat']: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeated repeated repeated repeated repeated repeated repeated repeated",first = "repeated",second = "repeated") == ['repeated', 'repeated', 'repeated', 'repeated', 'repeated', 'repeated']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeated repeated repeated repeated repeated repeated repeated repeated",first = "repeated",second = "repeated") == ['repeated', 'repeated', 'repeated', 'repeated', 'repeated', 'repeated']: {e}')
    
    total += 1
    try:
        result = candidate(text = "aa bb aa bb aa bb aa bb aa bb aa bb",first = "aa",second = "bb") == ['aa', 'aa', 'aa', 'aa', 'aa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aa bb aa bb aa bb aa bb aa bb aa bb",first = "aa",second = "bb") == ['aa', 'aa', 'aa', 'aa', 'aa']: {e}')
    
    total += 1
    try:
        result = candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick movement of the enemy will jeopardize six gunboats",first = "movement",second = "of") == ['the', 'the']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick movement of the enemy will jeopardize six gunboats",first = "movement",second = "of") == ['the', 'the']: {e}')
    
    total += 1
    try:
        result = candidate(text = "x y z x y z x y z x y z x y z x y z x y z x y z x y z x y z x y z",first = "y",second = "z") == ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "x y z x y z x y z x y z x y z x y z x y z x y z x y z x y z x y z",first = "y",second = "z") == ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']: {e}')
    
    total += 1
    try:
        result = candidate(text = "consecutive consecutive consecutive words words words in in in the the the sentence sentence sentence",first = "consecutive",second = "consecutive") == ['consecutive', 'words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "consecutive consecutive consecutive words words words in in in the the the sentence sentence sentence",first = "consecutive",second = "consecutive") == ['consecutive', 'words']: {e}')
    
    total += 1
    try:
        result = candidate(text = "this is a test this is only a test in case of an actual emergency this is a test",first = "this",second = "is") == ['a', 'only', 'a']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "this is a test this is only a test in case of an actual emergency this is a test",first = "this",second = "is") == ['a', 'only', 'a']: {e}')
    
    total += 1
    try:
        result = candidate(text = "to be or not to be that is the question to be or not to be",first = "to",second = "be") == ['or', 'that', 'or']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "to be or not to be that is the question to be or not to be",first = "to",second = "be") == ['or', 'that', 'or']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "hello world hello hello world",first = "hello",second = "world") == ['hello']
    assert candidate(text = "repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat']
    assert candidate(text = "look at the stars look at the moon",first = "look",second = "at") == ['the', 'the']
    assert candidate(text = "in the beginning there was the word",first = "the",second = "beginning") == ['there']
    assert candidate(text = "this is a test this is only a test",first = "this",second = "is") == ['a', 'only']
    assert candidate(text = "one two three two three four three five",first = "two",second = "three") == ['two', 'four']
    assert candidate(text = "every good boy does fine every good boy does fine",first = "good",second = "boy") == ['does', 'does']
    assert candidate(text = "alice is a good girl she is a good student",first = "a",second = "good") == ['girl', 'student']
    assert candidate(text = "we will we will rock you",first = "we",second = "will") == ['we', 'rock']
    assert candidate(text = "foo bar foo bar foo",first = "foo",second = "bar") == ['foo', 'foo']
    assert candidate(text = "in a village of la mancha the name of which i have no desire to call to mind",first = "village",second = "of") == ['la']
    assert candidate(text = "this is a test this is only a test",first = "is",second = "a") == ['test']
    assert candidate(text = "foo bar foo foo bar bar foo",first = "foo",second = "bar") == ['foo', 'bar']
    assert candidate(text = "the quick brown fox jumps over the lazy dog",first = "the",second = "lazy") == ['dog']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog",first = "quick",second = "brown") == ['fox', 'fox']
    assert candidate(text = "a b c a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c', 'c']
    assert candidate(text = "repeat repeat repeat repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat']
    assert candidate(text = "one two three four five six seven eight nine ten eleven twelve",first = "five",second = "six") == ['seven']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox",first = "quick",second = "brown") == ['fox', 'fox']
    assert candidate(text = "a tale of two cities a tale of two brothers a tale of two sisters",first = "tale",second = "of") == ['two', 'two', 'two']
    assert candidate(text = "once upon a time in a land far far away once upon a time in a magical land",first = "once",second = "upon") == ['a', 'a']
    assert candidate(text = "this is a simple test this is a more complex test this is a simple test",first = "is",second = "a") == ['simple', 'more', 'simple']
    assert candidate(text = "the rain in spain stays mainly in the plain the rain in spain",first = "rain",second = "in") == ['spain', 'spain']
    assert candidate(text = "one fish two fish red fish blue fish one fish two fish red fish blue fish",first = "fish",second = "red") == ['fish', 'fish']
    assert candidate(text = "one two three four five six seven eight nine ten one two three four five six",first = "three",second = "four") == ['five', 'five']
    assert candidate(text = "x y z x y z x y z x y z x y z x y z x y z x y z",first = "x",second = "y") == ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
    assert candidate(text = "this is a simple sentence to test the function this is a simple test",first = "simple",second = "sentence") == ['to']
    assert candidate(text = "a a a a a a a a a a a a a a a a a a a a a",first = "a",second = "a") == ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    assert candidate(text = "once upon a time in a land far far away once upon a time",first = "once",second = "upon") == ['a', 'a']
    assert candidate(text = "repeated repeated repeated repeated repeated repeated",first = "repeated",second = "repeated") == ['repeated', 'repeated', 'repeated', 'repeated']
    assert candidate(text = "abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl mno",first = "def",second = "ghi") == ['jkl', 'jkl']
    assert candidate(text = "a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d",first = "a",second = "b") == ['c', 'c']
    assert candidate(text = "this is a simple test case this is a very simple test case",first = "is",second = "a") == ['simple', 'very']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps",first = "quick",second = "brown") == ['fox', 'fox']
    assert candidate(text = "once upon a time in a land far far away once upon a time in a land",first = "once",second = "upon") == ['a', 'a']
    assert candidate(text = "find these occurrences carefully find these occurrences again find these occurrences one more time",first = "find",second = "these") == ['occurrences', 'occurrences', 'occurrences']
    assert candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick and silent movement of the enemy will jeopardize five gunboats",first = "quick",second = "and") == ['silent']
    assert candidate(text = "complex example with multiple matches and no matches complex example with multiple matches and no matches",first = "with",second = "multiple") == ['matches', 'matches']
    assert candidate(text = "she sells sea shells by the sea shore she sells sea shells by the sea shore",first = "sea",second = "shells") == ['by', 'by']
    assert candidate(text = "complex scenario with different words complex scenario with different words complex",first = "with",second = "different") == ['words', 'words']
    assert candidate(text = "repeated repeated repeated words words words in a sentence",first = "words",second = "in") == ['a']
    assert candidate(text = "unique words with no repetitions should return empty list",first = "no",second = "repetitions") == ['should']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the quick brown fox",first = "quick",second = "brown") == ['fox', 'fox', 'fox']
    assert candidate(text = "x y z a b c x y z a b c x y z a b c x y z a b c",first = "x",second = "y") == ['z', 'z', 'z', 'z']
    assert candidate(text = "word word word word word word word word word word word word word word word word word word word word",first = "word",second = "word") == ['word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word']
    assert candidate(text = "edge case where the last word is the second",first = "second",second = "word") == []
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "f",second = "g") == ['h', 'h']
    assert candidate(text = "the cat sat on the mat the dog sat on the log the cat sat on the mat the dog sat on the log",first = "sat",second = "on") == ['the', 'the', 'the', 'the']
    assert candidate(text = "hello there hello there hello there hello there hello there",first = "hello",second = "there") == ['hello', 'hello', 'hello', 'hello']
    assert candidate(text = "one fish two fish red fish blue fish one fish two fish red fish blue fish",first = "two",second = "fish") == ['red', 'red']
    assert candidate(text = "repeat after me repeat after me repeat after me repeat after me",first = "repeat",second = "after") == ['me', 'me', 'me', 'me']
    assert candidate(text = "one two three four five six seven eight nine ten eleven twelve",first = "three",second = "four") == ['five']
    assert candidate(text = "in the heart of the night the old owl hooted and the stars twinkled in the dark",first = "the",second = "old") == ['owl']
    assert candidate(text = "finding the third word after first second finding the third word after first",first = "finding",second = "the") == ['third', 'third']
    assert candidate(text = "abracadabra abracadabra abracadabra abracadabra abracadabra",first = "abracadabra",second = "abracadabra") == ['abracadabra', 'abracadabra', 'abracadabra']
    assert candidate(text = "find the pattern in this text pattern in this text pattern in this text pattern",first = "pattern",second = "in") == ['this', 'this', 'this']
    assert candidate(text = "a longer sentence with a variety of words and phrases to test the function properly",first = "variety",second = "of") == ['words']
    assert candidate(text = "she sells sea shells by the sea shore and the shells she sells are sea shells",first = "sea",second = "shells") == ['by']
    assert candidate(text = "example of a longer sentence where the pattern can be found multiple times example of a longer",first = "example",second = "of") == ['a', 'a']
    assert candidate(text = "multiple words in sequence are repeated multiple times multiple words in sequence",first = "multiple",second = "words") == ['in', 'in']
    assert candidate(text = "abc def ghi jkl mno pqr stu vwx yza abc def ghi jkl mno pqr stu vwx yza",first = "ghi",second = "jkl") == ['mno', 'mno']
    assert candidate(text = "abc abc abc abc abc abc abc abc abc abc",first = "abc",second = "abc") == ['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']
    assert candidate(text = "a quick movement of the enemy will jeopardize five gunboats a quick movement of the army will jeopardize five gunboats",first = "quick",second = "movement") == ['of', 'of']
    assert candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick movement of the enemy will jeopardize five gunboats",first = "quick",second = "movement") == ['of', 'of']
    assert candidate(text = "complex pattern with complex pattern and another complex pattern",first = "complex",second = "pattern") == ['with', 'and']
    assert candidate(text = "a b c a b c a b c a b c a b c",first = "a",second = "b") == ['c', 'c', 'c', 'c', 'c']
    assert candidate(text = "this is a simple test to see if the function works correctly with multiple occurrences of first second third",first = "first",second = "second") == ['third']
    assert candidate(text = "once upon a time in a galaxy far far away once upon a time in a galaxy",first = "once",second = "upon") == ['a', 'a']
    assert candidate(text = "cycling in the mountains mountains are beautiful cycling in the mountains",first = "cycling",second = "in") == ['the', 'the']
    assert candidate(text = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty",first = "one",second = "two") == ['three']
    assert candidate(text = "this is a simple sentence with multiple occurrences of the same word word",first = "the",second = "same") == ['word']
    assert candidate(text = "if you are reading this text then you are doing a great job reading",first = "reading",second = "this") == ['text']
    assert candidate(text = "this is a simple test case with multiple matches this is a simple test",first = "this",second = "is") == ['a', 'a']
    assert candidate(text = "to be or not to be that is the question to be or not to be that is the question",first = "be",second = "or") == ['not', 'not']
    assert candidate(text = "in the heart of the city in the heart of the heart in the heart of the city",first = "heart",second = "of") == ['the', 'the', 'the']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the lazy dog jumps over the quick brown fox",first = "the",second = "lazy") == ['dog', 'dog']
    assert candidate(text = "this is a simple test this is a simple test this is a simple test",first = "is",second = "a") == ['simple', 'simple', 'simple']
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c",first = "a",second = "b") == ['c', 'c']
    assert candidate(text = "last two words do not match first second",first = "first",second = "second") == []
    assert candidate(text = "every good boy does fine every good boy does fine every good boy does fine",first = "good",second = "boy") == ['does', 'does', 'does']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog again",first = "quick",second = "brown") == ['fox', 'fox']
    assert candidate(text = "repeat repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat', 'repeat']
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "x",second = "y") == ['z']
    assert candidate(text = "the quick brown fox jumps over the lazy dog the quick brown fox is quick",first = "quick",second = "brown") == ['fox', 'fox']
    assert candidate(text = "cycling through the words cycling through the words cycling",first = "through",second = "the") == ['words', 'words']
    assert candidate(text = "a b c a b c a b c d e f g h i j k l m n o p q r s t u v w x y z",first = "b",second = "c") == ['a', 'a', 'd']
    assert candidate(text = "she sells sea shells by the sea shore she sells sea shells",first = "sea",second = "shells") == ['by']
    assert candidate(text = "hello world hello world hello world hello world hello world hello world",first = "hello",second = "world") == ['hello', 'hello', 'hello', 'hello', 'hello']
    assert candidate(text = "consecutive consecutive words words words words in this sequence sequence",first = "words",second = "words") == ['words', 'words', 'in']
    assert candidate(text = "complex sentence with multiple occurrences of first second third first second third",first = "first",second = "second") == ['third', 'third']
    assert candidate(text = "every good boy does fine every good boy does fine every good boy does fine",first = "every",second = "good") == ['boy', 'boy', 'boy']
    assert candidate(text = "this is a test this is only a test this is a test this is a test",first = "this",second = "is") == ['a', 'only', 'a', 'a']
    assert candidate(text = "repeat repeat repeat repeat repeat repeat",first = "repeat",second = "repeat") == ['repeat', 'repeat', 'repeat', 'repeat']
    assert candidate(text = "repeated repeated repeated repeated repeated repeated repeated repeated",first = "repeated",second = "repeated") == ['repeated', 'repeated', 'repeated', 'repeated', 'repeated', 'repeated']
    assert candidate(text = "aa bb aa bb aa bb aa bb aa bb aa bb",first = "aa",second = "bb") == ['aa', 'aa', 'aa', 'aa', 'aa']
    assert candidate(text = "a quick movement of the enemy will jeopardize six gunboats a quick movement of the enemy will jeopardize six gunboats",first = "movement",second = "of") == ['the', 'the']
    assert candidate(text = "x y z x y z x y z x y z x y z x y z x y z x y z x y z x y z x y z",first = "y",second = "z") == ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    assert candidate(text = "consecutive consecutive consecutive words words words in in in the the the sentence sentence sentence",first = "consecutive",second = "consecutive") == ['consecutive', 'words']
    assert candidate(text = "this is a test this is only a test in case of an actual emergency this is a test",first = "this",second = "is") == ['a', 'only', 'a']
    assert candidate(text = "to be or not to be that is the question to be or not to be",first = "to",second = "be") == ['or', 'that', 'or']


