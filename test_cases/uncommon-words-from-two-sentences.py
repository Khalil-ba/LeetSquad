def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "overlap words here",s2 = "words here") == ['overlap']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap words here",s2 = "words here") == ['overlap']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello world",s2 = "hold the door") == ['hello', 'world', 'hold', 'the', 'door']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello world",s2 = "hold the door") == ['hello', 'world', 'hold', 'the', 'door']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello world",s2 = "hello there") == ['world', 'there']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello world",s2 = "hello there") == ['world', 'there']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "cat dog",s2 = "fish bird") == ['cat', 'dog', 'fish', 'bird']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "cat dog",s2 = "fish bird") == ['cat', 'dog', 'fish', 'bird']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words here",s2 = "some unique there") == ['words', 'here', 'some', 'there']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words here",s2 = "some unique there") == ['words', 'here', 'some', 'there']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words",s2 = "different words") == ['unique', 'different']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words",s2 = "different words") == ['unique', 'different']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "single",s2 = "word") == ['single', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "single",s2 = "word") == ['single', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three",s2 = "four five six") == ['one', 'two', 'three', 'four', 'five', 'six']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three",s2 = "four five six") == ['one', 'two', 'three', 'four', 'five', 'six']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same same",s2 = "same same") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same same",s2 = "same same") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "apple apple",s2 = "banana") == ['banana']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "apple apple",s2 = "banana") == ['banana']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c",s2 = "d e f") == ['a', 'b', 'c', 'd', 'e', 'f']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c",s2 = "d e f") == ['a', 'b', 'c', 'd', 'e', 'f']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "exclusive to s1",s2 = "exclusive to s2") == ['s1', 's2']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "exclusive to s1",s2 = "exclusive to s2") == ['s1', 's2']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello world",s2 = "world is great") == ['hello', 'is', 'great']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello world",s2 = "world is great") == ['hello', 'is', 'great']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c",s2 = "a b d") == ['c', 'd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c",s2 = "a b d") == ['c', 'd']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d",s2 = "d e f g") == ['a', 'b', 'c', 'e', 'f', 'g']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d",s2 = "d e f g") == ['a', 'b', 'c', 'e', 'f', 'g']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three",s2 = "three two one") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three",s2 = "three two one") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "this apple is sweet",s2 = "this apple is sour") == ['sweet', 'sour']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "this apple is sweet",s2 = "this apple is sour") == ['sweet', 'sour']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello from the other side",s2 = "hello from this side") == ['the', 'other', 'this']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello from the other side",s2 = "hello from this side") == ['the', 'other', 'this']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "long sentence with multiple occurrences of words",s2 = "words occurrences sentence") == ['long', 'with', 'multiple', 'of']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "long sentence with multiple occurrences of words",s2 = "words occurrences sentence") == ['long', 'with', 'multiple', 'of']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "shared unique shared",s2 = "unique shared unique") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "shared unique shared",s2 = "unique shared unique") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc def ghi jkl mno pqr stu vwx yz",s2 = "stu vwx yz abc def ghi jkl mno pqr") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc def ghi jkl mno pqr stu vwx yz",s2 = "stu vwx yz abc def ghi jkl mno pqr") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python is great",s2 = "great language python") == ['is', 'language']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python is great",s2 = "great language python") == ['is', 'language']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "alpha beta gamma",s2 = "delta epsilon zeta") == ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "alpha beta gamma",s2 = "delta epsilon zeta") == ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common common words in both",s2 = "common words in both sentences") == ['sentences']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common common words in both",s2 = "common words in both sentences") == ['sentences']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeat repeat repeat repeat",s2 = "single") == ['single']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeat repeat repeat repeat",s2 = "single") == ['single']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello world from python",s2 = "hello world from java") == ['python', 'java']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello world from python",s2 = "hello world from java") == ['python', 'java']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same same same same",s2 = "same") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same same same same",s2 = "same") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "multiple words in a sentence",s2 = "multiple unique words") == ['in', 'a', 'sentence', 'unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "multiple words in a sentence",s2 = "multiple unique words") == ['in', 'a', 'sentence', 'unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "alpha beta gamma delta",s2 = "delta epsilon zeta") == ['alpha', 'beta', 'gamma', 'epsilon', 'zeta']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "alpha beta gamma delta",s2 = "delta epsilon zeta") == ['alpha', 'beta', 'gamma', 'epsilon', 'zeta']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "",s2 = "single word") == ['single', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "",s2 = "single word") == ['single', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated words",s2 = "words words repeated") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated words",s2 = "words words repeated") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated repeated",s2 = "unique word") == ['unique', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated repeated",s2 = "unique word") == ['unique', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words only here",s2 = "completely different set of words") == ['unique', 'only', 'here', 'completely', 'different', 'set', 'of']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words only here",s2 = "completely different set of words") == ['unique', 'only', 'here', 'completely', 'different', 'set', 'of']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three four five six seven eight nine ten eleven twelve",s2 = "twelve eleven ten nine eight seven six five four three two one") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three four five six seven eight nine ten eleven twelve",s2 = "twelve eleven ten nine eight seven six five four three two one") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two one",s2 = "three two three") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two one",s2 = "three two three") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "apple orange banana",s2 = "banana orange grape") == ['apple', 'grape']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "apple orange banana",s2 = "banana orange grape") == ['apple', 'grape']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a quick brown fox jumps over the lazy dog",s2 = "the quick brown dog jumps over a lazy") == ['fox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a quick brown fox jumps over the lazy dog",s2 = "the quick brown dog jumps over a lazy") == ['fox']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common words appear here",s2 = "here common words appear") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common words appear here",s2 = "here common words appear") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common common common",s2 = "uncommon") == ['uncommon']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common common common",s2 = "uncommon") == ['uncommon']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "single",s2 = "different") == ['single', 'different']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "single",s2 = "different") == ['single', 'different']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three four five six seven eight nine ten",s2 = "ten nine eight seven six five four three two one") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three four five six seven eight nine ten",s2 = "ten nine eight seven six five four three two one") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlap this is a test",s2 = "this is another test") == ['overlap', 'a', 'another']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap this is a test",s2 = "this is another test") == ['overlap', 'a', 'another']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longer sentence with many uncommon words",s2 = "many uncommon words longer sentence") == ['with']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longer sentence with many uncommon words",s2 = "many uncommon words longer sentence") == ['with']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common words in both",s2 = "common words in both") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common words in both",s2 = "common words in both") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc def ghi jkl mno pqr stu vwx yza",s2 = "stu vwx yza abc def ghi jkl") == ['mno', 'pqr']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc def ghi jkl mno pqr stu vwx yza",s2 = "stu vwx yza abc def ghi jkl") == ['mno', 'pqr']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python java cplusplus",s2 = "java csharp python") == ['cplusplus', 'csharp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python java cplusplus",s2 = "java csharp python") == ['cplusplus', 'csharp']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same same same",s2 = "different different different") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same same same",s2 = "different different different") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello world hello",s2 = "world world") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello world hello",s2 = "world world") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "test test test",s2 = "unique test") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "test test test",s2 = "unique test") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "distinct words only",s2 = "entirely distinct words") == ['only', 'entirely']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "distinct words only",s2 = "entirely distinct words") == ['only', 'entirely']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "",s2 = "single") == ['single']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "",s2 = "single") == ['single']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated words",s2 = "unique words in second sentence") == ['unique', 'in', 'second', 'sentence']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated words",s2 = "unique words in second sentence") == ['unique', 'in', 'second', 'sentence']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "test test test",s2 = "test test test test") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "test test test",s2 = "test test test test") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "single",s2 = "unique") == ['single', 'unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "single",s2 = "unique") == ['single', 'unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated word",s2 = "word unique") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated word",s2 = "word unique") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique word in first sentence",s2 = "unique word in second sentence") == ['first', 'second']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique word in first sentence",s2 = "unique word in second sentence") == ['first', 'second']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "many many words in this sentence",s2 = "many words") == ['in', 'this', 'sentence']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "many many words in this sentence",s2 = "many words") == ['in', 'this', 'sentence']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words only",s2 = "completely different set") == ['unique', 'words', 'only', 'completely', 'different', 'set']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words only",s2 = "completely different set") == ['unique', 'words', 'only', 'completely', 'different', 'set']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words only",s2 = "different set words") == ['unique', 'only', 'different', 'set']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words only",s2 = "different set words") == ['unique', 'only', 'different', 'set']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "this is a test",s2 = "this is another test") == ['a', 'another']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "this is a test",s2 = "this is another test") == ['a', 'another']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same same same",s2 = "same") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same same same",s2 = "same") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique word in sentence one",s2 = "unique word in sentence two") == ['one', 'two']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique word in sentence one",s2 = "unique word in sentence two") == ['one', 'two']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "multiple words are present",s2 = "multiple words are missing") == ['present', 'missing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "multiple words are present",s2 = "multiple words are missing") == ['present', 'missing']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlap words in both",s2 = "overlap words in both") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap words in both",s2 = "overlap words in both") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longer sentence with more words",s2 = "shorter with") == ['longer', 'sentence', 'more', 'words', 'shorter']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longer sentence with more words",s2 = "shorter with") == ['longer', 'sentence', 'more', 'words', 'shorter']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "identical identical identical",s2 = "identical identical identical") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "identical identical identical",s2 = "identical identical identical") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "this is a test sentence",s2 = "sentence is a this") == ['test']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "this is a test sentence",s2 = "sentence is a this") == ['test']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common common words in both",s2 = "common words") == ['in', 'both']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common common words in both",s2 = "common words") == ['in', 'both']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlapping words in both",s2 = "overlapping words in both") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlapping words in both",s2 = "overlapping words in both") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated words here",s2 = "different words here") == ['different']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated words here",s2 = "different words here") == ['different']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "distinctive words in each sentence",s2 = "each sentence has distinctive words") == ['in', 'has']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "distinctive words in each sentence",s2 = "each sentence has distinctive words") == ['in', 'has']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a a a b b c d e f g h i j k l m n o p q r s t u v w x y z",s2 = "a b c") == ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a a a b b c d e f g h i j k l m n o p q r s t u v w x y z",s2 = "a b c") == ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d e f g h i j",s2 = "k l m n o p q r s t") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d e f g h i j",s2 = "k l m n o p q r s t") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words only here",s2 = "unique words are everywhere") == ['only', 'here', 'are', 'everywhere']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words only here",s2 = "unique words are everywhere") == ['only', 'here', 'are', 'everywhere']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three four five six",s2 = "six five four three two one") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three four five six",s2 = "six five four three two one") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longer sentence with multiple uncommon words here",s2 = "here are some uncommon words") == ['longer', 'sentence', 'with', 'multiple', 'are', 'some']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longer sentence with multiple uncommon words here",s2 = "here are some uncommon words") == ['longer', 'sentence', 'with', 'multiple', 'are', 'some']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "first sentence here",s2 = "second unique sentence") == ['first', 'here', 'second', 'unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "first sentence here",s2 = "second unique sentence") == ['first', 'here', 'second', 'unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same same same same",s2 = "different different") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same same same same",s2 = "different different") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words in each sentence",s2 = "other unique words") == ['in', 'each', 'sentence', 'other']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words in each sentence",s2 = "other unique words") == ['in', 'each', 'sentence', 'other']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common words and unique",s2 = "unique words and common") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common words and unique",s2 = "unique words and common") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "shared words words",s2 = "words shared") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "shared words words",s2 = "words shared") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python java c++",s2 = "java c++ python") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python java c++",s2 = "java c++ python") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlap overlap words",s2 = "words overlap") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap overlap words",s2 = "words overlap") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "some common words here",s2 = "here some unique") == ['common', 'words', 'unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "some common words here",s2 = "here some unique") == ['common', 'words', 'unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique word only",s2 = "entirely different") == ['unique', 'word', 'only', 'entirely', 'different']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique word only",s2 = "entirely different") == ['unique', 'word', 'only', 'entirely', 'different']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "multiple multiple words in first",s2 = "words in second") == ['first', 'second']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "multiple multiple words in first",s2 = "words in second") == ['first', 'second']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated words",s2 = "unique single") == ['words', 'unique', 'single']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated words",s2 = "unique single") == ['words', 'unique', 'single']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three four five",s2 = "six seven eight nine ten") == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three four five",s2 = "six seven eight nine ten") == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "complexity in first",s2 = "complexity in second") == ['first', 'second']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "complexity in first",s2 = "complexity in second") == ['first', 'second']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "",s2 = "") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "",s2 = "") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same same same",s2 = "same same") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same same same",s2 = "same same") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "no overlap",s2 = "no common words") == ['overlap', 'common', 'words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "no overlap",s2 = "no common words") == ['overlap', 'common', 'words']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "shared words shared",s2 = "shared words unique") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "shared words shared",s2 = "shared words unique") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common word common",s2 = "word common unique") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common word common",s2 = "word common unique") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "shared words are common",s2 = "common shared words") == ['are']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "shared words are common",s2 = "common shared words") == ['are']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "singleword",s2 = "singleword") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "singleword",s2 = "singleword") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a a a a a a a a a a",s2 = "b b b b b b b b b b") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a a a a a a a a a a",s2 = "b b b b b b b b b b") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated repeated",s2 = "repeated unique") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated repeated",s2 = "repeated unique") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello world hello",s2 = "world hello universe") == ['universe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello world hello",s2 = "world hello universe") == ['universe']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated word",s2 = "word") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated word",s2 = "word") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common words in both sentences",s2 = "common words in both sentences") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common words in both sentences",s2 = "common words in both sentences") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d e f g h i j",s2 = "j i h g f e d c b a") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d e f g h i j",s2 = "j i h g f e d c b a") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlap overlap here",s2 = "here overlap") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap overlap here",s2 = "here overlap") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "exclusive to first",s2 = "exclusive to second") == ['first', 'second']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "exclusive to first",s2 = "exclusive to second") == ['first', 'second']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "multiple unique words here",s2 = "here multiple") == ['unique', 'words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "multiple unique words here",s2 = "here multiple") == ['unique', 'words']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "one two three four",s2 = "five six seven eight") == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "one two three four",s2 = "five six seven eight") == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "singleword",s2 = "differentword") == ['singleword', 'differentword']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "singleword",s2 = "differentword") == ['singleword', 'differentword']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique words only",s2 = "completely different") == ['unique', 'words', 'only', 'completely', 'different']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique words only",s2 = "completely different") == ['unique', 'words', 'only', 'completely', 'different']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d e",s2 = "f g h i j") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d e",s2 = "f g h i j") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlap words here and there",s2 = "there and words") == ['overlap', 'here']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap words here and there",s2 = "there and words") == ['overlap', 'here']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "single",s2 = "") == ['single']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "single",s2 = "") == ['single']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "apple banana cherry",s2 = "banana cherry date") == ['apple', 'date']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "apple banana cherry",s2 = "banana cherry date") == ['apple', 'date']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d e f g",s2 = "h i j k l m n o p q r s t u v w x y z") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d e f g",s2 = "h i j k l m n o p q r s t u v w x y z") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "",s2 = "singleword") == ['singleword']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "",s2 = "singleword") == ['singleword']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "uncommon word one",s2 = "uncommon word two") == ['one', 'two']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "uncommon word one",s2 = "uncommon word two") == ['one', 'two']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "single",s2 = "single single") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "single",s2 = "single single") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d e f g h i j k l m n o p q r s t u v w x y z",s2 = "a b c") == ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d e f g h i j k l m n o p q r s t u v w x y z",s2 = "a b c") == ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repeated repeated repeated",s2 = "unique") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repeated repeated repeated",s2 = "unique") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a b c d e f g",s2 = "h i j k l m n") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a b c d e f g",s2 = "h i j k l m n") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longer sentence with more words included",s2 = "included more words with longer sentence") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longer sentence with more words included",s2 = "included more words with longer sentence") == []: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "overlap many words here",s2 = "many words overlap") == ['here']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "overlap many words here",s2 = "many words overlap") == ['here']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "singleword",s2 = "different") == ['singleword', 'different']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "singleword",s2 = "different") == ['singleword', 'different']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "multiple same words here and here",s2 = "here and") == ['multiple', 'same', 'words']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "multiple same words here and here",s2 = "here and") == ['multiple', 'same', 'words']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python programming language",s2 = "programming language for python") == ['for']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python programming language",s2 = "programming language for python") == ['for']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc def ghi jkl mno",s2 = "pqr stu vwx yza") == ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc def ghi jkl mno",s2 = "pqr stu vwx yza") == ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "single",s2 = "single unique") == ['unique']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "single",s2 = "single unique") == ['unique']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "many different words in this sentence",s2 = "completely different words in this sentence") == ['many', 'completely']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "many different words in this sentence",s2 = "completely different words in this sentence") == ['many', 'completely']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "only one word",s2 = "") == ['only', 'one', 'word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "only one word",s2 = "") == ['only', 'one', 'word']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "singleword",s2 = "") == ['singleword']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "singleword",s2 = "") == ['singleword']: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "common words overlap",s2 = "overlap common words") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "common words overlap",s2 = "overlap common words") == []: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "overlap words here",s2 = "words here") == ['overlap']
    assert candidate(s1 = "hello world",s2 = "hold the door") == ['hello', 'world', 'hold', 'the', 'door']
    assert candidate(s1 = "hello world",s2 = "hello there") == ['world', 'there']
    assert candidate(s1 = "cat dog",s2 = "fish bird") == ['cat', 'dog', 'fish', 'bird']
    assert candidate(s1 = "unique words here",s2 = "some unique there") == ['words', 'here', 'some', 'there']
    assert candidate(s1 = "unique words",s2 = "different words") == ['unique', 'different']
    assert candidate(s1 = "single",s2 = "word") == ['single', 'word']
    assert candidate(s1 = "one two three",s2 = "four five six") == ['one', 'two', 'three', 'four', 'five', 'six']
    assert candidate(s1 = "same same",s2 = "same same") == []
    assert candidate(s1 = "apple apple",s2 = "banana") == ['banana']
    assert candidate(s1 = "a b c",s2 = "d e f") == ['a', 'b', 'c', 'd', 'e', 'f']
    assert candidate(s1 = "exclusive to s1",s2 = "exclusive to s2") == ['s1', 's2']
    assert candidate(s1 = "hello world",s2 = "world is great") == ['hello', 'is', 'great']
    assert candidate(s1 = "a b c",s2 = "a b d") == ['c', 'd']
    assert candidate(s1 = "a b c d",s2 = "d e f g") == ['a', 'b', 'c', 'e', 'f', 'g']
    assert candidate(s1 = "one two three",s2 = "three two one") == []
    assert candidate(s1 = "this apple is sweet",s2 = "this apple is sour") == ['sweet', 'sour']
    assert candidate(s1 = "hello from the other side",s2 = "hello from this side") == ['the', 'other', 'this']
    assert candidate(s1 = "long sentence with multiple occurrences of words",s2 = "words occurrences sentence") == ['long', 'with', 'multiple', 'of']
    assert candidate(s1 = "shared unique shared",s2 = "unique shared unique") == []
    assert candidate(s1 = "abc def ghi jkl mno pqr stu vwx yz",s2 = "stu vwx yz abc def ghi jkl mno pqr") == []
    assert candidate(s1 = "python is great",s2 = "great language python") == ['is', 'language']
    assert candidate(s1 = "alpha beta gamma",s2 = "delta epsilon zeta") == ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']
    assert candidate(s1 = "common common words in both",s2 = "common words in both sentences") == ['sentences']
    assert candidate(s1 = "repeat repeat repeat repeat",s2 = "single") == ['single']
    assert candidate(s1 = "hello world from python",s2 = "hello world from java") == ['python', 'java']
    assert candidate(s1 = "same same same same",s2 = "same") == []
    assert candidate(s1 = "multiple words in a sentence",s2 = "multiple unique words") == ['in', 'a', 'sentence', 'unique']
    assert candidate(s1 = "alpha beta gamma delta",s2 = "delta epsilon zeta") == ['alpha', 'beta', 'gamma', 'epsilon', 'zeta']
    assert candidate(s1 = "",s2 = "single word") == ['single', 'word']
    assert candidate(s1 = "repeated repeated words",s2 = "words words repeated") == []
    assert candidate(s1 = "repeated repeated repeated",s2 = "unique word") == ['unique', 'word']
    assert candidate(s1 = "unique words only here",s2 = "completely different set of words") == ['unique', 'only', 'here', 'completely', 'different', 'set', 'of']
    assert candidate(s1 = "one two three four five six seven eight nine ten eleven twelve",s2 = "twelve eleven ten nine eight seven six five four three two one") == []
    assert candidate(s1 = "one two one",s2 = "three two three") == []
    assert candidate(s1 = "apple orange banana",s2 = "banana orange grape") == ['apple', 'grape']
    assert candidate(s1 = "a quick brown fox jumps over the lazy dog",s2 = "the quick brown dog jumps over a lazy") == ['fox']
    assert candidate(s1 = "common words appear here",s2 = "here common words appear") == []
    assert candidate(s1 = "common common common",s2 = "uncommon") == ['uncommon']
    assert candidate(s1 = "single",s2 = "different") == ['single', 'different']
    assert candidate(s1 = "one two three four five six seven eight nine ten",s2 = "ten nine eight seven six five four three two one") == []
    assert candidate(s1 = "overlap this is a test",s2 = "this is another test") == ['overlap', 'a', 'another']
    assert candidate(s1 = "longer sentence with many uncommon words",s2 = "many uncommon words longer sentence") == ['with']
    assert candidate(s1 = "common words in both",s2 = "common words in both") == []
    assert candidate(s1 = "abc def ghi jkl mno pqr stu vwx yza",s2 = "stu vwx yza abc def ghi jkl") == ['mno', 'pqr']
    assert candidate(s1 = "python java cplusplus",s2 = "java csharp python") == ['cplusplus', 'csharp']
    assert candidate(s1 = "same same same",s2 = "different different different") == []
    assert candidate(s1 = "hello world hello",s2 = "world world") == []
    assert candidate(s1 = "test test test",s2 = "unique test") == ['unique']
    assert candidate(s1 = "distinct words only",s2 = "entirely distinct words") == ['only', 'entirely']
    assert candidate(s1 = "",s2 = "single") == ['single']
    assert candidate(s1 = "repeated repeated words",s2 = "unique words in second sentence") == ['unique', 'in', 'second', 'sentence']
    assert candidate(s1 = "test test test",s2 = "test test test test") == []
    assert candidate(s1 = "single",s2 = "unique") == ['single', 'unique']
    assert candidate(s1 = "repeated repeated word",s2 = "word unique") == ['unique']
    assert candidate(s1 = "unique word in first sentence",s2 = "unique word in second sentence") == ['first', 'second']
    assert candidate(s1 = "many many words in this sentence",s2 = "many words") == ['in', 'this', 'sentence']
    assert candidate(s1 = "unique words only",s2 = "completely different set") == ['unique', 'words', 'only', 'completely', 'different', 'set']
    assert candidate(s1 = "unique words only",s2 = "different set words") == ['unique', 'only', 'different', 'set']
    assert candidate(s1 = "this is a test",s2 = "this is another test") == ['a', 'another']
    assert candidate(s1 = "same same same",s2 = "same") == []
    assert candidate(s1 = "unique word in sentence one",s2 = "unique word in sentence two") == ['one', 'two']
    assert candidate(s1 = "multiple words are present",s2 = "multiple words are missing") == ['present', 'missing']
    assert candidate(s1 = "overlap words in both",s2 = "overlap words in both") == []
    assert candidate(s1 = "longer sentence with more words",s2 = "shorter with") == ['longer', 'sentence', 'more', 'words', 'shorter']
    assert candidate(s1 = "identical identical identical",s2 = "identical identical identical") == []
    assert candidate(s1 = "this is a test sentence",s2 = "sentence is a this") == ['test']
    assert candidate(s1 = "common common words in both",s2 = "common words") == ['in', 'both']
    assert candidate(s1 = "overlapping words in both",s2 = "overlapping words in both") == []
    assert candidate(s1 = "repeated repeated words here",s2 = "different words here") == ['different']
    assert candidate(s1 = "distinctive words in each sentence",s2 = "each sentence has distinctive words") == ['in', 'has']
    assert candidate(s1 = "a a a b b c d e f g h i j k l m n o p q r s t u v w x y z",s2 = "a b c") == ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    assert candidate(s1 = "a b c d e f g h i j",s2 = "k l m n o p q r s t") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    assert candidate(s1 = "unique words only here",s2 = "unique words are everywhere") == ['only', 'here', 'are', 'everywhere']
    assert candidate(s1 = "one two three four five six",s2 = "six five four three two one") == []
    assert candidate(s1 = "longer sentence with multiple uncommon words here",s2 = "here are some uncommon words") == ['longer', 'sentence', 'with', 'multiple', 'are', 'some']
    assert candidate(s1 = "first sentence here",s2 = "second unique sentence") == ['first', 'here', 'second', 'unique']
    assert candidate(s1 = "same same same same",s2 = "different different") == []
    assert candidate(s1 = "unique words in each sentence",s2 = "other unique words") == ['in', 'each', 'sentence', 'other']
    assert candidate(s1 = "common words and unique",s2 = "unique words and common") == []
    assert candidate(s1 = "shared words words",s2 = "words shared") == []
    assert candidate(s1 = "python java c++",s2 = "java c++ python") == []
    assert candidate(s1 = "overlap overlap words",s2 = "words overlap") == []
    assert candidate(s1 = "some common words here",s2 = "here some unique") == ['common', 'words', 'unique']
    assert candidate(s1 = "unique word only",s2 = "entirely different") == ['unique', 'word', 'only', 'entirely', 'different']
    assert candidate(s1 = "multiple multiple words in first",s2 = "words in second") == ['first', 'second']
    assert candidate(s1 = "repeated repeated words",s2 = "unique single") == ['words', 'unique', 'single']
    assert candidate(s1 = "one two three four five",s2 = "six seven eight nine ten") == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    assert candidate(s1 = "complexity in first",s2 = "complexity in second") == ['first', 'second']
    assert candidate(s1 = "",s2 = "") == []
    assert candidate(s1 = "same same same",s2 = "same same") == []
    assert candidate(s1 = "no overlap",s2 = "no common words") == ['overlap', 'common', 'words']
    assert candidate(s1 = "shared words shared",s2 = "shared words unique") == ['unique']
    assert candidate(s1 = "common word common",s2 = "word common unique") == ['unique']
    assert candidate(s1 = "shared words are common",s2 = "common shared words") == ['are']
    assert candidate(s1 = "singleword",s2 = "singleword") == []
    assert candidate(s1 = "a a a a a a a a a a",s2 = "b b b b b b b b b b") == []
    assert candidate(s1 = "repeated repeated repeated",s2 = "repeated unique") == ['unique']
    assert candidate(s1 = "hello world hello",s2 = "world hello universe") == ['universe']
    assert candidate(s1 = "repeated repeated word",s2 = "word") == []
    assert candidate(s1 = "common words in both sentences",s2 = "common words in both sentences") == []
    assert candidate(s1 = "a b c d e f g h i j",s2 = "j i h g f e d c b a") == []
    assert candidate(s1 = "overlap overlap here",s2 = "here overlap") == []
    assert candidate(s1 = "exclusive to first",s2 = "exclusive to second") == ['first', 'second']
    assert candidate(s1 = "multiple unique words here",s2 = "here multiple") == ['unique', 'words']
    assert candidate(s1 = "one two three four",s2 = "five six seven eight") == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    assert candidate(s1 = "singleword",s2 = "differentword") == ['singleword', 'differentword']
    assert candidate(s1 = "unique words only",s2 = "completely different") == ['unique', 'words', 'only', 'completely', 'different']
    assert candidate(s1 = "a b c d e",s2 = "f g h i j") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    assert candidate(s1 = "overlap words here and there",s2 = "there and words") == ['overlap', 'here']
    assert candidate(s1 = "single",s2 = "") == ['single']
    assert candidate(s1 = "apple banana cherry",s2 = "banana cherry date") == ['apple', 'date']
    assert candidate(s1 = "a b c d e f g",s2 = "h i j k l m n o p q r s t u v w x y z") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    assert candidate(s1 = "",s2 = "singleword") == ['singleword']
    assert candidate(s1 = "uncommon word one",s2 = "uncommon word two") == ['one', 'two']
    assert candidate(s1 = "single",s2 = "single single") == []
    assert candidate(s1 = "a b c d e f g h i j k l m n o p q r s t u v w x y z",s2 = "a b c") == ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    assert candidate(s1 = "repeated repeated repeated",s2 = "unique") == ['unique']
    assert candidate(s1 = "a b c d e f g",s2 = "h i j k l m n") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    assert candidate(s1 = "longer sentence with more words included",s2 = "included more words with longer sentence") == []
    assert candidate(s1 = "overlap many words here",s2 = "many words overlap") == ['here']
    assert candidate(s1 = "singleword",s2 = "different") == ['singleword', 'different']
    assert candidate(s1 = "multiple same words here and here",s2 = "here and") == ['multiple', 'same', 'words']
    assert candidate(s1 = "python programming language",s2 = "programming language for python") == ['for']
    assert candidate(s1 = "abc def ghi jkl mno",s2 = "pqr stu vwx yza") == ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza']
    assert candidate(s1 = "single",s2 = "single unique") == ['unique']
    assert candidate(s1 = "many different words in this sentence",s2 = "completely different words in this sentence") == ['many', 'completely']
    assert candidate(s1 = "only one word",s2 = "") == ['only', 'one', 'word']
    assert candidate(s1 = "singleword",s2 = "") == ['singleword']
    assert candidate(s1 = "common words overlap",s2 = "overlap common words") == []


